# -*- coding: utf-8 -*-
"""Nickel und Nickelverbindungen – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen
für arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Nickel und Nickelverbindungen« (E NIC, Fassung Januar 2022), S. 429–450."""

SLUG = "nickel-2024"

CATALOG = {
    "version": 2,
    "title": "Nickel und Nickelverbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Nickel und Nickelverbindungen« (E NIC, "
             "Fassung Januar 2022), S. 429–450",
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
                    "label": "Welche Nickel-Vorsorge ist dies für Sie?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge wegen Nickel"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich war schon einmal zur Nickel-Vorsorge)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (die Tätigkeit mit Nickel ist beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge muss der Betrieb veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert nicht eingehalten wird, wiederholter Kontakt "
                            "mit krebserzeugenden Nickelverbindungen möglich ist oder "
                            "Hautkontakt mit Nickeltetracarbonyl nicht ausgeschlossen werden kann.",
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
            "title": "Tätigkeit & Nickelkontakt",
            "subtitle": "Ihre Arbeit mit Nickel und Nickelverbindungen",
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
                        {"value": "galvanik", "label": "Galvanik / elektrolytisches Vernickeln (z. B. offene Nickelbäder)"},
                        {"value": "pulver", "label": "Herstellen, Verarbeiten oder Anwenden von Nickel oder "
                                                     "Nickelverbindungen in Pulverform"},
                        {"value": "erz_recycling", "label": "Aufbereiten/Verarbeiten von Nickelerzen oder Recycling "
                                                            "nickelhaltiger Batterien und Akkus"},
                        {"value": "schleifen", "label": "Schleifen oder Polieren von Nickel oder nickelhaltigen "
                                                        "Legierungen (z. B. Magnete)"},
                        {"value": "giesserei", "label": "Gießerei/Stahlwerk: Zulegieren von Nickel, nickelhaltige "
                                                        "Spezialstähle"},
                        {"value": "katalysator", "label": "Feinverteiltes Nickel als Katalysator (z. B. Fetthärtung)"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an Produktionsanlagen für Nickel"},
                        {"value": "tetracarbonyl", "label": "Tätigkeiten mit Nickeltetracarbonyl "
                                                            "(z. B. Mond-Verfahren, Reinstnickel-Herstellung)"},
                        {"value": "andere", "label": "Andere Tätigkeit mit Nickelkontakt"},
                        {"value": "keine", "label": "Keine davon / weiß nicht"},
                    ],
                },
                {
                    "id": "enge_raeume",
                    "type": "yes_no",
                    "label": "Schweißen oder trennen Sie nickelhaltige Werkstoffe in engen Räumen "
                             "(z. B. Tanks, Kessel, Schächte, Rohrleitungen) ohne örtliche Absaugung?",
                    "required": True,
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt mit Nickel oder Nickelverbindungen?",
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
                    "label": "Waren Sie in früheren Tätigkeiten bereits Nickel oder anderen "
                             "krebserzeugenden Gefahrstoffen ausgesetzt (z. B. Chromate, Asbest, "
                             "Quarzstaub, Schweißrauche)?",
                    "required": True,
                    "followup": {"id": "frueher_expo_desc", "type": "textarea",
                                 "label": "Welche Stoffe, welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle, Unfälle oder ungewöhnliche "
                             "Betriebszustände, bei denen viel Staub, Rauch oder Dampf frei wurde?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "text",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
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
                    "id": "absaugung",
                    "type": "choice",
                    "label": "Gibt es an Ihrem Arbeitsplatz eine Absaugung oder technische Lüftung "
                             "gegen Staub und Rauch?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, durchgehend"},
                        {"value": "teilweise", "label": "Teilweise / nicht überall"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
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
            "subtitle": "Atemwege, Nase, Augen und Haut",
            "questions": [
                {
                    "id": "husten",
                    "type": "yes_no",
                    "label": "Haben Sie Husten, Heiserkeit oder Atemnot?",
                    "required": True,
                    "followup": {"id": "husten_desc", "type": "text",
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
                    "id": "rhinitis_konjunktivitis",
                    "type": "yes_no",
                    "label": "Haben Sie allergischen Schnupfen (laufende oder verstopfte Nase) "
                             "oder juckende, tränende Augen?",
                    "required": True,
                },
                {
                    "id": "urtikaria",
                    "type": "yes_no",
                    "label": "Hatten Sie Nesselsucht (Urtikaria: plötzlich juckende Quaddeln auf "
                             "der Haut), z. B. nach Hautkontakt bei der Arbeit?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                },
                {
                    "id": "nase_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie Beschwerden an Nase oder Nasennebenhöhlen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                    "options": [
                        {"value": "nnh_entzuendung", "label": "Wiederkehrende Nasennebenhöhlen-Entzündungen"},
                        {"value": "nasenbluten", "label": "Häufiges Nasenbluten"},
                        {"value": "nasenatmung", "label": "Behinderte Nasenatmung (Nase oft »zu«)"},
                        {"value": "riechstoerung", "label": "Riechstörungen (schlechter oder kein Geruchssinn)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "allgemein_symptome",
                    "type": "yes_no",
                    "label": "Haben Sie ungewollt Gewicht verloren oder fühlen Sie sich "
                             "auffallend schwach?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                    "followup": {"id": "allgemein_symptome_desc", "type": "text",
                                 "label": "Seit wann, und wie viel Gewicht?", "when": "yes"},
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
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "copd", "label": "COPD (chronisch verengte Atemwege, »Raucherlunge«)"},
                        {"value": "chronische_bronchitis", "label": "Chronische Bronchitis (Husten mit Auswurf über Monate)"},
                        {"value": "bronchiektasen", "label": "Bronchiektasen (krankhaft erweiterte Bronchien)"},
                        {"value": "pleuraschwarten", "label": "Pleuraschwarten (Verwachsungen des Rippenfells)"},
                        {"value": "andere", "label": "Andere Atemwegs- oder Lungenerkrankung"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "nnh_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten oder haben Sie chronische Erkrankungen der Nase oder "
                             "Nasennebenhöhlen (z. B. chronischer Schnupfen, wiederkehrende "
                             "Nebenhöhlen-Entzündungen, Nasenpolypen)?",
                    "required": True,
                    "followup": {"id": "nnh_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und seit wann?", "when": "yes"},
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
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Berufskrankheit anerkannt oder läuft derzeit ein "
                             "Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Berufskrankheit bzw. welches Verfahren?", "when": "yes"},
                },
                {
                    "id": "gesundheit_sonstig",
                    "type": "yes_no",
                    "label": "Haben Sie sonstige gesundheitliche Einschränkungen oder "
                             "dauerhafte Erkrankungen?",
                    "required": True,
                    "followup": {"id": "gesundheit_sonstig_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Nur für weibliche Beschäftigte: Sind Sie schwanger oder stillen Sie?",
                    "hint": "Viele Nickelverbindungen können das ungeborene Kind schädigen "
                            "(reproduktionstoxisch). Ihre Angabe ist freiwillig.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "keine_angabe", "label": "Keine Angabe"},
                        {"value": "nicht_zutreffend", "label": "Trifft auf mich nicht zu"},
                    ],
                },
            ],
        },
        # ── 6 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Rauchen und nickelhaltige Stäube belasten dieselben Organe",
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
    # ── Mutterschutz: Klärung vor (weiterer) Tätigkeit ────────────────────
    {"wenn": {"schwangerschaft": ["ja"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6 (Einstufung reproduktionstoxisch Kat. 1B) und 7.1 "
               "(Beratung zu Beschäftigungsbeschränkungen nach MuSchG)",
     "befund": "Schwangerschaft bzw. Stillzeit bei Tätigkeit mit Nickelverbindungen angegeben.",
     "konsequenz": "Vor (weiterer) Ausübung der Tätigkeit unverzüglich klären: Die meisten "
                   "Nickelverbindungen sind reproduktionstoxisch (entwicklungsschädigend) "
                   "Kategorie 1B. Beschäftigungsbeschränkungen nach Mutterschutzgesetz "
                   "prüfen, mutterschutzrechtliche Gefährdungsbeurteilung des Arbeitgebers "
                   "veranlassen und die versicherte Person entsprechend beraten."},
    # ── Haut ──────────────────────────────────────────────────────────────
    {"wenn": {"nickelallergie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut/Sensibilisierung",
     "quelle": "Abschnitte 6.3.1, 7.1 und 7.4 (Erkrankungen der Haut)",
     "befund": "Bekannte Nickelallergie angegeben.",
     "konsequenz": "Hautstatus erheben; Sensibilisierung bei der Beurteilung nach 7.4 "
                   "berücksichtigen. Beratung zur strikten Vermeidung von Hautkontakt "
                   "(TRGS 401); Maßnahmen nach 7.4.2 prüfen (z. B. Einsatz an Arbeitsplätzen "
                   "mit geringerer Exposition, geeignete Schutzhandschuhe); bei zu erwartender "
                   "Änderung des Schweregrads verkürzte Vorsorgefrist nach 7.4.3."},
    {"wenn": {"hauterkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Hauterkrankung (Ekzem/Hautallergie) in der Vorgeschichte oder aktuell.",
     "konsequenz": "Hautstatus erheben; bei unklaren allergischen Hauterkrankungen "
                   "hautärztliche Ergänzungsuntersuchung veranlassen. Beurteilung nach 7.4; "
                   "Maßnahmen nach 7.4.2, ggf. verkürzte Fristen (7.4.3). Haben die Maßnahmen "
                   "keine Aussicht auf Erfolg, Tätigkeitswechsel erwägen (7.4.4; Mitteilung an "
                   "den Arbeitgeber nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"ekzem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 7.2.2",
     "befund": "Aktuelle Hautekzeme, besonders an Händen/Unterarmen, angegeben.",
     "konsequenz": "Hautstatus erheben (Ekzeme und Hautallergien beachten); bei unklarer "
                   "Ursache hautärztliche Ergänzungsuntersuchung. An ein allergisches "
                   "Kontaktekzem durch Nickel denken (ggf. BK-Nr. 5101); dermale Exposition "
                   "und Schutzhandschuhe überprüfen."},
    {"wenn": {"urtikaria": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut/Sensibilisierung",
     "quelle": "Abschnitte 6.3.2 und 7.1 (weitere Vorsorgen)",
     "befund": "Nesselsucht (Urtikaria) angegeben.",
     "konsequenz": "Bei sensibilisierten Personen kann dermale Nickel-Exposition allergische "
                   "Urtikaria auslösen: hautärztliche Abklärung veranlassen, dermale "
                   "Exposition prüfen; reichen die Schutzmaßnahmen nicht aus, Mitteilung an "
                   "das Unternehmen mit Maßnahmenvorschlag (§ 6 (4) ArbMedVV)."},
    # ── Atemwege ──────────────────────────────────────────────────────────
    {"wenn": {"atemwegserkrankungen": ["asthma", "copd", "chronische_bronchitis",
                                       "bronchiektasen", "pleuraschwarten"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien) mit 7.4.2–7.4.4",
     "befund": "Beurteilungsrelevante Atemwegs-/Lungenerkrankung angegeben (Asthma, COPD, "
               "chronische Bronchitis, Bronchiektasen oder Pleuraschwarten).",
     "konsequenz": "Prüfen, ob die Tätigkeit im Einzelfall ohne gesundheitliche Gefährdung "
                   "möglich ist; Spirometrie sorgfältig bewerten. Bei weniger ausgeprägter "
                   "Erkrankung Maßnahmen nach 7.4.2 (Substitution, technische/organisatorische/"
                   "personenbezogene Schutzmaßnahmen); bei zu erwartender Änderung des "
                   "Schweregrads verkürzte Fristen (7.4.3); ohne Erfolgsaussicht "
                   "Tätigkeitswechsel erwägen (7.4.4, Mitteilung nur mit Einwilligung)."},
    {"wenn": {"husten": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 7.2.2 (Ergänzend)",
     "befund": "Husten, Heiserkeit oder Atemnot angegeben.",
     "konsequenz": "Spirometrie durchführen und bewerten; bei klinischem Verdacht auf "
                   "Lungenkrebs oder Lungenfibrose pulmologische Abklärung veranlassen. "
                   "Beurteilung nach 7.4."},
    {"wenn": {"allgemein_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allgemeinsymptome",
     "quelle": "Abschnitt 7.1 (weitere Vorsorgen: Gewichtsverlust, allgemeine Schwäche)",
     "befund": "Ungewollter Gewichtsverlust oder allgemeine Schwäche angegeben.",
     "konsequenz": "Warnsymptom ernst nehmen und ärztlich abklären; bei klinischem Verdacht "
                   "auf eine Tumorerkrankung der Atemwege/Lunge pulmologische Abklärung "
                   "(7.2.2) und ggf. weiterführende Diagnostik veranlassen."},
    # ── Nase und Nasennebenhöhlen ─────────────────────────────────────────
    {"wenn": {"nnh_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nase/Nasennebenhöhlen",
     "quelle": "Abschnitte 7.2.2 und 7.4 (Erkrankungen der Nasenhöhlen und Nasennebenhöhlen)",
     "befund": "Chronische Erkrankung der Nase oder Nasennebenhöhlen in der Vorgeschichte.",
     "konsequenz": "Rhinoskopie durchführen; in unklaren Fällen bildgebende Diagnostik der "
                   "Nasennebenhöhlen. Beurteilung nach 7.4; Maßnahmen nach 7.4.2 bzw. "
                   "verkürzte Fristen nach 7.4.3 prüfen."},
    {"wenn": {"nase_symptome": ["nnh_entzuendung", "nasenbluten", "nasenatmung", "riechstoerung"]},
     "schwere": "pruefen",
     "bereich": "Nase/Nasennebenhöhlen",
     "quelle": "Abschnitte 6.3.3, 7.1 (weitere Vorsorgen) und 7.2.2",
     "befund": "Nasensymptome angegeben (Nebenhöhlen-Entzündungen, Nasenbluten, behinderte "
               "Nasenatmung oder Riechstörung).",
     "konsequenz": "An chronische Schäden der Nasenschleimhaut durch Nickel denken "
                   "(Rhinitis/Sinusitis, Septumerosionen, Riechstörungen): Rhinoskopie, in "
                   "unklaren Fällen bildgebende Diagnostik der Nasennebenhöhlen bzw. "
                   "HNO-ärztliche Abklärung; verkürzte Vorsorgefrist nach 7.4.3 erwägen."},
    {"wenn": {"rhinitis_konjunktivitis": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sensibilisierung",
     "quelle": "Abschnitt 7.1 (Beschwerden: allergische Rhinitis und Konjunktivitis)",
     "befund": "Allergischer Schnupfen oder juckende, tränende Augen angegeben.",
     "konsequenz": "Rhinoskopie durchführen; an eine Sensibilisierung gegenüber Nickel bzw. "
                   "eine beginnende allergische Atemwegserkrankung denken (BK-Nr. 4301). "
                   "Zusammenhang mit der Tätigkeit klären, ggf. fachärztliche Abklärung."},
    # ── Exposition und Biomonitoring ──────────────────────────────────────
    {"wenn": {"frueher_expo": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorexposition/Biomonitoring",
     "quelle": "Abschnitte 7.2.2 (Erstuntersuchung) und 2 (nachgehende Vorsorge)",
     "befund": "Frühere Exposition gegenüber Nickel oder anderen krebserzeugenden "
               "Gefahrstoffen angegeben.",
     "konsequenz": "Bei der Erstuntersuchung Biomonitoring Nickel im Urin als Basiswert "
                   "durchführen. Frühere Expositionen dokumentieren; prüfen, ob eine "
                   "Anmeldung zur nachgehenden Vorsorge (Meldeportal »DGUV Vorsorge«, "
                   "www.dguv-vorsorge.de) besteht bzw. veranlasst werden muss."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "Abschnitt 7.1 (Zwischenfälle, ungewöhnliche Betriebszustände)",
     "befund": "Zwischenfälle/Unfälle oder ungewöhnliche Betriebszustände mit erhöhter "
               "Freisetzung angegeben.",
     "konsequenz": "Ereignis dokumentieren, Ausmaß der Exposition abschätzen; Biomonitoring "
                   "Nickel im Urin erwägen. Nach möglicher Nickeltetracarbonyl-Freisetzung an "
                   "akute Schädigung von Atemwegen und Lunge bis zum Lungenödem denken "
                   "(6.3.2). Rückmeldung an das Unternehmen zur Gefährdungsbeurteilung."},
    {"wenn": {"expo_taetigkeiten": ["tetracarbonyl"]},
     "schwere": "pruefen",
     "bereich": "Nickeltetracarbonyl",
     "quelle": "Abschnitte 2 (Pflichtvorsorge), 6.2 und 6.3.2",
     "befund": "Tätigkeit mit Nickeltetracarbonyl angegeben.",
     "konsequenz": "Nickeltetracarbonyl ist akut toxisch und hautresorptiv: Pflichtvorsorge-"
                   "Tatbestand, wenn eine Gesundheitsgefährdung durch Hautkontakt nicht "
                   "ausgeschlossen ist. Schutzmaßnahmen gegen Inhalation und Hautkontakt mit "
                   "der Gefährdungsbeurteilung abgleichen; auf akute Atemwegs-/Lungensymptome "
                   "achten und die versicherte Person hierzu beraten."},
    {"wenn": {"enge_raeume": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Erhöhte Exposition",
     "quelle": "Abschnitt 6.1.1",
     "befund": "Schweißen/Trennen nickelhaltiger Werkstoffe in engen Räumen ohne örtliche "
               "Absaugung angegeben.",
     "konsequenz": "Tätigkeit mit höherer Exposition: Abgleich mit der Gefährdungsbeurteilung; "
                   "dem Unternehmen Schutzmaßnahmen vorschlagen (§ 6 (4) ArbMedVV, TRGS 561). "
                   "Zusätzlich die DGUV Empfehlung »Schweißen und Trennen von Metallen« "
                   "anwenden."},
    # ── Schutzverhalten und Hygiene ───────────────────────────────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Atemschutz wird bei staub-/rauchintensiven Arbeiten selten oder nie getragen.",
     "konsequenz": "Beratung zum konsequenten Tragen geeigneter PSA; Ursachen der "
                   "Nichtbenutzung klären. Ergeben sich Anhaltspunkte, dass die "
                   "Schutzmaßnahmen nicht ausreichen, Mitteilung an das Unternehmen und "
                   "Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV, TRGS 561)."},
    {"wenn": {"handschutz": ["selten", "nie"]},
     "schwere": "hinweis",
     "bereich": "Hautschutz",
     "quelle": "Abschnitte 8.1 und 6.3.1 (Sensibilisierung bei Hautkontakt)",
     "befund": "Schutzhandschuhe werden bei Hautkontakt selten oder nie getragen.",
     "konsequenz": "Beratung zur sensibilisierenden Wirkung von Nickel und zur Vermeidung von "
                   "Hautkontakt (TRGS 401); geeignete Schutzhandschuhe und Hautschutzplan "
                   "empfehlen."},
    {"wenn": {"hygiene_essen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 7.1 (allgemeine Beratung: Hygiene am Arbeitsplatz)",
     "befund": "Essen, Trinken oder Rauchen am Arbeitsplatz angegeben.",
     "konsequenz": "Hygieneberatung: kein Essen und Trinken am Arbeitsplatz, gründliches "
                   "Händewaschen vor den Pausen (besonders vor Raucherpausen), Wechsel der "
                   "Arbeitskleidung – so wird die orale Nickelaufnahme vermieden."},
    # ── Rauchen ───────────────────────────────────────────────────────────
    {"wenn": {"rauchstatus": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 7.1 (Beratung: Wechselwirkung Rauchen/Lungenkanzerogene)",
     "befund": "Aktives Rauchen angegeben.",
     "konsequenz": "Beratung über die mögliche Wechselwirkung von Rauchen bzw. "
                   "Lungenkanzerogenen mit nickelhaltigen Stäuben (gleiches Zielorgan); "
                   "Händewaschen vor Raucherpausen einschärfen; Tabakentwöhnung anbieten."},
    # ── Nachgehende Vorsorge ──────────────────────────────────────────────
    {"wenn": {"vorsorge_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2 (Angebotsvorsorge/nachgehende Vorsorge), 6.4 und 7.2.2",
     "befund": "Vorstellung zur nachgehenden Vorsorge nach Ende der Nickel-Tätigkeit.",
     "konsequenz": "Programm nach ärztlichem Ermessen (Hautstatus, Rhinoskopie, Spirometrie); "
                   "Biomonitoring entfällt bei der nachgehenden Vorsorge. Ziel ist die "
                   "Früherkennung von Krebs der Atemwege, Nase und Lunge (BK-Nr. 4109); "
                   "fortlaufende Anmeldung über das Meldeportal »DGUV Vorsorge« "
                   "(www.dguv-vorsorge.de) sicherstellen."},
]
