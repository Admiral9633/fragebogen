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
    # Welle 2: stoffspezifische Gefahrstoff-Empfehlungen (Kapitel 2.1.1)
    "silikogener_staub_2024", "silikogener_staub_2016",
    "asbest_2024", "asbest_2016",
    "hochtemperaturwollen_2024", "hochtemperaturwollen_2016",
    "staubbelastung_2024", "staubbelastung_2016",
    "blei_2024", "blei_2016",
    "bleialkyle_2024", "bleialkyle_2016",
    "pak_2024", "pak_2016",
    "nitroglycerin_2024", "nitroglycerin_2016",
    "cs2_2024", "cs2_2016",
    "kohlenmonoxid_2024", "kohlenmonoxid_2016",
    "benzol_2024", "benzol_2016",
    "quecksilber_alkyl_2024", "quecksilber_anorganisch_2024", "quecksilber_2016",
    "methanol_2024", "methanol_2016",
    "schwefelwasserstoff_2024", "schwefelwasserstoff_2016",
    "phosphor_2024", "phosphor_2016",
    "platin_2024", "platin_2016",
    "ckw_2024", "ckw_2016",
    "chrom6_2024", "chrom6_2016",
    "arsen_2024", "arsen_2016",
    "dmf_2024", "dmf_2016",
    "oae_2024", "oae_2016",
    "isocyanate_2024", "isocyanate_2016",
    "toluol_xylol_2024", "toluol_xylol_2016",
    "cadmium_2024", "cadmium_2016",
    "ana_2024", "ana_2016",
    "fluor_2024", "fluor_2016",
    "vinylchlorid_2024", "vinylchlorid_2016",
    "nickel_2024", "nickel_2016",
    "schweissen_2024", "schweissen_2016",
    "keg_2024", "keg_2016",
    "hartholzstaub_2024", "hartholzstaub_2016",
    "styrol_2024", "styrol_2016",
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
