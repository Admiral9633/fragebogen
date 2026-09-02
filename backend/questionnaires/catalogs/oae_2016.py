# -*- coding: utf-8 -*-
"""G 23 Obstruktive Atemwegserkrankungen – DGUV Grundsatz 2016. Quelle: DGUV
Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 23
»Obstruktive Atemwegserkrankungen« (Fassung Oktober 2014), S. 355–365."""

SLUG = "g23-oae-2016"

CATALOG = {
    "version": 2,
    "title": "G 23 Obstruktive Atemwegserkrankungen (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 23 »Obstruktive Atemwegserkrankungen« (Fassung Oktober 2014), S. 355–365",
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
                    "label": "Ist dies Ihre Erstuntersuchung nach G 23 (obstruktive "
                             "Atemwegserkrankungen) oder eine Nachuntersuchung?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Erste "
                            "Nachuntersuchung nach 6–12 Monaten, weitere nach "
                            "12–36 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung"},
                    ],
                },
                {
                    "id": "zusammenhang_vermutung",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Arbeitsstoffe",
            "subtitle": "Ihre Arbeit und die Stoffe, die dort vorkommen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "stoffgruppen",
                    "type": "multi_choice",
                    "label": "Welche Stoffe kommen an Ihrem Arbeitsplatz vor?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "mehl_backmittel", "label": "Mehlstaub, Backmittel oder enzymhaltige Stäube (Bäckerei, Mühle)"},
                        {"value": "getreide_futter", "label": "Getreide- oder Futtermittelstäube (Landwirtschaft, Futtermittel)"},
                        {"value": "tierstaub", "label": "Stäube bzw. Haut-/Haarbestandteile von Labor- oder Nutztieren"},
                        {"value": "latex", "label": "Naturlatex (z. B. gepuderte Latexhandschuhe)"},
                        {"value": "friseur", "label": "Blondier-/Haarfärbemittel (Persulfate) im Friseurhandwerk"},
                        {"value": "saeuren_laugen", "label": "Säure- oder Laugen-Nebel (z. B. Salzsäure, Natronlauge, Schwefelsäure)"},
                        {"value": "epoxid_anhydride", "label": "Unausgehärtete Epoxidharze oder Kunstharz-Härter (Säureanhydride)"},
                        {"value": "formaldehyd", "label": "Formaldehyd"},
                        {"value": "isocyanate", "label": "Isocyanate (z. B. PU-Schäume, 2K-Lacke)"},
                        {"value": "metall", "label": "Metallstäube oder -rauche"},
                        {"value": "reizgase", "label": "Reizgase (z. B. Ammoniak, Chlor, Schwefeldioxid, nitrose Gase)"},
                        {"value": "loesungsmittel", "label": "Lösungsmittel mit Reizwirkung auf die Atemwege"},
                        {"value": "andere", "label": "Andere Stäube, Dämpfe oder Rauche"},
                        {"value": "unbekannt", "label": "Keiner davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie mit solchen Stoffen?",
                    "required": True,
                    "options": [
                        {"value": "beginnt", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis15", "label": "5 bis 15 Jahre"},
                        {"value": "ueber15", "label": "Mehr als 15 Jahre"},
                    ],
                },
                {
                    "id": "frueher_taetigkeiten",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt zu Stäuben, "
                             "Dämpfen, Rauchen oder reizenden Stoffen?",
                    "required": True,
                    "followup": {"id": "frueher_taetigkeiten_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, in welchen "
                                          "Zeiträumen?", "when": "yes"},
                },
                {
                    "id": "schutzmassnahmen",
                    "type": "multi_choice",
                    "label": "Welche Schutzmaßnahmen nutzen Sie bei der Arbeit?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "absaugung", "label": "Absaugung oder Lüftung an der Staub-/Dampfquelle"},
                        {"value": "atemschutz", "label": "Atemschutz (z. B. FFP-Maske)"},
                        {"value": "handschuhe", "label": "Schutzhandschuhe"},
                        {"value": "keine", "label": "Keine besonderen Schutzmaßnahmen"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 3 ─ Arbeitsplatzbezogene Beschwerden ───────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden an Augen, Nase, Atemwegen und Haut",
            "questions": [
                {
                    "id": "beschwerden_vorhanden",
                    "type": "yes_no",
                    "label": "Haben Sie Beschwerden wie Fließschnupfen, Niesen, "
                             "Augenbrennen, Atembeschwerden oder juckende Quaddeln auf "
                             "der Haut (Urtikaria)?",
                    "required": True,
                },
                {
                    "id": "beschwerden_art",
                    "type": "multi_choice",
                    "label": "Welche Beschwerden haben Sie?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "beschwerden_vorhanden", "in": ["yes"]},
                    "options": [
                        {"value": "fliessschnupfen", "label": "Fließschnupfen (laufende Nase)"},
                        {"value": "niesen", "label": "Niesanfälle"},
                        {"value": "augenbrennen", "label": "Brennende, juckende oder gerötete Augen"},
                        {"value": "husten", "label": "Husten oder Hustenreiz"},
                        {"value": "atembeschwerden", "label": "Atembeschwerden (Atemnot, pfeifende Atmung, Engegefühl)"},
                        {"value": "urtikaria", "label": "Juckende Quaddeln auf der Haut (Nesselsucht/Urtikaria)"},
                        {"value": "andere", "label": "Andere Beschwerden"},
                    ],
                },
                {
                    "id": "beschwerden_arbeit",
                    "type": "yes_no",
                    "label": "Treten die Beschwerden vermehrt am Arbeitsplatz oder während "
                             "der Arbeit auf?",
                    "required": True,
                    "show_if": {"id": "beschwerden_vorhanden", "in": ["yes"]},
                },
                {
                    "id": "besserung_karenz",
                    "type": "yes_no",
                    "label": "Werden die Beschwerden besser, wenn Sie nicht arbeiten "
                             "(z. B. am arbeitsfreien Wochenende oder im Urlaub)?",
                    "required": True,
                    "show_if": {"id": "beschwerden_vorhanden", "in": ["yes"]},
                },
                {
                    "id": "infekt_mehrwoechig",
                    "type": "yes_no",
                    "label": "Hatten Sie in letzter Zeit eine Atemwegserkrankung "
                             "(z. B. Bronchitis), die mehrere Wochen angedauert hat?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Allergien und Vorerkrankungen ──────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Allergien & Vorerkrankungen",
            "subtitle": "Bekannte Allergien und Erkrankungen der Atemwege",
            "questions": [
                {
                    "id": "rhinitis_allergisch",
                    "type": "yes_no",
                    "label": "Haben Sie saisonalen oder ärztlich festgestellten "
                             "allergischen Schnupfen (Heuschnupfen) oder eine allergische "
                             "Bindehautentzündung – auch als Dauerbeschwerden?",
                    "required": True,
                },
                {
                    "id": "asthma",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen Asthma bronchiale festgestellt?",
                    "required": True,
                    "followup": {"id": "asthma_desc", "type": "text",
                                 "label": "Seit wann, und welche Medikamente nehmen Sie "
                                          "dagegen?", "when": "yes"},
                },
                {
                    "id": "asthma_symptome",
                    "type": "yes_no",
                    "label": "Haben Sie trotz Behandlung weiterhin Asthma-Beschwerden "
                             "(z. B. Atemnot, pfeifende Atmung, nächtlicher Husten)?",
                    "required": True,
                    "show_if": {"id": "asthma", "in": ["yes"]},
                },
                {
                    "id": "neurodermitis",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen ärztlich ein atopisches Ekzem "
                             "(Neurodermitis) festgestellt?",
                    "required": True,
                },
                {
                    "id": "allergie_beruflich",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Allergie gegen Stoffe aus Ihrem "
                             "Arbeitsbereich festgestellt (z. B. Mehl, Tierhaare, Latex), "
                             "oder haben Sie allergische Beschwerden durch Arbeitsstoffe?",
                    "required": True,
                    "followup": {"id": "allergie_beruflich_desc", "type": "text",
                                 "label": "Gegen welche Stoffe?", "when": "yes"},
                },
                {
                    "id": "copd_emphysem",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine chronische Bronchitis, COPD "
                             "(dauerhafte Verengung der Atemwege) oder ein Lungenemphysem "
                             "(Überblähung der Lunge) festgestellt?",
                    "required": True,
                },
                {
                    "id": "lunge_sonstig",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine andere Erkrankung der Lunge "
                             "(z. B. Lungenfibrose, Sarkoidose, Tuberkulose)?",
                    "required": True,
                    "followup": {"id": "lunge_sonstig_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "hyperreagibilitaet",
                    "type": "yes_no",
                    "label": "Reagieren Ihre Atemwege überempfindlich auf Reize wie kalte "
                             "Luft, Staub, Rauch, Parfüm oder Anstrengung (Hustenreiz, "
                             "Engegefühl)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Raucheranamnese – Rauchen ist die häufigste Ursache der COPD",
            "questions": [
                {
                    "id": "rauchstatus",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "frueher", "label": "Früher geraucht, jetzt nicht mehr"},
                        {"value": "aktuell", "label": "Ja, ich rauche zurzeit"},
                    ],
                    "followup": {"id": "rauchstatus_desc", "type": "text",
                                 "label": "Wie viel etwa pro Tag, und seit wann?",
                                 "when": "aktuell"},
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
    {"wenn": {"asthma_symptome": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Obstruktive Atemwegserkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Asthma bronchiale mit trotz Behandlung anhaltenden Beschwerden "
               "(persistierende Symptomatik).",
     "konsequenz": "Manifeste obstruktive Atemwegserkrankung mit persistierender "
                   "Symptomatik: dauernde gesundheitliche Bedenken prüfen. Bei "
                   "Nachuntersuchung nur dann keine dauernden Bedenken, wenn Maßnahmen "
                   "nach 2.1.3 zu Beschwerdefreiheit oder guter Symptomkontrolle führen. "
                   "Pneumologische Objektivierung (Spirometrie, ggf. Ergänzungs"
                   "untersuchung 1.2.3); BK-Verdachtsanzeige (Nrn. 4301/4302) erwägen."},
    {"wenn": {"copd_emphysem": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Obstruktive Atemwegserkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Chronisch obstruktive Lungenerkrankung bzw. Lungenemphysem angegeben.",
     "konsequenz": "COPD und Lungenemphysem zählen zu den Erkrankungen, die dauernde "
                   "gesundheitliche Bedenken begründen: Schweregrad objektivieren "
                   "(Spirometrie, erweiterte Lungenfunktionsdiagnostik nach 1.2.3). Nur "
                   "bei weniger ausgeprägter Erkrankung Aufnahme/Fortsetzung unter den "
                   "Voraussetzungen nach 2.1.3 prüfen (Schutzmaßnahmen, optimierte PSA, "
                   "verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"lunge_sonstig": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Lungenerkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Sonstige Lungenerkrankung (z. B. Lungengerüsterkrankung) angegeben.",
     "konsequenz": "Erhebliche Erkrankungen der Lungen (z. B. Lungengerüsterkrankungen) "
                   "begründen dauernde gesundheitliche Bedenken: Vorbefunde einholen, "
                   "Lungenfunktion prüfen, ggf. Röntgen-Thorax indikationsbezogen (1.2.3); "
                   "Ausprägung ärztlich bewerten, bei geringer Ausprägung Voraussetzungen "
                   "nach 2.1.3 prüfen."},
    {"wenn": {"allergie_beruflich": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Berufsallergie",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Allergie bzw. allergische Beschwerden gegenüber berufsspezifischen "
               "Stoffen angegeben.",
     "konsequenz": "Bei symptomatischer Typ-I-Sensibilisierung der oberen und/oder "
                   "unteren Atemwege auf berufsspezifische Allergene bestehen dauernde "
                   "gesundheitliche Bedenken; BK-Verdachtsanzeige erwägen. "
                   "Sensibilisierung objektivieren (arbeitsplatzbezogene Allergie"
                   "diagnostik nach 1.2.3). Bei Nachuntersuchung prüfen, ob Maßnahmen "
                   "nach 2.1.3 zu Beschwerdefreiheit oder Symptomkontrolle führen."},
    # ── Befristete Bedenken, vorzeitige Nachuntersuchung (1.1, 2.1.2) ─────
    {"wenn": {"infekt_mehrwoechig": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorübergehende Überempfindlichkeit",
     "quelle": "Abschnitte 1.1 und 2.1.2 (Befristete gesundheitliche Bedenken)",
     "befund": "Mehrwöchige Atemwegserkrankung in letzter Zeit angegeben.",
     "konsequenz": "Vorübergehende Überempfindlichkeit der Atemwege möglich (z. B. nach "
                   "bronchopulmonalem Infekt): befristete gesundheitliche Bedenken "
                   "erwägen, da schon niedrige Konzentrationen inhalativer Agentien "
                   "verschlimmern können. Vorzeitige Nachuntersuchung nach 1.1 ansetzen "
                   "und nach Abklingen erneut beurteilen."},
    {"wenn": {"zusammenhang_vermutung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Proband vermutet einen Zusammenhang zwischen Erkrankung und Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung veranlassen (1.1); Beschwerden und "
                   "Exposition dokumentieren, weiterführende Diagnostik nach 1.2.3 "
                   "einleiten."},
    # ── Arbeitsplatzbezogene Beschwerden (1.2.1, 1.2.3, 3.2) ──────────────
    {"wenn": {"beschwerden_arbeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezogene Beschwerden",
     "quelle": "Abschnitte 1.1, 1.2.1 und 1.2.3",
     "befund": "Beschwerden treten vermehrt am Arbeitsplatz auf.",
     "konsequenz": "Weiterführende Diagnostik durch einen arbeitsmedizinisch, "
                   "allergologisch und pneumologisch erfahrenen Arzt: arbeitsplatz- bzw. "
                   "tätigkeitsspezifische Allergiediagnostik sowie PEF- oder FEV1-Messung "
                   "über 3–6 Wochen mindestens viermal täglich vor, während und nach der "
                   "Arbeit (auch an expositionsfreien Tagen) mit Dokumentation von "
                   "Messwerten, Exposition, Beschwerden und Therapie. Vorzeitige "
                   "Nachuntersuchung nach 1.1."},
    {"wenn": {"besserung_karenz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezogene Beschwerden",
     "quelle": "Abschnitte 3.2 (Beschwerden, Diagnostik)",
     "befund": "Besserung der Beschwerden bei Arbeitskarenz (Wochenende/Urlaub) angegeben.",
     "konsequenz": "Expositionsabhängigkeit spricht für eine berufsbedingte "
                   "Inhalationsallergie: Sensibilisierungsnachweis mittels Hauttest oder "
                   "In-vitro-Test, serielle Lungenfunktionsmessungen bei der Arbeit und "
                   "an arbeitsfreien Tagen; BK-Verdachtsanzeige erwägen."},
    {"wenn": {"beschwerden_art": ["atembeschwerden", "husten"]},
     "schwere": "pruefen",
     "bereich": "Untere Atemwege",
     "quelle": "Abschnitt 1.2.3 (Ergänzungsuntersuchung)",
     "befund": "Atembeschwerden bzw. Husten angegeben.",
     "konsequenz": "Ergänzungsuntersuchung nach 1.2.3: erweiterte Lungenfunktions"
                   "diagnostik, in begründeten Fällen Atemwegswiderstände ganzkörper"
                   "plethysmographisch, Prüfung auf bronchiale Hyperreagibilität gemäß "
                   "Anhang 1; Röntgen-Thorax nur indikationsbezogen. In Abhängigkeit von "
                   "Beschwerdebild und Exposition an exogen-allergische Alveolitis oder "
                   "Byssinose denken."},
    {"wenn": {"beschwerden_art": ["atembeschwerden", "husten"]},
     "wenn_nicht": {"rauchstatus": ["aktuell", "frueher"]},
     "schwere": "pruefen",
     "bereich": "Erstmanifestation bei Nichtrauchern",
     "quelle": "Abschnitt 3.2 (Diagnostik)",
     "befund": "Atemwegsbeschwerden bei einer Person, die nie geraucht hat.",
     "konsequenz": "Die Erstmanifestation einer obstruktiven Atemwegserkrankung bei "
                   "Nichtrauchern ist Anlass zu weiterführender Diagnostik: "
                   "Sensibilisierungsnachweis (Hauttest/In-vitro), Lungenfunktions"
                   "messungen bei der Arbeit und an arbeitsfreien Tagen; arbeitsplatz"
                   "bezogene Inhalationstests nur durch erfahrene Untersucher."},
    # ── Atopie und Hyperreagibilität (Abschnitt 2.1.3) ────────────────────
    {"wenn": {"neurodermitis": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atopische Disposition",
     "quelle": "Abschnitt 2.1.3 (Keine Bedenken unter bestimmten Voraussetzungen)",
     "befund": "Ärztlich diagnostiziertes atopisches Ekzem (Neurodermitis).",
     "konsequenz": "Erkrankung aus dem atopischen Formenkreis: Aufnahme/Fortsetzung der "
                   "Tätigkeit nur unter bestimmten Voraussetzungen – Einsatz an "
                   "Arbeitsplätzen mit geringerer Konzentration, optimierte PSA, "
                   "verkürzte Nachuntersuchungsfristen, Teilnahme an berufsgenossen"
                   "schaftlich anerkannten Präventionsprogrammen."},
    {"wenn": {"rhinitis_allergisch": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atopische Disposition",
     "quelle": "Abschnitte 1.2.1 und 2.1.3",
     "befund": "Saisonale bzw. allergisch gesicherte Rhinitis/Konjunktivitis angegeben.",
     "konsequenz": "Allergiediagnostik (Hauttest/spezifisches IgE) auf berufsspezifische "
                   "und kreuzreagierende Umweltallergene (z. B. Getreidepollen, "
                   "Tierhaare). Bei chronischer Konjunktivitis oder Rhinitis "
                   "Voraussetzungen nach 2.1.3 prüfen (Schutzmaßnahmen, optimierte PSA, "
                   "verkürzte Nachuntersuchungsfristen, Präventionsprogramme)."},
    {"wenn": {"hyperreagibilitaet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bronchiale Hyperreagibilität",
     "quelle": "Abschnitte 1.2.3 und 2.1.3",
     "befund": "Überempfindliche Reaktion der Atemwege auf unspezifische Reize angegeben.",
     "konsequenz": "Unspezifische bronchiale Hyperreagibilität abklären: Prüfung gemäß "
                   "Anhang 1 »Lungenfunktionsprüfung« (z. B. Methacholintest). Aufnahme/"
                   "Fortsetzung der Tätigkeit nur unter den Voraussetzungen nach 2.1.3; "
                   "beachten, dass auch schwächer irritative Stoffe (z. B. Lösungsmittel) "
                   "Symptome auslösen können (3.1.1)."},
    {"wenn": {"asthma": ["yes"]},
     "wenn_nicht": {"asthma_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Obstruktive Atemwegserkrankung",
     "quelle": "Abschnitt 2.1.3 (Keine Bedenken unter bestimmten Voraussetzungen)",
     "befund": "Asthma bronchiale ohne aktuell anhaltende Beschwerden angegeben.",
     "konsequenz": "Weniger ausgeprägte bzw. gut kontrollierte Erkrankung: prüfen, ob "
                   "Aufnahme/Fortsetzung der Tätigkeit unter bestimmten Voraussetzungen "
                   "möglich ist (technische/organisatorische Schutzmaßnahmen, optimierte "
                   "PSA, verkürzte Nachuntersuchungsfristen, Präventionsprogramme); "
                   "Lungenfunktion engmaschig kontrollieren."},
    # ── Beratung und Arbeitsschutz (Abschnitte 2.2, 3.1.1) ────────────────
    {"wenn": {"rauchstatus": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung: Zigarettenrauchen ist die häufigste Ursache der COPD; die "
                   "Aufgabe des inhalativen Tabakkonsums verbessert nachweislich die "
                   "Lungenfunktion. Auf die Möglichkeit einer erfolgreichen "
                   "Entwöhnungsbehandlung hinweisen."},
    {"wenn": {"schutzmassnahmen": ["keine", "unbekannt"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 2 und 2.2",
     "befund": "Keine besonderen Schutzmaßnahmen bekannt bzw. vorhanden.",
     "konsequenz": "Beratung zur Benutzung persönlicher Schutzausrüstung entsprechend der "
                   "Arbeitsplatzsituation. Ergeben sich Hinweise, dass die Gefährdungs"
                   "beurteilung aktualisiert werden muss, Mitteilung an den Arbeitgeber "
                   "unter Wahrung der schutzwürdigen Belange des Untersuchten."},
    {"wenn": {"stoffgruppen": ["isocyanate"]},
     "schwere": "hinweis",
     "bereich": "Stoffspezifischer Grundsatz",
     "quelle": "Abschnitt 3.1.1 (Vorkommen, Gefahrenquellen)",
     "befund": "Tätigkeit mit Isocyanaten angegeben.",
     "konsequenz": "Zusätzlich den DGUV Grundsatz G 27 »Isocyanate« anwenden (inkl. der "
                   "dort vorgesehenen speziellen Untersuchungen)."},
]
