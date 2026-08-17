# -*- coding: utf-8 -*-
"""
Erzeugt die deutsche i18n-Master-Datei (questionnaires/i18n/de.json) aus dem
Fragenkatalog plus den kanonischen UI-Texten des Patienten-Frontends.

Die Master-Datei ist die Referenz für alle Übersetzungen: Jede Sprachdatei
muss exakt dieselben Schlüssel enthalten (Prüfung: manage.py check_i18n).
"""
import json
from pathlib import Path

from django.core.management.base import BaseCommand

from questionnaires.catalog import CATALOG

I18N_DIR = Path(__file__).resolve().parents[2] / "i18n"

UI_STRINGS = {
    "header_title": "Verkehrsmedizinischer Fragebogen",
    "header_subtitle": "Bitte beantworten Sie alle Fragen",
    "language_label": "Sprache",
    "loading": "Lade Fragebogen …",
    "not_found_title": "Fragebogen nicht gefunden",
    "to_start": "Zur Startseite",
    "back": "Zurück",
    "next": "Weiter",
    "skip": "Überspringen",
    "submit": "Absenden",
    "sending": "Senden…",
    "question_of": "Frage {current} von {total}",
    "answer_placeholder": "Ihre Antwort…",
    "required_error": "Bitte beantworten Sie diese Frage.",
    "yes": "Ja",
    "no": "Nein",
    "consent_title": "Einwilligung",
    "followup_hint": "Freiwillige Zusatzangabe – hilft bei der ärztlichen Beurteilung.",
    "ess_question": "Wie wahrscheinlich ist es, dass Sie in dieser Situation einnicken würden?",
    "ess_sum": "Bisherige Summe",
    "ess_opt_0": "0 – Würde nie einnicken",
    "ess_opt_1": "1 – Geringe Wahrscheinlichkeit",
    "ess_opt_2": "2 – Mittlere Wahrscheinlichkeit",
    "ess_opt_3": "3 – Hohe Wahrscheinlichkeit",
    "privacy_button": "Datenschutzhinweise anzeigen",
    "privacy_title": "Datenschutzhinweise",
    "privacy_subtitle": "Information zur Verarbeitung Ihrer Daten nach Art. 13 DSGVO",
    "privacy_controller": "Verantwortlicher: Dr. med. Björn Micka, Betriebsmedizin · Notfallmedizin, Christoph-Dassler-Str. 22, 91074 Herzogenaurach",
    "privacy_purpose": "Zweck der Verarbeitung: Ihre Angaben in diesem Fragebogen (einschließlich Gesundheitsdaten) werden ausschließlich zur Vorbereitung und Durchführung Ihrer verkehrsmedizinischen Untersuchung verwendet.",
    "privacy_legal": "Rechtsgrundlage: Ihre Einwilligung (Art. 6 Abs. 1 lit. a, Art. 9 Abs. 2 lit. a DSGVO). Sie können die Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen.",
    "privacy_storage": "Speicherung: Das Ergebnis wird in Ihre Untersuchungsunterlagen übernommen und unterliegt den ärztlichen Aufbewahrungsfristen. Der Online-Zugang über Ihren persönlichen Link erlischt nach Ablauf der Gültigkeit; die Daten dieses Online-Fragebogens werden anschließend routinemäßig gelöscht.",
    "privacy_rights": "Ihre Rechte: Sie haben das Recht auf Auskunft, Berichtigung, Löschung und Einschränkung der Verarbeitung sowie ein Beschwerderecht bei der zuständigen Datenschutz-Aufsichtsbehörde.",
    "privacy_secrecy": "Alle Angaben unterliegen der ärztlichen Schweigepflicht.",
    "success_title": "Vielen Dank!",
    "success_text": "Ihr Fragebogen wurde erfolgreich übermittelt.",
    "success_result": "ESS-Ergebnis",
    "success_doctor_note": "Bitte besprechen Sie das Ergebnis mit Ihrem Arzt. Eine abschließende Bewertung erfolgt durch einen Facharzt.",
    "success_pdf": "PDF-Zusammenfassung herunterladen",
    "success_close": "Sie können dieses Fenster nun schließen.",
    "band_normal": "Normal (0–9)",
    "band_elevated": "Erhöht (10–15)",
    "band_severe": "Ausgeprägt (≥16)",
    "submit_error": "Fehler beim Absenden. Bitte prüfen Sie Ihre Angaben.",
}


class Command(BaseCommand):
    help = "Erzeugt questionnaires/i18n/de.json (Master) aus Katalog + UI-Texten"

    def handle(self, *args, **options):
        sections = {}
        questions = {}
        ess_items = {}

        for section in CATALOG["sections"]:
            sections[section["id"]] = {
                "title": section["title"],
                "subtitle": section.get("subtitle", ""),
            }
            for q in section["questions"]:
                if q["type"] == "ess_matrix":
                    for item in q.get("items", []):
                        ess_items[item["id"]] = item["label"]
                    continue
                entry = {"label": q["label"]}
                if q.get("hint"):
                    entry["hint"] = q["hint"]
                if q.get("error"):
                    entry["error"] = q["error"]
                if q.get("options"):
                    entry["options"] = {o["value"]: o["label"] for o in q["options"]}
                if q.get("followup"):
                    entry["followup"] = q["followup"]["label"]
                questions[q["id"]] = entry

        master = {
            "_meta": {"language": "de", "name": "Deutsch"},
            "ui": UI_STRINGS,
            "sections": sections,
            "questions": questions,
            "ess_items": ess_items,
        }

        I18N_DIR.mkdir(exist_ok=True)
        out = I18N_DIR / "de.json"
        out.write_text(
            json.dumps(master, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
        self.stdout.write(self.style.SUCCESS(
            f"Master geschrieben: {out} "
            f"({len(questions)} Fragen, {len(ess_items)} ESS-Items, "
            f"{len(UI_STRINGS)} UI-Texte)"
        ))
