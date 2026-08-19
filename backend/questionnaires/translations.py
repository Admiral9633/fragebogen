# -*- coding: utf-8 -*-
"""
Laden der Übersetzungsdateien (questionnaires/i18n/<code>.json).

Der Katalog bleibt deutsch (kanonisch, IDs/Values sprachunabhängig);
die Sprachdateien übersetzen ausschließlich die Anzeige-Texte für das
Patienten-Frontend. PDF und Auswertung für die Praxis bleiben deutsch.
"""
import json
import re
from pathlib import Path

I18N_DIR = Path(__file__).resolve().parent / "i18n"
LANG_RE = re.compile(r"^[a-z]{2,3}$")

# {lang: (mtime_ns, daten)} – nur Treffer cachen, damit später hinzukommende
# oder aktualisierte Sprachdateien ohne Server-Neustart wirksam werden
_cache = {}


def available_languages():
    """Sprachcodes aller vorhandenen Sprachdateien (inkl. 'de')."""
    return sorted(p.stem for p in I18N_DIR.glob("*.json") if LANG_RE.match(p.stem))


def load_translation(lang):
    """Sprachdatei laden; None bei unbekanntem/ungültigem Code."""
    if not LANG_RE.match(lang or ""):
        return None
    path = I18N_DIR / f"{lang}.json"
    if not path.exists():
        return None
    mtime = path.stat().st_mtime_ns
    hit = _cache.get(lang)
    if hit is not None and hit[0] == mtime:
        return hit[1]
    data = json.loads(path.read_text(encoding="utf-8"))
    _cache[lang] = (mtime, data)
    return data
