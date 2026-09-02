# -*- coding: utf-8 -*-
"""G 12 Phosphor (weißer) – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 12 »Phosphor (weißer)«
(Fassung Oktober 2014), S. 227–234."""

SLUG = "g12-phosphor-2016"

CATALOG = {
    "version": 2,
    "title": "G 12 Phosphor (weißer) (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 12 »Phosphor (weißer)« (Fassung Oktober 2014), S. 227–234",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "unt_art",
                    "type": "choice",
                    "label": "Ist dies Ihre erste Untersuchung nach G 12 (weißer Phosphor)?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt, "
                            "Nachuntersuchungen in der Regel nach 12 bis 24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Ja, Erstuntersuchung (vor Aufnahme der "
                                                   "Tätigkeit)"},
                        {"value": "nach", "label": "Nein, Nachuntersuchung"},
                    ],
                },
                {
                    "id": "letzte_unt",
                    "type": "choice",
                    "label": "Wie lange liegt Ihre letzte G 12-Untersuchung zurück?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "options": [
                        {"value": "unter12", "label": "Weniger als 12 Monate"},
                        {"value": "12bis24", "label": "12 bis 24 Monate"},
                        {"value": "ueber24", "label": "Mehr als 24 Monate"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kontakt mit weißem Phosphor",
            "subtitle": "Ihre Arbeit und der mögliche Kontakt mit dem Stoff",
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
                    "label": "In welchen Bereichen arbeiten Sie mit weißem Phosphor oder "
                             "können mit ihm in Kontakt kommen?",
                    "hint": "Mehrfachauswahl möglich. Weißer (gelber) Phosphor ist die sehr "
                            "giftige, selbstentzündliche Form des Phosphors.",
                    "required": True,
                    "options": [
                        {"value": "herstellen", "label": "Herstellen von weißem Phosphor "
                                                         "(Ofenhaus)"},
                        {"value": "abfuellen", "label": "Abfüllen und Reinigen"},
                        {"value": "sulfide_halogenide", "label": "Verarbeiten mit Schwefel zu "
                                                                 "Sulfiden bzw. mit Halogenen "
                                                                 "zu Halogeniden"},
                        {"value": "verbrennung", "label": "Thermische Verbrennung zu "
                                                          "Phosphorsäure"},
                        {"value": "reparatur", "label": "Reparatur- oder Reinigungsarbeiten an "
                                                        "phosphorführenden Apparaturen und "
                                                        "Leitungen"},
                        {"value": "sonstiges", "label": "Andere Tätigkeit mit weißem Phosphor"},
                        {"value": "keine", "label": "Keine davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit weißem Phosphor?",
                    "required": True,
                    "options": [
                        {"value": "beginnt", "label": "Noch gar nicht – Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "ueber5", "label": "Mehr als 5 Jahre"},
                    ],
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit schon Unfälle oder Zwischenfälle mit "
                             "Phosphor (z. B. Brand, Verätzung, Verbrennung der Haut)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit weißem Phosphor "
                             "oder ähnlichen Gefahrstoffen?",
                    "required": True,
                    "followup": {"id": "frueher_expo_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, wie lange?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Schutzausrüstung und Hygiene an Ihrem Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Tragen Sie bei Tätigkeiten mit möglichem Phosphor-Kontakt die "
                             "vorgesehene persönliche Schutzausrüstung (z. B. Schutzkleidung, "
                             "Handschuhe, Atemschutz)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "keine_noetig", "label": "Für meine Tätigkeit ist keine "
                                                           "Schutzausrüstung vorgesehen"},
                    ],
                },
                {
                    "id": "hygiene_umsetzung",
                    "type": "choice",
                    "label": "Halten Sie die Hygieneregeln am Arbeitsplatz ein (z. B. nicht "
                             "essen/trinken/rauchen im Arbeitsbereich, Hände waschen, "
                             "Arbeitskleidung wechseln)?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, vollständig"},
                        {"value": "teilweise", "label": "Teilweise"},
                        {"value": "nein", "label": "Nein / es gibt keine solchen Regeln"},
                    ],
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, auf die bei weißem Phosphor besonders zu achten ist",
            "questions": [
                {
                    "id": "appetit_gewicht",
                    "type": "yes_no",
                    "label": "Haben Sie in letzter Zeit Appetitlosigkeit, ungewollten "
                             "Gewichtsverlust oder auffällige Blässe bemerkt?",
                    "required": True,
                },
                {
                    "id": "muedigkeit_verdauung",
                    "type": "yes_no",
                    "label": "Leiden Sie unter ungewöhnlicher Müdigkeit oder "
                             "Verdauungsstörungen (z. B. Übelkeit, Durchfälle)?",
                    "required": True,
                },
                {
                    "id": "schleimhautblutungen",
                    "type": "yes_no",
                    "label": "Neigen Sie zu Blutungen der Haut oder Schleimhäute (z. B. "
                             "häufiges Zahnfleisch- oder Nasenbluten, schnell blaue Flecken)?",
                    "required": True,
                },
                {
                    "id": "knochenschmerzen",
                    "type": "yes_no",
                    "label": "Haben Sie Schmerzen in Knochen oder Gelenken, besonders im "
                             "Kieferbereich?",
                    "required": True,
                    "followup": {"id": "knochenschmerzen_desc", "type": "text",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "zahnschmerzen",
                    "type": "yes_no",
                    "label": "Haben Sie Zahnschmerzen oder Beschwerden am Zahnfleisch "
                             "(z. B. Entzündungen, wunde Stellen)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Zähne und Vorerkrankungen ──────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Zähne & Vorerkrankungen",
            "subtitle": "Zahnzustand und frühere bzw. bestehende Erkrankungen",
            "questions": [
                {
                    "id": "zahnstatus",
                    "type": "choice",
                    "label": "Wie ist der Zustand Ihrer Zähne?",
                    "hint": "Bei der G 12-Untersuchung wird besonders auf den Zahnstatus "
                            "geachtet: Unbehandelte Löcher (Karies) und Entzündungsherde an "
                            "Zahnwurzeln (Zahngranulome) können eine Eintrittspforte für "
                            "Phosphor in den Kieferknochen sein.",
                    "required": True,
                    "options": [
                        {"value": "saniert", "label": "Gesund oder vollständig behandelt "
                                                      "(saniert)"},
                        {"value": "karies", "label": "Ich habe unbehandelte Löcher (Karies), "
                                                     "abgebrochene oder stark beschädigte Zähne"},
                        {"value": "unbekannt", "label": "Weiß ich nicht / lange kein "
                                                        "Zahnarztbesuch"},
                    ],
                },
                {
                    "id": "leber_erkrankung",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung der Leber (z. B. "
                             "Hepatitis/Leberentzündung, Fettleber, Leberzirrhose)?",
                    "required": True,
                    "followup": {"id": "leber_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "nieren_erkrankung",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung der Nieren (z. B. "
                             "Nierenentzündung, eingeschränkte Nierenfunktion, Eiweiß im "
                             "Urin)?",
                    "required": True,
                    "followup": {"id": "nieren_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "knochen_erkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Erkrankung der Knochen, "
                             "z. B. Knochenschwund (Osteoporose)?",
                    "required": True,
                    "followup": {"id": "knochen_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "schwere_erkrankung_seit",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten G 12-Untersuchung eine schwere "
                             "oder länger dauernde Erkrankung?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_seit_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie, dass Beschwerden oder eine Erkrankung bei Ihnen "
                             "mit Ihrer Tätigkeit am Arbeitsplatz zusammenhängen?",
                    "required": True,
                    "followup": {"id": "zusammenhang_vermutet_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
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
    # ── Bedenkenstatbestände (Abschnitt 2.1.1/2.1.2) ──────────────────────
    {"wenn": {"leber_erkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Leber",
     "quelle": "Abschnitte 2.1.1, 2.1.2 und 1.2.2",
     "befund": "Lebererkrankung in der Vorgeschichte oder aktuell angegeben.",
     "konsequenz": "Schweregrad ärztlich klären: schwere Leberkrankheiten begründen "
                   "dauernde gesundheitliche Bedenken (2.1.1), bei zu erwartender "
                   "Wiederherstellung befristete Bedenken (2.1.2). Spezielle Untersuchung "
                   "(SGPT/ALAT, SGOT/ASAT, γ-GT) gezielt bewerten; bei Verdacht auf "
                   "Lebervorschädigung weitere leberspezifische Untersuchungen "
                   "(Elektrophorese, in unklaren Fällen evtl. Biopsie). Bei weniger "
                   "ausgeprägter Funktionsstörung keine Bedenken unter Voraussetzungen "
                   "(2.1.3): Schutzmaßnahmen, geringere Exposition, verkürzte "
                   "Nachuntersuchungsfristen."},
    {"wenn": {"nieren_erkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Niere",
     "quelle": "Abschnitte 2.1.1, 2.1.2 und 1.2",
     "befund": "Nierenerkrankung in der Vorgeschichte oder aktuell angegeben.",
     "konsequenz": "Schweregrad ärztlich klären: schwere Nierenkrankheiten begründen "
                   "dauernde gesundheitliche Bedenken (2.1.1), bei zu erwartender "
                   "Wiederherstellung befristete Bedenken (2.1.2). Urinstatus "
                   "(Mehrfachteststreifen, Albuminurie beachten) und Kreatinin im Serum "
                   "gezielt bewerten. Bei weniger ausgeprägter Störung keine Bedenken "
                   "unter Voraussetzungen (2.1.3) mit Schutzmaßnahmen und verkürzten "
                   "Nachuntersuchungsfristen."},
    {"wenn": {"knochen_erkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Knochensystem",
     "quelle": "Abschnitte 2.1.1, 2.1.2 und 1.2.3",
     "befund": "Chronische Erkrankung des Knochensystems (z. B. Osteoporose) angegeben.",
     "konsequenz": "Chronische Erkrankungen des Knochensystems begründen dauernde "
                   "gesundheitliche Bedenken (2.1.1), bei zu erwartender Wiederherstellung "
                   "befristete Bedenken (2.1.2). In unklaren Fällen "
                   "Ergänzungsuntersuchung: Röntgendiagnostik der Knochen, insbesondere "
                   "der Kieferknochen. Bei weniger ausgeprägter Erkrankung keine Bedenken "
                   "unter Voraussetzungen (2.1.3)."},
    # ── Zähne und Kiefer (1.2.1, 3.2.3) ───────────────────────────────────
    {"wenn": {"zahnstatus": ["karies", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Zähne/Kiefer",
     "quelle": "Abschnitte 1.2.1 (Zahnstatus, kariöses Gebiss) und 3.2.3",
     "befund": "Kariöses bzw. nicht saniertes Gebiss oder unklarer Zahnstatus angegeben.",
     "konsequenz": "Zahnstatus im Rahmen der allgemeinen Untersuchung gezielt erheben; "
                   "zahnärztliche Untersuchung und Sanierung veranlassen bzw. dringend "
                   "empfehlen. Zahngranulome als Endstadium einer Karies bieten eine "
                   "Eintrittspforte für elementaren Phosphor in den Kieferknochen "
                   "(Gefahr von Osteomyelitis/Kiefernekrose). Bis zur Sanierung verkürzte "
                   "Nachuntersuchungsfrist nach 2.1.3 erwägen."},
    {"wenn": {"zahnschmerzen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zähne/Kiefer",
     "quelle": "Abschnitte 1.2.1, 1.2.3 und 3.2.3",
     "befund": "Zahnschmerzen oder Zahnfleischbeschwerden angegeben.",
     "konsequenz": "Zahnärztliche Abklärung veranlassen; an phosphorbedingte Veränderungen "
                   "des Kieferknochens denken. In unklaren Fällen Ergänzungsuntersuchung: "
                   "Röntgendiagnostik der Kieferknochen."},
    {"wenn": {"knochenschmerzen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Knochensystem",
     "quelle": "Abschnitte 1.2.3 und 3.2.3",
     "befund": "Schmerzen in Knochen, Gelenken oder im Kieferbereich angegeben.",
     "konsequenz": "Gezielte Anamnese und Untersuchung (phosphorbedingte Osteoporose "
                   "betrifft insbesondere die Kieferknochen; Anfälligkeit des veränderten "
                   "Knochens für Osteomyelitis beachten). In unklaren Fällen "
                   "Ergänzungsuntersuchung: Röntgendiagnostik der Knochen, insbesondere "
                   "der Kieferknochen."},
    # ── Zeichen chronischer Einwirkung (1.2.1 Nachuntersuchung, 3.2.3) ────
    {"wenn": {"appetit_gewicht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Chronische Einwirkung",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung) und 3.2.3",
     "befund": "Appetitlosigkeit, Gewichtsverlust oder Blässe angegeben.",
     "konsequenz": "Mögliche Zeichen einer chronischen Phosphoreinwirkung: spezielle "
                   "Untersuchung (BSG/CRP, Hämoglobin, Kreatinin, Leberenzyme) gezielt "
                   "auswerten; bei Verdacht auf Lebervorschädigung weitere "
                   "leberspezifische Untersuchungen (Elektrophorese, in unklaren Fällen "
                   "evtl. Biopsie). Expositionssituation überprüfen."},
    {"wenn": {"muedigkeit_verdauung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Chronische Einwirkung",
     "quelle": "Abschnitt 3.2.3",
     "befund": "Ungewöhnliche Müdigkeit oder Verdauungsstörungen angegeben.",
     "konsequenz": "Als mögliche chronische Phosphorwirkung ärztlich abklären "
                   "(Müdigkeit und Verdauungsstörungen zählen zu den chronischen "
                   "Gesundheitsschädigungen); Laborprogramm nach 1.2.2 auswerten, in "
                   "unklaren Fällen Ergänzungsuntersuchung."},
    {"wenn": {"schleimhautblutungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Chronische Einwirkung",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung) und 3.2.3",
     "befund": "Blutungsneigung der Haut oder Schleimhäute angegeben.",
     "konsequenz": "Mögliches Zeichen chronischer Phosphoreinwirkung (Blutungsneigung in "
                   "Haut, Schleimhäuten und am Augenhintergrund): Hämoglobin und BSG/CRP "
                   "gezielt bewerten, internistische Abklärung erwägen; in unklaren "
                   "Fällen Ergänzungsuntersuchung."},
    # ── Vorzeitige Nachuntersuchung (1.1) ─────────────────────────────────
    {"wenn": {"schwere_erkrankung_seit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsanlass",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder länger dauernde Erkrankung seit der letzten Untersuchung "
               "angegeben.",
     "konsequenz": "Kriterium für eine vorzeitige Nachuntersuchung erfüllt: prüfen, ob die "
                   "Erkrankung Anlass zu Bedenken gegen eine Fortsetzung der Tätigkeit "
                   "gibt; vollständiges Untersuchungsprogramm (1.2.1/1.2.2) durchführen "
                   "und Beurteilung nach Abschnitt 2.1 vornehmen."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsanlass",
     "quelle": "Abschnitte 1.1 (vorzeitige Nachuntersuchung) und 4",
     "befund": "Proband vermutet einen Zusammenhang zwischen Erkrankung/Beschwerden und "
               "der Tätigkeit.",
     "konsequenz": "Kriterium für eine vorzeitige Nachuntersuchung erfüllt: Beschwerden "
                   "gezielt abklären, Untersuchungsprogramm vollständig durchführen. Bei "
                   "begründetem Verdacht auf eine Erkrankung durch Phosphor an die "
                   "BK-Anzeige denken (BK-Nr. 1109 »Erkrankungen durch Phosphor oder "
                   "seine anorganischen Verbindungen«)."},
    {"wenn": {"letzte_unt": ["ueber24", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Fristen",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungen nach 12–24 Monaten)",
     "befund": "Letzte G 12-Untersuchung liegt mehr als 24 Monate zurück oder ist unklar.",
     "konsequenz": "Nachuntersuchungsfrist (12–24 Monate) ist überschritten bzw. nicht "
                   "belegt: Untersuchung jetzt vollständig durchführen, Vorbefunde "
                   "beschaffen und die Fristeinhaltung für die Zukunft mit dem Betrieb "
                   "organisieren."},
    # ── Arbeitsanamnese und Schutzmaßnahmen (1.2.1, 2.2) ──────────────────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle/Unfälle",
     "quelle": "Abschnitte 1.2.1, 2.2 und 4",
     "befund": "Unfälle oder Zwischenfälle mit Phosphor angegeben.",
     "konsequenz": "Hergang dokumentieren; Folgeschäden abklären (Schädigungen können erst "
                   "nach Monaten oder Jahren auftreten). Ergeben sich Hinweise, die eine "
                   "Aktualisierung der Gefährdungsbeurteilung notwendig machen, Mitteilung "
                   "an den Arbeitgeber unter Wahrung der schutzwürdigen Belange des "
                   "Untersuchten; an BK-Nr. 1109 denken."},
    {"wenn": {"psa_nutzung": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen/PSA",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Eindringliche Beratung zu persönlicher Schutzausrüstung und "
                   "allgemeinen Hygienemaßnahmen (stoffspezifische Hinweise: GESTIS, "
                   "Rubrik »Umgang und Verwendung«). Machen die Angaben eine "
                   "Aktualisierung der Gefährdungsbeurteilung notwendig, Mitteilung an "
                   "den Arbeitgeber unter Wahrung der schutzwürdigen Belange."},
    {"wenn": {"hygiene_umsetzung": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht oder nur teilweise umgesetzt.",
     "konsequenz": "Beratung zu allgemeinen Hygienemaßnahmen (nicht essen/trinken/rauchen "
                   "im Arbeitsbereich, Hände waschen, Arbeitskleidung wechseln); Umsetzung "
                   "bei der nächsten Untersuchung erneut erfragen."},
    {"wenn": {"frueher_expo": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 1.2.1 (Arbeitsanamnese) und 3.2.3",
     "befund": "Frühere Tätigkeiten mit Phosphor-Kontakt oder ähnlichen Gefahrstoffen "
               "angegeben.",
     "konsequenz": "Frühere Expositionen in der Arbeitsanamnese dokumentieren und bei der "
                   "Beurteilung berücksichtigen; beachten, dass phosphorbedingte "
                   "Schädigungen erst nach Monaten oder Jahren auftreten können."},
]
