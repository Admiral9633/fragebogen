# -*- coding: utf-8 -*-
"""G 44 Hartholzstäube – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 44 »Hartholzstäube«
(Fassung Oktober 2014), S. 847–854."""

SLUG = "g44-hartholzstaub-2016"

CATALOG = {
    "version": 2,
    "title": "G 44 Hartholzstäube (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 44 »Hartholzstäube« (Fassung Oktober 2014), S. 847–854",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "anlass",
            "title": "Untersuchungsanlass",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "unt_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich heute?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachgehende "
                            "Untersuchung: nach dem Ende der Tätigkeit mit Hartholzstaub.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (Tätigkeit läuft bereits)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (Tätigkeit ist beendet)"},
                    ],
                },
                {
                    "id": "alter_ab45",
                    "type": "yes_no",
                    "label": "Sind Sie 45 Jahre alt oder älter?",
                    "hint": "Ab dem 45. Lebensjahr sieht der Grundsatz zusätzlich eine "
                            "Spiegelung der inneren Nase (Endoskopie) und kürzere "
                            "Untersuchungsabstände vor.",
                    "required": True,
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Staubbelastung ───────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Staubbelastung",
            "subtitle": "Ihre Arbeit mit Hartholz und Holzstaub",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "betriebsart",
                    "type": "multi_choice",
                    "label": "In welcher Art von Betrieb arbeiten Sie?",
                    "hint": "In diesen Betrieben ist erfahrungsgemäß mit Hartholzstaub zu "
                            "rechnen. Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "moebeltischlerei", "label": "Möbeltischlerei / Schreinerei"},
                        {"value": "stellmacherei", "label": "Stellmacherei / Wagnerei"},
                        {"value": "parkett_treppen", "label": "Parkettlegerei oder Treppenbau"},
                        {"value": "modellschreinerei", "label": "Modellschreinerei (Gießerei)"},
                        {"value": "holzmehl_pellets", "label": "Herstellung/Verarbeitung von Holzmehl oder Pellets"},
                        {"value": "andere", "label": "Anderer holzverarbeitender Betrieb"},
                        {"value": "keine", "label": "Keiner dieser Betriebe"},
                    ],
                },
                {
                    "id": "buche_eiche",
                    "type": "choice",
                    "label": "Be- oder verarbeiten Sie Buchen- oder Eichenholz?",
                    "hint": "Stäube von Buchen- und Eichenholz sind für die Berufskrankheit "
                            "Nr. 4203 (Adenokarzinom der Nase) besonders bedeutsam.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein, andere Hölzer"},
                        {"value": "weiss_nicht", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "expo_beginn",
                    "type": "choice",
                    "label": "Vor wie vielen Jahren hat Ihre Tätigkeit mit Holzstaub begonnen?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Noch gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter5", "label": "Vor weniger als 5 Jahren"},
                        {"value": "5bis15", "label": "Vor 5 bis 15 Jahren"},
                        {"value": "ueber15", "label": "Vor mehr als 15 Jahren"},
                    ],
                },
                {
                    "id": "staub_massnahmen",
                    "type": "choice",
                    "label": "Gibt es an Ihrem Arbeitsplatz wirksame Absaugungen oder andere "
                             "Maßnahmen gegen Holzstaub?",
                    "required": True,
                    "options": [
                        {"value": "wirksam", "label": "Ja, Maschinen sind abgesaugt, kaum sichtbarer Staub"},
                        {"value": "teilweise", "label": "Teilweise, es staubt trotzdem öfter"},
                        {"value": "keine", "label": "Nein, es ist regelmäßig staubig"},
                        {"value": "weiss_nicht", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "chemikalien",
                    "type": "yes_no",
                    "label": "Bearbeiten Sie chemisch behandeltes Holz oder arbeiten Sie mit "
                             "Holzschutzmitteln oder anderen Chemikalien am Holz?",
                    "required": True,
                    "followup": {"id": "chemikalien_desc", "type": "text",
                                 "label": "Welche Mittel bzw. welche Arbeiten?", "when": "yes"},
                },
                {
                    "id": "frueher_holzstaub",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Berufen oder Tätigkeiten Holzstaub ausgesetzt?",
                    "required": True,
                    "followup": {"id": "frueher_holzstaub_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden an der Nase",
            "subtitle": "Auf diese Beschwerden ist nach dem Grundsatz besonders zu achten",
            "questions": [
                {
                    "id": "nasenatmung",
                    "type": "yes_no",
                    "label": "Ist Ihre Nasenatmung behindert (Sie bekommen durch die Nase "
                             "schlecht Luft)?",
                    "required": True,
                    "followup": {"id": "nasenatmung_desc", "type": "text",
                                 "label": "Seit wann, und eher auf einer Seite oder beidseits?",
                                 "when": "yes"},
                },
                {
                    "id": "sekret",
                    "type": "yes_no",
                    "label": "Haben Sie vermehrten Ausfluss aus der Nase (ständig laufende "
                             "oder verschleimte Nase)?",
                    "required": True,
                },
                {
                    "id": "nasenbluten",
                    "type": "choice",
                    "label": "Haben Sie Nasenbluten?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein / praktisch nie"},
                        {"value": "selten", "label": "Gelegentlich"},
                        {"value": "haeufig", "label": "Häufig oder blutig gefärbter Schnupfen"},
                    ],
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Frühere und aktuelle Erkrankungen",
            "questions": [
                {
                    "id": "nase_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie Erkrankungen der Nase oder der Nasennebenhöhlen "
                             "(z. B. chronische Nebenhöhlen-Entzündung, Polypen)?",
                    "required": True,
                    "followup": {"id": "nase_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "tumor_nase",
                    "type": "yes_no",
                    "label": "Hatten Sie früher eine bösartige Tumorerkrankung (Krebs) der "
                             "inneren Nase oder der Nasennebenhöhlen?",
                    "required": True,
                },
                {
                    "id": "tumor_aktuell",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen derzeit eine bösartige Tumorerkrankung der "
                             "inneren Nase oder der Nasennebenhöhlen?",
                    "required": True,
                },
                {
                    "id": "dysplasie",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen durch eine Gewebeprobe (Biopsie) eine "
                             "Gewebeveränderung der Nasenschleimhaut festgestellt "
                             "(dysplastische Veränderung)?",
                    "required": True,
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach", "nachgehend"]},
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
                },
                {
                    "id": "allg_gesundheit",
                    "type": "yes_no",
                    "label": "Gibt es sonstige Erkrankungen oder gesundheitliche "
                             "Einschränkungen, die wir kennen sollten?",
                    "required": True,
                    "followup": {"id": "allg_gesundheit_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
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
    # ── Dauernde gesundheitliche Bedenken (Abschnitt 2.1.1) ───────────────
    {"wenn": {"tumor_nase": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Tumorerkrankung Nase/NNH",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Vorangegangene maligne Tumorerkrankung der inneren Nase bzw. der "
               "Nasennebenhöhlen angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken gegen Aufnahme bzw. Fortsetzung "
                   "einer Tätigkeit mit Hartholzstaubexposition aussprechen; HNO-Vorbefunde "
                   "einholen und die Person über die Beurteilung informieren."},
    {"wenn": {"tumor_aktuell": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Tumorerkrankung Nase/NNH",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Manifeste maligne Tumorerkrankung der inneren Nase bzw. der "
               "Nasennebenhöhlen angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken gegen die Fortsetzung der Tätigkeit; "
                   "fachärztliche (HNO-)Behandlung sicherstellen und Anzeige auf Verdacht "
                   "einer Berufskrankheit Nr. 4203 prüfen."},
    {"wenn": {"dysplasie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gewebeveränderung",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Bioptisch gesicherte dysplastische Veränderung der Nasenschleimhaut "
               "angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchungen ansetzen (engmaschige endoskopische "
                   "Kontrolle mit Fotodokumentation); Befunde der Biopsie beiziehen und "
                   "HNO-ärztliche Mitbetreuung sicherstellen."},
    # ── Beschwerden, auf die besonders zu achten ist (1.2.1/1.2.3) ────────
    {"wenn": {"nasenatmung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nasensymptome",
     "quelle": "Abschnitte 1.2.1 und 1.2.3",
     "befund": "Behinderte Nasenatmung angegeben.",
     "konsequenz": "Gezielte Inspektion der inneren Nase mit Nasenspekulum (ab dem "
                   "45. Lebensjahr zusätzlich Endoskopie); in unklaren Fällen "
                   "Ergänzungsuntersuchung: weiterführende HNO-ärztliche Untersuchung, "
                   "z. B. Wiederholung der Endoskopie, ggf. Biopsie zur histologischen "
                   "Abklärung."},
    {"wenn": {"sekret": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nasensymptome",
     "quelle": "Abschnitte 1.2.1 und 1.2.3",
     "befund": "Vermehrte Sekretabsonderung aus der Nase angegeben.",
     "konsequenz": "Gezielte Inspektion der inneren Nase; in unklaren Fällen "
                   "Ergänzungsuntersuchung (HNO-ärztliche Abklärung, Endoskopie-"
                   "Wiederholung, ggf. Biopsie)."},
    {"wenn": {"nasenbluten": ["haeufig"]},
     "schwere": "pruefen",
     "bereich": "Nasensymptome",
     "quelle": "Abschnitte 1.2.1 und 1.2.3",
     "befund": "Häufiges Nasenbluten bzw. blutig gefärbter Schnupfen angegeben.",
     "konsequenz": "Tumorverdacht ausschließen: Inspektion der inneren Nase, ggf. "
                   "Endoskopie; in unklaren Fällen weiterführende HNO-ärztliche "
                   "Untersuchung mit Biopsie zur histologischen Abklärung."},
    {"wenn": {"nase_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung Nase/NNH",
     "quelle": "Abschnitt 1.2.1 (Allgemeine Untersuchung)",
     "befund": "Vorausgegangene Erkrankung der Nase oder der Nasennebenhöhlen angegeben.",
     "konsequenz": "Vorbefunde beiziehen; Inspektion bzw. Endoskopie der inneren Nase "
                   "besonders sorgfältig durchführen, in unklaren Fällen HNO-ärztliche "
                   "Ergänzungsuntersuchung."},
    # ── Untersuchungsprogramm und Fristen ab 45 (1.1/1.2.2) ───────────────
    {"wenn": {"alter_ab45": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Untersuchungsprogramm ab 45",
     "quelle": "Abschnitt 1.2.2 (Spezielle Untersuchung)",
     "befund": "Alter 45 Jahre oder älter angegeben.",
     "konsequenz": "Zusätzlich zur Inspektion mit dem Nasenspekulum eine Endoskopie der "
                   "inneren Nase mit starrem oder ggf. flexiblem Endoskop durchführen; "
                   "bei auffälligem oder unklarem Befund Fotodokumentation."},
    {"wenn": {"alter_ab45": ["yes"], "expo_beginn": ["ueber15"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Alter ab 45 Jahren und Expositionsbeginn vor mehr als 15 Jahren.",
     "konsequenz": "Nachuntersuchungsfrist verkürzen: nächste Nachuntersuchung nach "
                   "weniger als 18 Monaten (statt weniger als 60 Monaten bis zum "
                   "45. Lebensjahr); Termin entsprechend einplanen."},
    # ── Vorzeitige Nachuntersuchungen (1.1) ───────────────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungen, vorzeitig)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen eine Fortsetzung "
                   "der Tätigkeit geben könnte; vorzeitige Nachuntersuchung ansetzen und "
                   "Befunde der behandelnden Ärzte beiziehen."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungen, vorzeitig)",
     "befund": "Die Person vermutet einen ursächlichen Zusammenhang zwischen Erkrankung "
               "und Tätigkeit am Arbeitsplatz.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen; Beschwerden gezielt abklären "
                   "und ggf. Anzeige auf Verdacht einer Berufskrankheit Nr. 4203 erstatten."},
    # ── Nachgehende Untersuchungen (1.1) ──────────────────────────────────
    {"wenn": {"unt_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitt 1.1 (Nachgehende Untersuchungen)",
     "befund": "Vorstellung zur nachgehenden Untersuchung nach Ausscheiden aus der "
               "Tätigkeit.",
     "konsequenz": "Untersuchungsprogramm wie bei der Nachuntersuchung durchführen "
                   "(Inspektion, ab dem 45. Lebensjahr Endoskopie); Organisation und "
                   "weitere Einladungen über den Organisationsdienst für nachgehende "
                   "Untersuchungen (ODIN, www.odin-info.de) sicherstellen."},
    {"wenn": {"frueher_holzstaub": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitt 1.1 (Nachgehende Untersuchungen)",
     "befund": "Frühere Tätigkeiten mit Holzstaubexposition angegeben.",
     "konsequenz": "Frühere Expositionszeiten dokumentieren (lange Latenzzeit der "
                   "Adenokarzinome); sicherstellen, dass die Person für nachgehende "
                   "Untersuchungen (ODIN) erfasst ist bzw. wird."},
    # ── Exposition und Arbeitsschutz (3.1, 3.2.1, 2.2) ────────────────────
    {"wenn": {"staub_massnahmen": ["keine", "teilweise"]},
     "schwere": "hinweis",
     "bereich": "Staubminderung",
     "quelle": "Abschnitte 3.1.2 und 2.2 (Beratung)",
     "befund": "Absaugung bzw. Staubminderung am Arbeitsplatz fehlt oder ist nur "
               "teilweise wirksam.",
     "konsequenz": "Auf das Minimierungsgebot der GefStoffV hinweisen (Holzstaub-"
                   "Konzentration möglichst unter 2 mg/m³). Ergeben sich Hinweise auf "
                   "notwendige Verbesserungen des Arbeitsschutzes, dies dem Arbeitgeber "
                   "zur Aktualisierung der Gefährdungsbeurteilung mitteilen – unter "
                   "Wahrung der schutzwürdigen Belange der untersuchten Person."},
    {"wenn": {"chemikalien": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Chemisch behandeltes Holz",
     "quelle": "Abschnitt 3.2.1 (Wirkungsweise)",
     "befund": "Bearbeitung chemisch vorbehandelten Holzes bzw. Umgang mit "
               "Holzschutzmitteln angegeben.",
     "konsequenz": "Exposition dokumentieren und mit der Gefährdungsbeurteilung "
                   "abgleichen: Erkrankungen wurden vorwiegend bei Personen beobachtet, "
                   "die chemisch vorbehandeltes Hartholz be- oder verarbeiteten; Beratung "
                   "zu Schutzmaßnahmen intensivieren."},
]
