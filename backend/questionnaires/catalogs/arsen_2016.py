# -*- coding: utf-8 -*-
"""G 16 Arsen oder seine Verbindungen (mit Ausnahme des Arsenwasserstoffs) –
DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für arbeitsmedizinische
Untersuchungen, 6. Auflage 2016, G 16 (Fassung Oktober 2014), S. 279–290."""

SLUG = "g16-arsen-2016"

CATALOG = {
    "version": 2,
    "title": "G 16 Arsen oder seine Verbindungen (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 16 »Arsen oder seine Verbindungen (mit Ausnahme des Arsenwasserstoffs)« "
             "(Fassung Oktober 2014), S. 279–290",
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
                    "label": "Um welche Untersuchung handelt es sich heute?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachuntersuchung: "
                            "in der Regel nach 6–12 Monaten. Nachgehende Untersuchung: nach "
                            "dem Ende der Tätigkeit mit Arsen.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich war schon einmal zur G 16-Untersuchung)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (die Tätigkeit mit Arsen ist beendet)"},
                    ],
                },
                {
                    "id": "zusammenhang_vermutung",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung oder "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Erkrankung bzw. Beschwerden, und warum vermuten "
                                          "Sie einen Zusammenhang?", "when": "yes"},
                },
                {
                    "id": "schwere_erkrankung_seit",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder länger "
                             "dauernde Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Arsen-Belastung",
            "subtitle": "Ihre Arbeit und der mögliche Kontakt mit Arsen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "arsen_bereiche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen kommen Sie mit Arsen oder seinen Verbindungen "
                             "in Kontakt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "aufbereitung", "label": "Aufbereiten oder Verarbeiten von Arsenverbindungen mit "
                                                           "Staubentwicklung"},
                        {"value": "metallurgie", "label": "Gewinnung von Nichteisenmetallen aus arsenhaltigen Erzen "
                                                          "oder Vormaterialien"},
                        {"value": "roesten", "label": "Rösten von Schwefelkies (Pyrit)"},
                        {"value": "filterreinigung", "label": "Reparatur oder Reinigung von Flugstaubanlagen und Filtern"},
                        {"value": "bleikammer", "label": "Verarbeiten von Bleikammerrückständen "
                                                         "(Schwefelsäureherstellung)"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an Produktionsanlagen für Arsen oder seine "
                                                      "Verbindungen"},
                        {"value": "glashuette", "label": "Gemengemacher in Glashütten (Arsen als Läuterungsmittel in "
                                                         "offenen Systemen)"},
                        {"value": "sonstiges", "label": "Anderer Bereich"},
                        {"value": "keine", "label": "Keiner davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit möglichem Arsen-Kontakt?",
                    "required": True,
                    "options": [
                        {"value": "beginnt", "label": "Noch gar nicht, die Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis15", "label": "5 bis 15 Jahre"},
                        {"value": "ueber15", "label": "Mehr als 15 Jahre"},
                    ],
                },
                {
                    "id": "expo_3tage",
                    "type": "yes_no",
                    "label": "Waren Sie an mindestens 3 Arbeitstagen hintereinander vor diesem "
                             "Termin gegenüber Arsen exponiert (mit möglichem Arsen-Kontakt "
                             "tätig)?",
                    "hint": "Wichtig für die Arsen-Messung im Urin: Sie soll nach mindestens "
                            "3 aufeinanderfolgenden Expositionstagen sofort nach Ende der "
                            "letzten Schicht erfolgen.",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                },
                {
                    "id": "frueher_krebs_stoffe",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit Arsen oder anderen "
                             "krebserzeugenden Gefahrstoffen (z. B. Asbest, Benzol, Chromate)?",
                    "required": True,
                    "followup": {"id": "frueher_krebs_desc", "type": "textarea",
                                 "label": "Welche Stoffe, welche Tätigkeiten, wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Benutzen Sie bei Tätigkeiten mit möglichem Arsen-Kontakt die "
                             "vorgesehene persönliche Schutzausrüstung (z. B. Atemschutz, "
                             "Schutzhandschuhe, Schutzkleidung) und halten Sie die Hygieneregeln "
                             "ein (nicht essen, trinken oder rauchen am Arbeitsplatz)?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "not_in": ["nachgehend"]},
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "teilweise", "label": "Nur teilweise"},
                        {"value": "nie", "label": "Nein"},
                        {"value": "keine_noetig", "label": "Für meine Tätigkeit ist keine Schutzausrüstung vorgesehen"},
                    ],
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, die mit Arsen zusammenhängen können",
            "questions": [
                {
                    "id": "haut_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie Veränderungen an der Haut bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "hyperkeratosen", "label": "Auffällige Hornhaut-Verdickungen, z. B. an Handflächen "
                                                             "oder Fußsohlen (Hyperkeratosen)"},
                        {"value": "pigment", "label": "Neue dunkle oder helle Flecken (Pigmentverschiebungen)"},
                        {"value": "ekzem", "label": "Ekzem, Hautausschlag oder anhaltende Hautreizung"},
                        {"value": "keine", "label": "Nein, keine davon"},
                    ],
                },
                {
                    "id": "augen_reizung",
                    "type": "yes_no",
                    "label": "Haben Sie gereizte Augen (Jucken, Brennen, Tränen, "
                             "Lichtempfindlichkeit) oder Reizungen in Nase und Rachen?",
                    "required": True,
                },
                {
                    "id": "atemwege",
                    "type": "yes_no",
                    "label": "Haben Sie Husten, Atemnot oder Schmerzen in der Brust?",
                    "required": True,
                },
                {
                    "id": "magen_darm",
                    "type": "yes_no",
                    "label": "Haben Sie Magen-Darm-Beschwerden wie Übelkeit, Erbrechen, Durchfall, "
                             "Bauchschmerzen oder einen metallischen bzw. knoblauchartigen "
                             "Geschmack im Mund?",
                    "required": True,
                },
                {
                    "id": "nerven",
                    "type": "yes_no",
                    "label": "Haben Sie Kribbeln, Taubheitsgefühl oder Schwäche in Händen oder "
                             "Füßen (Zeichen einer Nervenschädigung, sog. Polyneuropathie)?",
                    "required": True,
                },
                {
                    "id": "gefaesse",
                    "type": "yes_no",
                    "label": "Haben Sie Durchblutungsstörungen an den Fingern, z. B. weiße, kalte "
                             "oder schmerzende Finger?",
                    "required": True,
                },
                {
                    "id": "allgemein_einschraenkung",
                    "type": "yes_no",
                    "label": "Haben Sie sonstige gesundheitliche Einschränkungen oder Beschwerden?",
                    "required": True,
                    "followup": {"id": "allgemein_einschraenkung_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen, Alkohol, Rauchen ──────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Rauchen",
            "subtitle": "Ihre Krankengeschichte",
            "questions": [
                {
                    "id": "organ_erkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Erkrankungen festgestellt?",
                    "hint": "Mehrfachauswahl möglich. Diese Organe können durch Arsen zusätzlich "
                            "geschädigt werden.",
                    "required": True,
                    "options": [
                        {"value": "leber", "label": "Erkrankung der Leber"},
                        {"value": "niere", "label": "Erkrankung der Nieren"},
                        {"value": "magen_darm", "label": "Erkrankung des Magen-Darm-Trakts"},
                        {"value": "gefaesse", "label": "Gefäßerkrankung (z. B. Durchblutungsstörungen)"},
                        {"value": "blut", "label": "Bluterkrankung (z. B. Blutarmut/Anämie)"},
                        {"value": "nerven", "label": "Erkrankung der Nerven oder des Gehirns"},
                        {"value": "bronchien", "label": "Erkrankung der Bronchien (z. B. chronische Bronchitis, "
                                                        "Asthma)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "haut_erkrankungen",
                    "type": "multi_choice",
                    "label": "Besteht oder bestand bei Ihnen eine der folgenden Hauterkrankungen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "chron_ekzem", "label": "Chronisches Ekzem"},
                        {"value": "psoriasis", "label": "Schuppenflechte (Psoriasis)"},
                        {"value": "ichthyose", "label": "Fischschuppenkrankheit (Ichthyose)"},
                        {"value": "lichtempfindlich", "label": "Lichtüberempfindlichkeit der Haut"},
                        {"value": "landmannshaut", "label": "Starke Lichtschädigung der Haut (»Landmannshaut«)"},
                        {"value": "hyperkeratosen", "label": "Mehrfache Hornhaut-Verdickungen (multiple Hyperkeratosen)"},
                        {"value": "arsen_ueberempfindlich", "label": "Bekannte Überempfindlichkeit gegen Arsen"},
                        {"value": "andere", "label": "Andere chronische Hauterkrankung"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "alkohol",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Alkoholabhängigkeit?",
                    "required": True,
                },
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Rauchen ist besonders schädlich, wenn zugleich Arsen eingeatmet wird.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "frueher", "label": "Früher, nicht mehr"},
                        {"value": "nie", "label": "Nein, nie"},
                    ],
                },
            ],
        },
        # ── 5 ─ Einwilligung ───────────────────────────────────────────────
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
    # ── Bedenkentatbestände (Abschnitt 2.1) ───────────────────────────────
    {"wenn": {"organ_erkrankungen": ["leber", "niere", "magen_darm", "gefaesse",
                                     "blut", "nerven", "bronchien"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankungen",
     "quelle": "Abschnitte 2.1.1–2.1.3",
     "befund": "Erkrankung eines Arsen-Zielorgans angegeben (Leber, Niere, Magen-Darm, "
               "Gefäße, Blut, Nervensystem oder Bronchien).",
     "konsequenz": "Schweregrad ärztlich klären: Bei schwerer Erkrankung dauernde "
                   "gesundheitliche Bedenken (2.1.1); ist eine Wiederherstellung zu "
                   "erwarten, befristete Bedenken (2.1.2). Bei weniger ausgeprägten "
                   "Befunden keine Bedenken unter bestimmten Voraussetzungen (2.1.3): "
                   "technische/organisatorische Schutzmaßnahmen, Einsatz an Arbeitsplätzen "
                   "mit geringerer Exposition, PSA, verkürzte Nachuntersuchungsfristen."},
    {"wenn": {"haut_erkrankungen": ["chron_ekzem", "psoriasis", "ichthyose",
                                    "lichtempfindlich", "landmannshaut",
                                    "hyperkeratosen", "arsen_ueberempfindlich",
                                    "andere"]},
     "schwere": "kritisch",
     "bereich": "Hauterkrankung",
     "quelle": "Abschnitt 2.1.1 (Haut)",
     "befund": "Chronische Hauterkrankung angegeben (z. B. chronisches Ekzem, "
               "Schuppenflechte, Fischschuppenkrankheit, Lichtüberempfindlichkeit, "
               "Landmannshaut, multiple Hyperkeratosen oder Arsenüberempfindlichkeit).",
     "konsequenz": "Dermatologischen Befund erheben bzw. Vorbefunde einholen. Bei schwerer "
                   "Ausprägung dauernde gesundheitliche Bedenken (2.1.1); bei erwarteter "
                   "Wiederherstellung befristete Bedenken (2.1.2); bei geringer Ausprägung "
                   "Aufnahme/Fortsetzung nur unter den Voraussetzungen nach 2.1.3 "
                   "(Schutzmaßnahmen, verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"alkohol": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Alkoholabhängigkeit",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Alkoholabhängigkeit angegeben.",
     "konsequenz": "Alkoholabhängigkeit ist ein Tatbestand für dauernde gesundheitliche "
                   "Bedenken (2.1.1); aktuelle Situation ärztlich klären, bei erwarteter "
                   "Wiederherstellung befristete Bedenken (2.1.2), Beratungs- und "
                   "Behandlungsangebote vermitteln."},
    # ── Beschwerden → gezielte Abklärung (Abschnitte 1.2, 3.2) ────────────
    {"wenn": {"haut_beschwerden": ["hyperkeratosen", "pigment", "ekzem"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 1.2.2 und 3.2.3",
     "befund": "Hautveränderungen angegeben (Hyperkeratosen, Pigmentverschiebungen "
               "oder Ekzem).",
     "konsequenz": "Gezielte Untersuchung der Haut (spezielle Untersuchung 1.2.2, besonders "
                   "achten auf Hyperkeratosen, Pigmentverschiebungen, Ekzeme); in unklaren "
                   "Fällen Ergänzungsuntersuchung Biomonitoring (1.2.3). Bei Verdacht auf "
                   "arsenbedingte Hautschädigung Bedenken nach 2.1 prüfen und ärztliche "
                   "BK-Anzeige (BK-Nr. 1108) erwägen."},
    {"wenn": {"nerven": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 2.1.1 und 3.2.2/3.2.3",
     "befund": "Kribbeln, Taubheitsgefühl oder Schwäche in Händen/Füßen angegeben "
               "(mögliche periphere Neuropathie).",
     "konsequenz": "Neurologische Abklärung veranlassen; in unklaren Fällen Ergänzungs-"
                   "untersuchung Biomonitoring (Arsenbestimmung in biologischem Material, "
                   "1.2.3). Bei bestätigter Erkrankung des peripheren/zentralen Nerven-"
                   "systems Bedenken nach 2.1.1/2.1.2 aussprechen."},
    {"wenn": {"atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 1.2.2, 2.1.1 und 3.2.3",
     "befund": "Husten, Atemnot oder Brustschmerzen angegeben.",
     "konsequenz": "Atemwegssymptome abklären; bei der Nachuntersuchung ggf. radiologische "
                   "Diagnostik des Thorax (1.2.2, unter Beachtung der Leitlinien der "
                   "Bundesärztekammer und des Anhangs zur radiologischen Diagnostik im "
                   "G 1.1). Bei Erkrankung der Bronchien Bedenken nach 2.1 prüfen."},
    {"wenn": {"magen_darm": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm-Trakt",
     "quelle": "Abschnitte 2.1.1 und 3.2.2",
     "befund": "Magen-Darm-Beschwerden bzw. metallisch-knoblauchartiger Geschmack "
               "angegeben.",
     "konsequenz": "An akute/subakute Arsenaufnahme denken (gastrointestinale Verlaufs-"
                   "form): zeitnahe Abklärung, Laborprogramm der speziellen Untersuchung "
                   "(großes Blutbild, Leberwerte, Kreatinin) und Biomonitoring; bei "
                   "Erkrankung des Magen-Darm-Trakts Bedenken nach 2.1 prüfen."},
    {"wenn": {"gefaesse": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gefäße",
     "quelle": "Abschnitte 2.1.1 und 3.2.3",
     "befund": "Durchblutungsstörungen an den Fingern angegeben.",
     "konsequenz": "Abklärung peripherer Gefäßschäden (v. a. Fingerarterien); bei "
                   "Gefäßerkrankung Bedenken nach 2.1 prüfen, ggf. angiologische "
                   "Vorstellung."},
    {"wenn": {"augen_reizung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Reizwirkungen",
     "quelle": "Abschnitte 2.2 und 3.2.2",
     "befund": "Reizungen der Augen bzw. der oberen Atemwege angegeben.",
     "konsequenz": "Lokale Reizwirkung arsenhaltiger Stäube abklären; Arbeitsplatz- und "
                   "Schutzmaßnahmensituation prüfen. Ergibt sich Aktualisierungsbedarf "
                   "der Gefährdungsbeurteilung, Mitteilung an den Arbeitgeber unter "
                   "Wahrung der schutzwürdigen Belange (2.2)."},
    # ── Fristen und Untersuchungsanlässe (Abschnitt 1.1) ──────────────────
    {"wenn": {"zusammenhang_vermutung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Fristen)",
     "befund": "Die untersuchte Person vermutet einen Zusammenhang zwischen Erkrankung "
               "und Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen bzw. anbieten (1.1); Verdacht "
                   "dokumentieren, gezielt abklären und bei begründetem Verdacht auf eine "
                   "Berufskrankheit (BK-Nr. 1108) ärztliche Anzeige erstatten."},
    {"wenn": {"schwere_erkrankung_seit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Fristen)",
     "befund": "Schwere oder länger dauernde Erkrankung seit der letzten Untersuchung "
               "angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen eine Fortsetzung "
                   "der Tätigkeit gibt (vorzeitige Nachuntersuchung nach 1.1); Befunde "
                   "und Behandlungsunterlagen einholen, Beurteilung nach 2.1."},
    {"wenn": {"expo_3tage": ["no"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitte 1.2.2 und 3.1.4",
     "befund": "Vor dem Termin keine mindestens 3 aufeinanderfolgenden Expositionstage.",
     "konsequenz": "Voraussetzung für das Biomonitoring nicht erfüllt: Arsenbestimmung im "
                   "Urin nach einer Exposition von mindestens 3 aufeinanderfolgenden Tagen, "
                   "sofort nach Ende der letzten Schicht durchführen – Probenahme "
                   "entsprechend neu terminieren; Werte nach BLW (50 µg/l), BAR (15 µg/l) "
                   "und der EKA-Korrelation beurteilen."},
    # ── Nachgehende Untersuchungen, frühere Exposition ────────────────────
    {"wenn": {"frueher_krebs_stoffe": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 1.1 und 1.2.1",
     "befund": "Frühere Exposition gegenüber Arsen oder anderen krebserzeugenden "
               "Gefahrstoffen angegeben.",
     "konsequenz": "Frühere Expositionen in der Arbeitsanamnese dokumentieren (1.2.1). "
                   "Nachgehende Untersuchungen sicherstellen: bei bestehendem "
                   "Beschäftigungsverhältnis über den Arbeitgeber, nach Beendigung der "
                   "Beschäftigung über den Organisationsdienst für nachgehende "
                   "Untersuchungen (ODIN, www.odin-info.de) anmelden."},
    {"wenn": {"untersuchung_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitte 1.1 und 1.2.2",
     "befund": "Termin ist eine nachgehende Untersuchung nach Ende der Arsen-Tätigkeit.",
     "konsequenz": "Programm wie Nachuntersuchung anwenden (Anamnese, Urinstatus, "
                   "Laborprogramm, Untersuchung der Haut), ggf. radiologische Diagnostik "
                   "des Thorax; Durchführung über ODIN bzw. den zuständigen "
                   "Unfallversicherungsträger sicherstellen."},
    # ── Beratung (Abschnitt 2.2) ──────────────────────────────────────────
    {"wenn": {"rauchen": ["ja"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Aktives Rauchen angegeben.",
     "konsequenz": "Auf die Schädlichkeit des Zigarettenrauchens insbesondere in "
                   "Verbindung mit der Atemwegsexposition gegenüber Arsen hinweisen; "
                   "Tabakentwöhnung empfehlen."},
    {"wenn": {"psa_nutzung": ["teilweise", "nie"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen & Hygiene",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Persönliche Schutzausrüstung bzw. Hygieneregeln werden nicht oder nur "
               "teilweise eingehalten.",
     "konsequenz": "Auf allgemeine Hygienemaßnahmen und persönliche Schutzausrüstung "
                   "hinweisen (2.2, stoffspezifische Hinweise über GESTIS); die mögliche "
                   "keimzellmutagene Wirkung erwähnen. Bei Hinweisen auf unzureichenden "
                   "Arbeitsschutz Mitteilung an den Arbeitgeber zur Aktualisierung der "
                   "Gefährdungsbeurteilung, unter Wahrung der schutzwürdigen Belange."},
]
