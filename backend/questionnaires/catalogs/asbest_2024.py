# -*- coding: utf-8 -*-
"""Asbest – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische
Beratungen und Untersuchungen, 1. Auflage 2024, Kapitel »Asbest« (E ASB,
Fassung Januar 2022), S. 98–122."""

SLUG = "asbest-2024"

CATALOG = {
    "version": 2,
    "title": "Asbest (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Asbest« (E ASB, Fassung Januar 2022), S. 98–122",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen Asbest?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Asbest-Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur Asbest-Vorsorge"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (die Tätigkeit mit Asbest ist beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: bei Tätigkeiten mit Asbest, wenn eine wiederholte "
                            "Exposition nicht ausgeschlossen werden kann (z. B. wiederholte "
                            "Reparatur-, Wartungs-, Reinigungs- oder Abrissarbeiten). "
                            "Angebotsvorsorge: wenn eine Exposition nicht ausgeschlossen werden "
                            "kann, aber keine Pflichtvorsorge besteht.",
                    "required": True,
                    "options": [
                        {"value": "pflicht", "label": "Vom Betrieb verpflichtend veranlasst (Pflichtvorsorge)"},
                        {"value": "angebot", "label": "Vom Betrieb angeboten (Angebotsvorsorge)"},
                        {"value": "wunsch", "label": "Auf meinen eigenen Wunsch (Wunschvorsorge)"},
                        {"value": "nachgehend", "label": "Angebot nach Ende der Tätigkeit (nachgehende Vorsorge)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "alter_gruppe",
                    "type": "choice",
                    "label": "Wie alt sind Sie?",
                    "hint": "Das Alter ist wichtig für die Frage, ab wann bestimmte "
                            "Untersuchungen (z. B. Röntgenaufnahme der Lunge) sinnvoll sind.",
                    "required": True,
                    "options": [
                        {"value": "unter_45", "label": "Unter 45 Jahre"},
                        {"value": "45_54", "label": "45 bis 54 Jahre"},
                        {"value": "55_plus", "label": "55 Jahre oder älter"},
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
                    "hint": "Mehrfachauswahl möglich. Asbest steckt z. B. in alten "
                            "Asbestzementplatten, Dämmungen, Putzen, Spachtelmassen und Klebern.",
                    "required": True,
                    "options": [
                        {"value": "asi", "label": "Abbruch-, Sanierungs- oder Instandhaltungsarbeiten an asbesthaltigen Materialien"},
                        {"value": "rohstoffe", "label": "Arbeiten mit mineralischen Rohstoffen, die Asbest enthalten können (z. B. Steinbruch, Schotter)"},
                        {"value": "bestand", "label": "Bauen im Bestand (alte Putze, Spachtelmassen, Fliesenkleber)"},
                        {"value": "probenahme", "label": "Probenahmen an asbestverdächtigen Materialien"},
                        {"value": "bystander", "label": "Ich arbeite in der Nähe solcher Arbeiten, ohne sie selbst auszuführen (Bystander)"},
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
                        {"value": "vor_1985", "label": "Vor 1985"},
                        {"value": "1985_1992", "label": "1985 bis 1992"},
                        {"value": "1993_2010", "label": "1993 bis 2010"},
                        {"value": "nach_2010", "label": "Nach 2010"},
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
                {
                    "id": "technische_massnahmen",
                    "type": "yes_no",
                    "label": "Gibt es an Ihrem Arbeitsplatz technische Schutzmaßnahmen gegen "
                             "Faserstaub (z. B. Absaugung, staubarme Verfahren, Abschottung)?",
                    "required": True,
                    "show_if": {"id": "asbest_arbeiten", "not_in": ["keine"]},
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
                        {"value": "staublunge", "label": "Staublunge oder andere Lungenfibrose (Vernarbung der Lunge)"},
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
                    "id": "systemerkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Systemerkrankung, die die Lunge mitbetreffen kann "
                             "(z. B. Rheuma, Sarkoidose, Sklerodermie)?",
                    "required": True,
                    "followup": {"id": "systemerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "bk_anerkannt",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Berufskrankheit durch Asbest anerkannt "
                             "(z. B. Asbestose, BK-Nr. 4103)?",
                    "required": True,
                    "followup": {"id": "bk_anerkannt_desc", "type": "text",
                                 "label": "Welche Berufskrankheit, seit wann?", "when": "yes"},
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "textarea",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
                {
                    "id": "sonstige_krankheiten",
                    "type": "yes_no",
                    "label": "Haben Sie weitere dauerhafte (chronische) Erkrankungen?",
                    "required": True,
                    "followup": {"id": "sonstige_krankheiten_desc", "type": "textarea",
                                 "label": "Welche Erkrankungen?", "when": "yes"},
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
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
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
    # ── Kehlkopf: HNO-Abklärung (Abschnitt 7.2.2) ─────────────────────────
    {"wenn": {"heiserkeit_3w": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kehlkopf",
     "quelle": "Abschnitte 7.2.2 und 8.1",
     "befund": "Anhaltende Heiserkeit über mehr als 3 Wochen angegeben.",
     "konsequenz": "Wegen der Gefahr eines Larynxkarzinoms dokumentieren und HNO-ärztliche "
                   "Untersuchung veranlassen. Die versicherte Person darauf hinweisen, auch im "
                   "Vorsorgeintervall bei länger andauernder Heiserkeit HNO-ärztlich vorstellig "
                   "zu werden."},
    {"wenn": {"stimm_missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kehlkopf",
     "quelle": "Abschnitt 7.2.2",
     "befund": "Phonationsstörungen, Schluckbeschwerden oder Missempfindungen im Halsbereich angegeben.",
     "konsequenz": "Beschwerden dokumentieren (Larynxkarzinom-Gefahr); bei Hinweisen auf eine "
                   "Kehlkopferkrankung HNO-ärztliche Untersuchung veranlassen."},
    {"wenn": {"kehlkopf": ["neoplasie"]},
     "schwere": "pruefen",
     "bereich": "Kehlkopf",
     "quelle": "Abschnitt 7.2.2",
     "befund": "Bekannte intraepitheliale Neoplasie der Kehlkopfschleimhaut angegeben.",
     "konsequenz": "Den aktuellen HNO-ärztlichen Befund einholen und in die Beurteilung einbeziehen."},
    {"wenn": {"kehlkopf": ["chronisch", "op_bestrahlung"]},
     "schwere": "pruefen",
     "bereich": "Kehlkopf",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Chronische Kehlkopferkrankung bzw. Zustand nach Stimmband-/Kehlkopfresektion "
               "oder Strahlentherapie angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach Abschnitt 7.4: prüfen, ob die Tätigkeit "
                   "ohne gesundheitliche Gefährdung möglich ist; ggf. Maßnahmen nach 7.4.2 "
                   "(z. B. Expositionsbegrenzung, geeignete PSA) und verkürzte Vorsorgefristen "
                   "nach 7.4.3 empfehlen; HNO-Vorbefunde einholen."},
    # ── Atemwegs-/Lungensymptome (Abschnitte 6.3.3 und 7.2.2) ─────────────
    {"wenn": {"atemnot": ["belastung_leicht", "ruhe"]},
     "schwere": "pruefen",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitt 7.2.2 (Ergänzend)",
     "befund": "Atemnot bereits bei leichter Belastung oder in Ruhe angegeben.",
     "konsequenz": "Erweiterte Lungenfunktionsdiagnostik (z. B. Bronchodilatationstest, "
                   "Ganzkörperplethysmographie) in Betracht ziehen. Bei klinischem Verdacht auf "
                   "eine Lungenerkrankung ist die Indikation für eine Röntgenaufnahme des Thorax "
                   "unabhängig von Alter und Expositionsbeginn gegeben."},
    {"wenn": {"husten": ["yes"], "auswurf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Husten mit Auswurf angegeben (Teil der Beschwerdetrias der Asbestose: "
               "Reizhusten, Luftnot, Auswurf).",
     "konsequenz": "Gezielte Abklärung: Auskultation (Knisterrasseln?), Spirometrie bewerten, "
                   "ggf. erweiterte Lungenfunktionsdiagnostik. Bei klinischem Verdacht auf eine "
                   "Lungenerkrankung Röntgen-Thorax unabhängig von Alter und Expositionsbeginn "
                   "indiziert."},
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"lunge_vorerkrankungen": ["bronchitis", "asthma", "emphysem", "pleuritis",
                                        "staublunge", "tuberkulose"]},
     "schwere": "pruefen",
     "bereich": "Lungen-Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Beurteilungsrelevante Lungen-/Atemwegserkrankung angegeben (z. B. chronische "
               "Bronchitis, Asthma, Emphysem, Pleuritis, Staublunge, Tuberkulose).",
     "konsequenz": "Individuelles Ausmaß prüfen: Ist die Tätigkeit ohne gesundheitliche "
                   "Gefährdung möglich? Bei weniger ausgeprägten Befunden Maßnahmen nach 7.4.2 "
                   "(Expositionsbegrenzung, Einsatz an Arbeitsplätzen mit geringerer Exposition, "
                   "PSA) empfehlen; bei zu erwartender Änderung des Schweregrads verkürzte "
                   "Vorsorgefristen nach 7.4.3; ohne Aussicht auf Erfolg Tätigkeitswechsel nach "
                   "7.4.4 erwägen (Mitteilung an den Arbeitgeber nur mit Einwilligung)."},
    {"wenn": {"lunge_op_trauma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lungen-Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Zustand nach Lungenresektion oder -verletzung mit möglicher "
               "Funktionsbeeinträchtigung angegeben.",
     "konsequenz": "Funktionsbeeinträchtigung objektivieren (Spirometrie, ggf. erweiterte "
                   "Lungenfunktionsdiagnostik); Beurteilung nach 7.4, ggf. Maßnahmen nach 7.4.2 "
                   "oder verkürzte Fristen nach 7.4.3."},
    {"wenn": {"thorax_deformitaet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lungen-Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Deformierung von Brustkorb oder Wirbelsäule mit Beeinträchtigung der Atmung angegeben.",
     "konsequenz": "Ausmaß der Atembeeinträchtigung prüfen (Lungenfunktion); Beurteilung nach "
                   "7.4 mit ggf. Maßnahmen nach 7.4.2."},
    {"wenn": {"herz_kreislauf": ["insuffizienz", "klappenfehler", "hypertonie"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Beurteilungsrelevante Herz-Kreislauf-Erkrankung angegeben (Herzinsuffizienz, "
               "Herzklappenfehler/organischer Herzschaden oder nicht einstellbarer Bluthochdruck).",
     "konsequenz": "Kardiale Belastbarkeit klären (Vorbefunde, ggf. fachärztliche Abklärung); "
                   "Beurteilung nach 7.4: prüfen, ob die Tätigkeit ohne Gefährdung möglich ist; "
                   "ggf. Maßnahmen nach 7.4.2 und verkürzte Fristen nach 7.4.3."},
    {"wenn": {"systemerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Systemerkrankung",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Systemerkrankung mit möglicher Lungenbeteiligung angegeben.",
     "konsequenz": "Lungenbeteiligung abklären (Vorbefunde einholen, Spirometrie bewerten, ggf. "
                   "erweiterte Lungenfunktionsdiagnostik); als interstitielle Lungenerkrankung "
                   "bei der Beurteilung nach 7.4 berücksichtigen."},
    # ── Röntgen-Indikation bei Nachuntersuchungen (Abschnitt 7.2.2) ───────
    {"wenn": {"vorsorge_art": ["weitere", "nachgehend"],
              "alter_gruppe": ["45_54", "55_plus"]},
     "schwere": "hinweis",
     "bereich": "Radiologische Diagnostik",
     "quelle": "Abschnitt 7.2.2 (Nachuntersuchungen)",
     "befund": "Weitere/nachgehende Vorsorge bei einer Person ab dem vollendeten 45. Lebensjahr.",
     "konsequenz": "Rechtfertigende Indikation für eine Röntgenaufnahme des Thorax "
                   "(p. a.-Strahlengang) im Einzelfall prüfen: erfahrungsgemäß frühestens "
                   "15 Jahre nach Expositionsbeginn oder nach Vollendung des 45. Lebensjahres "
                   "indiziert; Expositionshöhe zusätzlich berücksichtigen. Befundung nach ILO, "
                   "Voraufnahmen (nicht älter als 1 Jahr) einbeziehen."},
    {"wenn": {"vorsorge_art": ["weitere", "nachgehend"],
              "asbest_beginn": ["vor_1985", "1985_1992", "1993_2010"]},
     "schwere": "hinweis",
     "bereich": "Radiologische Diagnostik",
     "quelle": "Abschnitt 7.2.2 (Nachuntersuchungen)",
     "befund": "Expositionsbeginn liegt mehr als 15 Jahre zurück.",
     "konsequenz": "Rechtfertigende Indikation für eine Röntgenaufnahme des Thorax im Einzelfall "
                   "prüfen (§ 83 StrlSchG); bei unklarem Befund der Übersichtsaufnahme "
                   "Low-dose-Volumen-HRCT mit Zweitbeurteiler (Verzeichnis bei GVS) erwägen; bei "
                   "Tumorverdacht qualifizierte CT nach Tumorprotokoll auch ohne Zweitbeurteiler "
                   "veranlassen."},
    # ── EVA-Lunge / nachgehende Vorsorge (Abschnitte 2 und 7.2.3.1) ───────
    {"wenn": {"alter_gruppe": ["55_plus"],
              "packungsjahre": ["30_plus"],
              "asbest_beginn": ["vor_1985"]},
     "schwere": "pruefen",
     "bereich": "Früherkennung Lungenkrebs",
     "quelle": "Abschnitt 7.2.3.1 (EVA-Lunge)",
     "befund": "Konstellation der EVA-Hochrisikogruppe: mindestens 55 Jahre alt, "
               "Expositionsbeginn vor 1985 und mindestens 30 Packungsjahre.",
     "konsequenz": "Prüfen, ob die EVA-Lunge-Kriterien erfüllt sind (mind. 55 Jahre, mind. "
                   "10 Jahre beruflich asbeststaubgefährdet mit Beginn vor 1985 oder anerkannte "
                   "BK-Nr. 4103, mind. 30 Packungsjahre). Wenn ja: jährliche "
                   "LD-HRCT-Untersuchung im Rahmen des erweiterten Vorsorgeangebots; das Angebot "
                   "erfolgt über die Gesundheitsvorsorge (GVS, https://gvs.bgetem.de)."},
    {"wenn": {"bk_anerkannt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Früherkennung Lungenkrebs",
     "quelle": "Abschnitte 2 und 7.2.3.1",
     "befund": "Anerkannte Berufskrankheit durch Asbest (z. B. BK-Nr. 4103) angegeben.",
     "konsequenz": "Vorbefunde und BK-Unterlagen einbeziehen. Bei anerkannter BK-Nr. 4103 "
                   "zusätzlich prüfen, ob das EVA-Lunge-Angebot (jährliche LD-HRCT über den "
                   "zuständigen Unfallversicherungsträger, § 26 Abs. 2 Nr. 1 SGB VII) greift "
                   "(mind. 55 Jahre und mind. 30 Packungsjahre)."},
    {"wenn": {"fruehere_expo": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2 und 8.1",
     "befund": "Frühere, inzwischen beendete Asbestexposition angegeben.",
     "konsequenz": "Frühere Exposition bei der Beurteilung berücksichtigen (Erkrankungen können "
                   "noch nach langer Latenzzeit auftreten). Sicherstellen, dass die Anmeldung "
                   "zur nachgehenden Vorsorge über das Meldeportal »DGUV Vorsorge« "
                   "(www.dguv-vorsorge.de) erfolgt ist; die versicherte Person über das Angebot "
                   "nachgehender Vorsorge informieren."},
    # ── Rauchen und Alkohol (Abschnitte 6.3.1, 7.2.2 und 8.1) ─────────────
    {"wenn": {"rauchstatus": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Tabakkonsum",
     "quelle": "Abschnitte 6.3.1 und 8.1",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Eindringlich beraten: Die Kombination von Asbestfaserstaub und "
                   "Zigarettenrauchen wirkt synergistisch/überadditiv auf das "
                   "Lungenkrebsrisiko. Auf die Möglichkeit einer erfolgreichen "
                   "Entwöhnungsbehandlung hinweisen; Packungsjahre dokumentieren."},
    {"wenn": {"alkohol": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Alkoholkonsum",
     "quelle": "Abschnitt 7.2.2",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Alkoholkonsum wegen der Gefahr eines Larynxkarzinoms dokumentieren; zu "
                   "Risikofaktoren für Kehlkopferkrankungen beraten."},
    # ── Schutzmaßnahmen (Abschnitte 3, 8.1 und 8.2) ───────────────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen/PSA",
     "quelle": "Abschnitte 3, 8.1 und 8.2",
     "befund": "Atemschutz/Schutzkleidung wird bei Asbestarbeiten selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA und zur Hygiene am Arbeitsplatz "
                   "(Vermeiden von Inhalation, Wechsel der Arbeitskleidung). Ergeben sich "
                   "Anhaltspunkte, dass die Schutzmaßnahmen nicht ausreichen: Mitteilung an das "
                   "Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"technische_massnahmen": ["no"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 3 und 8.2",
     "befund": "Keine technischen Schutzmaßnahmen gegen Faserstaub am Arbeitsplatz bekannt.",
     "konsequenz": "Abgleich mit der Gefährdungsbeurteilung; bei Anhaltspunkten für "
                   "unzureichende Maßnahmen dem Unternehmen technische/organisatorische "
                   "Schutzmaßnahmen vorschlagen (§ 6 (4) ArbMedVV)."},
]
