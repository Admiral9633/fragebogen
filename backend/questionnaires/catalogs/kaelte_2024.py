# -*- coding: utf-8 -*-
"""
Kältearbeiten – DGUV Empfehlung 2024.

Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und
Untersuchungen, Empfehlung "Kältearbeiten" (E KLT, Fassung Januar 2022),
Ausgabe 2024, S. 860–873.

Anlass: Pflichtvorsorge bei Tätigkeiten mit extremer Kältebelastung
(–25 °C und kälter) nach ArbMedVV; Wunschvorsorge ist zu ermöglichen.
Fristen richten sich nach AMR 2.1 (keine anlassspezifische Fristentabelle
mehr wie im alten G 21). Untersuchungen erfolgen nach ärztlichem Ermessen
und nur mit Einverständnis der versicherten Person.
"""

SLUG = "kaelte-2024"

CATALOG = {
    "version": 2,
    "title": "Kältearbeiten (DGUV Empfehlung 2024)",
    "basis": (
        "DGUV Empfehlungen für arbeitsmedizinische Beratungen und "
        "Untersuchungen, Empfehlung „Kältearbeiten“ (E KLT, Fassung "
        "Januar 2022), Ausgabe 2024, S. 860–873"
    ),
    "sections": [
        # ── 1 ─────────────────────────────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kälteexposition",
            "subtitle": "Angaben zu Ihrer Arbeit in extremer Kälte (–25 °C und kälter)",
            "questions": [
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge für "
                             "Kältearbeiten oder eine weitere Vorsorge?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge (vor oder kurz nach Aufnahme der Tätigkeit)"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich arbeite bereits in der Kälte)"},
                    ],
                },
                {
                    "id": "arbeitsbereiche",
                    "type": "multi_choice",
                    "label": "In welchen kalten Bereichen arbeiten Sie oder sollen Sie arbeiten?",
                    "hint": "Gemeint sind Räume mit technisch erzeugter Kälte von –25 °C und kälter "
                            "(auch Reparaturarbeiten und Kommissionierung).",
                    "required": True,
                    "options": [
                        {"value": "kuehlraum", "label": "Kühlräume"},
                        {"value": "gefrierraum", "label": "Gefrierräume / Tiefkühllager"},
                        {"value": "gefriertrockenraum", "label": "Gefriertrockenräume"},
                        {"value": "versuchskammer", "label": "Tieftemperatur-Versuchskammern"},
                        {"value": "sonstig", "label": "Andere kalte Arbeitsbereiche"},
                    ],
                },
                {
                    "id": "aufenthaltsdauer",
                    "type": "choice",
                    "label": "Wie lange halten Sie sich üblicherweise am Stück im Kältebereich auf?",
                    "hint": "Als kurzzeitig gilt ein Aufenthalt unter 15 Minuten zu Kontrollzwecken "
                            "oder zum Geben von Anweisungen – mit Kälteschutzkleidung.",
                    "required": True,
                    "options": [
                        {"value": "unter15", "label": "Nur kurz: unter 15 Minuten (z. B. Kontrollgänge)"},
                        {"value": "ueber15", "label": "Länger als 15 Minuten am Stück"},
                    ],
                },
                {
                    "id": "zusatzbelastung",
                    "type": "yes_no",
                    "label": "Verrichten Sie in der Kälte körperlich schwere Arbeiten "
                             "(z. B. Palettieren oder Kommissionieren schwerer Einheiten, "
                             "Reparaturen, Arbeiten mit Bohrhammer, Gerüstbau)?",
                    "required": True,
                },
                {
                    "id": "temp_wechsel",
                    "type": "yes_no",
                    "label": "Wechseln Sie bei der Arbeit häufig zwischen kalten und "
                             "warmen Temperaturbereichen?",
                    "hint": "Häufiger Temperaturwechsel verringert die Belastung nicht, "
                            "sondern erhöht sie.",
                    "required": True,
                },
                {
                    "id": "zugluft",
                    "type": "yes_no",
                    "label": "Sind Sie in der Kälte starker Luftbewegung ausgesetzt "
                             "(Zugluft, Ventilatoren, Fahrtwind)?",
                    "hint": "Starke Luftbewegung entzieht dem Körper vermehrt Wärme und Flüssigkeit.",
                    "required": True,
                },
                {
                    "id": "sauerstoffreduktion",
                    "type": "yes_no",
                    "label": "Arbeiten Sie in Räumen mit abgesenktem Sauerstoffgehalt "
                             "(Sauerstoffreduktionsanlage, z. B. zum Brandschutz)?",
                    "required": True,
                },
                {
                    "id": "hoehe_psa",
                    "type": "yes_no",
                    "label": "Arbeiten Sie in der Kälte in großer Höhe mit persönlicher "
                             "Schutzausrüstung gegen Absturz (Auffanggurt)?",
                    "required": True,
                },
                {
                    "id": "psa_kaelte",
                    "type": "yes_no",
                    "label": "Steht Ihnen vollständige Kälteschutzkleidung zur Verfügung "
                             "und tragen Sie diese bei der Arbeit?",
                    "required": True,
                },
                {
                    "id": "kontaktlinsen",
                    "type": "yes_no",
                    "label": "Tragen Sie weiche Kontaktlinsen?",
                    "hint": "Bei Arbeiten in extremer Kälte gilt ein Trageverbot für "
                            "weiche Kontaktlinsen.",
                    "required": True,
                },
            ],
        },
        # ── 2 ─────────────────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden bei Kälte",
            "subtitle": "Körperliche Reaktionen auf Kälte – bei der Arbeit oder in der Freizeit",
            "questions": [
                {
                    "id": "kaelte_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei Aufenthalt in der Kälte körperliche Beschwerden "
                             "(z. B. an Herz, Atmung, Haut oder Fingern)?",
                    "hint": "Wenn nein, überspringen Sie die folgenden Detailfragen automatisch.",
                    "required": True,
                },
                {
                    "id": "brust_atem_kaelte",
                    "type": "yes_no",
                    "label": "Bekommen Sie in der Kälte Engegefühl oder Schmerzen in der Brust, "
                             "Atemnot oder pfeifende Atmung?",
                    "hint": "Kälte kann reflektorisch Angina pectoris (Herzenge) oder einen "
                            "Bronchospasmus (Verkrampfung der Atemwege) auslösen.",
                    "required": True,
                    "show_if": {"id": "kaelte_beschwerden", "in": ["yes"]},
                },
                {
                    "id": "finger_weiss",
                    "type": "yes_no",
                    "label": "Werden Ihre Finger bei Kälte weiß oder blau und schmerzen dabei "
                             "(sogenannte „Weißfinger“, Raynaud-Syndrom)?",
                    "required": True,
                    "show_if": {"id": "kaelte_beschwerden", "in": ["yes"]},
                },
                {
                    "id": "taubheit_frostbeulen",
                    "type": "yes_no",
                    "label": "Haben Sie anhaltende Gefühlsstörungen oder Taubheit an den Fingern "
                             "oder Frostbeulen (Pernionen)?",
                    "required": True,
                    "show_if": {"id": "kaelte_beschwerden", "in": ["yes"]},
                },
                {
                    "id": "erfrierung",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal eine Erfrierung "
                             "(z. B. an Fingern, Zehen, Nase oder Ohren)?",
                    "required": True,
                    "followup": {
                        "id": "erfrierung_desc",
                        "type": "textarea",
                        "label": "Wann, an welcher Körperstelle, und sind Folgen geblieben?",
                        "when": "yes",
                    },
                },
                {
                    "id": "neue_symptome",
                    "type": "yes_no",
                    "label": "Sind seit der letzten Vorsorge neue Beschwerden bei der Arbeit "
                             "in der Kälte aufgetreten?",
                    "required": True,
                    "show_if": {"id": "vorsorge_anlass", "in": ["weitere"]},
                    "followup": {
                        "id": "neue_symptome_desc",
                        "type": "textarea",
                        "label": "Welche Beschwerden, und in welcher Situation treten sie auf?",
                        "when": "yes",
                    },
                },
            ],
        },
        # ── 3 ─────────────────────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Gesundheit",
            "subtitle": "Erkrankungen, die für Arbeiten in extremer Kälte wichtig sind",
            "questions": [
                {
                    "id": "herz_kreislauf",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung des Herzens oder des Kreislaufs "
                             "(z. B. koronare Herzkrankheit, Herzschwäche, "
                             "Herzrhythmusstörungen, hoher Blutdruck)?",
                    "required": True,
                    "followup": {
                        "id": "herz_kreislauf_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und sind Sie in Behandlung?",
                        "when": "yes",
                    },
                },
                {
                    "id": "atemwege",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der Atemwege oder der Lunge "
                             "(z. B. Asthma, COPD, chronische Bronchitis)?",
                    "required": True,
                    "followup": {
                        "id": "atemwege_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und wie wird sie behandelt?",
                        "when": "yes",
                    },
                },
                {
                    "id": "blut",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung des Blutes "
                             "(z. B. Blutarmut/Anämie, Gerinnungsstörung)?",
                    "required": True,
                },
                {
                    "id": "haut_durchblutung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Hauterkrankung, die die Durchblutung der Haut "
                             "beeinflusst?",
                    "required": True,
                },
                {
                    "id": "niere",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der Nieren oder der Harnwege?",
                    "required": True,
                },
                {
                    "id": "rheuma",
                    "type": "yes_no",
                    "label": "Haben Sie eine rheumatische Erkrankung oder ein bekanntes "
                             "Raynaud-Syndrom („Weißfingerkrankheit“)?",
                    "required": True,
                    "followup": {
                        "id": "rheuma_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und sind Sie in Behandlung?",
                        "when": "yes",
                    },
                },
                {
                    "id": "augen",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der äußeren Augen (z. B. trockene Augen/"
                             "Sicca-Syndrom, Flügelfell/Pterygium, häufige Bindehautentzündungen) "
                             "oder wurden Ihre Augen operiert?",
                    "required": True,
                    "followup": {
                        "id": "augen_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung bzw. welche Operation, und wann?",
                        "when": "yes",
                    },
                },
                {
                    "id": "kaelte_allergie",
                    "type": "yes_no",
                    "label": "Reagieren Sie überempfindlich auf Kälte – z. B. mit Nesselsucht/"
                             "Quaddeln (Kälteurtikaria) oder dunklem Urin nach Kälte "
                             "(Kältehämoglobinurie)?",
                    "required": True,
                    "followup": {
                        "id": "kaelte_allergie_desc",
                        "type": "textarea",
                        "label": "Wie äußert sich die Reaktion, und wurde sie ärztlich abgeklärt?",
                        "when": "yes",
                    },
                },
                {
                    "id": "anfallsleiden",
                    "type": "yes_no",
                    "label": "Hatten Sie jemals epileptische Anfälle oder ein anderes "
                             "Anfallsleiden?",
                    "required": True,
                    "followup": {
                        "id": "anfallsleiden_desc",
                        "type": "textarea",
                        "label": "Wann war der letzte Anfall, wie häufig treten Anfälle auf, "
                                 "und sind Sie in Behandlung?",
                        "when": "yes",
                    },
                },
                {
                    "id": "nervensystem",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung des Nervensystems mit spürbaren "
                             "Funktionsstörungen (z. B. Lähmungen, Gefühlsstörungen, "
                             "Gleichgewichtsstörungen)?",
                    "required": True,
                    "followup": {
                        "id": "nervensystem_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und welche Einschränkungen bestehen?",
                        "when": "yes",
                    },
                },
                {
                    "id": "abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Drogen oder Medikamenten?",
                    "required": True,
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {
                        "id": "medikamente_desc",
                        "type": "textarea",
                        "label": "Welche Medikamente, und wofür?",
                        "when": "yes",
                    },
                },
                {
                    "id": "gesundheit_veraendert",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Gesundheitszustand seit der letzten Vorsorge "
                             "wesentlich verändert (z. B. neue Herz-Kreislauf- oder "
                             "Atemwegserkrankung)?",
                    "required": True,
                    "show_if": {"id": "vorsorge_anlass", "in": ["weitere"]},
                    "followup": {
                        "id": "gesundheit_veraendert_desc",
                        "type": "textarea",
                        "label": "Was hat sich verändert?",
                        "when": "yes",
                    },
                },
            ],
        },
        # ── 4 ─────────────────────────────────────────────────────────────
        {
            "id": "einwilligung",
            "title": "Einwilligung",
            "subtitle": "Bestätigung Ihrer Angaben",
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
    # ── kritisch: Klärung VOR Einsatz ─────────────────────────────────────
    {"wenn": {"brust_atem_kaelte": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf / Atemwege",
     "quelle": "E KLT 6.3.2 / 7.4",
     "befund": "Engegefühl/Brustschmerz oder Atemnot bei Kälte – Verdacht auf "
               "reflektorisch ausgelöste Angina pectoris bzw. Bronchospasmus",
     "konsequenz": "Vor (weiterem) Einsatz in extremer Kälte ärztlich abklären: "
                   "Ruhe-EKG, ergänzend Ergometrie (Anhang 2 „Leitfaden Ergometrie“) "
                   "bzw. Lungenfunktionsprüfung (Anhang 1); prüfen, ob die Tätigkeit "
                   "im Einzelfall ohne gesundheitliche Gefährdung möglich ist."},
    {"wenn": {"kaelte_allergie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Kälteüberempfindlichkeit",
     "quelle": "E KLT 7.4",
     "befund": "Neigung zu Überempfindlichkeitsreaktionen bei Kälteeinwirkung "
               "(z. B. Kälteurtikaria, Kältehämoglobinurie) angegeben",
     "konsequenz": "Abklärung vor Einsatz zwingend (ggf. dermatologisch-allergologische "
                   "bzw. hämatologische Vorstellung, weitere Laboruntersuchungen nach 7.2.2). "
                   "Sind Maßnahmen nach 7.4.2/7.4.3 ohne Aussicht auf Erfolg, ist ein "
                   "Tätigkeitswechsel zu erwägen (7.4.4)."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Abhängigkeit",
     "quelle": "E KLT 7.4",
     "befund": "Alkohol-, Suchtmittel- oder Medikamentenabhängigkeit angegeben",
     "konsequenz": "Beurteilungsrelevantes Kriterium nach 7.4 – vor Einsatz klären "
                   "(Behandlungsstand, Abstinenz); bei fortbestehender Abhängigkeit "
                   "Tätigkeitswechsel erwägen (7.4.4), Mitteilung an den Arbeitgeber "
                   "nur mit Einwilligung der versicherten Person (§ 6 (4) ArbMedVV)."},

    # ── pruefen: Ergänzungsuntersuchung / Abklärung ───────────────────────
    {"wenn": {"herz_kreislauf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "E KLT 7.2.2 / 7.4.2 / 7.4.3",
     "befund": "Herz-Kreislauf-Erkrankung angegeben",
     "konsequenz": "Untersuchung mit Ruhe-EKG anbieten, ergänzend Ergometrie "
                   "(Anhang 2). Bei weniger ausgeprägter Erkrankung Maßnahmen nach "
                   "7.4.2 prüfen (Begrenzung der Belastungszeit, verlängerte "
                   "Aufwärmpausen, Arbeitsplatz mit geringerer Belastung – kein "
                   "Einsatz in wechselnden Temperaturbereichen); bei zu erwartender "
                   "Änderung des Schweregrades verkürzte Vorsorgefristen empfehlen (7.4.3)."},
    {"wenn": {"atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "E KLT 7.2.2 / 7.4",
     "befund": "Erkrankung der Atmungsorgane angegeben",
     "konsequenz": "Lungenfunktionsprüfung als ergänzende Untersuchung (Anhang 1 "
                   "„Leitfaden Lungenfunktionsprüfung“); prüfen, ob kältebedingter "
                   "Bronchospasmus droht und ob Maßnahmen nach 7.4.2 ausreichen."},
    {"wenn": {"blut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Blut",
     "quelle": "E KLT 7.2.2 / 7.4",
     "befund": "Erkrankung des Blutes angegeben",
     "konsequenz": "Blutbild im Rahmen der klinischen Untersuchung (7.2.2), ggf. "
                   "weitere Laboruntersuchungen; Relevanz für die Kältetoleranz "
                   "ärztlich bewerten."},
    {"wenn": {"haut_durchblutung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "E KLT 7.4",
     "befund": "Hauterkrankung mit Einfluss auf die Durchblutung angegeben",
     "konsequenz": "Hautbefund erheben; prüfen, ob lokale Kälteschäden "
                   "(Erfrierungen, Pernionen) drohen und ob PSA/organisatorische "
                   "Maßnahmen nach 7.4.2 ausreichen."},
    {"wenn": {"niere": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nieren / Harnwege",
     "quelle": "E KLT 7.2.2 / 7.4",
     "befund": "Erkrankung der Nieren oder ableitenden Harnwege angegeben",
     "konsequenz": "Urinstatus (Mehrfachteststreifen) und Kreatinin im Rahmen der "
                   "klinischen Untersuchung (7.2.2); Kältetauglichkeit unter "
                   "Berücksichtigung der Nierenfunktion beurteilen."},
    {"wenn": {"rheuma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Rheumatischer Formenkreis",
     "quelle": "E KLT 7.4",
     "befund": "Erkrankung des rheumatischen Formenkreises bzw. Raynaud-Syndrom angegeben",
     "konsequenz": "Krankheitsaktivität und Kälteauslösbarkeit klären (ggf. "
                   "rheumatologische Vorstellung); bei geringer Ausprägung Maßnahmen "
                   "nach 7.4.2 und verkürzte Fristen (7.4.3), sonst Tätigkeitswechsel "
                   "erwägen (7.4.4)."},
    {"wenn": {"finger_weiss": ["yes"]},
     "wenn_nicht": {"rheuma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Durchblutung der Hände",
     "quelle": "E KLT 6.3.2 / 7.4",
     "befund": "Weiß-/Blauverfärbung der Finger mit Schmerzen bei Kälte "
               "(Verdacht auf Raynaud-Syndrom), bislang ohne bekannte Diagnose",
     "konsequenz": "Abklärung eines Raynaud-Syndroms veranlassen (Anamnese vertiefen, "
                   "ggf. angiologische/rheumatologische Vorstellung), bevor die "
                   "Tätigkeit in extremer Kälte fortgesetzt wird."},
    {"wenn": {"augen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen",
     "quelle": "E KLT 7.4",
     "befund": "Erkrankung des äußeren Auges bzw. voroperierte Augen angegeben",
     "konsequenz": "Augenärztliches Konsil erforderlich (laut Empfehlung ausdrücklich "
                   "bei Sicca-Syndrom, Pterygium, häufigen Entzündungen der vorderen "
                   "Augenabschnitte und voroperierten Augen)."},
    {"wenn": {"anfallsleiden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Anfallsleiden",
     "quelle": "E KLT 7.4 / DGUV Information 250-001",
     "befund": "Epileptische Anfälle bzw. Anfallsleiden in der Vorgeschichte",
     "konsequenz": "Beurteilung in Abhängigkeit von Art, Häufigkeit, Prognose und "
                   "Behandlungsstand der Anfälle nach DGUV Information 250-001 "
                   "(„Berufliche Beurteilung bei Epilepsie und nach erstem "
                   "epileptischen Anfall“); neurologischen Befund anfordern."},
    {"wenn": {"nervensystem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "E KLT 7.4",
     "befund": "Erkrankung des zentralen oder peripheren Nervensystems mit "
               "Funktionsstörungen angegeben",
     "konsequenz": "Ausmaß der Funktionsstörungen klären (neurologische Vorstellung); "
                   "prüfen, ob Selbstrettungsfähigkeit und Kältewahrnehmung "
                   "eingeschränkt sind und ob Maßnahmen nach 7.4.2 ausreichen."},
    {"wenn": {"erfrierung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lokale Kälteschäden",
     "quelle": "E KLT 6.3.2 / 7.4.3",
     "befund": "Erfrierung in der Vorgeschichte",
     "konsequenz": "Betroffene Areale untersuchen (Durchblutung, Sensibilität); "
                   "erhöhte lokale Kälteempfindlichkeit berücksichtigen, Beratung zu "
                   "PSA gegen Kälte; verkürzte Vorsorgefristen erwägen (7.4.3)."},
    {"wenn": {"taubheit_frostbeulen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Chronische Kältewirkungen",
     "quelle": "E KLT 6.3.3",
     "befund": "Sensibilitätsminderung der Finger bzw. Pernionen (Frostbeulen) – "
               "mögliche chronische Kältewirkung",
     "konsequenz": "Sensibilität und Hautbefund der Hände prüfen; Zusammenhang mit "
                   "der Tätigkeit bewerten, Schutzmaßnahmen nach 7.4.2 veranlassen "
                   "und engmaschigere Vorsorge erwägen (7.4.3)."},
    {"wenn": {"psa_kaelte": ["no"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "E KLT 3 / 8.2, § 6 (4) ArbMedVV",
     "befund": "Kälteschutzkleidung fehlt oder wird nicht getragen",
     "konsequenz": "Hinweis auf unzureichende Arbeitsschutzmaßnahmen: dem Unternehmen "
                   "mitteilen und Schutzmaßnahmen vorschlagen; das Unternehmen muss "
                   "die Gefährdungsbeurteilung überprüfen."},
    {"wenn": {"neue_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Tätigkeitsspezifische Symptome",
     "quelle": "E KLT 7.1 (weitere Vorsorgen)",
     "befund": "Neue Beschwerden bei Kältearbeit seit der letzten Vorsorge",
     "konsequenz": "Beratung durch Untersuchung ergänzen (7.2), Ursache klären; "
                   "je nach Befund Maßnahmen nach 7.4.2, verkürzte Frist (7.4.3) "
                   "oder Tätigkeitswechsel (7.4.4) prüfen."},
    {"wenn": {"gesundheit_veraendert": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gesundheitsverlauf",
     "quelle": "E KLT 7.1 / 8.1",
     "befund": "Wesentliche Änderung des Gesundheitszustands seit der letzten Vorsorge",
     "konsequenz": "Aktualisierte Anamnese vertiefen und Untersuchung nach ärztlichem "
                   "Ermessen ergänzen (z. B. Ruhe-EKG, Lungenfunktion); Beurteilung "
                   "nach 7.4 neu vornehmen."},

    # ── hinweis: Beratungsthemen ─────────────────────────────────────────
    {"wenn": {"kontaktlinsen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Beratung",
     "quelle": "E KLT 7.1 / 8.1",
     "befund": "Trägt weiche Kontaktlinsen",
     "konsequenz": "Beratung: Trageverbot für weiche Kontaktlinsen bei Arbeiten in "
                   "extremer Kälte – Brille oder geeignete Alternativen verwenden; "
                   "zusätzlich zu vermehrter Flüssigkeitsaufnahme beraten."},
    {"wenn": {"sauerstoffreduktion": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinierte Belastung",
     "quelle": "E KLT 6.4",
     "befund": "Tätigkeit in sauerstoffreduzierter Atmosphäre (< 17 Vol.-%) zusätzlich "
               "zur extremen Kälte",
     "konsequenz": "Wechselwirkung der Belastungen beachten: Vorsorge mit dem Anlass "
                   "„Arbeiten in sauerstoffreduzierter Atmosphäre“ kombinieren und "
                   "kardiopulmonale Belastbarkeit besonders sorgfältig beurteilen "
                   "(Ergometrie erwägen)."},
]
