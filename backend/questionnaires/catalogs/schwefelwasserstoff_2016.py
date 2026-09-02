# -*- coding: utf-8 -*-
"""G 11 Schwefelwasserstoff – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 11 »Schwefelwasserstoff«
(Fassung Oktober 2014), S. 217–226."""

SLUG = "g11-schwefelwasserstoff-2016"

CATALOG = {
    "version": 2,
    "title": "G 11 Schwefelwasserstoff (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 11 »Schwefelwasserstoff« (Fassung Oktober 2014), S. 217–226",
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
                    "label": "Ist dies Ihre erste Untersuchung nach dem Grundsatz G 11 "
                             "(Schwefelwasserstoff)?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachuntersuchung: "
                            "in der Regel nach 12 bis 24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Ja, Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nein, Nachuntersuchung"},
                    ],
                },
                {
                    "id": "schwere_erkrankung_seit",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, wann, und wie lange?", "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {"id": "verdacht_zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
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
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
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
                        {"value": "kanalisation", "label": "Kanalisation oder Abwasserbereich"},
                        {"value": "biogas", "label": "Biogasanlage"},
                        {"value": "jauche", "label": "Entleeren/Befüllen von Gruben oder Tankfahrzeugen mit Jauche"},
                        {"value": "wasseraufbereitung", "label": "Wasseraufbereitung mit sulfidhaltigem Wasser"},
                        {"value": "industrie", "label": "Gummi-, Kunststoff-, Viskose- oder Zuckerindustrie"},
                        {"value": "gas_erdoel", "label": "Gaswerk, Raffinerie, Erdölgewinnung, Erdgasanlage oder Erdgasleitung (Rohgas)"},
                        {"value": "chemie", "label": "Sulfidfällung von Metallen / chemische Arbeiten mit Sulfiden"},
                        {"value": "koks", "label": "Füllen und Drücken von Koksbatterien"},
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
                    "hint": "Der Geruch ist die typische Warnwirkung von Schwefelwasserstoff – "
                            "sie fällt bei hohen Konzentrationen jedoch aus.",
                    "required": True,
                    "followup": {"id": "geruch_arbeitsplatz_desc", "type": "text",
                                 "label": "Wo, wie oft und in welchen Situationen?", "when": "yes"},
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle oder Unfälle mit "
                             "Schwefelwasserstoff (z. B. plötzlich starker Geruch, Übelkeit, "
                             "Schwindel oder Bewusstlosigkeit im Einsatz)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Persönliche Schutzausrüstung und Hautkontakt",
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
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit mit sulfidhaltigen Lösungen oder "
                             "Abwässern in Kontakt?",
                    "hint": "Schwefelwasserstoff kann auch über Haut und Schleimhäute "
                            "aufgenommen werden.",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Aktuelle Beschwerden ───────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden: Atemwege, Augen & Geruchssinn",
            "subtitle": "Beschwerden, auf die bei dieser Untersuchung besonders geachtet wird",
            "questions": [
                {
                    "id": "atemwege_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie derzeit eine oder mehrere dieser Beschwerden an den "
                             "Atemwegen?",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Husten / Bronchitis (Entzündung der Bronchien)"},
                        {"value": "kurzatmigkeit", "label": "Kurzatmigkeit / Luftnot"},
                        {"value": "rachenreizung", "label": "Reizung oder Entzündung von Rachen und Luftröhre (Kratzen, Halsschmerzen)"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "augen",
                    "type": "yes_no",
                    "label": "Haben Sie gereizte oder entzündete Augen (Bindehautentzündung: "
                             "Rötung, Brennen, Tränen)?",
                    "required": True,
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
                        {"value": "verwirrtheit", "label": "Verwirrtheitszustände"},
                        {"value": "bewegung", "label": "Unwillkürliche Bewegungen, Zittern oder Steifigkeit"},
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
    # ── Bedenkenstatbestände nach 2.1.1 (dauernde gesundheitliche Bedenken) ─
    {"wenn": {"herzkreislauferkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 2.1.1–2.1.3",
     "befund": "Herz-Kreislauf-Erkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Prüfen, ob eine hämodynamisch wirksame Herz-Kreislauf-Erkrankung vorliegt – "
                   "dann dauernde gesundheitliche Bedenken (2.1.1); bei zu erwartender "
                   "Wiederherstellung befristete Bedenken (2.1.2). Ruhe-EKG werten, Vorbefunde "
                   "einholen, in unklaren Fällen Ergometrie (1.2.3). Bei geringer Ausprägung "
                   "keine Bedenken unter Voraussetzungen (2.1.3: Schutzmaßnahmen, geringere "
                   "Exposition, verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"atemwegserkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 2.1.1–2.1.3",
     "befund": "Atemwegs- oder Lungenerkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Prüfen, ob ein Lungenemphysem oder eine Lungenerkrankung mit erheblicher "
                   "Funktionsstörung vorliegt – dann dauernde gesundheitliche Bedenken (2.1.1); "
                   "bei zu erwartender Wiederherstellung befristete Bedenken (2.1.2). Vorbefunde "
                   "einholen, ggf. pneumologische Abklärung; bei geringer Ausprägung keine "
                   "Bedenken unter Voraussetzungen (2.1.3)."},
    {"wenn": {"geruchssinn": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Geruchssinn/Warnwirkung",
     "quelle": "Abschnitte 2.1.1 und 2.2",
     "befund": "Störung des Geruchssinns angegeben.",
     "konsequenz": "Störungen des Geruchsvermögens sind Bedenkenstatbestand (2.1.1), weil die "
                   "Warnwirkung des Gases (Geruch nach faulen Eiern) entfällt: Geruchsvermögen "
                   "ärztlich prüfen, ggf. HNO-Abklärung. Nur bei geringer Ausprägung keine "
                   "Bedenken unter Voraussetzungen (2.1.3, z. B. Einsatz an Arbeitsplätzen mit "
                   "nachgewiesen geringerer Exposition)."},
    {"wenn": {"anaemie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Blut",
     "quelle": "Abschnitte 1.2.2, 2.1.1 und 2.1.2",
     "befund": "Bekannte Blutarmut (Anämie) angegeben.",
     "konsequenz": "Anämie ist Bedenkenstatbestand (2.1.1): Hämoglobin und Erythrozyten "
                   "bestimmen (spezielle Untersuchung, 1.2.2 – oxidativer Stoffwechsel, "
                   "O2-Abgabe), Ursache klären. Bei zu erwartender Wiederherstellung befristete "
                   "Bedenken (2.1.2), Nachuntersuchung nach Behandlung."},
    {"wenn": {"neuro_psych_erkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem/Psyche",
     "quelle": "Abschnitte 2.1.1 und 2.1.2",
     "befund": "Neurologische oder psychische Erkrankung bzw. ausgeprägte vegetative "
               "Beschwerden angegeben.",
     "konsequenz": "Ausgeprägte neurologische und psychische Krankheiten sowie ausgeprägte "
                   "psychovegetative Störungen sind Bedenkenstatbestand (2.1.1): Ausprägung "
                   "klären, ggf. fachärztliche Abklärung und Vorbefunde. Bei zu erwartender "
                   "Wiederherstellung befristete Bedenken (2.1.2); bei leichter Ausprägung "
                   "keine Bedenken unter Voraussetzungen (2.1.3)."},
    # ── Aktuelle Beschwerden (Achtungspunkte nach 1.2.1) ──────────────────
    {"wenn": {"augen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen",
     "quelle": "Abschnitte 1.2.1 und 2.1.1/2.1.2",
     "befund": "Gereizte oder entzündete Augenbindehäute (Konjunktivitis) angegeben.",
     "konsequenz": "Erkrankungen und Reizungen der Augenbindehäute sind beurteilungsrelevant "
                   "(2.1.1): Befund erheben, Zusammenhang mit der Exposition klären. Bei akuter "
                   "Reizung mit zu erwartender Wiederherstellung befristete Bedenken (2.1.2) "
                   "erwägen; Arbeitsplatzsituation prüfen und ggf. dem Arbeitgeber zur "
                   "Aktualisierung der Gefährdungsbeurteilung mitteilen (2.2)."},
    {"wenn": {"atemwege_beschwerden": ["husten", "kurzatmigkeit", "rachenreizung"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung) und 2.1.1/2.1.2",
     "befund": "Atemwegsbeschwerden (Husten/Bronchitis, Kurzatmigkeit oder Reizung von "
               "Rachen/Luftröhre) angegeben.",
     "konsequenz": "Achtungspunkte der Zwischenanamnese (Tracheopharyngitis, Bronchitis, "
                   "Kurzatmigkeit): Schleimhautreizung abklären, zeitlichen Zusammenhang mit "
                   "der Tätigkeit klären. Bei erheblicher Funktionsstörung Bedenken nach "
                   "2.1.1/2.1.2 erwägen; sonst verkürzte Nachuntersuchungsfrist (2.1.3, "
                   "Regelfrist 12–24 Monate unterschreiten)."},
    {"wenn": {"neuro_beschwerden": ["kopfschmerzen", "gleichgewicht", "schwindel", "muedigkeit",
                                    "reizbarkeit", "verwirrtheit", "bewegung"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung) und 3.2.2",
     "befund": "Nervensystem-Beschwerden (z. B. Kopfschmerzen, Gleichgewichtsstörungen, "
               "Schwindel, Müdigkeit, Reizbarkeit, Verwirrtheit, extrapyramidale Zeichen) "
               "angegeben.",
     "konsequenz": "Achtungspunkte der Zwischenanamnese: mögliche neurotoxische Wirkung "
                   "abklären, neurologische Untersuchung, ggf. Facharztvorstellung. "
                   "Expositionssituation und Zwischenfälle erfragen; verkürzte "
                   "Nachuntersuchungsfrist (2.1.3) und bei ausgeprägten Störungen Bedenken "
                   "nach 2.1.1 erwägen."},
    {"wenn": {"kreislauf_beschwerden": ["niedriger_blutdruck", "herzstolpern", "brustenge"]},
     "schwere": "pruefen",
     "bereich": "Kreislauf",
     "quelle": "Abschnitte 1.2.1, 1.2.2 und 1.2.3",
     "befund": "Kreislaufbeschwerden (niedriger Blutdruck, Herzstolpern oder Engegefühl in "
               "der Brust) angegeben.",
     "konsequenz": "Achtungspunkte Hypotonie (systolisch < 100 mmHg), Herzmuskelschädigung, "
                   "Extrasystolie, stenokardische Zustände: Blutdruck messen, Ruhe-EKG werten "
                   "(1.2.2); in unklaren Fällen Ergänzungsuntersuchung Ergometrie (1.2.3, "
                   "Leitfaden »Ergometrie«); ggf. kardiologische Abklärung."},
    {"wenn": {"magen_darm": ["metallgeschmack", "erbrechen", "durchfall", "appetitverlust",
                             "gewichtsverlust"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm-Trakt",
     "quelle": "Abschnitt 1.2.1 (Nachuntersuchung)",
     "befund": "Magen-Darm-Beschwerden (z. B. metallischer Geschmack, Erbrechen, Durchfall, "
               "Appetit- oder Gewichtsverlust) angegeben.",
     "konsequenz": "Achtungspunkte der Zwischenanamnese: als mögliche Folge einer "
                   "H2S-Belastung abklären, andere Ursachen ärztlich ausschließen; bei "
                   "Verdacht auf arbeitsbedingte Beschwerden Expositionssituation prüfen und "
                   "verkürzte Nachuntersuchungsfrist erwägen."},
    {"wenn": {"haut_entzuendung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung) und 3.1.3",
     "befund": "Akute oder chronische Hautentzündungen angegeben.",
     "konsequenz": "Achtungspunkt Haut der Zwischenanamnese: Hautbefund erheben, Zusammenhang "
                   "mit der Tätigkeit klären (Aufnahme auch über Haut und Schleimhäute "
                   "möglich); Beratung zu Hygienemaßnahmen und persönlicher Schutzausrüstung "
                   "(2.2), ggf. dermatologische Abklärung."},
    # ── Zwischenfälle und vorzeitige Nachuntersuchung ─────────────────────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle/Unfälle",
     "quelle": "Abschnitte 2.2, 3.2.2 und 4",
     "befund": "Zwischenfall/Unfall mit Schwefelwasserstoff angegeben.",
     "konsequenz": "Hergang dokumentieren, gezielt nach akuten Vergiftungszeichen und "
                   "möglichen Nachkrankheiten (ZNS-Schäden, psychische Symptome, Hypotonie) "
                   "fragen und untersuchen. Hinweise zur Verbesserung des Arbeitsschutzes dem "
                   "Arbeitgeber mitteilen (Aktualisierung der Gefährdungsbeurteilung, 2.2); "
                   "bei Erkrankungsverdacht BK-Anzeige nach BK-Nr. 1202 prüfen."},
    {"wenn": {"schwere_erkrankung_seit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Konstellation der vorzeitigen Nachuntersuchung: klären, ob die Erkrankung "
                   "Anlass zu Bedenken gegen die Fortsetzung der Tätigkeit gibt; "
                   "Behandlungsunterlagen einholen und Bedenken-Systematik nach 2.1 anwenden."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbedingte Beschwerden",
     "quelle": "Abschnitte 1.1 und 4",
     "befund": "Vermuteter Zusammenhang zwischen Erkrankung/Beschwerden und der Tätigkeit.",
     "konsequenz": "Anlass für eine (vorzeitige) Nachuntersuchung nach 1.1: Zusammenhang "
                   "arbeitsmedizinisch klären, Exposition und Befunde dokumentieren; bei "
                   "begründetem Verdacht auf eine Erkrankung durch Schwefelwasserstoff "
                   "BK-Anzeige (BK-Nr. 1202) erstatten."},
    # ── Schutzmaßnahmen und Beratung (Abschnitt 2.2) ──────────────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Atemschutz/PSA",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Vorgesehener Atemschutz wird selten oder nie getragen.",
     "konsequenz": "Eindringliche Beratung zu persönlicher Schutzausrüstung und zur "
                   "Giftigkeit von Schwefelwasserstoff; geeigneten Atemschutz nach GESTIS "
                   "(Rubrik »Umgang und Verwendung«) auswählen. Ergibt sich ein Hinweis auf "
                   "unzureichenden Arbeitsschutz, Mitteilung an den Arbeitgeber zur "
                   "Aktualisierung der Gefährdungsbeurteilung (2.2)."},
    {"wenn": {"geruch_arbeitsplatz": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Exposition/Warnwirkung",
     "quelle": "Abschnitte 2.2 und 3.2.1",
     "befund": "Häufige oder starke Geruchswahrnehmung (faule Eier) am Arbeitsplatz angegeben.",
     "konsequenz": "Beratung zur Warnwirkung: Der Geruch fällt bei hohen Konzentrationen "
                   "(Lähmung der Riechnerven ab ca. 300 ppm) aus und ist daher kein "
                   "verlässlicher Schutz. Expositionssituation dokumentieren; bei Hinweisen "
                   "auf erhöhte Exposition Mitteilung an den Arbeitgeber (2.2)."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautkontakt/Hygiene",
     "quelle": "Abschnitte 2.2 und 3.1.3; TRGS 401",
     "befund": "Hautkontakt zu sulfidhaltigen Lösungen oder Abwässern angegeben.",
     "konsequenz": "Beratung zu allgemeinen Hygienemaßnahmen und persönlicher "
                   "Schutzausrüstung (Schutzhandschuhe, Schutzkleidung), da die Aufnahme auch "
                   "über Haut und Schleimhäute erfolgt; Gefährdung durch Hautkontakt nach "
                   "TRGS 401 in der Gefährdungsbeurteilung berücksichtigen lassen."},
]
