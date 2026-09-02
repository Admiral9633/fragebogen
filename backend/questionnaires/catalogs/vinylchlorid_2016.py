# -*- coding: utf-8 -*-
"""G 36 Vinylchlorid – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für arbeitsmedizinische
Untersuchungen, 5. Auflage 2016, G 36 »Vinylchlorid« (Fassung Oktober 2014), S. 509–518."""

SLUG = "g36-vinylchlorid-2016"

CATALOG = {
    "version": 2,
    "title": "G 36 Vinylchlorid (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 5. Auflage 2016, "
             "G 36 »Vinylchlorid« (Fassung Oktober 2014), S. 509–518",
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
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachuntersuchung: in "
                            "der Regel nach 12–24 Monaten. Nachgehende Untersuchung: nach dem "
                            "Ausscheiden aus der Tätigkeit mit Vinylchlorid.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich wurde schon einmal nach G 36 untersucht)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (Tätigkeit mit Vinylchlorid ist beendet)"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kontakt mit Vinylchlorid",
            "subtitle": "Ihre Arbeit und die mögliche Belastung durch Vinylchlorid",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_bereiche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie (oder sollen Sie arbeiten)?",
                    "hint": "Mehrfachauswahl möglich. Vinylchlorid ist ein farbloses Gas mit "
                            "leicht süßlichem Geruch, aus dem PVC-Kunststoff hergestellt wird.",
                    "required": True,
                    "options": [
                        {"value": "vc_herstellung", "label": "Vinylchlorid-Herstellung"},
                        {"value": "umfuellanlagen", "label": "Vinylchlorid-Umfüllanlagen"},
                        {"value": "pvc_herstellung", "label": "Anlagen zur PVC-Herstellung (Polyvinylchlorid)"},
                        {"value": "rueckgewinnung", "label": "Vinylchlorid-Rückgewinnungsanlagen"},
                        {"value": "reaktionsbehaelter", "label": "Arbeiten im Bereich von Reaktionsbehältern"},
                        {"value": "behaelter_reinigung", "label": "Manuelles Reinigen von Behältern"},
                        {"value": "sonstiges", "label": "Anderer Bereich"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit möglichem Kontakt zu "
                             "Vinylchlorid?",
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
                    "id": "frueher_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit Vinylchlorid oder "
                             "anderen Gefahrstoffen (z. B. Lösungsmitteln)?",
                    "required": True,
                    "followup": {"id": "frueher_expo_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit mit flüssigem Vinylchlorid oder "
                             "vinylchloridhaltigen Produkten in Berührung?",
                    "hint": "Vinylchlorid wird vor allem über die Atemwege, aber auch über die "
                            "Haut aufgenommen.",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzausrüstung ───────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzausrüstung & Hygiene",
            "subtitle": "Schutzmaßnahmen an Ihrem Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_tragen",
                    "type": "choice",
                    "label": "Tragen Sie die vorgesehene persönliche Schutzausrüstung "
                             "(z. B. Atemschutz, Schutzhandschuhe, Schutzkleidung)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "keine_noetig", "label": "Für meine Tätigkeit ist keine vorgesehen"},
                    ],
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, auf die bei Vinylchlorid besonders geachtet wird",
            "questions": [
                {
                    "id": "oberbauch",
                    "type": "yes_no",
                    "label": "Haben Sie Beschwerden im Oberbauch (z. B. Druck- oder "
                             "Völlegefühl, Schmerzen)?",
                    "hint": "Vinylchlorid kann vor allem die Leber belasten.",
                    "required": True,
                },
                {
                    "id": "appetit",
                    "type": "yes_no",
                    "label": "Haben Sie Appetitlosigkeit, besonders eine Abneigung gegen "
                             "fettes Essen?",
                    "required": True,
                },
                {
                    "id": "finger_missempfindungen",
                    "type": "yes_no",
                    "label": "Haben Sie Missempfindungen in den Fingern (z. B. Kribbeln, "
                             "Taubheitsgefühl)?",
                    "required": True,
                },
                {
                    "id": "finger_kalt_weiss",
                    "type": "yes_no",
                    "label": "Werden Ihre Finger anfallsartig weiß, kalt oder schmerzhaft "
                             "(sogenanntes Raynaud-Syndrom, »Leichenfinger«)?",
                    "required": True,
                },
                {
                    "id": "hautveraenderungen",
                    "type": "yes_no",
                    "label": "Haben Sie Verhärtungen oder Verdickungen der Haut, besonders an "
                             "Händen oder Unterarmen?",
                    "hint": "Vinylchlorid kann sklerodermieartige (bindegewebsverhärtende) "
                            "Hautveränderungen verursachen.",
                    "required": True,
                },
                {
                    "id": "schwindel",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach der Arbeit Schwindelgefühl, Müdigkeit oder "
                             "Benommenheit?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, die für die Beurteilung wichtig sind",
            "questions": [
                {
                    "id": "leber",
                    "type": "yes_no",
                    "label": "Hatten Sie in den letzten 2 Jahren eine Lebererkrankung, oder "
                             "besteht aktuell eine (z. B. Hepatitis, Fettleber, Leberzirrhose)?",
                    "required": True,
                    "followup": {"id": "leber_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "blutkrankheit",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung des Blutes oder der Blutbildung "
                             "bekannt (z. B. Blutarmut, Mangel an Blutplättchen)?",
                    "required": True,
                },
                {
                    "id": "nerven",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung des Gehirns oder der Nerven bekannt "
                             "(zentrales oder peripheres Nervensystem)?",
                    "required": True,
                },
                {
                    "id": "atemfunktion",
                    "type": "yes_no",
                    "label": "Ist Ihre Atmung oder Lungenfunktion erheblich eingeschränkt "
                             "(z. B. durch Asthma, COPD)?",
                    "required": True,
                },
                {
                    "id": "diabetes_insulin",
                    "type": "yes_no",
                    "label": "Haben Sie eine Zuckerkrankheit (Diabetes mellitus), die mit Insulin "
                             "behandelt wird?",
                    "required": True,
                },
                {
                    "id": "sucht",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen ein Missbrauch oder eine Abhängigkeit von Alkohol, "
                             "Medikamenten oder Drogen festgestellt?",
                    "hint": "Diese Angabe ist wichtig, weil die Leber bei Vinylchlorid das "
                            "wichtigste Zielorgan ist.",
                    "required": True,
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "text",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Verlauf seit der letzten Untersuchung ──────────────────────
        {
            "id": "verlauf",
            "title": "Seit der letzten Untersuchung",
            "subtitle": "Nur bei Nachuntersuchung",
            "questions": [
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder länger "
                             "dauernde Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen Beschwerden "
                             "und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie einen "
                                          "Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 7 ─ Einwilligung ───────────────────────────────────────────────
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
    {"wenn": {"leber": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Leber",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "In den letzten 2 Jahren durchgemachte oder bestehende Lebererkrankung angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken erwägen; Leberwerte (SGPT, SGOT, γ-GT, "
                   "alkalische Phosphatase) und Blutbild gezielt bewerten, erwünscht weitere "
                   "Leberdiagnostik und Oberbauchsonographie mit besonderer Darstellung der Leber. "
                   "Ist eine Wiederherstellung zu erwarten: befristete Bedenken (2.1.2). Bei "
                   "weniger ausgeprägtem Befund prüfen, ob unter Voraussetzungen nach 2.1.3 "
                   "(Schutzmaßnahmen, geringere Exposition, verkürzte Nachuntersuchungsfristen) "
                   "keine Bedenken bestehen."},
    {"wenn": {"blutkrankheit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Blut",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Systemische Blutkrankheit angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken erwägen; großes Blutbild mit Thrombozyten "
                   "gezielt bewerten, Vorbefunde einholen. Bei weniger ausgeprägter Erkrankung "
                   "Voraussetzungen nach 2.1.3 prüfen (u. a. verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"nerven": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Störung des zentralen oder peripheren Nervensystems angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken erwägen; Ausmaß ärztlich klären (ggf. "
                   "neurologische Vorbefunde). Bei weniger ausgeprägter Störung Voraussetzungen "
                   "nach 2.1.3 prüfen."},
    {"wenn": {"atemfunktion": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwege",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Erheblich eingeschränkte Atemfunktion angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken erwägen (Aufnahme von Vinylchlorid vorwiegend "
                   "über die Atemwege, ggf. Atemschutz erforderlich); Ausmaß klären. Bei geringerer "
                   "Ausprägung Voraussetzungen nach 2.1.3 prüfen, PSA unter Beachtung des "
                   "individuellen Gesundheitszustandes."},
    {"wenn": {"diabetes_insulin": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Stoffwechsel",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Insulinpflichtiger Diabetes mellitus angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken erwägen (eigener Bedenkenstatbestand des "
                   "G 36); Stoffwechseleinstellung klären. Bei stabiler, gut eingestellter "
                   "Erkrankung Voraussetzungen nach 2.1.3 prüfen (z. B. verkürzte "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Suchtmittel",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Missbrauch oder Abhängigkeit von Alkohol, Medikamenten oder Drogen angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken erwägen (zusätzliche Leberbelastung); "
                   "Leberdiagnostik gezielt bewerten. Ist eine Wiederherstellung zu erwarten "
                   "(z. B. nach Entzugsbehandlung): befristete Bedenken nach 2.1.2."},
    # ── Stoffspezifische Leitsymptome (Abschnitt 1.2.1) ───────────────────
    {"wenn": {"oberbauch": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 1.2.1 (besonders achten auf) und 1.2.2",
     "befund": "Oberbauchbeschwerden angegeben (stoffspezifisches Leitsymptom).",
     "konsequenz": "Gezielte Abklärung der Leber: Leberwerte bewerten, erwünschte weitere "
                   "Leberdiagnostik und Oberbauchsonographie mit besonderer Darstellung der Leber "
                   "durchführen; in unklaren Fällen Ergänzungsuntersuchung nach Ablaufplan."},
    {"wenn": {"appetit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 1.2.1 (besonders achten auf) und 1.2.2",
     "befund": "Appetitlosigkeit bzw. Abneigung gegen Fett angegeben (stoffspezifisches Leitsymptom).",
     "konsequenz": "Gezielte Leberdiagnostik wie bei Oberbauchbeschwerden: Leberwerte bewerten, "
                   "erwünscht weitere Leberdiagnostik und Oberbauchsonographie."},
    {"wenn": {"finger_missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Finger/Knochen",
     "quelle": "Abschnitte 1.2.1, 3.2.3 und 2.1.1",
     "befund": "Missempfindungen in den Fingern angegeben (mögliches Frühzeichen von "
               "Akroosteolyse/Durchblutungsstörung).",
     "konsequenz": "Abklärung auf Akroosteolyse (Knochenabbau der Fingerendglieder) und "
                   "Durchblutungsstörungen, ggf. fachärztliche Diagnostik; bei bestätigtem Befund "
                   "Bedenken nach 2.1.1 prüfen."},
    {"wenn": {"finger_kalt_weiss": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gefäßsystem",
     "quelle": "Abschnitte 3.2.3 und 2.1.1",
     "befund": "Anfallsartig weiße, kalte oder schmerzhafte Finger (Hinweis auf Raynaud-Syndrom).",
     "konsequenz": "Angiologische Abklärung veranlassen; Gefäßveränderungen (insbesondere "
                   "Raynaud-Syndrom) sind Bedenkenstatbestand nach 2.1.1 – bei Bestätigung "
                   "Bedenken prüfen, sonst Voraussetzungen nach 2.1.3."},
    {"wenn": {"hautveraenderungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 3.2.3 und 2.1.1",
     "befund": "Verhärtungen/Verdickungen der Haut angegeben (Verdacht auf sklerodermieartige "
               "Hautveränderungen).",
     "konsequenz": "Dermatologische Abklärung veranlassen; sklerodermieartige Hauterkrankungen "
                   "sind Bedenkenstatbestand nach 2.1.1 – bei Bestätigung Bedenken prüfen."},
    {"wenn": {"schwindel": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Wirkung",
     "quelle": "Abschnitte 1.2.1, 3.2.2 und 2.2",
     "befund": "Schwindelgefühl/Benommenheit bei oder nach der Arbeit angegeben.",
     "konsequenz": "Mögliche akute (pränarkotische) Wirkung von Vinylchlorid abklären; ergeben "
                   "sich Hinweise auf unzureichenden Arbeitsschutz, Mitteilung an den Arbeitgeber "
                   "zur Aktualisierung der Gefährdungsbeurteilung (unter Wahrung der "
                   "schutzwürdigen Belange der untersuchten Person)."},
    # ── Verlauf und Fristen (Abschnitt 1.1) ───────────────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder länger dauernde Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen eine Fortsetzung der "
                   "Tätigkeit geben könnte; vorzeitige Nachuntersuchung veranlassen bzw. den "
                   "Befund vor Ablauf der regulären Frist (12–24 Monate) abschließend bewerten."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitte 1.1 (vorzeitige Nachuntersuchung) und 4 (Berufskrankheit)",
     "befund": "Die Person vermutet einen ursächlichen Zusammenhang zwischen Erkrankung/Beschwerden "
               "und der Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung veranlassen; Beschwerden gezielt abklären und bei "
                   "begründetem Verdacht auf eine Berufskrankheit (BK-Nr. 1302, Erkrankungen durch "
                   "Halogenkohlenwasserstoffe) die Anzeige beim Unfallversicherungsträger prüfen."},
    # ── Schutzmaßnahmen und nachgehende Untersuchungen ────────────────────
    {"wenn": {"psa_tragen": ["selten", "nie"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Auf allgemeine Hygienemaßnahmen und das Tragen der persönlichen "
                   "Schutzausrüstung hinweisen; Beratung zur krebserzeugenden Wirkung von "
                   "Vinylchlorid. Bei Hinweisen auf unzureichenden Arbeitsschutz Mitteilung an "
                   "den Arbeitgeber zur Aktualisierung der Gefährdungsbeurteilung."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitte 3.1.3 (Aufnahme) und 2.2",
     "befund": "Regelmäßiger Hautkontakt mit Vinylchlorid bzw. vinylchloridhaltigen Produkten "
               "angegeben.",
     "konsequenz": "Beratung: Vinylchlorid wird auch über die Haut aufgenommen – Hautkontakt "
                   "vermeiden, Schutzhandschuhe/Schutzkleidung benutzen (TRGS 401 »Gefährdung "
                   "durch Hautkontakt« beachten)."},
    {"wenn": {"untersuchung_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitte 1.1 und 1.2 (nachgehende Untersuchungen, ODIN)",
     "befund": "Nachgehende Untersuchung nach Ausscheiden aus der Tätigkeit mit Vinylchlorid.",
     "konsequenz": "Untersuchungsprogramm wie Nachuntersuchung durchführen (Zwischenanamnese, "
                   "Urinstatus, großes Blutbild mit Thrombozyten, Leberwerte, alkalische "
                   "Phosphatase; Biomonitoring ist nach 1.2.2 nur bei der Nachuntersuchung "
                   "vorgesehen); Fortführung der nachgehenden Vorsorge über den "
                   "Organisationsdienst für nachgehende Untersuchungen (ODIN, www.odin-info.de) "
                   "sicherstellen."},
]
