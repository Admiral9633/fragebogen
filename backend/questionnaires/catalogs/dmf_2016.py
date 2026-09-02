# -*- coding: utf-8 -*-
"""G 19 Dimethylformamid – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 19 »Dimethylformamid«
(Fassung Oktober 2014), S. 311–320."""

SLUG = "g19-dmf-2016"

CATALOG = {
    "version": 2,
    "title": "G 19 Dimethylformamid (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 19 »Dimethylformamid« (Fassung Oktober 2014), S. 311–320",
    "sections": [
        # ── 1 ─ Untersuchungsanlass & Fristen (Abschnitt 1.1) ──────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "unt_art",
                    "type": "choice",
                    "label": "Welche Untersuchung steht bei Ihnen an?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt. "
                            "Die erste Nachuntersuchung folgt nach 6–12 Monaten, weitere "
                            "nach 12–24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich arbeite bereits mit DMF)"},
                    ],
                },
                {
                    "id": "letzte_unt",
                    "type": "choice",
                    "label": "Wann war Ihre letzte Untersuchung nach G 19?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "options": [
                        {"value": "unter12", "label": "Vor weniger als 12 Monaten"},
                        {"value": "12bis24", "label": "Vor 12 bis 24 Monaten"},
                        {"value": "ueber24", "label": "Vor mehr als 24 Monaten"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Waren Sie seit der letzten Untersuchung schwer oder länger "
                             "krank (z. B. Krankenhausaufenthalt, mehrwöchige "
                             "Arbeitsunfähigkeit)?",
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
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition (Abschnitt 3.1) ───────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kontakt mit DMF",
            "subtitle": "Ihre Arbeit und Ihr Umgang mit Dimethylformamid",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus oder sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "arbeitsbereiche",
                    "type": "multi_choice",
                    "label": "In welchen dieser Bereiche arbeiten Sie oder werden Sie arbeiten?",
                    "hint": "In diesen Bereichen ist mit einer DMF-Belastung zu rechnen. "
                            "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "kunstleder", "label": "Kunstlederproduktion"},
                        {"value": "chemiefaser", "label": "Herstellung von Chemiefasern (Polyacrylnitril)"},
                        {"value": "pharma_chemie", "label": "Feinchemie, Pharma- oder Kosmetikproduktion"},
                        {"value": "kunststoff", "label": "Kunststoffbeschichtung (Polyurethan)"},
                        {"value": "schwefel_paraffin", "label": "Schwefel-Extraktion aus Gestein oder Reinigen von Rohparaffin"},
                        {"value": "reinigung_reparatur", "label": "Reinigungs- oder Reparaturarbeiten an Anlagen"},
                        {"value": "abbruch_sanierung", "label": "Abbruch-, Sanierungs- oder Instandsetzungsarbeiten "
                                                               "in Produktions- oder Abfüllanlagen"},
                        {"value": "kontaminiert", "label": "Arbeiten in verunreinigten (kontaminierten) Bereichen"},
                        {"value": "andere", "label": "Anderer Bereich mit DMF-Kontakt"},
                        {"value": "keine_davon", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt mit Dimethylformamid?",
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
                    "label": "Kommt Ihre Haut bei der Arbeit direkt mit flüssigem DMF in "
                             "Berührung (z. B. Spritzer, durchfeuchtete Handschuhe oder "
                             "Kleidung)?",
                    "hint": "DMF dringt sehr schnell durch die Haut ein: Schon 10 Minuten "
                            "Hautkontakt einer Hand entsprechen der Menge, die man bei "
                            "8 Stunden Arbeit über die Atemluft aufnehmen kann.",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                },
                {
                    "id": "frueher_dmf",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit Dimethylformamid "
                             "oder anderen Lösungsmitteln?",
                    "required": True,
                    "followup": {"id": "frueher_dmf_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, und wie lange?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen (Abschnitt 2.2) ────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Persönliche Schutzausrüstung und Verhalten am Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_handschuhe",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit möglichem DMF-Kontakt "
                             "Schutzhandschuhe?",
                    "hint": "Bei reinem DMF ist Butylkautschuk das geeignete "
                            "Handschuhmaterial.",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_kontakt", "label": "Bei meiner Arbeit gibt es keinen möglichen Hautkontakt"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme mit Ihrer Schutzausrüstung (z. B. undichte "
                             "oder beschädigte Handschuhe, Hautprobleme unter den "
                             "Handschuhen)?",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
                {
                    "id": "hygiene",
                    "type": "choice",
                    "label": "Halten Sie die Hygieneregeln am Arbeitsplatz ein (Hände waschen "
                             "vor Pausen, verschmutzte Arbeitskleidung wechseln)?",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "teilweise", "label": "Teilweise"},
                        {"value": "nein", "label": "Eher nicht"},
                    ],
                },
            ],
        },
        # ── 4 ─ Beschwerden – Zwischenanamnese (Abschnitt 1.2.1) ───────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden seit Beginn der Tätigkeit bzw. seit der letzten "
                        "Untersuchung – das wichtigste Zielorgan von DMF ist die Leber",
            "questions": [
                {
                    "id": "kopfschmerz",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Kopfschmerzen?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                },
                {
                    "id": "appetit_uebelkeit",
                    "type": "yes_no",
                    "label": "Leiden Sie unter Appetitlosigkeit, Übelkeit oder Erbrechen?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                },
                {
                    "id": "oberbauch_druck",
                    "type": "yes_no",
                    "label": "Haben Sie ein Druckgefühl im Oberbauch oder kolikartige "
                             "(krampfartige) Bauchschmerzen?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                },
                {
                    "id": "verdauung",
                    "type": "yes_no",
                    "label": "Haben Sie Verdauungsstörungen (Durchfall oder Verstopfung)?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                },
                {
                    "id": "gewichtsverlust",
                    "type": "yes_no",
                    "label": "Haben Sie in letzter Zeit ungewollt an Gewicht verloren?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                },
                {
                    "id": "flush_alkohol",
                    "type": "yes_no",
                    "label": "Vertragen Sie Alkohol schlechter als früher – z. B. "
                             "Gesichtsrötung, Schwindel, Übelkeit oder Engegefühl in der "
                             "Brust schon nach kleinen Mengen (»Flush«)?",
                    "hint": "Eine solche Alkoholunverträglichkeit kann bis zu 4 Tage nach "
                            "einer DMF-Belastung auftreten und ist ein deutliches Zeichen "
                            "dafür, dass DMF in den Körper aufgenommen wurde.",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen und Lebensweise (Abschnitte 2.1, 3.2) ──────
        {
            "id": "gesundheit",
            "title": "Vorerkrankungen & Lebensweise",
            "subtitle": "Erkrankungen und Gewohnheiten, die für DMF wichtig sind",
            "questions": [
                {
                    "id": "lebererkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine chronische Lebererkrankung (z. B. Fettleber, "
                             "chronische Hepatitis, Leberzirrhose)?",
                    "required": True,
                    "followup": {"id": "lebererkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "leber_frueher",
                    "type": "yes_no",
                    "label": "Hatten Sie früher eine Lebererkrankung, von der Sie inzwischen "
                             "wieder genesen sind (z. B. ausgeheilte Hepatitis)?",
                    "required": True,
                    "show_if": {"id": "lebererkrankung", "in": ["no"]},
                    "followup": {"id": "leber_frueher_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "leberwerte",
                    "type": "yes_no",
                    "label": "Wurden bei Ihnen schon einmal erhöhte Leberwerte festgestellt?",
                    "required": True,
                },
                {
                    "id": "abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Drogen (Rauschmitteln) oder Medikamenten?",
                    "required": True,
                },
                {
                    "id": "alkohol_konsum",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "DMF und Alkohol verstärken sich gegenseitig in ihrer Wirkung "
                            "auf die Leber – deshalb ist diese Frage hier wichtig.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "gelegentlich", "label": "Gelegentlich (z. B. zu besonderen Anlässen)"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche)"},
                    ],
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "hint": "Bestimmte Medikamente hemmen den Alkohol-Abbau im Körper "
                            "(Aldehyddehydrogenase) und können das Risiko einer "
                            "Leberschädigung durch DMF erhöhen.",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "text",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Sind Sie derzeit schwanger, oder könnte eine Schwangerschaft "
                             "bestehen?",
                    "hint": "DMF ist als fruchtschädigend für den Menschen eingestuft.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "moeglich", "label": "Unsicher / wäre möglich"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "nicht_zutreffend", "label": "Trifft auf mich nicht zu"},
                    ],
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
    # ── Bedenkenstatbestände (Abschnitt 2.1) ──────────────────────────────
    {"wenn": {"lebererkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Leber",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Chronische Lebererkrankung angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken (2.1.1): Befunde und "
                   "Ausprägung ärztlich klären (γ-GT, ALAT, ASAT; in unklaren Fällen "
                   "Oberbauch-Sonographie). Nur bei weniger ausgeprägter Erkrankung »keine "
                   "Bedenken unter bestimmten Voraussetzungen« (2.1.3) prüfen: technische/"
                   "organisatorische Schutzmaßnahmen, Arbeitsplatz mit geringerer Exposition, "
                   "PSA, verkürzte Nachuntersuchungsfristen. Andernfalls Bedenken gegen "
                   "Aufnahme bzw. Fortsetzung der Tätigkeit aussprechen."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Abhängigkeitserkrankung",
     "quelle": "Abschnitte 2.1.1 und 2.1.2",
     "befund": "Alkohol-, Rauschmittel- oder Medikamentenabhängigkeit angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken (2.1.1); bei zu "
                   "erwartender Wiederherstellung befristete Bedenken (2.1.2). Ausprägung "
                   "und Behandlungsstand ärztlich klären, Leberwerte kontrollieren; "
                   "Beratung zu Behandlungsangeboten."},
    {"wenn": {"leber_frueher": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitt 2.1.2 (Befristete gesundheitliche Bedenken)",
     "befund": "Frühere, inzwischen ausgeheilte Lebererkrankung angegeben.",
     "konsequenz": "Je nach Schwere der vorausgegangenen Leberfunktionsstörung mehrmonatige "
                   "DMF-Karenz erwägen; Weiterbeschäftigung erst nach Ablauf dieser Frist "
                   "und erneuter ärztlicher Untersuchung. Ggf. Maßnahmen nach § 3 BKV in "
                   "Erwägung ziehen."},
    {"wenn": {"leberwerte": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 1.2.2 und 1.2.3",
     "befund": "Früher erhöhte Leberwerte angegeben.",
     "konsequenz": "Spezielle Untersuchung besonders beachten: γ-GT, SGPT (ALAT), SGOT "
                   "(ASAT) bestimmen und mit Vorbefunden vergleichen; in unklaren Fällen "
                   "Ergänzungsuntersuchung (weitere Leberdiagnostik, z. B. "
                   "Oberbauch-Sonographie)."},
    # ── Zwischenanamnese-Symptome (Abschnitte 1.2.1, 3.2) ─────────────────
    {"wenn": {"flush_alkohol": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Alkoholunverträglichkeit",
     "quelle": "Abschnitte 1.2.1, 3.1.4 und 3.2.1",
     "befund": "Alkoholunverträglichkeit (Flush-Syndrom) angegeben – deutliches Indiz "
               "für eine DMF-Aufnahme.",
     "konsequenz": "Biomonitoring durchführen (N-Methylformamid plus N-Hydroxymethyl-N-"
                   "methylformamid im Urin, BGW 35 mg/l, Probennahme zum Expositions-/"
                   "Schichtende) und Leberwerte bestimmen. Expositionssituation prüfen; "
                   "bei Hinweisen auf unzureichenden Arbeitsschutz Mitteilung an den "
                   "Arbeitgeber zur Aktualisierung der Gefährdungsbeurteilung (unter "
                   "Wahrung der schutzwürdigen Belange)."},
    {"wenn": {"oberbauch_druck": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 1.2.1, 1.2.3 und 3.2.1",
     "befund": "Druckgefühl im Oberbauch bzw. kolikartige Leibschmerzen angegeben.",
     "konsequenz": "Mögliches Leitsymptom einer Leberzellschädigung: Leberwerte (γ-GT, "
                   "ALAT, ASAT) und Biomonitoring durchführen; in unklaren Fällen "
                   "Ergänzungsuntersuchung (Oberbauch-Sonographie); vorzeitige "
                   "Nachuntersuchung nach ärztlichem Ermessen festlegen."},
    {"wenn": {"appetit_uebelkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber/Magen-Darm",
     "quelle": "Abschnitte 1.2.1 und 3.2.2",
     "befund": "Appetitlosigkeit, Übelkeit oder Erbrechen angegeben.",
     "konsequenz": "Symptom der Zwischenanamnese ärztlich vertiefen (zeitlicher Bezug zur "
                   "Arbeit): Leberwerte und Biomonitoring durchführen; bei unklarem Befund "
                   "Ergänzungsuntersuchung veranlassen."},
    {"wenn": {"verdauung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm",
     "quelle": "Abschnitte 1.2.1 und 3.2.2",
     "befund": "Verdauungsstörungen (Durchfall oder Verstopfung) angegeben.",
     "konsequenz": "Im Rahmen der speziellen Untersuchung abklären (Leberwerte, "
                   "Biomonitoring); differenzialdiagnostisch auch an Pankreatitis und "
                   "andere Ursachen denken."},
    {"wenn": {"gewichtsverlust": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allgemeinsymptome",
     "quelle": "Abschnitte 1.2.1 und 3.2.2",
     "befund": "Ungewollter Gewichtsverlust angegeben.",
     "konsequenz": "Abklärung veranlassen: Leberwerte, Biomonitoring, in unklaren Fällen "
                   "Oberbauch-Sonographie; bei fortbestehender Unklarheit fachärztliche "
                   "Abklärung empfehlen."},
    {"wenn": {"kopfschmerz": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 1.2.1 und 3.2.2",
     "befund": "Häufige Kopfschmerzen angegeben.",
     "konsequenz": "Zeitlichen Zusammenhang mit der DMF-Exposition erfragen (ZNS-Wirkung "
                   "möglich); bei Arbeitsplatzbezug Expositionssituation prüfen und "
                   "Biomonitoring beachten."},
    # ── Fristen und vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Fristen",
     "quelle": "Abschnitt 1.1 (Vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt: prüfen, ob die Erkrankung "
                   "Anlass zu Bedenken gegen eine Fortsetzung der Tätigkeit geben könnte; "
                   "Befunde und Entlassberichte einbeziehen."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Fristen",
     "quelle": "Abschnitt 1.1 (Vorzeitige Nachuntersuchung)",
     "befund": "Die Person vermutet einen Zusammenhang zwischen Erkrankung und Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen; Beschwerden dokumentieren, "
                   "Leberdiagnostik und Biomonitoring veranlassen. Bei begründetem Verdacht "
                   "auf eine Lebererkrankung durch DMF an die Berufskrankheit Nr. 1316 "
                   "denken (BK-Anzeige prüfen)."},
    {"wenn": {"letzte_unt": ["ueber24"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungsfristen)",
     "befund": "Letzte G-19-Untersuchung liegt mehr als 24 Monate zurück.",
     "konsequenz": "Nachuntersuchungsfrist überschritten (erste Nachuntersuchung nach "
                   "6–12, weitere nach 12–24 Monaten): Untersuchung jetzt vollständig "
                   "durchführen und den nächsten Termin fristgerecht festlegen."},
    # ── Exposition und Schutzmaßnahmen (Abschnitte 2.2, 3.1) ──────────────
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautresorption",
     "quelle": "Abschnitte 3.1.3, 3.1.4 und 2.2",
     "befund": "Direkter Hautkontakt mit flüssigem DMF angegeben.",
     "konsequenz": "Wegen sehr guter Hautresorption ist das Biomonitoring von maßgeblicher "
                   "Bedeutung (TRGS 401): NMF im Urin bestimmen. Beratung zu PSA mit "
                   "geeignetem Handschuhmaterial (bei reinem DMF: Butylkautschuk) und "
                   "Hygienemaßnahmen."},
    {"wenn": {"psa_handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Schutzhandschuhe werden bei möglichem DMF-Kontakt selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zu PSA: Wegen der hautresorptiven Eigenschaften hat "
                   "das Tragen von Schutzausrüstung inklusive geeigneter Handschuhe "
                   "(Butylkautschuk bei reinem DMF) besondere Bedeutung. Ergibt sich Bedarf "
                   "zur Verbesserung des Arbeitsschutzes, Mitteilung an den Arbeitgeber "
                   "(Aktualisierung der Gefährdungsbeurteilung)."},
    {"wenn": {"hygiene": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Hygieneregeln werden nicht durchgehend eingehalten.",
     "konsequenz": "Auf allgemeine Hygienemaßnahmen hinweisen: Hautkontakt vermeiden, "
                   "Händewaschen vor Pausen, Wechsel verschmutzter Arbeitskleidung."},
    # ── Beratung (Abschnitte 2.2, 3.2) ────────────────────────────────────
    {"wenn": {"medikamente": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Medikamente",
     "quelle": "Abschnitte 2.2 und 3.2.2",
     "befund": "Regelmäßige Medikamenteneinnahme angegeben.",
     "konsequenz": "Medikamentenanamnese ärztlich prüfen: Medikamente mit "
                   "Aldehyddehydrogenase-Hemmung erhöhen das Risiko einer Leberschädigung "
                   "durch DMF. Ggf. Leberwerte engmaschiger kontrollieren und verkürzte "
                   "Nachuntersuchungsfristen festlegen."},
    {"wenn": {"alkohol_konsum": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 2.2 und 3.2.1",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Auf den synergistischen Effekt zwischen DMF und Alkohol sowie mögliche "
                   "Alkoholunverträglichkeiten hinweisen; Alkohol erhöht das Risiko einer "
                   "Leberschädigung durch DMF – Leberwerte besonders beachten."},
    {"wenn": {"schwangerschaft": ["ja", "moeglich"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 2.2 und 3.2.2 (fruchtschädigendes Potenzial)",
     "befund": "Schwangerschaft besteht oder ist möglich.",
     "konsequenz": "DMF ist als fruchtschädigend für den Menschen eingestuft: Exposition "
                   "Schwangerer vermeiden. Vor (weiterer) Tätigkeit mit DMF klären, "
                   "unverzüglich zum Mutterschutz beraten; bei unklarer Schwangerschaft "
                   "Klärung vor Fortsetzung der Tätigkeit empfehlen."},
    {"wenn": {"frueher_dmf": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 1.2.1 (Arbeitsanamnese) und 4",
     "befund": "Frühere Tätigkeit mit DMF- oder Lösungsmittel-Exposition angegeben.",
     "konsequenz": "Frühere Exposition in Arbeitsanamnese und Beurteilung einbeziehen; bei "
                   "Lebererkrankung mit möglichem Tätigkeitsbezug an die Berufskrankheit "
                   "Nr. 1316 (Erkrankungen der Leber durch DMF) denken."},
]
