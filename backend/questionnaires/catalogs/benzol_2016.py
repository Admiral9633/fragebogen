# -*- coding: utf-8 -*-
"""G 8 Benzol – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für arbeitsmedizinische
Untersuchungen, 5. Auflage 2016, G 8 »Benzol« (Fassung Oktober 2014), S. 187–196."""

SLUG = "g8-benzol-2016"

CATALOG = {
    "version": 2,
    "title": "G 8 Benzol (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 5. Auflage 2016, "
             "G 8 »Benzol« (Fassung Oktober 2014), S. 187–196",
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
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachuntersuchung: in der "
                            "Regel nach 6–12 Monaten. Nachgehende Untersuchung: nach dem Ausscheiden "
                            "aus der Tätigkeit mit Benzol.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich wurde schon einmal nach G 8 untersucht)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (Tätigkeit mit Benzol ist beendet)"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Benzol-Belastung ─────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Benzol-Belastung",
            "subtitle": "Ihre Arbeit und der mögliche Kontakt mit Benzol",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "benzol_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Bei welchen dieser Arbeiten können Sie mit Benzol oder benzolhaltigen "
                             "Produkten in Kontakt kommen?",
                    "hint": "Mehrfachauswahl möglich. Benzol steckt z. B. auch in Benzin "
                            "(Kraftstoff für Ottomotoren).",
                    "required": True,
                    "options": [
                        {"value": "herstellen_abfuellen",
                         "label": "Herstellen, Gewinnen, Weiterverarbeiten oder Transport von Benzol; "
                                  "Füllen, Entleeren oder Abfüllen von Fässern/Behältern"},
                        {"value": "ottokraftstoff", "label": "Umfüllen oder Abfüllen von Benzin (Kraftstoff für Ottomotoren)"},
                        {"value": "filter_probenahme", "label": "Filter- oder Katalysatorwechsel, Probenahme in Benzol-Anlagen"},
                        {"value": "tankreinigung", "label": "Reinigen von/in Tanks oder Behältern, Tankstellensanierung"},
                        {"value": "wartung_sanierung",
                         "label": "Reinigungs-, Wartungs-, Instandsetzungs-, Sanierungs- oder "
                                  "Abbrucharbeiten in Produktions- oder Abfüllanlagen"},
                        {"value": "kontaminiert", "label": "Arbeiten in verunreinigten Bereichen (z. B. Sondermüll, Altlasten)"},
                        {"value": "sonstige", "label": "Andere Arbeiten mit Benzol oder benzolhaltigen Produkten"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit mit Benzol, Benzin oder benzolhaltigen "
                             "Flüssigkeiten in Berührung?",
                    "hint": "Bei intensiver, großflächiger Benetzung der Haut wird Benzol auch über "
                            "die Haut aufgenommen. Auch durchnässte Kleidung zählt.",
                    "required": True,
                    "followup": {"id": "hautkontakt_desc", "type": "text",
                                 "label": "Bei welchen Arbeiten, und wie oft?", "when": "yes"},
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit möglichem Benzol-Kontakt?",
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
                    "id": "fruehere_exposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Berufen oder Tätigkeiten Kontakt mit Benzol "
                             "oder benzolhaltigen Produkten?",
                    "required": True,
                    "followup": {"id": "fruehere_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, in welchem Zeitraum?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Wie Sie sich bei der Arbeit schützen",
            "questions": [
                {
                    "id": "psa_benutzung",
                    "type": "multi_choice",
                    "label": "Welche persönliche Schutzausrüstung (PSA) benutzen Sie bei Arbeiten "
                             "mit möglichem Benzol-Kontakt?",
                    "hint": "Mehrfachauswahl möglich. Wegen der Aufnahme über die Haut ist "
                            "Schutzkleidung bei Benzol besonders wichtig.",
                    "required": True,
                    "options": [
                        {"value": "handschuhe", "label": "Geeignete Schutzhandschuhe"},
                        {"value": "schutzkleidung", "label": "Schutzkleidung"},
                        {"value": "atemschutz", "label": "Atemschutz"},
                        {"value": "schutzbrille", "label": "Schutzbrille"},
                        {"value": "keine", "label": "Keine Schutzausrüstung"},
                    ],
                },
                {
                    "id": "kleidung_wechsel",
                    "type": "yes_no",
                    "label": "Wechseln Sie mit Benzol oder Benzin benetzte Arbeitskleidung sofort "
                             "und waschen Sie betroffene Hautstellen gleich ab?",
                    "hint": "Allgemeine Hygienemaßnahmen verringern die Aufnahme über die Haut.",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Anzeichen, auf die bei Benzol besonders geachtet wird",
            "questions": [
                {
                    "id": "blutungsneigung",
                    "type": "yes_no",
                    "label": "Haben Sie eine erhöhte Blutungsneigung bemerkt – z. B. Zahnfleischbluten, "
                             "blaue Flecken (Blutergüsse) schon bei leichten Stößen oder eine "
                             "verstärkte/verlängerte Monatsblutung?",
                    "required": True,
                    "followup": {"id": "blutungsneigung_desc", "type": "textarea",
                                 "label": "Was genau, und seit wann?", "when": "yes"},
                },
                {
                    "id": "infektneigung",
                    "type": "yes_no",
                    "label": "Sind Sie in letzter Zeit auffällig oft krank, z. B. häufige Infekte "
                             "oder Entzündungen (vermehrte Infektneigung)?",
                    "required": True,
                },
                {
                    "id": "anaemie_symptome",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich ungewöhnlich müde, blass oder schnell erschöpft, "
                             "oder bekommen Sie bei Belastung schlecht Luft?",
                    "hint": "Solche Beschwerden können auf eine Blutarmut (Anämie) hinweisen.",
                    "required": True,
                },
                {
                    "id": "akutbeschwerden",
                    "type": "multi_choice",
                    "label": "Treten bei oder kurz nach der Arbeit folgende Beschwerden auf?",
                    "hint": "Mehrfachauswahl möglich. Benzol kann Haut und Schleimhäute reizen; "
                            "hohe Konzentrationen wirken betäubend (narkotisch).",
                    "required": True,
                    "options": [
                        {"value": "benommenheit", "label": "Benommenheit oder Schwindel"},
                        {"value": "kopfschmerzen", "label": "Kopfschmerzen"},
                        {"value": "uebelkeit", "label": "Übelkeit"},
                        {"value": "reizung", "label": "Gereizte Haut, Augen oder Atemwege (Brennen, Rötung)"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
            ],
        },
        # ── 5 ─ Seit der letzten Untersuchung ──────────────────────────────
        {
            "id": "zwischenanamnese",
            "title": "Seit der letzten Untersuchung",
            "subtitle": "Nur bei Nach- und nachgehenden Untersuchungen",
            "questions": [
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder längere "
                             "Erkrankung (z. B. mit Krankenhausaufenthalt oder längerer "
                             "Krankschreibung)?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutung",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Ihrer Erkrankungen "
                             "oder Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                    "followup": {"id": "zusammenhang_vermutung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung/Beschwerden, und warum vermuten Sie "
                                          "einen Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Vorerkrankungen und Alkohol ────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Alkohol",
            "subtitle": "Erkrankungen, die bei Benzol-Belastung besonders wichtig sind",
            "questions": [
                {
                    "id": "blut_erkrankung",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung des Blutes oder der blutbildenden Organe "
                             "(Knochenmark) bekannt – z. B. Blutarmut (Anämie), Mangel an weißen "
                             "Blutkörperchen oder Blutplättchen, Leukämie oder Lymphom?",
                    "required": True,
                    "followup": {"id": "blut_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, wie behandelt?", "when": "yes"},
                },
                {
                    "id": "chron_infektionen",
                    "type": "yes_no",
                    "label": "Haben Sie eine chronische bakterielle Infektion (dauerhafte oder "
                             "immer wiederkehrende Entzündung durch Bakterien)?",
                    "required": True,
                    "followup": {"id": "chron_infektionen_desc", "type": "text",
                                 "label": "Welche Infektion?", "when": "yes"},
                },
                {
                    "id": "alkohol_konsum",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Alkohol kann die schädigende Wirkung von Benzol auf das Blut verstärken "
                            "und die Laborwerte des Biomonitorings beeinflussen.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "selten", "label": "Selten (höchstens 1-mal pro Woche)"},
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
    # ── Bedenkenstatbestände (Abschnitt 2.1.1/2.1.2) ──────────────────────
    {"wenn": {"blut_erkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Hämatologische Erkrankung",
     "quelle": "Abschnitte 2.1.1/2.1.2 (Bedenken) und 1.2.3",
     "befund": "Erkrankung des Blutes bzw. der blutbildenden Organe angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1: dauernde gesundheitliche Bedenken erwägen; "
                   "bei zu erwartender Wiederherstellung befristete Bedenken nach 2.1.2. Großes "
                   "Blutbild, Vorbefunde einholen, in unklaren Fällen hämatologische Klärung "
                   "(Ergänzungsuntersuchung nach 1.2.3). Bei weniger ausgeprägter Erkrankung nach "
                   "2.1.3 prüfen, ob Aufnahme/Fortsetzung unter Voraussetzungen möglich ist "
                   "(technische/organisatorische Schutzmaßnahmen, Begrenzung der Expositionszeit, "
                   "Einsatz an Arbeitsplätzen mit geringerer Exposition, PSA, verkürzte "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"chron_infektionen": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Infektionen",
     "quelle": "Abschnitte 2.1.1/2.1.2 (Bedenken)",
     "befund": "Chronische bakterielle Infektion angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1 (chronische bakterielle Infektionen): Bedenken "
                   "gegen Aufnahme/Fortsetzung der Tätigkeit erwägen, bei erwartbarer "
                   "Wiederherstellung befristet nach 2.1.2. Ausprägung ärztlich klären (großes "
                   "Blutbild, ggf. hämatologische Klärung); bei geringer Ausprägung Voraussetzungen "
                   "nach 2.1.3 prüfen (Schutzmaßnahmen, verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"alkohol_abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 2.1.1 (Bedenken), 2.2 und 3.1.4",
     "befund": "Alkoholabhängigkeit angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1 (Alkoholabhängigkeit): Bedenken gegen "
                   "Aufnahme/Fortsetzung der Tätigkeit erwägen, bei erwartbarer Wiederherstellung "
                   "befristet nach 2.1.2. Beratung: Alkohol kann die benzolinduzierte "
                   "Hämatotoxizität verstärken; Hilfsangebote vermitteln. Alkoholkonsum als "
                   "Störfaktor (Confounder) bei der Interpretation des Biomonitorings beachten."},
    # ── Zielorgan-Symptome (Abschnitt 1.2.1, »besonders achten auf«) ──────
    {"wenn": {"blutungsneigung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Blutungsneigung",
     "quelle": "Abschnitte 1.2.1 und 1.2.3",
     "befund": "Erhöhte Blutungsneigung angegeben (z. B. Zahnfleischbluten, Sugillationen bei "
               "geringfügigen Traumen, Menorrhagien).",
     "konsequenz": "Anamnese vertiefen, großes Blutbild veranlassen; in unklaren Fällen "
                   "hämatologische Klärung (Ergänzungsuntersuchung nach 1.2.3). Ergebnis bei der "
                   "Beurteilung nach 2.1 berücksichtigen; ggf. vorzeitige Nachuntersuchung bzw. "
                   "verkürzte Nachuntersuchungsfrist."},
    {"wenn": {"infektneigung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Infektneigung",
     "quelle": "Abschnitte 1.2.1 und 1.2.3",
     "befund": "Vermehrte Infektneigung angegeben.",
     "konsequenz": "Großes Blutbild (mit Differenzialblutbild) veranlassen; in unklaren Fällen "
                   "hämatologische Klärung zur Abklärung einer möglichen Knochenmarksschädigung "
                   "durch Benzol (Ergänzungsuntersuchung nach 1.2.3)."},
    {"wenn": {"anaemie_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Anämie-Symptome",
     "quelle": "Abschnitte 3.2.3 und 1.2.3",
     "befund": "Müdigkeit, Blässe bzw. Belastungsluftnot angegeben (mögliche Anämie-Zeichen).",
     "konsequenz": "Großes Blutbild veranlassen (chronische Benzolwirkung kann das hämatopoetische "
                   "System schädigen, z. B. aplastische Anämie, Panzytopenie); in unklaren Fällen "
                   "hämatologische Klärung."},
    {"wenn": {"akutbeschwerden": ["benommenheit", "kopfschmerzen", "uebelkeit", "reizung"]},
     "schwere": "pruefen",
     "bereich": "Akutbeschwerden",
     "quelle": "Abschnitte 3.2.1/3.2.2 und 2.2",
     "befund": "Arbeitsplatzbezogene Beschwerden angegeben (narkotische Wirkung bzw. Reizung von "
               "Haut/Schleimhäuten).",
     "konsequenz": "Expositionssituation klären; Biomonitoring zum Expositions-/Schichtende "
                   "erwägen (Benzol im Vollblut, S-Phenylmerkaptursäure und t,t-Muconsäure im "
                   "Urin, Bewertung über EKA-Werte). Ergeben sich Hinweise auf unzureichenden "
                   "Arbeitsschutz, Mitteilung an den Arbeitgeber zur Aktualisierung der "
                   "Gefährdungsbeurteilung (Abschnitt 2.2) unter Wahrung der schutzwürdigen "
                   "Belange."},
    # ── Exposition und Schutzmaßnahmen (Abschnitte 3.1, 2.2) ──────────────
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitte 3.1.1, 3.1.3 und 2.2",
     "befund": "Hautkontakt mit Benzol bzw. benzolhaltigen Produkten angegeben.",
     "konsequenz": "Bei intensiver, großflächiger Benetzung ist mit perkutaner Aufnahme zu "
                   "rechnen: Expositionsbedingungen klären, Biomonitoring erwägen (erfasst auch "
                   "die Aufnahme über die Haut). Beratung: wegen der hautresorptiven Eigenschaften "
                   "von Benzol hat das Tragen von Schutzkleidung besondere Bedeutung "
                   "(stoffspezifische Hinweise in GESTIS, TRGS 401)."},
    {"wenn": {"psa_benutzung": ["keine"]},
     "wenn_nicht": {"benzol_taetigkeiten": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Schutzausrüstung",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Keine persönliche Schutzausrüstung trotz Tätigkeiten mit möglichem Benzol-Kontakt.",
     "konsequenz": "Intensive Beratung zu Hygienemaßnahmen und PSA – Schutzkleidung hat wegen der "
                   "Hautresorption besondere Bedeutung. Hinweis an den Arbeitgeber zur "
                   "Aktualisierung der Gefährdungsbeurteilung und Verbesserung des Arbeitsschutzes "
                   "(Abschnitt 2.2) unter Wahrung der schutzwürdigen Belange."},
    {"wenn": {"kleidung_wechsel": ["no"]},
     "wenn_nicht": {"benzol_taetigkeiten": ["keine"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Benetzte Arbeitskleidung wird nicht sofort gewechselt bzw. Haut nicht gereinigt.",
     "konsequenz": "Beratung zu allgemeinen Hygienemaßnahmen: benetzte Kleidung sofort wechseln, "
                   "Haut reinigen – wichtig wegen der Aufnahme von Benzol über die Haut."},
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenanamnese",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Tatbestand der vorzeitigen Nachuntersuchung: Erkrankung ärztlich bewerten, ob "
                   "sie Anlass zu Bedenken gegen die Fortsetzung der Tätigkeit geben könnte; "
                   "Untersuchungsprogramm vollständig durchführen (großes Blutbild, Biomonitoring), "
                   "ggf. verkürzte Nachuntersuchungsfrist festlegen."},
    {"wenn": {"zusammenhang_vermutung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenanamnese",
     "quelle": "Abschnitte 1.1 und 4 (Berufskrankheit)",
     "befund": "Proband/in vermutet einen Zusammenhang zwischen Erkrankung und Tätigkeit.",
     "konsequenz": "Tatbestand der vorzeitigen Nachuntersuchung (Beschäftigte, die einen "
                   "ursächlichen Zusammenhang vermuten): Beschwerden gezielt abklären (großes "
                   "Blutbild, ggf. hämatologische Klärung, Biomonitoring). Bei begründetem "
                   "Verdacht auf eine Berufskrankheit (BK-Nrn. 1303, 1317, 1318) BK-Anzeige "
                   "erstatten."},
    # ── Krebserzeugender Stoff: nachgehende Untersuchungen ────────────────
    {"wenn": {"untersuchung_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitte 1.1 und 1.2.2",
     "befund": "Termin im Rahmen der nachgehenden Untersuchung (Tätigkeit mit Benzol beendet).",
     "konsequenz": "Untersuchungsumfang: großes Blutbild; das Biomonitoring kann bei nachgehenden "
                   "Untersuchungen in der Regel entfallen. In unklaren Fällen hämatologische "
                   "Klärung. Nach Beendigung der Beschäftigung Organisation über den "
                   "Organisationsdienst für nachgehende Untersuchungen (ODIN, www.odin-info.de) "
                   "sicherstellen."},
    {"wenn": {"fruehere_exposition": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitte 1.1 und 2.2",
     "befund": "Frühere Tätigkeiten mit Benzol-Exposition angegeben.",
     "konsequenz": "Frühere Expositionen dokumentieren. Beratung zur krebserzeugenden und "
                   "erbgutverändernden Wirkung von Benzol und zu nachgehenden Untersuchungen nach "
                   "dem Ausscheiden aus der Tätigkeit (bei bestehendem Beschäftigungsverhältnis "
                   "durch den Betrieb, nach Beendigung der Beschäftigung über ODIN, "
                   "www.odin-info.de)."},
    # ── Beratung ──────────────────────────────────────────────────────────
    {"wenn": {"alkohol_konsum": ["regelmaessig", "taeglich"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 2.2 und 3.1.4",
     "befund": "Regelmäßiger bzw. täglicher Alkoholkonsum angegeben.",
     "konsequenz": "Beratung: konsumierter Alkohol kann die benzolinduzierte Hämatotoxizität "
                   "verstärken (Abschnitt 2.2). Alkoholkonsum als Störfaktor (Confounder) bei der "
                   "Interpretation der Biomonitoring-Ergebnisse berücksichtigen (Abschnitt 3.1.4)."},
]
