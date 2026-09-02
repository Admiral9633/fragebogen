# -*- coding: utf-8 -*-
"""G 32 Cadmium oder seine Verbindungen – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016,
G 32 (Fassung Oktober 2014), S. 459–469."""

SLUG = "g32-cadmium-2016"

CATALOG = {
    "version": 2,
    "title": "G 32 Cadmium oder seine Verbindungen (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 32 »Cadmium oder seine Verbindungen« (Fassung Oktober 2014), S. 459–469",
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
                    "label": "Um welche Untersuchung handelt es sich?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt, "
                            "die Nachuntersuchung regelmäßig nach 12 bis 24 Monaten. Die "
                            "nachgehende Untersuchung erfolgt nach dem Ende der Tätigkeit "
                            "mit Cadmium.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (Tätigkeit mit Cadmium ist beendet)"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "länger dauernde Erkrankung?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach", "nachgehend"]},
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Cadmiumbelastung ─────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Cadmium-Kontakt",
            "subtitle": "Ihre Arbeit und der Umgang mit Cadmium",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_verfahren",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten haben Sie Kontakt mit Cadmium oder seinen "
                             "Verbindungen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "verhuetten_herstellen", "label": "Verhütten von Blei- oder Zinkerzen, Herstellen von Cadmium oder Cadmium-Legierungen (Rösten, Schmelzen, Gießen, Glühen, Staubfilter, Elektrolyse)"},
                        {"value": "cd_verbindungen", "label": "Herstellen von Nickel-Cadmium-Akkus, löslichen Cadmiumverbindungen, Cadmium-Pigmenten (Farbstoffen) oder cadmiumhaltigen Stabilisatoren"},
                        {"value": "recycling", "label": "Recycling oder Verbrennen cadmiumhaltiger Abfälle/Altmaterialien, Entfernen cadmiumhaltiger Anstriche"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an Anlagen, in denen Cadmium hergestellt oder verarbeitet wurde"},
                        {"value": "pigmente_farben", "label": "Arbeiten mit cadmiumhaltigen Pigmenten, Emaillen, keramischen Farben oder Glasuren (auch Kunststoffe und Lacke)"},
                        {"value": "loesliche_verbindungen", "label": "Lösliche Cadmiumverbindungen in der Foto-, Glas-, Gummi- oder Schmuckindustrie"},
                        {"value": "elektronik", "label": "Cadmiumhaltige Elemente/Bauteile in Fernseh-, Mess-, Regel-, Reaktortechnik, Kfz- oder Luftfahrtindustrie, Fotozellen"},
                        {"value": "mechanisch", "label": "Mechanisches Bearbeiten cadmiumhaltiger Materialien (Staubentwicklung)"},
                        {"value": "andere", "label": "Andere Arbeiten mit Cadmium"},
                        {"value": "keine", "label": "Keine davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "heissverfahren",
                    "type": "yes_no",
                    "label": "Führen Sie Heißarbeiten an cadmiumhaltigen oder cadmiumbeschichteten "
                             "Materialien durch, z. B. Hartlöten, Schweißen, Schneiden, Glühen "
                             "oder Bedampfen?",
                    "hint": "Dabei kann Cadmiumoxidrauch entstehen – das ist besonders belastend "
                            "für Atemwege und Lunge. Auch Lötarbeiten mit cadmiumhaltigen "
                            "Hartloten (z. B. Schmuckherstellung/-reparatur) zählen dazu.",
                    "required": True,
                    "followup": {"id": "heissverfahren_desc", "type": "text",
                                 "label": "Welche Heißarbeiten, und wie oft?", "when": "yes"},
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit Cadmium oder seinen "
                             "Verbindungen (alle Tätigkeiten zusammengerechnet)?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis10", "label": "5 bis 10 Jahre"},
                        {"value": "ueber10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "frueher_cadmium",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit Cadmium oder "
                             "anderen Gefahrstoffen mit vergleichbarer Gefährdung?",
                    "required": True,
                    "followup": {"id": "frueher_cadmium_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, wie lange, und gab es "
                                          "dort arbeitsmedizinische Untersuchungen?", "when": "yes"},
                },
                {
                    "id": "zwischenfall",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle oder Unfälle, bei denen Sie "
                             "viel cadmiumhaltigen Staub oder Rauch eingeatmet haben könnten?",
                    "required": True,
                    "followup": {"id": "zwischenfall_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Schutzausrüstung und Verhalten am Arbeitsplatz",
            "questions": [
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei staub- oder rauchintensiven Arbeiten mit Cadmium "
                             "Atemschutz?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "Für meine Tätigkeit nicht vorgesehen / noch keine Tätigkeit"},
                    ],
                },
                {
                    "id": "hygiene",
                    "type": "multi_choice",
                    "label": "Welche Punkte treffen auf Ihren Arbeitsalltag zu?",
                    "hint": "Mehrfachauswahl möglich. Cadmium kann auch über den Mund in den "
                            "Körper gelangen – Hygiene am Arbeitsplatz ist deshalb wichtig.",
                    "required": True,
                    "options": [
                        {"value": "essen_am_platz", "label": "Ich esse, trinke oder rauche manchmal direkt am Arbeitsplatz"},
                        {"value": "haende_selten", "label": "Ich wasche mir vor Pausen (auch Raucherpausen) nicht immer gründlich die Hände"},
                        {"value": "kein_kleidungswechsel", "label": "Ich trage Arbeitskleidung auch nach Feierabend weiter / wechsle sie nicht"},
                        {"value": "alles_beachtet", "label": "Nichts davon – ich beachte die Hygieneregeln"},
                    ],
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die mit Cadmium zusammenhängen können",
            "questions": [
                {
                    "id": "geruchssinn",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Geruchssinn verschlechtert (Sie riechen schlechter "
                             "als früher oder gar nicht mehr)?",
                    "hint": "Auf Störungen des Geruchssinns ist bei Cadmium besonders zu achten.",
                    "required": True,
                },
                {
                    "id": "atemwege_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere der folgenden Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Häufiger Husten"},
                        {"value": "auswurf", "label": "Auswurf (Schleim beim Husten)"},
                        {"value": "atemnot", "label": "Atemnot oder Kurzatmigkeit"},
                        {"value": "brustschmerzen", "label": "Schmerzen im Brustkorb"},
                        {"value": "schnupfen", "label": "Ständiger Schnupfen oder behinderte Nasenatmung"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "metalldampffieber",
                    "type": "yes_no",
                    "label": "Hatten Sie nach Arbeiten mit Metallrauch (z. B. Schweißen, Löten) "
                             "schon einmal grippeartige Beschwerden wie Fieber, Frösteln, "
                             "Schweißausbruch oder Herzrasen (»Metalldampffieber«)?",
                    "hint": "Solche Beschwerden können erst mehrere Stunden bis 3 Tage nach dem "
                            "Einatmen von Cadmiumrauch auftreten.",
                    "required": True,
                    "followup": {"id": "metalldampffieber_desc", "type": "text",
                                 "label": "Wann zuletzt, und nach welcher Arbeit?", "when": "yes"},
                },
                {
                    "id": "allgemein_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine der folgenden Veränderungen bemerkt?",
                    "required": True,
                    "options": [
                        {"value": "gewichtsabnahme", "label": "Ungewollte Gewichtsabnahme"},
                        {"value": "muedigkeit", "label": "Auffallende Müdigkeit oder Abgeschlagenheit"},
                        {"value": "keine", "label": "Nichts davon"},
                    ],
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, auf die bei Cadmium besonders zu achten ist",
            "questions": [
                {
                    "id": "vorerkr_atemwege",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Erkrankungen der oberen oder tieferen "
                             "Atemwege (z. B. chronische Bronchitis, Asthma, COPD, "
                             "Lungenemphysem)?",
                    "required": True,
                    "followup": {"id": "vorerkr_atemwege_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, und sind Sie in "
                                          "Behandlung?", "when": "yes"},
                },
                {
                    "id": "vorerkr_niere",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Nierenerkrankung oder eine "
                             "eingeschränkte Nierenfunktion (z. B. Eiweiß im Urin, erhöhte "
                             "Nierenwerte)?",
                    "hint": "Die Niere ist das wichtigste Zielorgan von Cadmium.",
                    "required": True,
                    "followup": {"id": "vorerkr_niere_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vorerkr_leber",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Lebererkrankung (z. B. Hepatitis, "
                             "Fettleber mit erhöhten Leberwerten, Leberzirrhose)?",
                    "required": True,
                    "followup": {"id": "vorerkr_leber_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vorerkr_diabetes",
                    "type": "yes_no",
                    "label": "Haben Sie einen Diabetes mellitus (Zuckerkrankheit)?",
                    "hint": "Bei der Erstuntersuchung gehört eine Diabetes-Diagnostik zum "
                            "Untersuchungsprogramm.",
                    "required": True,
                },
                {
                    "id": "schwanger",
                    "type": "choice",
                    "label": "Sind Sie zurzeit schwanger oder stillen Sie?",
                    "hint": "Cadmium und einige Cadmiumverbindungen können fruchtschädigend "
                            "(das ungeborene Kind schädigend) wirken.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "entfaellt", "label": "Trifft auf mich nicht zu"},
                        {"value": "keine_angabe", "label": "Keine Angabe"},
                    ],
                },
            ],
        },
        # ── 6 ─ Rauchen und Alkohol ────────────────────────────────────────
        {
            "id": "genussmittel",
            "title": "Rauchen & Alkohol",
            "subtitle": "Wichtig für Beurteilung und Biomonitoring",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Tabakrauch enthält Cadmium. Für Raucher gelten beim Biomonitoring "
                            "(Cadmium im Blut/Urin) andere Vergleichswerte.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "ex", "label": "Früher, aber nicht mehr"},
                        {"value": "bis10", "label": "Ja, bis etwa 10 Zigaretten pro Tag"},
                        {"value": "10bis20", "label": "Ja, etwa 10 bis 20 Zigaretten pro Tag"},
                        {"value": "ueber20", "label": "Ja, mehr als 20 Zigaretten pro Tag"},
                    ],
                },
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie oder sehr selten"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche bis täglich)"},
                        {"value": "abhaengigkeit", "label": "Ich habe oder hatte ein Alkoholproblem (Abhängigkeit)"},
                    ],
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
    # ── Untersuchungsanlass / Fristen (Abschnitt 1.1) ─────────────────────
    {"wenn": {"unt_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitte 1.1 und 1.2.2 (Nachgehende Untersuchung)",
     "befund": "Vorstellung zur nachgehenden Untersuchung nach Ende der Cadmium-Tätigkeit.",
     "konsequenz": "Programm der Nachuntersuchung/nachgehenden Untersuchung durchführen "
                   "(u. a. Spirometrie, Biomonitoring nach 3.1.4, α1-Mikroglobulin und "
                   "N-Acetyl-β-D-Glucosaminidase im Urin), ggf. radiologische Diagnostik des "
                   "Thorax. Organisation über den Organisationsdienst für nachgehende "
                   "Untersuchungen (ODIN, www.odin-info.de) sicherstellen."},
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Schwere oder länger dauernde Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt (Frist von 12–24 Monaten nicht "
                   "abwarten): Erkrankung klären und prüfen, ob sie Anlass zu gesundheitlichen "
                   "Bedenken gegen eine Fortsetzung der Tätigkeit nach 2.1.1/2.1.2 gibt."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vermuteter Arbeitszusammenhang",
     "quelle": "Abschnitte 1.1 und 4 (Berufskrankheit)",
     "befund": "Die versicherte Person vermutet einen Zusammenhang zwischen Erkrankung und "
               "Tätigkeit am Arbeitsplatz.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen und Beschwerden gezielt abklären. "
                   "Bei begründetem Verdacht auf eine Erkrankung durch Cadmium ärztliche "
                   "Anzeige einer Berufskrankheit prüfen (BK-Nr. 1104 »Erkrankungen durch "
                   "Cadmium und seine Verbindungen«)."},
    # ── Exposition (Abschnitt 3.1) ────────────────────────────────────────
    {"wenn": {"heissverfahren": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Cadmiumoxidrauch",
     "quelle": "Abschnitte 3.1.1 und 3.2.2",
     "befund": "Heißarbeiten mit möglicher Bildung von Cadmiumoxidrauch angegeben "
               "(Hartlöten, Schweißen, Schneiden, Glühen, Bedampfen).",
     "konsequenz": "Erhöhte inhalative Gefährdung berücksichtigen: Expositionssituation mit der "
                   "Gefährdungsbeurteilung abgleichen (Pulverbeschichtung auf Cadmiumgehalt "
                   "überprüfen), Biomonitoring-Ergebnisse gezielt bewerten und zur akuten "
                   "Symptomatik nach Rauchexposition beraten (Latenzzeit bis 3 Tage)."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfall/Unfall",
     "quelle": "Abschnitt 3.2.2 (Akute/subakute Gesundheitsschädigung)",
     "befund": "Zwischenfall mit möglicher hoher Cadmiumstaub- oder Rauchexposition angegeben.",
     "konsequenz": "Ereignis dokumentieren und ärztlich abklären; an die Latenzzeit akuter "
                   "Wirkungen von mehreren Stunden bis zu 3 Tagen denken (u. U. Lungenödem, "
                   "Nierenschäden). Ergeben sich Hinweise auf unzureichenden Arbeitsschutz, "
                   "Mitteilung an den Arbeitgeber zur Aktualisierung der Gefährdungsbeurteilung "
                   "(Abschnitt 2.2)."},
    {"wenn": {"frueher_cadmium": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorbelastung",
     "quelle": "Abschnitte 1.2.1 (Anamnese) und 3.1.4 (Biomonitoring)",
     "befund": "Frühere Tätigkeiten mit Cadmium- oder vergleichbarer Gefahrstoff-Exposition.",
     "konsequenz": "Frühere Expositionen dokumentieren und bei der Bewertung des Biomonitorings "
                   "berücksichtigen; Vorbefunde früherer Untersuchungen anfordern. Anspruch auf "
                   "nachgehende Untersuchungen (ODIN) nach Ausscheiden aus der Tätigkeit klären."},
    # ── Beschwerden (Abschnitte 1.2.1 und 3.2) ────────────────────────────
    {"wenn": {"geruchssinn": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Geruchssinn",
     "quelle": "Abschnitte 1.2.1 (besonders zu achten) und 3.2.3",
     "befund": "Verschlechterung oder Verlust des Geruchssinns angegeben.",
     "konsequenz": "Mögliches Zeichen chronischer Cadmium-Einwirkung (Atrophie der "
                   "Nasenschleimhäute): Prüfung der Nasenatmung gezielt durchführen, Befund "
                   "dokumentieren; ggf. HNO-ärztliche Abklärung veranlassen und bei der "
                   "Beurteilung nach 2.1 berücksichtigen."},
    {"wenn": {"atemwege_beschwerden": ["husten", "auswurf", "atemnot", "brustschmerzen",
                                       "schnupfen"]},
     "schwere": "pruefen",
     "bereich": "Atemwegsbeschwerden",
     "quelle": "Abschnitte 1.2.2 (Spirometrie) und 3.2.3",
     "befund": "Atemwegsbeschwerden angegeben (Husten, Auswurf, Atemnot, Brustschmerzen oder "
               "ständiger Schnupfen).",
     "konsequenz": "Spirometrie-Befund gezielt bewerten (obstruktive Ventilationsstörung, "
                   "Emphysem-Hinweise); Zusammenhang mit der Tätigkeit prüfen. Bei schwerer "
                   "Erkrankung der Luftwege gesundheitliche Bedenken nach 2.1.1/2.1.2 erwägen, "
                   "sonst Maßnahmen und verkürzte Nachuntersuchungsfristen nach 2.1.3."},
    {"wenn": {"metalldampffieber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Rauchexposition",
     "quelle": "Abschnitte 3.2.2 und 2.2",
     "befund": "Metalldampffieber-artige Beschwerden nach Arbeiten mit Metallrauch angegeben.",
     "konsequenz": "Hinweis auf relevante inhalative Rauchexposition: Umstände klären, Nieren- "
                   "und Lungenparameter kontrollieren. Dem Arbeitgeber Hinweise zur "
                   "Aktualisierung der Gefährdungsbeurteilung geben (Absaugung, Atemschutz), "
                   "unter Wahrung der schutzwürdigen Belange der untersuchten Person."},
    {"wenn": {"allgemein_beschwerden": ["gewichtsabnahme", "muedigkeit"]},
     "schwere": "pruefen",
     "bereich": "Allgemeinsymptome",
     "quelle": "Abschnitte 1.2.1 (besonders zu achten: Gewichtsabnahme) und 3.2.3",
     "befund": "Ungewollte Gewichtsabnahme und/oder auffallende Müdigkeit angegeben.",
     "konsequenz": "Mögliche Zeichen einer chronischen Cadmium-Wirkung: gezielte ärztliche "
                   "Abklärung (u. a. Nieren- und Leberparameter, BSG/CRP) und "
                   "differenzialdiagnostische Klärung; Verlaufskontrolle, ggf. vorzeitige "
                   "Nachuntersuchung."},
    # ── Vorerkrankungen / Bedenken (Abschnitt 2.1) ────────────────────────
    {"wenn": {"vorerkr_niere": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nierenerkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Nierenerkrankung bzw. eingeschränkte Nierenfunktion angegeben.",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Tätigkeit klären: Bei Tubulopathien mit "
                   "Einschränkung der Nierenfunktion, diabetischer Nephropathie oder "
                   "signifikanter Einschränkung der Retentionswerte bestehen dauernde "
                   "gesundheitliche Bedenken (2.1.1); bei zu erwartender Wiederherstellung "
                   "befristete Bedenken (2.1.2). Kreatinin im Serum, α1-Mikroglobulin und "
                   "N-Acetyl-β-D-Glucosaminidase im Urin gezielt bewerten, Vorbefunde einholen."},
    {"wenn": {"vorerkr_atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3",
     "befund": "Erkrankung der oberen oder tieferen Luftwege in der Vorgeschichte.",
     "konsequenz": "Ausprägung klären (Spirometrie, Vorbefunde): Bei schwerer Erkrankung "
                   "dauernde gesundheitliche Bedenken (2.1.1), bei zu erwartender "
                   "Wiederherstellung befristete Bedenken (2.1.2). Bei geringerer Ausprägung "
                   "keine Bedenken unter Voraussetzungen (2.1.3): technische/organisatorische "
                   "Schutzmaßnahmen, expositionsärmerer Arbeitsplatz, PSA, verkürzte "
                   "Nachuntersuchungsfristen."},
    {"wenn": {"vorerkr_leber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lebererkrankung",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3",
     "befund": "Lebererkrankung in der Vorgeschichte.",
     "konsequenz": "Leberwerte (SGPT/ALAT, SGOT/ASAT, γ-GT) gezielt bestimmen und bewerten, "
                   "Vorbefunde einholen. Bei schwerer Lebererkrankung dauernde bzw. befristete "
                   "gesundheitliche Bedenken (2.1.1/2.1.2); bei geringerer Ausprägung "
                   "Voraussetzungen nach 2.1.3 einschließlich verkürzter "
                   "Nachuntersuchungsfristen prüfen."},
    {"wenn": {"vorerkr_diabetes": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Diabetes mellitus",
     "quelle": "Abschnitte 1.2.1, 1.2.2 (Diabetes-Diagnostik) und 2.1.1",
     "befund": "Diabetes mellitus angegeben.",
     "konsequenz": "Diabetes-Diagnostik und Nierenparameter (Kreatinin, α1-Mikroglobulin, "
                   "N-Acetyl-β-D-Glucosaminidase, Urinstatus) gezielt bewerten: Bei "
                   "diabetischer Nephropathie mit Einschränkung der Nierenfunktion bestehen "
                   "dauernde gesundheitliche Bedenken (2.1.1); sonst engmaschige Kontrolle und "
                   "ggf. verkürzte Nachuntersuchungsfristen (2.1.3)."},
    # ── Rauchen / Alkohol (Abschnitte 2.1.1 und 3.1.4) ────────────────────
    {"wenn": {"alkohol": ["abhaengigkeit"]},
     "schwere": "kritisch",
     "bereich": "Alkoholabhängigkeit",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Alkoholabhängigkeit angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1 (auch wegen der Gefahr mangelhafter "
                   "Hygienemaßnahmen): dauernde gesundheitliche Bedenken erwägen, Leberwerte "
                   "gezielt bewerten und Behandlungs-/Beratungsangebote vermitteln. Bei "
                   "erfolgreicher Behandlung Neubeurteilung (befristete Bedenken, 2.1.2)."},
    {"wenn": {"rauchen": ["ueber20"]},
     "schwere": "kritisch",
     "bereich": "Erheblicher Nikotinabusus",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Erheblicher Nikotinkonsum (mehr als 20 Zigaretten täglich).",
     "konsequenz": "Erheblicher Nikotinabusus ist Bedenkenstatbestand nach 2.1.1 (Gefahr "
                   "mangelhafter Hygienemaßnahmen, zusätzliche Cadmium-Aufnahme): Bedenken "
                   "prüfen, intensive Tabakentwöhnungsberatung anbieten; bei Reduktion "
                   "Neubeurteilung, ggf. keine Bedenken unter Voraussetzungen (2.1.3) mit "
                   "verkürzten Nachuntersuchungsfristen."},
    {"wenn": {"rauchen": ["bis10", "10bis20"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 3.1.4 (Biomonitoring, Fußnote zu Raucherwerten) und 2.2",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Raucherstatus beim Biomonitoring berücksichtigen (BAR-Werte von 0,8 µg/l "
                   "Urin bzw. 1 µg/l Vollblut gelten für Nichtraucher – für Raucher gelten "
                   "andere Werte). Beratung zur zusätzlichen Cadmium-Aufnahme durch Rauchen und "
                   "zu Hygienemaßnahmen (Händewaschen vor Raucherpausen); Rauchstopp empfehlen."},
    # ── Schutz / Hygiene (Abschnitt 2.2) ──────────────────────────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Atemschutz",
     "quelle": "Abschnitte 2.1.3 und 2.2",
     "befund": "Atemschutz wird bei staub-/rauchintensiven Arbeiten selten oder nie getragen.",
     "konsequenz": "Beratung zum Tragen der persönlichen Schutzausrüstung und zu den Gefahren "
                   "der inhalativen Cadmium-Aufnahme; Ursachen der Nichtbenutzung klären. "
                   "Ergibt sich Bedarf zur Verbesserung des Arbeitsschutzes, Mitteilung an den "
                   "Arbeitgeber zur Aktualisierung der Gefährdungsbeurteilung (2.2)."},
    {"wenn": {"hygiene": ["essen_am_platz", "haende_selten", "kein_kleidungswechsel"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 2.2 (Beratung) und 2.1.1",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht durchgehend eingehalten.",
     "konsequenz": "Einhaltung allgemeiner Hygienemaßnahmen empfehlen: kein Essen, Trinken "
                   "oder Rauchen am Arbeitsplatz, gründliches Händewaschen vor Pausen, "
                   "konsequenter Wechsel der Arbeitskleidung – Vermeidung der Cadmium-Aufnahme "
                   "über den Magen-Darm-Trakt."},
    # ── Mutterschutz ──────────────────────────────────────────────────────
    {"wenn": {"schwanger": ["ja"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 2.2 (Beratung: fruchtschädigende/fortpflanzungsgefährdende Wirkung)",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben.",
     "konsequenz": "Cadmium und einige Cadmiumverbindungen wirken fruchtschädigend und "
                   "fortpflanzungsgefährdend: Beschäftigungsbeschränkungen für werdende und "
                   "stillende Mütter unverzüglich klären, bevor die Tätigkeit (weiter) "
                   "ausgeübt wird; Arbeitgeber zur Anpassung der Arbeitsbedingungen beraten."},
]
