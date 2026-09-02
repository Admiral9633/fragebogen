# -*- coding: utf-8 -*-
"""G 14 Trichlorethen (Trichlorethylen) und andere Chlorkohlenwasserstoff-
Lösungsmittel – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 14 (Fassung
Oktober 2014), S. 251–266."""

SLUG = "g14-ckw-2016"

CATALOG = {
    "version": 2,
    "title": "G 14 Trichlorethen und andere Chlorkohlenwasserstoff-Lösungsmittel "
             "(DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 14 »Trichlorethen (Trichlorethylen) und andere Chlorkohlenwasserstoff-"
             "Lösungsmittel« (Fassung Oktober 2014), S. 251–266",
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
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. "
                            "Nachuntersuchung: in der Regel nach 12–24 Monaten. "
                            "Nachgehende Untersuchung: nach dem Ende der Tätigkeit "
                            "mit Trichlorethen.",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nachuntersuchung", "label": "Nachuntersuchung (Tätigkeit läuft bereits)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (Tätigkeit beendet)"},
                    ],
                },
                {
                    "id": "vorzeitig_anlass",
                    "type": "multi_choice",
                    "label": "Trifft eine der folgenden Aussagen auf Sie zu?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nachuntersuchung"]},
                    "options": [
                        {"value": "keine", "label": "Nein, keine davon"},
                        {"value": "schwere_erkrankung", "label": "Ich war seit der letzten Untersuchung "
                                                                 "schwer oder längere Zeit krank"},
                        {"value": "zusammenhang", "label": "Ich vermute, dass Beschwerden oder eine "
                                                           "Erkrankung mit meiner Arbeit zusammenhängen"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Umgang mit den Lösungsmitteln",
            "subtitle": "Ihre Arbeit und der Kontakt zu den Stoffen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "stoffe",
                    "type": "multi_choice",
                    "label": "Mit welchen der folgenden Lösungsmittel haben Sie bei der "
                             "Arbeit zu tun?",
                    "hint": "Mehrfachauswahl möglich. Die Namen stehen im "
                            "Sicherheitsdatenblatt oder auf dem Gebinde.",
                    "required": True,
                    "options": [
                        {"value": "trichlorethen", "label": "Trichlorethen (Trichlorethylen, »Tri«)"},
                        {"value": "tetrachlorethen", "label": "Tetrachlorethen (Perchlorethylen, »Per«)"},
                        {"value": "dichlormethan", "label": "Dichlormethan (Methylenchlorid)"},
                        {"value": "andere_ckw", "label": "Andere Chlorkohlenwasserstoff-Lösungsmittel "
                                                         "(z. B. Tetrachlormethan, Tetrachlorethan)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "arbeitsbereiche",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten kommen Sie mit den Lösungsmitteln in "
                             "Berührung?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "herstellen_abfuellen", "label": "Herstellen oder Abfüllen"},
                        {"value": "aufarbeiten", "label": "Aufarbeiten / Lösungsmittel-Recycling"},
                        {"value": "reinigen_entfetten", "label": "Reinigen und Entfetten von Teilen"},
                        {"value": "oberflaeche_kleben", "label": "Oberflächenbeschichtung, Kleben, "
                                                                 "Farbspritzen oder Formenschäumen"},
                        {"value": "abbeizen", "label": "Farb-/Lackentferner (Abbeizer) oder Rostschutzmittel"},
                        {"value": "extraktion", "label": "Lösungsmittel für Öle, Fette, Wachse oder Harze "
                                                         "(auch Extraktion)"},
                        {"value": "labor", "label": "Labor (z. B. Straßenbau-, Asphalt- oder Baustofflabor)"},
                        {"value": "vulkanisieren_stein", "label": "Vulkanisieren (Gummilösung) oder Steinbearbeitung"},
                        {"value": "abbruch_sanierung", "label": "Abbruch-, Sanierungs- oder Instandsetzungsarbeiten "
                                                                "in Produktions-/Abfüllanlagen"},
                        {"value": "kontaminiert", "label": "Arbeiten in kontaminierten (verunreinigten) Bereichen"},
                        {"value": "andere", "label": "Andere Arbeiten"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit diesen "
                             "Lösungsmitteln (auch frühere Zeiten mitzählen)?",
                    "required": True,
                    "options": [
                        {"value": "neu", "label": "Noch gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis10", "label": "1 bis 10 Jahre"},
                        {"value": "ueber10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "enge_raeume",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit den Lösungsmitteln in engen Räumen, Gruben "
                             "oder Behältern oder bei schlechter Lüftung?",
                    "hint": "Die Dämpfe sind schwerer als Luft und sammeln sich am Boden "
                            "und in Vertiefungen an.",
                    "required": True,
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit direkt mit den Lösungsmitteln "
                             "in Kontakt (z. B. Spritzer, benetzte Kleidung, Reinigen von "
                             "Teilen mit bloßen Händen)?",
                    "required": True,
                },
                {
                    "id": "frueher_ckw",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt zu Trichlorethen, "
                             "Tetrachlorethen, Dichlormethan oder anderen "
                             "Lösungsmitteln?",
                    "required": True,
                    "followup": {"id": "frueher_ckw_desc", "type": "textarea",
                                 "label": "Welche Stoffe, welche Tätigkeiten, und wie lange?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Persönliche Schutzausrüstung und Absaugung",
            "questions": [
                {
                    "id": "handschuhe",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit möglichem Hautkontakt geeignete "
                             "Schutzhandschuhe?",
                    "hint": "Die Lösungsmittel können durch die Haut aufgenommen werden "
                            "(hautresorptiv) – Hautschutz und Schutzkleidung sind deshalb "
                            "besonders wichtig.",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_kontakt", "label": "Es gibt keinen möglichen Hautkontakt"},
                    ],
                },
                {
                    "id": "weitere_psa",
                    "type": "multi_choice",
                    "label": "Welche weiteren Schutzmaßnahmen gibt es an Ihrem "
                             "Arbeitsplatz?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "absaugung", "label": "Absaugung / geschlossene Anlage"},
                        {"value": "atemschutz", "label": "Atemschutz (Maske)"},
                        {"value": "schutzkleidung", "label": "Schutzkleidung / Schürze"},
                        {"value": "schutzbrille", "label": "Schutzbrille"},
                        {"value": "hautschutzplan", "label": "Hautschutzplan / Hautschutzmittel"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die mit den Lösungsmitteln zusammenhängen können",
            "questions": [
                {
                    "id": "neuro_zentral",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine oder mehrere der folgenden "
                             "Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Keine davon"},
                        {"value": "kopfschmerzen", "label": "Häufige Kopfschmerzen"},
                        {"value": "schwindel", "label": "Schwindel"},
                        {"value": "rausch", "label": "Benommenheit oder rauschartige Zustände bei der Arbeit"},
                        {"value": "konzentration", "label": "Konzentrationsstörungen"},
                        {"value": "vergesslichkeit", "label": "Auffällige Vergesslichkeit"},
                    ],
                },
                {
                    "id": "neuro_peripher",
                    "type": "multi_choice",
                    "label": "Haben Sie Missempfindungen oder Störungen an Armen oder "
                             "Beinen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Keine davon"},
                        {"value": "kribbeln", "label": "Kribbeln, Taubheitsgefühl oder Gefühlsstörungen "
                                                       "(Sensibilitätsstörungen)"},
                        {"value": "gang", "label": "Unsicherer Gang / Gangstörungen"},
                    ],
                },
                {
                    "id": "sinne",
                    "type": "multi_choice",
                    "label": "Haben Sie Veränderungen an Ihren Sinnen bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Keine davon"},
                        {"value": "geschmack", "label": "Störungen des Geschmackssinns"},
                        {"value": "geruch", "label": "Störungen des Geruchssinns"},
                        {"value": "sehen", "label": "Sehstörungen"},
                        {"value": "hoeren", "label": "Hörstörungen"},
                    ],
                },
                {
                    "id": "reiz",
                    "type": "multi_choice",
                    "label": "Haben Sie Reizerscheinungen an Augen, Atemwegen oder Haut?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Keine davon"},
                        {"value": "augen", "label": "Brennende oder gereizte Augen"},
                        {"value": "atemwege", "label": "Reizung von Nase, Rachen oder Atemwegen (Husten)"},
                        {"value": "haut", "label": "Hautprobleme (trockene, gerötete, rissige oder "
                                                   "juckende Haut, Ekzem)"},
                    ],
                },
                {
                    "id": "magen",
                    "type": "multi_choice",
                    "label": "Haben Sie Magen-Darm-Beschwerden oder Veränderungen von "
                             "Appetit und Gewicht?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Keine davon"},
                        {"value": "appetitlosigkeit", "label": "Appetitlosigkeit"},
                        {"value": "gewichtsabnahme", "label": "Ungewollte Gewichtsabnahme"},
                        {"value": "uebelkeit", "label": "Übelkeit oder Erbrechen"},
                        {"value": "bauchschmerzen", "label": "Bauchschmerzen oder Krämpfe"},
                    ],
                },
                {
                    "id": "herz_palp",
                    "type": "yes_no",
                    "label": "Haben Sie »Herzunruhe« – also Herzstolpern, Herzrasen oder "
                             "spürbar unregelmäßigen Herzschlag (Palpitationen)?",
                    "required": True,
                },
                {
                    "id": "brustschmerz",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit oder bei Anstrengung Druck- oder "
                             "Engegefühl in der Brust (Brustschmerzen)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, die für die Beurteilung wichtig sind",
            "questions": [
                {
                    "id": "vk_nerven",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung des Gehirns oder der "
                             "Nerven (z. B. Epilepsie/Krampfanfälle, Polyneuropathie = "
                             "Nervenschädigung an Armen/Beinen, Schlaganfall)?",
                    "required": True,
                    "followup": {"id": "vk_nerven_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, wie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "vk_herz",
                    "type": "multi_choice",
                    "label": "Haben oder hatten Sie eine der folgenden Herz-Kreislauf-"
                             "Erkrankungen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Keine davon"},
                        {"value": "rhythmus", "label": "Herzrhythmusstörungen"},
                        {"value": "khk", "label": "Koronare Herzkrankheit (verengte Herzkranzgefäße, "
                                                  "Angina pectoris, Herzinfarkt)"},
                        {"value": "pavk", "label": "Durchblutungsstörungen der Beine "
                                                   "(»Schaufensterkrankheit«, pAVK)"},
                        {"value": "hochdruck", "label": "Bluthochdruck, der nicht gut eingestellt ist"},
                    ],
                },
                {
                    "id": "vk_leber",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Lebererkrankung (z. B. Hepatitis "
                             "= Leberentzündung, Fettleber, Leberzirrhose)?",
                    "required": True,
                    "followup": {"id": "vk_leber_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vk_niere",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Nierenerkrankung (z. B. "
                             "Nierenentzündung, eingeschränkte Nierenfunktion, Blut im "
                             "Urin)?",
                    "required": True,
                    "followup": {"id": "vk_niere_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vk_ulkus",
                    "type": "yes_no",
                    "label": "Haben Sie zurzeit oder immer wiederkehrend ein Geschwür des "
                             "Magens oder Zwölffingerdarms (Ulkus)?",
                    "required": True,
                },
                {
                    "id": "abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von "
                             "Alkohol, Drogen (Rauschmitteln) oder Medikamenten?",
                    "required": True,
                },
            ],
        },
        # ── 6 ─ Alkohol und Rauchen ────────────────────────────────────────
        {
            "id": "genussmittel",
            "title": "Alkohol & Rauchen",
            "subtitle": "Beides kann die Wirkung der Lösungsmittel verstärken",
            "questions": [
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Alkohol verstärkt (potenziert) die Giftwirkung dieser "
                            "Lösungsmittel – deshalb fragen wir danach.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "selten", "label": "Selten (höchstens 1-mal pro Woche)"},
                        {"value": "mehrmals", "label": "Mehrmals pro Woche"},
                        {"value": "taeglich", "label": "Täglich"},
                    ],
                },
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "An Arbeitsplätzen mit diesen Lösungsmitteln gilt Rauchverbot: "
                            "an der glimmenden Zigarette können aus den Dämpfen giftige "
                            "Zersetzungsprodukte (u. a. Phosgen) entstehen.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, nie geraucht"},
                        {"value": "frueher", "label": "Früher geraucht, jetzt nicht mehr"},
                        {"value": "ja", "label": "Ja, ich rauche"},
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
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"vorzeitig_anlass": ["schwere_erkrankung", "zusammenhang"]},
     "schwere": "pruefen",
     "bereich": "Untersuchungsanlass",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Schwere/längere Erkrankung seit der letzten Untersuchung bzw. "
               "vermuteter Zusammenhang zwischen Erkrankung und Tätigkeit angegeben.",
     "konsequenz": "Tatbestand für eine vorzeitige Nachuntersuchung: Erkrankung "
                   "ärztlich klären (könnte Anlass zu Bedenken gegen die Fortsetzung "
                   "der Tätigkeit geben); vollständiges Untersuchungsprogramm "
                   "einschließlich spezieller Untersuchung und Biomonitoring "
                   "durchführen, Nachuntersuchungsfrist (12–24 Monate) ggf. verkürzen."},
    # ── Akute narkotische Wirkung / Beschwerden (Abschnitte 1.2, 3.2) ─────
    {"wenn": {"neuro_zentral": ["rausch"]},
     "schwere": "pruefen",
     "bereich": "Akute Wirkung",
     "quelle": "Abschnitte 1.2.1, 3.1.4 und 3.2.2",
     "befund": "Benommenheit oder rauschartige Zustände bei der Arbeit angegeben.",
     "konsequenz": "Hinweis auf akute narkotische Wirkung: Exposition klären, "
                   "Biomonitoring durchführen (Tetrachlorethen: BGW 0,4 mg/l Vollblut, "
                   "Probennahme vor der letzten Schicht einer Arbeitswoche; "
                   "Dichlormethan: Vollblut während der Exposition, EKA-Werte; "
                   "Trichlorethen: Trichloressigsäure im Urin). Bei Hinweisen auf "
                   "unzureichenden Arbeitsschutz Mitteilung an den Arbeitgeber zur "
                   "Aktualisierung der Gefährdungsbeurteilung."},
    {"wenn": {"neuro_zentral": ["kopfschmerzen", "schwindel", "konzentration",
                                "vergesslichkeit"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 1.2.1 und 1.2.3",
     "befund": "Zentralnervöse Symptome (Kopfschmerzen, Schwindel, "
               "Konzentrationsstörungen, Vergesslichkeit) angegeben.",
     "konsequenz": "Orientierende neurologische Untersuchung durchführen; in nicht "
                   "abklärbaren Fällen Ergänzungsuntersuchung: neurologisch-"
                   "psychiatrische Untersuchung, ggf. unter Einbeziehung "
                   "testpsychologischer Verfahren. An chronische ZNS-Schädigung/"
                   "Enzephalopathie (BK-Nr. 1317) denken."},
    {"wenn": {"neuro_peripher": ["kribbeln", "gang"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 1.2.1, 1.2.3 und 4",
     "befund": "Sensibilitätsstörungen oder Gangstörungen angegeben.",
     "konsequenz": "Orientierende neurologische Untersuchung; bei unklarem Befund "
                   "Ergänzungsuntersuchung (neurologisch-psychiatrisch, ggf. "
                   "testpsychologisch). Mögliche Polyneuropathie (BK-Nr. 1317) "
                   "abklären und in die Beurteilung nach 2.1 einbeziehen."},
    {"wenn": {"sinne": ["geschmack", "geruch", "sehen", "hoeren"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 1.2.1 und 1.2.3",
     "befund": "Störungen des Geschmacks- oder Geruchssinns bzw. Seh- oder "
               "Hörstörungen angegeben.",
     "konsequenz": "Als expositionsbezogenes Symptom werten (mögliche "
                   "Hirnnervenschädigung durch Dichloracetylen): orientierende "
                   "neurologische Untersuchung, ggf. Ergänzungsuntersuchung bzw. "
                   "fachärztliche Abklärung veranlassen."},
    {"wenn": {"reiz": ["augen", "atemwege", "haut"]},
     "schwere": "pruefen",
     "bereich": "Reizwirkung/Haut",
     "quelle": "Abschnitte 1.2.1, 2.2 und 3.2",
     "befund": "Reizerscheinungen an Augen, Atemwegen oder Haut angegeben.",
     "konsequenz": "Befund ärztlich erheben (Ekzeme und Dermatitiden sind chronische "
                   "Wirkungen; die Stoffe entfetten die Haut). Beratung zu Hautschutz "
                   "und Schutzkleidung, stoffspezifische Hinweise über GESTIS; bei "
                   "Hinweisen auf unzureichenden Arbeitsschutz Mitteilung an den "
                   "Arbeitgeber."},
    {"wenn": {"magen": ["appetitlosigkeit", "gewichtsabnahme", "uebelkeit",
                        "bauchschmerzen"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm/Leber",
     "quelle": "Abschnitte 1.2.1, 1.2.2 und 1.2.3",
     "befund": "Appetitlosigkeit, Gewichtsabnahme, Übelkeit/Erbrechen oder "
               "Bauchschmerzen angegeben.",
     "konsequenz": "Spezielle Untersuchung auswerten (γ-GT, ALAT, ASAT), Urinstatus; "
                   "in nicht abklärbaren Fällen Ergänzungsuntersuchung mit weiterer "
                   "Leber- und Nierendiagnostik. Ulkusleiden erfragen "
                   "(Bedenkenstatbestand nach 2.1.1)."},
    {"wenn": {"herz_palp": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 1.2.1, 1.2.2 und 3.2.1",
     "befund": "»Herzunruhe« (Palpitationen) angegeben.",
     "konsequenz": "Ruhe-EKG durchführen (in der speziellen Untersuchung als "
                   "erwünscht vorgesehen, bei Palpitationen indiziert). "
                   "Sensibilisierung der Reizbildung und Reizleitung des Herzens "
                   "durch die Stoffe berücksichtigen; Beurteilung nach 2.1."},
    {"wenn": {"brustschmerz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 3.2.1 und 3.2.2 (Dichlormethan)",
     "befund": "Druck-/Engegefühl in der Brust (pektanginöse Beschwerden) angegeben.",
     "konsequenz": "Kardiale Abklärung (Ruhe-EKG, ggf. fachärztliche Vorstellung). "
                   "Bei Dichlormethan an die Bildung von Kohlenmonoxid denken: "
                   "CO-Hämoglobin-Spiegel soll unter 5 % liegen; Biomonitoring "
                   "(Dichlormethan im Vollblut während der Exposition, mindestens "
                   "2 Stunden nach Expositionsbeginn)."},
    # ── Bedenkenstatbestände (Abschnitt 2.1.1) ────────────────────────────
    {"wenn": {"vk_nerven": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung Nervensystem",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3",
     "befund": "Erkrankung des zentralen und/oder peripheren Nervensystems angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1 (dauernde gesundheitliche "
                   "Bedenken): Ausprägung ärztlich klären. Bei zu erwartender "
                   "Wiederherstellung befristete Bedenken (2.1.2); bei geringer "
                   "Ausprägung prüfen, ob keine Bedenken unter bestimmten "
                   "Voraussetzungen möglich sind (2.1.3: technische/organisatorische "
                   "Schutzmaßnahmen, geringere Exposition, PSA, verkürzte "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"vk_herz": ["rhythmus", "khk", "pavk", "hochdruck"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung Herz-Kreislauf",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3 und 3.2.1",
     "befund": "Herz-Kreislauf-Erkrankung angegeben (Rhythmusstörungen, KHK, "
               "periphere arterielle Durchblutungsstörungen oder unzureichend "
               "behandelter Bluthochdruck).",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1: Ruhe-EKG und kardiale Vorbefunde "
                   "einholen (Herzkammerflimmern als akute Gefahr, Sensibilisierung "
                   "des Herzens). Bei Dichlormethan-Exposition und KHK/pAVK muss der "
                   "CO-Hämoglobin-Spiegel unter 5 % liegen. Bei geringer Ausprägung "
                   "keine Bedenken unter Voraussetzungen (2.1.3), sonst befristete "
                   "bzw. dauernde Bedenken (2.1.2/2.1.1)."},
    {"wenn": {"vk_leber": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung Leber",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3 und 1.2.2",
     "befund": "Lebererkrankung angegeben.",
     "konsequenz": "Bei funktionellen Auswirkungen Bedenkenstatbestand nach 2.1.1: "
                   "Leberwerte (γ-GT, ALAT, ASAT) bestimmen, in unklaren Fällen "
                   "Ergänzungsuntersuchung (weitere Leberdiagnostik). Die Stoffe sind "
                   "lebertoxisch – bei geringer Ausprägung keine Bedenken nur unter "
                   "Voraussetzungen nach 2.1.3 (u. a. verkürzte "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"vk_niere": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung Niere",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3 und 1.2.2",
     "befund": "Nierenerkrankung angegeben.",
     "konsequenz": "Bei funktionellen Auswirkungen Bedenkenstatbestand nach 2.1.1: "
                   "Kreatinin im Serum bestimmen, Urinstatus mit Sediment; bei "
                   "Trichlorethen zusätzlich α1-Mikroglobulin im Harn. Bei geringer "
                   "Ausprägung keine Bedenken nur unter Voraussetzungen nach 2.1.3."},
    {"wenn": {"vk_ulkus": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung Magen-Darm",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3",
     "befund": "Florides oder chronisch wiederkehrendes Magen-/Zwölffingerdarm-"
               "Geschwür angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1: Behandlungsstand klären "
                   "(hausärztliche/gastroenterologische Betreuung). Bei Ausheilung "
                   "befristete Bedenken (2.1.2), bei geringer Ausprägung keine "
                   "Bedenken unter Voraussetzungen (2.1.3)."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Abhängigkeitserkrankung",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3 und 3.2.1",
     "befund": "Alkohol-, Rauschmittel- oder Medikamentenabhängigkeit angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1 – Alkohol potenziert die "
                   "Giftwirkung der Lösungsmittel. Suchtmedizinische Behandlung "
                   "klären; bei erfolgreicher Behandlung befristete Bedenken (2.1.2) "
                   "bzw. keine Bedenken unter Voraussetzungen (2.1.3) prüfen."},
    # ── Alkohol, Rauchen (Abschnitte 2.2, 3.1.4) ──────────────────────────
    {"wenn": {"alkohol": ["mehrmals", "taeglich"]},
     "wenn_nicht": {"abhaengigkeit": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 2.2, 3.1.4 und 3.2.1",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung: Alkohol potenziert die Giftwirkung der "
                   "Chlorkohlenwasserstoffe; nach Alkoholgenuss sind plötzliche "
                   "Todesfälle durch Herzkammerflimmern beschrieben. Beim "
                   "Trichlorethen-Biomonitoring beachten: Ethanol hemmt die "
                   "Metabolisierung deutlich (Confounder bei der Bewertung der "
                   "Trichloressigsäure-Werte)."},
    {"wenn": {"rauchen": ["ja"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 2.2 und 3.1.4",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung zum potenzierenden Einfluss des Tabakkonsums und "
                   "ausdrücklicher Hinweis auf das Rauchverbot am Arbeitsplatz "
                   "(Pyrolyseprodukte, u. a. Phosgen). Beim Dichlormethan-"
                   "Biomonitoring beachten: Rauchen kann auch ohne Exposition "
                   "CO-Hb-Werte über 5 % verursachen (Confounder)."},
    # ── Schutzmaßnahmen / Exposition ──────────────────────────────────────
    {"wenn": {"hautkontakt": ["yes"], "handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Hautschutz",
     "quelle": "Abschnitte 2.2 und 3.1.3",
     "befund": "Direkter Hautkontakt ohne regelmäßige Schutzhandschuhe angegeben.",
     "konsequenz": "Die Stoffe können über die Haut aufgenommen werden "
                   "(hautresorptiv): intensive Beratung zu Hautschutz, "
                   "Schutzkleidung und Hygienemaßnahmen (stoffspezifische Hinweise "
                   "über GESTIS). Bei Hinweisen auf unzureichenden Arbeitsschutz "
                   "Mitteilung an den Arbeitgeber zur Aktualisierung der "
                   "Gefährdungsbeurteilung – unter Wahrung der schutzwürdigen "
                   "Belange der untersuchten Person."},
    {"wenn": {"expo_dauer": ["ueber10"], "stoffe": ["trichlorethen"]},
     "schwere": "pruefen",
     "bereich": "Trichlorethen/Nieren",
     "quelle": "Abschnitte 1.2.3 und 3.2.1",
     "befund": "Trichlorethen-Exposition seit mehr als 10 Jahren (Latenzzeit "
               "erreicht).",
     "konsequenz": "Auf Nierenzelltumor-Risiko achten: Urinstatus und "
                   "α1-Mikroglobulin im Harn kontrollieren; bei Mikrohämaturie "
                   "und/oder erhöhtem α1-Mikroglobulin Ergänzungsuntersuchung mit "
                   "weiterer Nierendiagnostik, z. B. Ultraschalluntersuchung der "
                   "Nieren, veranlassen."},
    {"wenn": {"stoffe": ["trichlorethen"]},
     "schwere": "hinweis",
     "bereich": "Krebserzeugender Stoff/nachgehende Untersuchungen",
     "quelle": "Abschnitte 1.1 und 2.2",
     "befund": "Tätigkeit mit Trichlorethen (krebserzeugend) angegeben.",
     "konsequenz": "Beratung über die krebserzeugende Wirkung. Nur bei Trichlorethen: "
                   "Nachuntersuchungen nach dem Ausscheiden aus der Tätigkeit bei "
                   "bestehendem Beschäftigungsverhältnis sowie nachgehende "
                   "Untersuchungen nach Beendigung der Beschäftigung sicherstellen – "
                   "Anmeldung beim Organisationsdienst für nachgehende Untersuchungen "
                   "(ODIN, www.odin-info.de) veranlassen."},
]
