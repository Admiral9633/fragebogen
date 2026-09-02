# -*- coding: utf-8 -*-
"""Tätigkeiten mit Hochtemperaturwollen (Faserstäube Kategorie 1A oder 1B) –
DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische
Beratungen und Untersuchungen, 1. Auflage 2024, Kapitel »Tätigkeiten mit
Hochtemperaturwollen (Faserstäube Kategorie 1A oder 1B)« (E HTW,
Fassung Januar 2022), S. 657–679."""

SLUG = "hochtemperaturwollen-2024"

CATALOG = {
    "version": 2,
    "title": "Tätigkeiten mit Hochtemperaturwollen (Faserstäube Kategorie 1A oder 1B) "
             "(DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Tätigkeiten mit Hochtemperaturwollen (Faserstäube "
             "Kategorie 1A oder 1B)« (E HTW, Fassung Januar 2022), S. 657–679",
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
                    "label": "Um welche Vorsorge handelt es sich heute?",
                    "hint": "Nachgehende Vorsorge: Sie arbeiten nicht mehr mit diesen "
                            "Faserstäuben, werden aber weiterhin untersucht, weil die "
                            "Stoffe erst nach vielen Jahren Erkrankungen auslösen können.",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge wegen Hochtemperaturwollen/Faserstäuben"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich war schon einmal hier)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (Tätigkeit bereits beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn bei der "
                            "Arbeit krebserzeugende Faserstäube (Kategorie 1A oder 1B) "
                            "freigesetzt werden können.",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "not_in": ["nachgehend"]},
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
            "title": "Tätigkeit & Faserstaub-Belastung",
            "subtitle": "Ihre Arbeit mit Hochtemperaturwollen und anderen Faserstäuben",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "faser_material",
                    "type": "multi_choice",
                    "label": "Mit welchen Faser-Materialien haben Sie bei der Arbeit zu tun?",
                    "hint": "Mehrfachauswahl möglich. Die Angaben stehen meist im "
                            "Sicherheitsdatenblatt oder in Ihrer Betriebsanweisung.",
                    "required": True,
                    "options": [
                        {"value": "asw", "label": "Aluminiumsilikatwolle (ASW, früher »Keramikfaser«/RCF)"},
                        {"value": "aes", "label": "AES-Wolle (Erdalkalisilikatwolle, Hochtemperaturglaswolle)"},
                        {"value": "pcw", "label": "Polykristalline Wolle (PCW, Aluminiumoxid-Wolle)"},
                        {"value": "alte_daemmwolle", "label": "Alte Dämmwollen (z. B. beim Rückbau von Isolierungen)"},
                        {"value": "whisker_sic", "label": "Whisker oder Siliziumcarbid (SiC), z. B. Schleif-/Abrasivstoffe, Keramikherstellung"},
                        {"value": "glasfasern", "label": "Mikroglasfasern oder Textilglasfasern"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "expo_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Welche der folgenden Arbeiten führen Sie durch?",
                    "hint": "Mehrfachauswahl möglich. Bei diesen Arbeiten können lungengängige "
                            "Faserbruchstücke in die Atemluft gelangen.",
                    "required": True,
                    "options": [
                        {"value": "demontage_daemmwolle", "label": "Ausbau und Verpacken von hitzebelasteten Dämmwollen (Rohre, Kanäle, Behälter, Öfen)"},
                        {"value": "matten_bearbeiten", "label": "Zuschneiden, Einsetzen oder Anbringen von Matten, Filzen oder Platten aus Faserwolle"},
                        {"value": "reparatur_alte_wolle", "label": "Reparaturen an defekten Isolierungen mit alter Mineralwolle"},
                        {"value": "demontage_abdeckungen", "label": "Demontage von Abdeckungen, Ummantelungen, Kappen oder Hauben"},
                        {"value": "kabelzug", "label": "Kabelzugarbeiten in Zwischendecken mit abgelagerten Faserstäuben"},
                        {"value": "revision_schaechte", "label": "Öffnen/Revision von Versorgungsschächten und Kanälen mit alten Mineralwoll-Dämmstoffen"},
                        {"value": "transport_verpackt", "label": "Nur Transport/Lagerung in geschlossenen Behältern oder dichten Verpackungen"},
                        {"value": "sonstiges", "label": "Andere Arbeiten mit Faserwolle-Produkten"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wie vielen Jahren arbeiten Sie insgesamt mit solchen "
                            "Faserstäuben (auch frühere Arbeitsstellen mitzählen)?",
                    "required": True,
                    "options": [
                        {"value": "beginnt_erst", "label": "Die Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis15", "label": "5 bis 15 Jahre"},
                        {"value": "ueber15", "label": "Mehr als 15 Jahre"},
                    ],
                },
                {
                    "id": "alter_45",
                    "type": "yes_no",
                    "label": "Sind Sie 45 Jahre alt oder älter?",
                    "hint": "Das Alter spielt eine Rolle für die Frage, ob eine "
                            "Röntgenaufnahme der Lunge sinnvoll sein kann.",
                    "required": True,
                },
                {
                    "id": "frueher_faserstaub",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Tätigkeiten anderen Stäuben ausgesetzt, "
                            "z. B. Asbest, Quarz (z. B. Sandstrahlen, Steinbearbeitung) oder "
                            "anderen Mineralfasern?",
                    "required": True,
                    "followup": {"id": "frueher_faserstaub_desc", "type": "textarea",
                                 "label": "Welche Stoffe, welche Tätigkeiten, und wie lange?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Atemschutz, Technik und Hygiene an Ihrem Arbeitsplatz",
            "questions": [
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei staubenden Arbeiten Atemschutz "
                            "(z. B. FFP-Maske, Gebläse-Atemschutz)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_bedarf", "label": "Bei meiner Arbeit entsteht kein Staub / noch keine Tätigkeit"},
                    ],
                },
                {
                    "id": "tech_massnahmen",
                    "type": "yes_no",
                    "label": "Gibt es an Ihrem Arbeitsplatz technische Schutzmaßnahmen gegen "
                            "Staub (z. B. Absaugung, staubarme Verfahren), und werden diese "
                            "auch genutzt?",
                    "required": True,
                    "show_if": {"id": "atemschutz", "not_in": ["kein_bedarf"]},
                },
                {
                    "id": "hygiene_kleidung",
                    "type": "yes_no",
                    "label": "Wechseln Sie nach staubenden Arbeiten die Arbeitskleidung und "
                            "achten Sie auf Hygiene am Arbeitsplatz (z. B. getrennte "
                            "Aufbewahrung von Arbeits- und Straßenkleidung)?",
                    "required": True,
                    "show_if": {"id": "atemschutz", "not_in": ["kein_bedarf"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Atemwegs-Beschwerden",
            "subtitle": "Aktuelle Beschwerden von Lunge und Atemwegen",
            "questions": [
                {
                    "id": "husten",
                    "type": "yes_no",
                    "label": "Haben Sie häufig oder anhaltend Husten?",
                    "required": True,
                    "followup": {"id": "husten_desc", "type": "text",
                                 "label": "Seit wann, und haben Sie dabei Auswurf (Schleim)?",
                                 "when": "yes"},
                },
                {
                    "id": "atemnot",
                    "type": "choice",
                    "label": "Haben Sie Atemnot (Luftnot)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "starke_belastung", "label": "Nur bei starker körperlicher Belastung"},
                        {"value": "leichte_belastung", "label": "Schon bei leichter Belastung (z. B. Treppensteigen)"},
                        {"value": "ruhe", "label": "Auch in Ruhe"},
                    ],
                },
                {
                    "id": "beschwerden_verschlechtert",
                    "type": "yes_no",
                    "label": "Sind seit der letzten Vorsorge neue Beschwerden an Lunge oder "
                            "Atemwegen aufgetreten oder haben sich bestehende verschlechtert?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                    "followup": {"id": "beschwerden_verschlechtert_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, seit wann?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen von Lunge, Atemwegen, Herz und Kreislauf",
            "questions": [
                {
                    "id": "lunge_vorerkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Erkrankungen der Lunge oder "
                            "Atemwege festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "chron_bronchitis", "label": "Chronische Bronchitis (dauerhafter Husten mit Auswurf)"},
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "emphysem", "label": "Lungenemphysem / COPD (Lungenüberblähung)"},
                        {"value": "pleuritis", "label": "Rippenfellentzündung (Pleuritis), auch wiederholt"},
                        {"value": "staublunge", "label": "Staublunge, Lungenfibrose oder andere Vernarbung des Lungengewebes"},
                        {"value": "tuberkulose", "label": "Tuberkulose (auch ausgeheilt)"},
                        {"value": "lungen_op", "label": "Operation oder Verletzung der Lunge (z. B. Teilentfernung)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "kehlkopf",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine chronische Kehlkopferkrankung, eine "
                            "Operation an Kehlkopf oder Stimmbändern oder eine "
                            "Strahlentherapie in diesem Bereich?",
                    "required": True,
                    "followup": {"id": "kehlkopf_desc", "type": "text",
                                 "label": "Was genau, und wann?", "when": "yes"},
                },
                {
                    "id": "thorax_deform",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen eine Verformung des Brustkorbs oder der "
                            "Wirbelsäule, die das Atmen beeinträchtigt?",
                    "required": True,
                },
                {
                    "id": "systemerkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine sogenannte Systemerkrankung, die auch die Lunge "
                            "betreffen kann (z. B. Rheuma, Sarkoidose, Sklerodermie, "
                            "Kollagenose)?",
                    "required": True,
                    "followup": {"id": "systemerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "herz_kreislauf",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Herz-Kreislauf-Erkrankungen "
                            "festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "herzinsuffizienz", "label": "Herzschwäche (Herzinsuffizienz)"},
                        {"value": "klappenfehler", "label": "Herzklappenfehler oder andere organische Herzerkrankung"},
                        {"value": "hypertonie_schlecht", "label": "Bluthochdruck, der trotz Behandlung schlecht einstellbar ist"},
                        {"value": "hypertonie_behandelt", "label": "Bluthochdruck, gut eingestellt"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "textarea",
                                 "label": "Welche Medikamente, und wofür?", "when": "yes"},
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
                    "id": "raucher_status",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "ex", "label": "Früher ja, heute nicht mehr (Ex-Raucher/in)"},
                        {"value": "regelmaessig", "label": "Ja, ich rauche regelmäßig"},
                    ],
                },
                {
                    "id": "rauch_waren",
                    "type": "multi_choice",
                    "label": "Was rauchen bzw. rauchten Sie?",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ex", "regelmaessig"]},
                    "options": [
                        {"value": "zigaretten", "label": "Zigaretten"},
                        {"value": "zigarren", "label": "Zigarren/Zigarillos"},
                        {"value": "pfeife", "label": "Pfeife"},
                        {"value": "sonstiges", "label": "Sonstiges (z. B. E-Zigarette, Wasserpfeife)"},
                    ],
                },
                {
                    "id": "rauch_menge",
                    "type": "text",
                    "label": "Wie viel rauchen bzw. rauchten Sie ungefähr pro Tag, und seit "
                            "welchem Jahr (ggf. bis wann)?",
                    "hint": "Beispiel: »20 Zigaretten pro Tag, von 2005 bis 2020«.",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ex", "regelmaessig"]},
                },
                {
                    "id": "packungsjahre",
                    "type": "choice",
                    "label": "Wie viele »Packungsjahre« kommen ungefähr zusammen?",
                    "hint": "1 Packungsjahr = 1 Schachtel (20 Zigaretten) pro Tag über 1 Jahr. "
                            "Beispiel: 10 Jahre lang eine halbe Schachtel täglich = 5 Packungsjahre.",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ex", "regelmaessig"]},
                    "options": [
                        {"value": "unter10", "label": "Unter 10 Packungsjahre"},
                        {"value": "10bis20", "label": "10 bis 20 Packungsjahre"},
                        {"value": "ueber20", "label": "Mehr als 20 Packungsjahre"},
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
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"lunge_vorerkrankungen": ["chron_bronchitis", "asthma", "emphysem"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4 (Beurteilungskriterien)",
     "befund": "Chronische Bronchitis, Asthma bronchiale oder Lungenemphysem/COPD angegeben.",
     "konsequenz": "Spirometrie sorgfältig bewerten; erweiterte Lungenfunktionsdiagnostik "
                   "(Bronchodilatationstest, Ganzkörperplethysmographie) in Betracht ziehen. "
                   "Beurteilung nach 7.4: Prüfen, ob Maßnahmen nach 7.4.2 (Substitution, "
                   "technische/organisatorische Schutzmaßnahmen, Begrenzung der "
                   "Expositionszeit, Einsatz an Arbeitsplätzen mit geringerer Exposition) "
                   "ausreichen; ggf. verkürzte Vorsorgefristen nach 7.4.3."},
    {"wenn": {"lunge_vorerkrankungen": ["staublunge", "pleuritis"]},
     "schwere": "pruefen",
     "bereich": "Lungen-/Pleuraerkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4 (Beurteilungskriterien)",
     "befund": "Staublunge/Lungenfibrose bzw. (rezidivierende) Pleuritis in der Vorgeschichte.",
     "konsequenz": "Vorbefunde und Voraufnahmen (ILO-kodiert) beiziehen. Bei klinischem "
                   "Verdacht auf eine Lungenerkrankung ist die Röntgen-Thoraxaufnahme "
                   "(p. a.) unabhängig von Alter und Expositionsbeginn indiziert; bei "
                   "unklarem Befund Low-dose-Volumen-HRCT nur nach Zweitbeurteilung "
                   "(Verzeichnis bei GVS bzw. Landesverbänden). Beurteilung nach 7.4, "
                   "ggf. verkürzte Fristen nach 7.4.3."},
    {"wenn": {"lunge_vorerkrankungen": ["tuberkulose"]},
     "schwere": "pruefen",
     "bereich": "Tuberkulose",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Tuberkulose in der Vorgeschichte angegeben.",
     "konsequenz": "Aktivität und Ausdehnung klären (aktive, auch geschlossene sowie "
                   "ausgedehnte inaktive Tuberkulose sind beurteilungsrelevant); Vorbefunde "
                   "und ggf. fachärztliche Abklärung veranlassen, bevor die Beurteilung "
                   "nach 7.4 abgeschlossen wird."},
    {"wenn": {"lunge_vorerkrankungen": ["lungen_op"]},
     "schwere": "pruefen",
     "bereich": "Zustand nach Lungenresektion",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Operation oder Verletzung der Lunge in der Vorgeschichte.",
     "konsequenz": "Funktionsbeeinträchtigung der Brustorgane prüfen (Spirometrie, ggf. "
                   "erweiterte Lungenfunktionsdiagnostik); OP-Berichte einholen. Beurteilung "
                   "nach 7.4 mit Prüfung von Maßnahmen nach 7.4.2/7.4.3."},
    {"wenn": {"kehlkopf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kehlkopferkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Chronische Kehlkopferkrankung bzw. Zustand nach Stimmband-/Kehlkopf-"
               "Operation oder Strahlentherapie angegeben.",
     "konsequenz": "Funktionsbeeinträchtigung klären, ggf. HNO-ärztliche Vorstellung. "
                   "Beurteilungsrelevanz nach 7.4 prüfen; bei eingeschränkter Funktion "
                   "Maßnahmen nach 7.4.2 bzw. verkürzte Fristen nach 7.4.3 erwägen."},
    {"wenn": {"thorax_deform": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Thorax-/Wirbelsäulendeformität",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Verformung von Brustkorb oder Wirbelsäule mit Atembeeinträchtigung angegeben.",
     "konsequenz": "Ausmaß der Atembeeinträchtigung durch Spirometrie objektivieren; "
                   "beurteilungsrelevant nur, sofern die Atmung beeinträchtigt ist. "
                   "Beurteilung nach 7.4."},
    {"wenn": {"systemerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Systemerkrankung",
     "quelle": "Abschnitt 7.1 (Anamnese) und 7.4",
     "befund": "Systemerkrankung mit möglicher Lungenbeteiligung angegeben.",
     "konsequenz": "Lungenbeteiligung abklären (interstitielle Lungenerkrankungen sind "
                   "beurteilungsrelevant): erweiterte Lungenfunktionsdiagnostik in Betracht "
                   "ziehen, Vorbefunde der behandelnden Fachärzte einholen."},
    {"wenn": {"herz_kreislauf": ["herzinsuffizienz", "klappenfehler", "hypertonie_schlecht"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Herzinsuffizienz, Herzklappenfehler/organische Herzerkrankung oder "
               "therapeutisch schlecht einstellbarer Bluthochdruck angegeben.",
     "konsequenz": "Beurteilungsrelevant nach 7.4 sind manifeste oder vorzeitig zu "
                   "erwartende Herzinsuffizienz (z. B. bei gesichertem Herzklappenfehler) "
                   "und therapeutisch nicht einstellbarer Bluthochdruck: kardiologische "
                   "Vorbefunde einholen, Kreislauforgane untersuchen, bei Hypertonie "
                   "Therapieoptimierung empfehlen; Beurteilung nach 7.4 mit Prüfung von "
                   "Maßnahmen nach 7.4.2/7.4.3."},
    # ── Beschwerden ───────────────────────────────────────────────────────
    {"wenn": {"husten": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 7.2.2",
     "befund": "Häufiger oder anhaltender Husten angegeben.",
     "konsequenz": "Tätigkeitsbezug und Dauer klären; Spirometrie-Ergebnis beachten, "
                   "erweiterte Lungenfunktionsdiagnostik erwägen. Bei klinischem Verdacht "
                   "auf eine Lungenerkrankung Röntgen-Thorax (p. a.) unabhängig von Alter "
                   "und Expositionsbeginn indiziert."},
    {"wenn": {"atemnot": ["leichte_belastung", "ruhe"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 7.1 (Beschwerden), 7.2.2 und 7.4",
     "befund": "Atemnot bereits bei leichter Belastung oder in Ruhe angegeben.",
     "konsequenz": "Zeitnahe Abklärung: Spirometrie, erweiterte Lungenfunktionsdiagnostik "
                   "(z. B. Ganzkörperplethysmographie), Untersuchung der Kreislauforgane; "
                   "bei klinischem Verdacht Röntgen-Thorax. Erhebliche Störungen der "
                   "Lungenfunktion sind beurteilungsrelevant nach 7.4; ggf. Maßnahmen nach "
                   "7.4.2 bis 7.4.4 (bis hin zur Erwägung eines Tätigkeitswechsels, "
                   "Mitteilung an den Arbeitgeber nur mit Einwilligung)."},
    {"wenn": {"beschwerden_verschlechtert": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Verlauf",
     "quelle": "Abschnitte 7.1 (weitere Vorsorgen) und 7.4.3",
     "befund": "Neue oder verschlechterte Atembeschwerden seit der letzten Vorsorge.",
     "konsequenz": "Aktualisierte Anamnese vertiefen, Befunde mit Voruntersuchungen "
                   "vergleichen; erweiterte Diagnostik nach ärztlichem Ermessen. Verkürzte "
                   "Vorsorgefrist nach 7.4.3 erwägen, wenn eine Änderung des Schweregrads "
                   "der Erkrankung zu erwarten ist."},
    # ── Röntgenindikation (Abschnitt 7.2.2 Nachuntersuchung) ──────────────
    {"wenn": {"expo_dauer": ["ueber15"]},
     "schwere": "hinweis",
     "bereich": "Röntgenindikation",
     "quelle": "Abschnitt 7.2.2 (Nachuntersuchung/Nachgehende Untersuchung)",
     "befund": "Expositionsbeginn liegt mehr als 15 Jahre zurück.",
     "konsequenz": "Rechtfertigende Indikation für eine Röntgen-Thoraxaufnahme (p. a.) im "
                   "Einzelfall prüfen (§ 83 StrlSchG): Erfahrungsgemäß frühestens 15 Jahre "
                   "nach Expositionsbeginn oder nach Vollendung des 45. Lebensjahres "
                   "indiziert; Expositionshöhe berücksichtigen. Befundung standardisiert "
                   "nach ILO, Voraufnahmen zum Vergleich heranziehen."},
    {"wenn": {"alter_45": ["yes"]},
     "wenn_nicht": {"expo_dauer": ["ueber15"]},
     "schwere": "hinweis",
     "bereich": "Röntgenindikation",
     "quelle": "Abschnitt 7.2.2 (Nachuntersuchung/Nachgehende Untersuchung)",
     "befund": "Lebensalter 45 Jahre oder älter (Expositionsbeginn unter 15 Jahren).",
     "konsequenz": "Rechtfertigende Indikation für eine Röntgen-Thoraxaufnahme (p. a.) im "
                   "Einzelfall prüfen: ab Vollendung des 45. Lebensjahres kann sie auch vor "
                   "Ablauf von 15 Expositionsjahren indiziert sein; Expositionshöhe "
                   "berücksichtigen, keine generelle Indikation."},
    # ── Exposition und Schutzmaßnahmen ────────────────────────────────────
    {"wenn": {"faser_material": ["unbekannt"]},
     "schwere": "hinweis",
     "bereich": "Exposition",
     "quelle": "Abschnitte 2, 6.1 und 7 (Gefährdungsbeurteilung)",
     "befund": "Faserart am Arbeitsplatz ist der versicherten Person nicht bekannt.",
     "konsequenz": "Faserart anhand der Gefährdungsbeurteilung und Sicherheitsdatenblätter "
                   "klären (ASW Kategorie 1B → diese Empfehlung; AES- oder polykristalline "
                   "Wolle → DGUV Empfehlung »Staub«); Umfang der Vorsorge danach festlegen."},
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 7.1 (Arbeitsanamnese), 8.1 und 8.2",
     "befund": "Atemschutz wird bei staubenden Arbeiten selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA und zur krebserzeugenden "
                   "Wirkung der Faserstäube. Ergeben sich Anhaltspunkte, dass die "
                   "Schutzmaßnahmen nicht ausreichen, Mitteilung an den Unternehmer bzw. "
                   "die Unternehmerin und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"tech_massnahmen": ["no"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 7.1 (Arbeitsanamnese) und 8.2",
     "befund": "Technische Schutzmaßnahmen fehlen oder werden nicht genutzt.",
     "konsequenz": "Abgleich mit der Gefährdungsbeurteilung; dem Unternehmen technische "
                   "Schutzmaßnahmen (z. B. Absaugung, staubarme Verfahren, Substitution "
                   "nach TRGS 619) vorschlagen; Überprüfung der Gefährdungsbeurteilung "
                   "anregen."},
    {"wenn": {"hygiene_kleidung": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 8.1 (Beratung)",
     "befund": "Kein Kleidungswechsel bzw. unzureichende Hygiene nach staubenden Arbeiten.",
     "konsequenz": "Beratung zu Hygienemaßnahmen am Arbeitsplatz: Vermeiden der Inhalation, "
                   "Wechsel der Arbeitskleidung, getrennte Aufbewahrung; Hinweise aus "
                   "TRGS 558 bzw. TRGS 521 einbeziehen."},
    # ── Frühere Expositionen, nachgehende Vorsorge, Rauchen ───────────────
    {"wenn": {"frueher_faserstaub": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 7.1 (Arbeitsanamnese) und 7.2.2",
     "befund": "Frühere Exposition gegenüber Asbest, Quarz oder anderen fibrogenen "
               "Stäuben/Mineralfasern angegeben.",
     "konsequenz": "Frühere Expositionen dokumentieren und bei Beurteilung sowie "
                   "Röntgenindikation (Latenzzeit!) berücksichtigen; bei früherer "
                   "Asbestexposition Anmeldung zur nachgehenden Vorsorge (GVS) prüfen und "
                   "Untersuchungen koordinieren."},
    {"wenn": {"vorsorge_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2 (Angebotsvorsorge) und 8.1",
     "befund": "Vorstellung zur nachgehenden Vorsorge nach Ende der Tätigkeit.",
     "konsequenz": "Untersuchungsprogramm wie Nachuntersuchung (Atmungs-/Kreislauforgane, "
                   "Spirometrie, Röntgenindikation im Einzelfall). Sicherstellen, dass die "
                   "Anmeldung über das Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de) "
                   "erfolgt ist; über Sinn und Fortführung der nachgehenden Vorsorge beraten."},
    {"wenn": {"raucher_status": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 7.1 (Tabakanamnese) und 8.1 (Beratung)",
     "befund": "Regelmäßiger Tabakkonsum angegeben.",
     "konsequenz": "Beratung zum Rauchverhalten und zur Prognose: Zigarettenrauchen ist die "
                   "Hauptursache für Lungenkrebs; auf die Möglichkeit einer erfolgreichen "
                   "Entwöhnungsbehandlung hinweisen. Packungsjahre dokumentieren."},
]
