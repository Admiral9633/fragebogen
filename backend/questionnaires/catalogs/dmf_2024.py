# -*- coding: utf-8 -*-
"""Dimethylformamid – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Dimethylformamid« (E DMF, Fassung Januar 2022), S. 228–242."""

SLUG = "dmf-2024"

CATALOG = {
    "version": 2,
    "title": "Dimethylformamid (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Dimethylformamid« (E DMF, Fassung Januar 2022), S. 228–242",
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
                             "Dimethylformamid (DMF)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste DMF-Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur DMF-Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Luftgrenzwert für DMF nicht eingehalten wird oder eine Gefährdung "
                            "durch Hautkontakt nicht ausgeschlossen werden kann. "
                            "Angebotsvorsorge: wenn eine DMF-Belastung möglich ist.",
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
            "title": "Tätigkeit & Kontakt mit DMF",
            "subtitle": "Ihre Arbeit und Ihr Umgang mit Dimethylformamid",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
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
                                                               "an Produktions- oder Abfüllanlagen"},
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
                             "Berührung (z. B. Spritzer, durchfeuchtete Handschuhe oder Kleidung)?",
                    "hint": "DMF wird sehr gut über die Haut aufgenommen – Hautkontakt ist "
                            "deshalb besonders wichtig für die Beurteilung.",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                },
                {
                    "id": "agw_einhaltung",
                    "type": "choice",
                    "label": "Wissen Sie, ob der Luftgrenzwert (Arbeitsplatzgrenzwert) für DMF "
                             "an Ihrem Arbeitsplatz eingehalten wird?",
                    "hint": "Diese Information stammt aus der Gefährdungsbeurteilung Ihres "
                            "Betriebs, z. B. aus Unterweisungen oder Messberichten.",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                    "options": [
                        {"value": "eingehalten", "label": "Ja, er wird eingehalten"},
                        {"value": "ueberschritten", "label": "Nein, er wird überschritten"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
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
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
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
                    "hint": "Wegen der Aufnahme über die Haut sind geeignete Handschuhe "
                            "bei DMF besonders wichtig.",
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
                    "id": "psa_atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit DMF-Dämpfen Atemschutz?",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                    "options": [
                        {"value": "immer", "label": "Ja, immer wenn erforderlich"},
                        {"value": "teilweise", "label": "Nur manchmal"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_erforderlich", "label": "Atemschutz ist bei meiner Arbeit nicht vorgesehen"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme mit Ihrer Schutzausrüstung (z. B. undichte oder "
                             "beschädigte Handschuhe, Hautprobleme unter den Handschuhen)?",
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
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die mit DMF zusammenhängen können – "
                        "das wichtigste Zielorgan ist die Leber",
            "questions": [
                {
                    "id": "flush_alkohol",
                    "type": "yes_no",
                    "label": "Vertragen Sie Alkohol schlechter als früher – z. B. Gesichtsrötung, "
                             "Schwindel, Übelkeit oder Engegefühl in der Brust schon nach kleinen "
                             "Mengen (»Flush«)?",
                    "hint": "Eine solche Alkoholunverträglichkeit kann bis zu 4 Tage nach einer "
                            "DMF-Belastung auftreten und ist ein deutliches Zeichen dafür, dass "
                            "DMF in den Körper aufgenommen wurde.",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                },
                {
                    "id": "oberbauch_druck",
                    "type": "yes_no",
                    "label": "Haben Sie ein Druck- oder Völlegefühl im rechten Oberbauch oder "
                             "kolikartige (krampfartige) Bauchschmerzen?",
                    "required": True,
                },
                {
                    "id": "appetit_uebelkeit",
                    "type": "yes_no",
                    "label": "Leiden Sie unter Appetitlosigkeit, Übelkeit oder Erbrechen?",
                    "required": True,
                },
                {
                    "id": "verdauung",
                    "type": "yes_no",
                    "label": "Haben Sie Verdauungsstörungen (Durchfall oder Verstopfung)?",
                    "required": True,
                },
                {
                    "id": "gewichtsverlust",
                    "type": "yes_no",
                    "label": "Haben Sie in letzter Zeit ungewollt an Gewicht verloren?",
                    "required": True,
                },
                {
                    "id": "kopfschmerz",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Kopfschmerzen?",
                    "required": True,
                },
                {
                    "id": "reizung",
                    "type": "multi_choice",
                    "label": "Bemerken Sie bei der Arbeit Reizerscheinungen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                    "options": [
                        {"value": "atemwege", "label": "Brennen oder Reizung in Nase und Rachen"},
                        {"value": "haut", "label": "Hautreizung mit Juckreiz oder Schuppung"},
                        {"value": "augen", "label": "Gerötete, brennende oder tränende Augen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen und Lebensweise ────────────────────────────
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
                    "hint": "DMF und Alkohol beeinflussen sich gegenseitig im Körper – "
                            "deshalb ist diese Frage hier wichtig.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "gelegentlich", "label": "Gelegentlich (z. B. zu besonderen Anlässen)"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche)"},
                    ],
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Sind Sie derzeit schwanger, oder könnte eine Schwangerschaft "
                             "bestehen?",
                    "hint": "DMF kann das Kind im Mutterleib schädigen – auch wenn der "
                            "Grenzwert am Arbeitsplatz eingehalten wird.",
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
    # ── Mutterschutz (Abschnitte 6.3.3, 7.1 und 8.1) ──────────────────────
    {"wenn": {"schwangerschaft": ["ja", "moeglich"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6.3.3, 7.1 und 8.1 (Schädigung des Kindes im Mutterleib)",
     "befund": "Schwangerschaft besteht oder ist möglich.",
     "konsequenz": "Vor (weiterer) Tätigkeit mit DMF klären: Die fruchtschädigende Wirkung "
                   "kann auch bei Einhaltung des Arbeitsplatzgrenzwertes nicht ausgeschlossen "
                   "werden. Unverzüglich zum Mutterschutz beraten (Mutterschutzgesetz), "
                   "Expositionsvermeidung sicherstellen; bei unklarer Schwangerschaft "
                   "Klärung vor Fortsetzung der Tätigkeit empfehlen."},
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"lebererkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 7.4 bis 7.4.4 (Beurteilungskriterien)",
     "befund": "Chronische Lebererkrankung angegeben.",
     "konsequenz": "Prüfen, ob die Tätigkeit im Einzelfall ohne gesundheitliche Gefährdung "
                   "möglich ist: Leberwerte (γ-GT, ALAT, ASAT) und Biomonitoring durchführen, "
                   "Vorbefunde einholen. Bei weniger ausgeprägter Erkrankung Maßnahmen nach "
                   "7.4.2 (Substitution, technische/organisatorische Maßnahmen, Begrenzung "
                   "der Expositionszeit, Arbeitsplatz mit geringerer Exposition, PSA) und "
                   "verkürzte Fristen nach 7.4.3 empfehlen; ohne Aussicht auf Erfolg "
                   "Tätigkeitswechsel nach 7.4.4 erwägen (Mitteilung an den Arbeitgeber nur "
                   "mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Abhängigkeitserkrankung",
     "quelle": "Abschnitte 7.4 bis 7.4.4 (Beurteilungskriterien)",
     "befund": "Alkohol-, Rauschmittel- oder Medikamentenabhängigkeit angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung: Ausprägung ärztlich klären, Leberwerte "
                   "kontrollieren. Prüfen, ob die Tätigkeit mit Maßnahmen nach 7.4.2 bzw. "
                   "verkürzten Fristen nach 7.4.3 möglich ist; andernfalls Tätigkeitswechsel "
                   "nach 7.4.4 erwägen. Beratung zu Behandlungsangeboten."},
    {"wenn": {"leberwerte": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitt 7.2.2 (Klinische Untersuchungen)",
     "befund": "Früher erhöhte Leberwerte angegeben.",
     "konsequenz": "Aktuelle Leberwerte (γ-GT, ALAT, ASAT) bestimmen und mit Vorbefunden "
                   "vergleichen; in unklaren Fällen weitere Leberdiagnostik, z. B. "
                   "Oberbauch-Sonographie."},
    # ── Tätigkeitsspezifische Beschwerden (Abschnitte 6.3, 7.1, 7.2.2) ────
    {"wenn": {"flush_alkohol": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Alkoholunverträglichkeit",
     "quelle": "Abschnitte 6.3.1, 6.4 und 7.2.2",
     "befund": "Alkoholunverträglichkeit (Flush-Syndrom) angegeben – deutliches Indiz "
               "für eine DMF-Aufnahme.",
     "konsequenz": "Biomonitoring veranlassen (NMF plus N-Hydroxymethyl-N-methylformamid im "
                   "Urin, BGW 20 mg/l, bzw. AMCC 25 mg/g Kreatinin; Probennahme zum "
                   "Expositions-/Schichtende) und Leberwerte (γ-GT, ALAT, ASAT) bestimmen. "
                   "Expositionssituation mit der Gefährdungsbeurteilung abgleichen; reichen "
                   "die Schutzmaßnahmen nicht aus, Mitteilung an das Unternehmen und "
                   "Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"oberbauch_druck": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 6.3.1, 7.1 und 7.2.2",
     "befund": "Druck-/Völlegefühl im rechten Oberbauch bzw. kolikartige Leibschmerzen.",
     "konsequenz": "Mögliches Leitsymptom einer Leberzellschädigung: Leberwerte (γ-GT, ALAT, "
                   "ASAT) und Biomonitoring durchführen; in unklaren Fällen weitere "
                   "Leberdiagnostik (z. B. Oberbauch-Sonographie), ggf. fachärztliche "
                   "Abklärung."},
    {"wenn": {"appetit_uebelkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber/Magen-Darm",
     "quelle": "Abschnitte 6.3.3 und 7.1",
     "befund": "Appetitlosigkeit, Übelkeit oder Erbrechen angegeben.",
     "konsequenz": "Tätigkeitsspezifisches Symptom vertiefen (zeitlicher Bezug zur Arbeit): "
                   "Leberwerte und Biomonitoring durchführen; bei unklarem Befund weitere "
                   "Leberdiagnostik veranlassen."},
    {"wenn": {"verdauung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm",
     "quelle": "Abschnitte 6.3.3 und 7.1",
     "befund": "Verdauungsstörungen (Durchfall oder Verstopfung) angegeben.",
     "konsequenz": "Im Rahmen der Untersuchung abklären (Leberwerte, Biomonitoring); "
                   "differenzialdiagnostisch auch an Pankreatitis und andere Ursachen "
                   "denken, ggf. weiterführende Diagnostik."},
    {"wenn": {"gewichtsverlust": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allgemeinsymptome",
     "quelle": "Abschnitte 6.3.3 und 7.1",
     "befund": "Ungewollter Gewichtsverlust angegeben.",
     "konsequenz": "Abklärung veranlassen: Leberwerte, Biomonitoring, in unklaren Fällen "
                   "Oberbauch-Sonographie; bei fortbestehender Unklarheit hausärztliche/"
                   "fachärztliche Abklärung empfehlen."},
    {"wenn": {"kopfschmerz": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 6.3.3 und 7.1",
     "befund": "Häufige Kopfschmerzen angegeben.",
     "konsequenz": "Zeitlichen Zusammenhang mit der DMF-Exposition erfragen (ZNS-Wirkung "
                   "möglich); bei Arbeitsplatzbezug Expositionssituation prüfen und "
                   "Biomonitoring erwägen."},
    {"wenn": {"reizung": ["atemwege", "haut", "augen"]},
     "schwere": "pruefen",
     "bereich": "Reizwirkungen",
     "quelle": "Abschnitte 6.3.2 und 8.1",
     "befund": "Reizerscheinungen an Atemwegen, Haut oder Augen bei der Arbeit.",
     "konsequenz": "Hinweis auf direkten DMF-Kontakt: Schutzmaßnahmen und PSA überprüfen, "
                   "Biomonitoring zur Expositionskontrolle durchführen. Ergeben sich "
                   "Anhaltspunkte für unzureichende Schutzmaßnahmen, Mitteilung an das "
                   "Unternehmen mit Maßnahmenvorschlag (§ 6 (4) ArbMedVV)."},
    # ── Exposition und Schutzmaßnahmen (Abschnitte 6.4, 8.1, 8.2) ─────────
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautresorption",
     "quelle": "Abschnitte 6.2, 6.4 und 8.1",
     "befund": "Direkter Hautkontakt mit flüssigem DMF angegeben.",
     "konsequenz": "Wegen sehr guter Hautresorption Biomonitoring als maßgebliches "
                   "Instrument der Expositionskontrolle durchführen (TRGS 401). Beratung zu "
                   "geeigneten Handschuhmaterialien (Sicherheitsdatenblatt, GESTIS, GISCHEM, "
                   "WINGIS) und Hygienemaßnahmen; Schutzmaßnahmen mit dem Unternehmen "
                   "abstimmen."},
    {"wenn": {"agw_einhaltung": ["ueberschritten"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "Abschnitte 2 (Pflichtvorsorge), 6.4 und 8.2",
     "befund": "Überschreitung des Arbeitsplatzgrenzwertes angegeben.",
     "konsequenz": "Pflichtvorsorge-Konstellation: Biomonitoring zur Beurteilung der inneren "
                   "Belastung durchführen (BGW nach TRGS 903 beachten); Erkenntnisse "
                   "auswerten und dem Unternehmen Schutzmaßnahmen vorschlagen; Überprüfung "
                   "der Gefährdungsbeurteilung anstoßen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"psa_handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Schutzhandschuhe werden bei möglichem DMF-Kontakt selten oder nie getragen.",
     "konsequenz": "Intensive Beratung: Wegen der hautresorptiven Eigenschaften von DMF hat "
                   "PSA besondere Bedeutung. Ursachen klären, geeignete Handschuhmaterialien "
                   "empfehlen (Sicherheitsdatenblatt, GESTIS, GISCHEM, WINGIS); reichen die "
                   "Schutzmaßnahmen nicht aus, Mitteilung an das Unternehmen (§ 6 (4) "
                   "ArbMedVV)."},
    {"wenn": {"psa_atemschutz": ["teilweise", "nie"],
              "agw_einhaltung": ["ueberschritten"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Grenzwertüberschreitung bei gleichzeitig unvollständigem Atemschutz.",
     "konsequenz": "Dem Unternehmen unverzüglich zusätzliche Schutzmaßnahmen vorschlagen "
                   "(technisch/organisatorisch vor persönlich); Beratung zum konsequenten "
                   "Tragen des Atemschutzes; Biomonitoring zur Kontrolle der inneren "
                   "Belastung."},
    {"wenn": {"psa_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 8.1",
     "befund": "Probleme mit der Schutzausrüstung angegeben.",
     "konsequenz": "Individuelle PSA-Beratung: geeignete Handschuhmaterialien und Trageweise "
                   "klären (Hinweise in Sicherheitsdatenblatt, GESTIS, GISCHEM, WINGIS); "
                   "beschädigte PSA ersetzen lassen."},
    {"wenn": {"hygiene": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Hygieneregeln werden nicht durchgehend eingehalten.",
     "konsequenz": "Beratung zu Hygienemaßnahmen: Vermeiden von Inhalation und Hautkontakt, "
                   "Händewaschen vor Pausen, Wechsel der Arbeitskleidung."},
    # ── Beratung ──────────────────────────────────────────────────────────
    {"wenn": {"alkohol_konsum": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitt 6.3.1 (Wechselwirkung mit Ethanol)",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung zur Wechselwirkung von DMF mit dem Alkoholabbau "
                   "(Flush-Syndrom, erhöhtes Leberrisiko); Leberwerte im Rahmen der "
                   "Untersuchung besonders beachten."},
    {"wenn": {"frueher_dmf": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 6.5 und 7.1 (Arbeitsanamnese)",
     "befund": "Frühere Tätigkeit mit DMF- oder Lösungsmittel-Exposition angegeben.",
     "konsequenz": "Frühere Exposition in Anamnese und Beurteilung einbeziehen; bei "
                   "Lebererkrankung mit möglichem Tätigkeitsbezug an die Berufskrankheit "
                   "Nr. 1316 (Erkrankungen der Leber durch DMF) denken."},
    {"wenn": {"vorsorge_anlass": ["unbekannt"]},
     "schwere": "hinweis",
     "bereich": "Vorsorgeanlass",
     "quelle": "Abschnitt 2 (Anwendungsbereich)",
     "befund": "Anlass der Vorsorge ist der Person nicht bekannt.",
     "konsequenz": "Anlass der Vorstellung vor der Vorsorge mit dem Unternehmen klären "
                   "(Pflicht-, Angebots- oder Wunschvorsorge) und in der Eingangsberatung "
                   "erläutern."},
]
