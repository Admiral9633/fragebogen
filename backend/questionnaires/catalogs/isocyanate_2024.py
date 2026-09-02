# -*- coding: utf-8 -*-
"""Isocyanate – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Isocyanate« (E ISO, Fassung Januar 2022, Grenzwerte aktualisiert 2024),
S. 321–351."""

SLUG = "isocyanate-2024"

CATALOG = {
    "version": 2,
    "title": "Isocyanate (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Isocyanate« (E ISO, Fassung Januar 2022, "
             "Grenzwerte aktualisiert 2024), S. 321–351",
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
                             "Isocyanaten?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Isocyanat-Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur "
                                                      "Isocyanat-Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn "
                            "regelmäßiger Hautkontakt mit Isocyanaten nicht ausgeschlossen "
                            "werden kann oder in der Luft mehr als 0,05 mg/m³ Isocyanat "
                            "vorkommen. Angebotsvorsorge: wenn Hautkontakt nicht "
                            "ausgeschlossen ist oder die Luftkonzentration eingehalten wird.",
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
            "title": "Tätigkeit & Umgang mit Isocyanaten",
            "subtitle": "Ihre Arbeit mit Isocyanaten (z. B. in PU-/PUR-Schäumen, "
                        "Lacken, Klebstoffen, Gießharzen)",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_bereiche",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten haben Sie mit Isocyanaten oder "
                             "Polyurethan-Produkten (PU/PUR) zu tun?",
                    "hint": "Mehrfachauswahl möglich. Isocyanate stecken z. B. in "
                            "2-Komponenten-Lacken, Montageschaum, Klebstoffen, "
                            "Gießharzen und Dichtmassen.",
                    "required": True,
                    "options": [
                        {"value": "pur_schaeume", "label": "Herstellung von PUR-Schäumen "
                                                           "(z. B. Dämmplatten, Weich-/Hartschaum, "
                                                           "Formteile)"},
                        {"value": "spritzen", "label": "Beschichten/Lackieren durch Spritzen "
                                                       "(auch Sportplätze, Behälter, Spritzkabine)"},
                        {"value": "rollen_streichen", "label": "Beschichten durch Rollen, Spachteln "
                                                               "oder Streichen; Dichten und Kleben"},
                        {"value": "kleber_harze", "label": "Verarbeiten von isocyanathaltigen "
                                                           "Klebstoffen, Gießharzen, Bindern oder "
                                                           "Haftvermittlern"},
                        {"value": "montageschaum", "label": "Regelmäßiges Ausschäumen mit "
                                                            "Montageschaum"},
                        {"value": "giesserei", "label": "Gießerei-Arbeiten mit isocyanathaltigen "
                                                        "Bindersystemen (Cold-Box-Kerne)"},
                        {"value": "thermolyse", "label": "Schweißen, Löten oder starkes Erhitzen an "
                                                         "polyurethanhaltigem Material (Isolierungen, "
                                                         "Beschichtungen)"},
                        {"value": "umfuellen", "label": "Abwiegen oder manuelles Umfüllen von "
                                                        "Isocyanaten (Staub- oder Dampfentwicklung)"},
                        {"value": "wartung", "label": "Wartung, Reparatur, Reinigung, Probenahme "
                                                      "oder Umgang mit Isocyanat-Resten"},
                        {"value": "bystander", "label": "Ich arbeite in der Nähe solcher "
                                                        "Arbeitsplätze, ohne selbst damit umzugehen"},
                        {"value": "geschlossen", "label": "Nur geschlossene Anlagen, Messwarte, "
                                                          "Labor oder fertig ausgehärtete Produkte"},
                        {"value": "sonstiges", "label": "Andere Tätigkeit mit Isocyanaten"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "choice",
                    "label": "Kommt Ihre Haut bei der Arbeit mit flüssigen Isocyanaten oder "
                             "nicht ausgehärteten Produkten (z. B. frischem Schaum, Lack, "
                             "Kleber) in Berührung?",
                    "hint": "Auch Hautkontakt kann eine Allergie der Atemwege auslösen – "
                            "schon ein einmaliger großflächiger Kontakt kann ausreichen.",
                    "required": True,
                    "options": [
                        {"value": "regelmaessig", "label": "Ja, regelmäßig"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "nein", "label": "Nein, praktisch nie"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "zwischenfall",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle oder ungewöhnliche "
                             "Betriebszustände mit Isocyanaten (z. B. Verschütten, defekte "
                             "Absaugung, starke Dampf- oder Rauchentwicklung)?",
                    "required": True,
                    "followup": {"id": "zwischenfall_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten mit Isocyanaten oder anderen "
                             "Gefahrstoffen (z. B. Lösungsmitteln, Stäuben) zu tun?",
                    "required": True,
                    "followup": {"id": "frueher_expo_desc", "type": "textarea",
                                 "label": "Welche Stoffe/Tätigkeiten, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "psa",
                    "type": "multi_choice",
                    "label": "Welche Schutzausrüstung benutzen Sie beim Umgang mit "
                             "Isocyanaten?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "atemschutz", "label": "Atemschutz (Maske, Gebläsehaube)"},
                        {"value": "handschuhe", "label": "Geeignete Schutzhandschuhe"},
                        {"value": "brille", "label": "Schutzbrille / Gesichtsschutz"},
                        {"value": "schutzkleidung", "label": "Schutzkleidung / Schutzanzug"},
                        {"value": "keine", "label": "Keine Schutzausrüstung"},
                        {"value": "nicht_noetig", "label": "Bei meiner Tätigkeit ist keine "
                                                           "Schutzausrüstung erforderlich"},
                    ],
                },
                {
                    "id": "kleidung_kontaminiert",
                    "type": "yes_no",
                    "label": "Kommt es vor, dass Ihre Arbeitskleidung mit Isocyanaten "
                             "verschmutzt wird und Sie sie dann weitertragen?",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden an Augen, Atemwegen und Haut",
            "questions": [
                {
                    "id": "reiz_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie bei oder nach der Arbeit Reizbeschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "augen", "label": "Brennende oder tränende Augen"},
                        {"value": "nase", "label": "Laufende oder verstopfte Nase, Niesreiz"},
                        {"value": "hals", "label": "Kratzen im Hals, Heiserkeit, belegte Stimme"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "atem_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere der folgenden Atembeschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Husten oder Hustenreiz"},
                        {"value": "auswurf", "label": "Vermehrter Auswurf (Schleim beim Husten)"},
                        {"value": "kurzatmigkeit", "label": "Kurzatmigkeit bei Belastung"},
                        {"value": "pfeifen", "label": "Pfeifende oder verstärkte Atemgeräusche"},
                        {"value": "anfall", "label": "Anfallsartige Atemnot oder Asthmaanfälle"},
                        {"value": "brustenge", "label": "Engegefühl oder Schmerzen in der Brust"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "naechtlich",
                    "type": "yes_no",
                    "label": "Wachen Sie nachts mit Husten oder Atemnot auf?",
                    "required": True,
                },
                {
                    "id": "arbeitsbezug",
                    "type": "choice",
                    "label": "Falls Sie solche Beschwerden haben: Wie hängen sie mit der "
                             "Arbeit zusammen?",
                    "required": True,
                    "options": [
                        {"value": "bei_arbeit", "label": "Sie treten während der Arbeit auf oder "
                                                         "werden dort schlimmer"},
                        {"value": "verzoegert", "label": "Sie treten erst Stunden nach der Arbeit "
                                                         "oder abends/nachts auf"},
                        {"value": "besser_frei", "label": "Am Wochenende oder im Urlaub werden sie "
                                                          "deutlich besser"},
                        {"value": "kein_bezug", "label": "Kein Zusammenhang mit der Arbeit erkennbar"},
                        {"value": "keine_beschwerden", "label": "Ich habe keine solchen Beschwerden"},
                    ],
                },
                {
                    "id": "grippe_gefuehl",
                    "type": "yes_no",
                    "label": "Bekommen Sie einige Stunden nach der Arbeit manchmal Fieber, "
                             "Schüttelfrost oder Gliederschmerzen wie bei einer Grippe?",
                    "hint": "Das kann ein Hinweis auf eine allergische Entzündung der "
                            "Lungenbläschen (Alveolitis) sein.",
                    "required": True,
                },
                {
                    "id": "haut_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie Hautveränderungen, besonders an Händen oder "
                             "Unterarmen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "roetung", "label": "Rötung, Juckreiz oder trockene, rissige Haut"},
                        {"value": "quaddeln", "label": "Quaddeln / Nesselsucht (Urtikaria)"},
                        {"value": "ekzem", "label": "Ekzem (entzündeter, ggf. nässender Ausschlag)"},
                        {"value": "verfaerbung", "label": "Bräunliche Verfärbungen nach Kontakt mit "
                                                          "dem Produkt"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Allergien",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "atemwegserkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Erkrankungen der Atemwege "
                             "oder der Lunge festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "copd", "label": "COPD oder chronische Bronchitis"},
                        {"value": "emphysem", "label": "Lungenemphysem (überblähte Lunge)"},
                        {"value": "tuberkulose", "label": "Tuberkulose"},
                        {"value": "pneumokoniose", "label": "Staublunge (Pneumokoniose)"},
                        {"value": "andere_lunge", "label": "Andere Lungenerkrankung mit "
                                                           "eingeschränkter Lungenfunktion"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "hyperreagibilitaet",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen wiederholt festgestellt, dass Ihre Atemwege "
                             "überempfindlich reagieren (bronchiale Hyperreagibilität), "
                             "z. B. Hustenreiz bei kalter Luft, Rauch oder Duftstoffen?",
                    "required": True,
                },
                {
                    "id": "herzerkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Herzerkrankung, die Ihre Belastbarkeit "
                             "einschränkt (z. B. Herzschwäche, koronare Herzkrankheit)?",
                    "required": True,
                    "followup": {"id": "herzerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "allergien",
                    "type": "multi_choice",
                    "label": "Haben Sie Allergien oder allergische Erkrankungen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "heuschnupfen", "label": "Heuschnupfen / allergischer Schnupfen"},
                        {"value": "hausstaub_tier", "label": "Allergie gegen Hausstaubmilben oder "
                                                             "Tiere"},
                        {"value": "neurodermitis", "label": "Neurodermitis (endogenes Ekzem)"},
                        {"value": "kontaktallergie", "label": "Kontaktallergie der Haut "
                                                              "(z. B. gegen Nickel, Duftstoffe)"},
                        {"value": "andere", "label": "Andere Allergie"},
                        {"value": "keine", "label": "Keine Allergien bekannt"},
                    ],
                },
                {
                    "id": "iso_sensibilisierung",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen schon einmal eine Allergie oder "
                             "Überempfindlichkeit gegen Isocyanate festgestellt – oder "
                             "hatten Sie bei früherer Isocyanat-Arbeit Atemnot, Husten oder "
                             "Hautausschlag?",
                    "required": True,
                    "followup": {"id": "iso_sensibilisierung_desc", "type": "textarea",
                                 "label": "Was wurde festgestellt bzw. welche Beschwerden "
                                          "hatten Sie, und wann?", "when": "yes"},
                },
                {
                    "id": "rekonvaleszenz",
                    "type": "yes_no",
                    "label": "Hatten Sie in den letzten 2 Monaten eine Erkrankung der Lunge "
                             "oder des Rippenfells (z. B. Lungenentzündung, "
                             "Rippenfellentzündung)?",
                    "required": True,
                },
                {
                    "id": "akute_atemwegserkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie zurzeit oder hatten Sie in den letzten Wochen eine "
                             "akute Atemwegserkrankung (z. B. Bronchitis, starke Erkältung)?",
                    "required": True,
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Läuft bei Ihnen ein Berufskrankheiten-Verfahren, oder wurde "
                             "bei Ihnen eine Berufskrankheit anerkannt?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Um welche Erkrankung geht es?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Rauchen belastet die Lunge zusätzlich zu Isocyanaten",
            "questions": [
                {
                    "id": "raucher_status",
                    "type": "choice",
                    "label": "Rauchen Sie (Zigaretten, E-Zigaretten, Tabakerhitzer o. Ä.)?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, nie geraucht"},
                        {"value": "frueher", "label": "Früher geraucht, jetzt nicht mehr"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "taeglich", "label": "Ja, täglich"},
                    ],
                },
            ],
        },
        # ── 6 ─ Einwilligung ───────────────────────────────────────────────
        {
            "id": "einwilligung",
            "title": "Bestätigung & Einwilligung",
            "subtitle": "Zum Abschluss",
            "questions": [
                {
                    "id": "consent_truth",
                    "type": "consent",
                    "label": "Ich bestätige, dass meine Angaben vollständig und "
                             "wahrheitsgemäß sind.",
                    "error": "Bitte bestätigen Sie die Vollständigkeit Ihrer Angaben.",
                    "required": True,
                },
                {
                    "id": "consent_privacy",
                    "type": "consent",
                    "label": "Ich habe die Datenschutzhinweise gelesen und willige in die "
                             "Verarbeitung meiner Daten zu arbeitsmedizinischen Zwecken ein.",
                    "error": "Bitte akzeptieren Sie die Datenschutzhinweise.",
                    "required": True,
                },
            ],
        },
    ],
}

RULES = [
    # ── Sensibilisierung gegen Isocyanate ─────────────────────────────────
    {"wenn": {"iso_sensibilisierung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Isocyanat-Sensibilisierung",
     "quelle": "Abschnitte 6.3.2, 7.2.2 und 8.2",
     "befund": "Bekannte Isocyanat-Allergie bzw. Beschwerden bei früherer "
               "Isocyanat-Exposition angegeben.",
     "konsequenz": "Vor (weiterer) Tätigkeit mit Isocyanaten ärztlich klären: Bestimmung "
                   "spezifischer IgE- (ggf. IgG-) Antikörper gegen Isocyanate, Lungen- "
                   "funktionsdiagnostik. Sensibilisierte Personen sollten nach Abschnitt 8.2 "
                   "nicht weiter gegenüber Isocyanaten exponiert werden – Tätigkeitswechsel "
                   "nach 7.4.4 erwägen; Mitteilung an das Unternehmen nur mit Einwilligung "
                   "der versicherten Person (§ 6 (4) ArbMedVV)."},
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"atemwegserkrankungen": ["asthma", "copd", "emphysem", "tuberkulose",
                                       "pneumokoniose", "andere_lunge"]},
     "schwere": "pruefen",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 7.4, 7.4.2–7.4.4",
     "befund": "Erkrankung der Atemwege bzw. der Lunge in der Vorgeschichte angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Ausmaß objektivieren "
                   "(Spirometrie, ggf. erweiterte Lungenfunktionsdiagnostik, Vorbefunde). "
                   "Maßnahmen nach 7.4.2 prüfen (Substitution, technische/organisatorische/"
                   "persönliche Schutzmaßnahmen, expositionsärmerer Arbeitsplatz); bei zu "
                   "erwartender Änderung des Schweregrads verkürzte Vorsorgefristen nach "
                   "7.4.3; bleiben Maßnahmen ohne Erfolg, Tätigkeitswechsel nach 7.4.4 "
                   "erwägen."},
    {"wenn": {"hyperreagibilitaet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bronchiale Hyperreagibilität",
     "quelle": "Abschnitte 6.3.2 und 7.4",
     "befund": "Wiederholt festgestellte überempfindliche Atemwege (bronchiale "
               "Hyperreagibilität) angegeben.",
     "konsequenz": "Beurteilungsrelevant nach 7.4; Betroffene können schon unterhalb des "
                   "Arbeitsplatzgrenzwerts mit Bronchospasmus reagieren (6.3.2). Erweiterte "
                   "Lungenfunktionsdiagnostik veranlassen; Maßnahmen nach 7.4.2 und "
                   "verkürzte Vorsorgefristen nach 7.4.3 prüfen."},
    {"wenn": {"herzerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 7.4",
     "befund": "Herzerkrankung mit eingeschränkter Belastbarkeit angegeben.",
     "konsequenz": "Krankheiten mit Einschränkung der kardialen Funktion sind nach 7.4 "
                   "beurteilungsrelevant: kardiale Befunde einholen, Ausmaß der "
                   "Einschränkung klären; Maßnahmen nach 7.4.2 bzw. verkürzte Fristen "
                   "nach 7.4.3 erwägen."},
    {"wenn": {"allergien": ["neurodermitis"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 2, 7.4 und 8.1",
     "befund": "Neurodermitis (endogenes Ekzem) angegeben.",
     "konsequenz": "Endogenes Ekzem ist nach 7.4 beurteilungsrelevant. DGUV Empfehlung "
                   "»Gefährdung der Haut« zusätzlich einbeziehen; Hautzustand erheben, "
                   "optimalen Hautschutz empfehlen; Maßnahmen nach 7.4.2 und ggf. "
                   "verkürzte Vorsorgefristen prüfen."},
    {"wenn": {"allergien": ["heuschnupfen", "hausstaub_tier", "kontaktallergie", "andere"]},
     "schwere": "hinweis",
     "bereich": "Atopie/Allergie",
     "quelle": "Abschnitte 7.1, 8.1 und 8.2",
     "befund": "Allergische Erkrankung bzw. atopische Disposition angegeben.",
     "konsequenz": "Allergologische Anamnese mit den Standardfragebögen I und II (Anhang "
                   "der DGUV Empfehlung »Platinverbindungen«) vertiefen, ggf. Gesamt-IgE. "
                   "Spezielle Beratung nach 8.1: Personen, die gegen andere Allergene "
                   "sensibilisiert sind, entwickeln leichter eine Isocyanat-"
                   "Sensibilisierung (8.2)."},
    # ── Aktuelle Beschwerden ──────────────────────────────────────────────
    {"wenn": {"atem_symptome": ["husten", "auswurf", "kurzatmigkeit", "pfeifen",
                                "anfall", "brustenge"]},
     "schwere": "pruefen",
     "bereich": "Atembeschwerden",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Atembeschwerden (Husten, Auswurf, Kurzatmigkeit, Atemgeräusche, "
               "anfallsartige Atemnot oder Brustenge) angegeben.",
     "konsequenz": "Anamnestischer Verdacht auf eine Erkrankung nach 7.4: erweiterte "
                   "Lungenfunktionsdiagnostik veranlassen (Ganzkörperplethysmographie, "
                   "Untersuchung vor und nach einer Arbeitsschicht mit Exposition, "
                   "Peak-flow-Messungen); in unklaren Fällen spezifische IgE- (ggf. IgG-) "
                   "Antikörper gegen Isocyanate bestimmen."},
    {"wenn": {"naechtlich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atembeschwerden",
     "quelle": "Abschnitte 6.3.3 und 7.1",
     "befund": "Nächtlicher Husten bzw. nächtliche Atemnot angegeben.",
     "konsequenz": "Warnsymptom für Isocyanat-Asthma vom verzögerten oder dualen Typ: "
                   "erweiterte Lungenfunktionsdiagnostik mit Peak-flow-Messungen über "
                   "Arbeits- und arbeitsfreie Tage; in unklaren Fällen spezifische "
                   "Antikörper bestimmen."},
    {"wenn": {"arbeitsbezug": ["bei_arbeit", "verzoegert", "besser_frei"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug der Beschwerden",
     "quelle": "Abschnitte 6.3, 6.5 und 7.2.2",
     "befund": "Beschwerden mit erkennbarem Bezug zur Arbeit (während der Arbeit, "
               "verzögert nach der Arbeit oder Besserung an freien Tagen).",
     "konsequenz": "Verdacht auf arbeitsbedingte Atemwegserkrankung: Untersuchungen vor "
                   "und nach einer Arbeitsschicht, Peak-flow-Verlauf, spezifische IgE-/"
                   "IgG-Antikörper. Bei begründetem Verdacht ärztliche Anzeige einer "
                   "Berufskrankheit (BK-Nr. 1315) prüfen; ergeben sich Anhaltspunkte für "
                   "unzureichende Schutzmaßnahmen, Mitteilung an das Unternehmen mit "
                   "Maßnahmenvorschlag (§ 6 (4) ArbMedVV)."},
    {"wenn": {"grippe_gefuehl": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Alveolitis-Verdacht",
     "quelle": "Abschnitte 6.3.2 und 6.3.3",
     "befund": "Grippeartige Beschwerden (Fieber, Schüttelfrost, Gliederschmerzen) "
               "Stunden nach der Arbeit angegeben.",
     "konsequenz": "An eine exogen-allergische Alveolitis denken: erweiterte "
                   "Lungenfunktionsdiagnostik, Bestimmung spezifischer IgG-Antikörper, "
                   "zeitnahe pneumologische Abklärung veranlassen; bis zur Klärung "
                   "Exposition kritisch prüfen."},
    {"wenn": {"haut_symptome": ["roetung", "quaddeln", "ekzem", "verfaerbung"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 2, 6.3 und 6.5",
     "befund": "Hautveränderungen (Rötung/Juckreiz, Quaddeln, Ekzem oder bräunliche "
               "Kontaktverfärbungen) angegeben.",
     "konsequenz": "Isocyanate können Reizungen und Sensibilisierungen der Haut "
                   "(Urtikaria, Kontaktekzem) verursachen; bräunliche Verfärbungen zeigen "
                   "direkten Hautkontakt an. DGUV Empfehlung »Gefährdung der Haut« "
                   "einbeziehen, dermatologische Abklärung und Hautschutzberatung; bei "
                   "schwerer oder wiederholt rückfälliger Hauterkrankung BK-Nr. 5101 "
                   "beachten."},
    # ── Exposition, Schutzmaßnahmen, Biomonitoring ────────────────────────
    {"wenn": {"hautkontakt": ["regelmaessig"]},
     "schwere": "pruefen",
     "bereich": "Hautkontakt/Biomonitoring",
     "quelle": "Abschnitte 2, 6.2 und 6.4",
     "befund": "Regelmäßiger Hautkontakt mit Isocyanaten bzw. nicht ausgehärteten "
               "Produkten angegeben.",
     "konsequenz": "Bei regelmäßigem, nicht ausschließbarem Hautkontakt ist "
                   "Pflichtvorsorge erforderlich – Abgleich mit der Gefährdungsbeurteilung. "
                   "Biomonitoring im Urin durchführen bzw. anbieten (z. B. MDA für MDI, "
                   "BLW 10 µg/l; Hexamethylendiamin für HDI, BAT 15 µg/g Kreatinin; "
                   "Toluylendiamin-Summe für TDI, BAT 5 µg/g Kreatinin – Probennahme zum "
                   "Expositions-/Schichtende), da die biologischen Werte auch die Aufnahme "
                   "über die Haut erfassen; Hautschutz beraten."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfall/Exposition",
     "quelle": "Abschnitte 6.3.2 und 7.1",
     "befund": "Zwischenfall bzw. ungewöhnlicher Betriebszustand mit möglicher hoher "
               "Isocyanat-Freisetzung angegeben.",
     "konsequenz": "Hergang und Beschwerden dokumentieren (nach massiver Exposition sind "
                   "Bronchitis bis Lungenödem möglich), Lungenfunktion kontrollieren, ggf. "
                   "Biomonitoring. Ergeben sich Anhaltspunkte, dass Schutzmaßnahmen nicht "
                   "ausreichen, Mitteilung an das Unternehmen und Vorschlag von Maßnahmen "
                   "(§ 6 (4) ArbMedVV)."},
    {"wenn": {"psa": ["keine"]},
     "wenn_nicht": {"expo_bereiche": ["geschlossen"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen/PSA",
     "quelle": "Abschnitte 7.1, 8.1 und 8.2",
     "befund": "Umgang mit Isocyanaten ohne persönliche Schutzausrüstung angegeben.",
     "konsequenz": "Beratung zum Tragen geeigneter PSA und zur Arbeitshygiene (kein Essen "
                   "und Trinken am Arbeitsplatz, gründliches Händewaschen vor Pausen, "
                   "Wechsel der Arbeitskleidung). Abgleich mit der Gefährdungsbeurteilung; "
                   "bei Anhaltspunkten für unzureichende Schutzmaßnahmen Mitteilung an das "
                   "Unternehmen mit Maßnahmenvorschlag (§ 6 (4) ArbMedVV)."},
    {"wenn": {"kleidung_kontaminiert": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Arbeitshygiene",
     "quelle": "Abschnitt 6.2",
     "befund": "Kontaminierte Arbeitskleidung wird weitergetragen.",
     "konsequenz": "Beratung: kontaminierte Arbeitskleidung ist umgehend zu wechseln – "
                   "Hautkontakt (auch durch durchdrungene Kleidung) kann eine "
                   "Sensibilisierung der Atemwege verursachen."},
    {"wenn": {"reiz_symptome": ["augen", "nase", "hals"]},
     "schwere": "pruefen",
     "bereich": "Reizsymptome",
     "quelle": "Abschnitte 6.3.2 und 8.2",
     "befund": "Reizbeschwerden an Augen, Nase oder Rachen bei bzw. nach der Arbeit "
               "angegeben.",
     "konsequenz": "Mögliche Frühzeichen einer relevanten Isocyanat-Exposition "
                   "(Konjunktivitis, Rhinitis, Pharyngitis/Laryngitis): Arbeitsplatzbezug "
                   "und Einhaltung des AGW klären; bei Anhaltspunkten für unzureichende "
                   "Schutzmaßnahmen Mitteilung an das Unternehmen (§ 6 (4) ArbMedVV); "
                   "Verlauf bei der nächsten Vorsorge kontrollieren."},
    # ── Fristen ───────────────────────────────────────────────────────────
    {"wenn": {"rekonvaleszenz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorsorgefrist",
     "quelle": "Abschnitt 7.4.3",
     "befund": "Erkrankung der Lunge oder des Rippenfells in den letzten 2 Monaten "
               "angegeben.",
     "konsequenz": "Für Rekonvaleszenten nach folgenlos abgeklungener Erkrankung der Lunge "
                   "oder des Rippenfells gilt für die Dauer von 1 bis 2 Monaten eine "
                   "verkürzte Frist: Vorsorge in diesem Zeitraum wiederholen, ggf. "
                   "Maßnahmen nach 7.4.2 empfehlen."},
    {"wenn": {"akute_atemwegserkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorsorgefrist",
     "quelle": "Abschnitt 7.4.3 (weitere Vorsorgen)",
     "befund": "Aktuelle oder kurz zurückliegende akute Atemwegserkrankung angegeben.",
     "konsequenz": "Bei Personen mit oder kurzfristig nach akuten Erkrankungen der "
                   "Atemwege verkürzte Vorsorgefrist empfehlen; Spirometrie ggf. erst nach "
                   "Abklingen durchführen bzw. Befund nur unter Vorbehalt verwerten."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 6.5 und 7.1",
     "befund": "Laufendes oder abgeschlossenes Berufskrankheiten-Verfahren angegeben.",
     "konsequenz": "BK-Verfahren dokumentieren und Befunde daraus in die Beurteilung "
                   "einbeziehen (BK-Nr. 1315 Erkrankungen durch Isocyanate, BK-Nr. 5101 "
                   "Hauterkrankungen)."},
    # ── Beratung ──────────────────────────────────────────────────────────
    {"wenn": {"raucher_status": ["taeglich", "gelegentlich"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Aktuelles Rauchen angegeben.",
     "konsequenz": "Beratung: inhalatives Rauchen verschlechtert die Lungenfunktion; auf "
                   "mögliche additive Effekte von Rauchen und Isocyanat-Exposition "
                   "hinweisen. Arbeitshygiene betonen (gründliches Händewaschen besonders "
                   "vor Raucherpausen); zudem über die mögliche krebserzeugende Wirkung "
                   "einiger Isocyanate (MDI, TDI – Karzinogenität Kategorie 2) aufklären."},
]
