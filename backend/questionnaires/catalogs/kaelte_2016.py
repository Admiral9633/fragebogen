# -*- coding: utf-8 -*-
"""
G 21 Kältearbeiten – DGUV Grundsatz 2016.

Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, G 21
"Kältearbeiten" (Fassung Oktober 2014), Ausgabe 2016, S. 341–347.

Gezielte arbeitsmedizinische Untersuchung bei Tätigkeiten mit extremer
Kältebelastung (–25 °C oder kälter). Der Grundsatz enthält eigene
Nachuntersuchungsfristen (temperaturabhängig 3/6 bzw. 6/12 Monate),
ein obligates spezielles Untersuchungsprogramm (Urinstatus, Blutzucker,
Blutbild, Kreatinin, Ruhe-EKG) und die Beurteilungskategorien
"dauernde/befristete gesundheitliche Bedenken".
"""

SLUG = "g21-kaelte-2016"

CATALOG = {
    "version": 2,
    "title": "G 21 Kältearbeiten (DGUV Grundsatz 2016)",
    "basis": (
        "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, G 21 "
        "„Kältearbeiten“ (Fassung Oktober 2014), Ausgabe 2016, S. 341–347"
    ),
    "sections": [
        # ── 1 ─────────────────────────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Untersuchungsanlass & Tätigkeit",
            "subtitle": "Angaben zur Untersuchung und zu Ihrer Arbeit in extremer Kälte",
            "questions": [
                {
                    "id": "untersuchungsart",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich?",
                    "required": True,
                    "options": [
                        {"value": "erstuntersuchung",
                         "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "erste_nachuntersuchung",
                         "label": "Erste Nachuntersuchung"},
                        {"value": "weitere_nachuntersuchung",
                         "label": "Weitere Nachuntersuchung"},
                    ],
                },
                {
                    "id": "temperaturbereich",
                    "type": "choice",
                    "label": "In welchem Temperaturbereich arbeiten Sie oder sollen Sie arbeiten?",
                    "hint": "Von dieser Angabe hängen die Nachuntersuchungsfristen ab.",
                    "required": True,
                    "options": [
                        {"value": "minus25_45", "label": "–25 °C bis –45 °C"},
                        {"value": "unter_minus45", "label": "Kälter als –45 °C"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "arbeitsbereiche",
                    "type": "multi_choice",
                    "label": "In welchen kalten Bereichen arbeiten Sie oder sollen Sie arbeiten?",
                    "hint": "Gemeint sind Räume mit technisch erzeugter Kälte unter –25 °C "
                            "(auch Reparaturarbeiten).",
                    "required": True,
                    "options": [
                        {"value": "kuehlraum", "label": "Kühlräume"},
                        {"value": "gefrierraum", "label": "Gefrierräume / Tiefkühllager"},
                        {"value": "gefriertrockenraum", "label": "Gefriertrockenräume"},
                        {"value": "versuchskammer", "label": "Tieftemperatur-Versuchskammern"},
                        {"value": "sonstig", "label": "Andere kalte Arbeitsbereiche"},
                    ],
                },
                {
                    "id": "aufenthaltsdauer",
                    "type": "choice",
                    "label": "Wie lange halten Sie sich üblicherweise am Stück im Kältebereich auf?",
                    "hint": "Als kurzzeitig gilt ein Aufenthalt unter 15 Minuten zu Kontrollzwecken "
                            "oder zum Geben von Anweisungen – mit Kälteschutzkleidung.",
                    "required": True,
                    "options": [
                        {"value": "unter15", "label": "Nur kurz: unter 15 Minuten (z. B. Kontrollgänge)"},
                        {"value": "ueber15", "label": "Länger als 15 Minuten am Stück"},
                    ],
                },
                {
                    "id": "zugluft",
                    "type": "yes_no",
                    "label": "Sind Sie in der Kälte starker Luftbewegung ausgesetzt "
                             "(Zugluft, Ventilatoren, Fahrtwind)?",
                    "hint": "An solchen Arbeitsplätzen wird dem Körper besonders viel "
                            "Wärme entzogen.",
                    "required": True,
                },
                {
                    "id": "psa_kaelte",
                    "type": "yes_no",
                    "label": "Steht Ihnen vollständige Kälteschutzkleidung zur Verfügung "
                             "und tragen Sie diese bei der Arbeit?",
                    "required": True,
                },
            ],
        },
        # ── 2 ─────────────────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden bei Kälte",
            "subtitle": "Körperliche Reaktionen auf Kälte – bei der Arbeit oder in der Freizeit",
            "questions": [
                {
                    "id": "kaelte_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei Aufenthalt in der Kälte körperliche Beschwerden "
                             "(z. B. an Herz, Atmung, Haut oder Fingern)?",
                    "hint": "Wenn nein, überspringen Sie die folgenden Detailfragen automatisch.",
                    "required": True,
                },
                {
                    "id": "brust_atem_kaelte",
                    "type": "yes_no",
                    "label": "Bekommen Sie in der Kälte Engegefühl oder Schmerzen in der Brust, "
                             "Atemnot oder pfeifende Atmung?",
                    "hint": "Kälte kann reflektorisch Angina pectoris (Herzenge) oder einen "
                            "Bronchospasmus (Verkrampfung der Atemwege) auslösen.",
                    "required": True,
                    "show_if": {"id": "kaelte_beschwerden", "in": ["yes"]},
                },
                {
                    "id": "finger_weiss",
                    "type": "yes_no",
                    "label": "Werden Ihre Finger bei Kälte weiß oder blau und schmerzen dabei "
                             "(sogenannte „Weißfinger“, Raynaud-Syndrom)?",
                    "required": True,
                    "show_if": {"id": "kaelte_beschwerden", "in": ["yes"]},
                },
                {
                    "id": "schleimhaut",
                    "type": "yes_no",
                    "label": "Haben Sie bei Kälte häufig Entzündungen oder starke Reizungen "
                             "der Schleimhäute (z. B. Nase, Rachen, Augen)?",
                    "required": True,
                    "show_if": {"id": "kaelte_beschwerden", "in": ["yes"]},
                },
                {
                    "id": "erfrierung",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal eine Erfrierung "
                             "(z. B. an Fingern, Zehen, Nase oder Ohren)?",
                    "required": True,
                    "followup": {
                        "id": "erfrierung_desc",
                        "type": "textarea",
                        "label": "Wann, an welcher Körperstelle, und sind Folgen geblieben?",
                        "when": "yes",
                    },
                },
                {
                    "id": "erkrankung_laenger",
                    "type": "yes_no",
                    "label": "Waren Sie seit der letzten Untersuchung länger als sechs Wochen "
                             "am Stück krank oder innerhalb von sechs Monaten mehrmals "
                             "kurz erkrankt?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart",
                                "in": ["erste_nachuntersuchung", "weitere_nachuntersuchung"]},
                    "followup": {
                        "id": "erkrankung_laenger_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung(en), und wie lange waren Sie krank?",
                        "when": "yes",
                    },
                },
                {
                    "id": "zusammenhang_arbeit",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung oder "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "not_in": ["erstuntersuchung"]},
                    "followup": {
                        "id": "zusammenhang_arbeit_desc",
                        "type": "textarea",
                        "label": "Welche Beschwerden, und warum vermuten Sie den Zusammenhang?",
                        "when": "yes",
                    },
                },
            ],
        },
        # ── 3 ─────────────────────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Gesundheit",
            "subtitle": "Erkrankungen, die für Arbeiten in extremer Kälte wichtig sind",
            "questions": [
                {
                    "id": "herz_kreislauf",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung des Herzens oder des Kreislaufs "
                             "(z. B. koronare Herzkrankheit, Herzschwäche, "
                             "Herzrhythmusstörungen, hoher Blutdruck)?",
                    "required": True,
                    "followup": {
                        "id": "herz_kreislauf_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und sind Sie in Behandlung?",
                        "when": "yes",
                    },
                },
                {
                    "id": "atemwege",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der Atemwege oder der Lunge "
                             "(z. B. Asthma, COPD, chronische Bronchitis)?",
                    "required": True,
                    "followup": {
                        "id": "atemwege_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und wie wird sie behandelt?",
                        "when": "yes",
                    },
                },
                {
                    "id": "blut",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung des Blutes "
                             "(z. B. Blutarmut/Anämie, Gerinnungsstörung)?",
                    "required": True,
                },
                {
                    "id": "haut_durchblutung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Hauterkrankung, die die Durchblutung der Haut "
                             "beeinflusst?",
                    "required": True,
                },
                {
                    "id": "niere",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der Nieren oder der Harnwege?",
                    "required": True,
                },
                {
                    "id": "rheuma",
                    "type": "yes_no",
                    "label": "Haben Sie eine rheumatische Erkrankung oder ein bekanntes "
                             "Raynaud-Syndrom („Weißfingerkrankheit“)?",
                    "required": True,
                    "followup": {
                        "id": "rheuma_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und sind Sie in Behandlung?",
                        "when": "yes",
                    },
                },
                {
                    "id": "augen",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der äußeren Augen (z. B. trockene Augen/"
                             "Sicca-Syndrom, Flügelfell/Pterygium, häufige Bindehautentzündungen) "
                             "oder wurden Ihre Augen operiert?",
                    "required": True,
                    "followup": {
                        "id": "augen_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung bzw. welche Operation, und wann?",
                        "when": "yes",
                    },
                },
                {
                    "id": "kaelte_allergie",
                    "type": "yes_no",
                    "label": "Reagieren Sie überempfindlich auf Kälte – z. B. mit Nesselsucht/"
                             "Quaddeln (Kälteurtikaria) oder dunklem Urin nach Kälte "
                             "(Kältehämoglobinurie)?",
                    "required": True,
                    "followup": {
                        "id": "kaelte_allergie_desc",
                        "type": "textarea",
                        "label": "Wie äußert sich die Reaktion, und wurde sie ärztlich abgeklärt?",
                        "when": "yes",
                    },
                },
                {
                    "id": "anfallsleiden",
                    "type": "yes_no",
                    "label": "Hatten Sie jemals epileptische Anfälle oder ein anderes "
                             "Anfallsleiden?",
                    "required": True,
                    "followup": {
                        "id": "anfallsleiden_desc",
                        "type": "textarea",
                        "label": "Wann war der letzte Anfall, wie häufig treten Anfälle auf, "
                                 "und sind Sie in Behandlung?",
                        "when": "yes",
                    },
                },
                {
                    "id": "nervensystem",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung des Nervensystems mit spürbaren "
                             "Funktionsstörungen (z. B. Lähmungen, Gefühlsstörungen, "
                             "Gleichgewichtsstörungen)?",
                    "required": True,
                    "followup": {
                        "id": "nervensystem_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und welche Einschränkungen bestehen?",
                        "when": "yes",
                    },
                },
                {
                    "id": "abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Drogen oder Medikamenten?",
                    "required": True,
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {
                        "id": "medikamente_desc",
                        "type": "textarea",
                        "label": "Welche Medikamente, und wofür?",
                        "when": "yes",
                    },
                },
            ],
        },
        # ── 4 ─────────────────────────────────────────────────────────────
        {
            "id": "einwilligung",
            "title": "Einwilligung",
            "subtitle": "Bestätigung Ihrer Angaben",
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
    # ── Fristen (G 21, Abschnitt 1.1) ─────────────────────────────────────
    {"wenn": {"temperaturbereich": ["minus25_45"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfristen",
     "quelle": "G 21, 1.1",
     "befund": "Tätigkeit im Temperaturbereich –25 °C bis –45 °C",
     "konsequenz": "Nachuntersuchungsfristen nach G 21 einhalten: erste "
                   "Nachuntersuchung vor Ablauf von 6 Monaten, weitere "
                   "Nachuntersuchungen vor Ablauf von 12 Monaten (sofern keine "
                   "staatlichen Fristvorgaben gelten)."},
    {"wenn": {"temperaturbereich": ["unter_minus45"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfristen",
     "quelle": "G 21, 1.1",
     "befund": "Tätigkeit im Temperaturbereich kälter als –45 °C",
     "konsequenz": "Verkürzte Nachuntersuchungsfristen nach G 21 einhalten: erste "
                   "Nachuntersuchung vor Ablauf von 3 Monaten, weitere "
                   "Nachuntersuchungen vor Ablauf von 6 Monaten."},
    {"wenn": {"erkrankung_laenger": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "G 21, 1.1",
     "befund": "Zwischenzeitliche Erkrankung von mehr als sechs Wochen bzw. "
               "mehrmalige kurzzeitige Erkrankungen innerhalb von sechs Monaten",
     "konsequenz": "Beratung und ggf. vorzeitige Nachuntersuchung durchführen, wenn "
                   "die Erkrankungen Anlass zu Bedenken gegen die Fortsetzung der "
                   "Tätigkeit geben könnten."},
    {"wenn": {"zusammenhang_arbeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "G 21, 1.1",
     "befund": "Beschäftigte Person vermutet ursächlichen Zusammenhang zwischen "
               "Erkrankung und Tätigkeit am Arbeitsplatz",
     "konsequenz": "Vorzeitige Nachuntersuchung anbieten und den vermuteten "
                   "Zusammenhang abklären; ggf. Hinweis an den Arbeitgeber zur "
                   "Aktualisierung der Gefährdungsbeurteilung (Abschnitt 2.2)."},

    # ── kritisch: Bedenken gegen Aufnahme/Fortsetzung ────────────────────
    {"wenn": {"brust_atem_kaelte": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf / Atemwege",
     "quelle": "G 21, 3.2.2 / 2.1.1",
     "befund": "Engegefühl/Brustschmerz oder Atemnot bei Kälte – Verdacht auf "
               "reflektorisch ausgelöste Angina pectoris bzw. Bronchospasmus",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Tätigkeit abklären: Ruhe-EKG "
                   "(1.2.2), in unklaren Fällen Ergometrie (Anhang 2) bzw. "
                   "Lungenfunktionsprüfung (Anhang 1) als Ergänzungsuntersuchung; "
                   "bei chronischer relevanter Erkrankung dauernde gesundheitliche "
                   "Bedenken (2.1.1)."},
    {"wenn": {"kaelte_allergie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Kälteüberempfindlichkeit",
     "quelle": "G 21, 2.1.1",
     "befund": "Neigung zu Überempfindlichkeitsreaktionen bei Kälteeinwirkung "
               "(z. B. Kälteurtikaria, Kältehämoglobinurie) angegeben",
     "konsequenz": "Nach G 21 Kriterium für dauernde gesundheitliche Bedenken – "
                   "vor Einsatz abklären (ggf. dermatologisch-allergologisch bzw. "
                   "hämatologisch, weitere Laboruntersuchungen nach 1.2.3); bei "
                   "bestätigter Diagnose Tätigkeit in extremer Kälte nicht aufnehmen "
                   "bzw. nicht fortsetzen."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Abhängigkeit",
     "quelle": "G 21, 2.1.1",
     "befund": "Alkohol-, Suchtmittel- oder Medikamentenabhängigkeit angegeben",
     "konsequenz": "Nach G 21 Kriterium für dauernde gesundheitliche Bedenken – "
                   "Behandlungsstand und Abstinenz vor Einsatz klären; bei zu "
                   "erwartender Wiederherstellung befristete gesundheitliche "
                   "Bedenken (2.1.2) aussprechen."},

    # ── pruefen: Ergänzungsuntersuchung / Abklärung ───────────────────────
    {"wenn": {"herz_kreislauf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "G 21, 2.1.1 / 2.1.3 / 1.2.3",
     "befund": "Herz-Kreislauf-Erkrankung angegeben",
     "konsequenz": "Ruhe-EKG obligat (1.2.2), in unklaren Fällen Ergometrie als "
                   "Ergänzungsuntersuchung (Anhang 2). Bei chronischer relevanter "
                   "Erkrankung dauernde gesundheitliche Bedenken (2.1.1); bei "
                   "leichterer Erkrankung keine Bedenken unter bestimmten "
                   "Voraussetzungen, z. B. Einhaltung verkürzter "
                   "Nachuntersuchungsfristen (2.1.3)."},
    {"wenn": {"atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "G 21, 2.1.1 / 1.2.3",
     "befund": "Erkrankung der Atmungsorgane angegeben",
     "konsequenz": "In unklaren Fällen Lungenfunktionsprüfung als "
                   "Ergänzungsuntersuchung (Anhang 1); bei chronischer relevanter "
                   "Erkrankung dauernde gesundheitliche Bedenken (2.1.1), sonst "
                   "2.1.3 mit verkürzten Nachuntersuchungsfristen prüfen."},
    {"wenn": {"blut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Blut",
     "quelle": "G 21, 2.1.1 / 1.2.2",
     "befund": "Erkrankung des Blutes angegeben",
     "konsequenz": "Blutbild im Rahmen der speziellen Untersuchung (1.2.2), ggf. "
                   "weitere Laboruntersuchungen (1.2.3); bei chronischer relevanter "
                   "Erkrankung dauernde gesundheitliche Bedenken (2.1.1)."},
    {"wenn": {"haut_durchblutung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "G 21, 2.1.1",
     "befund": "Hauterkrankung mit Einfluss auf die Durchblutung angegeben",
     "konsequenz": "Hautbefund erheben; bei chronischer, für die Tätigkeit "
                   "relevanter Erkrankung dauernde gesundheitliche Bedenken "
                   "(2.1.1), bei leichterer Ausprägung 2.1.3 mit verkürzten "
                   "Fristen prüfen."},
    {"wenn": {"niere": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nieren / Harnwege",
     "quelle": "G 21, 2.1.1 / 1.2.2",
     "befund": "Erkrankung der Nieren oder ableitenden Harnwege angegeben",
     "konsequenz": "Urinstatus (Mehrfachteststreifen) und Kreatinin im Rahmen der "
                   "speziellen Untersuchung (1.2.2); bei chronischer relevanter "
                   "Erkrankung dauernde gesundheitliche Bedenken (2.1.1)."},
    {"wenn": {"rheuma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Rheumatischer Formenkreis",
     "quelle": "G 21, 2.1.1 / 2.1.2",
     "befund": "Erkrankung des rheumatischen Formenkreises bzw. Morbus Raynaud angegeben",
     "konsequenz": "Krankheitsaktivität klären (ggf. rheumatologische Vorstellung); "
                   "bei chronischer relevanter Erkrankung dauernde gesundheitliche "
                   "Bedenken (2.1.1), bei zu erwartender Wiederherstellung "
                   "befristete Bedenken (2.1.2)."},
    {"wenn": {"finger_weiss": ["yes"]},
     "wenn_nicht": {"rheuma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Durchblutung der Hände",
     "quelle": "G 21, 2.1.1",
     "befund": "Weiß-/Blauverfärbung der Finger mit Schmerzen bei Kälte "
               "(Verdacht auf Raynaud-Syndrom), bislang ohne bekannte Diagnose",
     "konsequenz": "Abklärung eines Morbus Raynaud veranlassen (ggf. angiologische/"
                   "rheumatologische Vorstellung), bevor die Tätigkeit in extremer "
                   "Kälte aufgenommen bzw. fortgesetzt wird."},
    {"wenn": {"augen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen",
     "quelle": "G 21, 2.1.1",
     "befund": "Erkrankung des äußeren Auges bzw. voroperierte Augen angegeben",
     "konsequenz": "Augenärztliches Konsil erforderlich (laut G 21 ausdrücklich bei "
                   "Sicca-Syndrom, Pterygium, häufigeren Entzündungen der vorderen "
                   "Augenabschnitte und voroperierten Augen)."},
    {"wenn": {"anfallsleiden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Anfallsleiden",
     "quelle": "G 21, 2.1.1 / DGUV Information 250-001",
     "befund": "Epileptische Anfälle bzw. Anfallsleiden in der Vorgeschichte",
     "konsequenz": "Beurteilung in Abhängigkeit von Art, Häufigkeit, Prognose und "
                   "Behandlungsstand der Anfälle nach DGUV Information 250-001 "
                   "(„Empfehlungen zur Beurteilung beruflicher Möglichkeiten von "
                   "Personen mit Epilepsie“); neurologischen Befund anfordern."},
    {"wenn": {"nervensystem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "G 21, 2.1.1",
     "befund": "Erkrankung des zentralen oder peripheren Nervensystems mit "
               "Funktionsstörungen angegeben",
     "konsequenz": "Ausmaß der Funktionsstörungen klären (neurologische Vorstellung); "
                   "bei wesentlichen Funktionsstörungen dauernde gesundheitliche "
                   "Bedenken (2.1.1)."},
    {"wenn": {"erfrierung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lokale Kälteschäden",
     "quelle": "G 21, 3.2.2 / 2.1.3",
     "befund": "Erfrierung in der Vorgeschichte",
     "konsequenz": "Betroffene Areale untersuchen (Durchblutung, Sensibilität); "
                   "erhöhte lokale Kälteempfindlichkeit berücksichtigen, Beratung zu "
                   "Kälteschutzkleidung; ggf. verkürzte Nachuntersuchungsfristen "
                   "nach 2.1.3."},
    {"wenn": {"psa_kaelte": ["no"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "G 21, 2.2",
     "befund": "Kälteschutzkleidung fehlt oder wird nicht getragen",
     "konsequenz": "Dem Arbeitgeber mitteilen, dass die Gefährdungsbeurteilung zu "
                   "aktualisieren und der Arbeitsschutz zu verbessern ist – unter "
                   "Wahrung der schutzwürdigen Belange der untersuchten Person; "
                   "Beratung zu technischen, organisatorischen und persönlichen "
                   "Schutzmaßnahmen."},

    # ── hinweis: Beratungsthemen ─────────────────────────────────────────
    {"wenn": {"schleimhaut": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Schleimhäute",
     "quelle": "G 21, 3.2.2",
     "befund": "Häufige katarrhalische bzw. entzündliche Schleimhautreaktionen bei Kälte",
     "konsequenz": "Beratung zu Schutzmaßnahmen (Atemschutz vor Kaltluft, "
                   "Aufwärmpausen); bei anhaltenden Beschwerden HNO-ärztliche bzw. "
                   "augenärztliche Abklärung erwägen."},
]
