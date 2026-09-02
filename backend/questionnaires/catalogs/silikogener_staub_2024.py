# -*- coding: utf-8 -*-
"""Silikogener Staub – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Silikogener Staub« (E SIS, Fassung Januar 2022), S. 566–611."""

SLUG = "silikogener_staub-2024"

CATALOG = {
    "version": 2,
    "title": "Silikogener Staub (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Silikogener Staub« (E SIS, Fassung Januar 2022), S. 566–611",
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
                             "Quarzstaub (silikogenem Staub)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge wegen Quarzstaub"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zu dieser Vorsorge"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge – ich übe die "
                                                         "Tätigkeit mit Quarzstaub nicht mehr aus"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn bei der "
                            "Arbeit eine wiederholte Belastung durch Quarzstaub nicht "
                            "ausgeschlossen werden kann. Angebotsvorsorge: Ihr Betrieb bietet "
                            "sie an, wenn eine Belastung möglich ist.",
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
        # ── 2 ─ Tätigkeit und Staubbelastung ───────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Staubbelastung",
            "subtitle": "Ihre Arbeit mit quarzhaltigem Staub",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich, Einsatzort)?",
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
                        {"value": "bergbau", "label": "Berg-, Stollen- oder Tunnelbau (Vortrieb, Abbau, Förderung)"},
                        {"value": "bau", "label": "Naturstein- oder Bauindustrie (Bohren, Zerkleinern, "
                                                  "Schneiden, Schleifen, Strahlen, Abbruch)"},
                        {"value": "keramik", "label": "Keramische oder Glasindustrie (Porzellan, Steingut, "
                                                      "Fliesen, Ziegel, feuerfeste Erzeugnisse)"},
                        {"value": "giesserei", "label": "Gießerei- oder Metallindustrie (Formerei, Entkernen, "
                                                        "Gussputzen)"},
                        {"value": "quarz_aufbereitung", "label": "Gewinnen, Mahlen, Abfüllen oder Verpacken von "
                                                                 "Quarzsand oder Quarzmehl"},
                        {"value": "feuerfest", "label": "Einbringen oder Ausbrechen feuerfester Materialien "
                                                        "(z. B. Öfen, Kessel, Glaswannen)"},
                        {"value": "sonstiges", "label": "Anderer Bereich mit Steinstaub oder Mineralstaub"},
                        {"value": "keine", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "hochexposition",
                    "type": "multi_choice",
                    "label": "Führen Sie eine oder mehrere dieser besonders staubintensiven "
                             "Arbeiten aus?",
                    "hint": "Mehrfachauswahl möglich. Diese Arbeiten gelten als Tätigkeiten "
                            "mit höherer Quarzstaub-Belastung.",
                    "required": True,
                    "options": [
                        {"value": "trockenbearbeitung", "label": "Trockenes Schneiden, Schleifen, Fräsen oder "
                                                                 "Schlitzen von Stein/Beton mit sichtbarer "
                                                                 "Staubentwicklung"},
                        {"value": "strahlen", "label": "Druckluft-Strahlarbeiten mit trockenem Strahlmittel "
                                                       "(z. B. Sandstrahlen)"},
                        {"value": "abbruch", "label": "Abbrucharbeiten oder Beräumen von Sprengstellen ohne "
                                                      "Staubniederschlagung mit Wasser"},
                        {"value": "feuerfest_ausbruch", "label": "Ausbrechen quarzhaltiger feuerfester "
                                                                 "Materialien aus Öfen oder Kesseln"},
                        {"value": "giesserei_arbeiten", "label": "Entformen, Entkernen, Gussputzen oder "
                                                                 "Brennschneiden sandbehafteter Gussstücke"},
                        {"value": "abfuellen", "label": "Verwiegen, Absacken oder Abfüllen trockener "
                                                        "quarzhaltiger Materialien ohne Absaugung"},
                        {"value": "wartung", "label": "Reinigungs-, Wartungs- oder Reparaturarbeiten mit "
                                                      "Quarzfeinstaub (z. B. Filterkammern)"},
                        {"value": "keine", "label": "Keine dieser Arbeiten"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit Belastung durch "
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
                    "hint": "Wichtig, weil eine Staublunge auch noch Jahre nach dem Ende "
                            "der Belastung entstehen und fortschreiten kann.",
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
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Technischer Schutz und Atemschutz an Ihrem Arbeitsplatz",
            "questions": [
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
                    "label": "Tragen Sie bei staubender Arbeit Atemschutz?",
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
                {
                    "id": "atemschutz_typ",
                    "type": "text",
                    "label": "Welchen Atemschutz benutzen Sie (z. B. FFP2-/FFP3-Maske, "
                             "Gebläsefilter-Haube)?",
                    "required": False,
                    "show_if": {"id": "atemschutz", "in": ["immer", "meist", "selten"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
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
                    "id": "heiserkeit",
                    "type": "yes_no",
                    "label": "Sind Sie seit mehreren Wochen anhaltend heiser?",
                    "required": True,
                },
                {
                    "id": "verschlechterung",
                    "type": "yes_no",
                    "label": "Haben Ihre Atembeschwerden seit der letzten Vorsorge zugenommen, "
                             "oder sind neue Beschwerden aufgetreten?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
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
                        {"value": "silikose", "label": "Staublunge (Silikose) oder andere Lungenfibrose "
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
                    "id": "herz_kreislauf",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine dieser Herz-Kreislauf-Erkrankungen "
                             "festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "herzinsuffizienz", "label": "Herzschwäche (Herzinsuffizienz)"},
                        {"value": "klappenfehler", "label": "Herzklappenfehler oder anderer organischer "
                                                            "Herzschaden"},
                        {"value": "hypertonie_schwer", "label": "Bluthochdruck, der sich mit Medikamenten "
                                                                "schlecht einstellen lässt"},
                        {"value": "keine", "label": "Keine dieser Erkrankungen"},
                    ],
                },
                {
                    "id": "systemerkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Systemerkrankung, die auch die Lunge betreffen kann "
                             "(z. B. Sarkoidose, Rheuma, Kollagenose)?",
                    "required": True,
                    "followup": {"id": "systemerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "chron_krankheit",
                    "type": "yes_no",
                    "label": "Haben Sie andere chronische (dauerhafte) Erkrankungen?",
                    "required": True,
                    "followup": {"id": "chron_krankheit_desc", "type": "textarea",
                                 "label": "Welche Erkrankungen?", "when": "yes"},
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "textarea",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Ihr Tabakkonsum – wichtig für die Beurteilung Ihrer Lunge",
            "questions": [
                {
                    "id": "rauchstatus",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
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
                             "(z. B. »10 Zigaretten am Tag, von 2005 bis 2020«)",
                    "required": True,
                    "show_if": {"id": "rauchstatus", "in": ["ex", "aktuell"]},
                },
                {
                    "id": "packungsjahre",
                    "type": "choice",
                    "label": "Wie viele Packungsjahre kommen bei Ihnen ungefähr zusammen?",
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
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"lungenerkrankungen": ["silikose"]},
     "schwere": "pruefen",
     "bereich": "Staublunge/Fibrose",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Bekannte Staublunge (Silikose) oder andere Lungenfibrose angegeben.",
     "konsequenz": "Röntgenologisch fassbare Staublungen sind beurteilungsrelevant (7.4): "
                   "Vorbefunde und Voraufnahmen beiziehen (ILO-Kodierung, Vergleich), "
                   "erweiterte Lungenfunktionsdiagnostik (z. B. Ganzkörperplethysmographie) "
                   "erwägen. Prüfen, ob die Tätigkeit ohne Gefährdung möglich ist: Maßnahmen "
                   "nach 7.4.2 (z. B. Einsatz mit geringerer Exposition), verkürzte "
                   "Vorsorgefristen nach 7.4.3; ohne Aussicht auf Erfolg Tätigkeitswechsel "
                   "nach 7.4.4 erwägen (Mitteilung nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"lungenerkrankungen": ["tumor"]},
     "schwere": "pruefen",
     "bereich": "Lungentumor",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Gutartige oder bösartige Geschwulst der Lunge angegeben.",
     "konsequenz": "Geschwülste und Lungenkrebs sind beurteilungsrelevant (7.4). Aktuelle "
                   "fachärztliche Befunde einholen; bei Tumorverdacht in der p. a.-Thorax-"
                   "aufnahme qualifizierte CT-Untersuchung nach Tumorprotokoll veranlassen "
                   "(ohne Zweitbeurteiler, 7.2.2). Maßnahmen nach 7.4.2–7.4.4 prüfen."},
    {"wenn": {"tuberkulose": ["aktiv"]},
     "schwere": "pruefen",
     "bereich": "Tuberkulose",
     "quelle": "Abschnitte 6.3.3 und 7.4",
     "befund": "Aktive bzw. in Behandlung befindliche Tuberkulose angegeben.",
     "konsequenz": "Aktive, auch geschlossene Tuberkulose ist beurteilungsrelevant (7.4); bei "
                   "Silikose verlaufen Tuberkulosen schwerer und therapieresistenter (6.3.3). "
                   "Behandlungsstand fachärztlich klären, bevor die Exposition aufgenommen "
                   "oder fortgesetzt wird; Maßnahmen nach 7.4.2, verkürzte Fristen nach 7.4.3, "
                   "ggf. Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"tuberkulose": ["frueher"]},
     "schwere": "pruefen",
     "bereich": "Tuberkulose",
     "quelle": "Abschnitt 7.4",
     "befund": "Früher durchgemachte Tuberkulose angegeben.",
     "konsequenz": "Klären, ob eine ausgedehnte inaktive Tuberkulose vorliegt (nach 7.4 "
                   "beurteilungsrelevant): Vorbefunde und ältere Röntgenaufnahmen (nicht älter "
                   "als 1 Jahr direkt verwertbar) einbeziehen; Beurteilung nach 7.4."},
    {"wenn": {"lungenerkrankungen": ["copd", "asthma", "emphysem", "pleuritis"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Chronische Bronchitis/COPD, Asthma, Lungenemphysem oder chronische/"
               "rezidivierende Pleuritis angegeben.",
     "konsequenz": "Nach 7.4 beurteilungsrelevante Erkrankung: Spirometrie gezielt bewerten, "
                   "erweiterte Lungenfunktionsdiagnostik (Bronchodilatationstest, Ganzkörper-"
                   "plethysmographie) in Betracht ziehen (7.2.2). Je nach Ausprägung Maßnahmen "
                   "nach 7.4.2 (z. B. Expositionsminderung, geeignete PSA) und verkürzte "
                   "Vorsorgefristen nach 7.4.3 empfehlen."},
    {"wenn": {"lunge_op": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lungen-OP/Verletzung",
     "quelle": "Abschnitt 7.4",
     "befund": "Operation oder Verletzung von Lunge/Brustkorb mit Beeinträchtigung angegeben.",
     "konsequenz": "Zustand nach Lungenresektion oder -verletzung mit Funktionsbeeinträchtigung "
                   "ist beurteilungsrelevant (7.4): OP-Berichte einholen, Lungenfunktion "
                   "gezielt prüfen; Maßnahmen nach 7.4.2/7.4.3 erwägen."},
    {"wenn": {"thorax_deform": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Thoraxdeformität",
     "quelle": "Abschnitt 7.4",
     "befund": "Verformung von Brustkorb oder Wirbelsäule mit Atembeeinträchtigung angegeben.",
     "konsequenz": "Nach 7.4 beurteilungsrelevant, sofern die Atmung beeinträchtigt ist: "
                   "Ausmaß der Ventilationsstörung mittels Lungenfunktionsprüfung objektivieren; "
                   "Beurteilung und ggf. Maßnahmen nach 7.4.2."},
    {"wenn": {"herz_kreislauf": ["herzinsuffizienz", "klappenfehler", "hypertonie_schwer"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 7.4",
     "befund": "Herzschwäche, Herzklappenfehler/organischer Herzschaden oder schlecht "
               "einstellbarer Bluthochdruck angegeben.",
     "konsequenz": "Manifeste oder vorzeitig zu erwartende Herzinsuffizienz sowie "
                   "therapeutisch nicht einstellbarer Bluthochdruck sind beurteilungsrelevant "
                   "(7.4): kardiologische bzw. hausärztlich/internistische Vorbefunde "
                   "einholen, kardiopulmonale Belastbarkeit klären und die Blutdruck-"
                   "einstellung optimieren lassen; Maßnahmen nach 7.4.2 und verkürzte "
                   "Vorsorgefristen nach 7.4.3 erwägen."},
    {"wenn": {"systemerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Systemerkrankung",
     "quelle": "Abschnitt 7.1 (Anamnese) und 7.4",
     "befund": "Systemerkrankung mit möglicher Lungenbeteiligung angegeben.",
     "konsequenz": "Fibrotische und granulomatöse Lungenveränderungen sind beurteilungsrelevant "
                   "(7.4): fachärztliche Vorbefunde einholen, Lungenbeteiligung abklären "
                   "(erweiterte Lungenfunktionsdiagnostik nach 7.2.2 erwägen)."},
    # ── Beschwerden (Abschnitte 6.3, 7.1, 7.2.2) ──────────────────────────
    {"wenn": {"atemnot": ["ruhe"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 6.3.3, 7.1 und 7.2.2",
     "befund": "Atemnot bereits in Ruhe bzw. bei leichter Tätigkeit angegeben.",
     "konsequenz": "Klinischer Verdacht auf eine Lungenerkrankung: erweiterte Lungenfunktions-"
                   "diagnostik (Bronchodilatationstest, Ganzkörperplethysmographie) veranlassen; "
                   "die Indikation für eine Röntgenaufnahme des Thorax ist bei klinischem "
                   "Verdacht unabhängig von Alter und Expositionsbeginn gegeben (7.2.2). "
                   "Beurteilung nach 7.4, ggf. verkürzte Frist nach 7.4.3."},
    {"wenn": {"husten": ["yes"], "auswurf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Husten und Auswurf angegeben (Beschwerdetrias mit Atemnot beachten).",
     "konsequenz": "Hinweis auf chronische Bronchitis/COPD: Spirometrie gezielt auswerten, "
                   "erweiterte Lungenfunktionsdiagnostik in Betracht ziehen; bei klinischem "
                   "Verdacht auf eine Lungenerkrankung Röntgen-Thorax p. a. indiziert (7.2.2). "
                   "Beratung zum Zusammenhang mit exogenen Faktoren (8.1)."},
    {"wenn": {"verschlechterung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Verlauf",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Zunahme bzw. Neuauftreten von Atembeschwerden seit der letzten Vorsorge.",
     "konsequenz": "Aktualisierte Anamnese mit tätigkeitsspezifischen Symptomen vertiefen; "
                   "rechtfertigende Indikation für Röntgen-Thorax p. a. im Einzelfall prüfen. "
                   "Bei unklarem Röntgenbefund Low-Dose-Volumen-HRCT erwägen – dazu "
                   "Zweitbeurteiler hören (Verzeichnis bei GVS bzw. Landesverbänden, 7.2.2)."},
    {"wenn": {"heiserkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitt 8.1",
     "befund": "Länger andauernde Heiserkeit angegeben.",
     "konsequenz": "Zeitnahe Vorstellung in einer HNO-ärztlichen Praxis empfehlen (8.1: bei "
                   "länger andauernder Heiserkeit im Untersuchungsintervall HNO-Praxis "
                   "aufsuchen)."},
    # ── Exposition und Schutzmaßnahmen (Abschnitte 6.1, 7.2.2, 8.2) ───────
    {"wenn": {"expo_dauer": ["10bis15", "ueber15"]},
     "schwere": "pruefen",
     "bereich": "Expositionsdauer",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Langjährige Exposition gegenüber silikogenem Staub (10 Jahre oder mehr).",
     "konsequenz": "Erfahrungsgemäß ist eine Röntgenaufnahme des Thorax zur Erkennung einer "
                   "staubbedingten Berufskrankheit erst nach ca. 10–15 Jahren Exposition "
                   "indiziert: rechtfertigende Indikation im Einzelfall unter Berücksichtigung "
                   "der Expositionshöhe prüfen (7.2.2); Befundung nach ILO, Voraufnahmen "
                   "vergleichen. Silikose-Latenz ~15 Jahre beachten (6.3.3)."},
    {"wenn": {"hochexposition": ["trockenbearbeitung", "strahlen", "abbruch",
                                 "feuerfest_ausbruch", "giesserei_arbeiten",
                                 "abfuellen", "wartung"]},
     "schwere": "pruefen",
     "bereich": "Hohe Exposition",
     "quelle": "Abschnitte 6.1.1, 2 (Hinweise) und 8.2",
     "befund": "Arbeitsverfahren/Tätigkeit mit höherer Exposition nach 6.1.1 angegeben.",
     "konsequenz": "Abgleich mit der Gefährdungsbeurteilung; Einhaltung des Beurteilungs-"
                   "maßstabs 50 µg/m³ (TRGS 559) thematisieren. Expositionshöhe bei der "
                   "Röntgenindikation berücksichtigen (7.2.2). Ergeben sich Anhaltspunkte, "
                   "dass Schutzmaßnahmen nicht ausreichen: Mitteilung an das Unternehmen und "
                   "Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV, 8.2)."},
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Atemschutz",
     "quelle": "Abschnitte 7.1, 8.1 und 8.2",
     "befund": "Atemschutz wird bei staubender Arbeit selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zu Vermeiden der Inhalation, Hygiene am Arbeitsplatz, "
                   "Wechsel der Arbeitskleidung und konsequentem Tragen der PSA (7.1/8.1). "
                   "Ursachen klären; bei unzureichenden Schutzmaßnahmen Mitteilung an das "
                   "Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV, 8.2)."},
    {"wenn": {"bystander": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Bystander-Exposition",
     "quelle": "Abschnitt 6.1",
     "befund": "Regelmäßiger Aufenthalt in der Nähe staubintensiver Arbeitsplätze.",
     "konsequenz": "Exposition durch benachbarte Arbeitsbereiche (Bystander) bei der "
                   "Gefährdungsbeurteilung berücksichtigen lassen; Gesamtbild der Belastung "
                   "durch zeitliche Gewichtung aller Tätigkeiten erheben (6.1); ggf. Vorsorge-"
                   "pflicht des Betriebs klären."},
    # ── Rauchen und nachgehende Vorsorge ──────────────────────────────────
    {"wenn": {"rauchstatus": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Entwöhnungsberatung anbieten (7.1). Beratung: Zigarettenrauchen ist die "
                   "Hauptursache für Lungenkrebs; zusätzliches Risiko durch die "
                   "krebserzeugende Wirkung von Quarzfeinstaub erläutern (8.1). "
                   "Packungsjahre dokumentieren."},
    {"wenn": {"vorsorge_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2, 7.2.2 und 8.1; Anlage 2",
     "befund": "Nachgehende Vorsorge nach Ende der Tätigkeit mit silikogenem Staub.",
     "konsequenz": "Untersuchungsprogramm wie Nachuntersuchung (7.2.2). Anmeldung über das "
                   "Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de) sicherstellen; über "
                   "Sinn der nachgehenden Vorsorge bei krebserzeugender Exposition informieren "
                   "(8.1). Ggf. Teilnahme am erweiterten Vorsorgeangebot EVA-Lunge "
                   "(LD-HRCT-Früherkennung, Anlage 2) prüfen."},
    {"wenn": {"frueher_staub": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 2, 6.3.3 und 8.1",
     "befund": "Frühere Tätigkeiten mit Quarz-/Mineralstaub-Exposition angegeben.",
     "konsequenz": "Frühere Expositionen dokumentieren und bei der kumulativen Belastung "
                   "berücksichtigen – Quarzstaublungenveränderungen können auch Jahre nach "
                   "Expositionsende auftreten und fortschreiten (6.3.3). Prüfen, ob eine "
                   "Anmeldung zur nachgehenden Vorsorge (»DGUV Vorsorge«) erfolgt ist."},
]
