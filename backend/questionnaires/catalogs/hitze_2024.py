# -*- coding: utf-8 -*-
"""Hitzearbeiten – DGUV Empfehlung 2024 (Kurzbezeichnung E HTZ, Fassung Januar 2022).

Quelle: DGUV Empfehlungen zur arbeitsmedizinischen Vorsorge, Kapitel
"Hitzearbeiten", S. 838–859 (Anwendungsbereich, AMR 13.1-Tätigkeiten,
Hitzeadaption, Abschnitt 7.1 Eingangsberatung, 7.2 Untersuchung,
7.3 Fristen, 7.4 Beurteilungskriterien, 8 Abschließende Beratung).
"""

SLUG = "hitze-2024"

CATALOG = {
    "version": 2,
    "title": "Hitzearbeiten (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen zur arbeitsmedizinischen Vorsorge, 3. Auflage 2024, "
             "Kapitel „Hitzearbeiten“ (E HTZ), Fassung Januar 2022, S. 838–859",
    "sections": [
        {
            "id": "taetigkeit",
            "title": "Ihre Tätigkeit in der Hitze",
            "subtitle": "Angaben zu Arbeitsplatz, Hitzebelastung und Schutzmaßnahmen",
            "questions": [
                {
                    "id": "anlass",
                    "type": "choice",
                    "label": "Aus welchem Anlass sind Sie heute hier?",
                    "required": True,
                    "options": [
                        {"value": "erste_vorsorge", "label": "Erste Vorsorge (vor oder kurz nach Aufnahme der Hitzearbeit)"},
                        {"value": "weitere_vorsorge", "label": "Weitere Vorsorge (ich arbeite bereits in der Hitze)"},
                        {"value": "wunschvorsorge", "label": "Wunschvorsorge (auf meinen eigenen Wunsch)"},
                    ],
                },
                {
                    "id": "hitze_taetigkeit",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie mit großer Hitze? "
                             "(Mehrfachauswahl möglich)",
                    "hint": "Gemeint sind Arbeitsplätze mit hoher Wärmestrahlung, hoher "
                            "Temperatur oder feucht-warmem Klima.",
                    "required": True,
                    "options": [
                        {"value": "stahl_huette", "label": "Stahlwerk / Hütte / Gießerei (z.B. Pfannen, Hochofen, Stranggießanlage, Konverter)"},
                        {"value": "schmiede", "label": "Schmiede / Arbeiten mit glühenden Werkstücken"},
                        {"value": "schweissen_warm", "label": "Schweißen oder Flämmen an vorgewärmten, heißen Werkstücken"},
                        {"value": "behaelter_ofen", "label": "Arbeiten in noch warmen Behältern, Kesseln, Industrieöfen oder Trocknungsanlagen"},
                        {"value": "glas_keramik", "label": "Glas- oder Keramikindustrie (z.B. Heißreparaturen an Öfen und Wannen)"},
                        {"value": "kokerei_kraftwerk", "label": "Kokerei / Kraftwerk (z.B. Arbeiten auf der Ofendecke)"},
                        {"value": "feuerwehr", "label": "Feuerwehr mit möglichem Einsatz am Brandherd"},
                        {"value": "sauna_sonstiges", "label": "Sauna-Bereich oder anderer Hitzearbeitsplatz"},
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
                        {"value": "leicht", "label": "Leicht (z.B. Kontrollgänge, Bedienen von Anlagen, Kranführen)"},
                        {"value": "mittel", "label": "Mittelschwer (z.B. ständige Hand- und Armarbeit, Schieben leichter Karren)"},
                        {"value": "schwer", "label": "Schwer (z.B. Tragen schweren Materials, Schaufeln, Ofenmaurerarbeit)"},
                        {"value": "sehr_schwer", "label": "Sehr schwer (z.B. sehr intensive Arbeit mit hohem Tempo, Steigen auf Leitern und Rampen)"},
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
                             "Schutzkleidung (z.B. Hitzeschutzanzug, Feuerwehr-Schutzkleidung)?",
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
                {
                    "id": "fluessigkeit",
                    "type": "yes_no",
                    "label": "Können Sie während der Arbeit ausreichend trinken "
                             "(geeignete Getränke stehen bereit und Sie nutzen sie)?",
                    "required": True,
                },
                {
                    "id": "entwaermung",
                    "type": "yes_no",
                    "label": "Können Sie regelmäßig Pausen in einem kühleren Bereich machen "
                             "(sogenannte Entwärmungsphasen)?",
                    "required": True,
                },
            ],
        },
        {
            "id": "beschwerden",
            "title": "Beschwerden bei Hitzearbeit",
            "subtitle": "Wie Ihr Körper auf die Hitze reagiert",
            "questions": [
                {
                    "id": "hitze_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach der Arbeit in der Hitze Beschwerden wie "
                             "Schwächegefühl, Unwohlsein, Kopfschmerzen oder Übelkeit?",
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
                             "Kreislaufkollaps (Hitzekollaps), Hitzekrämpfe, eine "
                             "Hitzeerschöpfung oder einen Hitzschlag?",
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
                        "(Abschnitt 7.4 der DGUV Empfehlung)",
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
                             "Zuckerkrankheit (Diabetes mellitus) oder eine "
                             "Schilddrüsenerkrankung?",
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
                             "(z.B. Leberentzündung/Hepatitis, Fettleber mit Beschwerden, "
                             "Leberzirrhose)?",
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
                    "hint": "Wichtig bei Arbeit mit starker Wärmestrahlung: Sie kann auf Dauer "
                            "die Augenlinse schädigen (Berufskrankheit Nr. 2401).",
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
                             "Drogen oder Medikamenten, oder ein regelmäßig übermäßiger "
                             "Konsum?",
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
                             "Vorsorge ein.",
                    "error": "Bitte akzeptieren Sie die Datenschutzhinweise.",
                    "required": True,
                },
            ],
        },
    ],
}

RULES = [
    # ── Vorerkrankungen mit hoher Relevanz (Abschnitt 7.4 / 7.4.4) ──────────
    {"wenn": {"herz_kreislauf": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 7.4 / 7.4.4",
     "befund": "Erkrankung des Herzens oder des Kreislaufs mit möglicher Einschränkung "
               "der Leistungs- oder Regulationsfähigkeit angegeben (z.B. Zustand nach "
               "Herzinfarkt, Blutdruckveränderung stärkeren Grades, Arteriosklerose)",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Hitzearbeit klären: Belastungs-EKG "
                   "mit Brustwandableitung (Ergometrie, Anhang 2), Blutdruck-/Pulsmessung; "
                   "Schweregrad prüfen. Bei weniger ausgeprägtem Befund Maßnahmen nach "
                   "7.4.2 (Abschirmung, Expositionszeit begrenzen, geeignete PSA) und ggf. "
                   "verkürzte Fristen nach 7.4.3; sind diese ohne Aussicht auf Erfolg, "
                   "Tätigkeitswechsel nach 7.4.4 erwägen (Mitteilung an Arbeitgeber nur "
                   "mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"anfallsleiden": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Anfallsleiden",
     "quelle": "Abschnitt 7.4",
     "befund": "Anfallsleiden (Epilepsie) bzw. Krampfanfall in der Vorgeschichte",
     "konsequenz": "Beurteilung in Abhängigkeit von Art, Häufigkeit, Prognose und "
                   "Behandlungsstand der Anfälle nach DGUV Information 250-001 "
                   "(„Berufliche Beurteilung bei Epilepsie“) VOR Einsatz an "
                   "Hitzearbeitsplätzen; neurologische Befunde beiziehen. Erschwerte "
                   "Rettungsmöglichkeiten (Behälter, Öfen) besonders berücksichtigen."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Suchterkrankung",
     "quelle": "Abschnitt 7.4",
     "befund": "Abhängigkeit oder Missbrauch von Alkohol, Suchtmitteln oder Medikamenten",
     "konsequenz": "Klärung vor Einsatz: aktuelle Behandlungssituation und Abstinenz "
                   "erfragen, Leberwerte bestimmen; Ausübung der Tätigkeit ohne "
                   "gesundheitliche Gefährdung prüfen, ggf. Tätigkeitswechsel nach "
                   "7.4.4 erwägen."},

    # ── Vorerkrankungen mit Abklärungsbedarf (Abschnitt 7.4 / 7.2.2) ────────
    {"wenn": {"atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atmungsorgane",
     "quelle": "Abschnitt 7.4 / 7.2.2",
     "befund": "Erkrankung der Atmungsorgane angegeben (z.B. COPD, Asthma, Emphysem, "
               "Pneumokoniose, Tuberkulose)",
     "konsequenz": "Ausmaß der Funktionsbeeinträchtigung prüfen; Röntgenaufnahme des "
                   "Thorax (p.a.) nur bei spezieller diagnostischer Fragestellung, "
                   "vorhandene Aufnahme (nicht älter als 12 Monate) berücksichtigen. Bei "
                   "stärkerer Beeinträchtigung Maßnahmen nach 7.4.2/7.4.3 festlegen."},
    {"wenn": {"nervensystem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 7.4",
     "befund": "Erkrankung oder Schädigung des zentralen/peripheren Nervensystems bzw. "
               "Folgen einer Schädel-Hirn-Verletzung",
     "konsequenz": "Wesentliche Funktionsstörungen abklären (ggf. neurologische "
                   "Vorbefunde); prüfen, ob die Tätigkeit ohne gesundheitliche "
                   "Gefährdung möglich ist, sonst Maßnahmen nach 7.4.2."},
    {"wenn": {"stoffwechsel": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechsel",
     "quelle": "Abschnitt 7.4 / 7.2.2",
     "befund": "Stoffwechselerkrankung, insbesondere Diabetes mellitus, angegeben",
     "konsequenz": "Blutzucker bestimmen (klinische Untersuchung 7.2.2), Einschränkung "
                   "der Belastbarkeit prüfen; bei zu erwartender Änderung des "
                   "Schweregrades verkürzte Vorsorgefristen nach 7.4.3 festlegen."},
    {"wenn": {"nieren": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nieren/Harnwege",
     "quelle": "Abschnitt 7.4 / 7.2.2",
     "befund": "Erkrankung der Nieren oder der harnableitenden Organe angegeben",
     "konsequenz": "Urinstatus und Nierenwerte bestimmen (7.2.2); hoher "
                   "Flüssigkeitsverlust durch Schwitzen erhöht das Risiko – "
                   "Trinkverhalten beraten, Schweregrad ärztlich beurteilen."},
    {"wenn": {"magen_darm": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm",
     "quelle": "Abschnitt 7.4",
     "befund": "Chronische Magen-Darm-Erkrankung angegeben",
     "konsequenz": "Aktivität und Flüssigkeits-/Elektrolytverluste abklären; prüfen, ob "
                   "Hitzearbeit ohne Gefährdung möglich ist, ggf. Maßnahmen nach 7.4.2 "
                   "und verkürzte Fristen nach 7.4.3."},
    {"wenn": {"leber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitt 7.4 / 7.2.2",
     "befund": "Chronische Lebererkrankung angegeben",
     "konsequenz": "Leberwerte bestimmen (klinische Untersuchung 7.2.2), Schweregrad "
                   "beurteilen; ggf. Maßnahmen nach 7.4.2/7.4.3."},
    {"wenn": {"haut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 7.4",
     "befund": "Chronisch wiederkehrende oder großflächige Hauterkrankung angegeben",
     "konsequenz": "Beeinträchtigung der Schweißabgabe und Verträglichkeit von "
                   "Hitzeschutzkleidung prüfen; ggf. dermatologische Abklärung und "
                   "Maßnahmen nach 7.4.2 (PSA-Auswahl, Expositionsbegrenzung)."},
    {"wenn": {"auge_katarakt": ["yes"], "waermestrahlung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen/Wärmestrahlung",
     "quelle": "Abschnitt 7.4 / 6.3.3 / 6.5",
     "befund": "Grauer Star (Katarakt) bei Tätigkeit mit überwiegender "
               "Wärmestrahlungsexposition",
     "konsequenz": "Augenärztliche Abklärung veranlassen; möglicher Zusammenhang mit "
                   "Infrarotstrahlung (Berufskrankheit Nr. 2401 „Grauer Star durch "
                   "Wärmestrahlung“) prüfen und ggf. BK-Anzeige erwägen; "
                   "Strahlenschutz (Abschirmung, Schutzbrille) beraten."},
    {"wenn": {"uebergewicht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Adipositas",
     "quelle": "Abschnitt 7.4",
     "befund": "Ausgeprägte Adipositas (starkes Übergewicht) angegeben",
     "konsequenz": "Kardiopulmonale Belastbarkeit objektivieren (Ergometrie nach 7.2.2); "
                   "eingeschränkte Entwärmung berücksichtigen, ggf. Expositionszeit "
                   "begrenzen und verkürzte Fristen nach 7.4.3 festlegen."},

    # ── Hitzespezifische Beanspruchung und Anamnese (Abschnitt 7.1) ─────────
    {"wenn": {"hitze_zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hitzeerkrankung in der Vorgeschichte",
     "quelle": "Abschnitt 6.3.2 / 7.1",
     "befund": "Frühere akute Hitzeerkrankung (Hitzekollaps, Hitzekrämpfe, "
               "Hitzeerschöpfung oder Hitzschlag)",
     "konsequenz": "Umstände und Ursachen des Zwischenfalls klären (Adaption, "
                   "Flüssigkeitszufuhr, Grunderkrankung); individuelle Hitzetoleranz "
                   "beurteilen, Schutzmaßnahmen und Verhaltensregeln nach "
                   "DGUV Information 213-002 beraten, ggf. verkürzte Vorsorgefristen."},
    {"wenn": {"hitze_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hitzespezifische Beschwerden",
     "quelle": "Abschnitt 7.1 (Beschwerden)",
     "befund": "Individuelle hitzespezifische Beanspruchungsfolgen (Schwächegefühl, "
               "Unwohlsein, Kopfschmerzen, Übelkeit) bei der Arbeit",
     "konsequenz": "Arbeitsplatzsituation und Beanspruchung prüfen (Untersuchung nach "
                   "ärztlichem Ermessen ergänzen); reichen die Schutzmaßnahmen nicht "
                   "aus, Mitteilung an den Unternehmer und Vorschlag von "
                   "Schutzmaßnahmen nach § 6 (4) ArbMedVV."},
    {"wenn": {"akut_krank": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Akute Erkrankung",
     "quelle": "Abschnitt 6.1",
     "befund": "Aktuell akute Erkrankung – die Hitzetoleranz kann vermindert sein",
     "konsequenz": "Individuelle gesundheitliche Situation beachten; Hitzearbeit "
                   "möglichst erst nach Abklingen der akuten Erkrankung wieder "
                   "aufnehmen, Beratung zu Warnzeichen."},

    # ── Arbeitsanamnese und Schutzverhalten (Abschnitte 6.4, 7.1, 8.1) ──────
    {"wenn": {"fluessigkeit": ["no"]},
     "schwere": "hinweis",
     "bereich": "Flüssigkeitsaufnahme",
     "quelle": "Abschnitt 7.1 / 8.1",
     "befund": "Keine ausreichende Flüssigkeitsaufnahme während der Hitzearbeit",
     "konsequenz": "Beratung zur ausreichenden Flüssigkeitsaufnahme; Bereitstellung "
                   "geeigneter Getränke beim Unternehmen anregen (Beratung des "
                   "Unternehmers nach Abschnitt 8.2)."},
    {"wenn": {"entwaermung": ["no"]},
     "schwere": "hinweis",
     "bereich": "Entwärmungsphasen",
     "quelle": "Abschnitt 7.1 / 8.1",
     "befund": "Entwärmungsphasen in einem kühleren Bereich werden nicht eingehalten",
     "konsequenz": "Beratung zu ausreichenden Entwärmungsphasen (DGUV Information "
                   "213-002); dem Unternehmen organisatorische Schutzmaßnahmen "
                   "(Begrenzung der Expositionszeit, Pausenregelung) vorschlagen."},
    {"wenn": {"hitze_adaption": ["eingewoehnung", "unterbrochen", "gelegentlich"]},
     "schwere": "hinweis",
     "bereich": "Hitzeadaption",
     "quelle": "Abschnitt 6.1 / 6.4",
     "befund": "Keine vollständige Hitzeadaption (Eingewöhnung, längere Unterbrechung "
               "oder nur gelegentliche Exposition)",
     "konsequenz": "Beratung: Eingewöhnungszeit von etwa 2 Wochen einhalten, "
                   "vollständige Adaption erst nach etwa 4 Wochen; nach 3–4 Wochen "
                   "ohne Hitzearbeit geht die Adaption verloren. Für nicht adaptierte "
                   "Beschäftigte gelten die strengeren Richtwerte der Gruppe 2 "
                   "(Tabellen 2 und 3) – Expositionszeit entsprechend begrenzen."},
    {"wenn": {"medikamente": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Medikamente",
     "quelle": "Abschnitt 7.1 / 8.1",
     "befund": "Regelmäßige Medikamenteneinnahme angegeben",
     "konsequenz": "Prüfen, ob die Medikamente Wärmeregulation, Kreislauf oder "
                   "Flüssigkeitshaushalt beeinflussen (z.B. Diuretika, Betablocker, "
                   "Psychopharmaka); individuelle Beratung zum Verhalten bei "
                   "Hitzearbeit."},
]
