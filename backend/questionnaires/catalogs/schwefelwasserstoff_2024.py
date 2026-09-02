# -*- coding: utf-8 -*-
"""Schwefelwasserstoff – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Schwefelwasserstoff« (E H2S, Fassung Januar 2022), S. 523–539."""

SLUG = "schwefelwasserstoff-2024"

CATALOG = {
    "version": 2,
    "title": "Schwefelwasserstoff (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Schwefelwasserstoff« (E H2S, Fassung Januar 2022), S. 523–539",
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
                             "Schwefelwasserstoff?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge zu Schwefelwasserstoff"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zu dieser Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert für Schwefelwasserstoff (5 ppm nach TRGS 900) "
                            "nicht eingehalten wird. Angebotsvorsorge: wenn eine Belastung nicht "
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
            "title": "Tätigkeit & Belastung",
            "subtitle": "Ihre Arbeit mit möglichem Kontakt zu Schwefelwasserstoff (H2S)",
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
                    "label": "In welchen Bereichen arbeiten Sie, in denen Schwefelwasserstoff "
                             "auftreten kann?",
                    "hint": "Schwefelwasserstoff ist ein giftiges Gas, das nach faulen Eiern "
                            "riecht. Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "klaerwerk_kanal", "label": "Klärwerk, Abwasseranlage oder Kanalisation"},
                        {"value": "biogas", "label": "Biogasanlage"},
                        {"value": "guelle", "label": "Entleeren/Befüllen von Gruben oder Tankfahrzeugen mit Gülle/Flüssigmist"},
                        {"value": "wasseraufbereitung", "label": "Wasseraufbereitung mit sulfidhaltigem Wasser (z. B. Gerberei, Abdeckerei, Gelatine- oder Zuckerfabrik)"},
                        {"value": "gas_erdoel", "label": "Gaswerk, Raffinerie, Erdöl- oder Erdgasanlage (Rohgas, Sauergas)"},
                        {"value": "chemie_labor", "label": "Chemische Industrie oder analytisches Labor (z. B. Arbeiten mit Sulfiden und Säuren)"},
                        {"value": "koks_viskose", "label": "Koksbatterien oder Viskoseindustrie (Schwefelkohlenstoff)"},
                        {"value": "sonstige", "label": "Anderer Bereich"},
                        {"value": "keine", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon in Bereichen mit möglichem "
                             "Schwefelwasserstoff-Kontakt?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "ueber5", "label": "Mehr als 5 Jahre"},
                    ],
                },
                {
                    "id": "frueher_h2s",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt zu Schwefelwasserstoff "
                             "oder anderen giftigen Gasen?",
                    "required": True,
                    "followup": {"id": "frueher_h2s_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "geruch_arbeitsplatz",
                    "type": "yes_no",
                    "label": "Nehmen Sie bei der Arbeit häufig oder stark den Geruch nach faulen "
                             "Eiern wahr?",
                    "hint": "Der Geruch ist die typische Warnwirkung von Schwefelwasserstoff. "
                            "Häufige oder starke Geruchswahrnehmung kann auf ungewöhnliche "
                            "Betriebszustände hindeuten.",
                    "required": True,
                    "followup": {"id": "geruch_arbeitsplatz_desc", "type": "text",
                                 "label": "Wo, wie oft und in welchen Situationen?", "when": "yes"},
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle oder Unfälle mit "
                             "Schwefelwasserstoff (z. B. Gasalarm, plötzlich starker Geruch, "
                             "Übelkeit, Schwindel oder Bewusstlosigkeit im Einsatz)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Läuft bei Ihnen derzeit ein Berufskrankheiten-Verfahren, oder wurde "
                             "bei Ihnen früher eine Berufskrankheit anerkannt?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Erkrankung bzw. welches Verfahren?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Atemschutz, Gaswarngeräte und Hygiene an Ihrem Arbeitsplatz",
            "questions": [
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei Tätigkeiten, bei denen Schwefelwasserstoff frei "
                             "werden kann, den vorgesehenen Atemschutz?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_vorgesehen", "label": "Atemschutz ist bei mir nicht vorgesehen"},
                    ],
                },
                {
                    "id": "gaswarngeraet",
                    "type": "yes_no",
                    "label": "Wird an Ihrem Arbeitsplatz ein Gaswarngerät für Schwefelwasserstoff "
                             "eingesetzt (tragbar oder fest installiert)?",
                    "hint": "Wichtig, weil man den Geruch bei höheren Konzentrationen nicht mehr "
                            "wahrnimmt – die Warnwirkung der Nase fällt dann aus.",
                    "required": True,
                },
                {
                    "id": "hygiene",
                    "type": "yes_no",
                    "label": "Können Sie die Hygieneregeln an Ihrem Arbeitsplatz gut einhalten "
                             "(z. B. Waschen, Wechsel der Arbeitskleidung, getrennte Aufbewahrung "
                             "von Arbeits- und Straßenkleidung)?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Aktuelle Beschwerden ───────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden: Atemwege, Augen & Geruchssinn",
            "subtitle": "Beschwerden, die auf eine Wirkung von Schwefelwasserstoff hinweisen können",
            "questions": [
                {
                    "id": "atemwege_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie derzeit eine oder mehrere dieser Beschwerden an den "
                             "Atemwegen?",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Husten"},
                        {"value": "heiserkeit", "label": "Heiserkeit"},
                        {"value": "luftnot", "label": "Luftnot / Kurzatmigkeit"},
                        {"value": "nasenatmung", "label": "Behinderte Nasenatmung (verstopfte Nase)"},
                        {"value": "nasenlaufen", "label": "Ständiges Nasenlaufen"},
                        {"value": "rachenreizung", "label": "Reizung oder Entzündung von Rachen und Luftröhre (Kratzen, Halsschmerzen)"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "geruchssinn",
                    "type": "yes_no",
                    "label": "Ist Ihr Geruchssinn gestört – riechen Sie schlechter als früher "
                             "oder gar nicht mehr?",
                    "hint": "Wichtig, weil der Geruch nach faulen Eiern die Warnwirkung von "
                            "Schwefelwasserstoff ist.",
                    "required": True,
                },
                {
                    "id": "augen",
                    "type": "yes_no",
                    "label": "Haben Sie gereizte oder entzündete Augen (Bindehautentzündung: "
                             "Rötung, Brennen, Tränen, Lichtempfindlichkeit)?",
                    "required": True,
                },
                {
                    "id": "haut_entzuendung",
                    "type": "yes_no",
                    "label": "Haben Sie akute oder immer wiederkehrende Hautentzündungen?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Nervensystem, Kreislauf, Magen-Darm ────────────────────────
        {
            "id": "beschwerden_allgemein",
            "title": "Beschwerden: Nerven, Kreislauf & Verdauung",
            "subtitle": "Weitere Beschwerden, die mit Schwefelwasserstoff zusammenhängen können",
            "questions": [
                {
                    "id": "neuro_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere dieser Beschwerden?",
                    "required": True,
                    "options": [
                        {"value": "kopfschmerzen", "label": "Häufige Kopfschmerzen"},
                        {"value": "gleichgewicht", "label": "Gleichgewichtsstörungen"},
                        {"value": "schwindel", "label": "Schwindel"},
                        {"value": "muedigkeit", "label": "Ungewöhnliche Müdigkeit / Mattigkeit"},
                        {"value": "reizbarkeit", "label": "Leichte Reizbarkeit oder Stimmungsschwankungen"},
                        {"value": "gedaechtnis", "label": "Gedächtnis- oder Konzentrationsstörungen"},
                        {"value": "verwirrtheit", "label": "Verwirrtheitszustände"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "kreislauf_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie Beschwerden mit Herz oder Kreislauf?",
                    "required": True,
                    "options": [
                        {"value": "niedriger_blutdruck", "label": "Sehr niedriger Blutdruck (z. B. unter 100 mmHg systolisch) oder Schwächegefühl"},
                        {"value": "herzstolpern", "label": "Herzstolpern / unregelmäßiger Herzschlag (Extrasystolen)"},
                        {"value": "brustenge", "label": "Engegefühl oder Schmerzen in der Brust"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "magen_darm",
                    "type": "multi_choice",
                    "label": "Haben Sie Beschwerden im Magen-Darm-Bereich?",
                    "required": True,
                    "options": [
                        {"value": "metallgeschmack", "label": "Metallischer Geschmack im Mund"},
                        {"value": "erbrechen", "label": "Übelkeit oder Erbrechen"},
                        {"value": "durchfall", "label": "Durchfall"},
                        {"value": "appetitverlust", "label": "Appetitverlust"},
                        {"value": "gewichtsverlust", "label": "Ungewollter Gewichtsverlust"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
            ],
        },
        # ── 6 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, die für die Beurteilung wichtig sind",
            "questions": [
                {
                    "id": "atemwegserkrankung",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Erkrankungen der Atemwege oder der Lunge "
                             "(z. B. Asthma, chronische Bronchitis, Lungenemphysem)?",
                    "required": True,
                    "followup": {"id": "atemwegserkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "herzkreislauferkrankung",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Erkrankungen von Herz oder Kreislauf "
                             "(z. B. Herzschwäche, Herzrhythmusstörungen, koronare Herzkrankheit)?",
                    "required": True,
                    "followup": {"id": "herzkreislauferkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann, in Behandlung?", "when": "yes"},
                },
                {
                    "id": "neuro_psych_erkrankung",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie neurologische oder psychische Erkrankungen "
                             "(z. B. Krampfleiden, Nervenerkrankung, Depression, ausgeprägte "
                             "vegetative Beschwerden wie Herzrasen, Schweißausbrüche, "
                             "Schlafstörungen)?",
                    "required": True,
                    "followup": {"id": "neuro_psych_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "anaemie",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Blutarmut (Anämie) bekannt?",
                    "hint": "Schwefelwasserstoff stört den Sauerstofftransport im Blut – eine "
                            "Blutarmut ist deshalb für die Beurteilung wichtig.",
                    "required": True,
                },
                {
                    "id": "sonstige_einschraenkungen",
                    "type": "yes_no",
                    "label": "Gibt es sonstige gesundheitliche Einschränkungen oder Erkrankungen, "
                             "die wir kennen sollten?",
                    "required": True,
                    "followup": {"id": "sonstige_einschraenkungen_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
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
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"herzkreislauferkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 7.4 und 7.4.2–7.4.4",
     "befund": "Herz-Kreislauf-Erkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Prüfen, ob eine hämodynamisch wirksame Herz-Kreislauf-Erkrankung vorliegt "
                   "(beurteilungsrelevant nach 7.4): Vorbefunde einholen, Ruhe-EKG-Befund werten, "
                   "ggf. kardiologische Abklärung. Bei geringerer Ausprägung Maßnahmen nach 7.4.2 "
                   "(z. B. Expositionsbegrenzung, Einsatz an Arbeitsplätzen mit geringerer "
                   "Exposition); bei erwarteter Änderung des Schweregrads verkürzte Vorsorgefrist "
                   "nach 7.4.3; sind Maßnahmen erfolglos, Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"atemwegserkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 7.4 und 7.4.2–7.4.4",
     "befund": "Atemwegs- oder Lungenerkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Prüfen, ob ein Lungenemphysem oder eine Lungenerkrankung mit erheblicher "
                   "Funktionsstörung vorliegt (beurteilungsrelevant nach 7.4): Spirometrie-Befund "
                   "werten, Vorbefunde einholen, ggf. pneumologische Abklärung. Je nach Ausprägung "
                   "Maßnahmen nach 7.4.2, verkürzte Frist nach 7.4.3 oder Tätigkeitswechsel-"
                   "Erwägung nach 7.4.4."},
    {"wenn": {"neuro_psych_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem/Psyche",
     "quelle": "Abschnitte 7.2.1, 7.2.2 und 7.4",
     "befund": "Neurologische oder psychische Erkrankung bzw. ausgeprägte vegetative "
               "Beschwerden angegeben.",
     "konsequenz": "Ausgeprägte neurologische/psychische Krankheiten und psychovegetative "
                   "Störungen sind beurteilungsrelevant (7.4): orientierende neurologische "
                   "Untersuchung vertiefen, psychonervalen Fragebogen (z. B. Q18) auswerten, "
                   "ggf. neurologisch-psychiatrische Facharztvorstellung. Maßnahmen nach "
                   "7.4.2/7.4.3 prüfen."},
    {"wenn": {"anaemie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Blut",
     "quelle": "Abschnitte 6.3.1, 7.2.2 und 7.4",
     "befund": "Bekannte Blutarmut (Anämie) angegeben.",
     "konsequenz": "Anämie ist beurteilungsrelevant (7.4), da Schwefelwasserstoff den "
                   "Sauerstofftransport (Hämoglobin) beeinträchtigt: kleines Blutbild werten, "
                   "Ursache und Ausprägung klären (ggf. hausärztliche/hämatologische Abklärung). "
                   "Maßnahmen nach 7.4.2 und verkürzte Frist nach 7.4.3 prüfen."},
    {"wenn": {"geruchssinn": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Geruchssinn/Warnwirkung",
     "quelle": "Abschnitte 6.3.1, 7.2.2, 7.4 und 8.1",
     "befund": "Störung des Geruchssinns angegeben.",
     "konsequenz": "Störungen des Geruchsvermögens sind beurteilungsrelevant (7.4), weil damit "
                   "die Warnwirkung des Gases entfällt: Riechtest (Screeningtest, z. B. Sniffin' "
                   "Sticks mit 8 Sticks) durchführen und werten. Beratung zum Wegfall der "
                   "Warnwirkung; Maßnahmen nach 7.4.2 (z. B. Gaswarngerät, geringere Exposition) "
                   "prüfen; sind Maßnahmen ohne Erfolg, Tätigkeitswechsel nach 7.4.4 erwägen."},
    # ── Aktuelle Beschwerden (Abschnitte 7.1 und 7.4) ─────────────────────
    {"wenn": {"augen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen",
     "quelle": "Abschnitte 6.3.2, 7.1 und 7.4",
     "befund": "Gereizte oder entzündete Augenbindehäute angegeben.",
     "konsequenz": "Erkrankungen und Reizungen der Augenbindehäute sind beurteilungsrelevant "
                   "(7.4): Konjunktivitis abklären und Zusammenhang mit der Exposition prüfen "
                   "(Reizwirkung ab ca. 100 ppm). Ergibt sich ein Hinweis auf unzureichende "
                   "Schutzmaßnahmen, Mitteilung an das Unternehmen und Vorschlag von "
                   "Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"atemwege_beschwerden": ["husten", "heiserkeit", "luftnot", "nasenatmung",
                                       "nasenlaufen", "rachenreizung"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 6.3.2, 7.1 und 7.4",
     "befund": "Reizbeschwerden der Atemwege (z. B. Husten, Heiserkeit, Luftnot, behinderte "
               "Nasenatmung, Nasenlaufen, Rachenreizung) angegeben.",
     "konsequenz": "Schleimhautreizung der oberen/tieferen Luftwege abklären: Spirometrie-Befund "
                   "werten, zeitlichen Zusammenhang mit der Tätigkeit klären (Besserung an "
                   "arbeitsfreien Tagen?). Bei expositionsbezogenen Beschwerden Abgleich mit der "
                   "Gefährdungsbeurteilung, ggf. Mitteilung an das Unternehmen nach § 6 (4) "
                   "ArbMedVV und verkürzte Vorsorgefrist nach 7.4.3."},
    {"wenn": {"neuro_beschwerden": ["kopfschmerzen", "gleichgewicht", "schwindel", "muedigkeit",
                                    "reizbarkeit", "gedaechtnis", "verwirrtheit"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 6.3.2, 6.3.3, 7.1 und 7.2",
     "befund": "Nervensystem-Beschwerden (z. B. Kopfschmerzen, Gleichgewichtsstörungen, "
               "Schwindel, Müdigkeit, Reizbarkeit, Gedächtnisstörungen, Verwirrtheit) angegeben.",
     "konsequenz": "Mögliche neurotoxische Beanspruchungsfolge abklären: orientierende "
                   "neurologische Untersuchung, psychonervalen Fragebogen (z. B. Q18) einsetzen "
                   "und auswerten; bei auffälligem Befund neurologische Facharztvorstellung. "
                   "Expositionssituation prüfen (Zwischenfälle, ungewöhnliche Betriebszustände) "
                   "und verkürzte Vorsorgefrist nach 7.4.3 erwägen."},
    {"wenn": {"kreislauf_beschwerden": ["niedriger_blutdruck", "herzstolpern", "brustenge"]},
     "schwere": "pruefen",
     "bereich": "Kreislauf",
     "quelle": "Abschnitte 6.3.2, 7.1 und 7.2.2",
     "befund": "Kreislaufbeschwerden (niedriger Blutdruck, Herzstolpern oder Engegefühl in der "
               "Brust) angegeben.",
     "konsequenz": "Auf Hypotonie (systolisch < 100 mmHg), Extrasystolie und stenokardische "
                   "Zustände achten: Blutdruck messen, Ruhe-EKG werten (z. B. T-Wellen-"
                   "Veränderungen, Rhythmusstörungen); bei auffälligem Befund kardiologische "
                   "Abklärung veranlassen. Beurteilung nach 7.4, ggf. Maßnahmen nach 7.4.2."},
    {"wenn": {"magen_darm": ["metallgeschmack", "erbrechen", "durchfall", "appetitverlust",
                             "gewichtsverlust"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm-Trakt",
     "quelle": "Abschnitte 6.3.2 und 7.1",
     "befund": "Magen-Darm-Beschwerden (z. B. metallischer Geschmack, Erbrechen, Durchfall, "
               "Appetit- oder Gewichtsverlust) angegeben.",
     "konsequenz": "Als mögliche Beanspruchungsfolge einer H2S-Exposition abklären: zeitlichen "
                   "Zusammenhang mit der Arbeit und ungewöhnlichen Betriebszuständen klären, "
                   "andere Ursachen ärztlich ausschließen; bei Verdacht auf arbeitsbedingte "
                   "Beschwerden Abgleich mit der Gefährdungsbeurteilung und ggf. Mitteilung an "
                   "das Unternehmen."},
    {"wenn": {"haut_entzuendung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 7.1 (Beschwerden: Haut)",
     "befund": "Akute oder chronische Hautentzündungen angegeben.",
     "konsequenz": "Hautbefund erheben und Zusammenhang mit der Tätigkeit klären; Beratung zu "
                   "Hygiene am Arbeitsplatz, Vermeiden von Hautkontakt und Wechsel der "
                   "Arbeitskleidung (Abschnitt 8.1); ggf. dermatologische Abklärung."},
    # ── Zwischenfälle, BK-Verfahren ───────────────────────────────────────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle/Unfälle",
     "quelle": "Abschnitte 7.1 und 6.5; § 6 (4) ArbMedVV",
     "befund": "Zwischenfall/Unfall oder ungewöhnliche Betriebszustände mit Schwefelwasserstoff "
               "angegeben.",
     "konsequenz": "Hergang und Häufigkeit dokumentieren (einschließlich Geruchswahrnehmungen); "
                   "nach Vergiftungssymptomen und möglichen Nachkrankheiten (ZNS, Kreislauf) "
                   "gezielt fragen und untersuchen. Mitteilung an das Unternehmen mit Vorschlag "
                   "von Schutzmaßnahmen (§ 6 (4) ArbMedVV); bei Erkrankungsverdacht "
                   "BK-Anzeige nach BK-Nr. 1202 prüfen."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 7.1 und 6.5",
     "befund": "Laufendes oder abgeschlossenes Berufskrankheiten-Verfahren angegeben.",
     "konsequenz": "Art der Berufskrankheit und Verfahrensstand dokumentieren, Vorbefunde "
                   "einholen und bei der Beurteilung nach 7.4 berücksichtigen."},
    # ── Schutzmaßnahmen und Beratung (Abschnitte 8.1 und 8.2) ─────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Atemschutz/PSA",
     "quelle": "Abschnitte 8.1 und 8.2; § 6 (4) ArbMedVV",
     "befund": "Vorgesehener Atemschutz wird selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA (Atemschutz) und zur "
                   "Lebensgefahr durch Schwefelwasserstoff (ab 500 ppm lebensbedrohlich); "
                   "Ursachen der Nichtbenutzung klären (Auswahl nach GESTIS, Rubrik »Umgang und "
                   "Verwendung«). Reichen die Schutzmaßnahmen nicht aus, Mitteilung an das "
                   "Unternehmen und Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"gaswarngeraet": ["no"]},
     "wenn_nicht": {"arbeitsbereiche": ["keine"]},
     "schwere": "hinweis",
     "bereich": "Warnwirkung/Gefahrenerkennung",
     "quelle": "Abschnitte 6.3.1 und 8.1",
     "befund": "Kein Gaswarngerät am Arbeitsplatz mit möglicher H2S-Exposition angegeben.",
     "konsequenz": "Beratung: Die Geruchswarnung ist trügerisch – bei anhaltender Exposition "
                   "tritt Gewöhnung ein, ab ca. 100 ppm fällt die Geruchswahrnehmung ganz aus. "
                   "Dem Unternehmen die Überprüfung der Gefährdungsbeurteilung und technische/"
                   "organisatorische Schutzmaßnahmen (z. B. Gaswarneinrichtungen) vorschlagen."},
    {"wenn": {"geruch_arbeitsplatz": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Exposition/Betriebszustände",
     "quelle": "Abschnitt 7.1 (weitere Vorsorgen) und 8.2",
     "befund": "Häufige oder starke Geruchswahrnehmung (faule Eier) am Arbeitsplatz angegeben.",
     "konsequenz": "Häufigkeit und Stärke der Geruchswahrnehmungen sowie zugehörige "
                   "Betriebszustände dokumentieren und mit der Gefährdungsbeurteilung abgleichen; "
                   "bei Hinweisen auf erhöhte Exposition Mitteilung an das Unternehmen und "
                   "Vorschlag von Schutzmaßnahmen."},
    {"wenn": {"hygiene": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Hygieneregeln können am Arbeitsplatz nicht gut eingehalten werden.",
     "konsequenz": "Beratung zu Hygienemaßnahmen (Waschen, Wechsel der Arbeitskleidung, "
                   "Vermeiden von Inhalation und Hautkontakt); Hindernisse klären und dem "
                   "Unternehmen organisatorische Verbesserungen vorschlagen."},
]
