# -*- coding: utf-8 -*-
"""Platinverbindungen – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Platinverbindungen« (E PLT, Fassung Januar 2022), S. 451–476."""

SLUG = "platin-2024"

CATALOG = {
    "version": 2,
    "title": "Platinverbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Platinverbindungen« (E PLT, Fassung Januar 2022), "
             "S. 451–476",
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
                             "Platinverbindungen (Platinsalzen)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zu dieser Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn eine wiederholte "
                            "Exposition gegenüber krebserzeugenden oder erbgutverändernden "
                            "Platinverbindungen (Kategorie 1A/1B) oder eine Gefährdung durch "
                            "Hautkontakt nicht ausgeschlossen werden kann. Nachgehende Vorsorge: "
                            "Untersuchung nach dem Ende einer solchen Tätigkeit.",
                    "required": True,
                    "options": [
                        {"value": "pflicht", "label": "Vom Betrieb verpflichtend veranlasst (Pflichtvorsorge)"},
                        {"value": "angebot", "label": "Vom Betrieb angeboten (Angebotsvorsorge)"},
                        {"value": "wunsch", "label": "Auf meinen eigenen Wunsch (Wunschvorsorge)"},
                        {"value": "nachgehend", "label": "Nach dem Ende der Tätigkeit (nachgehende Vorsorge)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kontakt mit Platinverbindungen",
            "subtitle": "Ihre Arbeit und der mögliche Kontakt mit Platinsalzen (Chloroplatinaten)",
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
                    "hint": "Mehrfachauswahl möglich. In diesen Bereichen ist mit Platinsalzen "
                            "(Chloroplatinaten) zu rechnen.",
                    "required": True,
                    "options": [
                        {"value": "scheiderei", "label": "Edelmetallscheiderei (Trennen und Aufbereiten von Edelmetallen)"},
                        {"value": "katalysator", "label": "Herstellung von platinhaltigen Katalysatoren"},
                        {"value": "zytostatika", "label": "Herstellung von platinhaltigen Krebsmedikamenten "
                                                          "(Zytostatika, z. B. Cisplatin, Carboplatin)"},
                        {"value": "andere_verbindungen", "label": "Herstellung anderer platinhaltiger Verbindungen"},
                        {"value": "halbleiter_laser", "label": "Halbleiter- oder Lasertechnik (z. B. mit Magnus-Salzen)"},
                        {"value": "galvanik", "label": "Galvanikbetrieb (elektrochemische Beschichtung)"},
                        {"value": "service", "label": "Handwerks-, Reinigungs- oder Laborarbeiten in solchen Bereichen"},
                        {"value": "anderes", "label": "Anderer Bereich / keiner davon"},
                    ],
                },
                {
                    "id": "direkter_kontakt",
                    "type": "yes_no",
                    "label": "Haben Sie bei Ihrer Arbeit direkten Umgang mit Platinsalzen "
                             "(Chloroplatinaten), z. B. mit Pulvern, Lösungen oder Stäuben?",
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
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle, Unfälle oder ungewöhnliche "
                             "Betriebszustände mit diesen Stoffen (z. B. Verschütten, defekte "
                             "Absaugung)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_exposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten schon einmal Kontakt mit "
                             "Platinsalzen (Chloroplatinaten) oder ähnlichen Stoffen?",
                    "required": True,
                    "followup": {"id": "frueher_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "cisplatin_laerm",
                    "type": "yes_no",
                    "label": "Arbeiten Sie bei der Herstellung von Cisplatin (platinhaltiges "
                             "Krebsmedikament) zusätzlich in einem lauten Arbeitsbereich "
                             "(Lärmbereich)?",
                    "hint": "Cisplatin kann das Gehör zusätzlich belasten (ototoxische Wirkung) – "
                            "zusammen mit Lärm ist das wichtig für die Vorsorge.",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Arbeitshygiene",
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
                    "id": "hygiene",
                    "type": "yes_no",
                    "label": "Wechseln Sie nach der Arbeit die Arbeitskleidung und können Sie "
                             "sich am Arbeitsplatz waschen (Arbeitshygiene)?",
                    "required": True,
                },
                {
                    "id": "informiert",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich über die Schutzmaßnahmen an Ihrem Arbeitsplatz "
                             "gut informiert?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
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
                        {"value": "fliessschnupfen", "label": "Fließschnupfen, Niesanfälle oder eine laufende/juckende Nase"},
                        {"value": "husten", "label": "Wiederholter Husten"},
                        {"value": "pfeifen", "label": "Pfeifendes oder giemendes Geräusch im Brustkorb"},
                        {"value": "kurzatmigkeit", "label": "Anfälle von Kurzatmigkeit oder Atemnot"},
                        {"value": "engegefuehl", "label": "Engegefühl im Brustkorb"},
                        {"value": "augen", "label": "Augenbrennen, Augentränen oder Augenjucken"},
                        {"value": "quaddeln", "label": "Juckende Quaddeln auf der Haut nach direktem Kontakt "
                                                       "(Nesselausschlag, Kontakturtikaria)"},
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
        # ── 5 ─ Allergien ──────────────────────────────────────────────────
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
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Berufskrankheit anerkannt, oder läuft derzeit "
                             "ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Erkrankung bzw. welches Verfahren?", "when": "yes"},
                },
                {
                    "id": "platin_medikamente",
                    "type": "yes_no",
                    "label": "Wurden Sie schon einmal mit platinhaltigen Medikamenten behandelt "
                             "(z. B. Chemotherapie mit Cisplatin, Carboplatin oder Oxaliplatin)?",
                    "hint": "Das ist wichtig, weil solche Behandlungen den Platinwert im Urin "
                            "(Biomonitoring) erhöhen können.",
                    "required": True,
                },
                {
                    "id": "zahnersatz",
                    "type": "yes_no",
                    "label": "Haben Sie edelmetallhaltigen Zahnersatz, z. B. Inlays, Kronen, "
                             "Brücken oder Wurzelstifte?",
                    "hint": "Zahngold kann bis zu 28 % Platin enthalten, Wurzelstifte bis zu 70 % – "
                            "das kann den Platinwert im Urin (Biomonitoring) beeinflussen.",
                    "required": True,
                },
                {
                    "id": "silikonimplantat",
                    "type": "yes_no",
                    "label": "Tragen Sie Silikonimplantate (z. B. Brustimplantate)?",
                    "hint": "Auch Silikonimplantate können den Platinwert im Urin beeinflussen.",
                    "required": True,
                },
            ],
        },
        # ── 7 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen_sektion",
            "title": "Rauchen",
            "subtitle": "Rauchen erhöht das Risiko, eine Allergie zu entwickeln",
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
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"asthma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 7.4 und 7.4.2–7.4.4",
     "befund": "Symptomatische obstruktive Atemwegserkrankung (z. B. Asthma bronchiale) angegeben.",
     "konsequenz": "Ärztlich prüfen, ob die Tätigkeit ohne gesundheitliche Gefährdung möglich "
                   "ist (7.4): eingehende Untersuchung der Atemorgane und Spirometrie mit "
                   "Fluss-Volumen-Kurve durchführen; Maßnahmen nach 7.4.2 prüfen (Substitution, "
                   "technische/organisatorische Maßnahmen, Einsatz im geringen/sehr geringen "
                   "Expositionsbereich, PSA) sowie verkürzte Vorsorgefristen nach 7.4.3; bei "
                   "fehlender Erfolgsaussicht Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"lungenerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lungenerkrankung",
     "quelle": "Abschnitte 7.1 und 7.4",
     "befund": "Erhebliche Lungenerkrankung (fortgeschrittene Lungengerüsterkrankung/Emphysem) "
               "angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Vorbefunde einholen, "
                   "Lungenfunktion prüfen; Maßnahmen nach 7.4.2 bzw. verkürzte Fristen nach "
                   "7.4.3 prüfen, bei fehlender Erfolgsaussicht Tätigkeitswechsel nach 7.4.4 "
                   "erwägen."},
    {"wenn": {"platin_sensibilisierung": ["yes"], "arbeitsbezogene_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Platinsalz-Sensibilisierung",
     "quelle": "Abschnitt 7.4.3",
     "befund": "Bekannte Sensibilisierung gegenüber Chloroplatinaten mit arbeitsbezogenen "
               "Beschwerden (symptomatisch).",
     "konsequenz": "Einsatz symptomatisch Sensibilisierter nur in Bereichen ohne Umgang mit "
                   "Chloroplatinaten (unabhängig vom Platin-Luftmesswert) oder in Bereichen "
                   "mit sehr geringer Exposition (< 0,02 µg/m³) unter verkürzten "
                   "Nachuntersuchungsintervallen; Pricktest-Verlaufskontrolle, Spirometrie; "
                   "bei Erfolglosigkeit der Maßnahmen Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"platin_sensibilisierung": ["yes"]},
     "wenn_nicht": {"arbeitsbezogene_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Platinsalz-Sensibilisierung",
     "quelle": "Abschnitte 7.4.2 und 7.4.3",
     "befund": "Bekannte Sensibilisierung gegenüber Chloroplatinaten ohne aktuelle Beschwerden "
               "(asymptomatisch).",
     "konsequenz": "Einsatz nur in Bereichen ohne Umgang mit Chloroplatinaten oder in Bereichen "
                   "mit geringer/sehr geringer Exposition (< 0,2 µg/m³) unter verkürzten "
                   "Nachuntersuchungsintervallen; Exposition auf ein absolutes Minimum "
                   "begrenzen, Verlauf und Mitwirkung berücksichtigen; regelmäßige "
                   "Pricktest-Verlaufskontrolle."},
    # ── Arbeitsbezogene Beschwerden (Abschnitte 7.2, 7.3, 7.4.2) ──────────
    {"wenn": {"arbeitsbezogene_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezogene Beschwerden",
     "quelle": "Abschnitte 7.2.2, 7.3 und 7.4.2",
     "befund": "Beschwerden der Nase, Haut, Lungen oder Atemwege, die vermehrt bei der Arbeit "
               "auftreten.",
     "konsequenz": "Umgehend Pricktest mit wässriger Natriumhexachloroplatinat-Lösung sowie "
                   "Spirometrie mit Fluss-Volumen-Kurve durchführen (Pricktest umgehend beim "
                   "Auftreten arbeitsplatzbezogener Symptome, 7.3). Bis zur diagnostischen "
                   "Klärung Maßnahmen nach 7.4.2 (Expositionsminderung). Bei negativem "
                   "Pricktest und unklaren Befunden weitere Abklärung; spezifische "
                   "Provokationstestung nur in spezialisierten Zentren; optional "
                   "Peak-Flow-Monitoring."},
    {"wenn": {"symptome": ["husten", "pfeifen", "kurzatmigkeit", "engegefuehl"]},
     "schwere": "pruefen",
     "bereich": "Atemwegssymptome",
     "quelle": "Abschnitte 6.3, 7.2.2 und 7.4.2",
     "befund": "Bronchiale Symptome angegeben (Husten, Pfeifen/Giemen, Kurzatmigkeit oder "
               "Engegefühl im Brustkorb).",
     "konsequenz": "Verdacht auf beginnende obstruktive Atemwegserkrankung (Platinsalz-Asthma): "
                   "Lungenfunktion sorgfältig prüfen, unklare Atemwegssymptomatik bis zur "
                   "diagnostischen Klärung wie unter 7.4.2 behandeln; an Berufskrankheit "
                   "BK-Nr. 4301 denken und ggf. Meldung prüfen."},
    {"wenn": {"symptome": ["quaddeln", "ausschlag"]},
     "schwere": "pruefen",
     "bereich": "Hautsymptome",
     "quelle": "Abschnitte 6.3 und 6.5",
     "befund": "Juckende Quaddeln (Kontakturtikaria) oder Hautausschläge angegeben.",
     "konsequenz": "Dermale Symptome abklären (V. a. Kontakturtikaria durch Chloroplatinate); "
                   "Hautkontakt konsequent vermeiden, ggf. hautärztliche Vorstellung; an "
                   "Berufskrankheit BK-Nr. 5101 denken und ggf. Hautarztverfahren einleiten."},
    # ── Frühere Exposition / Erstvorsorge (Abschnitt 7.2.2) ───────────────
    {"wenn": {"frueher_exposition": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorexposition",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Frühere Exposition gegenüber Chloroplatinaten angegeben.",
     "konsequenz": "Bereits bei der ersten Vorsorge Pricktest durchführen (bei Erstuntersuchung "
                   "nur bei Hinweisen auf vorhergehende Chloroplatinat-Exposition indiziert); "
                   "Biomonitoring (Platin im Urin) erwägen; frühere Tätigkeiten und "
                   "Schutzmaßnahmen dokumentieren."},
    # ── Kombinationswirkung Cisplatin + Lärm (Abschnitt 6.1.1) ────────────
    {"wenn": {"cisplatin_laerm": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kombinationswirkung Gehör",
     "quelle": "Abschnitt 6.1.1",
     "befund": "Tätigkeit mit höherer Cisplatin-Exposition in Lärmbereichen angegeben.",
     "konsequenz": "Wegen der ototoxischen Eigenschaft von Cisplatin mögliche "
                   "Kombinationswirkungen mit Lärm bei der Gehöruntersuchung nach der "
                   "DGUV Empfehlung »Lärm« berücksichtigen; Abgleich mit der "
                   "Gefährdungsbeurteilung."},
    # ── Nachgehende Vorsorge (Abschnitt 2) ────────────────────────────────
    {"wenn": {"vorsorge_anlass": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitt 2 (Anwendungsbereich, ArbMedVV)",
     "befund": "Vorstellung zur nachgehenden Vorsorge nach Ende der Tätigkeit.",
     "konsequenz": "Nachgehende Vorsorge nach Exposition gegenüber krebserzeugenden oder "
                   "keimzellmutagenen Platinverbindungen (Kategorie 1A/1B): Anamnese auf "
                   "Spätfolgen ausrichten; Anmeldung bzw. Fortführung über das Meldeportal "
                   "»DGUV Vorsorge« (www.dguv-vorsorge.de) sicherstellen."},
    # ── Schutzmaßnahmen (Abschnitte 3, 6.2, 8) ────────────────────────────
    {"wenn": {"psa": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 3, 7.1 und 8.2",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zu Sensibilisierungsgefahr und PSA-Benutzung; Ursachen "
                   "klären. Ergeben sich Anhaltspunkte, dass die Maßnahmen des Arbeitsschutzes "
                   "nicht ausreichen, Mitteilung an das Unternehmen und Vorschlag von "
                   "Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitte 6.2 und 8.1",
     "befund": "Hautkontakt mit Platinverbindungen bei der Arbeit angegeben.",
     "konsequenz": "Beratung: Hautkontakt vermeiden – eine Atemwegsallergisierung durch "
                   "Hautkontakt ist für Chloroplatinate nicht auszuschließen; geeignete "
                   "Schutzhandschuhe und Hygienemaßnahmen; Abgleich mit der "
                   "Gefährdungsbeurteilung (TRGS 401), ggf. Maßnahmenvorschlag an das "
                   "Unternehmen."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitte 7.1 und 8.2",
     "befund": "Zwischenfälle, Unfälle oder ungewöhnliche Betriebszustände angegeben.",
     "konsequenz": "Ereignisse erfragen und dokumentieren; kurzfristige Beschwerden erfassen, "
                   "ggf. Pricktest/Spirometrie vorziehen; Abgleich mit der "
                   "Gefährdungsbeurteilung und ggf. Mitteilung an das Unternehmen mit "
                   "Maßnahmenvorschlag (§ 6 (4) ArbMedVV)."},
    # ── Allergologische Disposition (Abschnitte 7.1, 7.2.2) ───────────────
    {"wenn": {"unspez_reize": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bronchiale Hyperreagibilität",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Husten/Atemnot bei unspezifischen Reizen (Deospray, Parfüm, Kochgerüche, "
               "Zigarettenrauch) angegeben.",
     "konsequenz": "Hinweis auf unspezifische bronchiale Hyperreagibilität: Lungenfunktion "
                   "sorgfältig bewerten, bei unklaren Befunden weitere Abklärung nach 7.2.2 "
                   "(ggf. in spezialisiertem Zentrum); Befund bei der Beurteilung nach 7.4 "
                   "berücksichtigen."},
    {"wenn": {"fruehere_firma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere arbeitsbedingte Beschwerden",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Arbeitsbezogene Beschwerden der Nase, Haut, Lungen oder Atemwege in einer "
               "früheren Firma angegeben.",
     "konsequenz": "Vorbefunde und Behandlungsunterlagen einholen; klären, ob damals eine "
                   "Exposition gegenüber Chloroplatinaten oder anderen Allergenen bestand – "
                   "dann Pricktest bereits bei der ersten Vorsorge; Beurteilung nach 7.4."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 6.5 und 7.1",
     "befund": "Anerkannte Berufskrankheit oder laufendes BK-Verfahren angegeben.",
     "konsequenz": "Art und Stand des Verfahrens dokumentieren, Befunde in die Beurteilung "
                   "einbeziehen (relevant: BK-Nr. 4301 obstruktive Atemwegserkrankungen, "
                   "BK-Nr. 5101 Hauterkrankungen)."},
    # ── Biomonitoring-Störgrößen (Abschnitt 6.4) ──────────────────────────
    {"wenn": {"platin_medikamente": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 6.4",
     "befund": "Frühere Behandlung mit platinhaltigen Medikamenten (Zytostatika) angegeben.",
     "konsequenz": "Bei der Bewertung des Biomonitorings (Platin im Urin, Referenzwert "
                   "10 ng/l) berücksichtigen: zurückliegende Platin-Zytostatika-Behandlung "
                   "kann den Wert erhöhen; berufliche Belastung ggf. durch Vergleich von "
                   "Vor- und Nachschichtwerten abgrenzen."},
    {"wenn": {"zahnersatz": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitte 6.4 und 7.1",
     "befund": "Edelmetallhaltiger Zahnersatz (Inlays, Kronen, Brücken, Wurzelstifte) angegeben.",
     "konsequenz": "Beim Biomonitoring berücksichtigen: Der UBA-Referenzwert (10 ng/l Platin "
                   "im Urin) gilt nur für Personen ohne Inlays, Brücken oder Kronen; "
                   "Dentallegierungen können den Wert erhöhen – Abgrenzung über Vor-/"
                   "Nachschichtvergleich."},
    {"wenn": {"silikonimplantat": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 7.1 (Anamnese) und Literatur (Schierl et al. 2014)",
     "befund": "Silikonimplantate angegeben.",
     "konsequenz": "Als mögliche Störgröße bei der Bewertung des Platin-Biomonitorings "
                   "berücksichtigen und dokumentieren."},
    # ── Beratung (Abschnitte 7.1 und 8.1) ─────────────────────────────────
    {"wenn": {"rauchen": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 7.1 und 8.1 (Beratung)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung: Inhalatives Rauchen steigert die Allergieinzidenz – "
                   "Rauchstopp empfehlen, insbesondere wegen der sensibilisierenden Wirkung "
                   "der Chloroplatinate; Unterstützungsangebote aufzeigen."},
]
