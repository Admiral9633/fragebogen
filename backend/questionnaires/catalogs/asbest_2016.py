# -*- coding: utf-8 -*-
"""G 1.2 Mineralischer Staub, Teil 2: Asbestfaserhaltiger Staub – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016,
G 1.2 (Fassung Oktober 2014), S. 77–96."""

SLUG = "g1-2-asbest-2016"

CATALOG = {
    "version": 2,
    "title": "G 1.2 Asbestfaserhaltiger Staub (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 1.2 »Mineralischer Staub, Teil 2: Asbestfaserhaltiger Staub« "
             "(Fassung Oktober 2014), S. 77–96",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich heute?",
                    "hint": "Nachuntersuchungen finden nach 12 bis 36 Monaten statt. "
                            "Nachgehende Untersuchungen werden nach dem Ende der Tätigkeit "
                            "mit Asbest angeboten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich arbeite weiter mit möglichem Asbest-Kontakt)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (die Tätigkeit mit Asbest ist beendet)"},
                    ],
                },
                {
                    "id": "alter_gruppe",
                    "type": "choice",
                    "label": "Wie alt sind Sie?",
                    "hint": "Ab dem vollendeten 45. Lebensjahr kann eine Röntgenaufnahme der "
                            "Lunge sinnvoll sein.",
                    "required": True,
                    "options": [
                        {"value": "unter_45", "label": "Unter 45 Jahre"},
                        {"value": "45_plus", "label": "45 Jahre oder älter"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Asbest-Belastung ─────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Asbest-Belastung",
            "subtitle": "Ihre Arbeit und der mögliche Kontakt mit Asbestfasern",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "asbest_arbeiten",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten können Sie mit Asbest in Kontakt kommen?",
                    "hint": "Mehrfachauswahl möglich. Seit 1993 ist Asbest verboten; Kontakt ist "
                            "vor allem bei Abbruch-, Sanierungs- und Instandhaltungsarbeiten "
                            "(ASI) an alten Materialien möglich.",
                    "required": True,
                    "options": [
                        {"value": "asi", "label": "Abbruch-, Sanierungs- oder Instandhaltungsarbeiten an asbesthaltigen Materialien (TRGS 519)"},
                        {"value": "rohstoffe", "label": "Arbeiten mit mineralischen Rohstoffen, die Asbest enthalten können (TRGS 517)"},
                        {"value": "frueher_industrie", "label": "Frühere Arbeit in der Asbestindustrie (z. B. Asbestzement, Isolierung, Bremsbeläge, Schiffbau)"},
                        {"value": "keine", "label": "Keine davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "asbest_beginn",
                    "type": "choice",
                    "label": "Wann hatten Sie zum ersten Mal beruflich Kontakt mit Asbest "
                             "(auch in früheren Tätigkeiten)?",
                    "required": True,
                    "options": [
                        {"value": "vor_mehr_15", "label": "Vor mehr als 15 Jahren"},
                        {"value": "unter_15", "label": "Vor 15 Jahren oder weniger"},
                        {"value": "noch_nicht", "label": "Bisher noch gar nicht / Tätigkeit beginnt erst"},
                    ],
                },
                {
                    "id": "asbest_dauer",
                    "type": "choice",
                    "label": "Wie viele Jahre haben Sie insgesamt mit möglichem Asbest-Kontakt gearbeitet?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht"},
                        {"value": "unter_1", "label": "Weniger als 1 Jahr"},
                        {"value": "1_bis_10", "label": "1 bis 10 Jahre"},
                        {"value": "ueber_10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "fruehere_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren, inzwischen beendeten Tätigkeiten Kontakt "
                             "mit Asbest (z. B. vor dem Asbestverbot 1993)?",
                    "required": True,
                    "followup": {"id": "fruehere_expo_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, in welchem Zeitraum?", "when": "yes"},
                },
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit möglichem Asbest-Kontakt Atemschutz "
                             "(z. B. Maske) und Schutzkleidung?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_kontakt", "label": "Ich habe (noch) keinen Asbest-Kontakt"},
                    ],
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden an Atemwegen, Lunge und Kehlkopf",
            "questions": [
                {
                    "id": "husten",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Husten (z. B. Reizhusten)?",
                    "required": True,
                },
                {
                    "id": "auswurf",
                    "type": "yes_no",
                    "label": "Haben Sie regelmäßig Auswurf (Schleim beim Husten)?",
                    "required": True,
                },
                {
                    "id": "atemnot",
                    "type": "choice",
                    "label": "Haben Sie Atemnot (Luftnot)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "belastung_stark", "label": "Ja, nur bei starker körperlicher Anstrengung"},
                        {"value": "belastung_leicht", "label": "Ja, schon bei leichter Anstrengung (z. B. Treppensteigen)"},
                        {"value": "ruhe", "label": "Ja, auch in Ruhe"},
                    ],
                },
                {
                    "id": "heiserkeit_3w",
                    "type": "yes_no",
                    "label": "Sind Sie seit mehr als 3 Wochen anhaltend heiser?",
                    "hint": "Länger anhaltende Heiserkeit muss wegen der Gefahr einer "
                            "Kehlkopferkrankung abgeklärt werden.",
                    "required": True,
                },
                {
                    "id": "stimm_missempfindungen",
                    "type": "yes_no",
                    "label": "Haben Sie Stimmstörungen, Schluckbeschwerden oder ein "
                             "Fremdkörpergefühl im Hals (»Kloß im Hals«)?",
                    "required": True,
                    "followup": {"id": "stimm_missempfindungen_desc", "type": "text",
                                 "label": "Was genau, und seit wann?", "when": "yes"},
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "mehrwöchige Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie, dass gesundheitliche Beschwerden bei Ihnen mit Ihrer "
                             "Tätigkeit am Arbeitsplatz zusammenhängen?",
                    "required": True,
                    "followup": {"id": "zusammenhang_vermutet_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den Zusammenhang?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen von Lunge, Kehlkopf und Herz-Kreislauf-System",
            "questions": [
                {
                    "id": "lunge_vorerkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Lungen- oder "
                             "Atemwegserkrankungen festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "bronchitis", "label": "Chronische Bronchitis (dauerhafte Entzündung der Bronchien)"},
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "emphysem", "label": "Lungenemphysem (überblähte Lunge)"},
                        {"value": "pleuritis", "label": "Rippenfellentzündung (Pleuritis), dauerhaft oder wiederholt"},
                        {"value": "staublunge", "label": "Staublunge, Lungenfibrose oder andere Vernarbung der Lunge"},
                        {"value": "tuberkulose", "label": "Tuberkulose (auch ausgeheilte, ausgedehnte Tuberkulose)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "lunge_op_trauma",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen ein Teil der Lunge entfernt, oder hatten Sie eine "
                             "Lungen- oder Brustkorbverletzung mit bleibenden Folgen?",
                    "required": True,
                    "followup": {"id": "lunge_op_trauma_desc", "type": "text",
                                 "label": "Was genau, und wann?", "when": "yes"},
                },
                {
                    "id": "thorax_deformitaet",
                    "type": "yes_no",
                    "label": "Haben Sie eine Verformung des Brustkorbs oder der Wirbelsäule, "
                             "die Ihre Atmung beeinträchtigt?",
                    "required": True,
                },
                {
                    "id": "kehlkopf",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine Erkrankung des Kehlkopfs festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "chronisch", "label": "Dauerhafte (chronische) Kehlkopferkrankung mit Beschwerden"},
                        {"value": "op_bestrahlung", "label": "Operation oder Bestrahlung an Stimmband oder Kehlkopf (z. B. wegen einer Geschwulst)"},
                        {"value": "neoplasie", "label": "Bekannte Zellveränderung der Kehlkopfschleimhaut (intraepitheliale Neoplasie)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "herz_kreislauf",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine Herz-Kreislauf-Erkrankung festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "insuffizienz", "label": "Herzschwäche (Herzinsuffizienz)"},
                        {"value": "klappenfehler", "label": "Herzklappenfehler oder anderer organischer Herzschaden"},
                        {"value": "hypertonie", "label": "Bluthochdruck, der trotz Medikamenten nicht gut einstellbar ist"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine asbestbedingte Erkrankung als Berufskrankheit "
                             "angezeigt oder anerkannt, oder läuft ein solches Verfahren "
                             "(z. B. Asbestose, Rippenfell-Veränderungen, Kehlkopferkrankung)?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Erkrankung, Stand des Verfahrens?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Rauchen und Alkohol ────────────────────────────────────────
        {
            "id": "rauchen_alkohol",
            "title": "Rauchen & Alkohol",
            "subtitle": "Rauchen erhöht das Lungenkrebsrisiko bei Asbest-Kontakt besonders stark",
            "questions": [
                {
                    "id": "rauchstatus",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht (Nie-Raucher/in)"},
                        {"value": "ehemals", "label": "Nein, aber früher habe ich geraucht (Ex-Raucher/in)"},
                        {"value": "aktuell", "label": "Ja, ich rauche"},
                    ],
                },
                {
                    "id": "tabak_art",
                    "type": "multi_choice",
                    "label": "Was rauchen bzw. rauchten Sie?",
                    "required": True,
                    "show_if": {"id": "rauchstatus", "in": ["ehemals", "aktuell"]},
                    "options": [
                        {"value": "zigaretten", "label": "Zigaretten"},
                        {"value": "zigarren", "label": "Zigarren/Zigarillos"},
                        {"value": "pfeife", "label": "Pfeife"},
                    ],
                },
                {
                    "id": "packungsjahre",
                    "type": "choice",
                    "label": "Wie viele »Packungsjahre« kommen bei Ihnen ungefähr zusammen?",
                    "hint": "1 Packungsjahr = 1 Schachtel (20 Zigaretten) pro Tag über 1 Jahr. "
                            "Beispiel: 10 Jahre lang 2 Schachteln pro Tag = 20 Packungsjahre.",
                    "required": True,
                    "show_if": {"id": "rauchstatus", "in": ["ehemals", "aktuell"]},
                    "options": [
                        {"value": "unter_10", "label": "Weniger als 10 Packungsjahre"},
                        {"value": "10_29", "label": "10 bis 29 Packungsjahre"},
                        {"value": "30_plus", "label": "30 Packungsjahre oder mehr"},
                        {"value": "unbekannt", "label": "Kann ich nicht einschätzen"},
                    ],
                },
                {
                    "id": "rauchen_zeitraum",
                    "type": "text",
                    "label": "In welchem Jahr haben Sie mit dem Rauchen begonnen – und ggf. "
                             "in welchem Jahr aufgehört?",
                    "required": False,
                    "show_if": {"id": "rauchstatus", "in": ["ehemals", "aktuell"]},
                },
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Alkohol ist neben dem Rauchen ein Risikofaktor für "
                            "Kehlkopferkrankungen und wird deshalb erfragt.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie oder fast nie"},
                        {"value": "gelegentlich", "label": "Gelegentlich (z. B. am Wochenende)"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche bis täglich)"},
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
    # ── Bedenkenstatbestände nach Abschnitt 2.1.1 ─────────────────────────
    {"wenn": {"lunge_vorerkrankungen": ["bronchitis", "asthma", "emphysem", "pleuritis",
                                        "staublunge", "tuberkulose"]},
     "schwere": "kritisch",
     "bereich": "Lungen-Vorerkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Vorerkrankung des bronchopulmonalen Systems angegeben (z. B. chronische "
               "Bronchitis, Asthma, Emphysem, Pleuritis, Staublunge/Lungenfibrose, Tuberkulose).",
     "konsequenz": "Möglicher Tatbestand dauernder gesundheitlicher Bedenken: Schweregrad "
                   "objektivieren (Vorbefunde, Spirometrie mit Mindest-Sollwerten nach Anhang). "
                   "Bei zu erwartender klinisch relevanter Verschlimmerung durch die Exposition "
                   "dauernde Bedenken (2.1.1); bei erwartbarer Wiederherstellung befristete "
                   "Bedenken (2.1.2); bei weniger ausgeprägten Befunden keine Bedenken unter "
                   "bestimmten Voraussetzungen (2.1.3), z. B. Beschäftigung mit geringer "
                   "Exposition."},
    {"wenn": {"lunge_op_trauma": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Lungen-Vorerkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Zustand nach Lungenresektion oder -verletzung mit möglicher "
               "Funktionsbeeinträchtigung der Brustorgane angegeben.",
     "konsequenz": "Funktionsbeeinträchtigung objektivieren (Spirometrie, Vorbefunde). Bei "
                   "wesentlicher Beeinträchtigung dauernde gesundheitliche Bedenken erwägen "
                   "(2.1.1); bei geringer Ausprägung prüfen, ob die Tätigkeit unter bestimmten "
                   "Voraussetzungen möglich ist (2.1.3)."},
    {"wenn": {"thorax_deformitaet": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Lungen-Vorerkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Deformierung von Brustkorb oder Wirbelsäule mit Beeinträchtigung der Atmung angegeben.",
     "konsequenz": "Ausmaß der Atembeeinträchtigung prüfen (Lungenfunktion). Bei wesentlicher "
                   "Beeinträchtigung Bedenkenstatbestand nach 2.1.1; sonst 2.1.3 prüfen."},
    {"wenn": {"kehlkopf": ["chronisch", "op_bestrahlung"]},
     "schwere": "kritisch",
     "bereich": "Kehlkopf-Vorerkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Chronische Kehlkopferkrankung mit Funktionsbeeinträchtigung bzw. Zustand nach "
               "Stimmband-/Kehlkopf-Teil- oder Gesamtresektion oder Strahlentherapie angegeben.",
     "konsequenz": "HNO-ärztliche Vorbefunde einholen. Bedenkenstatbestand nach 2.1.1 prüfen; "
                   "bei weniger ausgeprägten Befunden keine Bedenken unter bestimmten "
                   "Voraussetzungen (2.1.3)."},
    {"wenn": {"herz_kreislauf": ["insuffizienz", "klappenfehler"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Herzinsuffizienz bzw. Herzklappenfehler/anderer organischer Herzschaden angegeben.",
     "konsequenz": "Kardiologische Vorbefunde einholen; manifeste oder vorzeitig zu erwartende "
                   "Herzinsuffizienz ist Bedenkenstatbestand nach 2.1.1. Bei geringer Ausprägung "
                   "Tätigkeit unter bestimmten Voraussetzungen prüfen (2.1.3)."},
    {"wenn": {"herz_kreislauf": ["hypertonie"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Therapeutisch nicht gut einstellbarer Bluthochdruck angegeben.",
     "konsequenz": "Blutdruckeinstellung überprüfen (Vorbefunde, ggf. hausärztliche/"
                   "kardiologische Abklärung). Therapeutisch nicht einstellbarer Bluthochdruck "
                   "ist Bedenkenstatbestand nach 2.1.1; nach erfolgreicher Einstellung neu "
                   "beurteilen (befristete Bedenken, 2.1.2)."},
    # ── BK-Verfahren (Abschnitt 2.1.3) ────────────────────────────────────
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "pruefen",
     "bereich": "BK-Verfahren",
     "quelle": "Abschnitt 2.1.3",
     "befund": "Angezeigte oder anerkannte asbestbedingte Erkrankung bzw. laufendes "
               "BK-Feststellungsverfahren angegeben.",
     "konsequenz": "Befunde und Verfahrensstand einholen. Bei anzeigepflichtiger Asbestfibrose, "
                   "asbestbedingten pleuralen Veränderungen oder asbestbedingter "
                   "Kehlkopferkrankung gilt bis zum Abschluss des BK-Feststellungsverfahrens: "
                   "keine gesundheitlichen Bedenken unter bestimmten Voraussetzungen (z. B. "
                   "Beschäftigung mit geringer Exposition); Verlauf engmaschig kontrollieren."},
    # ── Kehlkopf: HNO-Abklärung (Abschnitt 1.2.1) ─────────────────────────
    {"wenn": {"heiserkeit_3w": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kehlkopf",
     "quelle": "Abschnitte 1.2.1 und 2.2",
     "befund": "Anhaltende Heiserkeit über 3 Wochen oder länger angegeben.",
     "konsequenz": "Wegen der Gefahr eines Larynxkarzinoms dokumentieren und HNO-ärztliche "
                   "Untersuchung veranlassen. Den Versicherten darauf hinweisen, auch im "
                   "Untersuchungsintervall bei länger andauernder Heiserkeit einen HNO-Arzt "
                   "aufzusuchen."},
    {"wenn": {"stimm_missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kehlkopf",
     "quelle": "Abschnitt 1.2.1",
     "befund": "Phonationsstörungen, Schluckbeschwerden oder Missempfindungen im Halsbereich angegeben.",
     "konsequenz": "Beschwerden dokumentieren; bei Hinweisen auf eine Kehlkopferkrankung "
                   "HNO-ärztliche Untersuchung veranlassen."},
    {"wenn": {"kehlkopf": ["neoplasie"]},
     "schwere": "pruefen",
     "bereich": "Kehlkopf",
     "quelle": "Abschnitt 1.2.1",
     "befund": "Bekannte intraepitheliale Neoplasie der Kehlkopfschleimhaut angegeben.",
     "konsequenz": "Den aktuellen HNO-ärztlichen Befund einholen und in die Beurteilung einbeziehen."},
    # ── Atemwegs-/Lungensymptome (Abschnitte 1.2.2, 1.2.3 und 3.2.3) ──────
    {"wenn": {"atemnot": ["belastung_leicht", "ruhe"]},
     "schwere": "pruefen",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 1.2.2, 1.2.3 und Anhang (Spirometrie-Sollwerte)",
     "befund": "Atemnot bereits bei leichter Belastung oder in Ruhe angegeben.",
     "konsequenz": "Lungenfunktion sorgfältig bewerten (Vitalkapazität gegen Mindest-Sollwerte "
                   "des Anhangs, Atemstoßtest). Lässt der Befund der Thoraxübersichtsaufnahme "
                   "keine eindeutige Aussage zu: Ergänzungsuntersuchung mit qualifizierter "
                   "Low-dose-Volumen-CT/HRCT nach Anhörung eines Zweitbeurteilers (Verzeichnis "
                   "bei GVS bzw. Landesverbänden); Beurteilung nach Abschnitt 2.1."},
    {"wenn": {"husten": ["yes"], "auswurf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 1.2.2 und 3.2.3",
     "befund": "Husten mit Auswurf angegeben (Teil der Beschwerdetrias der Asbestose: "
               "Reizhusten, Luftnot, Auswurf).",
     "konsequenz": "Gezielte Abklärung: Auskultation (Knisterrasseln?), Spirometrie und "
                   "Röntgenbefund (ILO-Klassifikation) bewerten; bei Tumorverdacht qualifizierte "
                   "CT-Untersuchung nach Tumorprotokoll auch ohne Zweitbeurteiler veranlassen."},
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Untersuchungsfristen",
     "quelle": "Abschnitt 1.1 (Vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder mehrwöchige Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen die Fortsetzung der "
                   "Tätigkeit gibt; ggf. vorzeitige Nachuntersuchung ansetzen (regulär nach "
                   "12–36 Monaten)."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Untersuchungsfristen",
     "quelle": "Abschnitt 1.1 (Vorzeitige Nachuntersuchung)",
     "befund": "Die versicherte Person vermutet einen ursächlichen Zusammenhang zwischen "
               "Erkrankung/Beschwerden und der Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen; Beschwerden gezielt abklären und "
                   "bei begründetem Verdacht auf eine asbestbedingte Erkrankung die "
                   "BK-Anzeige prüfen."},
    # ── Röntgen-Indikation bei Nachuntersuchungen (Abschnitt 1.2.2) ───────
    {"wenn": {"untersuchung_art": ["nach", "nachgehend"], "alter_gruppe": ["45_plus"]},
     "schwere": "hinweis",
     "bereich": "Radiologische Diagnostik",
     "quelle": "Abschnitt 1.2.2 (Nachuntersuchung/Nachgehende Untersuchung)",
     "befund": "Nachuntersuchung/nachgehende Untersuchung bei einer Person ab dem vollendeten "
               "45. Lebensjahr.",
     "konsequenz": "Rechtfertigende Indikation für die Röntgenaufnahme des Thorax "
                   "(p. a.-Strahlengang) im Einzelfall prüfen – erfahrungsgemäß etwa 15 Jahre "
                   "nach Expositionsbeginn oder nach Vollendung des 45. Lebensjahres sinnvoll. "
                   "Befundung nach ILO 2000; Voraufnahmen (bei Nachuntersuchungen nicht älter "
                   "als 1/2 Jahr) berücksichtigen."},
    {"wenn": {"untersuchung_art": ["nach", "nachgehend"], "asbest_beginn": ["vor_mehr_15"]},
     "schwere": "hinweis",
     "bereich": "Radiologische Diagnostik",
     "quelle": "Abschnitt 1.2.2 (Nachuntersuchung/Nachgehende Untersuchung)",
     "befund": "Expositionsbeginn liegt mehr als 15 Jahre zurück.",
     "konsequenz": "Rechtfertigende Indikation für die Röntgenaufnahme des Thorax im Einzelfall "
                   "prüfen. Bei Versicherten mit besonderen Expositionsbedingungen "
                   "(Hochrisikogruppe) spezielles Untersuchungsprogramm mit qualifiziertem "
                   "Low-dose-Mehrzeilen-Volumen-CT mit HRCT anstelle der Übersichtsaufnahme "
                   "erwägen."},
    # ── Nachgehende Untersuchungen (Abschnitte 1.1 und 2.2) ───────────────
    {"wenn": {"fruehere_expo": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchungen",
     "quelle": "Abschnitte 1.1 und 2.2",
     "befund": "Frühere, inzwischen beendete Asbestexposition angegeben.",
     "konsequenz": "Auf das Angebot nachgehender Untersuchungen hinweisen: erstmals 15 Jahre "
                   "nach Expositionsbeginn oder nach Vollendung des 45. Lebensjahres, dann nach "
                   "12–36 Monaten je nach kumulativer Expositionshöhe und Befund. Die "
                   "Organisation erfolgt über die Gesundheitsvorsorge (GVS, "
                   "http://gvs.bgetem.de) nach Ausscheiden aus dem Unternehmen."},
    # ── Rauchen und Alkohol (Abschnitte 1.2.1 und 2.2) ────────────────────
    {"wenn": {"rauchstatus": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Tabakkonsum",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Eindringlich beraten: Die Kombination von Asbestfaserstaubexposition und "
                   "Zigarettenrauchen wirkt synergistisch auf das Lungenkrebsrisiko. Auf die "
                   "Möglichkeit einer erfolgreichen Entwöhnungsbehandlung hinweisen; "
                   "Packungsjahre dokumentieren."},
    {"wenn": {"alkohol": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Alkoholkonsum",
     "quelle": "Abschnitt 1.2.1",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Alkoholkonsum wegen der Gefahr eines Larynxkarzinoms dokumentieren; zu "
                   "Risikofaktoren für Kehlkopferkrankungen beraten."},
    # ── Schutzmaßnahmen (Abschnitt 2.2) ───────────────────────────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen/PSA",
     "quelle": "Abschnitte 2 und 2.2",
     "befund": "Atemschutz/Schutzkleidung wird bei Asbestarbeiten selten oder nie getragen.",
     "konsequenz": "Individuelle Aufklärung und Beratung zu Schutzmaßnahmen (TRGS 519/517). "
                   "Ergeben sich Hinweise, dass die Gefährdungsbeurteilung aktualisiert werden "
                   "muss: Mitteilung an den Arbeitgeber unter Wahrung der schutzbedürftigen "
                   "Belange der untersuchten Person."},
]
