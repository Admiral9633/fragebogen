r"""
GDT Bridge – Windows Service
=============================
Überwacht einen lokalen GDT-Eingangsordner (aus SAMAS),
sendet Patientendaten per HTTPS an den Django-Server,
und schreibt Ergebnis-GDT-Dateien zurück wenn der Fragebogen
ausgefüllt wurde.

Ablauf
------
1. SAMAS schreibt  → C:\GDT\inbox\<patient>.gdt   (Satz 6310)
2. Dieser Service liest die Datei, parsed GDT-Felder
3. POST /api/gdt/session/  → Django erstellt Session, gibt Token + URL zurück
4. Service schreibt sofort eine "Link-GDT" → C:\GDT\outbox\<patient>.gdt
   (SAMAS zeigt den Link zum Fragebogen an)
5. Service prüft alle N Sekunden per GET /api/gdt/result/<token>/
   ob der Fragebogen abgeschlossen wurde
6. Wenn ja: schreibt finale Ergebnis-GDT → C:\GDT\outbox\<patient>_result.gdt

Installation / Deinstallation
------------------------------
  install.bat   (als Administrator ausführen)
  uninstall.bat (als Administrator ausführen)

Konfiguration
-------------
  config.ini  (liegt im selben Ordner wie diese Datei)
"""

import configparser
import json
import logging
import os
import re
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

import requests
import servicemanager
import win32event
import win32service
import win32serviceutil

# ──────────────────────────────────────────────────────────────────────────────
# Pfad-Konstanten
# ──────────────────────────────────────────────────────────────────────────────
SERVICE_DIR  = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent
CONFIG_FILE  = SERVICE_DIR / "config.ini"
LOG_FILE     = SERVICE_DIR / "bridge.log"
PENDING_FILE = SERVICE_DIR / "pending.json"  # offene Sessions die noch auf Ergebnis warten


# ──────────────────────────────────────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────────────────────────────────────
logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("gdt_bridge")


# ──────────────────────────────────────────────────────────────────────────────
# Konfiguration laden
# ──────────────────────────────────────────────────────────────────────────────
def load_config() -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.read(str(CONFIG_FILE), encoding="utf-8")
    return cfg


# ──────────────────────────────────────────────────────────────────────────────
# GDT-Parser  (GDT 2.1, Windows-1252)
# ──────────────────────────────────────────────────────────────────────────────
def parse_gdt(path: Path) -> dict:
    """
    Liest eine GDT-Datei (Satz 6310 – Anforderung) und gibt ein dict zurück.
    Zeilenformat:  LLLFFFFFWert  (LLL = 3-stellige Länge, FFFFF = 5-stellige Feldkennung)
    """
    fields: dict[str, list[str]] = {}
    try:
        with open(path, encoding="cp1252", errors="replace") as fh:
            for raw in fh:
                line = raw.rstrip("\r\n")
                if len(line) < 8:
                    continue
                # Zeilenlänge (3 Zeichen) + Feldkennung (4 oder 5 Zeichen)
                # GDT 2.1 verwendet 4-stellige Feldkennungen
                field_id = line[3:7]
                value    = line[7:]
                fields.setdefault(field_id, []).append(value)
    except Exception as exc:
        log.error("GDT parse error %s: %s", path, exc)
        raise

    def first(fid: str) -> str:
        return (fields.get(fid) or [""])[0].strip()

    # Geburtsdatum DDMMYYYY → YYYY-MM-DD
    birth_date_raw = first("3103")
    birth_date_iso = ""
    if len(birth_date_raw) == 8 and birth_date_raw.isdigit():
        birth_date_iso = f"{birth_date_raw[4:8]}-{birth_date_raw[2:4]}-{birth_date_raw[0:2]}"

    return {
        "gdt_patient_id":     first("3000"),
        "patient_last_name":  first("3102"),
        "patient_first_name": first("3101"),
        "patient_birth_date": birth_date_iso,
        "gdt_request_id":     first("8315"),
        "record_type":        first("8000"),  # 6310 = Anforderung
    }


# ──────────────────────────────────────────────────────────────────────────────
# GDT-Writer  (Ergebnis zurück an SAMAS)
# ──────────────────────────────────────────────────────────────────────────────
def _gdt_line(field_id: str, value: str) -> str:
    """Erzeugt eine korrekte GDT-Zeile mit Längenangabe."""
    # Länge = 3 (Längenfeld) + 4 (Feldkennung) + len(value) + 2 (CRLF)
    content = f"{field_id}{value}"
    length  = 3 + len(content) + 2
    return f"{length:03d}{content}\r\n"


def write_link_gdt(path: Path, patient: dict, questionnaire_url: str) -> None:
    """
    Schreibt sofortige Antwort an SAMAS: Fragebogen-Link als GDT-Satz 6311.
    SAMAS zeigt diesen Befundtext in der Patientenakte an.
    """
    today = datetime.now().strftime("%d%m%Y")
    now   = datetime.now().strftime("%H%M%S")

    lines = [
        _gdt_line("8000", "6311"),          # Satzidentifikation: Ergebnis
        _gdt_line("8100", "Fragebogen"),    # Gerätename (muss in SAMAS konfiguriert sein)
        _gdt_line("8315", patient.get("gdt_request_id", "")),
        _gdt_line("3000", patient.get("gdt_patient_id", "")),
        _gdt_line("3101", patient.get("patient_first_name", "")),
        _gdt_line("3102", patient.get("patient_last_name", "")),
    ]
    if patient.get("patient_birth_date"):
        # Zurück zu DDMMYYYY
        bd = patient["patient_birth_date"]   # YYYY-MM-DD
        if len(bd) == 10:
            lines.append(_gdt_line("3103", f"{bd[8:10]}{bd[5:7]}{bd[0:4]}"))

    lines += [
        _gdt_line("6200", today),           # Untersuchungsdatum
        _gdt_line("6201", now),             # Uhrzeit
        _gdt_line("6220", "Fragebogen-Link wurde erstellt."),
        _gdt_line("6221", questionnaire_url),
        _gdt_line("6222", "Bitte senden Sie dem Patienten diesen Link."),
        _gdt_line("8001", "6311"),          # Satzende
    ]

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="cp1252", errors="replace") as fh:
        fh.writelines(lines)
    log.info("Link-GDT geschrieben: %s", path)


def write_result_gdt(path: Path, patient: dict, result: dict) -> None:
    """
    Schreibt finales Ergebnis an SAMAS wenn Fragebogen ausgefüllt wurde.
    Enthält ESS-Score und Befundtext.
    """
    ess_total     = result.get("ess_total", "?")
    ess_band_text = result.get("ess_band_text", "")
    completed_at  = result.get("completed_at", "")

    # Datum zurück in DDMMYYYY für GDT
    exam_date = ""
    if completed_at and len(completed_at) == 10:
        exam_date = f"{completed_at[0:2]}{completed_at[3:5]}{completed_at[6:10]}"

    lines = [
        _gdt_line("8000", "6311"),
        _gdt_line("8100", "Fragebogen"),
        _gdt_line("8315", patient.get("gdt_request_id", "")),
        _gdt_line("3000", patient.get("gdt_patient_id", "")),
        _gdt_line("3101", patient.get("patient_first_name", "")),
        _gdt_line("3102", patient.get("patient_last_name", "")),
    ]
    if patient.get("patient_birth_date"):
        bd = patient["patient_birth_date"]
        if len(bd) == 10:
            lines.append(_gdt_line("3103", f"{bd[8:10]}{bd[5:7]}{bd[0:4]}"))

    lines += [
        _gdt_line("6200", exam_date if exam_date else datetime.now().strftime("%d%m%Y")),
        _gdt_line("6201", datetime.now().strftime("%H%M%S")),
        _gdt_line("6220", "Verkehrsmedizinischer Fragebogen ausgefüllt"),
        _gdt_line("6221", f"Ausgefüllt am: {completed_at}"),
        _gdt_line("6222", f"ESS-Gesamtscore: {ess_total}/24"),
        _gdt_line("6223", f"Befund: {ess_band_text}"),
        _gdt_line("8001", "6311"),
    ]

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="cp1252", errors="replace") as fh:
        fh.writelines(lines)
    log.info("Ergebnis-GDT geschrieben: %s", path)


# ──────────────────────────────────────────────────────────────────────────────
# Pending-Sessions (warten auf Fragebogen-Abschluss)
# ──────────────────────────────────────────────────────────────────────────────
def load_pending() -> list[dict]:
    if PENDING_FILE.exists():
        try:
            return json.loads(PENDING_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return []


def save_pending(pending: list[dict]) -> None:
    PENDING_FILE.write_text(
        json.dumps(pending, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


# ──────────────────────────────────────────────────────────────────────────────
# Kern-Logik des Bridge
# ──────────────────────────────────────────────────────────────────────────────
class GdtBridge:
    def __init__(self, cfg: configparser.ConfigParser):
        s = cfg["bridge"]
        self.inbox        = Path(s["gdt_inbox"])
        self.outbox       = Path(s["gdt_outbox"])
        self.processed    = self.inbox / "processed"
        self.api_url      = s["api_url"].rstrip("/")
        self.api_key      = s["api_key"]
        self.template_slug = s.get("template_slug", "")
        self.poll_inbox_secs  = int(s.get("poll_inbox_seconds",  "5"))
        self.poll_result_secs = int(s.get("poll_result_seconds", "30"))
        self.session          = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type":  "application/json",
        })
        self.processed.mkdir(parents=True, exist_ok=True)
        self.outbox.mkdir(parents=True, exist_ok=True)

    # ── Eingang verarbeiten ────────────────────────────────────────────────
    def process_inbox(self) -> None:
        for gdt_file in sorted(self.inbox.glob("*.gdt")):
            log.info("Neue GDT-Datei gefunden: %s", gdt_file.name)
            try:
                patient = parse_gdt(gdt_file)
                log.info(
                    "Patient: %s %s, GDT-ID: %s",
                    patient["patient_first_name"],
                    patient["patient_last_name"],
                    patient["gdt_patient_id"],
                )

                # Session beim Django-Server anlegen
                payload = {
                    "patient_last_name":  patient["patient_last_name"],
                    "patient_first_name": patient["patient_first_name"],
                    "patient_birth_date": patient["patient_birth_date"],
                    "gdt_patient_id":     patient["gdt_patient_id"],
                    "gdt_request_id":     patient["gdt_request_id"],
                }
                if self.template_slug:
                    payload["template_slug"] = self.template_slug

                resp = self.session.post(
                    f"{self.api_url}/gdt/session/",
                    json=payload,
                    timeout=15,
                )
                resp.raise_for_status()
                data = resp.json()
                token = data["token"]
                url   = data["url"]
                log.info("Session erstellt: token=%s  url=%s", token, url)

                # Sofort Link-GDT für SAMAS schreiben
                out_name = gdt_file.stem + ".gdt"
                write_link_gdt(self.outbox / out_name, patient, url)

                # In pending-Liste eintragen (auf Ergebnis warten)
                pending = load_pending()
                pending.append({
                    "token":         token,
                    "patient":       patient,
                    "out_stem":      gdt_file.stem,
                    "created_at":    datetime.now().isoformat(),
                })
                save_pending(pending)

                # Datei verschieben
                gdt_file.rename(self.processed / gdt_file.name)

            except requests.HTTPError as exc:
                log.error("HTTP-Fehler beim Erstellen der Session: %s – %s", exc, exc.response.text if exc.response else "")
            except Exception as exc:
                log.error("Fehler bei %s: %s", gdt_file.name, exc)

    # ── Pending-Sessions auf Ergebnis prüfen ──────────────────────────────
    def check_pending(self) -> None:
        pending = load_pending()
        if not pending:
            return

        still_pending = []
        for entry in pending:
            token   = entry["token"]
            patient = entry["patient"]
            try:
                resp = self.session.get(
                    f"{self.api_url}/gdt/result/{token}/",
                    timeout=10,
                )
                if resp.status_code == 202:
                    # Noch nicht abgeschlossen
                    still_pending.append(entry)
                    continue

                resp.raise_for_status()
                result = resp.json()

                if result.get("completed"):
                    out_path = self.outbox / f"{entry['out_stem']}_result.gdt"
                    write_result_gdt(out_path, patient, result)
                    log.info("Ergebnis erhalten und GDT geschrieben für token=%s", token)
                    # Nicht mehr in pending aufnehmen → fertig
                else:
                    still_pending.append(entry)

            except requests.HTTPError as exc:
                log.error("HTTP-Fehler beim Abfragen von %s: %s", token, exc)
                still_pending.append(entry)
            except Exception as exc:
                log.error("Fehler beim Abfragen von %s: %s", token, exc)
                still_pending.append(entry)

        save_pending(still_pending)

    # ── Haupt-Loop (läuft im Service-Thread) ──────────────────────────────
    def run(self, stop_event: threading.Event) -> None:
        log.info("GDT Bridge gestartet. Inbox: %s", self.inbox)
        inbox_counter  = 0
        result_counter = 0

        while not stop_event.is_set():
            try:
                inbox_counter += 1
                if inbox_counter >= self.poll_inbox_secs:
                    self.process_inbox()
                    inbox_counter = 0

                result_counter += 1
                if result_counter >= self.poll_result_secs:
                    self.check_pending()
                    result_counter = 0

            except Exception as exc:
                log.error("Unerwarteter Fehler im Hauptloop: %s", exc)

            stop_event.wait(1)   # 1 Sekunde warten, dabei auf Stop reagieren

        log.info("GDT Bridge gestoppt.")


# ──────────────────────────────────────────────────────────────────────────────
# Windows Service
# ──────────────────────────────────────────────────────────────────────────────
class GdtBridgeService(win32serviceutil.ServiceFramework):
    _svc_name_        = "GdtBridgeService"
    _svc_display_name_ = "GDT Bridge – Fragebogen SAMAS Schnittstelle"
    _svc_description_  = (
        "Überwacht den GDT-Eingangsordner von SAMAS, erstellt Fragebogen-Sessions "
        "auf dem Django-Server und schreibt Ergebnis-GDT-Dateien zurück."
    )

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self._stop_event = win32event.CreateEvent(None, 0, 0, None)
        self._thread_stop = threading.Event()

    def SvcStop(self):
        log.info("Service wird gestoppt …")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self._stop_event)
        self._thread_stop.set()

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ""),
        )
        log.info("Service gestartet (PID %s)", os.getpid())

        try:
            cfg    = load_config()
            bridge = GdtBridge(cfg)
        except Exception as exc:
            log.critical("Fehler beim Laden der Konfiguration: %s", exc)
            servicemanager.LogErrorMsg(f"GDT Bridge Konfigurationsfehler: {exc}")
            return

        worker = threading.Thread(
            target=bridge.run,
            args=(self._thread_stop,),
            daemon=True,
        )
        worker.start()

        # Warten bis Stop-Signal kommt
        win32event.WaitForSingleObject(self._stop_event, win32event.INFINITE)
        worker.join(timeout=10)
        log.info("Service beendet.")


# ──────────────────────────────────────────────────────────────────────────────
# Konsolenmodus zum Testen (ohne Windows Service)
# ──────────────────────────────────────────────────────────────────────────────
def run_console():
    """Startet den Bridge direkt in der Konsole (Strg+C zum Stoppen)."""
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    log.info("Konsolenmodus – zum Beenden Strg+C drücken")
    try:
        cfg    = load_config()
        bridge = GdtBridge(cfg)
        stop   = threading.Event()
        try:
            bridge.run(stop)
        except KeyboardInterrupt:
            stop.set()
            log.info("Gestoppt.")
    except Exception as exc:
        log.critical("Fehler: %s", exc)
        sys.exit(1)


# ──────────────────────────────────────────────────────────────────────────────
# Einstiegspunkt
# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Kein Argument: als Windows Service starten (von SCM aufgerufen)
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(GdtBridgeService)
        servicemanager.StartServiceCtrlDispatcher()
    elif sys.argv[1] == "console":
        # python gdt_bridge_service.py console
        run_console()
    else:
        # install / remove / start / stop / restart / debug
        win32serviceutil.HandleCommandLine(GdtBridgeService)
