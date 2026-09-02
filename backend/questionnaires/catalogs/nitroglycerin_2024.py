# -*- coding: utf-8 -*-
"""Glycerintrinitrat (Nitroglycerin) und Glykoldinitrat (Nitroglykol) – DGUV
Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen
und Untersuchungen, 1. Auflage 2024, »Glycerintrinitrat (Nitroglycerin) und
Glykoldinitrat (Nitroglykol)« (E GLY, Fassung Januar 2022), S. 287–302."""

SLUG = "nitroglycerin-2024"

CATALOG = {
    "version": 2,
    "title": "Glycerintrinitrat (Nitroglycerin) und Glykoldinitrat (Nitroglykol) "
             "(DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Glycerintrinitrat (Nitroglycerin) und Glykoldinitrat "
             "(Nitroglykol)« (E GLY, Fassung Januar 2022), S. 287–302",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen "
                             "Nitroglycerin/Nitroglykol (Sprengöl)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge zu diesem Anlass"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zu dieser Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert nicht eingehalten wird oder eine "
                            "Gesundheitsgefährdung durch Hautkontakt nicht ausgeschlossen "
                            "werden kann. Angebotsvorsorge: wenn eine Exposition nicht "
                            "ausgeschlossen werden kann.",
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
            "title": "Tätigkeit & Umgang mit Sprengöl",
            "subtitle": "Ihre Arbeit mit Nitroglycerin (Glycerintrinitrat) und "
                        "Nitroglykol (Glykoldinitrat)",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
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
                                                             "Pulverrohmasse oder Pulvervorkonzentrat"},
                        {"value": "abfuellen", "label": "Abfüllen aus Lagertanks in Transport- oder Mischbehälter"},
                        {"value": "nitrieren", "label": "Herstellen durch Nitrieren (diskontinuierliches Verfahren)"},
                        {"value": "gelatinieren", "label": "Gelatinieren von Nitroglykol"},
                        {"value": "wartung", "label": "Wartungs-, Reinigungs- oder Instandhaltungsarbeiten "
                                                      "an Anlagenteilen"},
                        {"value": "lagern", "label": "Umgang mit oder Lagern von gelatinösen Sprengstoffen"},
                        {"value": "probennahme", "label": "Probennahme (z. B. Qualitätsprüfung von Sprengstoffpatronen)"},
                        {"value": "vernichten", "label": "Vernichten von Stoffresten oder Anlagenteilen"},
                        {"value": "labor", "label": "Laborarbeiten"},
                        {"value": "andere", "label": "Andere Tätigkeit mit möglichem Kontakt"},
                        {"value": "keine", "label": "Keine davon / nur geschlossene Anlagen"},
                    ],
                },
                {
                    "id": "stoffe",
                    "type": "multi_choice",
                    "label": "Mit welchen Stoffen haben Sie dabei zu tun?",
                    "hint": "Mehrfachauswahl möglich. Nitroglykol ist deutlich flüchtiger "
                            "als Nitroglycerin und kann auch eingeatmet werden.",
                    "required": True,
                    "options": [
                        {"value": "nitroglycerin", "label": "Glycerintrinitrat (Nitroglycerin)"},
                        {"value": "nitroglykol", "label": "Glykoldinitrat (Nitroglykol)"},
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
                    "hint": "Die Stoffe werden sehr gut über die Haut aufgenommen – das ist "
                            "unter Arbeitsbedingungen der wichtigste Aufnahmeweg.",
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
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle, Unfälle oder ungewöhnliche "
                             "Betriebszustände (z. B. Verschütten, undichte Anlage, Störung)?",
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
                    "label": "Haben Sie seit der letzten Vorsorge eine oder mehrere der "
                             "folgenden Beschwerden bemerkt?",
                    "hint": "Mehrfachauswahl möglich. Solche Beschwerden können bei "
                            "länger dauerndem Umgang mit Sprengöl auftreten.",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere"]},
                    "options": [
                        {"value": "herzrhythmus", "label": "Herzstolpern oder Herzrasen "
                                                           "(Herzrhythmusstörungen)"},
                        {"value": "kopfschmerzen_haeufig", "label": "Häufige Kopfschmerzen"},
                        {"value": "appetitlosigkeit", "label": "Appetitlosigkeit"},
                        {"value": "alkoholintoleranz", "label": "Alkohol wird schlechter vertragen als früher "
                                                                "(Alkoholintoleranz)"},
                        {"value": "waermegefuehl", "label": "Ungewohntes Wärmegefühl"},
                        {"value": "trunkenheitsgefuehl", "label": "Gefühl wie »benommen« oder »betrunken« "
                                                                  "ohne Alkohol (Trunkenheitsgefühl)"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
            ],
        },
        # ── 5 ─ Herz, Kreislauf, Vorerkrankungen ───────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Herz, Kreislauf & Vorerkrankungen",
            "subtitle": "Erkrankungen und Medikamente, die für diese Vorsorge wichtig sind",
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
                    "label": "Nehmen Sie gefäßerweiternde Medikamente ein (Vasodilatantien, "
                             "z. B. Nitropräparate wie Nitrospray oder Nitro-Kapseln)?",
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
                    "id": "chron_kopfschmerz",
                    "type": "yes_no",
                    "label": "Leiden Sie an chronischen, also häufig wiederkehrenden "
                             "Kopfschmerzen oder Migräne?",
                    "required": True,
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
    # ── Akute Einwirkung / Kollaps ────────────────────────────────────────
    {"wenn": {"ohnmacht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Akute Einwirkung",
     "quelle": "Abschnitte 6.3.2 und 7.4",
     "befund": "Ohnmacht bzw. Kreislaufkollaps bei der Arbeit angegeben.",
     "konsequenz": "Vor Fortsetzung der Tätigkeit ärztlich klären (Verdacht auf akute "
                   "Einwirkung von Salpetersäureestern – Lebensgefahr bei Haut- und "
                   "Atemkontakt): Kreislauffunktionsprüfung (z. B. Schellong) und "
                   "Langzeit-Blutdruckmessung durchführen, Expositionssituation mit der "
                   "Gefährdungsbeurteilung abgleichen. Reichen die Schutzmaßnahmen nicht "
                   "aus, Mitteilung an das Unternehmen mit Vorschlag von Maßnahmen "
                   "(§ 6 (4) ArbMedVV); BK-Nr. 1309 prüfen."},
    {"wenn": {"brustschmerz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Angina-pectoris-Symptomatik",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 7.4",
     "befund": "Schmerzen, Druck- oder Engegefühl in Brust/Herzgegend angegeben.",
     "konsequenz": "Kardiologische Abklärung veranlassen (EKG; auf eine Ergometrie wird "
                   "in der Empfehlung ausdrücklich verzichtet). Zeitlichen Zusammenhang "
                   "mit Exposition bzw. expositionsfreien Tagen klären; Beurteilung nach "
                   "Abschnitt 7.4, Maßnahmen nach 7.4.2 bzw. verkürzte Vorsorgefristen "
                   "nach 7.4.3 prüfen; BK-Nr. 1309 im Blick behalten."},
    {"wenn": {"akutbeschwerden": ["kopfschmerzen", "schwindel", "uebelkeit",
                                  "gesichtsroetung", "missempfindungen", "angstgefuehl"]},
     "schwere": "pruefen",
     "bereich": "Akute Einwirkung",
     "quelle": "Abschnitt 6.3.2",
     "befund": "Arbeitsbezogene Beschwerden angegeben, die zu einer akuten/subakuten "
               "Wirkung von Glycerintrinitrat/Glykoldinitrat passen.",
     "konsequenz": "Blutdruck kontrollieren, Kreislauffunktionsprüfung (z. B. Schellong) "
                   "erwägen; Expositionsquellen (v. a. Hautkontakt, bei Glykoldinitrat "
                   "auch Inhalation) und Schutzmaßnahmen überprüfen. Ergeben sich "
                   "Anhaltspunkte für unzureichende Schutzmaßnahmen, Mitteilung an das "
                   "Unternehmen nach § 6 (4) ArbMedVV."},
    {"wenn": {"chronisch_beschwerden": ["herzrhythmus", "kopfschmerzen_haeufig",
                                        "appetitlosigkeit", "alkoholintoleranz",
                                        "waermegefuehl", "trunkenheitsgefuehl"]},
     "schwere": "pruefen",
     "bereich": "Chronische Einwirkung",
     "quelle": "Abschnitte 6.3.3 und 7.1 (weitere Vorsorgen)",
     "befund": "Beschwerden angegeben, die zu einer chronischen Einwirkung passen "
               "(z. B. Herzrhythmusstörungen, Kopfschmerzen, Appetitlosigkeit, "
               "Alkoholintoleranz, Wärme-/Trunkenheitsgefühl).",
     "konsequenz": "Vertiefte ärztliche Anamnese; Blutdruckkontrolle bzw. "
                   "Langzeit-Blutdruckmessung und EKG erwägen. Verkürzte Vorsorgefrist "
                   "nach 7.4.3 prüfen; bei Verdacht auf eine Erkrankung durch "
                   "Salpetersäureester BK-Nr. 1309 (Verdachtsanzeige) prüfen."},
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"herzkrankheit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herzerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Herzerkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung: prüfen, ob die Tätigkeit im "
                   "Einzelfall ohne gesundheitliche Gefährdung möglich ist. Befunde der "
                   "behandelnden Ärzte einholen; Maßnahmen nach 7.4.2 (Substitution, "
                   "technische/organisatorische Maßnahmen, Begrenzung der Expositionszeit, "
                   "expositionsärmerer Arbeitsplatz, PSA) und verkürzte Fristen nach 7.4.3 "
                   "prüfen; ohne Erfolgsaussicht Tätigkeitswechsel erwägen (7.4.4, "
                   "Mitteilung an den Arbeitgeber nur mit Einwilligung)."},
    {"wenn": {"vasodilatantien": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Medikamente",
     "quelle": "Abschnitt 7.4 (Therapie mit Vasodilatantien)",
     "befund": "Therapie mit gefäßerweiternden Medikamenten (z. B. Nitropräparaten) angegeben.",
     "konsequenz": "Additive gefäßerweiternde Wirkung mit den Arbeitsstoffen "
                   "berücksichtigen (Beurteilungskriterium nach 7.4). Rücksprache mit den "
                   "behandelnden Ärztinnen/Ärzten; Blutdruckkontrolle; Maßnahmen nach "
                   "7.4.2 bzw. verkürzte Vorsorgefristen nach 7.4.3 prüfen."},
    {"wenn": {"ekg_auffaellig": ["yes"]},
     "schwere": "pruefen",
     "bereich": "EKG-Veränderungen",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "EKG-Veränderung bzw. Herzrhythmusstörung ärztlich festgestellt.",
     "konsequenz": "Vorbefunde einholen, aktuelles EKG erwägen. EKG-Veränderungen von "
                   "Krankheitswert sind bei der Beurteilung nach 7.4 zu berücksichtigen; "
                   "Maßnahmen nach 7.4.2 und verkürzte Fristen nach 7.4.3 prüfen."},
    {"wenn": {"blutdruck": ["hoch", "niedrig"]},
     "schwere": "pruefen",
     "bereich": "Blutdruck",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Auffälliger Blutdruck (zu hoch oder zu niedrig) bekannt.",
     "konsequenz": "Langzeit-Blutdruckmessung veranlassen (bei auffälligen Werten "
                   "ausdrücklich erwünscht). Beurteilungsgrenzen nach 7.4: systolisch über "
                   "140 mmHg oder unter 90 mmHg, diastolisch über 90 mmHg oder unter "
                   "60 mmHg, Amplitude unter 30 mmHg. Beratung zu regelmäßiger "
                   "Blutdruckkontrolle (Abschnitt 8.1); ggf. Maßnahmen nach 7.4.2 und "
                   "verkürzte Fristen nach 7.4.3."},
    {"wenn": {"hypotonie_neigung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kreislauf",
     "quelle": "Abschnitte 7.1 (Anamnese) und 7.2.2",
     "befund": "Neigung zu Hypotonie, Kollaps oder Synkopen angegeben.",
     "konsequenz": "Kreislauffunktionsprüfung (z. B. Schellong) durchführen; da die "
                   "Arbeitsstoffe den Blutdruck zusätzlich senken, Beurteilung nach 7.4 "
                   "(systolisch unter 90 mmHg, diastolisch unter 60 mmHg) und Maßnahmen "
                   "nach 7.4.2 prüfen."},
    {"wenn": {"organ_erkrankungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Andere Organerkrankungen",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Erkrankung angegeben, die Herz oder Kreislauf zusätzlich belasten kann.",
     "konsequenz": "Abklären, ob eine Herz-Kreislauf-Belastung durch anderweitige "
                   "Organschäden vorliegt (Beurteilungskriterium nach 7.4); Befunde "
                   "einholen, ggf. Maßnahmen nach 7.4.2 bzw. verkürzte Fristen nach 7.4.3."},
    {"wenn": {"chron_kopfschmerz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Chronischer Kopfschmerz",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Chronische Kopfschmerzen angegeben.",
     "konsequenz": "Chronischer Kopfschmerz ist Beurteilungskriterium nach 7.4: "
                   "unterscheiden, ob vorbestehend oder arbeitsbezogen (Salpetersäureester "
                   "verursachen typische Kopfschmerzen). Beurteilung nach 7.4; Maßnahmen "
                   "nach 7.4.2 bzw. verkürzte Vorsorgefristen nach 7.4.3 prüfen."},
    # ── Exposition und Schutzmaßnahmen ────────────────────────────────────
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitte 2, 6.2 und 8.1",
     "befund": "Direkter Hautkontakt mit Sprengöl bzw. benetzten Teilen möglich.",
     "konsequenz": "Hauptaufnahmeweg ist die Haut (Lebensgefahr bei Hautkontakt, H 310): "
                   "prüfen, ob Pflichtvorsorge-Voraussetzungen vorliegen. Abgleich mit der "
                   "Gefährdungsbeurteilung (TRGS 401); Beratung zu geeigneter PSA, "
                   "Hautschutz, Hygiene und Wechsel der Arbeitskleidung; ggf. dem "
                   "Unternehmen zusätzliche Schutzmaßnahmen vorschlagen."},
    {"wenn": {"psa_tragen": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzausrüstung",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA und zu den Gefahren der "
                   "Hautresorption; Ursachen der Nichtbenutzung klären. Ergeben sich "
                   "Anhaltspunkte, dass die Maßnahmen des Arbeitsschutzes nicht "
                   "ausreichen, Mitteilung an das Unternehmen mit Vorschlag von "
                   "Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"hygiene_umsetzung": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht durchgehend eingehalten.",
     "konsequenz": "Beratung zu Hygienemaßnahmen: Hände waschen vor Pausen, nicht am "
                   "Arbeitsplatz essen oder rauchen, regelmäßiger Wechsel der "
                   "Arbeitskleidung; Umsetzung bei der nächsten Vorsorge erneut erfragen."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese)",
     "befund": "Zwischenfälle, Unfälle oder ungewöhnliche Betriebszustände angegeben.",
     "konsequenz": "Hergang dokumentieren und mit der Gefährdungsbeurteilung abgleichen; "
                   "auf Beschwerden im zeitlichen Zusammenhang achten. Ggf. Mitteilung an "
                   "das Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"zusatzstoffe": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zusatzstoffe",
     "quelle": "Abschnitt 7.2.2",
     "befund": "Umgang mit weiteren Explosiv-/Zusatzstoffen (z. B. TNT) angegeben.",
     "konsequenz": "Auf die spezifische Giftwirkung der Zusatzstoffe achten (z. B. TNT); "
                   "prüfen, ob hierfür eigene Vorsorgeanlässe bestehen, und Untersuchungs- "
                   "umfang entsprechend erweitern."},
    {"wenn": {"stoffe": ["nitroglykol"]},
     "schwere": "hinweis",
     "bereich": "Inhalative Aufnahme",
     "quelle": "Abschnitte 6 und 6.2",
     "befund": "Umgang mit Glykoldinitrat (Nitroglykol) angegeben.",
     "konsequenz": "Glykoldinitrat ist deutlich flüchtiger als Glycerintrinitrat: auch den "
                   "inhalativen Aufnahmeweg berücksichtigen (Exposition selbst in "
                   "temperierten Lägern möglich). Beratung zum Vermeiden von Inhalation; "
                   "Einhaltung des Arbeitsplatzgrenzwerts (0,01 ml/m³, TRGS 900) mit der "
                   "Gefährdungsbeurteilung abgleichen."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 6.5 und 7.1",
     "befund": "Anerkannte Berufskrankheit bzw. laufendes BK-Verfahren angegeben.",
     "konsequenz": "Angaben dokumentieren und bei der Beurteilung berücksichtigen; für "
                   "Erkrankungen durch Salpetersäureester ist BK-Nr. 1309 einschlägig. "
                   "Befunde bzw. Bescheide einbeziehen."},
]
