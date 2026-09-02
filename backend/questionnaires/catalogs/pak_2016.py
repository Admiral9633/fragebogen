# -*- coding: utf-8 -*-
"""G 4 Gefahrstoffe, die Hautkrebs oder zur Krebsbildung neigende Hautveränderungen
hervorrufen – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für arbeitsmedizinische
Vorsorgeuntersuchungen, 6. Auflage 2016, G 4 (Fassung Oktober 2014), S. 145–154."""

SLUG = "g4-pak-2016"

CATALOG = {
    "version": 2,
    "title": "G 4 Gefahrstoffe, die Hautkrebs oder zur Krebsbildung neigende "
             "Hautveränderungen hervorrufen (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Vorsorgeuntersuchungen, "
             "6. Auflage 2016, G 4 »Gefahrstoffe, die Hautkrebs oder zur Krebsbildung "
             "neigende Hautveränderungen hervorrufen« (Fassung Oktober 2014), S. 145–154",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Welche Untersuchung steht bei Ihnen an?",
                    "hint": "Es geht um Stoffe wie Teer, Pech, Ruß und ähnliche "
                            "Verbrennungsprodukte (polycyclische aromatische Kohlen"
                            "wasserstoffe, kurz PAK), die Hautkrebs oder Hautveränderungen "
                            "mit Krebsrisiko hervorrufen können. Nachgehende Untersuchung: "
                            "Untersuchung nach dem Ende der Tätigkeit mit diesen Stoffen.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung – vor Aufnahme der Tätigkeit"},
                        {"value": "nach", "label": "Nachuntersuchung – ich arbeite bereits mit diesen Stoffen"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung – ich arbeite nicht mehr mit diesen Stoffen"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Belastung",
            "subtitle": "Ihre Arbeit mit Teer, Pech, Ruß oder Verbrennungsprodukten",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "taetigkeitsbereiche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie (oder haben Sie gearbeitet)?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "kokerei", "label": "Ofenarbeiten in einer Steinkohlekokerei"},
                        {"value": "festpech", "label": "Lagern, Transport oder Verarbeitung von Festpech "
                                                       "für Elektroden"},
                        {"value": "feuerfest", "label": "Herstellen/Verarbeiten von Feuerfestmaterial "
                                                        "mit Teerpechbindung"},
                        {"value": "elektroden", "label": "Anschlagen gebrannter Elektroden zur "
                                                         "Aluminiumgewinnung oder Herstellen von Kleinkörpern "
                                                         "aus Kohlenstoff/Elektrographit"},
                        {"value": "metall", "label": "Metallerzeugung: Hochofen-Abstich oder "
                                                     "Pfannenfeuerplatz in der Stahlerzeugung"},
                        {"value": "teerauftrag", "label": "Spritzauftrag von Teer bzw. Teer-/Epoxid-"
                                                          "Beschichtungen (Korrosionsschutz)"},
                        {"value": "sanierung", "label": "Herstellen/Demontage von Kork-Teer-Dämmungen oder "
                                                        "Entfernen von Holzpflaster mit Teerpech-Heißkleber"},
                        {"value": "brennschneiden", "label": "Brennschneidarbeiten an teerbehafteten Teilen"},
                        {"value": "schornstein", "label": "Schornsteinreinigung von Feuerungen mit "
                                                          "Braunkohle, Steinkohle oder Holz"},
                        {"value": "sonstige", "label": "Andere Tätigkeit mit Teer, Pech, Ruß oder "
                                                       "Verbrennungsrückständen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit diesen Stoffen "
                             "(bzw. wie lange haben Sie damit gearbeitet)?",
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
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit direkt mit Teer, Pech, Ruß "
                             "oder deren Dämpfen in Kontakt?",
                    "hint": "Diese Stoffe können auch über die Haut in den Körper gelangen "
                            "(hautresorptiv). Auch verschmutzte Arbeitskleidung kann die "
                            "Haut schädigen.",
                    "required": True,
                },
                {
                    "id": "inhalativ_exposition",
                    "type": "yes_no",
                    "label": "Atmen Sie bei der Arbeit Rauch, Dämpfe oder Staub dieser "
                             "Stoffe ein (z. B. bei heißer Verarbeitung)?",
                    "hint": "Je nach Verarbeitungstemperatur können die Stoffe auch über "
                            "die Atemwege aufgenommen werden.",
                    "required": True,
                },
                {
                    "id": "frueher_exposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Berufen oder Tätigkeiten Kontakt mit "
                             "Teer, Pech, Ruß oder anderen krebserzeugenden Stoffen?",
                    "required": True,
                    "followup": {"id": "frueher_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, und wie lange?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Ihre Schutzausrüstung am Arbeitsplatz",
            "questions": [
                {
                    "id": "psa",
                    "type": "multi_choice",
                    "label": "Welche Schutzausrüstung benutzen Sie bei diesen Arbeiten?",
                    "hint": "Mehrfachauswahl möglich. Wegen der Aufnahme über die Haut ist "
                            "der Hautschutz besonders wichtig.",
                    "required": True,
                    "options": [
                        {"value": "handschuhe", "label": "Geeignete Schutzhandschuhe"},
                        {"value": "atemschutz", "label": "Atemschutz (Maske)"},
                        {"value": "schutzkleidung", "label": "Schutzkleidung / regelmäßiger Wechsel der Arbeitskleidung"},
                        {"value": "hautschutz", "label": "Hautschutz- und Hautpflegemittel"},
                        {"value": "keine", "label": "Keine Schutzausrüstung"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie gesundheitliche Probleme mit der Schutzausrüstung "
                             "(z. B. Hautprobleme unter Handschuhen, Beschwerden unter Atemschutz)?",
                    "required": True,
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Haut ───────────────────────────────────────────────────────
        {
            "id": "haut",
            "title": "Haut",
            "subtitle": "Beschwerden und Vorerkrankungen der Haut",
            "questions": [
                {
                    "id": "haut_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie derzeit Hautbeschwerden?",
                    "hint": "Die genannten Stoffe können entzündliche Rötungen, Ekzeme "
                            "mit Juckreiz und Lichtempfindlichkeit der Haut hervorrufen.",
                    "required": True,
                    "options": [
                        {"value": "juckreiz", "label": "Juckreiz"},
                        {"value": "roetung", "label": "Hautrötungen, Entzündungen oder Ekzem (nässender/"
                                                      "schuppender Ausschlag)"},
                        {"value": "pigment", "label": "Dunkle Verfärbungen oder Flecken der Haut "
                                                      "(Pigmentveränderungen)"},
                        {"value": "keine", "label": "Nein, keine Hautbeschwerden"},
                    ],
                },
                {
                    "id": "hautveraenderungen",
                    "type": "yes_no",
                    "label": "Haben Sie neue oder veränderte Hautstellen bemerkt – z. B. "
                             "Warzen, raue verhornte Stellen oder schlecht heilende Stellen?",
                    "hint": "Sogenannte Teer- oder Pechwarzen treten bevorzugt im Gesicht, "
                            "an den Ohren, am Handrücken, mitunter auch an Unterarm, "
                            "Unterbauch und im Genitalbereich auf – teils erst Jahre nach "
                            "dem Ende der Tätigkeit.",
                    "required": True,
                    "followup": {"id": "hautveraenderungen_desc", "type": "textarea",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "sonnenempfindlichkeit",
                    "type": "yes_no",
                    "label": "Ist Ihre Haut besonders empfindlich gegen Sonnenlicht "
                             "(schnelle Rötung, Sonnenbrand, Lichtreaktionen)?",
                    "hint": "UV-Licht kann die Haut zusätzlich schädigen; die Stoffe können "
                            "die Lichtempfindlichkeit weiter steigern.",
                    "required": True,
                },
                {
                    "id": "hautkrebs_vorgeschichte",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal Hautkrebs oder eine Vorstufe davon "
                             "(z. B. aktinische Keratose, Basaliom) – auch wenn er erfolgreich "
                             "behandelt wurde?",
                    "required": True,
                    "followup": {"id": "hautkrebs_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "hauterkrankungen",
                    "type": "multi_choice",
                    "label": "Bestehen bei Ihnen Hauterkrankungen oder besondere Hautzustände?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "ekzemneigung", "label": "Neigung zu Ekzemen (juckende, entzündete "
                                                           "Hautausschläge)"},
                        {"value": "akne", "label": "Akne (über die gewöhnliche Jugend-Akne hinaus)"},
                        {"value": "seborrhoe", "label": "Seborrhoe (auffallend fettige Haut)"},
                        {"value": "vitiligo", "label": "Ausgedehnte Vitiligo (Weißfleckenkrankheit)"},
                        {"value": "ichthyose", "label": "Ausgeprägte Ichthyose (Fischschuppenkrankheit)"},
                        {"value": "porphyrie", "label": "Porphyria cutanea tarda (Stoffwechselerkrankung mit "
                                                        "Blasenbildung an lichtausgesetzter Haut)"},
                        {"value": "lichtschaeden", "label": "Deutliche Lichtschäden der Haut "
                                                            "(»Seemanns-« oder »Landmannshaut«)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
            ],
        },
        # ── 5 ─ Weitere Organe ─────────────────────────────────────────────
        {
            "id": "weitere_organe",
            "title": "Atemwege & Harnwege",
            "subtitle": "Die Stoffe können auch andere Organe betreffen",
            "questions": [
                {
                    "id": "atem_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie derzeit Beschwerden der Atemwege?",
                    "hint": "Bei Aufnahme über die Atemwege können im Einzelfall auch "
                            "Kehlkopf oder Lunge betroffen sein.",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Husten"},
                        {"value": "heiserkeit", "label": "Anhaltende Heiserkeit"},
                        {"value": "auswurf", "label": "Auswurf (Schleim beim Husten)"},
                        {"value": "atemnot", "label": "Atemnot / Luftnot"},
                        {"value": "keine", "label": "Nein, keine Beschwerden"},
                    ],
                },
                {
                    "id": "blut_urin",
                    "type": "yes_no",
                    "label": "Haben Sie Blut im Urin bemerkt (auch nur einmal, z. B. rötliche "
                             "oder bräunliche Verfärbung)?",
                    "required": True,
                },
            ],
        },
        # ── 6 ─ Gesundheitliche Entwicklung ────────────────────────────────
        {
            "id": "verlauf",
            "title": "Gesundheitliche Entwicklung",
            "subtitle": "Erkrankungen seit der letzten Untersuchung",
            "questions": [
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "not_in": ["erst"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung "
                             "bei Ihnen und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "not_in": ["erst"]},
                    "followup": {"id": "verdacht_zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und warum vermuten Sie den "
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
    # ── Dauernde gesundheitliche Bedenken (Abschnitt 2.1.1) ───────────────
    {"wenn": {"hautkrebs_vorgeschichte": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Hautkrebserkrankung und/oder deren Vorstufen (auch nach erfolgreicher "
               "Behandlung) angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken gegen Aufnahme/Fortsetzung der "
                   "Tätigkeit nach 2.1.1 prüfen – Hautkrebs und Vorstufen gelten auch nach "
                   "erfolgreicher Behandlung als Bedenkenstatbestand. Hautfachärztliche "
                   "Befunde einholen; Ganzkörperinspektion durchführen und dokumentieren."},
    {"wenn": {"sonnenempfindlichkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Empfindlichkeit der Haut gegenüber UV-Strahlen/Sonnenlicht angegeben.",
     "konsequenz": "Ausprägung ärztlich klären: Bei anamnestisch bekannter ausgeprägter "
                   "UV-Empfindlichkeit dauernde gesundheitliche Bedenken nach 2.1.1. Bei "
                   "besonders lichtempfindlicher Haut geringerer Ausprägung Tätigkeit nur "
                   "unter Voraussetzungen nach 2.1.3 (Schutzmaßnahmen) mit verkürzter "
                   "Nachuntersuchungsfrist von 12 Monaten; auf UV-Empfindlichkeit achten, "
                   "Lichtschutz beraten."},
    {"wenn": {"hauterkrankungen": ["vitiligo", "ichthyose", "porphyrie", "lichtschaeden",
                                   "seborrhoe"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Bedenkenrelevante Hauterkrankung angegeben (ausgedehnte Vitiligo, "
               "ausgeprägte Ichthyose, Porphyria cutanea tarda, Seemanns-/Landmannshaut "
               "oder Seborrhoe).",
     "konsequenz": "Ausprägung ärztlich beurteilen: Bei schwerer Ausprägung (ausgedehnte "
                   "Vitiligo, ausgeprägte Ichthyose, Porphyria cutanea tarda, deutlich "
                   "ausgebildete Seemanns-/Landmannshaut, ausgeprägte Seborrhoe) dauernde "
                   "gesundheitliche Bedenken nach 2.1.1. Bei weniger ausgeprägten Formen "
                   "keine Bedenken unter Voraussetzungen nach 2.1.3: technische/"
                   "organisatorische Schutzmaßnahmen, Expositionsbegrenzung, PSA, verkürzte "
                   "Nachuntersuchungsfristen (bei mäßiger Seborrhoe 12 Monate)."},
    # ── Verkürzte Fristen nach 2.1.3 ──────────────────────────────────────
    {"wenn": {"hauterkrankungen": ["ekzemneigung", "akne"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 2.1.3 (Keine Bedenken unter bestimmten Voraussetzungen)",
     "befund": "Ekzemneigung oder Akne (über einfache Akne juvenilis hinaus) angegeben.",
     "konsequenz": "Keine gesundheitlichen Bedenken nur unter Voraussetzungen nach 2.1.3: "
                   "Schutzmaßnahmen sicherstellen und verkürzte Nachuntersuchungsfrist von "
                   "12 Monaten festlegen (Personen mit Akne außer einfacher Akne juvenilis "
                   "bzw. mit Ekzemneigung)."},
    # ── Hautbefunde (Abschnitte 1.2.2 und 3.2) ────────────────────────────
    {"wenn": {"hautveraenderungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 1.2.2 (Spezielle Untersuchung, Nachuntersuchung/nachgehende "
               "Untersuchung)",
     "befund": "Neue oder veränderte Hautstellen (Warzen, Verhornungen, schlecht heilende "
               "Stellen) angegeben.",
     "konsequenz": "Ganzkörperinspektion (einschließlich Skrotalbereich) mit besonderem "
                   "Augenmerk auf suspekte Veränderungen (Keratosen, Teer-/Pechwarzen, "
                   "Basaliome, Plattenepithelkarzinome u. a.). Bei Vorhandensein von Warzen "
                   "hautfachärztliche Untersuchung, evtl. Exzision und histologische "
                   "Untersuchung; ggf. Fotodokumentation des Hautbefundes zur "
                   "Vergleichskontrolle."},
    {"wenn": {"haut_beschwerden": ["juckreiz", "roetung", "pigment"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 3.2 (Funktionsstörungen, Krankheitsbild)",
     "befund": "Aktuelle Hautbeschwerden (Juckreiz, Rötung/Ekzem oder Pigmentveränderungen) "
               "angegeben.",
     "konsequenz": "Hautstatus gezielt erfassen: entzündliche Rötung, Dermatitis, "
                   "Hyperpigmentierung/Melanose, Follikulitiden oder Akne abklären; "
                   "Zusammenhang mit der Exposition prüfen. Bei unklarem oder suspektem "
                   "Befund hautfachärztliche Vorstellung; Hautschutzberatung intensivieren."},
    # ── Inhalative Exposition → G 40 (Abschnitte 1.2.2 und 3.2) ───────────
    {"wenn": {"inhalativ_exposition": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Inhalative Exposition",
     "quelle": "Abschnitte 1.2.2 (Erwünscht) und 3.2",
     "befund": "Neben Hautkontakt auch inhalative Exposition (Rauch, Dämpfe, Staub) "
               "angegeben.",
     "konsequenz": "Prüfen, ob die Untersuchungen nicht unter Beachtung des Grundsatzes "
                   "G 40 »Krebserzeugende Gefahrstoffe – allgemein« durchzuführen sind "
                   "(erhöhte inhalative Exposition; systemische Karzinome wie Kehlkopf- "
                   "oder Lungenkrebs möglich). Abgleich mit der Gefährdungsbeurteilung."},
    {"wenn": {"atem_beschwerden": ["husten", "heiserkeit", "auswurf", "atemnot"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitt 3.2",
     "befund": "Atemwegsbeschwerden (Husten, Heiserkeit, Auswurf oder Atemnot) angegeben.",
     "konsequenz": "Beschwerden ärztlich abklären; bei inhalativer Aufnahme sind im "
                   "Einzelfall systemische Karzinome (Kehlkopf-, Lungenkrebs) zu "
                   "berücksichtigen (BK-Nrn. 4110, 4113). Prüfen, ob Untersuchungen nach "
                   "G 40 »Krebserzeugende Gefahrstoffe – allgemein« angezeigt sind."},
    {"wenn": {"blut_urin": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Harnwege",
     "quelle": "Abschnitte 1.2.2 (Urinstatus) und 3.2",
     "befund": "Blut im Urin (Hämaturie) angegeben.",
     "konsequenz": "Urinstatus (Mehrfachteststreifen) gezielt auswerten und zeitnahe "
                   "urologische Abklärung veranlassen; ein Zusammenhang der Exposition mit "
                   "Blasenkrebs wird diskutiert und ist bei der Untersuchung zu "
                   "berücksichtigen."},
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen: klären, ob die Erkrankung "
                   "Anlass zu Bedenken gegen die Fortsetzung der Tätigkeit gibt "
                   "(Beurteilung nach 2.1); Befunde und Vorbefunde einbeziehen."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Vorzeitige Nachuntersuchung)",
     "befund": "Proband vermutet ursächlichen Zusammenhang zwischen Erkrankung und "
               "Tätigkeit am Arbeitsplatz.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen; Verdacht dokumentieren und "
                   "abklären. Bei begründetem Verdacht auf eine Berufskrankheit "
                   "(BK-Nrn. 4110, 4113, 5102) BK-Anzeige erstatten."},
    # ── Schutzmaßnahmen und Beratung (Abschnitte 2.1.3 und 2.2) ───────────
    {"wenn": {"psa": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Keine persönliche Schutzausrüstung bei Tätigkeiten mit hautkrebs-"
               "erzeugenden Gefahrstoffen angegeben.",
     "konsequenz": "Auf allgemeine Hygienemaßnahmen und persönliche Schutzausrüstung "
                   "hinweisen; wegen der hautresorptiven Eigenschaften kommt dem "
                   "Hautschutz besondere Bedeutung zu. Ergibt sich ein Hinweis auf "
                   "notwendige Aktualisierung der Gefährdungsbeurteilung, dies dem "
                   "Arbeitgeber mitteilen (unter Wahrung der schutzwürdigen Belange des "
                   "Untersuchten)."},
    {"wenn": {"psa_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 2.1.3",
     "befund": "Gesundheitliche Probleme mit der persönlichen Schutzausrüstung angegeben.",
     "konsequenz": "Persönliche Schutzausrüstung unter Beachtung des individuellen "
                   "Gesundheitszustandes auswählen bzw. anpassen (2.1.3); geeignete "
                   "Handschuh- und Hautschutzauswahl beraten."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitte 2.2 und 3.2.1",
     "befund": "Direkter Hautkontakt mit Teer, Pech, Ruß oder deren Dämpfen angegeben.",
     "konsequenz": "Beratung: Schädigung auch durch Staub, Dämpfe und behaftete "
                   "Arbeitskleidung möglich; Hitze und mechanische Reize begünstigen dies. "
                   "Zu Hautschutz, Hygiene und Kleidungswechsel anleiten; zur regelmäßigen "
                   "Selbstbeobachtung der Haut und ggf. zum Lichtschutz motivieren."},
    # ── Nachgehende Untersuchungen (Abschnitte 1.1 und 1.2.2) ─────────────
    {"wenn": {"frueher_exposition": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitt 1.1 (Nachgehende Untersuchungen)",
     "befund": "Frühere Tätigkeiten mit Exposition gegenüber Teer, Pech, Ruß oder anderen "
               "Karzinogenen angegeben.",
     "konsequenz": "Frühere Expositionszeiten und -umstände dokumentieren. Prüfen, ob "
                   "nachgehende Untersuchungen angezeigt sind bzw. eine Meldung an den "
                   "Organisationsdienst für nachgehende Untersuchungen (ODIN, "
                   "www.odin-info.de) erfolgt ist – Hautveränderungen können auch noch "
                   "Jahre nach Expositionsende auftreten."},
    {"wenn": {"untersuchung_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitte 1.1 und 1.2.2",
     "befund": "Termin im Rahmen der nachgehenden Untersuchung (nach Ausscheiden aus der "
               "Tätigkeit bzw. Beendigung der Beschäftigung).",
     "konsequenz": "Programm der Nachuntersuchung anwenden: Urinstatus "
                   "(Mehrfachteststreifen), spezielle Anamnese zu Hautveränderungen und "
                   "Sonnenlichtempfindlichkeit, Ganzkörperinspektion einschließlich "
                   "Skrotalbereich; bei Warzen hautfachärztliche Untersuchung. Das "
                   "Biomonitoring (1-Hydroxypyren im Urin) entfällt bei nachgehenden "
                   "Untersuchungen. Organisation über ODIN (www.odin-info.de) "
                   "sicherstellen."},
]
