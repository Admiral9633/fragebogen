# -*- coding: utf-8 -*-
"""G 30 Hitzearbeiten – DGUV Grundsatz 2016 (Fassung Oktober 2014).

Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016,
G 30 „Hitzearbeiten“, S. 439–447 (1 Untersuchungen inkl. Fristen,
1.2 Untersuchungsprogramm, 2 Arbeitsmedizinische Beurteilung und Beratung
mit Kriterien 2.1.1–2.1.4, 3 Ergänzende Hinweise zur Hitzeexposition).
"""

SLUG = "g30-hitze-2016"

CATALOG = {
    "version": 2,
    "title": "G 30 Hitzearbeiten (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 30 „Hitzearbeiten“, Fassung Oktober 2014, S. 439–447",
    "sections": [
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Erstuntersuchung oder Nachuntersuchung nach G 30",
            "questions": [
                {
                    "id": "untersuchungsart",
                    "type": "choice",
                    "label": "Welche Untersuchung steht bei Ihnen an?",
                    "required": True,
                    "options": [
                        {"value": "erstuntersuchung", "label": "Erstuntersuchung (vor Aufnahme der Hitzearbeit)"},
                        {"value": "nachuntersuchung", "label": "Nachuntersuchung (ich arbeite bereits in der Hitze)"},
                        {"value": "vorzeitig", "label": "Vorzeitige Nachuntersuchung (z.B. nach längerer Krankheit oder auf eigenen Wunsch)"},
                    ],
                },
                {
                    "id": "alter_ueber_50",
                    "type": "yes_no",
                    "label": "Sind Sie älter als 50 Jahre?",
                    "hint": "Ab 50 Jahren sind kürzere Untersuchungsabstände vorgesehen "
                            "(alle 24 statt alle 60 Monate).",
                    "required": True,
                },
                {
                    "id": "letzte_untersuchung",
                    "type": "choice",
                    "label": "Wann war Ihre letzte Untersuchung nach G 30?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart",
                                "in": ["nachuntersuchung", "vorzeitig"]},
                    "options": [
                        {"value": "unter_24", "label": "Vor weniger als 24 Monaten (2 Jahren)"},
                        {"value": "24_60", "label": "Vor 24 bis 60 Monaten (2 bis 5 Jahren)"},
                        {"value": "ueber_60", "label": "Vor mehr als 60 Monaten (mehr als 5 Jahren)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        {
            "id": "taetigkeit",
            "title": "Ihre Tätigkeit in der Hitze",
            "subtitle": "Angaben zu Arbeitsplatz und Hitzebelastung",
            "questions": [
                {
                    "id": "hitze_taetigkeit",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie mit großer Hitze? "
                             "(Mehrfachauswahl möglich)",
                    "hint": "Gemeint sind Arbeitsplätze mit hoher Lufttemperatur, starker "
                            "Wärmestrahlung oder feucht-warmem Klima.",
                    "required": True,
                    "options": [
                        {"value": "stahl_huette", "label": "Stahlwerk / Hütte / Gießerei"},
                        {"value": "schmiede", "label": "Schmiede / Arbeiten mit glühenden Werkstücken"},
                        {"value": "behaelter_ofen", "label": "Arbeiten in oder an noch warmen Behältern, Kesseln oder Industrieöfen"},
                        {"value": "glas_keramik", "label": "Glas- oder Keramikindustrie"},
                        {"value": "kokerei_kraftwerk", "label": "Kokerei / Kraftwerk"},
                        {"value": "feuerwehr", "label": "Feuerwehr mit möglichem Einsatz am Brandherd"},
                        {"value": "sonstiges", "label": "Anderer Hitzearbeitsplatz"},
                    ],
                },
                {
                    "id": "exposition_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie üblicherweise am Stück in der Hitze, "
                             "ohne Pause in einem kühleren Bereich?",
                    "required": True,
                    "options": [
                        {"value": "unter_15", "label": "Weniger als 15 Minuten"},
                        {"value": "15_30", "label": "15 bis 30 Minuten"},
                        {"value": "31_60", "label": "31 bis 60 Minuten"},
                        {"value": "ueber_60", "label": "Mehr als 60 Minuten"},
                    ],
                },
                {
                    "id": "arbeitsschwere",
                    "type": "choice",
                    "label": "Wie schwer ist Ihre körperliche Arbeit in der Hitze meistens?",
                    "required": True,
                    "options": [
                        {"value": "leicht", "label": "Leicht (z.B. Kontrollgänge, Bedienen von Anlagen)"},
                        {"value": "mittel", "label": "Mittelschwer (z.B. ständige Hand- und Armarbeit)"},
                        {"value": "schwer", "label": "Schwer (z.B. Tragen schweren Materials, Schaufeln)"},
                        {"value": "sehr_schwer", "label": "Sehr schwer (sehr intensive Arbeit mit hohem Tempo)"},
                    ],
                },
                {
                    "id": "waermestrahlung",
                    "type": "yes_no",
                    "label": "Sind Sie bei der Arbeit starker Wärmestrahlung ausgesetzt "
                             "(z.B. durch glühendes Material, offene Öfen, Schmelzen)?",
                    "required": True,
                },
                {
                    "id": "schutzkleidung",
                    "type": "yes_no",
                    "label": "Tragen Sie bei der Hitzearbeit dicke oder stark isolierende "
                             "Schutzkleidung (z.B. Hitzeschutzanzug)?",
                    "required": True,
                },
                {
                    "id": "hitze_adaption",
                    "type": "choice",
                    "label": "Wie regelmäßig arbeiten Sie zurzeit in der Hitze?",
                    "hint": "Der Körper gewöhnt sich in etwa 2 bis 4 Wochen an Hitzearbeit "
                            "(Hitzeadaption). Nach 3 bis 4 Wochen ohne Hitzearbeit geht "
                            "diese Gewöhnung wieder verloren.",
                    "required": True,
                    "options": [
                        {"value": "adaptiert", "label": "Regelmäßig seit mehr als 4 Wochen (an Hitze gewöhnt)"},
                        {"value": "eingewoehnung", "label": "Erst seit weniger als 2 Wochen (noch in der Eingewöhnung)"},
                        {"value": "unterbrochen", "label": "Ich hatte gerade 3–4 Wochen oder länger keine Hitzearbeit (z.B. Urlaub, Krankheit)"},
                        {"value": "gelegentlich", "label": "Nur gelegentlich oder kurzzeitig (keine Gewöhnung zu erwarten)"},
                    ],
                },
            ],
        },
        {
            "id": "beschwerden",
            "title": "Beschwerden und Erkrankungen seit der letzten Untersuchung",
            "subtitle": "Wie Ihr Körper auf die Hitze reagiert",
            "questions": [
                {
                    "id": "hitze_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach der Arbeit in der Hitze Beschwerden wie "
                             "Schwächegefühl, Unwohlsein, Kopfschmerzen, Übelkeit oder "
                             "Kreislaufprobleme?",
                    "required": True,
                    "followup": {
                        "id": "hitze_beschwerden_desc",
                        "type": "textarea",
                        "label": "Welche Beschwerden, wie oft und in welchen Situationen?",
                        "when": "yes",
                        "required": False,
                    },
                },
                {
                    "id": "hitze_zwischenfall",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal einen Hitze-Zwischenfall, z.B. einen "
                             "Kreislaufkollaps (Hitzekollaps), Hitzekrämpfe oder einen "
                             "Hitzschlag?",
                    "required": True,
                    "followup": {
                        "id": "hitze_zwischenfall_desc",
                        "type": "textarea",
                        "label": "Was ist passiert, wann, und mussten Sie behandelt werden?",
                        "when": "yes",
                        "required": False,
                    },
                },
                {
                    "id": "mehrwoechige_erkrankung",
                    "type": "yes_no",
                    "label": "Waren Sie in letzter Zeit mehrere Wochen am Stück krank oder "
                             "körperlich beeinträchtigt?",
                    "required": True,
                    "followup": {
                        "id": "mehrwoechige_erkrankung_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und wie lange waren Sie krank?",
                        "when": "yes",
                        "required": False,
                    },
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie, dass gesundheitliche Beschwerden bei Ihnen mit "
                             "Ihrer Arbeit in der Hitze zusammenhängen?",
                    "required": True,
                },
                {
                    "id": "akut_krank",
                    "type": "yes_no",
                    "label": "Sind Sie zurzeit akut krank (z.B. Infekt, Fieber, Durchfall, "
                             "Erbrechen)?",
                    "hint": "Bei akuten Erkrankungen kann der Körper Hitze schlechter vertragen.",
                    "required": True,
                },
            ],
        },
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, die bei Hitzearbeit wichtig sein können "
                        "(Abschnitt 2.1.1 des Grundsatzes)",
            "questions": [
                {
                    "id": "herz_kreislauf",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung des Herzens oder des "
                             "Kreislaufs (z.B. Herzinfarkt, stark erhöhter oder zu niedriger "
                             "Blutdruck, Gefäßverkalkung/Arteriosklerose, Herzschwäche)?",
                    "required": True,
                    "followup": {
                        "id": "herz_kreislauf_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, seit wann, wie wird sie behandelt?",
                        "when": "yes",
                        "required": False,
                    },
                },
                {
                    "id": "atemwege",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der Lunge oder der Atemwege "
                             "(z.B. COPD, Asthma, Lungenemphysem, Staublunge, Tuberkulose)?",
                    "required": True,
                    "followup": {
                        "id": "atemwege_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und wie stark sind Sie im Alltag eingeschränkt?",
                        "when": "yes",
                        "required": False,
                    },
                },
                {
                    "id": "anfallsleiden",
                    "type": "yes_no",
                    "label": "Haben Sie ein Anfallsleiden (Epilepsie) oder hatten Sie schon "
                             "einmal einen Krampfanfall?",
                    "required": True,
                    "followup": {
                        "id": "anfallsleiden_desc",
                        "type": "textarea",
                        "label": "Wann war der letzte Anfall, und nehmen Sie Medikamente dagegen?",
                        "when": "yes",
                        "required": False,
                    },
                },
                {
                    "id": "nervensystem",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung des Nervensystems oder Folgen einer "
                             "Kopfverletzung (z.B. Schlaganfall, Lähmungen, "
                             "Schädel-Hirn-Verletzung)?",
                    "required": True,
                },
                {
                    "id": "stoffwechsel",
                    "type": "yes_no",
                    "label": "Haben Sie eine Stoffwechselerkrankung, insbesondere "
                             "Zuckerkrankheit (Diabetes mellitus)?",
                    "required": True,
                    "followup": {
                        "id": "stoffwechsel_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und wie wird sie behandelt (z.B. Insulin, Tabletten)?",
                        "when": "yes",
                        "required": False,
                    },
                },
                {
                    "id": "nieren",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der Nieren oder der Harnwege "
                             "(z.B. Nierensteine, Nierenschwäche, häufige Harnwegsinfekte)?",
                    "required": True,
                },
                {
                    "id": "magen_darm",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Magen-Darm-Erkrankung "
                             "(z.B. chronische Durchfälle, Morbus Crohn, Colitis ulcerosa)?",
                    "required": True,
                },
                {
                    "id": "leber",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Lebererkrankung "
                             "(z.B. Leberentzündung/Hepatitis, Leberzirrhose)?",
                    "required": True,
                },
                {
                    "id": "haut",
                    "type": "yes_no",
                    "label": "Haben Sie eine immer wiederkehrende oder großflächige "
                             "Hauterkrankung (z.B. schwere Neurodermitis oder Schuppenflechte)?",
                    "required": True,
                },
                {
                    "id": "auge_katarakt",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen ein Grauer Star (Katarakt, Trübung der "
                             "Augenlinse) festgestellt?",
                    "hint": "Wichtig bei Arbeit mit starker Wärmestrahlung.",
                    "required": True,
                },
                {
                    "id": "uebergewicht",
                    "type": "yes_no",
                    "label": "Haben Sie starkes Übergewicht (ausgeprägte Adipositas)?",
                    "required": True,
                },
                {
                    "id": "sucht",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Drogen oder Medikamenten?",
                    "required": True,
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein (z.B. entwässernde "
                             "Tabletten, Blutdruck- oder Herzmedikamente, Beruhigungsmittel)?",
                    "required": True,
                    "followup": {
                        "id": "medikamente_desc",
                        "type": "textarea",
                        "label": "Welche Medikamente nehmen Sie ein?",
                        "when": "yes",
                        "required": False,
                    },
                },
            ],
        },
        {
            "id": "einwilligung",
            "title": "Einwilligung",
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
                             "Verarbeitung meiner Daten zum Zweck der arbeitsmedizinischen "
                             "Untersuchung ein.",
                    "error": "Bitte akzeptieren Sie die Datenschutzhinweise.",
                    "required": True,
                },
            ],
        },
    ],
}

RULES = [
    # ── Dauernde gesundheitliche Bedenken (Kriterien 2.1.1) ─────────────────
    {"wenn": {"herz_kreislauf": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Erkrankung oder Veränderung des Herzens/Kreislaufs mit möglicher "
               "Einschränkung der Leistungs- oder Regulationsfähigkeit (z.B. Zustand "
               "nach Herzinfarkt, Blutdruckveränderung stärkeren Grades, "
               "Arteriosklerose)",
     "konsequenz": "Dauernde gesundheitliche Bedenken nach 2.1.1 erwägen; EKG mit "
                   "Brustwandableitung in Ruhe und unter Belastung (Ergometrie, "
                   "Anhang 2) durchführen. Bei weniger ausgeprägtem Befund nach 2.1.3 "
                   "prüfen: verbesserte Arbeitsplatzverhältnisse, verkürzte "
                   "Expositionszeit, optimierte PSA und verkürzte "
                   "Nachuntersuchungsfristen."},
    {"wenn": {"anfallsleiden": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Anfallsleiden",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Anfallsleiden (Epilepsie) bzw. Krampfanfall in der Vorgeschichte",
     "konsequenz": "Beurteilung in Abhängigkeit von Art, Häufigkeit, Prognose und "
                   "Behandlungsstand der Anfälle nach DGUV Information 250-001; bis "
                   "zur Klärung gesundheitliche Bedenken gegen Hitzearbeit; "
                   "neurologische Befunde beiziehen."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Suchterkrankung",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Alkohol-, Suchtmittel- oder Medikamentenabhängigkeit",
     "konsequenz": "Dauernde gesundheitliche Bedenken nach 2.1.1 erwägen; aktuelle "
                   "Behandlungs- und Abstinenzsituation klären. Bei zu erwartender "
                   "Wiederherstellung befristete Bedenken nach 2.1.2 aussprechen und "
                   "vorzeitige Nachuntersuchung festlegen."},

    # ── Erkrankungen mit Abklärungsbedarf (2.1.1–2.1.3) ─────────────────────
    {"wenn": {"atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atmungsorgane",
     "quelle": "Abschnitt 2.1.1 / 1.2.2",
     "befund": "Erkrankung der Atmungsorgane angegeben (z.B. COPD, Asthma, Emphysem, "
               "Pneumokoniose, Tuberkulose)",
     "konsequenz": "Grad der Funktionsbeeinträchtigung prüfen (kardiopulmonale "
                   "Funktionstüchtigkeit, 1.2.1); Röntgenaufnahme des Thorax (p.a.) "
                   "nur bei spezieller diagnostischer Fragestellung, vorhandenes Bild "
                   "(nicht älter als 1 Jahr) berücksichtigen. Bei stärkerer "
                   "Beeinträchtigung dauernde Bedenken nach 2.1.1."},
    {"wenn": {"nervensystem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Erkrankung oder Schädigung des zentralen/peripheren Nervensystems bzw. "
               "Folgen einer Schädel-Hirn-Verletzung",
     "konsequenz": "Wesentliche Funktionsstörungen abklären; bei ausgeprägtem Befund "
                   "dauernde Bedenken nach 2.1.1, sonst Voraussetzungen nach 2.1.3 "
                   "prüfen (Schutzmaßnahmen, verkürzte Fristen)."},
    {"wenn": {"stoffwechsel": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechsel",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Stoffwechselerkrankung, insbesondere Diabetes mellitus, angegeben",
     "konsequenz": "Prüfen, ob die Belastbarkeit stärker eingeschränkt ist "
                   "(Stoffwechseleinstellung, Behandlung); ggf. Bedenken nach 2.1.1 "
                   "oder Tätigkeit unter Voraussetzungen nach 2.1.3 mit verkürzten "
                   "Nachuntersuchungsfristen."},
    {"wenn": {"nieren": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nieren/Harnwege",
     "quelle": "Abschnitt 2.1.1 / 1.2.1",
     "befund": "Erkrankung der Nieren oder der harnableitenden Organe angegeben",
     "konsequenz": "Urinstatus (Mehrfachteststreifen, 1.2.1) durchführen und "
                   "Funktionstüchtigkeit der harnbildenden und harnabführenden Organe "
                   "besonders beachten; hoher Flüssigkeitsverlust durch Schwitzen "
                   "erhöht das Risiko."},
    {"wenn": {"magen_darm": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm",
     "quelle": "Abschnitt 2.1.1 / 2.1.2",
     "befund": "Chronische Magen-Darm-Erkrankung angegeben",
     "konsequenz": "Aktivität und Flüssigkeits-/Elektrolytverluste abklären; bei zu "
                   "erwartender Wiederherstellung befristete gesundheitliche Bedenken "
                   "nach 2.1.2 aussprechen und Nachuntersuchung nach Genesung."},
    {"wenn": {"leber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitt 2.1.1 / 1.2.1",
     "befund": "Chronische Lebererkrankung angegeben",
     "konsequenz": "Funktionstüchtigkeit der Leber besonders beachten (1.2.1); "
                   "Schweregrad klären, ggf. internistische Vorbefunde beiziehen; bei "
                   "ausgeprägtem Befund dauernde Bedenken nach 2.1.1."},
    {"wenn": {"haut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Chronisch rezidivierende oder generalisierte Hauterkrankung angegeben",
     "konsequenz": "Beeinträchtigung der Schweißabgabe und Verträglichkeit der "
                   "Hitzeschutzkleidung prüfen; ggf. dermatologische Abklärung, sonst "
                   "Tätigkeit unter Voraussetzungen nach 2.1.3 (optimierte PSA, "
                   "verkürzte Expositionszeit)."},
    {"wenn": {"auge_katarakt": ["yes"], "waermestrahlung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen/Wärmestrahlung",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Grauer Star (Katarakt) bei Tätigkeit mit überwiegender "
               "Wärmestrahlungsexposition",
     "konsequenz": "Augenärztliche Abklärung veranlassen; bei überwiegender "
                   "Wärmestrahlungsexposition dauernde Bedenken nach 2.1.1 erwägen, "
                   "Abschirmung und Augenschutz beraten."},
    {"wenn": {"uebergewicht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Adipositas",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Ausgeprägte Adipositas (starkes Übergewicht) angegeben",
     "konsequenz": "Kardiopulmonale Belastbarkeit objektivieren (Ergometrie, 1.2.2); "
                   "eingeschränkte Entwärmung berücksichtigen, ggf. Tätigkeit nur "
                   "unter Voraussetzungen nach 2.1.3 (kürzere Expositionszeit, "
                   "verkürzte Nachuntersuchungsfristen)."},

    # ── Hitzespezifische Anamnese ───────────────────────────────────────────
    {"wenn": {"hitze_zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hitzeerkrankung in der Vorgeschichte",
     "quelle": "Abschnitt 3.2 / 1.2.1",
     "befund": "Frühere akute Hitzeerkrankung (Hitzekollaps, Hitzekrämpfe, Hitzschlag)",
     "konsequenz": "Umstände und Ursachen klären (Adaption, Flüssigkeitszufuhr, "
                   "Grunderkrankung); kardiopulmonale Funktionstüchtigkeit gezielt "
                   "untersuchen, individuelle Hitzetoleranz beurteilen, ggf. "
                   "verkürzte Nachuntersuchungsfrist festlegen."},
    {"wenn": {"hitze_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hitzespezifische Beschwerden",
     "quelle": "Abschnitt 1.2.1 / 2.2",
     "befund": "Beschwerden bei oder nach Hitzearbeit (Schwäche, Unwohlsein, "
               "Kopfschmerzen, Übelkeit, Kreislaufprobleme)",
     "konsequenz": "Im Rahmen der Anamnese besonders auf Funktionstüchtigkeit des "
                   "kardiopulmonalen Systems, der Leber und der harnbildenden Organe "
                   "achten (1.2.1); ergeben sich Hinweise auf unzureichenden "
                   "Arbeitsschutz, Mitteilung an den Arbeitgeber zur Aktualisierung "
                   "der Gefährdungsbeurteilung (2.2)."},
    {"wenn": {"akut_krank": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Akute Erkrankung",
     "quelle": "Abschnitt 3.1.1",
     "befund": "Aktuell akute Erkrankung – die Hitzetoleranz kann vermindert sein",
     "konsequenz": "Persönliche Befindlichkeit beachten, auch wenn keine "
                   "gesundheitlichen Bedenken geäußert werden; Hitzearbeit möglichst "
                   "erst nach Abklingen der akuten Erkrankung wieder aufnehmen."},
    {"wenn": {"hitze_adaption": ["eingewoehnung", "unterbrochen", "gelegentlich"]},
     "schwere": "hinweis",
     "bereich": "Hitzeadaption",
     "quelle": "Abschnitt 3.1.1",
     "befund": "Keine vollständige Hitzeadaption (Eingewöhnung, längere Unterbrechung "
               "oder nur gelegentliche Exposition)",
     "konsequenz": "Beratung: Eingewöhnungszeit von etwa 2 Wochen einhalten, "
                   "vollständige Adaption erst nach etwa 4 Wochen; nach 3–4 Wochen "
                   "ohne Hitzearbeit geht die Adaption verloren. Expositionszeit "
                   "anfangs begrenzen; bei kurzzeitiger/gelegentlicher Belastung ist "
                   "keine Adaption zu erwarten."},

    # ── Fristen und vorzeitige Nachuntersuchung (Abschnitt 1.1) ─────────────
    {"wenn": {"letzte_untersuchung": ["ueber_60"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1",
     "befund": "Letzte G 30-Untersuchung liegt mehr als 60 Monate zurück",
     "konsequenz": "Nachuntersuchungsfrist überschritten (Personen bis 50 Jahre: vor "
                   "Ablauf von 60 Monaten) – vollständige Nachuntersuchung jetzt "
                   "durchführen und nächste Frist nach Alter festlegen."},
    {"wenn": {"letzte_untersuchung": ["24_60"], "alter_ueber_50": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1",
     "befund": "Über 50 Jahre und letzte G 30-Untersuchung vor mehr als 24 Monaten",
     "konsequenz": "Für Personen über 50 Jahre gilt die Nachuntersuchungsfrist von "
                   "24 Monaten – Frist überschritten, Nachuntersuchung jetzt "
                   "durchführen und künftig alle 24 Monate einbestellen."},
    {"wenn": {"mehrwoechige_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1",
     "befund": "Mehrwöchige Erkrankung oder körperliche Beeinträchtigung",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt, wenn die Erkrankung "
                   "Anlass zu Bedenken gegen die Fortsetzung der Hitzearbeit geben "
                   "könnte; Bedenken gegen die Fortsetzung prüfen, ggf. befristete "
                   "Bedenken nach 2.1.2 bis zur Wiederherstellung."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1",
     "befund": "Beschäftigte Person vermutet einen Zusammenhang zwischen Erkrankung "
               "und Tätigkeit am Hitzearbeitsplatz",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen; Beschwerden gezielt "
                   "abklären und bei Hinweisen auf unzureichenden Arbeitsschutz den "
                   "Arbeitgeber zur Aktualisierung der Gefährdungsbeurteilung "
                   "informieren (2.2, Wahrung der schutzwürdigen Belange)."},
]
