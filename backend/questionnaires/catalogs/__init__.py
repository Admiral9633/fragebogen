# -*- coding: utf-8 -*-
"""
Katalog-Registry: alle verfügbaren Untersuchungs-Fragebögen.

Jeder Eintrag verbindet ein Template-Schema (Format v2, siehe schema.py) mit
seinen Auswertungsregeln. Verkehrsmedizin nutzt ein eigenes Python-Regelwerk
(evaluation.evaluate_answers); die DGUV-Kataloge nutzen datengetriebene Regeln
(RULES-Listen, ausgewertet von evaluation.evaluate_rules).

Ein Katalogmodul in diesem Paket exportiert:
  SLUG     – Template-Slug (eindeutig, z.B. "laerm-2024" / "g20-laerm-2016")
  CATALOG  – Schema-Dict (version/title/basis/sections)
  RULES    – Liste datengetriebener Auswertungsregeln:
             {"wenn": {frage_id: [werte…]},          # alle Bedingungen müssen zutreffen
                                                     # (Multi-Choice: einer der ange-
                                                     #  kreuzten Werte genügt; Werte
                                                     #  sind immer Skalare)
              "schwere": "kritisch"|"pruefen"|"hinweis",
              "bereich": "…", "quelle": "…",          # Kapitel/Abschnitt der Empfehlung
              "befund": "…",
              "konsequenz": "…"}                      # Verfahrensanweisung: was ist zu tun
"""
from importlib import import_module

# Verkehrsmedizin (BASt-Leitlinien) – bespoke-Regelwerk in evaluation.py
from questionnaires.catalog import CATALOG as VERKEHRSMEDIZIN_CATALOG

# DGUV-Katalogmodule (jeweils alte Grundsätze 2016 und neue Empfehlungen 2024)
DGUV_MODULE = [
    "laerm_2024", "laerm_2016",
    "haut_2024", "haut_2016",
    "atemschutz_2024", "atemschutz_2016",
    "hitze_2024", "hitze_2016",
    "kaelte_2024", "kaelte_2016",
    "ausland_2024", "ausland_2016",
    "bildschirm_2024", "bildschirm_2016",
    "absturz_2024", "absturz_2016",
    "infektion_2024", "infektion_2016",
    "muskel_skelett_2024", "muskel_skelett_2016",
]


def _build_registry():
    registry = {
        "verkehrsmedizin-leitlinien": {
            "catalog": VERKEHRSMEDIZIN_CATALOG,
            "rules": None,  # bespoke: evaluation.evaluate_answers
        }
    }
    for name in DGUV_MODULE:
        try:
            mod = import_module(f"questionnaires.catalogs.{name}")
        except ImportError:
            continue  # Katalog (noch) nicht vorhanden
        registry[mod.SLUG] = {"catalog": mod.CATALOG, "rules": mod.RULES}
    return registry


CATALOG_REGISTRY = _build_registry()
