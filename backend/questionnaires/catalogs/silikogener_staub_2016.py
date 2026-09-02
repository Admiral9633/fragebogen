# -*- coding: utf-8 -*-
"""G 1.1 Mineralischer Staub, Teil 1: Silikogener Staub – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, G 1.1
(Fassung Oktober 2014), S. 45–76."""

SLUG = "g1-1-silikogener_staub-2016"

CATALOG = {
    "version": 2,
    "title": "G 1.1 Silikogener Staub (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, "
             "G 1.1 »Mineralischer Staub, Teil 1: Silikogener Staub« "
             "(Fassung Oktober 2014), S. 45–76",
    "sections": [
        # ── 1 ─ Anlass der Untersuchung ────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "unt_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich heute?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachuntersuchung: "
                            "in der Regel nach 36 Monaten. Nachgehende Untersuchung: nach dem "
                            "Ende der Beschäftigung mit Quarzstaub.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung – vor Aufnahme der Tätigkeit"},
                        {"value": "nach", "label": "Nachuntersuchung – regelmäßige Wiederholung"},
                        {"value": "vorzeitig", "label": "Vorzeitige Nachuntersuchung – z. B. wegen "
                                                        "Beschwerden oder auf ärztlichen Rat"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung – nach Ende der "
                                                         "Beschäftigung"},
                    ],
                },
                {
                    "id": "laengere_krankheit",
                    "type": "yes_no",
                    "label": "Waren Sie seit der letzten Untersuchung mehrere Wochen am Stück "
                             "krank oder körperlich beeinträchtigt?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach", "vorzeitig", "nachgehend"]},
                    "followup": {"id": "laengere_krankheit_desc", "type": "textarea",
                                 "label": "Was war der Grund, und wie lange waren Sie krank?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Staubbelastung ───────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Staubbelastung",
            "subtitle": "Ihre Arbeit mit quarzhaltigem (silikogenem) Staub",
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
                    "label": "In welchen Bereichen arbeiten Sie oder haben Sie gearbeitet?",
                    "hint": "Mehrfachauswahl möglich. Quarzstaub entsteht vor allem beim "
                            "Gewinnen und Bearbeiten von Stein und Mineralien.",
                    "required": True,
                    "options": [
                        {"value": "bergbau", "label": "Berg- oder Stollenbau (Vortrieb, Abbau, Förderung)"},
                        {"value": "bau", "label": "Stein- und Bauindustrie (Bohren, Abbauen, Zerkleinern, "
                                                  "Schneiden, Schleifen, Strahlen, Bauarbeiten unter Tage)"},
                        {"value": "keramik", "label": "Keramische Industrie (Porzellan, Steingut, Steinzeug, "
                                                      "feuerfeste Erzeugnisse)"},
                        {"value": "giesserei", "label": "Gießereiindustrie"},
                        {"value": "aes_wolle", "label": "Arbeiten mit Hochtemperaturglaswollen (AES-Wollen) "
                                                        "bei über 900 °C"},
                        {"value": "sonstiges", "label": "Anderer Bereich mit Steinstaub oder Mineralstaub"},
                        {"value": "keine", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "hoehere_exposition",
                    "type": "choice",
                    "label": "Üben Sie Tätigkeiten mit besonders hoher Staubbelastung aus "
                             "(z. B. Sandstrahlen, trockenes Schneiden oder Schleifen von Stein "
                             "mit sichtbarer Staubentwicklung, Abbrucharbeiten)?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon an Arbeitsplätzen mit "
                             "Quarzstaub (alle Tätigkeiten zusammengerechnet)?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis10", "label": "1 bis 10 Jahre"},
                        {"value": "10bis15", "label": "10 bis 15 Jahre"},
                        {"value": "ueber15", "label": "Mehr als 15 Jahre"},
                    ],
                },
                {
                    "id": "frueher_staub",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Berufen oder Tätigkeiten Quarz- oder "
                             "Mineralstaub ausgesetzt?",
                    "hint": "Wichtig, weil eine Staublunge auch noch nach dem Ende der "
                            "Belastung entstehen und fortschreiten kann.",
                    "required": True,
                    "followup": {"id": "frueher_staub_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
                {
                    "id": "bystander",
                    "type": "yes_no",
                    "label": "Arbeiten Sie regelmäßig in der Nähe von staubintensiven "
                             "Arbeitsplätzen, ohne selbst dort zu arbeiten (z. B. Nachbarbereich "
                             "mit Schneid- oder Strahlarbeiten)?",
                    "required": True,
                },
                {
                    "id": "tech_schutz",
                    "type": "multi_choice",
                    "label": "Welche technischen Schutzmaßnahmen gibt es an Ihrem Arbeitsplatz?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "absaugung", "label": "Absaugung an Maschinen oder Geräten"},
                        {"value": "nassverfahren", "label": "Nassbearbeitung / Staubbindung mit Wasser"},
                        {"value": "kabine", "label": "Staubfrei belüftete Kabine oder Messwarte"},
                        {"value": "keine", "label": "Keine technischen Schutzmaßnahmen"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei staubender Arbeit Atemschutz "
                             "(persönliche Schutzausrüstung)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "An meinem Arbeitsplatz ist kein Atemschutz "
                                                           "vorgesehen"},
                    ],
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Atembeschwerden",
            "subtitle": "Beschwerden von Atemwegen und Lunge",
            "questions": [
                {
                    "id": "atemnot",
                    "type": "choice",
                    "label": "Haben Sie Atemnot (Luftnot)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "belastung", "label": "Ja, bei körperlicher Anstrengung "
                                                        "(z. B. Treppensteigen, schnelles Gehen)"},
                        {"value": "ruhe", "label": "Ja, schon in Ruhe oder bei leichter Tätigkeit"},
                    ],
                },
                {
                    "id": "husten",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Husten?",
                    "required": True,
                    "followup": {"id": "husten_desc", "type": "text",
                                 "label": "Seit wann, und wie oft?", "when": "yes"},
                },
                {
                    "id": "auswurf",
                    "type": "yes_no",
                    "label": "Haben Sie regelmäßig Auswurf (Schleim beim Husten)?",
                    "required": True,
                },
                {
                    "id": "verschlechterung",
                    "type": "yes_no",
                    "label": "Haben Ihre Atembeschwerden seit der letzten Untersuchung "
                             "zugenommen, oder sind neue Beschwerden aufgetreten?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach", "vorzeitig", "nachgehend"]},
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen von Lunge, Herz und Kreislauf",
            "questions": [
                {
                    "id": "lungenerkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine dieser Lungen- oder Atemwegserkrankungen "
                             "festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "copd", "label": "Chronische Bronchitis oder COPD (dauerhaft verengte "
                                                   "Atemwege)"},
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "emphysem", "label": "Lungenemphysem (überblähte Lunge)"},
                        {"value": "staublunge", "label": "Staublunge (Silikose) oder andere Lungenfibrose "
                                                         "(Vernarbung der Lunge)"},
                        {"value": "pleuritis", "label": "Rippenfellentzündung (Pleuritis), chronisch oder "
                                                        "wiederholt"},
                        {"value": "tumor", "label": "Gutartige oder bösartige Geschwulst der Lunge "
                                                    "(z. B. Lungenkrebs)"},
                        {"value": "keine", "label": "Keine dieser Erkrankungen"},
                    ],
                },
                {
                    "id": "tuberkulose",
                    "type": "choice",
                    "label": "Hatten oder haben Sie eine Tuberkulose (Lungen-Tbc)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "frueher", "label": "Ja, früher – gilt als ausgeheilt"},
                        {"value": "aktiv", "label": "Ja, aktive bzw. derzeit behandelte Tuberkulose"},
                    ],
                },
                {
                    "id": "lunge_op",
                    "type": "yes_no",
                    "label": "Wurden Sie an Lunge oder Brustkorb operiert, oder hatten Sie eine "
                             "Verletzung mit bleibender Beeinträchtigung der Atmung?",
                    "required": True,
                    "followup": {"id": "lunge_op_desc", "type": "text",
                                 "label": "Was genau, und wann?", "when": "yes"},
                },
                {
                    "id": "thorax_deform",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen eine Verformung von Brustkorb oder Wirbelsäule, "
                             "die die Atmung beeinträchtigt?",
                    "required": True,
                },
                {
                    "id": "herz",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine dieser Herz-Kreislauf-Erkrankungen "
                             "festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "insuffizienz", "label": "Herzschwäche (Herzinsuffizienz)"},
                        {"value": "klappe", "label": "Gesicherter Herzklappenfehler oder anderer "
                                                     "organischer Herzschaden"},
                        {"value": "hypertonie", "label": "Bluthochdruck, der sich mit Medikamenten "
                                                         "schlecht einstellen lässt"},
                        {"value": "keine", "label": "Keine dieser Erkrankungen"},
                    ],
                },
                {
                    "id": "chron_krankheit",
                    "type": "yes_no",
                    "label": "Haben Sie andere chronische (dauerhafte) Erkrankungen, die Ihre "
                             "allgemeine Widerstandskraft schwächen?",
                    "required": True,
                    "followup": {"id": "chron_krankheit_desc", "type": "textarea",
                                 "label": "Welche Erkrankungen?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Detaillierte Erfassung des Tabakkonsums (laut Grundsatz G 1.1)",
            "questions": [
                {
                    "id": "rauchstatus",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht (Nie-Raucher/in)"},
                        {"value": "ex", "label": "Nein, ich habe früher geraucht (Ex-Raucher/in)"},
                        {"value": "aktuell", "label": "Ja, ich rauche"},
                    ],
                },
                {
                    "id": "rauch_art",
                    "type": "multi_choice",
                    "label": "Was rauchen bzw. rauchten Sie?",
                    "required": True,
                    "show_if": {"id": "rauchstatus", "in": ["ex", "aktuell"]},
                    "options": [
                        {"value": "zigaretten", "label": "Zigaretten"},
                        {"value": "zigarren", "label": "Zigarren / Zigarillos"},
                        {"value": "pfeife", "label": "Pfeife"},
                        {"value": "sonstiges", "label": "Sonstiges (z. B. E-Zigarette, Shisha)"},
                    ],
                },
                {
                    "id": "rauch_details",
                    "type": "text",
                    "label": "Wie viel pro Tag, seit welchem Jahr, ggf. bis wann? "
                             "(z. B. »10 Zigaretten am Tag, von 2000 bis 2015«)",
                    "required": True,
                    "show_if": {"id": "rauchstatus", "in": ["ex", "aktuell"]},
                },
                {
                    "id": "packungsjahre",
                    "type": "choice",
                    "label": "Wie viele Zigaretten-Packungsjahre kommen bei Ihnen ungefähr "
                             "zusammen?",
                    "hint": "Packungsjahre = Schachteln pro Tag mal Jahre. Beispiel: eine halbe "
                            "Schachtel täglich über 20 Jahre = 10 Packungsjahre.",
                    "required": True,
                    "show_if": {"id": "rauchstatus", "in": ["ex", "aktuell"]},
                    "options": [
                        {"value": "unter10", "label": "Weniger als 10"},
                        {"value": "10bis20", "label": "10 bis 20"},
                        {"value": "20bis30", "label": "20 bis 30"},
                        {"value": "ueber30", "label": "Mehr als 30"},
                        {"value": "unbekannt", "label": "Kann ich nicht einschätzen"},
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
    # ── Bedenkenstatbestände nach 2.1.1 (Dauernde gesundheitliche Bedenken)
    {"wenn": {"lungenerkrankungen": ["staublunge"]},
     "schwere": "kritisch",
     "bereich": "Staublunge/Fibrose",
     "quelle": "Abschnitte 2.1.1 und 2.2",
     "befund": "Bekannte Staublunge (Silikose) oder andere Lungenfibrose angegeben.",
     "konsequenz": "Röntgenologisch fassbare Staublungen und fibrotische/granulomatöse "
                   "Lungenveränderungen sind Bedenkenstatbestand (2.1.1): dauernde "
                   "gesundheitliche Bedenken gegen Aufnahme/Fortsetzung der Exposition "
                   "prüfen. Voraufnahmen beiziehen (ILO-Kodierung), Differenzialdiagnosen "
                   "(z. B. Sarkoidose, miliare Tuberkulose, Histiozytose X) abklären (2.2). "
                   "Bei weniger ausgeprägtem Befund keine Bedenken unter bestimmten "
                   "Voraussetzungen (2.1.3): Tätigkeit mit nachgewiesen geringerer Exposition, "
                   "Verkürzung der 36-Monats-Frist."},
    {"wenn": {"tuberkulose": ["aktiv"]},
     "schwere": "kritisch",
     "bereich": "Tuberkulose",
     "quelle": "Abschnitte 2.1.1 und 3.2.3",
     "befund": "Aktive bzw. in Behandlung befindliche Tuberkulose angegeben.",
     "konsequenz": "Aktive, auch geschlossene Tuberkulose ist Bedenkenstatbestand (2.1.1): "
                   "gesundheitliche Bedenken gegen die Exposition; Klärung vor Aufnahme/"
                   "Fortsetzung der Tätigkeit. Siliko-Tuberkulosen verlaufen schwer und "
                   "therapieresistent (3.2.3). Bei zu erwartender Wiederherstellung befristete "
                   "gesundheitliche Bedenken aussprechen (2.1.2), danach Neubeurteilung."},
    {"wenn": {"lungenerkrankungen": ["tumor"]},
     "schwere": "kritisch",
     "bereich": "Lungentumor",
     "quelle": "Abschnitte 2.1.1 und 4",
     "befund": "Gutartige oder bösartige Geschwulst der Lunge angegeben.",
     "konsequenz": "Benigne Geschwülste und Lungenkrebs sind Bedenkenstatbestand (2.1.1): "
                   "fachärztliche Befunde einholen, Bedenken gegen die Exposition prüfen. "
                   "Hinweis: Bei Silikose plus Lungenkrebs ist eine BK-Anzeige nach "
                   "BK-Nr. 4112 begründet (Abschnitt 4)."},
    {"wenn": {"herz": ["insuffizienz", "klappe"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Herzschwäche, gesicherter Herzklappenfehler oder anderer organischer "
               "Herzschaden angegeben.",
     "konsequenz": "Manifeste oder vorzeitig zu erwartende Herzinsuffizienz (z. B. bei "
                   "gesichertem Herzklappenfehler) ist Bedenkenstatbestand (2.1.1): "
                   "kardiologische Abklärung vor Einsatz; je nach Ausprägung dauernde oder "
                   "befristete Bedenken bzw. keine Bedenken unter Voraussetzungen (2.1.3: "
                   "geringere Exposition, verkürzte Fristen)."},
    # ── Abklärungsbedürftige Angaben (2.1.1 i. V. m. 1.2.3) ───────────────
    {"wenn": {"lungenerkrankungen": ["copd", "asthma", "emphysem", "pleuritis"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 2.1.1, 2.1.3 und 1.2.3",
     "befund": "Chronische Bronchitis/COPD, Asthma, Lungenemphysem oder chronische/"
               "rezidivierende Pleuritis angegeben.",
     "konsequenz": "Nach 2.1.1 möglicher Bedenkenstatbestand – Ausprägung entscheidet: "
                   "Lungenfunktionsprüfung gezielt bewerten, Ergänzungsuntersuchung "
                   "(Bodyplethysmographie, Spiroergometrie, 1.2.3) erwägen. Bei weniger "
                   "ausgeprägtem Befund keine Bedenken unter bestimmten Voraussetzungen "
                   "(2.1.3: geringere Exposition, Verkürzung der Nachuntersuchungsfrist)."},
    {"wenn": {"tuberkulose": ["frueher"]},
     "schwere": "pruefen",
     "bereich": "Tuberkulose",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Früher durchgemachte Tuberkulose angegeben.",
     "konsequenz": "Klären, ob eine ausgedehnte inaktive Tuberkulose vorliegt (Bedenken-"
                   "statbestand nach 2.1.1): Vorbefunde und ältere Röntgenaufnahmen "
                   "(nicht älter als 1 Jahr direkt verwertbar) einbeziehen; danach Beurteilung "
                   "nach 2.1."},
    {"wenn": {"lunge_op": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lungen-OP/Verletzung",
     "quelle": "Abschnitte 2.1.1 und 1.2.3",
     "befund": "Operation oder Verletzung von Lunge/Brustkorb mit Beeinträchtigung angegeben.",
     "konsequenz": "Zustand nach Lungenresektion oder -verletzung mit Funktionsbeeinträchtigung "
                   "der Brustorgane ist Bedenkenstatbestand (2.1.1): OP-Berichte einholen, "
                   "Lungenfunktion prüfen, ggf. Ergänzungsuntersuchung (1.2.3); Beurteilung "
                   "nach 2.1."},
    {"wenn": {"thorax_deform": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Thoraxdeformität",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Verformung von Brustkorb oder Wirbelsäule mit Atembeeinträchtigung angegeben.",
     "konsequenz": "Nach 2.1.1 Bedenkenstatbestand, sofern die Atmung beeinträchtigt ist: "
                   "Ausmaß mittels Lungenfunktionsprüfung objektivieren; Beurteilung nach "
                   "2.1, ggf. keine Bedenken unter Voraussetzungen (2.1.3)."},
    {"wenn": {"herz": ["hypertonie"]},
     "schwere": "pruefen",
     "bereich": "Bluthochdruck",
     "quelle": "Abschnitte 2.1.1 und 2.1.2",
     "befund": "Therapeutisch schlecht einstellbarer Bluthochdruck angegeben.",
     "konsequenz": "Bluthochdruck, insbesondere wenn therapeutisch nicht einstellbar, ist "
                   "Bedenkenstatbestand (2.1.1): Blutdruckeinstellung hausärztlich/"
                   "internistisch optimieren lassen; bis zur Wiederherstellung befristete "
                   "gesundheitliche Bedenken erwägen (2.1.2)."},
    {"wenn": {"chron_krankheit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Chronische Erkrankung",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Sonstige chronische Erkrankung mit geschwächter Widerstandskraft angegeben.",
     "konsequenz": "Sonstige chronische Krankheiten, die die allgemeine Widerstandskraft "
                   "herabsetzen, sind Bedenkenstatbestand (2.1.1): Art und Schwere ärztlich "
                   "bewerten, Vorbefunde einholen; Beurteilung nach 2.1."},
    # ── Beschwerden und Verlauf ───────────────────────────────────────────
    {"wenn": {"atemnot": ["ruhe"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 2.1.1, 2.1.2 und 1.2.3",
     "befund": "Atemnot bereits in Ruhe bzw. bei leichter Tätigkeit angegeben.",
     "konsequenz": "Verdacht auf erhebliche Störung der Lungenfunktion (2.1.1): "
                   "Ergänzungsuntersuchung (Bodyplethysmographie, Spiroergometrie, 1.2.3) "
                   "und Röntgen-Thorax p. a. veranlassen. Während der Abklärung eines "
                   "unklaren Befundes befristete gesundheitliche Bedenken (2.1.2)."},
    {"wenn": {"husten": ["yes"], "auswurf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 3.2.3 und 1.2.3",
     "befund": "Husten und Auswurf angegeben (Beschwerdetrias mit Luftnot beachten).",
     "konsequenz": "Hinweis auf chronische Bronchitis/CURS (3.2.3): Lungenfunktionsprüfung "
                   "gezielt auswerten, in begründeten Fällen Ergänzungsuntersuchung (1.2.3); "
                   "Beurteilung nach 2.1, ggf. Fristverkürzung (2.1.3)."},
    {"wenn": {"verschlechterung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Verlauf",
     "quelle": "Abschnitte 1.2.2, 1.2.3 und 2.1.2",
     "befund": "Zunahme bzw. Neuauftreten von Atembeschwerden seit der letzten Untersuchung.",
     "konsequenz": "Zwischenanamnese auffällig: rechtfertigende Indikation für Röntgen-Thorax "
                   "p. a. im Einzelfall prüfen (1.2.2); bei unklarer Morphologie qualifizierte "
                   "Low-dose-Volumen-CT nach sorgfältiger Indikationsstellung (1.2.3, "
                   "ICOERD-Befundung). Während der Abklärung befristete Bedenken möglich "
                   "(2.1.2)."},
    {"wenn": {"laengere_krankheit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1",
     "befund": "Mehrwöchige Erkrankung bzw. körperliche Beeinträchtigung seit der letzten "
               "Untersuchung angegeben.",
     "konsequenz": "Nach 1.1 Anlass für eine vorzeitige Nachuntersuchung: vollständiges "
                   "Untersuchungsprogramm (allgemeine und spezielle Untersuchung) vor "
                   "Fortsetzung der Exposition durchführen; prüfen, ob die Erkrankung "
                   "Bedenken gegen die Fortsetzung begründet (2.1)."},
    # ── Exposition und Schutzmaßnahmen ────────────────────────────────────
    {"wenn": {"hoehere_exposition": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Hohe Exposition",
     "quelle": "Abschnitt 1.2.2 (i. V. m. DGUV Information 240-011)",
     "befund": "Tätigkeit mit höherer Exposition gegenüber silikogenem Staub angegeben.",
     "konsequenz": "Bei Nachuntersuchungen ist bei Tätigkeiten mit höherer Exposition eine "
                   "Röntgenaufnahme des Thorax im p. a.-Strahlengang vorgesehen (1.2.2); "
                   "rechtfertigende Indikation abhängig von der Zwischenanamnese prüfen, "
                   "ILO-Kodierung, Voraufnahmen vergleichen. Nachuntersuchungsfrist von "
                   "36 Monaten einhalten, ggf. verkürzen (2.1.3)."},
    {"wenn": {"expo_dauer": ["ueber15"]},
     "schwere": "hinweis",
     "bereich": "Expositionsdauer",
     "quelle": "Abschnitt 3.2.3",
     "befund": "Mehr als 15 Jahre Exposition gegenüber silikogenem Staub.",
     "konsequenz": "Die Latenzzeit bis zum Auftreten einer Silikose beträgt größenordnungs-"
                   "mäßig 15 Jahre und mehr (3.2.3): auf Frühzeichen achten, Röntgenbefunde "
                   "im Verlauf vergleichen, Nachuntersuchungsintervalle konsequent einhalten."},
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 2.2",
     "befund": "Atemschutz wird bei staubender Arbeit selten oder nie getragen.",
     "konsequenz": "Individuelle Aufklärung und Beratung zu Schutzmaßnahmen; ergeben sich "
                   "Anhaltspunkte für unzureichende Schutzmaßnahmen, Mitteilung an den "
                   "Unternehmer und Vorschlag von Schutzmaßnahmen (2.2), ggf. Aktualisierung "
                   "der Gefährdungsbeurteilung anregen."},
    {"wenn": {"bystander": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Bystander-Exposition",
     "quelle": "Abschnitt 2.2",
     "befund": "Regelmäßiger Aufenthalt in der Nähe staubintensiver Arbeitsplätze.",
     "konsequenz": "Mögliche Gefährdung als »Bystander« dem Unternehmer mitteilen und "
                   "Schutzmaßnahmen vorschlagen; Beratung im Hinblick auf geeignete "
                   "persönliche Schutzausrüstung (2.2)."},
    # ── Rauchen und nachgehende Untersuchung ──────────────────────────────
    {"wenn": {"rauchstatus": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 2.2",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung: Zigarettenrauchen ist die Hauptursache für Lungenkrebs und "
                   "chronisch obstruktive Atemwegserkrankungen; mögliche Gefährdung der "
                   "weiteren Beschäftigungsfähigkeit erläutern und auf Angebote zur "
                   "Raucherentwöhnung hinweisen (2.2). Packungsjahre dokumentieren."},
    {"wenn": {"unt_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitt 1.1",
     "befund": "Nachgehende Untersuchung nach Beendigung der Beschäftigung.",
     "konsequenz": "Nachgehende Untersuchungen nach Beendigung der Beschäftigung fortführen "
                   "(1.1); bei früherer Exposition gegenüber fibrogenen Grubenstäuben hat der "
                   "Unternehmer nach § 3 GesBergV Untersuchungen in Abständen von längstens "
                   "fünf Jahren zu ermöglichen. Untersuchungsprogramm wie Nachuntersuchung."},
]
