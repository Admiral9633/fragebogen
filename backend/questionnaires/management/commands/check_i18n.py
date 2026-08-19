# -*- coding: utf-8 -*-
"""
Prüft alle Sprachdateien in questionnaires/i18n/ gegen die Master-Datei de.json:
identische Schlüsselmengen (ui, sections, questions inkl. options-Werten,
ess_items) und gültiges JSON. Exit-Code 1 bei Abweichungen.
"""
import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

I18N_DIR = Path(__file__).resolve().parents[2] / "i18n"


def _flatten(d, prefix=""):
    keys = set()
    for k, v in d.items():
        path = f"{prefix}{k}"
        if isinstance(v, dict):
            keys |= _flatten(v, path + ".")
        else:
            keys.add(path)
    return keys


class Command(BaseCommand):
    help = "Vergleicht alle i18n-Sprachdateien mit dem Master (de.json)"

    def handle(self, *args, **options):
        master_path = I18N_DIR / "de.json"
        if not master_path.exists():
            raise CommandError("Master fehlt – zuerst manage.py build_i18n_master ausführen.")
        master = json.loads(master_path.read_text(encoding="utf-8"))
        master_keys = _flatten({k: v for k, v in master.items() if k != "_meta"})

        problems = 0
        files = sorted(p for p in I18N_DIR.glob("*.json") if p.stem != "de")
        for path in files:
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                self.stderr.write(self.style.ERROR(f"{path.name}: ungültiges JSON ({exc})"))
                problems += 1
                continue
            keys = _flatten({k: v for k, v in data.items() if k != "_meta"})
            missing = master_keys - keys
            extra = keys - master_keys
            empty = [k for k in sorted(keys & master_keys) if _lookup(data, k) == ""]
            if missing or extra or empty:
                problems += 1
                if missing:
                    self.stderr.write(self.style.ERROR(
                        f"{path.name}: {len(missing)} fehlende Schlüssel, z.B. "
                        + ", ".join(sorted(missing)[:5])
                    ))
                if extra:
                    self.stderr.write(self.style.WARNING(
                        f"{path.name}: {len(extra)} überzählige Schlüssel, z.B. "
                        + ", ".join(sorted(extra)[:5])
                    ))
                if empty:
                    self.stderr.write(self.style.ERROR(
                        f"{path.name}: {len(empty)} leere Werte, z.B. "
                        + ", ".join(empty[:5])
                    ))

        self.stdout.write(
            f"{len(files)} Sprachdateien geprüft gegen {len(master_keys)} Master-Schlüssel."
        )
        if problems:
            raise CommandError(f"{problems} Datei(en) weichen vom Master ab.")
        self.stdout.write(self.style.SUCCESS("Alle Sprachdateien vollständig."))


def _lookup(data, dotted):
    cur = data
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur
