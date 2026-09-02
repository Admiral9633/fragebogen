# -*- coding: utf-8 -*-
"""Vinylchlorid – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische
Beratungen und Untersuchungen, 1. Auflage 2024, »Vinylchlorid« (E VNC, Fassung Januar 2022,
Grenzwerte aktualisiert 2024), S. 738–755."""

SLUG = "vinylchlorid-2024"

CATALOG = {
    "version": 2,
    "title": "Vinylchlorid (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Vinylchlorid« (E VNC, Fassung Januar 2022, Grenzwerte "
             "aktualisiert 2024), S. 738–755",
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
                    "label": "Um welche Vorsorge handelt es sich heute?",
                    "hint": "Nachgehende Vorsorge: Vinylchlorid ist krebserzeugend, deshalb wird "
                            "Ihnen auch nach dem Ende der Tätigkeit weiter Vorsorge angeboten.",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge wegen Vinylchlorid"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich war schon einmal zur Vinylchlorid-Vorsorge)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (die Tätigkeit mit Vinylchlorid ist beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert nicht eingehalten wird oder eine wiederholte "
                            "Belastung nicht ausgeschlossen werden kann. Angebotsvorsorge: Ihr "
                            "Betrieb muss sie anbieten. Wunschvorsorge: auf Ihren eigenen Wunsch.",
                    "required": True,
                    "options": [
                        {"value": "pflicht", "label": "Vom Betrieb verpflichtend veranlasst (Pflichtvorsorge)"},
                        {"value": "angebot", "label": "Vom Betrieb angeboten (Angebots- oder nachgehende Vorsorge)"},
                        {"value": "wunsch", "label": "Auf meinen eigenen Wunsch (Wunschvorsorge)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
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
                        {"value": "vc_herstellung", "label": "Herstellung, Umfüllen oder Rückgewinnung von Vinylchlorid"},
                        {"value": "pvc_herstellung", "label": "Herstellung von PVC (Polyvinylchlorid), z. B. an Reaktionsbehältern"},
                        {"value": "pvc_verarbeitung", "label": "PVC-Weiterverarbeitung, Absackanlagen oder Lagerung/Transport von Roh-PVC"},
                        {"value": "heissverfahren", "label": "Be- und Verarbeitung von PVC mit Hitze (z. B. Kunststoffschweißen)"},
                        {"value": "transport", "label": "Transport von Vinylchlorid mit Tankschiff oder Eisenbahnkesselwagen"},
                        {"value": "deponie", "label": "Arbeiten auf Mülldeponien mit Kontakt zu Deponiegasen"},
                        {"value": "geschlossen", "label": "Nur geschlossene Anlagen, Labor oder fertige PVC-Produkte"},
                        {"value": "sonstiges", "label": "Anderer Bereich"},
                    ],
                },
                {
                    "id": "wartung_reinigung",
                    "type": "yes_no",
                    "label": "Führen Sie Wartungs-, Instandhaltungs- oder manuelle Reinigungsarbeiten "
                             "an Anlagenteilen durch, in denen Vinylchlorid enthalten sein kann "
                             "(z. B. Behälter, Rohrleitungen, Entgasungsanlagen, Störungsbeseitigung)?",
                    "required": True,
                },
                {
                    "id": "dichlorethan",
                    "type": "yes_no",
                    "label": "Haben Sie bei Ihrer Arbeit auch Kontakt mit 1,2-Dichlorethan "
                             "(z. B. in der Vinylchlorid-Herstellung)?",
                    "hint": "Wichtig für die Bewertung der Urinuntersuchung (Biomonitoring): "
                            "beide Stoffe werden im Körper zum selben Abbauprodukt umgewandelt.",
                    "required": True,
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
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es an Ihrem Arbeitsplatz Zwischenfälle, Unfälle oder ungewöhnliche "
                             "Betriebszustände mit möglicher erhöhter Vinylchlorid-Belastung "
                             "(z. B. Leckagen, Störungen)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Läuft bei Ihnen derzeit ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
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
                {
                    "id": "kleidung_wechsel",
                    "type": "yes_no",
                    "label": "Wird verunreinigte Arbeitskleidung bei Ihnen regelmäßig gewechselt "
                             "und fachgerecht gereinigt?",
                    "hint": "Aus verunreinigter Kleidung kann Vinylchlorid wieder ausgasen und "
                            "eingeatmet werden.",
                    "required": True,
                    "show_if": {"id": "psa_tragen", "not_in": ["keine_noetig"]},
                },
                {
                    "id": "essen_am_arbeitsplatz",
                    "type": "yes_no",
                    "label": "Essen oder trinken Sie am Arbeitsplatz?",
                    "required": True,
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
                    "hint": "Vinylchlorid kann in seltenen Fällen sklerodermieartige "
                            "(bindegewebsverhärtende) Hautveränderungen verursachen.",
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
        # ── 5 ─ Vorerkrankungen und Lebensweise ────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Lebensweise",
            "subtitle": "Erkrankungen und Angaben, die für die Beurteilung wichtig sind",
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
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein, nie geraucht"},
                        {"value": "frueher", "label": "Früher geraucht, jetzt nicht mehr"},
                        {"value": "ja", "label": "Ja"},
                    ],
                },
            ],
        },
        # ── 6 ─ Besondere Schutzgruppen ────────────────────────────────────
        {
            "id": "schutzgruppen",
            "title": "Besonderer Schutz",
            "subtitle": "Gesetzliche Beschäftigungsbeschränkungen",
            "questions": [
                {
                    "id": "unter_18",
                    "type": "yes_no",
                    "label": "Sind Sie unter 18 Jahre alt?",
                    "required": True,
                },
                {
                    "id": "schwanger",
                    "type": "choice",
                    "label": "Sind Sie schwanger, oder stillen Sie derzeit?",
                    "hint": "Für werdende und stillende Mütter gelten bei krebserzeugenden "
                            "Stoffen besondere Schutzvorschriften (Mutterschutzgesetz).",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "keine_angabe", "label": "Trifft nicht zu / keine Angabe"},
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
    # ── Zielorgan Leber (Abschnitte 6.3, 7.2.2, 7.4) ──────────────────────
    {"wenn": {"leber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 7.2.2 und 7.4 (Beurteilungskriterien)",
     "befund": "In den letzten 2 Jahren durchgemachte oder bestehende Lebererkrankung angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach Abschnitt 7.4: Leberenzyme (SGOT, SGPT, "
                   "γ-GT), alkalische Phosphatase und Blutbild gezielt bewerten; ergänzend weitere "
                   "Leberdiagnostik und Oberbauchsonographie mit besonderer Darstellung der Leber "
                   "veranlassen. Maßnahmen nach 7.4.2 (z. B. Expositionsbegrenzung, Einsatz an "
                   "Arbeitsplätzen mit geringerer Exposition) und verkürzte Vorsorgefristen nach "
                   "7.4.3 prüfen; ohne Aussicht auf Erfolg Tätigkeitswechsel nach 7.4.4 erwägen "
                   "(Mitteilung an den Arbeitgeber nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"oberbauch": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 7.2.2",
     "befund": "Oberbauchbeschwerden angegeben (stoffspezifisches Leitsymptom).",
     "konsequenz": "Gezielte Abklärung der Leber: Leberwerte bewerten, ergänzend weitere "
                   "Leberdiagnostik und Oberbauchsonographie mit Darstellung der Leber erwägen; "
                   "Beratung zur hepatotoxischen Wirkung von Vinylchlorid (Abschnitt 8.1)."},
    {"wenn": {"appetit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 7.2.2",
     "befund": "Appetitlosigkeit bzw. Abneigung gegen Fett angegeben (stoffspezifisches Leitsymptom).",
     "konsequenz": "Gezielte Leberdiagnostik wie bei Oberbauchbeschwerden: Leberwerte bewerten, "
                   "ggf. weitere Leberdiagnostik und Oberbauchsonographie veranlassen."},
    # ── Gefäße, Haut, Knochen (VC-Krankheit) ──────────────────────────────
    {"wenn": {"finger_missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Finger/Knochen",
     "quelle": "Abschnitte 6.3.3, 7.1 (Beschwerden) und 7.4",
     "befund": "Missempfindungen in den Fingern angegeben (mögliches Frühzeichen der VC-Krankheit).",
     "konsequenz": "Abklärung auf Durchblutungsstörungen und Akroosteolyse (Knochenabbau der "
                   "Fingerendglieder): gezielte klinische Untersuchung, ggf. fachärztliche "
                   "Diagnostik veranlassen; Beurteilung nach Abschnitt 7.4, ggf. Maßnahmen nach "
                   "7.4.2 und verkürzte Fristen nach 7.4.3."},
    {"wenn": {"finger_kalt_weiss": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gefäßsystem",
     "quelle": "Abschnitte 6.3.3 und 7.4",
     "befund": "Anfallsartig weiße, kalte oder schmerzhafte Finger (Hinweis auf Raynaud-Syndrom).",
     "konsequenz": "Gefäßveränderungen (insbesondere Raynaud-Syndrom) sind beurteilungsrelevant "
                   "nach Abschnitt 7.4: angiologische Abklärung veranlassen; Maßnahmen nach 7.4.2 "
                   "und verkürzte Vorsorgefristen nach 7.4.3 prüfen."},
    {"wenn": {"hautveraenderungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3.3 und 7.4",
     "befund": "Verhärtungen/Verdickungen der Haut angegeben (Verdacht auf sklerodermieartige "
               "Hautveränderungen).",
     "konsequenz": "Dermatologische Abklärung veranlassen; sklerodermieartige Hauterkrankungen "
                   "sind beurteilungsrelevant nach Abschnitt 7.4 – Maßnahmen nach 7.4.2 bzw. "
                   "verkürzte Fristen nach 7.4.3 prüfen."},
    {"wenn": {"schwindel": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Wirkung",
     "quelle": "Abschnitte 6.3.2, 7.1 (Beschwerden) und 8.2",
     "befund": "Schwindelgefühl/Benommenheit bei oder nach der Arbeit angegeben.",
     "konsequenz": "Mögliche akute (pränarkotische) Wirkung von Vinylchlorid abklären: aktuelle "
                   "Expositionssituation mit der Gefährdungsbeurteilung abgleichen; ergeben sich "
                   "Anhaltspunkte für unzureichende Schutzmaßnahmen, Mitteilung an das Unternehmen "
                   "und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    # ── Weitere beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────
    {"wenn": {"blutkrankheit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Blut",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Systemische Blutkrankheit angegeben.",
     "konsequenz": "Großes Blutbild mit Thrombozyten gezielt bewerten, Vorbefunde einholen; "
                   "Beurteilung nach Abschnitt 7.4, ggf. Maßnahmen nach 7.4.2 und verkürzte "
                   "Vorsorgefristen nach 7.4.3."},
    {"wenn": {"nerven": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Erkrankung des zentralen oder peripheren Nervensystems angegeben.",
     "konsequenz": "Störungen des zentralen und peripheren Nervensystems sind beurteilungsrelevant: "
                   "Ausmaß ärztlich klären (ggf. neurologische Vorbefunde), Maßnahmen nach 7.4.2 "
                   "und verkürzte Fristen nach 7.4.3 prüfen."},
    {"wenn": {"atemfunktion": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Erheblich eingeschränkte Atemfunktion angegeben.",
     "konsequenz": "Ausmaß der Einschränkung klären (Vinylchlorid wird überwiegend eingeatmet, "
                   "ggf. Atemschutz erforderlich); Beurteilung nach Abschnitt 7.4, Maßnahmen nach "
                   "7.4.2 – insbesondere PSA unter Beachtung des individuellen Gesundheitszustandes."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Suchtmittel",
     "quelle": "Abschnitte 7.1 und 7.4 (Beurteilungskriterien)",
     "befund": "Missbrauch oder Abhängigkeit von Alkohol, Medikamenten oder Drogen angegeben.",
     "konsequenz": "Beurteilungsrelevant nach Abschnitt 7.4 (zusätzliche Leberbelastung): "
                   "Leberdiagnostik gezielt bewerten, Beratung; Maßnahmen nach 7.4.2 und verkürzte "
                   "Vorsorgefristen nach 7.4.3 prüfen."},
    # ── Exposition und Biomonitoring ──────────────────────────────────────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese) und § 6 (4) ArbMedVV",
     "befund": "Zwischenfälle, Unfälle oder ungewöhnliche Betriebszustände mit möglicher erhöhter "
               "Exposition angegeben.",
     "konsequenz": "Ereignis dokumentieren und mit der Gefährdungsbeurteilung abgleichen; "
                   "Biomonitoring (Thiodiglykolsäure im Urin) zur Expositionsabschätzung erwägen. "
                   "Bei Anhaltspunkten für unzureichende Schutzmaßnahmen Mitteilung an das "
                   "Unternehmen und Vorschlag von Maßnahmen."},
    {"wenn": {"wartung_reinigung": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Exposition",
     "quelle": "Abschnitte 6.1.1 und 7.1 (Arbeitsanamnese)",
     "befund": "Wartungs-, Instandhaltungs- oder manuelle Reinigungsarbeiten an Vinylchlorid "
               "führenden Anlagenteilen angegeben (Tätigkeit mit höherer Exposition).",
     "konsequenz": "Umfang der Arbeiten dokumentieren und mit der Gefährdungsbeurteilung "
                   "abgleichen; Biomonitoring-Ergebnisse (TDGA im Urin, BAR 1,5 mg/l) besonders "
                   "beachten; intensive Beratung zu PSA, Inhalations- und Hautkontaktvermeidung."},
    {"wenn": {"dichlorethan": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 6.4 (Biomonitoring)",
     "befund": "Mischexposition mit 1,2-Dichlorethan angegeben.",
     "konsequenz": "1,2-Dichlorethan wird ebenfalls zu Thiodiglykolsäure (TDGA) abgebaut: den "
                   "Rückschluss von der TDGA-Ausscheidung im Urin auf die Vinylchlorid-Konzentration "
                   "am Arbeitsplatz kritisch vornehmen, insbesondere bei niedriger Luftbelastung."},
    # ── Schutzmaßnahmen und Hygiene ───────────────────────────────────────
    {"wenn": {"psa_tragen": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA und zur krebserzeugenden Wirkung "
                   "von Vinylchlorid; Ursachen klären. Ergeben sich Anhaltspunkte, dass die "
                   "Maßnahmen des Arbeitsschutzes nicht ausreichen, Mitteilung an das Unternehmen "
                   "und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"kleidung_wechsel": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 8.2 (Hinweis)",
     "befund": "Verunreinigte Arbeitskleidung wird nicht regelmäßig gewechselt/fachgerecht gereinigt.",
     "konsequenz": "Auf konsequenten Austausch und fachgerechte Reinigung verunreinigter "
                   "Arbeitskleidung hinwirken – sie kann durch Ausgasung und nachfolgende "
                   "Einatmung eine permanente Expositionsquelle darstellen; Unternehmen beraten."},
    {"wenn": {"rauchen": ["ja"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 7.1 (Anamnese und allgemeine Beratung)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung: gründliches Händewaschen besonders auch vor Raucherpausen, um eine "
                   "zusätzliche Stoffaufnahme zu vermeiden; allgemeine Beratung zum Rauchverhalten."},
    # ── Besondere Schutzgruppen und nachgehende Vorsorge ──────────────────
    {"wenn": {"schwanger": ["ja"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 7.1 (Beschäftigungsbeschränkungen, MuSchG)",
     "befund": "Schwangerschaft oder Stillzeit bei Tätigkeit mit einem krebserzeugenden Stoff "
               "(Kategorie 1A) angegeben.",
     "konsequenz": "Beschäftigungsbeschränkungen nach dem Mutterschutzgesetz vor (weiterer) "
                   "Ausübung der Tätigkeit klären: keine Tätigkeit mit Exposition gegenüber "
                   "Vinylchlorid für werdende/stillende Mütter; unverzügliche Information und "
                   "Umgestaltung/Umsetzung über das Unternehmen veranlassen."},
    {"wenn": {"unter_18": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Jugendarbeitsschutz",
     "quelle": "Abschnitt 7.1 (Beschäftigungsbeschränkungen, JArbSchG)",
     "befund": "Person ist unter 18 Jahre alt.",
     "konsequenz": "Beschäftigungsbeschränkungen für Jugendliche nach dem Jugendarbeitsschutzgesetz "
                   "prüfen (Tätigkeiten mit krebserzeugenden Gefahrstoffen); Klärung mit dem "
                   "Unternehmen vor Aufnahme bzw. Fortsetzung der Tätigkeit."},
    {"wenn": {"vorsorge_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitt 2 (Angebotsvorsorge/nachgehende Vorsorge) und 8.1",
     "befund": "Nachgehende Vorsorge nach Ende der Tätigkeit mit Vinylchlorid.",
     "konsequenz": "Untersuchungsumfang wie Nachuntersuchung (Urinstatus, großes Blutbild, "
                   "Leberenzyme, alkalische Phosphatase, ggf. weitere Leberdiagnostik/"
                   "Oberbauchsonographie); über die Fortführung der nachgehenden Vorsorge beraten "
                   "und Anmeldung über das Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de) "
                   "sicherstellen."},
]
