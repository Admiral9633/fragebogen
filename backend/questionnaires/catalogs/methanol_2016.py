# -*- coding: utf-8 -*-
"""G 10 Methanol – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, Grundsatz G 10 »Methanol«
(Fassung Oktober 2014), S. 207–215."""

SLUG = "g10-methanol-2016"

CATALOG = {
    "version": 2,
    "title": "G 10 Methanol (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 10 »Methanol« (Fassung Oktober 2014), S. 207–215",
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
                    "label": "Um welche Untersuchung nach dem Grundsatz G 10 (Methanol) "
                             "handelt es sich?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachuntersuchung: "
                            "erste nach 12–24 Monaten, weitere jeweils nach 24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung (z. B. Krankenhausaufenthalt, längere "
                             "Krankschreibung)?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
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
            "title": "Tätigkeit & Kontakt mit Methanol",
            "subtitle": "Ihre Arbeit und der Umgang mit Methanol (Methylalkohol)",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten haben Sie Kontakt mit Methanol oder "
                             "methanolhaltigen Produkten?",
                    "hint": "Mehrfachauswahl möglich. Methanol steckt z. B. in manchen "
                            "Reinigungs- und Lösemitteln.",
                    "required": True,
                    "options": [
                        {"value": "anlagen", "label": "Abbruch-, Reinigungs- oder Reparaturarbeiten "
                                                      "an Herstellungs- oder Abfüllanlagen"},
                        {"value": "zubereitungen", "label": "Verarbeitung methanolhaltiger Zubereitungen "
                                                            "(z. B. Farben, Lacke, Lösemittel)"},
                        {"value": "filter", "label": "Filterwechsel oder Filterwäsche"},
                        {"value": "praeparation", "label": "Konservierung oder Präparation von Tierkörpern"},
                        {"value": "reinigung_tauchen", "label": "Offener Umgang mit Methanol bei "
                                                                "Reinigungsarbeiten oder Tauchverfahren"},
                        {"value": "textil", "label": "Textilveredelung"},
                        {"value": "papier", "label": "Herstellung/Verarbeitung von Papier, Karton, Pappe"},
                        {"value": "beschichtung", "label": "Oberflächenbeschichtung in der "
                                                           "Metallverarbeitung (maschinelles Auftragen)"},
                        {"value": "kontaminiert", "label": "Arbeiten in Bereichen, die mit Methanol "
                                                           "verunreinigt sind"},
                        {"value": "andere", "label": "Andere Arbeiten mit Methanol"},
                        {"value": "keine", "label": "Keine davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "beengt_lueftung",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Methanol in engen Räumen, bei schlechter Lüftung "
                             "oder im Spritzverfahren?",
                    "hint": "Dabei können sich Methanoldämpfe in der Atemluft anreichern.",
                    "required": True,
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit direkt mit Methanol oder "
                             "methanolhaltigen Flüssigkeiten in Berührung (z. B. Spritzer, "
                             "benetzte Handschuhe oder Kleidung)?",
                    "hint": "Methanol wird auch über die Haut in den Körper aufgenommen.",
                    "required": True,
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt mit Methanol oder methanolhaltigen "
                             "Produkten?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "ueber5", "label": "Mehr als 5 Jahre"},
                    ],
                },
                {
                    "id": "frueher_loesungsmittel",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit Methanol oder "
                             "anderen Lösungsmitteln?",
                    "required": True,
                    "followup": {"id": "frueher_loesungsmittel_desc", "type": "textarea",
                                 "label": "Welche Stoffe/Tätigkeiten, und wie lange?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Persönliche Schutzausrüstung an Ihrem Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_handschuhe",
                    "type": "choice",
                    "label": "Tragen Sie beim Umgang mit Methanol Schutzhandschuhe und "
                             "Schutzkleidung?",
                    "hint": "Weil Methanol über die Haut aufgenommen wird, kommt dem Tragen "
                            "von Schutzkleidung besondere Bedeutung zu.",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_kontakt", "label": "Ich habe keinen direkten Kontakt mit Methanol"},
                    ],
                },
                {
                    "id": "atemschutz",
                    "type": "yes_no",
                    "label": "Nutzen Sie bei Arbeiten mit Methanoldämpfen Atemschutz?",
                    "required": True,
                    "show_if": {"id": "psa_handschuhe", "not_in": ["kein_kontakt"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die mit Methanol zusammenhängen können",
            "questions": [
                {
                    "id": "sehstoerung",
                    "type": "yes_no",
                    "label": "Haben Sie Sehstörungen bemerkt, z. B. verschwommenes oder "
                             "»nebliges« Sehen?",
                    "required": True,
                    "followup": {"id": "sehstoerung_desc", "type": "text",
                                 "label": "Seit wann, und in welchen Situationen?", "when": "yes"},
                },
                {
                    "id": "farbsehen",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Farbsehen verändert (Farben wirken blasser oder sind "
                             "schwerer zu unterscheiden als früher)?",
                    "hint": "Eine neu aufgetretene Farbsehstörung gilt als Frühzeichen einer "
                            "Methanolwirkung auf den Sehnerv.",
                    "required": True,
                },
                {
                    "id": "reizung",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit gereizte, brennende Augen oder Reizungen "
                             "der Atemwege (z. B. Brennen in Nase oder Rachen, Hustenreiz)?",
                    "hint": "Methanoldämpfe reizen die Augen und die Schleimhäute der Atemwege.",
                    "required": True,
                },
                {
                    "id": "akut_symptome",
                    "type": "multi_choice",
                    "label": "Treten bei oder nach der Arbeit mit Methanol folgende Beschwerden "
                             "auf (»Kater«-Beschwerden)?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "kopfschmerz", "label": "Kopfschmerzen"},
                        {"value": "schwindel", "label": "Schwindel"},
                        {"value": "schwaeche", "label": "Schwächegefühl / starke Müdigkeit"},
                        {"value": "uebelkeit", "label": "Übelkeit oder Erbrechen"},
                        {"value": "bauchschmerz", "label": "Krampfartige Magen-Darm-Schmerzen"},
                        {"value": "atemnot", "label": "Atemnot"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "neuro_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere der folgenden Beschwerden?",
                    "hint": "Mehrfachauswahl möglich. Diese Beschwerden können auf eine Wirkung "
                            "von Lösungsmitteln auf das Nervensystem hinweisen.",
                    "required": True,
                    "options": [
                        {"value": "kribbeln", "label": "Kribbeln, Taubheitsgefühl oder Brennen in "
                                                       "Händen oder Füßen"},
                        {"value": "hoeren", "label": "Neu aufgetretene Hörstörungen oder Ohrgeräusche"},
                        {"value": "zittern", "label": "Zittern, Steifigkeit oder verlangsamte Bewegungen"},
                        {"value": "konzentration", "label": "Auffällige Konzentrations- oder "
                                                            "Gedächtnisstörungen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "haut_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie an Händen oder Unterarmen sehr trockene, rissige Haut "
                             "oder einen Hautausschlag (Ekzem)?",
                    "hint": "Methanol entfettet die Haut; sie kann austrocknen, rissig werden "
                            "und sich leichter entzünden.",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen & Alkohol ──────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Alkohol",
            "subtitle": "Erkrankungen, die bei der Beurteilung nach G 10 wichtig sind",
            "questions": [
                {
                    "id": "vk_nerven",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung des Nervensystems bekannt "
                             "(z. B. Polyneuropathie/Nervenschädigung, Epilepsie, "
                             "Parkinson-Krankheit)?",
                    "required": True,
                    "followup": {"id": "vk_nerven_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vk_sehnerv",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung oder Schädigung des Sehnervs "
                             "bekannt (z. B. Sehnerventzündung, Grüner Star/Glaukom mit "
                             "Sehnervschaden)?",
                    "required": True,
                    "followup": {"id": "vk_sehnerv_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vk_leber",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Lebererkrankung "
                             "(z. B. Fettleber mit Entzündung, Hepatitis, Leberzirrhose)?",
                    "required": True,
                    "followup": {"id": "vk_leber_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vk_niere",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Nierenerkrankung?",
                    "required": True,
                    "followup": {"id": "vk_niere_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vk_diabetes",
                    "type": "yes_no",
                    "label": "Haben Sie Diabetes mellitus (Zuckerkrankheit)?",
                    "required": True,
                },
                {
                    "id": "alkohol_konsum",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Alkohol (Ethanol) verstärkt die Wirkung von Methanol im Körper und "
                            "kann außerdem die Messwerte des Biomonitorings beeinflussen – "
                            "deshalb ist diese Frage hier wichtig.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "gelegentlich", "label": "Gelegentlich (höchstens 1-mal pro Woche)"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche)"},
                        {"value": "taeglich", "label": "Täglich"},
                    ],
                },
                {
                    "id": "alkohol_abhaengigkeit",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen jemals eine Alkoholabhängigkeit festgestellt oder "
                             "behandelt?",
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
    # ── Bedenkenstatbestände (Abschnitt 2.1.1) ────────────────────────────
    {"wenn": {"vk_nerven": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 2.1.1–2.1.3 und 1.2.3",
     "befund": "Erkrankung des peripheren oder zentralen Nervensystems angegeben.",
     "konsequenz": "Möglicher Tatbestand dauernder gesundheitlicher Bedenken (2.1.1): "
                   "neurologische Ergänzungsuntersuchung veranlassen (1.2.3), Vorbefunde "
                   "einholen. Bei zu erwartender Wiederherstellung befristete Bedenken (2.1.2); "
                   "bei weniger ausgeprägter Erkrankung prüfen, ob keine Bedenken unter "
                   "bestimmten Voraussetzungen möglich sind (2.1.3: technische/organisatorische "
                   "Schutzmaßnahmen, geringere Exposition, PSA, verkürzte "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"vk_sehnerv": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Sehnerv",
     "quelle": "Abschnitte 2.1.1–2.1.3, 1.2.2 und 1.2.3",
     "befund": "Veränderung/Erkrankung am Sehnerv angegeben.",
     "konsequenz": "Möglicher Tatbestand dauernder gesundheitlicher Bedenken (2.1.1): Sehtest "
                   "mit Prüfung auf erworbene Farbsehstörungen und Gesichtsfeldprüfung "
                   "durchführen, augenärztliche Ergänzungsuntersuchung veranlassen (1.2.3). "
                   "Nur bei weniger ausgeprägtem Befund keine Bedenken unter Voraussetzungen "
                   "nach 2.1.3 erwägen."},
    {"wenn": {"vk_leber": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Leber",
     "quelle": "Abschnitte 2.1.1–2.1.3, 1.2.2 und 1.2.3",
     "befund": "Chronische Leberkrankheit angegeben.",
     "konsequenz": "Möglicher Tatbestand dauernder gesundheitlicher Bedenken (2.1.1): "
                   "Leberwerte (γ-GT, ALAT, ASAT) bestimmen, in unklaren Fällen "
                   "leberspezifische Ergänzungsuntersuchungen (1.2.3). Ausprägung klären; ggf. "
                   "keine Bedenken unter Voraussetzungen nach 2.1.3 (u. a. verkürzte "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"vk_niere": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Niere",
     "quelle": "Abschnitte 2.1.1–2.1.3 und 1.2.1",
     "befund": "Chronische Nierenkrankheit angegeben.",
     "konsequenz": "Möglicher Tatbestand dauernder gesundheitlicher Bedenken (2.1.1): "
                   "Urinstatus (Mehrfachteststreifen, bei Auffälligkeiten Sediment) auswerten, "
                   "Vorbefunde einholen. Ausprägung klären; ggf. keine Bedenken unter "
                   "Voraussetzungen nach 2.1.3."},
    {"wenn": {"vk_diabetes": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Stoffwechsel",
     "quelle": "Abschnitte 2.1.1–2.1.3",
     "befund": "Zuckerkrankheit (Diabetes mellitus) angegeben.",
     "konsequenz": "Möglicher Tatbestand dauernder gesundheitlicher Bedenken (2.1.1): "
                   "Stoffwechseleinstellung ärztlich klären. Bei gut eingestellter, wenig "
                   "ausgeprägter Erkrankung keine Bedenken unter Voraussetzungen nach 2.1.3 "
                   "(u. a. verkürzte Nachuntersuchungsfristen) prüfen."},
    {"wenn": {"alkohol_abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 2.1.1–2.1.3 und 2.2",
     "befund": "Alkoholismus (aktuell oder früher) angegeben.",
     "konsequenz": "Alkoholismus ist Tatbestand dauernder gesundheitlicher Bedenken (2.1.1): "
                   "aktuellen Status klären (Abstinenz, Behandlung); bei zu erwartender "
                   "Wiederherstellung befristete Bedenken (2.1.2). Beratung zum die "
                   "Methanolwirkung potenzierenden Einfluss von Alkohol (2.2)."},
    # ── Stoffspezifische Symptome (Abschnitte 3.2 und 1.2) ────────────────
    {"wenn": {"farbsehen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 3.2.1, 1.2.2 und 1.2.3",
     "befund": "Veränderung des Farbsehens angegeben (Frühsymptom einer Methanolwirkung "
               "auf den Sehnerv).",
     "konsequenz": "Sehtest mit Prüfung auf erworbene Farbsehstörungen durchführen; bei "
                   "gestörter Farbtüchtigkeit Gesichtsfeldprüfung (1.2.2) und augenärztliche "
                   "Ergänzungsuntersuchung (1.2.3). Biomonitoring (Methanol im Urin, "
                   "BGW 30 mg/l, Probenahme bei Expositions-/Schichtende) durchführen; "
                   "vorzeitige Nachuntersuchung nach ärztlichem Ermessen erwägen."},
    {"wenn": {"sehstoerung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 3.2.2, 1.2.2 und 1.2.3",
     "befund": "Sehstörungen (z. B. »nebliges Sehen«) angegeben.",
     "konsequenz": "Sehtest einschließlich Farbsehprüfung durchführen; in unklaren Fällen "
                   "augenärztliche Ergänzungsuntersuchung. Zusammenhang mit der "
                   "Methanolexposition prüfen (Biomonitoring); bei Hinweisen auf unzureichenden "
                   "Arbeitsschutz Mitteilung an den Arbeitgeber unter Wahrung der "
                   "schutzwürdigen Belange (2.2)."},
    {"wenn": {"neuro_symptome": ["kribbeln", "hoeren", "zittern", "konzentration"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 3.2.3, 1.2.3 und 4",
     "befund": "Mögliche neurologische Symptome angegeben (Hinweis auf zentralnervöse "
               "Störungen, periphere Polyneuritis, Acusticus-/Opticusneuritis oder "
               "Parkinson-ähnliche Symptome).",
     "konsequenz": "Neurologische Ergänzungsuntersuchung veranlassen (1.2.3). Zusammenhang mit "
                   "der Lösungsmittelexposition prüfen; bei begründetem Verdacht an die "
                   "Berufskrankheiten Nr. 1306 (Methanol) und Nr. 1317 (Polyneuropathie/ "
                   "Enzephalopathie durch organische Lösungsmittel) denken."},
    {"wenn": {"akut_symptome": ["kopfschmerz", "schwindel", "schwaeche", "uebelkeit",
                                "bauchschmerz", "atemnot"]},
     "schwere": "pruefen",
     "bereich": "Akute Wirkungen",
     "quelle": "Abschnitte 3.2.2, 3.1.4 und 2.2",
     "befund": "»Kater«-Beschwerden bzw. akute Symptome bei oder nach der Arbeit mit Methanol "
               "angegeben.",
     "konsequenz": "Hinweis auf relevante Methanolaufnahme: Biomonitoring durchführen "
                   "(Methanol im Urin, BGW 30 mg/l, Probenahme bei Expositions- bzw. "
                   "Schichtende). Bei Hinweisen auf unzureichenden Arbeitsschutz Mitteilung an "
                   "den Arbeitgeber zur Aktualisierung der Gefährdungsbeurteilung (2.2); "
                   "vorzeitige Nachuntersuchung nach ärztlichem Ermessen."},
    {"wenn": {"haut_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 3.2.1 und 2.2",
     "befund": "Trockene, rissige Haut oder Ekzem an Händen/Unterarmen angegeben.",
     "konsequenz": "Haut ärztlich beurteilen, ggf. hautärztliche Abklärung. Beratung zu "
                   "Hygienemaßnahmen und Schutzkleidung (2.2); geschädigte Haut begünstigt "
                   "die Aufnahme des hautresorptiven Methanols und die Entstehung von "
                   "Ekzemen und Infektionen."},
    {"wenn": {"reizung": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Reizwirkung",
     "quelle": "Abschnitte 3.2.1, 3.2.2 und 2.2",
     "befund": "Reizung von Augen oder Atemwegsschleimhäuten bei der Arbeit angegeben.",
     "konsequenz": "Beratung zu Expositionsminderung, Augenschutz und geeignetem Atemschutz "
                   "(stoffspezifische Hinweise in GESTIS, Rubrik »Umgang und Verwendung«); "
                   "bei fortbestehenden Beschwerden Arbeitgeber-Mitteilung zur Überprüfung "
                   "der Schutzmaßnahmen."},
    # ── Fristen (Abschnitt 1.1) ───────────────────────────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt, wenn die Erkrankung Anlass zu "
                   "Bedenken gegen die Fortsetzung der Tätigkeit geben könnte: Art und Verlauf "
                   "der Erkrankung klären, Befunde anfordern, Untersuchungsumfang entsprechend "
                   "erweitern."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Die untersuchte Person vermutet einen ursächlichen Zusammenhang zwischen "
               "Erkrankung und Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist vorgesehen: Beschwerden und "
                   "Expositionssituation gezielt abklären (ggf. Ergänzungsuntersuchungen nach "
                   "1.2.3, Biomonitoring); bei begründetem Verdacht Berufskrankheiten-Anzeige "
                   "(BK-Nr. 1306/1317) prüfen."},
    # ── Schutzmaßnahmen und Confounder ────────────────────────────────────
    {"wenn": {"psa_handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 2.2 und 3.1.3",
     "befund": "Schutzhandschuhe/Schutzkleidung werden beim Umgang mit Methanol selten oder "
               "nie getragen.",
     "konsequenz": "Wegen der hautresorptiven Eigenschaften von Methanol kommt der "
                   "Schutzkleidung besondere Bedeutung zu: eindringlich zum konsequenten "
                   "Tragen beraten (stoffspezifische Hinweise in GESTIS). Ergibt sich daraus "
                   "die Notwendigkeit, die Gefährdungsbeurteilung zu aktualisieren, Mitteilung "
                   "an den Arbeitgeber unter Wahrung der schutzwürdigen Belange (2.2)."},
    {"wenn": {"alkohol_konsum": ["regelmaessig", "taeglich"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 2.2 und 3.1.4",
     "befund": "Regelmäßiger bis täglicher Alkoholkonsum angegeben.",
     "konsequenz": "Beratung zum die Methanolwirkung potenzierenden Einfluss von konsumiertem "
                   "Alkohol (2.2). Beim Biomonitoring Störfaktor beachten: Ethanol hemmt die "
                   "Methanol-Oxidation kompetitiv – bei gleichzeitiger Aufnahme kann die "
                   "Methanolausscheidung im Urin erhöht sein (3.1.4)."},
    {"wenn": {"beengt_lueftung": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Inhalative Exposition",
     "quelle": "Abschnitte 3.1.1 und 2.2",
     "befund": "Arbeiten in beengten Verhältnissen, bei ungünstiger Lüftung oder im "
               "Spritzverfahren angegeben.",
     "konsequenz": "Erhöhte inhalative Exposition möglich: Biomonitoring erwägen (Methanol im "
                   "Urin, BGW 30 mg/l). Beratung zu Lüftung und Atemschutz; ggf. "
                   "Arbeitgeber-Mitteilung zur Aktualisierung der Gefährdungsbeurteilung (2.2)."},
]
