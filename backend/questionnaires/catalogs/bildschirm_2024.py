# -*- coding: utf-8 -*-
"""Tätigkeiten an Bildschirmgeräten – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen
für arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024, Kapitel
»Tätigkeiten an Bildschirmgeräten« (E TBS, Fassung Januar 2022), S. 1014–1034."""

SLUG = "bildschirm-2024"

CATALOG = {
    "version": 2,
    "title": "Tätigkeiten an Bildschirmgeräten (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Tätigkeiten an Bildschirmgeräten« (E TBS, Fassung "
             "Januar 2022), S. 1014–1034",
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
                             "Bildschirmarbeit?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur "
                                                      "Bildschirm-Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Bei Tätigkeiten an Bildschirmgeräten gibt es keine Pflichtvorsorge. "
                            "Ihr Betrieb muss Ihnen die Vorsorge anbieten (Angebotsvorsorge). "
                            "Zusätzlich können Sie die Vorsorge selbst wünschen (Wunschvorsorge), "
                            "z. B. bei Beschwerden durch Arbeit mit mobilen Geräten.",
                    "required": True,
                    "options": [
                        {"value": "angebot", "label": "Vom Betrieb angeboten (Angebotsvorsorge)"},
                        {"value": "wunsch", "label": "Auf meinen eigenen Wunsch (Wunschvorsorge)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "gesundheit_veraendert",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Gesundheitszustand seit der letzten Vorsorge "
                             "verändert?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere"]},
                    "followup": {"id": "gesundheit_veraendert_desc", "type": "textarea",
                                 "label": "Was hat sich verändert?", "when": "yes"},
                },
                {
                    "id": "arbeitsplatz_veraendert",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Arbeitsplatz oder Ihre Aufgabe seit der letzten "
                             "Vorsorge verändert (z. B. neue Geräte, neue Software, anderer "
                             "Arbeitsort)?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere"]},
                    "followup": {"id": "arbeitsplatz_veraendert_desc", "type": "text",
                                 "label": "Was hat sich verändert?", "when": "yes"},
                },
                {
                    "id": "massnahmen_frueher",
                    "type": "choice",
                    "label": "Wurden nach einer früheren Vorsorge Maßnahmen umgesetzt "
                             "(z. B. Bildschirmbrille, ergonomische Anpassungen) – und "
                             "helfen sie Ihnen?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere"]},
                    "options": [
                        {"value": "keine", "label": "Es gab keine Maßnahmen"},
                        {"value": "wirksam", "label": "Ja, sie helfen mir"},
                        {"value": "unwirksam", "label": "Ja, aber sie helfen nicht oder "
                                                        "nur wenig"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Bildschirmarbeit ─────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Bildschirmarbeit",
            "subtitle": "Ihre Arbeit am Bildschirm",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "bildschirm_dauer",
                    "type": "choice",
                    "label": "Wie viele Stunden arbeiten Sie an einem normalen Arbeitstag "
                             "am Bildschirm?",
                    "required": True,
                    "options": [
                        {"value": "unter2", "label": "Weniger als 2 Stunden"},
                        {"value": "2bis4", "label": "2 bis 4 Stunden"},
                        {"value": "4bis6", "label": "4 bis 6 Stunden"},
                        {"value": "ueber6", "label": "Mehr als 6 Stunden"},
                    ],
                },
                {
                    "id": "unterbrechungen",
                    "type": "yes_no",
                    "label": "Können Sie die Bildschirmarbeit regelmäßig durch andere "
                             "Aufgaben oder kurze Pausen unterbrechen?",
                    "hint": "Gemeint ist, ob Sie Arbeitsablauf und Pausen selbst "
                            "beeinflussen können.",
                    "required": True,
                },
                {
                    "id": "geraete",
                    "type": "multi_choice",
                    "label": "Mit welchen Geräten arbeiten Sie? (Mehrfachauswahl möglich)",
                    "required": True,
                    "options": [
                        {"value": "monitor", "label": "Fester Arbeitsplatz mit einem Bildschirm"},
                        {"value": "mehrere", "label": "Mehrere Bildschirme gleichzeitig"},
                        {"value": "notebook", "label": "Notebook/Laptop"},
                        {"value": "mobil", "label": "Tablet oder Smartphone (mobile Geräte)"},
                        {"value": "sonstige", "label": "Andere Geräte"},
                    ],
                },
                {
                    "id": "taetigkeit_art",
                    "type": "multi_choice",
                    "label": "Welche Beschreibung passt zu Ihrer Bildschirmarbeit? "
                             "(Mehrfachauswahl möglich)",
                    "required": True,
                    "options": [
                        {"value": "dateneingabe", "label": "Schnelle, immer gleiche Dateneingabe "
                                                           "oder -erfassung"},
                        {"value": "cad", "label": "CAD/CAM, Bildverarbeitung oder Grafik"},
                        {"value": "ueberwachung", "label": "Video-, Verkehrs- oder "
                                                           "Prozessüberwachung"},
                        {"value": "telefon", "label": "Arbeit am Servicetelefon/Callcenter"},
                        {"value": "sachbearbeitung", "label": "Sachbearbeitung/Büroarbeit"},
                        {"value": "andere", "label": "Andere Tätigkeit"},
                    ],
                },
                {
                    "id": "eingabe_repetitiv",
                    "type": "yes_no",
                    "label": "Geben Sie mehr als 3 Stunden am Tag fast ununterbrochen und "
                             "sehr schnell Daten über die Tastatur ein (z. B. Schreibdienst, "
                             "Datenerfassung)?",
                    "hint": "Gemeint sind sehr schnelle, immer gleiche Tastatureingaben. "
                            "Normales Schreiben oder Arbeit mit der Maus zählt nicht dazu.",
                    "required": True,
                },
                {
                    "id": "einweisung",
                    "type": "yes_no",
                    "label": "Wurden Sie in die richtige Einstellung Ihres Arbeitsplatzes "
                             "eingewiesen (Stuhl, Tisch, Bildschirm)?",
                    "required": True,
                },
                {
                    "id": "ergonomie_probleme",
                    "type": "yes_no",
                    "label": "Gibt es an Ihrem Arbeitsplatz ergonomische Probleme (z. B. zu "
                             "kleine Schrift, Spiegelungen, schlecht einstellbarer Stuhl oder "
                             "Tisch, unpraktische Software, langsame Datenverbindung)?",
                    "required": True,
                    "followup": {"id": "ergonomie_probleme_desc", "type": "textarea",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Sehen und Augen ────────────────────────────────────────────
        {
            "id": "sehen",
            "title": "Sehen & Augen",
            "subtitle": "Ihr Sehvermögen und Beschwerden an den Augen",
            "questions": [
                {
                    "id": "sehhilfe",
                    "type": "choice",
                    "label": "Tragen Sie eine Brille oder Kontaktlinsen?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Nein"},
                        {"value": "ferne", "label": "Ja, Brille oder Kontaktlinsen für "
                                                    "die Ferne"},
                        {"value": "lese", "label": "Ja, eine Lesebrille (Alterssichtigkeit)"},
                        {"value": "gleitsicht", "label": "Ja, eine Gleitsicht- oder "
                                                         "Bifokalbrille"},
                        {"value": "bildschirmbrille", "label": "Ja, eine spezielle "
                                                               "Bildschirmbrille"},
                    ],
                },
                {
                    "id": "gleitsicht_haltung",
                    "type": "yes_no",
                    "label": "Müssen Sie am Bildschirm den Kopf heben oder in den Nacken "
                             "legen, um durch den richtigen Brillenbereich scharf zu sehen?",
                    "required": True,
                    "show_if": {"id": "sehhilfe", "in": ["gleitsicht"]},
                },
                {
                    "id": "sehen_unscharf",
                    "type": "yes_no",
                    "label": "Haben Sie Schwierigkeiten, Texte oder Zeichen am Bildschirm "
                             "scharf zu erkennen – auch mit Ihrer Brille oder Ihren "
                             "Kontaktlinsen?",
                    "required": True,
                },
                {
                    "id": "augen_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach Bildschirmarbeit Beschwerden an den "
                             "Augen oder Kopfschmerzen?",
                    "required": True,
                },
                {
                    "id": "augen_symptome",
                    "type": "multi_choice",
                    "label": "Welche Beschwerden haben Sie? (Mehrfachauswahl möglich)",
                    "required": True,
                    "show_if": {"id": "augen_beschwerden", "in": ["yes"]},
                    "options": [
                        {"value": "brennen", "label": "Brennende, müde oder tränende Augen"},
                        {"value": "trocken", "label": "Trockenheitsgefühl, Rötung oder "
                                                      "Fremdkörpergefühl im Auge"},
                        {"value": "kopfschmerz", "label": "Kopfschmerzen"},
                        {"value": "flimmern", "label": "Flimmern oder verschwommenes Sehen"},
                        {"value": "doppel", "label": "Doppelbilder"},
                        {"value": "andere", "label": "Andere Beschwerden"},
                    ],
                },
                {
                    "id": "beschwerden_zunahme",
                    "type": "yes_no",
                    "label": "Nehmen diese Beschwerden zu, je länger Sie am Bildschirm "
                             "arbeiten?",
                    "required": True,
                    "show_if": {"id": "augen_beschwerden", "in": ["yes"]},
                },
                {
                    "id": "augenerkrankung",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Augenerkrankung bekannt (z. B. Grauer oder "
                             "Grüner Star, Netzhauterkrankung, Schielen oder verstecktes "
                             "Schielen)?",
                    "required": True,
                    "followup": {"id": "augenerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "sehbehinderung",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen eine erhebliche Sehbehinderung, Blindheit "
                             "oder Einäugigkeit (Sehen nur mit einem Auge)?",
                    "required": True,
                },
                {
                    "id": "farbsehen",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Farbsehschwäche bekannt (z. B. "
                             "Rot-Grün-Schwäche)?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Bewegungsapparat ───────────────────────────────────────────
        {
            "id": "bewegungsapparat",
            "title": "Muskeln & Gelenke",
            "subtitle": "Beschwerden am Bewegungsapparat",
            "questions": [
                {
                    "id": "msk_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach der Arbeit Beschwerden an Muskeln, "
                             "Gelenken oder der Wirbelsäule?",
                    "required": True,
                },
                {
                    "id": "msk_regionen",
                    "type": "multi_choice",
                    "label": "Wo haben Sie Beschwerden? (Mehrfachauswahl möglich)",
                    "required": True,
                    "show_if": {"id": "msk_beschwerden", "in": ["yes"]},
                    "options": [
                        {"value": "nacken", "label": "Nacken/Halswirbelsäule"},
                        {"value": "schulter", "label": "Schultern"},
                        {"value": "unterarm", "label": "Unterarme, Handgelenke oder Hände"},
                        {"value": "ruecken", "label": "Unterer Rücken/Lendenwirbelsäule"},
                        {"value": "andere", "label": "Andere Körperregion"},
                    ],
                },
                {
                    "id": "msk_frueher",
                    "type": "yes_no",
                    "label": "Hatten Sie ähnliche Beschwerden schon früher, vor Ihrer "
                             "jetzigen Tätigkeit?",
                    "required": True,
                },
                {
                    "id": "sehnenscheiden",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Sehnenscheidenentzündung, ein "
                             "»Tennisarm« oder ein Karpaltunnelsyndrom (Nervenengpass am "
                             "Handgelenk) festgestellt?",
                    "required": True,
                    "followup": {"id": "sehnenscheiden_desc", "type": "text",
                                 "label": "Was wurde festgestellt, und wann?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Allgemeine Gesundheit ──────────────────────────────────────
        {
            "id": "gesundheit",
            "title": "Allgemeine Gesundheit",
            "subtitle": "Vorerkrankungen und Medikamente",
            "questions": [
                {
                    "id": "med_dauer",
                    "type": "yes_no",
                    "label": "Nehmen Sie dauerhaft Medikamente ein?",
                    "required": True,
                    "followup": {"id": "med_dauer_desc", "type": "text",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
                {
                    "id": "stoffwechsel",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Stoffwechselerkrankung bekannt (z. B. "
                             "Diabetes/Zuckerkrankheit, Schilddrüsenerkrankung)?",
                    "required": True,
                    "followup": {"id": "stoffwechsel_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "blutdruck",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen Bluthochdruck bekannt?",
                    "required": True,
                },
                {
                    "id": "neuro",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine neurologische Erkrankung bekannt "
                             "(Erkrankung des Nervensystems, z. B. Migräne, Epilepsie, "
                             "Lähmungen)?",
                    "required": True,
                    "followup": {"id": "neuro_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "psych",
                    "type": "yes_no",
                    "label": "Sind bei Ihnen psychische Erkrankungen bekannt oder in "
                             "Behandlung (z. B. Depression, Angststörung)?",
                    "required": True,
                    "followup": {"id": "psych_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "psych_belastung",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich durch Ihre Bildschirmarbeit psychisch stark "
                             "belastet (z. B. Termin- und Leistungsdruck, viele Aufgaben "
                             "gleichzeitig, eintönige Arbeit, ständige Erreichbarkeit)?",
                    "required": True,
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
    # ── Sehvermögen: Untersuchung der Augen (Abschnitte 7.2.2, 7.4) ───────
    {"wenn": {"sehen_unscharf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 7.2.2 und 7.4; AMR 14.1",
     "befund": "Schwierigkeiten, Zeichen am Bildschirm scharf zu erkennen (auch mit Sehhilfe).",
     "konsequenz": "Angemessene Untersuchung der Augen und des Sehvermögens durchführen: "
                   "Sehschärfe Ferne, Nähe und bildschirmarbeitsplatzbezogen (jeweils mit "
                   "Sehhilfe), Phorie, zentrales Gesichtsfeld, Farbensinn (Verfahren nach "
                   "DIN 58220 Teil 5). Bei Auffälligkeiten Maßnahmen zur Verbesserung der "
                   "Sehschärfe; erweist sich eine augenärztliche Untersuchung als "
                   "erforderlich, ist diese zu ermöglichen."},
    {"wenn": {"augen_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Asthenopische Beschwerden",
     "quelle": "Abschnitte 6.4 und 7.2.2",
     "befund": "Augenbeschwerden oder Kopfschmerzen bei bzw. nach Bildschirmarbeit.",
     "konsequenz": "Abklärung asthenopischer Beschwerden: Sehtest anbieten (Sehschärfe, "
                   "Phorie), Korrekturbedarf und Sehabstände am Arbeitsplatz prüfen, "
                   "Indikation für eine spezielle Sehhilfe (Bildschirmbrille) prüfen. "
                   "§ 5 Abs. 2 ArbMedVV gilt entsprechend für Sehbeschwerden: bei Bedarf "
                   "augenärztliche Untersuchung ermöglichen."},
    {"wenn": {"beschwerden_zunahme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Asthenopische Beschwerden",
     "quelle": "Abschnitt 6.4",
     "befund": "Beschwerden nehmen mit der Dauer der Bildschirmarbeit zu.",
     "konsequenz": "Zunahme nach mehrstündiger Bildschirmarbeit ist typisch für nicht oder "
                   "unzureichend korrigierte Fehlsichtigkeit oder latente/manifeste "
                   "Schielfehler (Eso-/Exophorie): Phorie-Prüfung und Refraktionskontrolle "
                   "gezielt veranlassen."},
    {"wenn": {"augen_symptome": ["trocken"]},
     "schwere": "pruefen",
     "bereich": "Trockenes Auge",
     "quelle": "Abschnitt 6.4 (Trockenes Auge)",
     "befund": "Trockenheitsgefühl, Rötung oder Fremdkörpergefühl der Augen angegeben.",
     "konsequenz": "Hinweis auf Keratokonjunktivitis sicca (»Trockenes Auge«): Beratung zu "
                   "bewussten Lidschlägen, Bildschirmpausen und Raumluftbefeuchtung; "
                   "Medikamente, hormonelle Störungen und Autoimmun-/Systemerkrankungen "
                   "als Ursache prüfen; bei anhaltenden Beschwerden augenärztliche "
                   "Abklärung ermöglichen."},
    {"wenn": {"gleitsicht_haltung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Spezielle Sehhilfe",
     "quelle": "Abschnitt 6.4 (Spezielle Sehhilfe/Bildschirmbrille)",
     "befund": "Zwangshaltung (Kopf heben/Nacken überstrecken) bei Gleitsichtbrille am "
               "Bildschirm.",
     "konsequenz": "Indikation für eine spezielle Sehhilfe (Bildschirmbrille): Korrektur an "
                   "die konkreten Sehabstände (Bildschirm, Tastatur, Schriftstücke; "
                   "Nahbereich bis 80 cm bzw. 200 cm) anpassen lassen. Sind normale "
                   "Sehhilfen nicht geeignet, muss der Arbeitgeber die spezielle Sehhilfe "
                   "im erforderlichen Umfang zur Verfügung stellen."},
    {"wenn": {"sehhilfe": ["lese", "gleitsicht"]},
     "schwere": "hinweis",
     "bereich": "Presbyopie",
     "quelle": "Abschnitte 6.4 und 7.1 (Allgemeine Anamnese: Presbyopie)",
     "befund": "Alterssichtigkeit (Lese-/Gleitsichtkorrektur) angegeben.",
     "konsequenz": "Gebrauchsakkommodation für den Bildschirmabstand prüfen: bei "
                   "fortgeschrittener Reduktion der Akkommodation (unter 2 Dioptrien) "
                   "Indikation für eine Bildschirmbrille; Beratung zur Auswahl geeigneter "
                   "Gläser (DGUV Information 250-008)."},
    {"wenn": {"augenerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augenerkrankung",
     "quelle": "Abschnitte 7.4 und 7.4.3",
     "befund": "Bekannte Augenerkrankung angegeben.",
     "konsequenz": "Augenärztliche Vorbefunde einbeziehen; klinische Untersuchung nach "
                   "Abschnitt 7.2.2 durchführen. Ist eine Änderung des Schweregrads der "
                   "Erkrankung zu erwarten, verkürzte Vorsorgefrist nach 7.4.3 empfehlen."},
    {"wenn": {"sehbehinderung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehbehinderung/Blindheit",
     "quelle": "Abschnitte 6.4 (Behinderung) und 7.4.2",
     "befund": "Erhebliche Sehbehinderung, Blindheit oder Einäugigkeit angegeben.",
     "konsequenz": "Tätigkeit ist in der Regel mit geeigneten Hilfsmitteln ausführbar: "
                   "Kompensation prüfen (Lupen-, Vorlese- und Diktierfunktion, "
                   "Braillezeile, alternative Eingabemittel). Arbeitsplatz in enger "
                   "Zusammenarbeit mit Berufsförderungswerken, Integrations-/"
                   "Inklusionsämtern oder Zentren für blinde und sehbehinderte Personen "
                   "einrichten; Fachberatung veranlassen."},
    {"wenn": {"farbsehen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Farbensinn",
     "quelle": "Abschnitt 7.2.2",
     "befund": "Bekannte Farbsehschwäche angegeben.",
     "konsequenz": "Farbensinnprüfung (Farbtafeln z. B. nach Ishihara oder Testgeräte) und "
                   "Abgleich mit der Arbeitsaufgabe (farbcodierte Darstellungen); ggf. "
                   "Software-Einstellungen (Farbschemata, Kontraste) anpassen lassen."},
    # ── Bewegungsapparat (Abschnitte 6.4, 6.5, 7.4.2) ─────────────────────
    {"wenn": {"msk_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bewegungsapparat",
     "quelle": "Abschnitte 6.4 und 7.4.2",
     "befund": "Beschwerden an Muskeln, Gelenken oder Wirbelsäule bei bzw. nach der Arbeit.",
     "konsequenz": "Ergonomie des Arbeitsplatzes prüfen (Höheneinstellung des Arbeitsstuhls, "
                   "dynamisches Sitzen, Begrenzung des Sitzneigungswinkels auf ca. 8°); "
                   "Beratung zu Bewegungsförderung und Training der stabilisierenden "
                   "Rumpfmuskulatur; unzureichendes Sehvermögen als Mitursache "
                   "(Ausgleichsbewegungen, Fehlhaltung) mitprüfen. Dem Unternehmen ggf. "
                   "technische Anpassungen oder organisatorische Maßnahmen vorschlagen."},
    {"wenn": {"msk_frueher": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Bewegungsapparat",
     "quelle": "Abschnitte 6.4 und 7.4.3",
     "befund": "Gleichartige Beschwerden bereits vor Aufnahme der Tätigkeit.",
     "konsequenz": "Gleichartige Beschwerden in der Anamnese sind der größte Risikofaktor "
                   "(v. a. Halswirbelsäule, meiste Beschwerden im ersten Monat nach "
                   "Tätigkeitsaufnahme): frühzeitige ergonomische Beratung; bei zu "
                   "erwartender Änderung des Schweregrads verkürzte Vorsorgefrist nach "
                   "7.4.3 erwägen."},
    {"wenn": {"sehnenscheiden": ["yes"], "eingabe_repetitiv": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitt 6.5 (BK-Nr. 2101)",
     "befund": "Sehnenscheiden-/Sehnenansatzerkrankung bzw. Karpaltunnelsyndrom bei "
               "hochrepetitiver Eingabetätigkeit über 3 Stunden täglich.",
     "konsequenz": "Berufskrankheiten-Verdacht prüfen (BK-Nr. 2101, Erkrankungen der "
                   "Sehnenscheiden): relevant sind kurzzyklische, repetitive Tätigkeiten "
                   "mit mindestens 10 000 Bewegungsabläufen pro Stunde bzw. 3 pro Sekunde "
                   "über mehr als 3 Stunden pro Tag (z. B. Datenerfassung, Schreibdienst). "
                   "Ggf. ärztliche BK-Anzeige erstatten; Belastungszeit begrenzen und "
                   "alternative Eingabemittel vorschlagen."},
    {"wenn": {"sehnenscheiden": ["yes"]},
     "wenn_nicht": {"eingabe_repetitiv": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bewegungsapparat",
     "quelle": "Abschnitte 6.4, 6.5 und 7.4.2",
     "befund": "Sehnenscheiden-/Sehnenansatzerkrankung bzw. Karpaltunnelsyndrom ohne "
               "hochrepetitive Eingabetätigkeit.",
     "konsequenz": "Abklärung und Behandlung sicherstellen; nach Abschnitt 6.5 stellen "
                   "Mausbedienung und Sachbearbeitung keine BK-Gefährdung dar. Maßnahmen "
                   "nach 7.4.2 prüfen: alternative Eingabemittel, ergonomische Anpassung "
                   "der Arbeitsmittel."},
    # ── Psychische Belastung, Organisation (Abschnitte 6.4, 8.2) ──────────
    {"wenn": {"psych_belastung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Psychische Belastung",
     "quelle": "Abschnitte 6.4 und 8.2",
     "befund": "Starke psychische Belastung durch die Bildschirmarbeit angegeben.",
     "konsequenz": "Beratung zu Arbeitsaufgabe und Arbeitsorganisation (Termin- und "
                   "Leistungsdruck, Multitasking, Monotonie). Ergeben sich Anhaltspunkte, "
                   "dass die Arbeitsschutzmaßnahmen nicht ausreichen, Mitteilung an das "
                   "Unternehmen mit Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV) und "
                   "Überprüfung der Gefährdungsbeurteilung psychischer Belastung anregen."},
    {"wenn": {"ergonomie_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Ergonomie",
     "quelle": "Abschnitte 6.1.1 und 8",
     "befund": "Ergonomische Probleme am Bildschirmarbeitsplatz angegeben.",
     "konsequenz": "Beratung zur individuellen Arbeitsplatzergonomie (DGUV Information "
                   "215-410 »Bildschirm- und Büroarbeitsplätze«); dem Unternehmen "
                   "technische Anpassungen der Arbeitsmittel vorschlagen."},
    {"wenn": {"bildschirm_dauer": ["ueber6"], "unterbrechungen": ["no"]},
     "schwere": "hinweis",
     "bereich": "Belastungsprofil",
     "quelle": "Abschnitte 6.1.1 und 7.4.2",
     "befund": "Sehr lange tägliche Bildschirmarbeit ohne regelmäßige Unterbrechungen.",
     "konsequenz": "Tätigkeit mit höherer Belastung (lange Dauer, geringe Autonomie): "
                   "organisatorische Maßnahmen empfehlen (Begrenzung der Belastungszeit, "
                   "Mischarbeit, Kurzpausen); Beratung zur Prävention asthenopischer "
                   "Beschwerden und zur Bewegungsförderung."},
    {"wenn": {"einweisung": ["no"]},
     "schwere": "hinweis",
     "bereich": "Arbeitseinweisung",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese)",
     "befund": "Keine Einweisung in die ergonomische Einstellung des Arbeitsplatzes erfolgt.",
     "konsequenz": "Einweisung in die richtige Einstellung von Stuhl, Tisch und Bildschirm "
                   "veranlassen; dem Unternehmen die Unterweisung als Maßnahme vorschlagen."},
    # ── Allgemeine Gesundheit (Abschnitt 7.4) ─────────────────────────────
    {"wenn": {"stoffwechsel": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechselerkrankung",
     "quelle": "Abschnitte 7.4 und 7.4.3",
     "befund": "Stoffwechselerkrankung (z. B. Diabetes) angegeben.",
     "konsequenz": "Bei der Beurteilung berücksichtigen (mögliche Auswirkungen auf das "
                   "Sehvermögen, z. B. diabetische Retinopathie); Behandlungsstand klären. "
                   "Ist eine Änderung des Schweregrads zu erwarten, verkürzte "
                   "Vorsorgefrist nach 7.4.3 empfehlen."},
    {"wenn": {"med_dauer": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Medikamente",
     "quelle": "Abschnitte 7.1 und 7.4",
     "befund": "Dauerbehandlung mit Medikamenten angegeben.",
     "konsequenz": "Wirkungen der Medikamente bei der Beurteilung berücksichtigen "
                   "(u. a. Einfluss auf Tränenfilm/Trockenes Auge und Akkommodation); "
                   "Medikamentenanamnese ärztlich vertiefen."},
    {"wenn": {"massnahmen_frueher": ["unwirksam"]},
     "schwere": "pruefen",
     "bereich": "Wirksamkeit von Maßnahmen",
     "quelle": "Abschnitte 7.1 (weitere Vorsorgen), 7.4.2 und 7.4.4",
     "befund": "Früher veranlasste arbeitsplatzbezogene Maßnahmen sind nicht oder kaum "
               "wirksam.",
     "konsequenz": "Maßnahmen überprüfen und anpassen (technisch, organisatorisch, "
                   "individuell nach 7.4.2; ggf. verkürzte Frist nach 7.4.3). Sind die "
                   "Maßnahmen nicht erfolgreich, Tätigkeitswechsel erwägen (7.4.4); die "
                   "Mitteilung an den Arbeitgeber bedarf der Einwilligung der "
                   "beschäftigten Person (§ 6 (4) ArbMedVV)."},
]
