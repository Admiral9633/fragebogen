# -*- coding: utf-8 -*-
"""G 5 Glykoldinitrat oder Glycerintrinitrat (Nitroglykol oder Nitroglycerin) –
DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für arbeitsmedizinische
Untersuchungen, 6. Auflage 2016, G 5 (Fassung Oktober 2014), S. 155–163."""

SLUG = "g5-nitroglycerin-2016"

CATALOG = {
    "version": 2,
    "title": "G 5 Glykoldinitrat oder Glycerintrinitrat (Nitroglykol oder "
             "Nitroglycerin) (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 5 »Glykoldinitrat oder Glycerintrinitrat (Nitroglykol oder "
             "Nitroglycerin)« (Fassung Oktober 2014), S. 155–163",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Untersuchungsanlass",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Ist dies Ihre Erstuntersuchung oder eine Nachuntersuchung "
                             "nach dem Grundsatz G 5?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. "
                            "Nachuntersuchungen: erste nach 6–12 Monaten, weitere nach "
                            "12–24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Umgang mit Sprengöl",
            "subtitle": "Ihre Arbeit mit Nitroglykol (Glykoldinitrat) und "
                        "Nitroglycerin (Glycerintrinitrat)",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "taetigkeiten",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten haben Sie Kontakt mit Sprengöl oder "
                             "sprengölhaltigen Produkten?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "pulverrohmasse", "label": "Herstellen oder innerbetrieblicher Transport von "
                                                             "Pulverrohmasse für gelatinöse Sprengstoffe"},
                        {"value": "abfuellen", "label": "Abfüllen aus Lagertanks in Transportbehälter"},
                        {"value": "nitrieren", "label": "Herstellen von Nitroglykol durch Nitrieren "
                                                        "(diskontinuierliches Verfahren)"},
                        {"value": "gelatinieren", "label": "Gelatinieren von Nitroglykol"},
                        {"value": "reparatur", "label": "Reparatur- oder Instandhaltungsarbeiten an "
                                                        "nitroglykolhaltigen Anlagenteilen"},
                        {"value": "lagern", "label": "Lagern von gelatinösen Sprengstoffen"},
                        {"value": "probennahme", "label": "Probennahme (z. B. Qualitätsprüfung von Sprengstoffpatronen)"},
                        {"value": "vernichten", "label": "Vernichten von nitroglykolhaltigen Stoffresten "
                                                         "oder Anlagenteilen"},
                        {"value": "labor", "label": "Laborarbeiten"},
                        {"value": "andere", "label": "Andere Tätigkeit mit möglichem Kontakt"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "stoffe",
                    "type": "multi_choice",
                    "label": "Mit welchen Stoffen haben Sie dabei zu tun?",
                    "hint": "Mehrfachauswahl möglich. Nitroglykol ist etwa 30-fach "
                            "flüchtiger als Nitroglycerin.",
                    "required": True,
                    "options": [
                        {"value": "nitroglykol", "label": "Glykoldinitrat (Nitroglykol)"},
                        {"value": "nitroglycerin", "label": "Glycerintrinitrat (Nitroglycerin)"},
                        {"value": "gemisch", "label": "Gemische / Sprengöl allgemein"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt mit diesen Stoffen?",
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
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kann es bei Ihrer Arbeit zu direktem Hautkontakt mit Sprengöl "
                             "oder benetzten Teilen kommen (z. B. beim Anfassen, Reinigen, "
                             "bei Spritzern)?",
                    "hint": "Die Stoffe werden über die Atemwege und sehr gut über die "
                            "Haut aufgenommen.",
                    "required": True,
                },
                {
                    "id": "zusatzstoffe",
                    "type": "yes_no",
                    "label": "Arbeiten Sie zusätzlich mit anderen Explosivstoffen oder "
                             "Zusatzstoffen, z. B. TNT (Trinitrotoluol)?",
                    "required": True,
                    "followup": {"id": "zusatzstoffe_desc", "type": "text",
                                 "label": "Mit welchen Stoffen?", "when": "yes"},
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle oder Unfälle mit diesen "
                             "Stoffen (z. B. Verschütten, undichte Anlage)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_exposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit Sprengstoffen, "
                             "Sprengölen oder vergleichbaren Gefahrstoffen?",
                    "required": True,
                    "followup": {"id": "frueher_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, und wie lange?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Persönliche Schutzausrüstung und Hygiene am Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_tragen",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit möglichem Kontakt Ihre persönliche "
                             "Schutzausrüstung (z. B. geeignete Schutzhandschuhe, "
                             "Schutzkleidung)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_umgang", "label": "Ich habe (noch) keinen Umgang mit diesen Stoffen"},
                    ],
                },
                {
                    "id": "hygiene_umsetzung",
                    "type": "yes_no",
                    "label": "Halten Sie die Hygieneregeln am Arbeitsplatz ein (Arbeitskleidung "
                             "regelmäßig wechseln, Hände waschen vor Pausen, nicht am "
                             "Arbeitsplatz essen oder rauchen)?",
                    "required": True,
                    "show_if": {"id": "psa_tragen", "not_in": ["kein_umgang"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die mit diesen Stoffen zusammenhängen können",
            "questions": [
                {
                    "id": "brustschmerz",
                    "type": "yes_no",
                    "label": "Haben Sie Schmerzen, Druck- oder Engegefühl in der Brust oder "
                             "in der Herzgegend (Angina-pectoris-ähnliche Beschwerden)?",
                    "required": True,
                    "followup": {"id": "brustschmerz_desc", "type": "textarea",
                                 "label": "Wann treten die Beschwerden auf (z. B. bei Anstrengung, "
                                          "in Ruhe, an arbeitsfreien Tagen oder am Wochenende)?",
                                 "when": "yes"},
                },
                {
                    "id": "akutbeschwerden",
                    "type": "multi_choice",
                    "label": "Treten bei Ihnen während oder kurz nach der Arbeit folgende "
                             "Beschwerden auf?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "kopfschmerzen", "label": "Kopfschmerzen"},
                        {"value": "schwindel", "label": "Schwindel"},
                        {"value": "uebelkeit", "label": "Übelkeit oder Brechreiz"},
                        {"value": "gesichtsroetung", "label": "Gesichtsrötung oder Hitzegefühl im Kopf"},
                        {"value": "missempfindungen", "label": "Kribbeln oder Taubheitsgefühl "
                                                               "(z. B. in Händen oder Füßen)"},
                        {"value": "angstgefuehl", "label": "Angst- oder Beklemmungsgefühl"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "ohnmacht",
                    "type": "yes_no",
                    "label": "Sind Sie bei der Arbeit schon einmal ohnmächtig geworden oder "
                             "ist Ihr Kreislauf zusammengebrochen (Kollaps)?",
                    "required": True,
                    "followup": {"id": "ohnmacht_desc", "type": "textarea",
                                 "label": "Wann, und bei welcher Tätigkeit?", "when": "yes"},
                },
                {
                    "id": "chronisch_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie seit der letzten Untersuchung eine oder mehrere der "
                             "folgenden Beschwerden bemerkt?",
                    "hint": "Mehrfachauswahl möglich. Solche Beschwerden können bei "
                            "länger dauerndem Umgang mit Sprengöl auftreten.",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "options": [
                        {"value": "kopfschmerzen_haeufig", "label": "Häufige Kopfschmerzen"},
                        {"value": "waermegefuehl", "label": "Ungewohntes Wärmegefühl"},
                        {"value": "trunkenheitsgefuehl", "label": "Gefühl wie »benommen« oder »betrunken« "
                                                                  "ohne Alkohol (Trunkenheitsgefühl)"},
                        {"value": "appetitlosigkeit", "label": "Appetitlosigkeit"},
                        {"value": "alkoholintoleranz", "label": "Alkohol wird schlechter vertragen als früher "
                                                                "(Alkoholintoleranz)"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "schwere_erkrankung_seit",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung (z. B. mit Krankenhausaufenthalt oder "
                             "längerer Krankschreibung)?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {"id": "verdacht_zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den Zusammenhang?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Herz, Kreislauf, Vorerkrankungen ───────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Herz, Kreislauf & Vorerkrankungen",
            "subtitle": "Erkrankungen und Medikamente, die für diese Untersuchung wichtig sind",
            "questions": [
                {
                    "id": "herzkrankheit",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Herzerkrankung bekannt (z. B. koronare "
                             "Herzkrankheit, Herzinfarkt, Herzschwäche, Herzklappenfehler)?",
                    "required": True,
                    "followup": {"id": "herzkrankheit_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, und wie wird sie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "vasodilatantien",
                    "type": "yes_no",
                    "label": "Nehmen Sie gefäßerweiternde Medikamente ein (z. B. Nitropräparate "
                             "wie Nitrospray oder Nitro-Kapseln)?",
                    "hint": "Solche Medikamente wirken ähnlich wie die Arbeitsstoffe – die "
                            "Wirkungen können sich verstärken.",
                    "required": True,
                    "followup": {"id": "vasodilatantien_desc", "type": "text",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
                {
                    "id": "ekg_auffaellig",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen jemals eine krankhafte Veränderung im EKG "
                             "(Herzstromkurve) oder eine Herzrhythmusstörung festgestellt?",
                    "required": True,
                },
                {
                    "id": "blutdruck",
                    "type": "choice",
                    "label": "Wurde bei Ihnen ein auffälliger Blutdruck festgestellt?",
                    "required": True,
                    "options": [
                        {"value": "hoch", "label": "Ja, zu hoher Blutdruck (Hypertonie)"},
                        {"value": "niedrig", "label": "Ja, zu niedriger Blutdruck (Hypotonie)"},
                        {"value": "nein", "label": "Nein, Blutdruck ist normal"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "hypotonie_neigung",
                    "type": "yes_no",
                    "label": "Neigen Sie zu Kreislaufschwäche, Schwindel beim Aufstehen, "
                             "Kollaps oder Ohnmachtsanfällen (Synkopen)?",
                    "required": True,
                },
                {
                    "id": "organ_erkrankungen",
                    "type": "yes_no",
                    "label": "Haben Sie andere Erkrankungen, die Herz oder Kreislauf belasten "
                             "können (z. B. Schilddrüsenüberfunktion, schwere Lungen- oder "
                             "Nierenerkrankung, Blutarmut)?",
                    "required": True,
                    "followup": {"id": "organ_erkrankungen_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Berufskrankheit anerkannt oder läuft "
                             "derzeit ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Berufskrankheit bzw. welches Verfahren?",
                                 "when": "yes"},
                },
                {
                    "id": "gesundheit_allgemein",
                    "type": "yes_no",
                    "label": "Gibt es sonstige gesundheitliche Einschränkungen oder "
                             "Erkrankungen, die wir kennen sollten?",
                    "required": True,
                    "followup": {"id": "gesundheit_allgemein_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
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
    # ── Bedenken-Tatbestände (Abschnitt 2.1.1) ────────────────────────────
    {"wenn": {"herzkrankheit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herzerkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Herzerkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken: kardiologische "
                   "Befunde einholen, EKG und Ergometrie (Untersuchungsprogramm 1.2.2) "
                   "besonders sorgfältig bewerten. Bei weniger ausgeprägter Erkrankung "
                   "prüfen, ob nach 2.1.3 keine Bedenken unter Voraussetzungen möglich "
                   "sind (technische/organisatorische Schutzmaßnahmen, Begrenzung der "
                   "Expositionszeit, expositionsärmerer Arbeitsplatz, PSA, verkürzte "
                   "Nachuntersuchungsfristen); bei zu erwartender Wiederherstellung "
                   "befristete Bedenken (2.1.2)."},
    {"wenn": {"ekg_auffaellig": ["yes"]},
     "schwere": "kritisch",
     "bereich": "EKG-Veränderungen",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "EKG-Veränderung bzw. Herzrhythmusstörung ärztlich festgestellt.",
     "konsequenz": "EKG-Veränderungen von Krankheitswert sind Tatbestand für dauernde "
                   "gesundheitliche Bedenken: Vorbefunde einholen, aktuelles EKG und "
                   "Ergometrie durchführen und beurteilen. Bei weniger ausgeprägtem "
                   "Befund Voraussetzungen nach 2.1.3 (Schutzmaßnahmen, verkürzte "
                   "Nachuntersuchungsfristen) prüfen."},
    {"wenn": {"ohnmacht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Akute Einwirkung",
     "quelle": "Abschnitte 3.2.2 und 2.1",
     "befund": "Ohnmacht bzw. Kreislaufkollaps bei der Arbeit angegeben.",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Tätigkeit klären (Verdacht auf "
                   "akute Vergiftung durch Salpetersäureester): Kreislauffunktionsprüfung "
                   "(z. B. Schellong), Langzeit-Blutdruckmessung, EKG/Ergometrie bewerten; "
                   "Expositionssituation und Schutzmaßnahmen überprüfen und dem "
                   "Arbeitgeber ggf. Aktualisierung der Gefährdungsbeurteilung mitteilen. "
                   "BK-Nr. 1309 (Verdachtsanzeige) prüfen."},
    {"wenn": {"blutdruck": ["hoch", "niedrig"]},
     "schwere": "pruefen",
     "bereich": "Blutdruck",
     "quelle": "Abschnitt 2.1.1 (Blutdruckwerte)",
     "befund": "Auffälliger Blutdruck (zu hoch oder zu niedrig) bekannt.",
     "konsequenz": "Langzeit-Blutdruckmessung durchführen (im Grundsatz ausdrücklich "
                   "hervorgehoben). Dauernde gesundheitliche Bedenken bei bestätigten "
                   "Werten: systolisch über 140 mmHg oder unter 90 mmHg, diastolisch über "
                   "90 mmHg oder unter 60 mmHg, Amplitude unter 30 mmHg. Bei weniger "
                   "ausgeprägten Befunden 2.1.3 anwenden (Schutzmaßnahmen, verkürzte "
                   "Nachuntersuchungsfristen); Beratung zu regelmäßiger Blutdruckkontrolle."},
    {"wenn": {"hypotonie_neigung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kreislauf",
     "quelle": "Abschnitte 1.2.2 und 2.1.1",
     "befund": "Neigung zu Kreislaufschwäche, Kollaps oder Synkopen angegeben.",
     "konsequenz": "Kreislauffunktionsprüfung (z. B. Schellong) und Langzeit-Blutdruck- "
                   "messung durchführen; da die Arbeitsstoffe den Blutdruck zusätzlich "
                   "senken, Beurteilung nach 2.1.1 (systolisch unter 90 mmHg, diastolisch "
                   "unter 60 mmHg) vornehmen; ggf. Bedenken bzw. Voraussetzungen nach "
                   "2.1.3 prüfen."},
    {"wenn": {"organ_erkrankungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Andere Organerkrankungen",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Erkrankung angegeben, die Herz oder Kreislauf zusätzlich belasten kann.",
     "konsequenz": "Abklären, ob eine Herz- und Kreislaufbelastung durch anderweitige "
                   "Organschäden vorliegt (Bedenken-Tatbestand nach 2.1.1); Befunde "
                   "einholen; ggf. Voraussetzungen nach 2.1.3 oder befristete Bedenken "
                   "nach 2.1.2 prüfen."},
    {"wenn": {"vasodilatantien": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Medikamente",
     "quelle": "Abschnitte 2.1.1 (Herzkrankheiten) und 3.2.1",
     "befund": "Therapie mit gefäßerweiternden Medikamenten (z. B. Nitropräparaten) angegeben.",
     "konsequenz": "Zugrunde liegende Herz-Kreislauf-Erkrankung abklären (möglicher "
                   "Bedenken-Tatbestand nach 2.1.1); additive gefäßerweiternde Wirkung "
                   "mit den Arbeitsstoffen berücksichtigen. Rücksprache mit den "
                   "behandelnden Ärztinnen/Ärzten; Blutdruckkontrolle."},
    # ── Beschwerden ───────────────────────────────────────────────────────
    {"wenn": {"brustschmerz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Angina-pectoris-Symptomatik",
     "quelle": "Abschnitte 3.2.2/3.2.3 und 2.1.1",
     "befund": "Schmerzen, Druck- oder Engegefühl in Brust/Herzgegend angegeben.",
     "konsequenz": "Kardiologische Abklärung: EKG und Ergometrie (1.2.2) besonders "
                   "sorgfältig bewerten; zeitlichen Zusammenhang mit Exposition bzw. "
                   "expositionsfreien Tagen klären. Bei bestätigter Herzkrankheit "
                   "Bedenken nach 2.1.1; BK-Nr. 1309 (Verdachtsanzeige) prüfen."},
    {"wenn": {"akutbeschwerden": ["kopfschmerzen", "schwindel", "uebelkeit",
                                  "gesichtsroetung", "missempfindungen", "angstgefuehl"]},
     "schwere": "pruefen",
     "bereich": "Akute Einwirkung",
     "quelle": "Abschnitt 3.2.2",
     "befund": "Arbeitsbezogene Beschwerden angegeben, die zu einer akuten/subakuten "
               "Vergiftung durch Salpetersäureester passen.",
     "konsequenz": "Blutdruck kontrollieren, Kreislauffunktionsprüfung (z. B. Schellong) "
                   "erwägen; bei Nachuntersuchung Biomonitoring (3.1.4) heranziehen. "
                   "Exposition und Schutzmaßnahmen überprüfen; wenn die Gefährdungs- "
                   "beurteilung aktualisiert werden muss, Mitteilung an den Arbeitgeber "
                   "(unter Wahrung der schutzwürdigen Belange)."},
    {"wenn": {"chronisch_beschwerden": ["kopfschmerzen_haeufig", "waermegefuehl",
                                        "trunkenheitsgefuehl", "appetitlosigkeit",
                                        "alkoholintoleranz"]},
     "schwere": "pruefen",
     "bereich": "Chronische Einwirkung",
     "quelle": "Abschnitte 3.2.3 und 1.1",
     "befund": "Beschwerden angegeben, die zu einer chronischen Einwirkung passen "
               "(Kopfschmerzen, Wärme-/Trunkenheitsgefühl, Appetitlosigkeit, "
               "Alkoholintoleranz).",
     "konsequenz": "Vertiefte ärztliche Anamnese, Blutdruck-/Langzeit-Blutdruckmessung "
                   "und EKG bewerten; Biomonitoring (3.1.4) heranziehen. Verkürzte "
                   "Nachuntersuchungsfrist (2.1.3) bzw. vorzeitige Nachuntersuchung nach "
                   "ärztlichem Ermessen (1.1) erwägen; BK-Nr. 1309 (Verdachtsanzeige) "
                   "prüfen."},
    # ── Fristen und Biomonitoring (Abschnitte 1.1, 1.2.2, 3.1.4) ──────────
    {"wenn": {"untersuchung_art": ["nach"],
              "stoffe": ["nitroglykol", "gemisch", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitte 1.2.2 und 3.1.4",
     "befund": "Nachuntersuchung mit (möglicher) Exposition gegenüber Glykoldinitrat.",
     "konsequenz": "Biomonitoring durchführen (nur bei der Nachuntersuchung): Parameter "
                   "Ethylendinitrat (Ethylenglykoldinitrat) im Vollblut, Biologischer "
                   "Grenzwert (BGW) 0,3 µg/l nach TRGS 903; Probennahme bei Expositions- "
                   "bzw. Schichtende. Qualitätssicherung nach Anhang 3 »Leitfaden "
                   "Biomonitoring« und AMR 6.2 beachten; Beschäftigte über das Ergebnis "
                   "informieren."},
    {"wenn": {"schwere_erkrankung_seit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungen, vorzeitig)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt: prüfen, ob die Erkrankung "
                   "Anlass zu Bedenken gegen eine Fortsetzung der Tätigkeit gibt; "
                   "Befunde der behandelnden Ärztinnen/Ärzte einholen; Beurteilung nach "
                   "2.1 (ggf. befristete Bedenken nach 2.1.2)."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungen, vorzeitig)",
     "befund": "Beschäftigte Person vermutet Zusammenhang zwischen Erkrankung und "
               "Tätigkeit am Arbeitsplatz.",
     "konsequenz": "Vorzeitige Nachuntersuchung ermöglichen; Beschwerden gezielt "
                   "abklären (EKG, Ergometrie, Langzeit-Blutdruckmessung, Biomonitoring). "
                   "Bei begründetem Verdacht auf eine Erkrankung durch Salpetersäureester "
                   "Verdachtsanzeige auf BK-Nr. 1309 stellen."},
    # ── Exposition und Schutzmaßnahmen ────────────────────────────────────
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitte 3.1.3 und 2.2",
     "befund": "Direkter Hautkontakt mit Sprengöl bzw. benetzten Teilen möglich.",
     "konsequenz": "Die Aufnahme erfolgt über Atemwege und Haut: Schutzmaßnahmen nach "
                   "TRGS 401 (Gefährdung durch Hautkontakt) mit der Gefährdungs- "
                   "beurteilung abgleichen; Beratung zu Hygienemaßnahmen und geeigneter "
                   "persönlicher Schutzausrüstung (2.2); ggf. Mitteilung an den "
                   "Arbeitgeber zur Aktualisierung der Gefährdungsbeurteilung."},
    {"wenn": {"psa_tragen": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzausrüstung",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Eindringliche Beratung zu persönlicher Schutzausrüstung und "
                   "Hygienemaßnahmen; Ursachen klären. Ergibt sich daraus die "
                   "Notwendigkeit, die Gefährdungsbeurteilung zu aktualisieren, dies dem "
                   "Arbeitgeber mitteilen (unter Wahrung der schutzwürdigen Belange der "
                   "untersuchten Person)."},
    {"wenn": {"zusatzstoffe": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zusatzstoffe",
     "quelle": "Abschnitt 1.2.2 (Spezielle Untersuchung)",
     "befund": "Umgang mit weiteren Explosiv-/Zusatzstoffen (z. B. TNT) angegeben.",
     "konsequenz": "Auf die spezifische Giftwirkung der Zusatzstoffe achten (z. B. TNT); "
                   "prüfen, ob weitere Grundsätze/Untersuchungsanlässe einschlägig sind, "
                   "und das Untersuchungsprogramm entsprechend erweitern."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitte 2.2 und 3.1.1",
     "befund": "Zwischenfälle oder Unfälle mit Sprengöl angegeben.",
     "konsequenz": "Hergang dokumentieren; auf Beschwerden im zeitlichen Zusammenhang "
                   "achten. Bei Hinweisen auf unzureichenden Arbeitsschutz dem "
                   "Arbeitgeber die Aktualisierung der Gefährdungsbeurteilung mitteilen."},
    {"wenn": {"hygiene_umsetzung": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht durchgehend eingehalten.",
     "konsequenz": "Auf die allgemeinen Hygienemaßnahmen hinweisen (Hände waschen vor "
                   "Pausen, nicht am Arbeitsplatz essen oder rauchen, Arbeitskleidung "
                   "wechseln); stoffspezifische Hinweise gibt GESTIS (»Umgang und "
                   "Verwendung«)."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitt 4 (Berufskrankheit)",
     "befund": "Anerkannte Berufskrankheit bzw. laufendes BK-Verfahren angegeben.",
     "konsequenz": "Angaben dokumentieren und bei der Beurteilung berücksichtigen; für "
                   "Erkrankungen durch Salpetersäureester ist BK-Nr. 1309 einschlägig. "
                   "Befunde bzw. Bescheide einbeziehen."},
]
