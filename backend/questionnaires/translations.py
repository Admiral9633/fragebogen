# -*- coding: utf-8 -*-
"""
Laden der Übersetzungsdateien (questionnaires/i18n/<code>.json).

Der Katalog bleibt deutsch (kanonisch, IDs/Values sprachunabhängig);
die Sprachdateien übersetzen ausschließlich die Anzeige-Texte für das
Patienten-Frontend. PDF und Auswertung für die Praxis bleiben deutsch.
"""
import json
import re
from functools import lru_cache
from pathlib import Path

I18N_DIR = Path(__file__).resolve().parent / "i18n"
LANG_RE = re.compile(r"^[a-z]{2,3}$")


def available_languages():
    """Sprachcodes aller vorhandenen Sprachdateien (inkl. 'de')."""
    return sorted(p.stem for p in I18N_DIR.glob("*.json") if LANG_RE.match(p.stem))


@lru_cache(maxsize=64)
def load_translation(lang):
    """Sprachdatei laden; None bei unbekanntem/ungültigem Code."""
    if not LANG_RE.match(lang or ""):
        return None
    path = I18N_DIR / f"{lang}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
