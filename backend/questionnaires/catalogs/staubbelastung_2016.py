# -*- coding: utf-8 -*-
"""G 1.4 Staubbelastung – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 1.4 »Staubbelastung«
(Fassung Oktober 2014), S. 107–117."""

SLUG = "g1-4-staubbelastung-2016"

CATALOG = {
    "version": 2,
    "title": "G 1.4 Staubbelastung (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 1.4 »Staubbelastung« (Fassung Oktober 2014), S. 107–117",
    "sections": [
        # ── 1 ─ Anlass der Untersuchung ────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Ist dies Ihre erste Untersuchung nach G 1.4 (Staubbelastung)?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt; "
                            "Nachuntersuchungen folgen in regelmäßigen Abständen.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Ja, Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nein, Nachuntersuchung"},
                    ],
                },
                {
                    "id": "altersgruppe",
                    "type": "choice",
                    "label": "Wie alt sind Sie?",
                    "hint": "Das Alter ist wichtig für den Abstand bis zur nächsten "
                            "Nachuntersuchung (unter 40 Jahren: 60 Monate, ab 40 Jahren: "
                            "36 Monate).",
                    "required": True,
                    "options": [
                        {"value": "unter40", "label": "Unter 40 Jahre"},
                        {"value": "ab40", "label": "40 Jahre oder älter"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Staubbelastung ───────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Staubbelastung",
            "subtitle": "Ihre jetzige und frühere Arbeit mit Staub",
            "questions": [
                {
                    "id": "taetigkeit_jetzt",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "staub_branche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie mit Staubbelastung?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "bau", "label": "Bauwirtschaft (z. B. Abbruch, Stemmen, Schleifen, Putzarbeiten)"},
                        {"value": "bergbau_steine", "label": "Bergbau, Naturstein-, Kies-, Sand- oder Kalkindustrie"},
                        {"value": "keramik_glas", "label": "Keramik- oder Glasindustrie"},
                        {"value": "giesserei", "label": "Gießereiindustrie"},
                        {"value": "holz_kunststoff", "label": "Holz- oder Kunststoffindustrie / Handwerk"},
                        {"value": "textil_papier", "label": "Textil- oder Papierindustrie"},
                        {"value": "mahlen_bearbeitung", "label": "Mahlen, mechanische Bearbeitung, Abfüllen"},
                        {"value": "andere", "label": "Anderer Bereich mit Staub"},
                        {"value": "keine", "label": "Keine besondere Staubbelastung"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie schon mit höherer Staubbelastung?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis15", "label": "5 bis 15 Jahre"},
                        {"value": "ueber15", "label": "Mehr als 15 Jahre"},
                    ],
                },
                {
                    "id": "frueher_staub",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Tätigkeiten Stäuben oder anderen Stoffen "
                             "ausgesetzt, die die Atemwege schädigen können?",
                    "required": True,
                    "followup": {"id": "frueher_staub_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, in welchen "
                                          "Zeiträumen?", "when": "yes"},
                },
                {
                    "id": "irritativ_sensibilisierend",
                    "type": "yes_no",
                    "label": "Kommen an Ihrem Arbeitsplatz reizende (irritative) oder "
                             "allergieauslösende (sensibilisierende) Stoffe vor, z. B. "
                             "Säuredämpfe, Lösungsmittel, Mehl-, Holz- oder Metallstäube?",
                    "required": True,
                    "followup": {"id": "irritativ_desc", "type": "text",
                                 "label": "Welche Stoffe?", "when": "yes"},
                },
                {
                    "id": "schweissrauch",
                    "type": "yes_no",
                    "label": "Besteht Ihre Arbeit überwiegend aus Schweißen oder Trennen von "
                             "Metallen (Schweißrauche)?",
                    "required": True,
                },
                {
                    "id": "aes_wollen",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Hochtemperatur-Dämmwollen (AES-Wollen, "
                             "polykristalline Wollen), z. B. im Ofen- und Feuerungsbau?",
                    "required": True,
                },
                {
                    "id": "atemschutz",
                    "type": "yes_no",
                    "label": "Tragen Sie bei der Arbeit Atemschutzgeräte (z. B. Masken mit "
                             "Filter, Gebläse- oder Pressluftatmer)?",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Atembeschwerden",
            "subtitle": "Husten, Auswurf, Atemnot und Beschwerden bei der Arbeit",
            "questions": [
                {
                    "id": "husten",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Husten?",
                    "required": True,
                    "followup": {"id": "husten_desc", "type": "text",
                                 "label": "Seit wann, wie oft, und wie lange jeweils?",
                                 "when": "yes"},
                },
                {
                    "id": "auswurf",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Auswurf (Schleim beim Husten)?",
                    "required": True,
                    "followup": {"id": "auswurf_desc", "type": "text",
                                 "label": "Seit wann, und wie oft?", "when": "yes"},
                },
                {
                    "id": "atemnot",
                    "type": "choice",
                    "label": "Haben Sie Atemnot (Luftnot, Kurzatmigkeit)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "belastung", "label": "Ja, bei körperlicher Anstrengung "
                                                        "(z. B. Treppensteigen, schwere Arbeit)"},
                        {"value": "ruhe", "label": "Ja, auch in Ruhe"},
                    ],
                },
                {
                    "id": "atemnot_seit",
                    "type": "text",
                    "label": "Seit wann besteht die Atemnot?",
                    "required": False,
                    "show_if": {"id": "atemnot", "in": ["belastung", "ruhe"]},
                },
                {
                    "id": "beschwerden_arbeitsbezug",
                    "type": "yes_no",
                    "label": "Treten Ihre Beschwerden (Husten, Auswurf, Atemnot) vor allem am "
                             "Arbeitsplatz oder bei bestimmten Tätigkeiten auf – und bessern "
                             "sie sich am Wochenende oder im Urlaub?",
                    "required": True,
                    "followup": {"id": "arbeitsbezug_desc", "type": "textarea",
                                 "label": "Bei welchen Tätigkeiten oder an welchen Orten, und "
                                          "seit wann?", "when": "yes"},
                },
                {
                    "id": "reizempfindlich",
                    "type": "yes_no",
                    "label": "Bekommen Sie schon bei geringen Mengen Staub, Rauch, kalter Luft "
                             "oder Gerüchen Beschwerden (Hustenreiz, Engegefühl, Atemnot)?",
                    "required": True,
                },
                {
                    "id": "infekt_mehrwoechig",
                    "type": "yes_no",
                    "label": "Hatten Sie in letzter Zeit eine mehrwöchige Erkrankung der "
                             "Atemwege (z. B. hartnäckige Bronchitis nach einem Infekt)?",
                    "required": True,
                    "followup": {"id": "infekt_desc", "type": "text",
                                 "label": "Wann, und wie lange?", "when": "yes"},
                },
                {
                    "id": "sonstige_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie sonstige Beschwerden (z. B. Leistungsknick, "
                             "Gewichtsverlust, Brustschmerzen)?",
                    "required": True,
                    "followup": {"id": "sonstige_beschwerden_desc", "type": "textarea",
                                 "label": "Welche Beschwerden?", "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen von Lunge, Atemwegen und Herz",
            "questions": [
                {
                    "id": "asthma",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen jemals Asthma bronchiale festgestellt?",
                    "required": True,
                },
                {
                    "id": "copd",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine chronische (obstruktive) Bronchitis, COPD "
                             "oder ein Lungenemphysem (überblähte Lunge) festgestellt?",
                    "required": True,
                },
                {
                    "id": "hyperreagibilitaet",
                    "type": "yes_no",
                    "label": "Reagieren Ihre Atemwege seit mehr als 6 Monaten dauerhaft "
                             "überempfindlich (bronchiale Hyperreagibilität)?",
                    "required": True,
                },
                {
                    "id": "staublunge",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Staublunge (z. B. Silikose, Asbestose), "
                             "eine Lungenfibrose (Vernarbung der Lunge), eine Sarkoidose oder "
                             "eine Allergie-Lungenentzündung (exogen allergische Alveolitis, "
                             "z. B. »Farmerlunge«) festgestellt?",
                    "required": True,
                    "followup": {"id": "staublunge_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "thorax",
                    "type": "yes_no",
                    "label": "Haben Sie eine starke Verformung des Brustkorbs oder "
                             "Verwachsungen des Rippenfells (z. B. nach Rippenfellentzündung "
                             "oder Operation), die die Atmung einschränken?",
                    "required": True,
                },
                {
                    "id": "herzinsuffizienz",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Herzschwäche (Herzinsuffizienz) oder eine "
                             "andere Herz-Kreislauf-Erkrankung mit Auswirkung auf die Atmung "
                             "festgestellt?",
                    "required": True,
                    "followup": {"id": "herzinsuffizienz_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "bronchial_medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie Medikamente für die Bronchien (z. B. Asthma-Sprays, "
                             "bronchialerweiternde Mittel, Kortison zum Inhalieren)?",
                    "required": True,
                    "followup": {"id": "bronchial_medikamente_desc", "type": "text",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Tabakkonsum – wichtig für die Beurteilung der Atemwege",
            "questions": [
                {
                    "id": "raucher_status",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht (Nie-Raucher/in)"},
                        {"value": "ex", "label": "Früher ja, jetzt nicht mehr (Ex-Raucher/in)"},
                        {"value": "raucher", "label": "Ja, ich rauche"},
                    ],
                },
                {
                    "id": "rauch_details",
                    "type": "textarea",
                    "label": "Was rauchen bzw. rauchten Sie (Zigaretten, Zigarren, Pfeife), "
                             "wie viel pro Tag, und von wann bis wann?",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ex", "raucher"]},
                },
                {
                    "id": "packungsjahre",
                    "type": "choice",
                    "label": "Wie viele »Packungsjahre« kommen bei Ihnen ungefähr zusammen?",
                    "hint": "Packungsjahre = Schachteln pro Tag × Raucherjahre. Beispiel: "
                            "1 Schachtel täglich über 10 Jahre = 10 Packungsjahre.",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ex", "raucher"]},
                    "options": [
                        {"value": "unter10", "label": "Weniger als 10"},
                        {"value": "10bis20", "label": "10 bis 20"},
                        {"value": "ueber20", "label": "Mehr als 20"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
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
    # ── Dauernde gesundheitliche Bedenken (Abschnitt 2.1.1) ───────────────
    {"wenn": {"asthma": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 2.1.1 und 1.2.3",
     "befund": "Asthma bronchiale in der Vorgeschichte angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken (manifeste obstruktive "
                   "Atemwegserkrankung): Schweregrad objektivieren – Spirometrie mit "
                   "Fluss-Volumen-Kurve, Ergänzungsuntersuchung mit Reversibilitätsprüfung "
                   "der Obstruktion. Bei weniger stark ausgeprägter Erkrankung Voraussetzungen "
                   "nach 2.1.3 prüfen (Schutzmaßnahmen, Expositionsbegrenzung, verkürzte "
                   "Nachuntersuchungsfristen), sonst dauernde Bedenken aussprechen."},
    {"wenn": {"copd": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 2.1.1 und 1.2.3",
     "befund": "Chronische (obstruktive) Bronchitis, COPD oder Lungenemphysem angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken bei wesentlicher "
                   "funktioneller Auswirkung: Lungenfunktion objektivieren; bei "
                   "Emphysemverdacht Ganzkörperplethysmographie, Diffusionskapazität TLCO "
                   "oder Blutgasanalyse in Ruhe und unter Belastung (1.2.3). Bei geringer "
                   "Ausprägung 2.1.3 (Bedenken unter Voraussetzungen) prüfen; Beratung, "
                   "dass eine gezielte Behandlung geboten und möglich ist (2.2)."},
    {"wenn": {"hyperreagibilitaet": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 2.1.1 und 1.2.3",
     "befund": "Anhaltend überempfindliche Atemwege (länger als 6 Monate) angegeben.",
     "konsequenz": "Bei symptomatischer, irreversibler bronchialer Hyperreagibilität "
                   "(länger als 6 Monate) dauernde gesundheitliche Bedenken prüfen. "
                   "Ergänzungsuntersuchung auf unspezifische bronchiale Hyperreagibilität "
                   "(Leitfaden Lungenfunktionsprüfung); bei Verdacht auf klinisch bedeutsame "
                   "Hyperreagibilität Lungenfunktion vor und nach der Exposition am "
                   "Arbeitsplatz messen (Spirometrie, Peak-Flow)."},
    {"wenn": {"staublunge": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Lungenerkrankung",
     "quelle": "Abschnitte 2.1.1 und 1.2.3",
     "befund": "Staublungen-, fibrosierende oder granulomatöse Lungenerkrankung bzw. "
               "exogen allergische Alveolitis in der Vorgeschichte angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken (u. a. röntgenologisch "
                   "objektivierbare Quarz- oder Asbeststaublungenerkrankung, fibrosierende/"
                   "granulomatöse Veränderungen, erhebliche Vorschädigung): "
                   "Ergänzungsuntersuchung Röntgen-Thorax; Vorbilder (nicht älter als "
                   "1 Jahr) heranziehen. Zusätzlich Notwendigkeit des Grundsatzes G 1.1 "
                   "prüfen (3.3)."},
    {"wenn": {"thorax": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Lungenerkrankung",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Funktionell wirksame Brustkorbverformung bzw. Rippenfellverwachsungen "
               "angegeben.",
     "konsequenz": "Funktionell wirksame Thoraxdeformitäten/Pleuraverschwartungen zählen zu "
                   "den Tatbeständen dauernder gesundheitlicher Bedenken: funktionelle "
                   "Auswirkung mit Spirometrie und erweiterter Lungenfunktionsdiagnostik "
                   "objektivieren; bei geringer Ausprägung 2.1.3 prüfen."},
    {"wenn": {"herzinsuffizienz": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Herzinsuffizienz bzw. kardiopulmonale Erkrankung angegeben.",
     "konsequenz": "Bestehende Herzinsuffizienz und kardiopulmonale Erkrankungen, bei denen "
                   "stärkere Staubbelastung ein zusätzliches Risiko bedeutet (z. B. "
                   "Stauungsbronchitis), sind Tatbestände dauernder gesundheitlicher "
                   "Bedenken: kardiologische Vorbefunde einholen, Untersuchung der Atmungs- "
                   "und Kreislauforgane; bei geringer Ausprägung 2.1.3 prüfen."},
    # ── Befristete gesundheitliche Bedenken (Abschnitt 2.1.2) ─────────────
    {"wenn": {"infekt_mehrwoechig": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorübergehende Überempfindlichkeit",
     "quelle": "Abschnitte 2.1.2 und 1.1",
     "befund": "Mehrwöchige Atemwegserkrankung in letzter Zeit angegeben.",
     "konsequenz": "Befristete gesundheitliche Bedenken erwägen (vorübergehende "
                   "Überempfindlichkeit der Atemwege infolge bronchopulmonaler Infekte); "
                   "nach Abklingen erneut beurteilen. Nach mehrwöchigen "
                   "Atemwegserkrankungen mit Hinweis auf Atemwegsobstruktion vorzeitige "
                   "Nachuntersuchung veranlassen (1.1)."},
    {"wenn": {"reizempfindlich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorübergehende Überempfindlichkeit",
     "quelle": "Abschnitte 2.1.2 und 1.2.3",
     "befund": "Beschwerden bereits bei geringen Konzentrationen inhalativer Reize "
               "(Staub, Rauch, kalte Luft, Gerüche) angegeben.",
     "konsequenz": "Befristete gesundheitliche Bedenken prüfen (Beschwerden bei relativ "
                   "niedrigen Konzentrationen inhalativer Noxen); Ergänzungsuntersuchung "
                   "auf unspezifische bronchiale Hyperreagibilität durchführen."},
    # ── Beschwerden und Verlauf ───────────────────────────────────────────
    {"wenn": {"husten": ["yes"], "auswurf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 1.2.1, 3.2 und 2.2",
     "befund": "Häufiger Husten und Auswurf angegeben.",
     "konsequenz": "Verdacht auf chronische Bronchitis (WHO-Definition: Husten und Auswurf "
                   "an den meisten Tagen während mindestens je 3 Monaten in 2 aufeinander "
                   "folgenden Jahren): Dauer und Häufigkeit klären, Spirometrie bewerten, "
                   "ggf. Ergänzungsuntersuchung. Beratung, dass bei Hinweisen auf eine "
                   "chronisch obstruktive Atemwegserkrankung eine gezielte Behandlung "
                   "medizinisch geboten und möglich ist (2.2)."},
    {"wenn": {"atemnot": ["belastung", "ruhe"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 1.2.1 und 1.2.3",
     "befund": "Atemnot bei Belastung bzw. in Ruhe angegeben.",
     "konsequenz": "Obstruktive Ventilationsstörung abklären: Spirometrie mit "
                   "Fluss-Volumen-Kurve; Ergänzungsuntersuchung mit erweiterter "
                   "Lungenfunktionsdiagnostik (Atemwegswiderstand, Reversibilitätsprüfung), "
                   "bei Verdacht auf klinisch bedeutsames Emphysem "
                   "Ganzkörperplethysmographie, TLCO oder Blutgasanalyse in Ruhe und unter "
                   "Belastung; ggf. Röntgen-Thorax."},
    {"wenn": {"beschwerden_arbeitsbezug": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug",
     "quelle": "Abschnitte 1.1, 1.2.1 und 2.2",
     "befund": "Arbeitsplatz- bzw. tätigkeitsbezogene Atembeschwerden mit Besserung in "
               "arbeitsfreien Zeiten (positive Karenzprobe) angegeben.",
     "konsequenz": "Orts- und Zeitbezug der Beschwerden dokumentieren (Zwischenanamnese); "
                   "Lungenfunktion vor und nach Exposition am Arbeitsplatz messen "
                   "(Spirometrie, Peak-Flow). Vorzeitige Nachuntersuchung ist angezeigt, "
                   "wenn Beschwerden auf eine Atemwegsobstruktion hinweisen oder die "
                   "versicherte Person einen Zusammenhang mit der Tätigkeit vermutet (1.1). "
                   "Ergibt sich Bedarf zur Aktualisierung der Gefährdungsbeurteilung, "
                   "Mitteilung an den Arbeitgeber unter Wahrung der schutzwürdigen Belange "
                   "(2.2)."},
    # ── Abgrenzung zu anderen Grundsätzen (Vorbemerkungen, 3.3) ───────────
    {"wenn": {"schweissrauch": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Abgrenzung Untersuchungsanlass",
     "quelle": "Abschnitt 3.3 (Bemerkungen)",
     "befund": "Überwiegende Exposition gegenüber Schweißrauchen angegeben.",
     "konsequenz": "Bei überwiegender Schweißrauch-Exposition den Grundsatz G 39 "
                   "(Schweißrauche) für die arbeitsmedizinische Untersuchung anwenden."},
    {"wenn": {"irritativ_sensibilisierend": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Abgrenzung Untersuchungsanlass",
     "quelle": "Vorbemerkungen und Abschnitt 1.2.1",
     "befund": "Irritative und/oder sensibilisierende Stoffe am Arbeitsplatz angegeben.",
     "konsequenz": "Die entsprechenden DGUV Grundsätze für erbgutverändernde, "
                   "krebserzeugende, fibrogene, allergisierende oder chemisch-irritative "
                   "Bestandteile einbeziehen (z. B. G 23); Stoffliste über die "
                   "Gefährdungsbeurteilung klären."},
    {"wenn": {"atemschutz": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Abgrenzung Untersuchungsanlass",
     "quelle": "Abschnitt 3.3 (Bemerkungen)",
     "befund": "Tragen von Atemschutzgeräten angegeben.",
     "konsequenz": "Zur Vermeidung von Mehrfachuntersuchungen die Notwendigkeit der "
                   "Grundsätze G 26 (Atemschutzgeräte) und ggf. G 1.1 prüfen und die "
                   "Untersuchungen koordinieren."},
    {"wenn": {"aes_wollen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Exposition",
     "quelle": "Abschnitt 3.1.1",
     "befund": "Tätigkeit mit AES-Wollen bzw. polykristallinen Wollen angegeben.",
     "konsequenz": "Dabei entstehende partikelförmige Stäube als A- und E-Stäube bewerten; "
                   "weitere Hinweise der DGUV Information 240-014 (Handlungsanleitung "
                   "G 1.4) beachten."},
    # ── Fristen (Abschnitt 1.1) ───────────────────────────────────────────
    {"wenn": {"untersuchung_art": ["nach"], "altersgruppe": ["ab40"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1",
     "befund": "Nachuntersuchung bei einer Person ab 40 Jahren.",
     "konsequenz": "Nächste Nachuntersuchung nach 36 Monaten anberaumen (sofern keine "
                   "staatlichen Fristvorgaben gelten); bei Beschwerden oder auffälligen "
                   "Befunden vorzeitig."},
    {"wenn": {"untersuchung_art": ["nach"], "altersgruppe": ["unter40"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1",
     "befund": "Nachuntersuchung bei einer Person unter 40 Jahren.",
     "konsequenz": "Nächste Nachuntersuchung nach 60 Monaten anberaumen (sofern keine "
                   "staatlichen Fristvorgaben gelten); bei Beschwerden oder auffälligen "
                   "Befunden vorzeitig, außerdem Nachuntersuchung bei Beendigung der "
                   "Tätigkeit."},
    # ── Rauchen (Abschnitt 2.2) ───────────────────────────────────────────
    {"wenn": {"raucher_status": ["raucher"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung: Zigarettenrauchen ist die Hauptursache der chronischen "
                   "obstruktiven Atemwegserkrankung; auf die nachweisliche Besserung der "
                   "Lungenfunktion nach Rauchstopp und die Möglichkeit einer erfolgreichen "
                   "Entwöhnungsbehandlung hinweisen; Packungsjahre dokumentieren (1.2.1)."},
]
