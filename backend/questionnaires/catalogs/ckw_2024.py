# -*- coding: utf-8 -*-
"""Trichlorethen (Trichlorethylen), Tetrachlorethen (Perchlorethylen) und
Dichlormethan (Methylenchlorid) – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen
für arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Trichlorethen (Trichlorethylen), Tetrachlorethen (Perchlorethylen),
Dichlormethan (Methylenchlorid)« (E CKW, Fassung Januar 2022), S. 715–737."""

SLUG = "ckw-2024"

CATALOG = {
    "version": 2,
    "title": "Trichlorethen, Tetrachlorethen und Dichlormethan (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Trichlorethen (Trichlorethylen), Tetrachlorethen "
             "(Perchlorethylen), Dichlormethan (Methylenchlorid)« (E CKW, "
             "Fassung Januar 2022), S. 715–737",
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
                             "Chlorkohlenwasserstoff-Lösungsmitteln (Tri, Per oder "
                             "Dichlormethan)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge zu diesen Stoffen"},
                        {"value": "weitere", "label": "Nein, ich war deswegen schon einmal zur Vorsorge"},
                        {"value": "nachgehend", "label": "Ich arbeite nicht mehr mit den Stoffen "
                                                         "(nachgehende Vorsorge)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: bei Trichlorethen, wenn wiederholte Exposition oder "
                            "Hautkontakt nicht ausgeschlossen werden können; bei Tetrachlorethen, "
                            "wenn der Arbeitsplatzgrenzwert nicht eingehalten wird oder Hautkontakt "
                            "möglich ist. Angebotsvorsorge: wenn eine Exposition nicht "
                            "ausgeschlossen werden kann.",
                    "required": True,
                    "options": [
                        {"value": "pflicht", "label": "Vom Betrieb verpflichtend veranlasst (Pflichtvorsorge)"},
                        {"value": "angebot", "label": "Vom Betrieb angeboten (Angebotsvorsorge)"},
                        {"value": "wunsch", "label": "Auf meinen eigenen Wunsch (Wunschvorsorge)"},
                        {"value": "nachgehend", "label": "Einladung nach dem Ausscheiden (nachgehende Vorsorge)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
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
                        {"value": "chemischreinigung", "label": "Chemische Reinigung (Textilreinigung)"},
                        {"value": "reinigen_entfetten", "label": "Reinigen und Entfetten von Teilen"},
                        {"value": "abbeizen", "label": "Farb- oder Schichtenentferner (Abbeizer, Lackentferner)"},
                        {"value": "kleben_beschichten", "label": "Kleben, Beschichten oder Formenschäumen"},
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
                {
                    "id": "laerm",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit den Lösungsmitteln in einem Lärmbereich "
                             "(so laut, dass Gehörschutz vorgeschrieben ist)?",
                    "hint": "Trichlorethen kann das Gehör zusätzlich belasten "
                            "(»ototoxisch« = ohrschädigend).",
                    "required": True,
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
                            "(hautresorptiv) – geeignete Handschuhe sind deshalb besonders "
                            "wichtig.",
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
                        {"value": "kleiderwechsel", "label": "Getrennte Arbeitskleidung mit Wechselmöglichkeit"},
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
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Alkohol verstärkt die Giftwirkung dieser Lösungsmittel – "
                            "deshalb fragen wir danach.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "selten", "label": "Selten (höchstens 1-mal pro Woche)"},
                        {"value": "mehrmals", "label": "Mehrmals pro Woche"},
                        {"value": "taeglich", "label": "Täglich"},
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
    # ── Akute narkotische Wirkung / unzureichender Schutz ─────────────────
    {"wenn": {"neuro_zentral": ["rausch"]},
     "schwere": "pruefen",
     "bereich": "Akute Wirkung",
     "quelle": "Abschnitte 6.3.2, 7.1 und 8.2",
     "befund": "Benommenheit oder rauschartige Zustände bei der Arbeit angegeben.",
     "konsequenz": "Hinweis auf akute narkotische Wirkung: Exposition ärztlich klären, "
                   "Biomonitoring durchführen (Tetrachlorethen 0,2 mg/l Vollblut, "
                   "Dichlormethan 0,5 mg/l Vollblut, Trichlorethen: Trichloressigsäure "
                   "im Urin), orientierende neurologische Untersuchung. Anhaltspunkte "
                   "für unzureichende Schutzmaßnahmen dem Unternehmen mitteilen und "
                   "Maßnahmen vorschlagen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"neuro_zentral": ["kopfschmerzen", "schwindel", "konzentration",
                                "vergesslichkeit"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Tätigkeitsspezifische zentralnervöse Symptome (Kopfschmerzen, Schwindel, "
               "Konzentrationsstörungen, Vergesslichkeit) angegeben.",
     "konsequenz": "Orientierende neurologische Untersuchung durchführen; in nicht "
                   "abklärbaren Fällen neurologisch-psychiatrische Untersuchung, ggf. "
                   "unter Einbeziehung testpsychologischer Verfahren (7.2.2). An "
                   "chronische ZNS-Schädigung/Enzephalopathie (BK-Nr. 1317) denken."},
    {"wenn": {"neuro_peripher": ["kribbeln", "gang"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 7.1, 7.2.2 und 6.5",
     "befund": "Sensibilitätsstörungen oder Gangstörungen angegeben.",
     "konsequenz": "Orientierende neurologische Untersuchung; bei unklarem Befund "
                   "neurologisch-psychiatrische Untersuchung, ggf. mit "
                   "testpsychologischen Verfahren. Mögliche Polyneuropathie "
                   "(BK-Nr. 1317) abklären und Beurteilung nach 7.4 vornehmen."},
    {"wenn": {"sinne": ["geschmack", "geruch", "sehen", "hoeren"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Störungen des Geschmacks- oder Geruchssinns bzw. Seh- oder "
               "Hörstörungen angegeben.",
     "konsequenz": "Als tätigkeitsspezifisches Symptom werten (mögliche "
                   "Hirnnervenschädigung): orientierende neurologische Untersuchung, "
                   "ggf. neurologisch-psychiatrische bzw. fachärztliche Abklärung "
                   "veranlassen."},
    {"wenn": {"reiz": ["augen", "atemwege", "haut"]},
     "schwere": "pruefen",
     "bereich": "Reizwirkung/Haut",
     "quelle": "Abschnitte 6.3, 7.1 und 8.1",
     "befund": "Reizerscheinungen an Augen, Atemwegen oder Haut angegeben.",
     "konsequenz": "Befund ärztlich erheben (Ekzeme und Dermatitiden sind chronische "
                   "Wirkungen). Beratung zu Hautschutz und geeigneten "
                   "Handschuhmaterialien (Sicherheitsdatenblatt Kapitel 8, GESTIS, "
                   "GISCHEM, WINGIS); bei Anhaltspunkten für unzureichende "
                   "Schutzmaßnahmen Mitteilung an das Unternehmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"magen": ["appetitlosigkeit", "gewichtsabnahme", "uebelkeit",
                        "bauchschmerzen"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm/Leber",
     "quelle": "Abschnitte 6.3, 7.1 und 7.2.2",
     "befund": "Appetitlosigkeit, Gewichtsabnahme, Übelkeit/Erbrechen oder "
               "Bauchschmerzen angegeben.",
     "konsequenz": "Leberwerte bestimmen (γ-GT, ALAT, ASAT), Urinstatus; in nicht "
                   "abklärbaren Fällen weitere Leber- und Nierendiagnostik. "
                   "Ulkusleiden erfragen und Beurteilung nach 7.4 berücksichtigen."},
    {"wenn": {"herz_palp": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "»Herzunruhe« (Palpitationen) angegeben.",
     "konsequenz": "Ruhe-EKG bei Verdacht auf Herzrhythmusstörungen (ergänzende "
                   "Untersuchung nach 7.2.2). Sensibilisierung des Herzens durch die "
                   "Lösungsmittel berücksichtigen; Beurteilung nach 7.4."},
    {"wenn": {"brustschmerz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 6.3.1 und 6.3.2 (Dichlormethan)",
     "befund": "Druck-/Engegefühl in der Brust (pektanginöse Beschwerden) angegeben.",
     "konsequenz": "Kardiale Abklärung (Ruhe-EKG, ggf. fachärztliche Vorstellung). Bei "
                   "Dichlormethan an die Bildung von Kohlenmonoxid denken: "
                   "CO-Hämoglobin-Spiegel soll unter 5 % liegen, Biomonitoring "
                   "(Dichlormethan 0,5 mg/l Vollblut, unmittelbar nach Exposition)."},
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"vk_nerven": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung Nervensystem",
     "quelle": "Abschnitte 7.4 bis 7.4.4",
     "befund": "Erkrankung des zentralen und/oder peripheren Nervensystems angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Ausmaß prüfen, ob die "
                   "Tätigkeit ohne gesundheitliche Gefährdung möglich ist. Maßnahmen "
                   "nach 7.4.2 erwägen (Substitution, technische/organisatorische "
                   "Schutzmaßnahmen, Expositionsbegrenzung, PSA); bei zu erwartender "
                   "Änderung des Schweregrads verkürzte Fristen (7.4.3), bei fehlender "
                   "Erfolgsaussicht Tätigkeitswechsel erwägen (7.4.4, Mitteilung nur "
                   "mit Einwilligung)."},
    {"wenn": {"vk_herz": ["rhythmus", "khk", "pavk", "hochdruck"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung Herz-Kreislauf",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Herz-Kreislauf-Erkrankung angegeben (Rhythmusstörungen, KHK, periphere "
               "arterielle Durchblutungsstörungen oder unzureichend behandelter "
               "Bluthochdruck).",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Ruhe-EKG veranlassen, "
                   "kardiale Vorbefunde einholen. Maßnahmen nach 7.4.2 bzw. verkürzte "
                   "Vorsorgefristen nach 7.4.3 prüfen (Sensibilisierung des Herzens "
                   "durch die Stoffe, Herzkammerflimmern als akute Gefahr)."},
    {"wenn": {"vk_herz": ["khk", "pavk"], "stoffe": ["dichlormethan"]},
     "schwere": "pruefen",
     "bereich": "Dichlormethan/CO-Bildung",
     "quelle": "Abschnitte 6.3.1 und 7.4",
     "befund": "Koronare Herzkrankheit oder periphere arterielle "
               "Durchblutungsstörungen bei Tätigkeit mit Dichlormethan.",
     "konsequenz": "Kritischer Effekt von Dichlormethan ist die CO-Bildung: "
                   "CO-Hämoglobin-Spiegel muss unter 5 % bleiben. Biomonitoring "
                   "(Dichlormethan 0,5 mg/l Vollblut) engmaschig durchführen; "
                   "Maßnahmen nach 7.4.2 (Substitution, Expositionsbegrenzung) und "
                   "verkürzte Fristen nach 7.4.3 prüfen; bei fehlender Erfolgsaussicht "
                   "Tätigkeitswechsel erwägen (7.4.4)."},
    {"wenn": {"vk_leber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung Leber",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Lebererkrankung angegeben.",
     "konsequenz": "Bei funktionellen Auswirkungen beurteilungsrelevant nach 7.4: "
                   "Leberwerte (γ-GT, ALAT, ASAT) kontrollieren, in unklaren Fällen "
                   "weitere Leberdiagnostik. Maßnahmen nach 7.4.2 bzw. verkürzte "
                   "Fristen nach 7.4.3 erwägen (Lösungsmittel sind lebertoxisch)."},
    {"wenn": {"vk_niere": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung Niere",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Nierenerkrankung angegeben.",
     "konsequenz": "Bei funktionellen Auswirkungen beurteilungsrelevant nach 7.4: "
                   "Kreatinin im Serum bestimmen (7.2.2), Urinstatus mit Sediment; bei "
                   "Trichlorethen zusätzlich α1-Mikroglobulin im Harn. Maßnahmen nach "
                   "7.4.2 bzw. verkürzte Fristen nach 7.4.3 erwägen."},
    {"wenn": {"expo_dauer": ["ueber10"], "stoffe": ["trichlorethen"]},
     "schwere": "pruefen",
     "bereich": "Trichlorethen/Nieren",
     "quelle": "Abschnitt 7.2.2 (ergänzende Untersuchungen)",
     "befund": "Trichlorethen-Exposition seit mehr als 10 Jahren (Latenzzeit erreicht).",
     "konsequenz": "Auf Nierenzelltumor-Risiko achten: Urinstatus und α1-Mikroglobulin "
                   "im Harn kontrollieren; bei Mikrohämaturie und/oder erhöhtem "
                   "α1-Mikroglobulin weitere Nierendiagnostik, z. B. "
                   "Ultraschalluntersuchung der Nieren, veranlassen."},
    {"wenn": {"vk_ulkus": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung Magen-Darm",
     "quelle": "Abschnitt 7.4",
     "befund": "Florides oder chronisch wiederkehrendes Magen-/Zwölffingerdarm-"
               "Geschwür angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Behandlungsstand klären "
                   "(hausärztliche/gastroenterologische Betreuung), Maßnahmen nach "
                   "7.4.2 bzw. verkürzte Fristen nach 7.4.3 erwägen."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Abhängigkeitserkrankung",
     "quelle": "Abschnitte 7.4 und 6.3.1",
     "befund": "Alkohol-, Rauschmittel- oder Medikamentenabhängigkeit angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4 – Alkohol verstärkt die "
                   "Giftwirkung der Lösungsmittel. Suchtmedizinische Behandlung "
                   "klären; Maßnahmen nach 7.4.2 bzw. verkürzte Fristen nach 7.4.3 "
                   "prüfen, bei fehlender Erfolgsaussicht Tätigkeitswechsel erwägen "
                   "(7.4.4)."},
    {"wenn": {"alkohol": ["mehrmals", "taeglich"]},
     "wenn_nicht": {"abhaengigkeit": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 6.3.1 und 6.3.2",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung: Alkohol verstärkt die Giftwirkung der "
                   "Chlorkohlenwasserstoffe; nach Alkoholgenuss sind plötzliche "
                   "Todesfälle durch Herzkammerflimmern beschrieben. Zu reduziertem "
                   "Konsum an Arbeitstagen raten."},
    # ── Schutzmaßnahmen / Exposition ──────────────────────────────────────
    {"wenn": {"hautkontakt": ["yes"], "handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Hautschutz",
     "quelle": "Abschnitte 6.2, 8.1 und 8.2",
     "befund": "Direkter Hautkontakt ohne regelmäßige Schutzhandschuhe angegeben.",
     "konsequenz": "Die Stoffe werden über die Haut aufgenommen: intensive Beratung zu "
                   "PSA und geeigneten Handschuhmaterialien (Sicherheitsdatenblatt, "
                   "GESTIS, GISCHEM, WINGIS, Portal der BG ETEM). Anhaltspunkte für "
                   "unzureichende Schutzmaßnahmen dem Unternehmen mitteilen und "
                   "Schutzmaßnahmen vorschlagen (§ 6 (4) ArbMedVV); "
                   "Pflichtvorsorge-Tatbestand (Hautkontakt) beachten."},
    {"wenn": {"laerm": ["yes"], "stoffe": ["trichlorethen"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 6.1",
     "befund": "Trichlorethen-Exposition in Lärmbereichen angegeben.",
     "konsequenz": "Wegen der ototoxischen Eigenschaften von Trichlorethen mögliche "
                   "Kombinationswirkungen mit Lärm bei der Gehörvorsorge nach der "
                   "DGUV Empfehlung »Lärm« berücksichtigen; Abstimmung mit der "
                   "Lärm-Vorsorge sicherstellen."},
    {"wenn": {"stoffe": ["trichlorethen", "tetrachlorethen"]},
     "schwere": "hinweis",
     "bereich": "Krebserzeugender Stoff/nachgehende Vorsorge",
     "quelle": "Abschnitte 2, 6 und 8.1",
     "befund": "Tätigkeit mit Trichlorethen (krebserzeugend Kategorie 1B) bzw. "
               "Tetrachlorethen (Kategorie 2) angegeben.",
     "konsequenz": "Beratung zur krebserzeugenden und erbgutverändernden Wirkung "
                   "(bei Trichlorethen Kategorie 1B). Nachgehende Vorsorge: Bei "
                   "Tätigkeiten mit Trichlorethen oder Tetrachlorethen hat das "
                   "Unternehmen nach dem Ausscheiden aus der Tätigkeit nachgehende "
                   "Vorsorge anzubieten – Anmeldung über das Meldeportal "
                   "»DGUV Vorsorge« (www.dguv-vorsorge.de) sicherstellen. Bei "
                   "Untersuchungen im Rahmen der nachgehenden Vorsorge kann das "
                   "Biomonitoring bei Trichlorethen in der Regel entfallen (7.2.2)."},
]
