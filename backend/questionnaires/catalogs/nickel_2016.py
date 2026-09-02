# -*- coding: utf-8 -*-
"""G 38 Nickel oder seine Verbindungen – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze
für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 38 »Nickel oder seine
Verbindungen« (Fassung Oktober 2014), S. 529–540."""

SLUG = "g38-nickel-2016"

CATALOG = {
    "version": 2,
    "title": "G 38 Nickel oder seine Verbindungen (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 38 »Nickel oder seine Verbindungen« (Fassung Oktober 2014), S. 529–540",
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
                    "label": "Welche Untersuchung nach G 38 ist dies für Sie?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachuntersuchung: "
                            "in der Regel nach 24 bis 60 Monaten. Nachgehende Untersuchung: "
                            "nach dem Ende der Tätigkeit mit Nickel.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich wurde schon einmal nach G 38 untersucht)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (die Tätigkeit mit Nickel ist beendet)"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Nickelkontakt",
            "subtitle": "Ihre Arbeit mit Nickel oder seinen Verbindungen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten haben Sie Kontakt mit Nickel, "
                             "Nickelverbindungen oder nickelhaltigen Stäuben/Rauchen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "schweissen", "label": "Schweißen, thermisches Spritzen oder Plasma-/Laserschneiden "
                                                         "von Nickel, Nickellegierungen oder Chrom-Nickel-Stahl"},
                        {"value": "elektrolyse", "label": "Elektrolytische Nickelgewinnung / elektrolytisches "
                                                          "Abscheiden von Nickel"},
                        {"value": "galvanik", "label": "Galvanik (z. B. offene, warme Nickelbäder)"},
                        {"value": "pulver", "label": "Herstellen oder Verarbeiten von Nickel oder "
                                                     "Nickelverbindungen in Pulverform"},
                        {"value": "erz", "label": "Aufbereiten/Verarbeiten von Nickelerzen "
                                                  "(auch Arbeiten an Staubfiltern)"},
                        {"value": "schleifen", "label": "Schleifen oder Polieren von Nickel oder nickelhaltigen "
                                                        "Legierungen (z. B. Magnete)"},
                        {"value": "giesserei", "label": "Gießerei/Stahlwerk: Zulegieren von Nickel, nickelhaltige "
                                                        "Spezialstähle"},
                        {"value": "katalysator", "label": "Feinverteiltes Nickel als Katalysator (z. B. Fetthärtung)"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an Produktionsanlagen für Nickel"},
                        {"value": "tetracarbonyl", "label": "Tätigkeiten mit Nickeltetracarbonyl "
                                                            "(z. B. Mondprozess) oder möglicher Hautkontakt damit"},
                        {"value": "andere", "label": "Andere Tätigkeit mit Nickelkontakt"},
                        {"value": "keine", "label": "Keine davon / weiß nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt mit Nickel oder seinen Verbindungen?",
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
                    "id": "frueher_krebsstoffe",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Tätigkeiten anderen krebserzeugenden "
                             "Gefahrstoffen ausgesetzt (z. B. Chromate, Asbest, Quarzstaub, "
                             "Schweißrauche)?",
                    "required": True,
                    "followup": {"id": "frueher_krebsstoffe_desc", "type": "textarea",
                                 "label": "Welche Stoffe, welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Schutz vor Staub, Rauch und Hautkontakt",
            "questions": [
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei staub- oder rauchintensiven Arbeiten Atemschutz?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_erforderlich", "label": "Atemschutz ist bei mir nicht vorgesehen"},
                    ],
                },
                {
                    "id": "handschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei Hautkontakt mit nickelhaltigen Materialien oder "
                             "Lösungen Schutzhandschuhe?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_hautkontakt", "label": "Ich habe keinen Hautkontakt"},
                    ],
                },
                {
                    "id": "hygiene_essen",
                    "type": "yes_no",
                    "label": "Essen, trinken oder rauchen Sie manchmal direkt am Arbeitsplatz?",
                    "hint": "Über verschmutzte Hände kann Nickel in den Mund gelangen.",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Atemwege, Nase und Haut",
            "questions": [
                {
                    "id": "atembeschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Husten, Auswurf oder Atemnot?",
                    "required": True,
                    "followup": {"id": "atembeschwerden_desc", "type": "text",
                                 "label": "Seit wann, und in welchen Situationen?", "when": "yes"},
                },
                {
                    "id": "ekzem",
                    "type": "yes_no",
                    "label": "Haben Sie Hautekzeme – juckende, gerötete oder nässende Hautstellen –, "
                             "besonders an Händen oder Unterarmen?",
                    "required": True,
                    "followup": {"id": "ekzem_desc", "type": "text",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "nase_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Beschwerden an der Nase, z. B. dauerhaft behinderte "
                             "Nasenatmung, häufiges Nasenbluten, wiederkehrende "
                             "Nebenhöhlen-Entzündungen oder einen schlechten Geruchssinn?",
                    "required": True,
                    "followup": {"id": "nase_beschwerden_desc", "type": "text",
                                 "label": "Welche Beschwerden, und seit wann?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen und Allergien ──────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Allergien",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "nickelallergie",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Nickelallergie bekannt (z. B. Hautausschlag durch "
                             "Modeschmuck, Uhren, Brillen oder Jeansknöpfe)?",
                    "required": True,
                },
                {
                    "id": "allergie_disposition",
                    "type": "yes_no",
                    "label": "Neigen Sie zu Allergien (z. B. Heuschnupfen, allergisches Asthma, "
                             "Neurodermitis)?",
                    "required": True,
                    "followup": {"id": "allergie_disposition_desc", "type": "text",
                                 "label": "Welche Allergien?", "when": "yes"},
                },
                {
                    "id": "atemwegserkrankungen",
                    "type": "multi_choice",
                    "label": "Hatten oder haben Sie Erkrankungen der Atemwege oder Lunge?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "schwere_obstruktion", "label": "Schwere Verengung der Atemwege "
                                                                  "(z. B. schweres Asthma, schwere COPD)"},
                        {"value": "asthma", "label": "Asthma bronchiale (leichter ausgeprägt)"},
                        {"value": "chronische_bronchitis", "label": "Chronische Bronchitis (Husten mit Auswurf über Monate)"},
                        {"value": "bronchiektasen", "label": "Bronchiektasen (krankhaft erweiterte Bronchien)"},
                        {"value": "pleuraschwarten", "label": "Pleuraschwarten (Verwachsungen des Rippenfells)"},
                        {"value": "andere", "label": "Andere Atemwegs- oder Lungenerkrankung"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "hauterkrankung",
                    "type": "yes_no",
                    "label": "Hatten oder haben Sie Hauterkrankungen (z. B. Ekzeme, "
                             "Kontaktallergien der Haut)?",
                    "required": True,
                    "followup": {"id": "hauterkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder längere "
                             "Erkrankung (z. B. Krankenhausaufenthalt, lange Krankschreibung)?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung oder "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {"id": "verdacht_zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den Zusammenhang?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Raucheranamnese – Rauchen belastet dieselben Organe wie Nickelstäube",
            "questions": [
                {
                    "id": "rauchstatus",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "frueher", "label": "Früher, ich habe aufgehört"},
                        {"value": "aktuell", "label": "Ja, ich rauche"},
                    ],
                    "followup": {"id": "rauchstatus_desc", "type": "text",
                                 "label": "Was und wie viel pro Tag, seit wann?", "when": "aktuell"},
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
    # ── Bedenkentatbestände nach 2.1.1 (Atemwege) ─────────────────────────
    {"wenn": {"atemwegserkrankungen": ["schwere_obstruktion"]},
     "schwere": "kritisch",
     "bereich": "Atemwege",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Schwere Atemwegsobstruktion angegeben.",
     "konsequenz": "Bedenkentatbestand nach 2.1.1: Bei schweren Gesundheitsstörungen der "
                   "Atemwege dauernde gesundheitliche Bedenken gegen Aufnahme bzw. "
                   "Fortsetzung der Tätigkeit prüfen; Spirometrie und Vorbefunde heranziehen. "
                   "Ist eine Wiederherstellung zu erwarten, befristete Bedenken (2.1.2) "
                   "aussprechen und Nachuntersuchung vor Fristablauf ansetzen."},
    {"wenn": {"atemwegserkrankungen": ["chronische_bronchitis", "bronchiektasen",
                                       "pleuraschwarten"]},
     "schwere": "kritisch",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3",
     "befund": "Chronische Bronchitis, Bronchiektasen oder Pleuraschwarten angegeben.",
     "konsequenz": "Nach 2.1.1 als Bedenkentatbestand werten und Ausprägung klären "
                   "(Spirometrie, ggf. radiologische Diagnostik des Thorax). Bei weniger "
                   "ausgeprägtem Befund keine Bedenken unter bestimmten Voraussetzungen "
                   "(2.1.3): technische/organisatorische Schutzmaßnahmen, Einsatz an "
                   "Arbeitsplätzen mit geringerer Exposition, PSA, verkürzte "
                   "Nachuntersuchungsfristen."},
    {"wenn": {"atemwegserkrankungen": ["asthma", "andere"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 1.2.1 (allgemeine Untersuchung) und 2.1.3",
     "befund": "Atemwegs-/Lungenerkrankung leichterer Ausprägung angegeben.",
     "konsequenz": "Erkrankungen der Atemwege in der Anamnese vertiefen; Spirometrie "
                   "sorgfältig bewerten. Prüfen, ob die Tätigkeit unter bestimmten "
                   "Voraussetzungen (2.1.3) möglich ist – z. B. Schutzmaßnahmen, geringere "
                   "Exposition, verkürzte Nachuntersuchungsfristen."},
    # ── Bedenkentatbestände nach 2.1.1 (Haut) ─────────────────────────────
    {"wenn": {"hauterkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "Abschnitte 2.1.1 und 1.2.3",
     "befund": "Hauterkrankung (Ekzem/Hautallergie) in der Vorgeschichte oder aktuell.",
     "konsequenz": "Erkrankungen der Haut (Ekzeme und Hautallergien) sind Bedenkentatbestand "
                   "nach 2.1.1: Ausprägung klären, bei unklaren allergischen "
                   "Hauterkrankungen hautärztliche Ergänzungsuntersuchung veranlassen. Bei "
                   "weniger ausgeprägtem Befund Voraussetzungen nach 2.1.3 prüfen "
                   "(Schutzmaßnahmen, verkürzte Nachuntersuchungsfristen); bei erwarteter "
                   "Wiederherstellung befristete Bedenken (2.1.2)."},
    {"wenn": {"nickelallergie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Haut/Sensibilisierung",
     "quelle": "Abschnitte 2.1.1, 3.2.1 und 3.2.3",
     "befund": "Bekannte Nickelallergie (Kontaktsensibilisierung) angegeben.",
     "konsequenz": "Sensibilisierung gegenüber dem Arbeitsstoff selbst: als Hautallergie "
                   "Bedenkentatbestand nach 2.1.1 werten und vor Aufnahme bzw. Fortsetzung "
                   "der Tätigkeit klären. Auf allergische Ekzeme (vereinzelt begleitet von "
                   "allergischem Bronchialasthma) achten; Hautkontakt konsequent vermeiden, "
                   "sonst Bedenken aussprechen."},
    {"wenn": {"ekzem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 1.2.1 (besonders achten auf Ekzeme) und 1.2.3",
     "befund": "Aktuelle Hautekzeme, besonders an Händen/Unterarmen, angegeben.",
     "konsequenz": "Hautbefund erheben (besonders auf Ekzeme und Hautallergien achten); bei "
                   "unklarer allergischer Hauterkrankung hautärztliche "
                   "Ergänzungsuntersuchung. An ein Nickelekzem denken (ggf. BK-Nr. 5101); "
                   "je nach Befund Bedenken nach 2.1.1/2.1.2 erwägen."},
    {"wenn": {"allergie_disposition": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Allergische Disposition",
     "quelle": "Abschnitt 1.2.1 (Feststellung der Vorgeschichte)",
     "befund": "Allergische Disposition (z. B. Heuschnupfen, Neurodermitis) angegeben.",
     "konsequenz": "Allergische Disposition dokumentieren und bei der Beurteilung "
                   "berücksichtigen; Beratung zur sensibilisierenden Wirkung von "
                   "Nickelmetall und einigen Nickelverbindungen sowie zur Vermeidung von "
                   "Hautkontakt."},
    # ── Beschwerden ───────────────────────────────────────────────────────
    {"wenn": {"atembeschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 1.2.1, 1.2.2 (Spirometrie, ggf. Röntgen-Thorax)",
     "befund": "Husten, Auswurf oder Atemnot angegeben.",
     "konsequenz": "Spirometrie durchführen und bewerten; gegebenenfalls radiologische "
                   "Diagnostik des Thorax veranlassen. Je nach Befund Beurteilung nach "
                   "2.1 (Bedenken/keine Bedenken unter Voraussetzungen)."},
    {"wenn": {"nase_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nase/Nasennebenhöhlen",
     "quelle": "Abschnitte 1.2.2 (Spekulumuntersuchung) und 1.2.3",
     "befund": "Nasenbeschwerden angegeben (behinderte Nasenatmung, Nasenbluten, "
               "Nebenhöhlen-Entzündungen oder Riechstörung).",
     "konsequenz": "Spekulumuntersuchung der Nase sorgfältig durchführen; in unklaren Fällen "
                   "Röntgenuntersuchung der Nasennebenhöhlen als Ergänzungsuntersuchung. An "
                   "Krebs der Nasenhöhlen und Nasennebenhöhlen als seltene Folge denken "
                   "(BK-Nr. 4109)."},
    # ── Exposition mit Zusatzprogramm ─────────────────────────────────────
    {"wenn": {"expo_taetigkeiten": ["tetracarbonyl", "elektrolyse"]},
     "schwere": "pruefen",
     "bereich": "Erweitertes Untersuchungsprogramm",
     "quelle": "Abschnitt 1.2.2 (Spezielle Untersuchung)",
     "befund": "Exposition gegenüber Nickeltetracarbonyl bzw. Tätigkeit in der "
               "elektrolytischen Nickelgewinnung angegeben.",
     "konsequenz": "Zusätzlich zur speziellen Untersuchung BSG oder CRP bestimmen. Bei "
                   "Nickeltetracarbonyl an die akute Toxizität denken (interstitielle "
                   "Pneumonie, evtl. Lungenödem) und die versicherte Person zu "
                   "Frühsymptomen beraten."},
    {"wenn": {"frueher_krebsstoffe": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 1.2.1 (Arbeitsanamnese) und 1.1 (nachgehende Untersuchungen)",
     "befund": "Frühere Exposition gegenüber krebserzeugenden Gefahrstoffen angegeben.",
     "konsequenz": "Arbeitsanamnese im Hinblick auf frühere Exposition gegen krebserzeugende "
                   "Gefahrstoffe vertiefen und dokumentieren; prüfen, ob eine Anmeldung zu "
                   "nachgehenden Untersuchungen (Organisationsdienst ODIN, "
                   "www.odin-info.de) besteht bzw. veranlasst werden muss."},
    # ── Vorzeitige Nachuntersuchung ───────────────────────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt (nach schwerer oder längerer "
                   "Erkrankung, die Anlass zu Bedenken gegen eine Fortsetzung der Tätigkeit "
                   "geben könnte): Erkrankung klären, Beurteilung nach 2.1 aktualisieren, "
                   "Frist (regulär 24–60 Monate) verkürzen."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitte 1.1 (vorzeitige Nachuntersuchung) und 2.2",
     "befund": "Die untersuchte Person vermutet einen Zusammenhang zwischen Erkrankung "
               "und Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung ermöglichen; Verdacht ärztlich abklären "
                   "(Atemwege, Nase, Haut). Bei begründetem Verdacht auf eine "
                   "Berufskrankheit (BK-Nr. 4109 oder 5101) BK-Anzeige erstatten; ergeben "
                   "sich Hinweise auf unzureichenden Arbeitsschutz, Mitteilung an den "
                   "Arbeitgeber zur Aktualisierung der Gefährdungsbeurteilung."},
    # ── Schutzverhalten und Hygiene ───────────────────────────────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitt 2.2 (Beratung, Mitteilung an den Arbeitgeber)",
     "befund": "Atemschutz wird bei staub-/rauchintensiven Arbeiten selten oder nie getragen.",
     "konsequenz": "Auf persönliche Schutzausrüstungen hinweisen und Ursachen der "
                   "Nichtbenutzung klären. Ergeben sich Hinweise, die eine Aktualisierung "
                   "der Gefährdungsbeurteilung notwendig machen, dies dem Arbeitgeber "
                   "mitteilen (unter Wahrung der schutzwürdigen Belange der untersuchten "
                   "Person)."},
    {"wenn": {"handschutz": ["selten", "nie"]},
     "schwere": "hinweis",
     "bereich": "Hautschutz",
     "quelle": "Abschnitte 2.2 und 3.2.1 (Sensibilisierung bei Hautkontakt)",
     "befund": "Schutzhandschuhe werden bei Hautkontakt selten oder nie getragen.",
     "konsequenz": "Beratung zur sensibilisierenden Wirkung von Nickel bei Hautkontakt und "
                   "zu geeigneten Schutzhandschuhen; auf allgemeine Hygienemaßnahmen "
                   "hinweisen."},
    {"wenn": {"hygiene_essen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 2.2 (allgemeine Hygienemaßnahmen)",
     "befund": "Essen, Trinken oder Rauchen am Arbeitsplatz angegeben.",
     "konsequenz": "Hygieneberatung: nicht am Arbeitsplatz essen, trinken oder rauchen; "
                   "Hände vor Pausen gründlich waschen, Arbeitskleidung wechseln – so wird "
                   "die Nickelaufnahme über den Magen-Darm-Trakt vermieden."},
    # ── Rauchen ───────────────────────────────────────────────────────────
    {"wenn": {"rauchstatus": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 1.2.1 (Raucheranamnese) und 2.2 (Beratung)",
     "befund": "Aktives Rauchen angegeben.",
     "konsequenz": "Die krankheitsverursachende Wirkung des Zigarettenrauchens ansprechen – "
                   "Rauchen und nickelhaltige Stäube betreffen dieselben Zielorgane "
                   "(Atemwege/Lunge). Tabakentwöhnung anbieten."},
    # ── Nachgehende Untersuchung ──────────────────────────────────────────
    {"wenn": {"untersuchung_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitte 1.1 und 1.2.2",
     "befund": "Vorstellung zur nachgehenden Untersuchung nach Ende der Nickel-Tätigkeit.",
     "konsequenz": "Untersuchungsprogramm wie Nachuntersuchung (Spekulumuntersuchung der "
                   "Nase, Spirometrie, ggf. Röntgen-Thorax); das Biomonitoring entfällt bei "
                   "der nachgehenden Untersuchung. Ziel ist die Früherkennung bösartiger "
                   "Neubildungen der Atemwege und Lungen (BK-Nr. 4109); die weitere "
                   "Betreuung über den Organisationsdienst ODIN (www.odin-info.de) "
                   "sicherstellen."},
]
