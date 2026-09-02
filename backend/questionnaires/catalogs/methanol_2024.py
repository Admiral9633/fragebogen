# -*- coding: utf-8 -*-
"""Methanol – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische
Beratungen und Untersuchungen, 1. Auflage 2024, Kapitel »Methanol« (E MTH,
Fassung Januar 2022), S. 414–428."""

SLUG = "methanol-2024"

CATALOG = {
    "version": 2,
    "title": "Methanol (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Methanol« (E MTH, Fassung Januar 2022), S. 414–428",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen Methanol?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Methanol-Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur Methanol-Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert für Methanol (130 mg/m³) nicht eingehalten wird "
                            "oder eine Gesundheitsgefährdung durch Hautkontakt nicht ausgeschlossen "
                            "werden kann. Angebotsvorsorge: wenn eine Belastung mit Methanol nicht "
                            "ausgeschlossen werden kann.",
                    "required": True,
                    "options": [
                        {"value": "pflicht", "label": "Vom Betrieb verpflichtend veranlasst (Pflichtvorsorge)"},
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
                            "Reinigungs-, Löse-, Kleb- und Dichtmitteln.",
                    "required": True,
                    "options": [
                        {"value": "anlagen", "label": "Abbruch-, Reinigungs- oder Reparaturarbeiten "
                                                      "an Herstellungs- oder Abfüllanlagen"},
                        {"value": "gemische", "label": "Verarbeitung methanolhaltiger Gemische "
                                                       "(z. B. Farben, Lacke, Lösemittel)"},
                        {"value": "filter", "label": "Filterwechsel oder Filterwäsche"},
                        {"value": "praeparation", "label": "Konservierung oder Präparation von Tierkörpern"},
                        {"value": "reinigung_tauchen", "label": "Offene Reinigungsarbeiten oder Tauchverfahren mit Methanol"},
                        {"value": "haerterei", "label": "Härterei (Aufkohlen von Metall-Werkstücken)"},
                        {"value": "gipsbinden", "label": "Herstellung von Gipsbinden"},
                        {"value": "dicht_klebstoffe", "label": "Methanolabspaltende Dichtstoffe oder Klebstoffe "
                                                               "(z. B. beim Parkettverlegen)"},
                        {"value": "kontaminiert", "label": "Arbeiten in Bereichen, die mit Methanol verunreinigt sind"},
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
                    "label": "Tragen Sie beim Umgang mit Methanol Schutzhandschuhe?",
                    "hint": "Wegen der Aufnahme über die Haut sind geeignete Schutzhandschuhe "
                            "bei Methanol besonders wichtig.",
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
                    "id": "psa_sonstige",
                    "type": "multi_choice",
                    "label": "Welche weitere Schutzausrüstung nutzen Sie bei der Arbeit mit "
                             "Methanol?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "schutzbrille", "label": "Schutzbrille"},
                        {"value": "schutzkleidung", "label": "Schutzkleidung / Schürze"},
                        {"value": "atemschutz", "label": "Atemschutz"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
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
                    "hint": "Eine neu aufgetretene Farbsehstörung kann ein Frühzeichen einer "
                            "Methanolwirkung auf den Sehnerv sein.",
                    "required": True,
                },
                {
                    "id": "augen_reizung",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit gereizte, brennende oder tränende Augen?",
                    "hint": "Methanoldämpfe wirken reizend auf die Augen.",
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
            "subtitle": "Erkrankungen, die bei Methanol-Arbeit besonders wichtig sind",
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
                    "hint": "Alkohol (Ethanol) verstärkt die Wirkung von Methanol im Körper – "
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
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"vk_nerven": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 7.4, 7.4.2–7.4.4 und 7.2.2",
     "befund": "Erkrankung des peripheren oder zentralen Nervensystems angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Ausmaß ärztlich klären, in "
                   "unklaren Fällen fachärztliche neurologische Untersuchung veranlassen. "
                   "Maßnahmen nach 7.4.2 prüfen (Substitution, technische/organisatorische "
                   "Maßnahmen, Expositionsminderung, PSA); bei zu erwartender Zunahme des "
                   "Schweregrads verkürzte Vorsorgefristen nach 7.4.3, bei Erfolglosigkeit der "
                   "Maßnahmen Tätigkeitswechsel nach 7.4.4 erwägen (Mitteilung an den "
                   "Arbeitgeber nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"vk_sehnerv": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehnerv",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Veränderung/Erkrankung am Sehnerv angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Sehtest einschließlich Prüfung "
                   "auf erworbene Farbsehstörungen durchführen, bei erworbener Farbsehstörung "
                   "Gesichtsfeldprüfung; in unklaren Fällen augenärztliche fachärztliche "
                   "Untersuchung. Maßnahmen nach 7.4.2/7.4.3 prüfen, ggf. Tätigkeitswechsel "
                   "nach 7.4.4 erwägen."},
    {"wenn": {"vk_leber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Chronische Lebererkrankung angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Leberwerte (γ-GT, ALAT, ASAT) "
                   "bestimmen, in unklaren Fällen ergänzende leberspezifische Untersuchungen. "
                   "Vorbefunde einholen; Maßnahmen nach 7.4.2 und verkürzte Fristen nach 7.4.3 "
                   "prüfen."},
    {"wenn": {"vk_niere": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Niere",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Chronische Nierenerkrankung angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Urinstatus (Mehrfachteststreifen, "
                   "bei Auffälligkeiten Sediment) auswerten, Vorbefunde einholen. Maßnahmen "
                   "nach 7.4.2 und ggf. verkürzte Vorsorgefristen nach 7.4.3 prüfen."},
    {"wenn": {"vk_diabetes": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechsel",
     "quelle": "Abschnitt 7.4",
     "befund": "Diabetes mellitus angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Einstellung und Ausmaß ärztlich "
                   "klären. Maßnahmen nach 7.4.2 prüfen; bei zu erwartender Zunahme des "
                   "Schweregrads verkürzte Vorsorgefristen nach 7.4.3 empfehlen."},
    {"wenn": {"alkohol_abhaengigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 7.4 und 8.1",
     "befund": "Alkoholabhängigkeit (aktuell oder früher) angegeben.",
     "konsequenz": "Alkoholabhängigkeit ist beurteilungsrelevant nach 7.4: aktuellen Status "
                   "ärztlich klären (Abstinenz, Behandlung). Beratung zum die Methanolwirkung "
                   "verstärkenden Einfluss von Alkohol; Maßnahmen nach 7.4.2/7.4.3 prüfen, bei "
                   "Erfolglosigkeit Tätigkeitswechsel nach 7.4.4 erwägen."},
    # ── Stoffspezifische Symptome (Abschnitte 6.3 und 7.1) ────────────────
    {"wenn": {"farbsehen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 6.3.1, 7.1 und 7.2.2",
     "befund": "Veränderung des Farbsehens angegeben (mögliches Frühsymptom einer "
               "Methanolwirkung auf den Sehnerv).",
     "konsequenz": "Sehtest mit Prüfung auf erworbene Farbsehstörungen durchführen; bei "
                   "bestätigter erworbener Farbsehstörung Gesichtsfeldprüfung und "
                   "augenärztliche fachärztliche Untersuchung veranlassen. Biomonitoring "
                   "(Methanol im Urin, BGW 15 mg/l, Probenahme bei Expositions-/Schichtende) "
                   "durchführen und Arbeitsplatzexposition anhand der Gefährdungsbeurteilung "
                   "überprüfen."},
    {"wenn": {"sehstoerung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 6.3.2, 7.1 und 7.2.2",
     "befund": "Sehstörungen (z. B. »nebliges Sehen«) angegeben.",
     "konsequenz": "Sehtest einschließlich Farbsehprüfung durchführen; in unklaren Fällen "
                   "augenärztliche Abklärung. Zusammenhang mit der Methanolexposition prüfen "
                   "(Biomonitoring, Abgleich mit der Gefährdungsbeurteilung); bei Anhaltspunkten "
                   "für unzureichende Schutzmaßnahmen Mitteilung an das Unternehmen nach "
                   "§ 6 (4) ArbMedVV."},
    {"wenn": {"neuro_symptome": ["kribbeln", "hoeren", "zittern", "konzentration"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 6.3.3, 7.1 und 7.2.2",
     "befund": "Mögliche neurologische Symptome angegeben (Hinweis auf periphere Polyneuritis, "
               "Acusticus-/Opticusneuritis, zentralnervöse Störungen oder Parkinson-ähnliche "
               "Symptome).",
     "konsequenz": "Neurologische Anamnese ärztlich vertiefen; in unklaren Fällen fachärztliche "
                   "Untersuchung durch Neurologen bzw. Neurologin. Zusammenhang mit der "
                   "Lösungsmittelexposition prüfen; bei begründetem Verdacht an die "
                   "Berufskrankheiten Nr. 1306 (Methanol) und Nr. 1317 (Polyneuropathie/ "
                   "Enzephalopathie durch organische Lösungsmittel) denken."},
    {"wenn": {"akut_symptome": ["kopfschmerz", "schwindel", "schwaeche", "uebelkeit",
                                "bauchschmerz", "atemnot"]},
     "schwere": "pruefen",
     "bereich": "Akute Wirkungen",
     "quelle": "Abschnitte 6.3.2, 6.4 und 8.2",
     "befund": "»Kater«-Beschwerden bzw. akute Symptome bei oder nach der Arbeit mit Methanol "
               "angegeben.",
     "konsequenz": "Hinweis auf relevante akute Methanolaufnahme: Biomonitoring durchführen "
                   "(Methanol im Urin, BGW 15 mg/l, Probenahme bei Expositions- bzw. "
                   "Schichtende). Expositionssituation mit der Gefährdungsbeurteilung abgleichen; "
                   "ergeben sich Anhaltspunkte, dass die Schutzmaßnahmen nicht ausreichen, "
                   "Mitteilung an das Unternehmen und Vorschlag von Schutzmaßnahmen "
                   "(§ 6 (4) ArbMedVV)."},
    {"wenn": {"haut_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3.1 und 8.1",
     "befund": "Trockene, rissige Haut oder Ekzem an Händen/Unterarmen angegeben.",
     "konsequenz": "Haut ärztlich beurteilen, ggf. hautärztliche Abklärung. Beratung zu "
                   "Hautschutz und Hygiene; geeignete Handschuhmaterialien nach "
                   "Sicherheitsdatenblatt bzw. GESTIS/GISCHEM/WINGIS auswählen. Beachten: "
                   "geschädigte Haut begünstigt die Aufnahme des hautresorptiven Methanols."},
    {"wenn": {"augen_reizung": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Augenreizung",
     "quelle": "Abschnitte 6.3.1 und 8.2",
     "befund": "Augenreizung bei der Arbeit angegeben (Methanoldämpfe wirken reizend auf die "
               "Augen).",
     "konsequenz": "Beratung zu Augenschutz und Expositionsminderung; Lüftungssituation und "
                   "Gefährdungsbeurteilung überprüfen lassen, dem Unternehmen ggf. "
                   "Schutzmaßnahmen vorschlagen."},
    # ── Schutzmaßnahmen und Exposition (Abschnitte 6.1, 6.2, 8.1) ─────────
    {"wenn": {"psa_handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 6.2, 8.1 und 8.2",
     "befund": "Schutzhandschuhe werden beim Umgang mit Methanol selten oder nie getragen.",
     "konsequenz": "Wegen der hautresorptiven Eigenschaften von Methanol kommt der PSA "
                   "besondere Bedeutung zu: eindringlich zum konsequenten Tragen geeigneter "
                   "Schutzhandschuhe beraten (Materialauswahl nach Sicherheitsdatenblatt, "
                   "GESTIS, GISCHEM, WINGIS). Bei Anhaltspunkten für unzureichende "
                   "Schutzmaßnahmen Mitteilung an das Unternehmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitte 2, 6.2 und 8.1",
     "befund": "Regelmäßiger direkter Hautkontakt mit Methanol angegeben.",
     "konsequenz": "Beratung zu Hautschutz, Hygiene und Wechsel benetzter Arbeitskleidung. "
                   "Abgleich mit der Gefährdungsbeurteilung: kann eine Gesundheitsgefährdung "
                   "durch Hautkontakt nicht ausgeschlossen werden, ist Pflichtvorsorge zu "
                   "veranlassen – Vorsorgeanlass ggf. mit dem Unternehmen klären."},
    {"wenn": {"beengt_lueftung": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Inhalative Exposition",
     "quelle": "Abschnitte 6.1 und 8.2",
     "befund": "Arbeiten in beengten Verhältnissen, bei ungünstiger Lüftung oder im "
               "Spritzverfahren angegeben.",
     "konsequenz": "Erhöhte inhalative Exposition möglich: Abgleich mit der "
                   "Gefährdungsbeurteilung, Biomonitoring erwägen (Methanol im Urin). Dem "
                   "Unternehmen ggf. technische/organisatorische Maßnahmen (Lüftung, "
                   "Begrenzung der Expositionszeit) oder Atemschutz vorschlagen."},
    # ── Alkohol (Abschnitt 8.1) ───────────────────────────────────────────
    {"wenn": {"alkohol_konsum": ["regelmaessig", "taeglich"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitt 8.1",
     "befund": "Regelmäßiger bis täglicher Alkoholkonsum angegeben.",
     "konsequenz": "Beratung hinsichtlich des die Methanolwirkung verstärkenden Einflusses von "
                   "konsumiertem Alkohol; auf Wechselwirkungen mit der beruflichen "
                   "Methanolexposition hinweisen."},
]
