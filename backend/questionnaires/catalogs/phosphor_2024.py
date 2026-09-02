# -*- coding: utf-8 -*-
"""Weißer Phosphor – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Weißer Phosphor« (E WPH, Fassung Januar 2022), S. 756–770."""

SLUG = "phosphor-2024"

CATALOG = {
    "version": 2,
    "title": "Weißer Phosphor (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Weißer Phosphor« (E WPH, Fassung Januar 2022), S. 756–770",
    "sections": [
        # ── 1 ─ Anlass der Vorsorge ────────────────────────────────────────
        {
            "id": "vorsorge",
            "title": "Anlass der Vorsorge",
            "subtitle": "Angaben zu Ihrem Vorsorgetermin",
            "questions": [
                {
                    "id": "vorsorge_art",
                    "type": "choice",
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen "
                             "weißem Phosphor?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur "
                                                      "Vorsorge wegen weißem Phosphor"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert für weißen Phosphor nicht eingehalten "
                            "wird. Angebotsvorsorge: wenn eine Belastung (Exposition) nicht "
                            "ausgeschlossen werden kann.",
                    "required": True,
                    "options": [
                        {"value": "pflicht", "label": "Vom Betrieb verpflichtend veranlasst "
                                                      "(Pflichtvorsorge)"},
                        {"value": "angebot", "label": "Vom Betrieb angeboten (Angebotsvorsorge)"},
                        {"value": "wunsch", "label": "Auf meinen eigenen Wunsch (Wunschvorsorge)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kontakt mit weißem Phosphor",
            "subtitle": "Ihre Arbeit und der mögliche Kontakt mit dem Stoff",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_bereiche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie mit weißem Phosphor "
                             "oder können mit ihm in Kontakt kommen?",
                    "hint": "Mehrfachauswahl möglich. Weißer (gelber) Phosphor ist die "
                            "sehr giftige, selbstentzündliche Form des Phosphors.",
                    "required": True,
                    "options": [
                        {"value": "herstellung", "label": "Herstellung von weißem Phosphor, "
                                                          "Abfüllung oder Reinigung (Ofenhaus)"},
                        {"value": "verbrennung", "label": "Thermische Verbrennung zu "
                                                          "Phosphorpentoxid oder Phosphorsäure"},
                        {"value": "halogenide", "label": "Verarbeitung mit Halogenen zu "
                                                         "Phosphorhalogeniden"},
                        {"value": "reparatur", "label": "Reparatur- oder Reinigungsarbeiten an "
                                                        "phosphorführenden Apparaturen und "
                                                        "Leitungen"},
                        {"value": "kampfmittel", "label": "Kampfmittelbeseitigung (z. B. "
                                                          "phosphorhaltige Brandbomben)"},
                        {"value": "lager_labor", "label": "Nur Lagerung/Transport in dicht "
                                                          "geschlossenen Gebinden, Messwarte, "
                                                          "Labor oder Arzneimittelherstellung"},
                        {"value": "sonstiges", "label": "Andere Tätigkeit mit weißem Phosphor"},
                        {"value": "keine", "label": "Keine davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit schon Zwischenfälle oder Unfälle mit "
                             "Phosphor (z. B. Brand, Verätzung, Verbrennung der Haut) oder "
                             "ungewöhnliche Betriebszustände (z. B. Leckagen, Störungen)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_taetigkeiten",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit weißem Phosphor "
                             "oder eine vergleichbare Belastung mit Gefahrstoffen?",
                    "required": True,
                    "followup": {"id": "frueher_taetigkeiten_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Berufskrankheit anerkannt, oder läuft "
                             "derzeit ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Berufskrankheit bzw. welches Verfahren?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Schutzausrüstung und Hygiene an Ihrem Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Tragen Sie bei Tätigkeiten mit möglichem Phosphor-Kontakt die "
                             "vorgesehene persönliche Schutzausrüstung (z. B. Schutzkleidung, "
                             "Handschuhe, Atemschutz)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "keine_noetig", "label": "Für meine Tätigkeit ist keine "
                                                           "Schutzausrüstung vorgesehen"},
                    ],
                },
                {
                    "id": "hygiene_umsetzung",
                    "type": "choice",
                    "label": "Halten Sie die Hygieneregeln am Arbeitsplatz ein (z. B. nicht "
                             "essen/trinken/rauchen im Arbeitsbereich, Hände waschen, "
                             "Arbeitskleidung wechseln)?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, vollständig"},
                        {"value": "teilweise", "label": "Teilweise"},
                        {"value": "nein", "label": "Nein / es gibt keine solchen Regeln"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt es bei Ihrer Arbeit zu Hautkontakt mit weißem Phosphor "
                             "oder mit phosphorhaltigen Rückständen?",
                    "hint": "Weißer Phosphor verursacht auf der Haut stark schmerzende "
                            "Brandwunden; über solche Wunden kann der Stoff auch in den "
                            "Körper aufgenommen werden.",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die bei Kontakt mit weißem Phosphor wichtig sind",
            "questions": [
                {
                    "id": "zahnschmerzen",
                    "type": "yes_no",
                    "label": "Haben Sie länger anhaltende (chronische) Zahnschmerzen oder "
                             "Schmerzen im Kieferbereich?",
                    "required": True,
                },
                {
                    "id": "mundschleimhaut",
                    "type": "yes_no",
                    "label": "Haben Sie Entzündungen der Mundschleimhaut (z. B. wunde "
                             "Stellen, entzündetes Zahnfleisch)?",
                    "required": True,
                },
                {
                    "id": "bewegungsapparat",
                    "type": "yes_no",
                    "label": "Haben Sie Schmerzen des Bewegungsapparats (Knochen, Gelenke, "
                             "Muskeln)?",
                    "required": True,
                    "followup": {"id": "bewegungsapparat_desc", "type": "text",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "appetit_gewicht",
                    "type": "yes_no",
                    "label": "Haben Sie in letzter Zeit Appetitlosigkeit, ungewollten "
                             "Gewichtsverlust oder auffällige Blässe bemerkt?",
                    "required": True,
                },
                {
                    "id": "schleimhautblutungen",
                    "type": "yes_no",
                    "label": "Neigen Sie zu Blutungen der Haut oder Schleimhäute (z. B. "
                             "häufiges Zahnfleisch- oder Nasenbluten, schnell blaue Flecken)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Zähne und Vorerkrankungen ──────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Zähne & Vorerkrankungen",
            "subtitle": "Zahnzustand und frühere bzw. bestehende Erkrankungen",
            "questions": [
                {
                    "id": "zahnstatus",
                    "type": "choice",
                    "label": "Wie ist der Zustand Ihrer Zähne?",
                    "hint": "Unbehandelte Löcher (Karies) und Entzündungsherde an "
                            "Zahnwurzeln (Zahngranulome) können eine Eintrittspforte für "
                            "Phosphor in den Kieferknochen sein.",
                    "required": True,
                    "options": [
                        {"value": "saniert", "label": "Gesund oder vollständig behandelt "
                                                      "(saniert)"},
                        {"value": "karies", "label": "Ich habe unbehandelte Löcher (Karies), "
                                                     "abgebrochene oder stark beschädigte Zähne"},
                        {"value": "unbekannt", "label": "Weiß ich nicht / lange kein "
                                                        "Zahnarztbesuch"},
                    ],
                },
                {
                    "id": "zahn_granulom",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen ein Zahngranulom festgestellt (eitriger "
                             "Entzündungsherd an einer Zahnwurzel)?",
                    "required": True,
                },
                {
                    "id": "leber_erkrankung",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung der Leber (z. B. "
                             "Hepatitis/Leberentzündung, Fettleber, Leberzirrhose)?",
                    "required": True,
                    "followup": {"id": "leber_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "nieren_erkrankung",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung der Nieren (z. B. "
                             "Nierenentzündung, eingeschränkte Nierenfunktion, Eiweiß im "
                             "Urin)?",
                    "required": True,
                    "followup": {"id": "nieren_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "knochen_erkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Erkrankung der Knochen, "
                             "z. B. Knochenschwund (Osteoporose)?",
                    "required": True,
                    "followup": {"id": "knochen_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "atemwegs_erkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Erkrankung der Atemwege "
                             "oder der Lunge (z. B. Asthma, COPD, chronische Bronchitis)?",
                    "required": True,
                    "followup": {"id": "atemwegs_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "allgemein_einschraenkung",
                    "type": "yes_no",
                    "label": "Haben Sie weitere gesundheitliche Einschränkungen oder "
                             "Erkrankungen, die noch nicht genannt wurden?",
                    "required": True,
                    "followup": {"id": "allgemein_einschraenkung_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Besonderer Schutz ──────────────────────────────────────────
        {
            "id": "besonderer_schutz",
            "title": "Besonderer gesetzlicher Schutz",
            "subtitle": "Für einige Personengruppen gelten Beschäftigungsbeschränkungen",
            "questions": [
                {
                    "id": "schwanger_stillend",
                    "type": "choice",
                    "label": "Sind Sie schwanger, oder stillen Sie zurzeit?",
                    "hint": "Für werdende und stillende Mütter gelten beim Umgang mit "
                            "Gefahrstoffen besondere Schutzvorschriften (Mutterschutzgesetz).",
                    "required": True,
                    "options": [
                        {"value": "schwanger", "label": "Ja, ich bin schwanger"},
                        {"value": "stillend", "label": "Ja, ich stille"},
                        {"value": "nein", "label": "Nein / trifft nicht zu"},
                        {"value": "keine_angabe", "label": "Keine Angabe"},
                    ],
                },
                {
                    "id": "unter_18",
                    "type": "yes_no",
                    "label": "Sind Sie jünger als 18 Jahre?",
                    "hint": "Für Jugendliche gelten beim Umgang mit Gefahrstoffen besondere "
                            "Schutzvorschriften (Jugendarbeitsschutzgesetz).",
                    "required": True,
                },
            ],
        },
        # ── 7 ─ Einwilligung ───────────────────────────────────────────────
        {
            "id": "einwilligung",
            "title": "Bestätigung & Einwilligung",
            "subtitle": "Zum Abschluss",
            "questions": [
                {
                    "id": "consent_truth",
                    "type": "consent",
                    "label": "Ich bestätige, dass meine Angaben vollständig und wahrheitsgemäß sind.",
                    "error": "Bitte bestätigen Sie die Vollständigkeit Ihrer Angaben.",
                    "required": True,
                },
                {
                    "id": "consent_privacy",
                    "type": "consent",
                    "label": "Ich habe die Datenschutzhinweise gelesen und willige in die Verarbeitung "
                             "meiner Daten zu arbeitsmedizinischen Zwecken ein.",
                    "error": "Bitte akzeptieren Sie die Datenschutzhinweise.",
                    "required": True,
                },
            ],
        },
    ],
}

RULES = [
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"leber_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Lebererkrankung in der Vorgeschichte oder aktuell angegeben.",
     "konsequenz": "Leberwerte (ALAT, ASAT, γ-GT) im Rahmen der klinischen Untersuchung "
                   "gezielt bewerten; bei Verdacht auf Leberschädigung weiterführende "
                   "hepatologische Diagnostik veranlassen. Schweregrad klären: bei schwerer "
                   "Leberkrankheit prüfen, ob die Tätigkeit ohne gesundheitliche Gefährdung "
                   "möglich ist – Maßnahmen nach 7.4.2 (z. B. Expositionsminderung, PSA), "
                   "verkürzte Vorsorgefristen nach 7.4.3, bei fehlender Erfolgsaussicht "
                   "Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"nieren_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Niere",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Nierenerkrankung in der Vorgeschichte oder aktuell angegeben.",
     "konsequenz": "Urinstatus (Mehrfachteststreifen) und Kreatinin im Serum gezielt "
                   "bewerten; bei Verdacht auf Nierenschädigung (Proteinurie) "
                   "weiterführende nephrologische Diagnostik veranlassen. Bei schwerer "
                   "Nierenkrankheit prüfen, ob die Tätigkeit ohne Gefährdung möglich ist; "
                   "Maßnahmen nach 7.4.2, verkürzte Fristen nach 7.4.3, ggf. "
                   "Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"knochen_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Knochensystem",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Chronische Erkrankung des Knochensystems (z. B. Osteoporose) angegeben.",
     "konsequenz": "Bei Verdacht auf Osteoporose weiterführende spezialisierte Diagnostik "
                   "veranlassen. Chronische Knochenerkrankungen sind beurteilungsrelevant "
                   "nach 7.4: Maßnahmen nach 7.4.2 prüfen; bei zu erwartender Änderung des "
                   "Schweregrads verkürzte Vorsorgefristen nach 7.4.3 empfehlen."},
    {"wenn": {"atemwegs_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 6.2, 6.3.2 und 7.4",
     "befund": "Chronische Erkrankung der Atmungsorgane angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Aufnahme von weißem Phosphor "
                   "erfolgt hauptsächlich über die Atemwege, Dämpfe und Rauch reizen die "
                   "Atemwege. Prüfen, ob die Tätigkeit ohne Gefährdung möglich ist; "
                   "Maßnahmen nach 7.4.2 (z. B. Einsatz an Arbeitsplätzen mit geringerer "
                   "Exposition, Atemschutz unter Beachtung des Gesundheitszustands) und "
                   "verkürzte Fristen nach 7.4.3 erwägen."},
    # ── Zähne und Kiefer (Abschnitte 6.3.3, 7.1, 7.4) ─────────────────────
    {"wenn": {"zahnstatus": ["karies", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Zähne/Kiefer",
     "quelle": "Abschnitte 6.3.3, 7.1 und 7.4",
     "befund": "Kariöses bzw. nicht saniertes Gebiss oder unklarer Zahnstatus angegeben.",
     "konsequenz": "Zahnstatus ärztlich erheben; zahnärztliche Untersuchung und Sanierung "
                   "veranlassen bzw. dringend empfehlen. Kariöses Gebiss und Zahngranulome "
                   "sind beurteilungsrelevant nach 7.4 (Eintrittspforte für Phosphor in den "
                   "Kieferknochen, Gefahr von Osteomyelitis und Kiefernekrose); bis zur "
                   "Sanierung Maßnahmen nach 7.4.2 und verkürzte Vorsorgefrist nach 7.4.3 "
                   "erwägen."},
    {"wenn": {"zahn_granulom": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zähne/Kiefer",
     "quelle": "Abschnitte 6.3.3 und 7.4",
     "befund": "Zahngranulom (Entzündungsherd an der Zahnwurzel) angegeben.",
     "konsequenz": "Zahnärztliche Behandlung des Granulomherdes veranlassen; Zahngranulome "
                   "bieten eine Eintrittspforte für elementaren Phosphor in den "
                   "Kieferknochen (Gefahr der Kiefernekrose). Beurteilung nach 7.4; bis zur "
                   "Sanierung Expositionsminderung nach 7.4.2 und verkürzte Frist nach "
                   "7.4.3 erwägen."},
    {"wenn": {"zahnschmerzen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zähne/Kiefer",
     "quelle": "Abschnitte 6.3.3 und 7.1 (Beschwerden)",
     "befund": "Chronische Zahn- oder Kieferschmerzen angegeben.",
     "konsequenz": "Zahnärztliche Abklärung veranlassen; an phosphorbedingte Veränderungen "
                   "des Kieferknochens (Osteoporose, Osteomyelitis, Kiefernekrose) denken. "
                   "Befund bei der Beurteilung nach 7.4 berücksichtigen."},
    {"wenn": {"mundschleimhaut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Mundschleimhaut",
     "quelle": "Abschnitt 7.1 (Beschwerden)",
     "befund": "Entzündungen der Mundschleimhaut angegeben.",
     "konsequenz": "Mundschleimhaut ärztlich inspizieren und abklären (mögliche lokale "
                   "Wirkung von weißem Phosphor); ggf. zahnärztliche Mitbeurteilung. "
                   "Hygieneregime und Expositionssituation überprüfen."},
    # ── Zeichen chronischer Einwirkung (Abschnitte 6.3.3, 7.1) ────────────
    {"wenn": {"appetit_gewicht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Chronische Einwirkung",
     "quelle": "Abschnitte 6.3.3 und 7.1 (weitere Vorsorgen)",
     "befund": "Appetitlosigkeit, Gewichtsverlust oder Blässe angegeben.",
     "konsequenz": "Mögliche Zeichen einer chronischen Phosphoreinwirkung: klinische "
                   "Untersuchung nach 7.2.2 durchführen (Urinstatus, BSG/CRP, Hämoglobin, "
                   "Kreatinin, Leberenzyme); bei Verdacht auf Leberschädigung "
                   "weiterführende hepatologische Diagnostik. Expositionssituation mit der "
                   "Gefährdungsbeurteilung abgleichen."},
    {"wenn": {"schleimhautblutungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Chronische Einwirkung",
     "quelle": "Abschnitte 6.3.3 und 7.1 (weitere Vorsorgen)",
     "befund": "Blutungsneigung der Haut oder Schleimhäute angegeben.",
     "konsequenz": "Mögliches Zeichen chronischer Phosphoreinwirkung (Blutungsneigung in "
                   "Haut, Schleimhäuten, Augenhintergrund): klinische Untersuchung nach "
                   "7.2.2 (u. a. Hämoglobin, BSG/CRP) durchführen und internistische "
                   "Abklärung erwägen; Expositionssituation überprüfen."},
    {"wenn": {"bewegungsapparat": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Knochensystem",
     "quelle": "Abschnitte 6.3.3, 7.1 und 7.2.2",
     "befund": "Schmerzen des Bewegungsapparats angegeben.",
     "konsequenz": "Gezielte Anamnese und Untersuchung; bei Verdacht auf Osteoporose "
                   "weiterführende spezialisierte Diagnostik veranlassen (phosphorbedingte "
                   "Osteoporose betrifft insbesondere die Kieferknochen; Anfälligkeit für "
                   "Osteomyelitis beachten)."},
    # ── Arbeitsanamnese und Schutzmaßnahmen ───────────────────────────────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle/Unfälle",
     "quelle": "Abschnitte 7.1 und 8.2; § 6 (4) ArbMedVV",
     "befund": "Zwischenfälle, Unfälle oder ungewöhnliche Betriebszustände mit Phosphor "
               "angegeben.",
     "konsequenz": "Hergang dokumentieren und mit der Gefährdungsbeurteilung abgleichen. "
                   "Ergeben sich Anhaltspunkte, dass die Arbeitsschutzmaßnahmen nicht "
                   "ausreichen, Mitteilung an das Unternehmen und Vorschlag von "
                   "Schutzmaßnahmen (§ 6 (4) ArbMedVV). Bei zurückliegender Vergiftung "
                   "oder Verletzung Folgeschäden abklären (Schädigungen können erst nach "
                   "Monaten oder Jahren auftreten); an BK-Nr. 1109 denken."},
    {"wenn": {"psa_nutzung": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen/PSA",
     "quelle": "Abschnitte 8.1 und 8.2; § 6 (4) ArbMedVV",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Eindringliche Beratung zum Tragen geeigneter PSA (individuelle Aspekte "
                   "aufzeigen) und zur Giftigkeit von weißem Phosphor. Ursachen der "
                   "Nichtbenutzung klären; ergeben sich Anhaltspunkte, dass die "
                   "Schutzmaßnahmen nicht ausreichen, Mitteilung an das Unternehmen und "
                   "Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"hygiene_umsetzung": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 (weitere Vorsorgen) und 8.1",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht oder nur teilweise umgesetzt.",
     "konsequenz": "Beratung zu Hygienemaßnahmen: Vermeiden von Inhalation und Hautkontakt, "
                   "Hygiene am Arbeitsplatz (nicht essen/trinken im Arbeitsbereich), "
                   "regelmäßiger Wechsel der Arbeitskleidung. Umsetzung bei der nächsten "
                   "Vorsorge erneut erfragen."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitte 6.2, 6.3.2 und 8.2",
     "befund": "Hautkontakt mit weißem Phosphor bzw. phosphorhaltigen Rückständen "
               "angegeben.",
     "konsequenz": "Hautkontakt muss vermieden werden (stark schmerzende, schwer heilende "
                   "Brandwunden; Resorption toxischer Mengen über Brandwunden möglich). "
                   "Schutzmaßnahmen und PSA überprüfen, Abgleich mit der "
                   "Gefährdungsbeurteilung (TRGS 401); dem Unternehmen ggf. zusätzliche "
                   "Maßnahmen vorschlagen."},
    # ── Beschäftigungsbeschränkungen ──────────────────────────────────────
    {"wenn": {"schwanger_stillend": ["schwanger", "stillend"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 7.1 (allgemeine Beratung); MuSchG",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben.",
     "konsequenz": "Vor (weiterer) Tätigkeit mit weißem Phosphor Beschäftigungsbeschränkungen "
                   "nach dem Mutterschutzgesetz klären: Über mögliche "
                   "Beschäftigungsverbote beim Umgang mit dem sehr giftigen Gefahrstoff "
                   "informieren, unverzügliche mutterschutzrechtliche "
                   "Gefährdungsbeurteilung durch das Unternehmen anstoßen; bis zur Klärung "
                   "keine Exposition."},
    {"wenn": {"unter_18": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Jugendarbeitsschutz",
     "quelle": "Abschnitt 7.1 (allgemeine Beratung); JArbSchG",
     "befund": "Person ist jünger als 18 Jahre.",
     "konsequenz": "Vor Tätigkeitsaufnahme Beschäftigungsbeschränkungen für Jugendliche "
                   "nach dem Jugendarbeitsschutzgesetz klären (Tätigkeiten mit sehr "
                   "giftigen Gefahrstoffen sind für Jugendliche grundsätzlich beschränkt); "
                   "Klärung mit dem Unternehmen vor Einsatz."},
    # ── Dokumentation und Beratung ────────────────────────────────────────
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 6.5 und 7.1",
     "befund": "Anerkannte Berufskrankheit oder laufendes BK-Verfahren angegeben.",
     "konsequenz": "Vorbefunde und Verfahrensstand dokumentieren und bei der Beurteilung "
                   "berücksichtigen (BK-Nr. 1109 »Erkrankungen durch Phosphor oder seine "
                   "anorganischen Verbindungen«); Erkenntnisse für die "
                   "Gefährdungsbeurteilung nutzen."},
    {"wenn": {"frueher_taetigkeiten": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 6.3.3 und 7.1 (Arbeitsanamnese)",
     "befund": "Frühere Tätigkeiten mit Phosphor-Kontakt oder vergleichbarer Gefährdung "
               "angegeben.",
     "konsequenz": "Frühere Expositionen dokumentieren und bei der Beurteilung "
                   "berücksichtigen; beachten, dass phosphorbedingte Schädigungen erst "
                   "nach Monaten oder Jahren auftreten können. Gezielt nach Zeichen "
                   "chronischer Einwirkung fragen und untersuchen."},
]
