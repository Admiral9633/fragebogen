# -*- coding: utf-8 -*-
"""G 41 Arbeiten mit Absturzgefahr – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze
für arbeitsmedizinische Untersuchungen, 7. Auflage 2016 (Gentner Verlag),
G 41 »Arbeiten mit Absturzgefahr« (Fassung Oktober 2014), S. 625–633."""

SLUG = "g41-absturz-2016"

CATALOG = {
    "version": 2,
    "title": "G 41 Arbeiten mit Absturzgefahr (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 7. Auflage 2016, "
             "G 41 »Arbeiten mit Absturzgefahr« (Fassung Oktober 2014), S. 625–633",
    "sections": [
        # ── 1 ─ Untersuchungsanlass & Fristen (Abschnitt 1.1) ──────────────
        {
            "id": "untersuchung",
            "title": "Untersuchungsanlass",
            "subtitle": "Angaben zu Ihrer G-41-Untersuchung",
            "questions": [
                {
                    "id": "untersuchungsart",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich?",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit "
                                                   "mit Absturzgefahr)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich wurde schon einmal "
                                                   "nach G 41 untersucht)"},
                    ],
                },
                {
                    "id": "alter",
                    "type": "choice",
                    "label": "Wie alt sind Sie?",
                    "hint": "Nach dem Grundsatz richten sich die Nachuntersuchungsfristen nach "
                            "dem Alter: bis zum 25. Lebensjahr nach 36 Monaten, über 25 bis "
                            "49 Jahre nach 24–36 Monaten, ab dem 50. Lebensjahr nach "
                            "12–18 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "unter25", "label": "Bis 25 Jahre"},
                        {"value": "25bis49", "label": "Über 25 bis 49 Jahre"},
                        {"value": "ab50", "label": "50 Jahre oder älter"},
                    ],
                },
                {
                    "id": "letzte_g41",
                    "type": "choice",
                    "label": "Wie lange liegt Ihre letzte G-41-Untersuchung zurück?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach"]},
                    "options": [
                        {"value": "unter12", "label": "Weniger als 12 Monate"},
                        {"value": "12bis24", "label": "12 bis 24 Monate"},
                        {"value": "24bis36", "label": "24 bis 36 Monate"},
                        {"value": "ueber36", "label": "Mehr als 36 Monate"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "vorzeitig_anlass",
                    "type": "multi_choice",
                    "label": "Trifft einer der folgenden Punkte seit der letzten Untersuchung "
                             "auf Sie zu?",
                    "hint": "Mehrfachauswahl möglich. Solche Anlässe können eine vorgezogene "
                            "Nachuntersuchung erforderlich machen.",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach"]},
                    "options": [
                        {"value": "laengere_krankheit", "label": "Ich war mehrere Wochen oder länger "
                                                                 "krank oder körperlich beeinträchtigt"},
                        {"value": "eigene_bedenken", "label": "Ich vermute selbst, dass meine Gesundheit "
                                                              "bei der Arbeit mit Absturzgefahr "
                                                              "gefährdet ist"},
                        {"value": "keine", "label": "Nichts davon"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit & Absturzgefährdung (Abschnitte 2, 3.1.1) ────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Absturzgefährdung",
            "subtitle": "Ihre Arbeit in der Höhe",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "einsatzbereiche",
                    "type": "multi_choice",
                    "label": "Wo bzw. wie arbeiten Sie mit Absturzgefahr?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "freileitungen", "label": "Frei- oder Fahrleitungen (z. B. Strommasten, Bahn)"},
                        {"value": "antennen_flutlicht", "label": "Antennenanlagen oder Flutlichtanlagen"},
                        {"value": "bruecken_tuerme", "label": "Brücken, Masten, Türme oder Schornsteine"},
                        {"value": "montage", "label": "Auf-, Um- oder Abbau freitragender Konstruktionen "
                                                      "(Stahlbau, Stahlbetonfertigteilbau, Holzbau)"},
                        {"value": "bergbau", "label": "Schächte und Blindschächte im Bergbau"},
                        {"value": "geruest_dach", "label": "Gerüstbau-, Dach- oder Fassadenarbeiten"},
                        {"value": "sonstiges", "label": "Andere Arbeiten mit Absturzgefahr"},
                    ],
                },
                {
                    "id": "staendig_gesichert",
                    "type": "choice",
                    "label": "Sind Sie bei diesen Arbeiten durchgehend gegen Absturz gesichert "
                             "(z. B. Geländer, Seitenschutz, Wände oder angelegte "
                             "Absturz-Schutzausrüstung)?",
                    "hint": "Bei ständiger Sicherung ist nach dem Grundsatz keine erhöhte "
                            "Absturzgefahr anzunehmen.",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "teilweise", "label": "Nur teilweise – zeitweise ungesichert"},
                        {"value": "nein", "label": "Nein"},
                    ],
                },
                {
                    "id": "koerperlich_schwer",
                    "type": "yes_no",
                    "label": "Ist Ihre Tätigkeit körperlich erheblich belastend (z. B. schweres "
                             "Tragen, langes Klettern oder Steigen)?",
                    "hint": "Bei erheblich belastender Tätigkeit sieht der Grundsatz eine "
                            "Belastungs-Untersuchung (Ergometrie) auch unter 40 Jahren vor.",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schwindel & Beschwerden (Abschnitt 1.2.1) ──────────────────
        {
            "id": "beschwerden",
            "title": "Schwindel & Beschwerden",
            "subtitle": "Gleichgewicht, Sehen und Hören",
            "questions": [
                {
                    "id": "schwindel",
                    "type": "yes_no",
                    "label": "Leiden Sie unter Schwindel oder Gleichgewichtsstörungen?",
                    "required": True,
                },
                {
                    "id": "schwindel_art",
                    "type": "multi_choice",
                    "label": "Wie äußert sich der Schwindel?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "schwindel", "in": ["yes"]},
                    "options": [
                        {"value": "schwank", "label": "Schwankschwindel – Gefühl zu schwanken"},
                        {"value": "dreh", "label": "Drehschwindel – alles dreht sich"},
                        {"value": "lift", "label": "Liftgefühl – wie in einem fahrenden Aufzug"},
                        {"value": "fallneigung", "label": "Fallneigung – Neigung umzufallen"},
                        {"value": "schwarzwerden", "label": "Schwarzwerden vor den Augen"},
                        {"value": "unsicherheit", "label": "Unsicherheit beim Gehen oder Stehen"},
                    ],
                },
                {
                    "id": "schwindel_chronisch",
                    "type": "yes_no",
                    "label": "Treten die Schwindelbeschwerden schon seit längerer Zeit immer "
                             "wieder anfallsartig auf?",
                    "required": True,
                    "show_if": {"id": "schwindel", "in": ["yes"]},
                },
                {
                    "id": "vegetativ",
                    "type": "multi_choice",
                    "label": "Hatten Sie im letzten Jahr eine der folgenden Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "schweiss", "label": "Plötzliche Schweißausbrüche ohne Anstrengung"},
                        {"value": "uebelkeit", "label": "Übelkeit oder Erbrechen ohne erkennbaren Grund"},
                        {"value": "kollaps", "label": "Kollaps – Zusammensacken oder kurze Bewusstlosigkeit"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "sehstoerungen",
                    "type": "multi_choice",
                    "label": "Haben Sie eine der folgenden Sehstörungen?",
                    "hint": "Gemeint sind Probleme, die auch mit Brille oder Kontaktlinsen "
                            "bestehen. Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "unschaerfe", "label": "Unscharfes Sehen"},
                        {"value": "doppelbilder", "label": "Doppelbilder"},
                        {"value": "tanzend", "label": "Tanzende oder verschwimmende Bilder"},
                        {"value": "gesichtsfeld", "label": "Ausfälle im Blickfeld (Gesichtsfeld)"},
                        {"value": "farbsehen", "label": "Probleme, Farben zu unterscheiden"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "ohrensymptome",
                    "type": "multi_choice",
                    "label": "Trifft einer der folgenden Punkte zu Ihren Ohren zu?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "ohrensausen", "label": "Ohrgeräusche wie Sausen oder Pfeifen (Tinnitus)"},
                        {"value": "hoerminderung", "label": "Ich höre schlecht – normale Gespräche sind "
                                                            "schwer zu verstehen"},
                        {"value": "ohr_op", "label": "Ich wurde am Ohr operiert"},
                        {"value": "keine", "label": "Nichts davon"},
                    ],
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen (Abschnitte 1.2.1, 2.1.1) ──────────────────
        {
            "id": "vorerkrankungen",
            "title": "Frühere & bestehende Erkrankungen",
            "subtitle": "Bitte auch länger zurückliegende Erkrankungen angeben",
            "questions": [
                {
                    "id": "hoehenangst",
                    "type": "choice",
                    "label": "Haben Sie Angst vor der Höhe (Höhenangst)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ja_behandelt", "label": "Ja, sie wurde oder wird behandelt"},
                        {"value": "ja_unbehandelt", "label": "Ja, ohne Behandlung"},
                    ],
                },
                {
                    "id": "psychisch",
                    "type": "yes_no",
                    "label": "Sind bei Ihnen seelische oder psychiatrische Erkrankungen bekannt – "
                             "auch früher (z. B. Depression, Angststörung, Psychose)?",
                    "required": True,
                    "followup": {"id": "psychisch_desc", "type": "text",
                                 "label": "Welche Erkrankung, und sind Sie in Behandlung?",
                                 "when": "yes"},
                },
                {
                    "id": "anfallsleiden",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen ein Anfallsleiden bekannt (z. B. Epilepsie, "
                             "Krampfanfälle)?",
                    "required": True,
                    "followup": {"id": "anfallsleiden_desc", "type": "text",
                                 "label": "Wann war der letzte Anfall, und werden Sie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "herz_kreislauf",
                    "type": "multi_choice",
                    "label": "Sind bei Ihnen Erkrankungen des Herzens oder des Kreislaufs bekannt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "rhythmus", "label": "Herzrhythmusstörungen (Herzstolpern, Herzrasen)"},
                        {"value": "insuffizienz", "label": "Herzschwäche (Herzinsuffizienz)"},
                        {"value": "infarkt", "label": "Herzinfarkt in der Vorgeschichte"},
                        {"value": "schlaganfall", "label": "Schlaganfall in der Vorgeschichte"},
                        {"value": "blutdruck", "label": "Stark erhöhter oder stark schwankender Blutdruck"},
                        {"value": "durchblutung", "label": "Durchblutungsstörungen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "diabetes",
                    "type": "choice",
                    "label": "Haben Sie Diabetes mellitus (Zuckerkrankheit)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "diaet", "label": "Ja, nur mit Ernährung/Bewegung behandelt"},
                        {"value": "tabletten", "label": "Ja, mit Tabletten behandelt"},
                        {"value": "insulin", "label": "Ja, mit Insulin behandelt"},
                    ],
                },
                {
                    "id": "hypoglykaemie",
                    "type": "yes_no",
                    "label": "Hatten Sie Unterzuckerungen (Hypoglykämien) während der Arbeit "
                             "oder mit Bewusstseinsstörungen?",
                    "required": True,
                    "show_if": {"id": "diabetes", "in": ["diaet", "tabletten", "insulin"]},
                },
                {
                    "id": "weitere_erkrankungen",
                    "type": "multi_choice",
                    "label": "Sind bei Ihnen weitere Erkrankungen aus dieser Liste bekannt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "sht_hws", "label": "Schwere Kopfverletzung (Schädel-Hirn-Trauma) "
                                                      "oder Verletzung der Halswirbelsäule"},
                        {"value": "nieren", "label": "Nierenerkrankung"},
                        {"value": "endokrin", "label": "Erkrankung der Schilddrüse, der Nebenschilddrüsen "
                                                       "oder der Nebennieren"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "bewegungsapparat",
                    "type": "yes_no",
                    "label": "Haben Sie eine erhebliche Einschränkung der Beweglichkeit, der "
                             "Kraft oder des Gefühls an Armen oder Beinen?",
                    "required": True,
                    "followup": {"id": "bewegungsapparat_desc", "type": "text",
                                 "label": "Welche Einschränkungen?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Medikamente & Genussmittel (Abschnitt 1.2.1) ───────────────
        {
            "id": "medikamente",
            "title": "Medikamente & Genussmittel",
            "subtitle": "Was Sie regelmäßig einnehmen oder konsumieren",
            "questions": [
                {
                    "id": "medikamente_regelmaessig",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "textarea",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
                {
                    "id": "medikamente_gruppen",
                    "type": "multi_choice",
                    "label": "Sind darunter Medikamente aus einer dieser Gruppen?",
                    "hint": "Mehrfachauswahl möglich. Im Zweifel bitte den Beipackzettel prüfen "
                            "oder das Medikament beim Termin mitbringen.",
                    "required": True,
                    "show_if": {"id": "medikamente_regelmaessig", "in": ["yes"]},
                    "options": [
                        {"value": "sedativ", "label": "Beruhigende oder müde machende Mittel "
                                                      "(z. B. Schlafmittel, starke Schmerzmittel)"},
                        {"value": "diuretika", "label": "Entwässerungsmittel (Diuretika)"},
                        {"value": "antibiotika", "label": "Bestimmte Antibiotika über längere Zeit "
                                                          "(Aminoglykoside, z. B. Gentamicin)"},
                        {"value": "antivertiginosa", "label": "Mittel gegen Schwindel (Antivertiginosa)"},
                        {"value": "keine", "label": "Keines davon"},
                    ],
                },
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "gelegentlich", "label": "Gelegentlich (z. B. am Wochenende)"},
                        {"value": "regelmaessig", "label": "Mehrmals pro Woche"},
                        {"value": "taeglich", "label": "(Fast) täglich"},
                    ],
                },
                {
                    "id": "abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "anderen Suchtmitteln oder Medikamenten?",
                    "required": True,
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
    # ── Fristen (Abschnitt 1.1) ────────────────────────────────────────────
    {"wenn": {"alter": ["ab50"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Alter 50 Jahre oder älter.",
     "konsequenz": "Ab dem 50. Lebensjahr Nachuntersuchungen bereits nach 12–18 Monaten "
                   "veranlassen (bis zum 25. Lebensjahr: 36 Monate, über 25 bis 49 Jahre: "
                   "24–36 Monate); nächsten Untersuchungstermin entsprechend vormerken."},
    {"wenn": {"vorzeitig_anlass": ["laengere_krankheit", "eigene_bedenken"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Mehrwöchige Erkrankung/körperliche Beeinträchtigung seit der letzten "
               "Untersuchung bzw. eigene gesundheitliche Bedenken angegeben.",
     "konsequenz": "Diese Untersuchung als vorzeitige Nachuntersuchung führen: gezielt klären, "
                   "ob die Erkrankung bzw. die vermutete Gefährdung Anlass zu Bedenken gegen "
                   "die weitere Ausübung der Tätigkeit mit Absturzgefahr gibt; Befunde der "
                   "zwischenzeitlichen Behandlung beiziehen."},
    # ── Höhenangst & Psyche (Abschnitte 2.1.1, 2.1.2, 3.1) ─────────────────
    {"wenn": {"hoehenangst": ["ja_unbehandelt"]},
     "schwere": "kritisch",
     "bereich": "Höhenangst",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Unbehandelte Höhenangst angegeben.",
     "konsequenz": "Unbehandelte Höhenangst begründet dauernde gesundheitliche Bedenken gegen "
                   "die Tätigkeit mit Absturzgefahr. Behandlung empfehlen; erst nach "
                   "erfolgreicher Behandlung Neubewertung, bis dahin allenfalls befristete "
                   "Bedenken nach 2.1.2 aussprechen."},
    {"wenn": {"hoehenangst": ["ja_behandelt"]},
     "schwere": "pruefen",
     "bereich": "Höhenangst",
     "quelle": "Abschnitte 2.1.2 und 3.1",
     "befund": "Behandelte Höhenangst angegeben.",
     "konsequenz": "Behandlungserfolg prüfen und dokumentieren. Bei zu erwartender Besserung "
                   "befristete gesundheitliche Bedenken mit erneuter Überprüfung in "
                   "einjährigem Abstand; nach vier Jahren ist eine Besserung in der Regel "
                   "nicht mehr zu erwarten (3.1)."},
    {"wenn": {"psychisch": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Psychische Erkrankung",
     "quelle": "Abschnitt 2.1.1 (psychiatrische/psychische Störungen)",
     "befund": "Seelische oder psychiatrische Erkrankung angegeben (auch zurückliegend).",
     "konsequenz": "Fachpsychiatrische Abklärung veranlassen: Störungen wesentlicher Art "
                   "begründen auch nach Abklingen dauernde gesundheitliche Bedenken, wenn ein "
                   "Rückfall nicht hinreichend sicher ausgeschlossen werden kann."},
    # ── Anfallsleiden & Bewusstlosigkeit (Abschnitte 1.2.1, 2.1.1) ─────────
    {"wenn": {"anfallsleiden": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Anfallsleiden",
     "quelle": "Abschnitt 2.1.1; DGUV Information 250-001",
     "befund": "Anfallsleiden (z. B. Epilepsie) angegeben.",
     "konsequenz": "Gesundheitliche Bedenken in Abhängigkeit von Art, Häufigkeit, Prognose und "
                   "Behandlungsstand der Anfälle: neurologische Stellungnahme vor Einsatz "
                   "einholen und nach DGUV Information 250-001 (»Berufliche Möglichkeiten von "
                   "Personen mit Epilepsie«) beurteilen; bis dahin keine Tätigkeit mit "
                   "Absturzgefahr."},
    {"wenn": {"vegetativ": ["kollaps"]},
     "schwere": "kritisch",
     "bereich": "Kollaps/Bewusstlosigkeit",
     "quelle": "Abschnitte 1.2.1 und 2.1.1",
     "befund": "Kollaps bzw. kurze Bewusstlosigkeit im letzten Jahr angegeben.",
     "konsequenz": "Vor (weiterem) Einsatz Ursache abklären: EKG, ggf. Ergometrie und "
                   "internistisch-neurologische Ergänzungsuntersuchung (1.2.3). Erkrankungen "
                   "mit eingeschränkter Kreislauf-Regulationsfähigkeit begründen gesundheitliche "
                   "Bedenken."},
    # ── Schwindel & Gleichgewicht (Abschnitte 1.2.2, 2.1.1) ────────────────
    {"wenn": {"schwindel_chronisch": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Gleichgewicht/Schwindel",
     "quelle": "Abschnitt 2.1.1 (chronische Schwindelanfälle)",
     "befund": "Chronisch-anfallsartige Schwindelbeschwerden angegeben.",
     "konsequenz": "Neurootologische Abklärung (elektronystagmographische Untersuchung) durch "
                   "einen neurootologisch versierten HNO-Arzt (1.2.3): chronische "
                   "Schwindelanfälle mit nachweisbaren vestibulookulären oder retinookulären "
                   "Augenbewegungsstörungen begründen dauernde gesundheitliche Bedenken."},
    {"wenn": {"schwindel": ["yes"]},
     "wenn_nicht": {"schwindel_chronisch": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gleichgewicht/Schwindel",
     "quelle": "Abschnitte 1.2.2 und 2.1.1",
     "befund": "Schwindel bzw. Gleichgewichtsstörungen angegeben.",
     "konsequenz": "Prüfung der Kopf-Körper-Gleichgewichtsfunktion: Stehversuch nach Romberg "
                   "und Tretversuch nach Unterberger/Fukuda (je 1 Minute), möglichst mit "
                   "quantitativer Dokumentation (Cranio-Corpo-Graphie). Grenzwerte nach 2.1.1 "
                   "beachten (Tretversuch: Lateralschwankung ab 20 cm bzw. Seitenabweichung "
                   "über 80° rechts/70° links; Stehversuch: Längsschwankung ab 12 cm, "
                   "Querschwankung ab 10 cm → dauernde Bedenken); ggf. neurootologische "
                   "Ergänzungsuntersuchung (1.2.3)."},
    # ── Sehen (Abschnitte 1.2.2, 2.1.1) ────────────────────────────────────
    {"wenn": {"sehstoerungen": ["tanzend"]},
     "schwere": "kritisch",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitt 2.1.1 (Sehstörungen)",
     "befund": "Tanzende oder verschwimmende Bilder angegeben.",
     "konsequenz": "Sehstörungen mit tanzenden oder verschwimmenden Bildern begründen dauernde "
                   "gesundheitliche Bedenken; vor jedem weiteren Einsatz augenärztliche und "
                   "neurootologische Abklärung (1.2.3)."},
    {"wenn": {"sehstoerungen": ["unschaerfe", "doppelbilder", "gesichtsfeld", "farbsehen"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 1.2.2 und 2.1.1",
     "befund": "Sehstörung angegeben (Unschärfe, Doppelbilder, Gesichtsfeld- oder "
               "Farbsehprobleme).",
     "konsequenz": "Sehtest einschließlich Farbsehen und Perimetrie durchführen. Bedenken bei "
                   "korrigierter Sehschärfe unter 0,7/0,7 bzw. beidäugig unter 0,8 in der "
                   "Ferne, Einschränkung des Gesichtsfeldes im 30°-Zentralbereich oder "
                   "Farbsinnstörung, sofern erhöhte Anforderungen an das Farbsehen "
                   "sicherheitsrelevant sind (mit dem Betrieb klären); ggf. augenärztliche "
                   "Abklärung."},
    # ── Hören & Ohren (Abschnitte 1.2.1, 1.2.2, 2.1.1) ─────────────────────
    {"wenn": {"ohrensymptome": ["ohrensausen", "hoerminderung", "ohr_op"]},
     "schwere": "pruefen",
     "bereich": "Ohren/Hörvermögen",
     "quelle": "Abschnitte 1.2.1, 1.2.2 und 2.1.1",
     "befund": "Ohrensausen, Hörminderung oder Zustand nach Ohroperation angegeben.",
     "konsequenz": "Hörprüfung durchführen: Hörvermögen unter 3 m Umgangssprache beiderseits "
                   "begründet gesundheitliche Bedenken. Nach Ohroperation und bei Ohrensausen "
                   "zusätzlich die Gleichgewichtsfunktion prüfen; ggf. neurootologisch "
                   "versierten HNO-Arzt hinzuziehen (1.2.3)."},
    # ── Herz-Kreislauf (Abschnitte 1.2.2, 2.1.1) ───────────────────────────
    {"wenn": {"herz_kreislauf": ["infarkt", "schlaganfall"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Zustand nach Herzinfarkt oder Schlaganfall angegeben.",
     "konsequenz": "Zustand nach Herzinfarkt oder Schlaganfall zählt zu den dauernden "
                   "gesundheitlichen Bedenken. Kardiologische bzw. neurologische Stellungnahme "
                   "einholen und prüfen, ob ausnahmsweise »keine Bedenken unter bestimmten "
                   "Voraussetzungen« (2.1.3: verkürzte Nachuntersuchungsfristen, spezifische "
                   "Auflagen) vertretbar sind."},
    {"wenn": {"herz_kreislauf": ["rhythmus", "insuffizienz", "blutdruck", "durchblutung"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 1.2.2 und 2.1.1",
     "befund": "Herz-Kreislauf-Erkrankung angegeben (Rhythmusstörung, Herzschwäche, "
               "Blutdruckveränderungen oder Durchblutungsstörungen).",
     "konsequenz": "EKG (12 Ableitungen) und Ergometrie durchführen: Erkrankungen mit "
                   "Einschränkung der Leistungs- oder Regulationsfähigkeit oder "
                   "Blutdruckveränderungen stärkeren Grades begründen gesundheitliche "
                   "Bedenken; ggf. kardiologische Ergänzungsuntersuchung (1.2.3)."},
    # ── Stoffwechsel & weitere Erkrankungen (Abschnitte 1.2, 2.1.1) ────────
    {"wenn": {"hypoglykaemie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Stoffwechsel",
     "quelle": "Abschnitt 2.1.1 (Stoffwechselkrankheiten)",
     "befund": "Tätigkeitsrelevante Unterzuckerungen (bei der Arbeit bzw. mit "
               "Bewusstseinsstörung) angegeben.",
     "konsequenz": "Medikamentös behandelter Diabetes mellitus mit tätigkeitsrelevanten "
                   "Hypoglykämien begründet dauernde gesundheitliche Bedenken. Diabetologische "
                   "Stellungnahme einholen; bis zur stabilen, hypoglykämiefreien Einstellung "
                   "keine Tätigkeit mit Absturzgefahr."},
    {"wenn": {"diabetes": ["tabletten", "insulin"]},
     "wenn_nicht": {"hypoglykaemie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechsel",
     "quelle": "Abschnitte 1.2.2, 2.1.1 und 2.1.3",
     "befund": "Medikamentös behandelter Diabetes mellitus ohne angegebene "
               "tätigkeitsrelevante Unterzuckerungen.",
     "konsequenz": "Stoffwechseleinstellung klären (Nüchtern-Blutzucker, Urinstatus, Befunde "
                   "der behandelnden Praxis). Bei stabiler Einstellung ohne "
                   "tätigkeitsrelevante Hypoglykämien und ohne Folgeerkrankungen keine "
                   "Bedenken unter bestimmten Voraussetzungen (2.1.3: verkürzte "
                   "Nachuntersuchungsfristen, spezifische Auflagen)."},
    {"wenn": {"weitere_erkrankungen": ["sht_hws", "nieren", "endokrin"]},
     "schwere": "pruefen",
     "bereich": "Weitere Vorerkrankungen",
     "quelle": "Abschnitte 1.2.1, 1.2.2 und 2.1.1",
     "befund": "Schädel-Hirn-/HWS-Trauma, Nierenerkrankung oder endokrine Erkrankung "
               "(Schilddrüse, Epithelkörperchen, Nebennieren) angegeben.",
     "konsequenz": "Gezielt abklären: nach Schädel-Hirn- oder HWS-Trauma neurologische "
                   "Abklärung; bei Nieren- und endokrinen Erkrankungen Kreatinin, Urinstatus "
                   "und Stoffwechsellage bewerten – Erkrankungen der Schilddrüse, der "
                   "Epithelkörperchen oder der Nebennieren können gesundheitliche Bedenken "
                   "begründen; in unklaren Fällen weitere Labordiagnostik bzw. fachärztliche "
                   "Ergänzungsuntersuchung (1.2.3)."},
    # ── Bewegungsapparat (Abschnitte 1.2.2, 2.1.1) ─────────────────────────
    {"wenn": {"bewegungsapparat": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Bewegungsapparat",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Erhebliche Einschränkung von Beweglichkeit, Kraft oder Sensibilität an Armen "
               "oder Beinen angegeben.",
     "konsequenz": "Erhebliche Einschränkung einer für die Tätigkeit wichtigen Gliedmaße "
                   "begründet dauernde gesundheitliche Bedenken. Funktion gezielt prüfen "
                   "(Ganzkörperstatus), ggf. orthopädische Abklärung; ist die sichere "
                   "Ausübung nicht gewährleistet, Tätigkeitswechsel empfehlen."},
    # ── Suchtmittel & Medikamente (Abschnitte 1.2.1, 2.1.1) ────────────────
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Suchtmittel",
     "quelle": "Abschnitt 2.1.1 (Abhängigkeit)",
     "befund": "Alkohol-, Suchtmittel- oder Medikamentenabhängigkeit angegeben "
               "(aktuell oder früher).",
     "konsequenz": "Abhängigkeit begründet dauernde gesundheitliche Bedenken. Suchtmedizinische "
                   "Abklärung; Wiedereinsatz allenfalls nach belegter stabiler Abstinenz und "
                   "dann nur mit verkürzten Nachuntersuchungsfristen bzw. Auflagen (2.1.3)."},
    {"wenn": {"medikamente_gruppen": ["sedativ", "diuretika", "antibiotika", "antivertiginosa"]},
     "schwere": "pruefen",
     "bereich": "Medikamente",
     "quelle": "Abschnitt 1.2.1 (Pharmaka)",
     "befund": "Einnahme von sedierenden Mitteln, Diuretika, aminoglykosidischen Antibiotika "
               "oder Antivertiginosa angegeben.",
     "konsequenz": "Medikation ärztlich bewerten: sedierende Mittel und Antivertiginosa können "
                   "Wachheit und Reaktionsfähigkeit, Diuretika den Kreislauf und "
                   "aminoglykosidische Antibiotika das Gleichgewichtsorgan beeinträchtigen. "
                   "Rücksprache mit den Behandelnden, ggf. Umstellung vor weiterem Einsatz "
                   "in der Höhe."},
]
