# -*- coding: utf-8 -*-
"""G 13 Chloroplatinate – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 13 »Chloroplatinate«
(Fassung Oktober 2014), S. 235–249."""

SLUG = "g13-platin-2016"

CATALOG = {
    "version": 2,
    "title": "G 13 Chloroplatinate (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 13 »Chloroplatinate« (Fassung Oktober 2014), S. 235–249",
    "sections": [
        # ── 1 ─ Anlass der Untersuchung (Abschnitt 1.1) ────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Welche Untersuchung steht bei Ihnen an?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachuntersuchung: "
                            "erste nach 3 Monaten, weitere nach 6 bis 12 Monaten – Platinsalze "
                            "können schon nach wenigen Tagen eine Allergie auslösen.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nachuntersuchung", "label": "Nachuntersuchung"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie mit Chloroplatinaten (Platinsalzen)?",
                    "required": True,
                    "options": [
                        {"value": "noch_nicht", "label": "Noch gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter3m", "label": "Weniger als 3 Monate"},
                        {"value": "3bis12m", "label": "3 bis 12 Monate"},
                        {"value": "ueber1j", "label": "Mehr als 1 Jahr"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nachuntersuchung"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nachuntersuchung"]},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition (Abschnitt 3.1.1) ─────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kontakt mit Chloroplatinaten",
            "subtitle": "Ihre Arbeit und der mögliche Kontakt mit Platinsalzen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "arbeitsbereich",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie (oder sollen Sie arbeiten)?",
                    "hint": "Mehrfachauswahl möglich. In diesen Bereichen ist mit Chloroplatinaten "
                            "(chlorhaltigen Platinsalzen) zu rechnen.",
                    "required": True,
                    "options": [
                        {"value": "scheiderei", "label": "Edelmetallscheiderei (Trennen und Aufbereiten von Edelmetallen)"},
                        {"value": "katalysator", "label": "Herstellung von platinhaltigen Katalysatoren"},
                        {"value": "zytostatika", "label": "Herstellung von platinhaltigen Krebsmedikamenten (Zytostatika)"},
                        {"value": "andere_verbindungen", "label": "Herstellung anderer platinhaltiger Verbindungen"},
                        {"value": "galvanik", "label": "Galvanikbetrieb (elektrochemische Beschichtung)"},
                        {"value": "service", "label": "Handwerks-, Reinigungs- oder Laborarbeiten in solchen Bereichen"},
                        {"value": "anderes", "label": "Anderer Bereich / keiner davon"},
                    ],
                },
                {
                    "id": "direkter_kontakt",
                    "type": "yes_no",
                    "label": "Haben Sie bei Ihrer Arbeit direkten Umgang mit Chloroplatinaten "
                             "(z. B. mit Pulvern, Lösungen oder Stäuben)?",
                    "required": True,
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit mit diesen Stoffen in Berührung "
                             "(z. B. durch Spritzer, Staub oder verschmutzte Oberflächen)?",
                    "required": True,
                },
                {
                    "id": "frueher_exposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten schon einmal Kontakt mit "
                             "Chloroplatinaten (Platinsalzen)?",
                    "required": True,
                    "followup": {"id": "frueher_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen (Standardfragebogen II, Abschnitt 2.2) ─────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Wie Sie sich bei der Arbeit schützen",
            "questions": [
                {
                    "id": "psa",
                    "type": "choice",
                    "label": "Tragen Sie beim Umgang mit diesen Stoffen die vorgesehene "
                             "persönliche Schutzausrüstung (z. B. Atemschutz, Schutzhandschuhe, "
                             "Schutzbrille)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "keine_vorgesehen", "label": "Es ist keine Schutzausrüstung vorgesehen / "
                                                               "ich habe (noch) keinen Umgang"},
                    ],
                },
                {
                    "id": "informiert",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich über die Schutzmaßnahmen an Ihrem Arbeitsplatz "
                             "gut informiert?",
                    "required": True,
                },
                {
                    "id": "geschuetzt",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich durch die Schutzmaßnahmen gut geschützt?",
                    "required": True,
                    "followup": {"id": "geschuetzt_verbesserung", "type": "text",
                                 "label": "Was würden Sie verbessern?", "when": "no"},
                },
            ],
        },
        # ── 4 ─ Beschwerden (Standardfragebogen II) ────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden bei der Arbeit",
            "subtitle": "Beschwerden an Atemwegen, Augen oder Haut",
            "questions": [
                {
                    "id": "arbeitsbezogene_beschwerden",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Beschwerden der Nase, der Haut, der Lungen "
                             "oder der Atemwege, die vermehrt bei der Arbeit auftreten?",
                    "required": True,
                    "followup": {"id": "arbeitsbezogene_beschwerden_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, seit wann, und worin vermuten Sie "
                                          "die Ursache?", "when": "yes"},
                },
                {
                    "id": "symptome",
                    "type": "multi_choice",
                    "label": "Welche Beschwerden sind das?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "arbeitsbezogene_beschwerden", "in": ["yes"]},
                    "options": [
                        {"value": "fliessschnupfen", "label": "Niesanfälle, eine laufende oder juckende Nase (Fließschnupfen)"},
                        {"value": "husten", "label": "Wiederholter Husten"},
                        {"value": "pfeifen", "label": "Pfeifendes oder giemendes Geräusch im Brustkorb"},
                        {"value": "kurzatmigkeit", "label": "Anfälle von Kurzatmigkeit unter Belastung"},
                        {"value": "engegefuehl", "label": "Engegefühl im Brustkorb"},
                        {"value": "augen", "label": "Juckreiz oder Brennen an Augen oder Gehörgängen, Augentränen"},
                        {"value": "quaddeln", "label": "Juckende Quaddeln auf der Haut nach direktem Kontakt "
                                                       "(Nesselausschlag)"},
                        {"value": "ausschlag", "label": "Andere Hautausschläge"},
                        {"value": "sonstiges", "label": "Andere Beschwerden"},
                    ],
                },
                {
                    "id": "besserung_frei",
                    "type": "choice",
                    "label": "Bessern sich diese Beschwerden im Urlaub oder an freien Tagen?",
                    "required": True,
                    "show_if": {"id": "arbeitsbezogene_beschwerden", "in": ["yes"]},
                    "options": [
                        {"value": "ja", "label": "Ja, deutlich"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unklar", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "au_beschwerden",
                    "type": "yes_no",
                    "label": "Waren Sie wegen dieser Beschwerden schon einmal arbeitsunfähig "
                             "(krankgeschrieben)?",
                    "required": True,
                    "show_if": {"id": "arbeitsbezogene_beschwerden", "in": ["yes"]},
                },
            ],
        },
        # ── 5 ─ Allergien (Standardfragebogen I) ───────────────────────────
        {
            "id": "allergie",
            "title": "Allergien",
            "subtitle": "Allergische Erkrankungen bei Ihnen und in Ihrer Familie",
            "questions": [
                {
                    "id": "atopie_kind",
                    "type": "yes_no",
                    "label": "Hatten Sie als Kind Milchschorf oder Neurodermitis "
                             "(juckende, schuppende Hautausschläge)?",
                    "required": True,
                },
                {
                    "id": "allergie_familie",
                    "type": "yes_no",
                    "label": "Sind in Ihrer Familie Allergien bekannt?",
                    "required": True,
                },
                {
                    "id": "heuschnupfen",
                    "type": "yes_no",
                    "label": "Haben Sie Heuschnupfen?",
                    "required": True,
                },
                {
                    "id": "andere_allergien",
                    "type": "yes_no",
                    "label": "Haben Sie andere allergische Beschwerden (z. B. gegen Tiere, "
                             "Hausstaub, Lebensmittel)?",
                    "required": True,
                    "followup": {"id": "andere_allergien_desc", "type": "text",
                                 "label": "Welche?", "when": "yes"},
                },
                {
                    "id": "allergietest",
                    "type": "yes_no",
                    "label": "Sind Sie schon einmal wegen einer Allergie getestet worden "
                             "(z. B. Hauttest, Bluttest)?",
                    "required": True,
                    "followup": {"id": "allergietest_desc", "type": "text",
                                 "label": "Wann, worauf, und mit welchem Ergebnis?", "when": "yes"},
                },
                {
                    "id": "unspez_reize",
                    "type": "yes_no",
                    "label": "Bekommen Sie Husten oder Atemnot bei Kontakt mit Deospray, "
                             "Parfüm, Kochgerüchen oder Zigarettenrauch?",
                    "hint": "Das kann ein Hinweis auf überempfindliche Atemwege sein "
                            "(bronchiale Hyperreagibilität).",
                    "required": True,
                },
                {
                    "id": "fruehere_firma",
                    "type": "yes_no",
                    "label": "Hatten Sie in einer früheren Firma Beschwerden der Nase, der Haut, "
                             "der Lungen oder der Atemwege, die vermehrt bei der Arbeit auftraten?",
                    "required": True,
                    "followup": {"id": "fruehere_firma_desc", "type": "textarea",
                                 "label": "Welche Beschwerden? Waren Sie deswegen in ärztlicher "
                                          "Behandlung oder arbeitsunfähig?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Gesundheit & besondere Angaben ─────────────────────────────
        {
            "id": "gesundheit",
            "title": "Vorerkrankungen & besondere Angaben",
            "subtitle": "Erkrankungen und Angaben, die für Untersuchung und Biomonitoring wichtig sind",
            "questions": [
                {
                    "id": "asthma",
                    "type": "yes_no",
                    "label": "Haben Sie Asthma bronchiale oder eine andere chronische "
                             "Atemwegserkrankung mit Beschwerden (z. B. COPD)?",
                    "required": True,
                },
                {
                    "id": "lungenerkrankung",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine erhebliche Lungenerkrankung bekannt, z. B. eine "
                             "fortgeschrittene Lungengerüsterkrankung (Lungenfibrose) oder ein "
                             "Lungenemphysem (überblähte Lunge)?",
                    "required": True,
                },
                {
                    "id": "platin_sensibilisierung",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen schon einmal eine Allergie oder Sensibilisierung "
                             "gegenüber Platinsalzen festgestellt (z. B. ein positiver "
                             "Pricktest/Hauttest)?",
                    "required": True,
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie Medikamente ein?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "text",
                                 "label": "Welche?", "when": "yes"},
                },
                {
                    "id": "platin_medikamente",
                    "type": "yes_no",
                    "label": "Wurden Sie schon einmal mit platinhaltigen Medikamenten behandelt "
                             "(z. B. Chemotherapie mit Cisplatin oder Carboplatin)?",
                    "hint": "Das ist wichtig, weil solche Behandlungen den Platinwert im Urin "
                            "(Biomonitoring) erhöhen können.",
                    "required": True,
                },
                {
                    "id": "zahnersatz",
                    "type": "yes_no",
                    "label": "Haben Sie edelmetallhaltigen Zahnersatz, z. B. Inlays, Kronen "
                             "oder Brücken?",
                    "hint": "Zahngold (Dentalgold) kann Platin enthalten und den Platinwert "
                            "im Urin (Biomonitoring) beeinflussen.",
                    "required": True,
                },
            ],
        },
        # ── 7 ─ Rauchen (Standardfragebogen II, Abschnitt 2.2) ─────────────
        {
            "id": "rauchen_sektion",
            "title": "Rauchen",
            "subtitle": "Rauchen belastet die Lunge zusätzlich",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "frueher", "label": "Nein, aber früher habe ich geraucht"},
                        {"value": "aktuell", "label": "Ja"},
                    ],
                    "followup": {"id": "rauchen_seit", "type": "text",
                                 "label": "Seit wann?", "when": "aktuell"},
                },
                {
                    "id": "rauchen_menge",
                    "type": "choice",
                    "label": "Wie viele Zigaretten rauchen Sie ungefähr pro Tag?",
                    "required": True,
                    "show_if": {"id": "rauchen", "in": ["aktuell"]},
                    "options": [
                        {"value": "unter10", "label": "Weniger als 10"},
                        {"value": "bis20", "label": "10 bis 20"},
                        {"value": "ueber20", "label": "Mehr als 20"},
                    ],
                },
            ],
        },
        # ── 8 ─ Einwilligung ───────────────────────────────────────────────
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
    {"wenn": {"asthma": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Symptomatische obstruktive Atemwegserkrankung (z. B. Asthma bronchiale) angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken gegen Aufnahme bzw. Fortsetzung der "
                   "Tätigkeit mit Chloroplatinaten erwägen; Diagnose sichern (eingehende "
                   "Untersuchung der Atemorgane, Spirometrie mit Fluss-Volumen-Kurve, "
                   "Vorbefunde einholen)."},
    {"wenn": {"lungenerkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Lungenerkrankung",
     "quelle": "Abschnitte 1.2.1 und 2.1.1",
     "befund": "Erhebliche Lungenerkrankung (fortgeschrittene Lungengerüsterkrankung/"
               "Lungenemphysem) angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1: dauernde gesundheitliche Bedenken erwägen; "
                   "Lungenfunktion prüfen, Vorbefunde einholen, ggf. fachärztliche Abklärung "
                   "vor der Beurteilung."},
    {"wenn": {"platin_sensibilisierung": ["yes"], "arbeitsbezogene_beschwerden": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Platinsalz-Sensibilisierung",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Sensibilisierung gegenüber Chloroplatinaten mit arbeitsbezogenen Beschwerden "
               "der Atemwege (symptomatisch).",
     "konsequenz": "Symptomatische Sensibilisierung der oberen und/oder unteren Atemwege ist "
                   "Bedenkenstatbestand nach 2.1.1 (dauernde gesundheitliche Bedenken); "
                   "Case-Management nach der Handlungsanleitung (DGUV Information 240-130) "
                   "einleiten; an Berufskrankheit BK-Nr. 4301 denken und Meldung prüfen."},
    # ── Befristete Bedenken bei unklarer Atemwegssymptomatik (2.1.2) ──────
    {"wenn": {"symptome": ["husten", "pfeifen", "kurzatmigkeit", "engegefuehl"]},
     "schwere": "kritisch",
     "bereich": "Atemwegssymptome",
     "quelle": "Abschnitte 2.1.2 und 1.2.3",
     "befund": "Bronchiale, arbeitsbezogene Symptome angegeben (Husten, Pfeifen/Giemen, "
               "Kurzatmigkeit oder Engegefühl im Brustkorb).",
     "konsequenz": "Unklare Atemwegssymptomatik: befristete gesundheitliche Bedenken bis zur "
                   "diagnostischen Klärung (2.1.2). Abklärung mit Pricktest und Spirometrie; "
                   "bei negativem Pricktest weitere Abklärung nach 1.2.3, spezifische "
                   "Provokationstestung nur in spezialisierten Zentren; optional "
                   "Peak-Flow-Monitoring."},
    # ── Positiver Pricktest ohne Symptome (2.1.3) ─────────────────────────
    {"wenn": {"platin_sensibilisierung": ["yes"]},
     "wenn_nicht": {"arbeitsbezogene_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Platinsalz-Sensibilisierung",
     "quelle": "Abschnitt 2.1.3 (Keine Bedenken unter bestimmten Voraussetzungen)",
     "befund": "Sensibilisierung gegenüber Chloroplatinaten (z. B. positiver Pricktest) ohne "
               "aktuelle Beschwerden.",
     "konsequenz": "Keine gesundheitlichen Bedenken nur unter bestimmten Voraussetzungen: "
                   "Einsatz in Arbeitsbereichen mit nachgewiesen geringerer Exposition "
                   "(Low-/Very-low-Exposure-Bereich), technische und organisatorische "
                   "Schutzmaßnahmen, PSA und verkürzte Nachuntersuchungsfristen; Exposition "
                   "auf ein absolutes Minimum begrenzen, bisherigen Verlauf und Mitwirkung "
                   "berücksichtigen (Case-Management, DGUV Information 240-130)."},
    # ── Arbeitsbezogene Beschwerden (1.1, 1.2.2, 3.2.1) ───────────────────
    {"wenn": {"arbeitsbezogene_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezogene Beschwerden",
     "quelle": "Abschnitte 1.1, 1.2.2 und 3.2.1 (Prävention)",
     "befund": "Beschwerden der Nase, Haut, Lungen oder Atemwege, die vermehrt bei der Arbeit "
               "auftreten.",
     "konsequenz": "Vorzeitige Nachuntersuchung bzw. sofortige Abklärung: Pricktest mit "
                   "wässriger Natriumhexachloroplatinat-Lösung und Spirometrie mit "
                   "Fluss-Volumen-Kurve durchführen; nach ärztlicher Indikation "
                   "Hyperreaktivitätstestung oder weitergehende Diagnostik im "
                   "Facharztzentrum (1.2.2)."},
    {"wenn": {"symptome": ["quaddeln", "ausschlag"]},
     "schwere": "pruefen",
     "bereich": "Hautsymptome",
     "quelle": "Abschnitte 1.2.2 und 3.1.3",
     "befund": "Arbeitsbezogene Hautsymptome angegeben (Quaddeln/Nesselausschlag oder "
               "Hautausschläge).",
     "konsequenz": "Dermale Symptome früh erfassen (1.2.2): V. a. Kontakturtikaria/Dermatitis "
                   "durch Chloroplatinate; Hautkontakt konsequent vermeiden (3.1.3), "
                   "hautärztliche Abklärung erwägen."},
    # ── Vorexposition (1.2.2) ─────────────────────────────────────────────
    {"wenn": {"frueher_exposition": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorexposition",
     "quelle": "Abschnitt 1.2.2 (Spezielle Untersuchung)",
     "befund": "Frühere Exposition gegenüber Chloroplatinaten angegeben.",
     "konsequenz": "Pricktest bereits bei der Erstuntersuchung durchführen (vor Aufnahme der "
                   "Tätigkeit nur bei Hinweisen auf vorhergehende Chloroplatinat-Exposition "
                   "sinnvoll); Biomonitoring (Platin im Urin) nach Exposition erwägen; frühere "
                   "Tätigkeiten dokumentieren."},
    # ── Vorzeitige Nachuntersuchung (1.1) ─────────────────────────────────
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Die versicherte Person vermutet einen ursächlichen Zusammenhang zwischen "
               "Erkrankung/Beschwerden und der Tätigkeit am Arbeitsplatz.",
     "konsequenz": "Vorzeitige Nachuntersuchung veranlassen (1.1); Beschwerden gezielt "
                   "explorieren, Pricktest und Spirometrie durchführen, Ergebnis in die "
                   "Beurteilung nach Abschnitt 2 einbeziehen."},
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen eine Fortsetzung der "
                   "Tätigkeit geben könnte (vorzeitige Nachuntersuchung nach 1.1); Befunde "
                   "und Entlassungsberichte einholen."},
    # ── Allergologische Disposition (1.2.2, Anhang 7.1) ───────────────────
    {"wenn": {"unspez_reize": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bronchiale Hyperreagibilität",
     "quelle": "Abschnitte 1.2.2 und Anhang 7.1.1",
     "befund": "Husten/Atemnot bei unspezifischen Reizen (Deospray, Parfüm, Kochgerüche, "
               "Zigarettenrauch) angegeben.",
     "konsequenz": "Hinweis auf unspezifische bronchiale Hyperreagibilität: Lungenfunktion "
                   "sorgfältig bewerten; nach ärztlicher Indikationsstellung "
                   "Hyperreaktivitätstestung bzw. weitergehende Diagnostik im "
                   "Facharztzentrum (1.2.2)."},
    {"wenn": {"fruehere_firma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere arbeitsbedingte Beschwerden",
     "quelle": "Abschnitte 1.2.2 und Anhang 7.1.1",
     "befund": "Arbeitsbezogene Beschwerden der Nase, Haut, Lungen oder Atemwege in einer "
               "früheren Firma angegeben.",
     "konsequenz": "Vorbefunde und Behandlungsunterlagen einholen; klären, ob damals eine "
                   "Chloroplatinat-Exposition bestand – dann Pricktest bereits bei der "
                   "Erstuntersuchung; Ergebnis in die Beurteilung nach Abschnitt 2 "
                   "einbeziehen."},
    # ── Schutzmaßnahmen und Hautkontakt (2.2, 3.1.3) ──────────────────────
    {"wenn": {"psa": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Eindringliche Beratung zur besonderen Bedeutung von Hygienemaßnahmen und "
                   "PSA (2.2); Ursachen klären. Ergeben sich Hinweise auf unzureichenden "
                   "Arbeitsschutz, Mitteilung an den Arbeitgeber zur Aktualisierung der "
                   "Gefährdungsbeurteilung – unter Wahrung der schutzwürdigen Belange der "
                   "untersuchten Person."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitt 3.1.3 (Aufnahme)",
     "befund": "Hautkontakt mit Chloroplatinaten bei der Arbeit angegeben.",
     "konsequenz": "Beratung: Hautkontakt vermeiden – eine Atemwegsallergisierung durch "
                   "Hautkontakt ist für Chloroplatinate nicht auszuschließen; geeignete "
                   "Schutzhandschuhe und Hygienemaßnahmen; stoffspezifische Hinweise zu "
                   "Schutzmaßnahmen über GESTIS."},
    {"wenn": {"geschuetzt": ["no"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 2.2 (Beratung) und Anhang 7.1.2",
     "befund": "Die versicherte Person fühlt sich durch die Schutzmaßnahmen nicht gut "
               "geschützt.",
     "konsequenz": "Verbesserungsvorschläge dokumentieren und in der Beratung aufgreifen; bei "
                   "Hinweisen auf Schutzlücken Mitteilung an den Arbeitgeber zur "
                   "Aktualisierung der Gefährdungsbeurteilung."},
    # ── Biomonitoring-Störgrößen (3.1.4) ──────────────────────────────────
    {"wenn": {"platin_medikamente": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 3.1.4 (Biomonitoring)",
     "befund": "Frühere Behandlung mit platinhaltigen Zytostatika angegeben.",
     "konsequenz": "Bei der Bewertung des Biomonitorings (Platin im Urin, UBA-Referenzwert "
                   "10 ng/l) berücksichtigen: Eine zurückliegende Behandlung mit "
                   "Platin-Zytostatika kann den Wert erhöhen; berufliche Belastung ggf. "
                   "durch Vergleich von Vor- und Nachschichtwerten abgrenzen."},
    {"wenn": {"zahnersatz": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 3.1.4 (Biomonitoring)",
     "befund": "Edelmetallhaltiger Zahnersatz (Inlays, Kronen, Brücken) angegeben.",
     "konsequenz": "Beim Biomonitoring berücksichtigen: Der UBA-Referenzwert (10 ng/l Platin "
                   "im Urin) gilt nur für Personen ohne Inlays, Brücken oder Kronen; "
                   "platinhaltiges Dentalgold kann den Wert erhöhen – Abgrenzung über "
                   "Vor-/Nachschichtvergleich."},
    # ── Beratung (2.2) ────────────────────────────────────────────────────
    {"wenn": {"rauchen": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung: Inhalatives Rauchen verschlechtert u. a. die Lungenfunktion – "
                   "Rauchstopp empfehlen, Unterstützungsangebote aufzeigen."},
]
