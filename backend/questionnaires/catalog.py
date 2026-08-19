# -*- coding: utf-8 -*-
"""
Fragenkatalog des verkehrsmedizinischen Anamnese-Fragebogens.

Grundlage: Begutachtungsleitlinien zur Kraftfahreignung (BASt, Stand 2022),
Kapitel 3.1–3.20. Die Fragen sind patientenverständlich formuliert und
enthalten die eignungsrelevanten Zeitfenster der Leitlinien (z.B. anfallsfrei
seit X, Fremdhilfe-Hypoglykämie in den letzten 12 Monaten).

Der Katalog wird per `manage.py load_catalog` als QuestionnaireTemplate
(schema_json, Format-Version 2) geladen; Frontend, Validierung und beide
PDF-Renderer arbeiten mit genau diesem Schema (siehe schema.py).
"""

def _yn(qid, label, required=True, hint=None, followup=None, show_if=None):
    q = {"id": qid, "type": "yes_no", "label": label, "required": required}
    if hint:
        q["hint"] = hint
    if followup:
        q["followup"] = followup
    if show_if:
        q["show_if"] = show_if
    return q


def _follow(qid, label, kind="textarea"):
    return {"id": qid, "type": kind, "label": label, "when": "yes"}


def _choice(qid, label, options, required=True, hint=None, show_if=None, followup=None):
    q = {
        "id": qid,
        "type": "choice",
        "label": label,
        "required": required,
        "options": [{"value": v, "label": l} for v, l in options],
    }
    if hint:
        q["hint"] = hint
    if show_if:
        q["show_if"] = show_if
    if followup:
        q["followup"] = followup
    return q


CATALOG = {
    "version": 2,
    "title": "Verkehrsmedizinischer Fragebogen",
    "basis": "Fragenkatalog nach den Begutachtungsleitlinien zur Kraftfahreignung (BASt, Stand 2022)",
    "sections": [
        # ── 1 ─────────────────────────────────────────────────────────────
        {
            "id": "anlass",
            "title": "Anlass & Fahrprofil",
            "subtitle": "Angaben zur Untersuchung und Ihrer Fahrtätigkeit",
            "questions": [
                _choice("exam_occasion", "Für welche Fahrerlaubnis findet die Untersuchung statt?", [
                    ("pkw", "PKW / andere Klasse"),
                    ("lkw", "LKW (C, C1, CE, C1E)"),
                    ("bus", "Bus (D, D1, DE, D1E)"),
                    ("fahrgast", "Fahrgastbeförderung (Taxi, Mietwagen, Krankentransport)"),
                ]),
                _choice("exam_kind", "Handelt es sich um eine Ersterteilung oder eine Verlängerung?", [
                    ("erst", "Ersterteilung"),
                    ("verlaengerung", "Verlängerung"),
                ]),
                {
                    "id": "license_classes",
                    "type": "multi_choice",
                    "label": "Welche Führerscheinklassen besitzen oder beantragen Sie?",
                    "required": True,
                    "options": [{"value": c, "label": c} for c in
                                ["AM", "A1", "A2", "A", "B", "BE", "C1", "C1E", "C", "CE", "D1", "D", "DE", "T"]],
                },
                _choice("license_years", "Seit wie vielen Jahren besitzen Sie eine Fahrerlaubnis?", [
                    ("erstantrag", "Noch keine (Erstantrag)"),
                    ("unter3", "Weniger als 3 Jahre"),
                    ("3bis10", "3 bis 10 Jahre"),
                    ("ueber10", "Mehr als 10 Jahre"),
                ]),
                _choice("driving_hours", "Wie viele Stunden fahren Sie durchschnittlich pro Tag?", [
                    ("<1", "Weniger als 1 Stunde"),
                    ("1-2", "1 bis 2 Stunden"),
                    ("2-4", "2 bis 4 Stunden"),
                    (">4", "Mehr als 4 Stunden"),
                ]),
                _yn("night_driving", "Fahren Sie regelmäßig nachts?"),
                _yn("accidents",
                    "Hatten Sie in den letzten 24 Monaten Unfälle oder Beinahe-Unfälle im Straßenverkehr?",
                    followup=_follow("accidents_desc", "Was ist passiert?")),
                _yn("license_withdrawn",
                    "Wurde Ihnen schon einmal die Fahrerlaubnis entzogen oder mussten Sie an einer "
                    "medizinisch-psychologischen Untersuchung (MPU) teilnehmen?",
                    followup=_follow("license_withdrawn_desc", "Wann und aus welchem Grund?")),
                _yn("psych_test_done",
                    "Haben Sie für diese Fahrerlaubnis bereits einen psychologischen Leistungstest "
                    "(Reaktions-, Konzentrations- und Aufmerksamkeitstest) absolviert?",
                    hint="Bei Bus-Klassen und Fahrgastbeförderung ist dieser Nachweis nach Anlage 5 FeV vorgeschrieben. "
                         "Bitte bringen Sie ein vorhandenes Gutachten zur Untersuchung mit.",
                    show_if={"id": "exam_occasion", "in": ["bus", "fahrgast"]},
                    followup=_follow("psych_test_desc", "Wann und wo wurde der Test durchgeführt?", "text")),
            ],
        },
        # ── 1b ────────────────────────────────────────────────────────────
        {
            "id": "gesundheit",
            "title": "Gesundheitszustand",
            "subtitle": "Eine Frage vorab",
            "questions": [
                _yn("has_conditions",
                    "Haben Sie eine bekannte Vorerkrankung, eine dauerhafte körperliche "
                    "Einschränkung, oder sind Sie in regelmäßiger ärztlicher Behandlung?",
                    hint="Dazu zählen auch länger zurückliegende ernsthafte Erkrankungen "
                         "(z.B. Herz, Diabetes, Nerven, Psyche). Wenn nein, verkürzt sich "
                         "der Fragebogen deutlich."),
            ],
        },
        # ── 2 ─────────────────────────────────────────────────────────────
        {
            "id": "anfaelle",
            "title": "Anfälle & Bewusstlosigkeit",
            "subtitle": "Plötzliches Ausfallrisiko – epileptische Anfälle und Ohnmachten",
            "questions": [
                _yn("seizure_ever",
                    "Hatten Sie jemals einen epileptischen Anfall oder Krampfanfall?",
                    followup=_follow("seizure_desc",
                                     "Wann war der letzte Anfall, wie viele hatten Sie insgesamt, "
                                     "und gab es einen Auslöser (z.B. Schlafentzug, Fieber, Alkohol)?")),
                _yn("epilepsy",
                    "Wurde bei Ihnen eine Epilepsie diagnostiziert?",
                    show_if={"id": "seizure_ever", "in": ["yes"]},
                    followup=_follow("epilepsy_desc",
                                     "Treten die Anfälle ausschließlich im Schlaf auf? "
                                     "Sind Sie in regelmäßiger neurologischer Behandlung?")),
                _choice("seizure_free", "Wie lange sind Sie inzwischen anfallsfrei?", [
                    ("unter3m", "Weniger als 3 Monate"),
                    ("3bis6m", "3 bis 6 Monate"),
                    ("6bis12m", "6 bis 12 Monate"),
                    ("1bis2j", "1 bis 2 Jahre"),
                    ("2bis5j", "2 bis 5 Jahre"),
                    ("ueber5j", "Mehr als 5 Jahre"),
                ], show_if={"id": "seizure_ever", "in": ["yes"]},
                   hint="Die Leitlinien knüpfen die Fahreignung an konkrete anfallsfreie Zeiträume."),
                _choice("antiepileptics", "Nehmen Sie Medikamente gegen Anfälle (Antiepileptika) ein?", [
                    ("nie", "Nein, nie eingenommen"),
                    ("aktuell", "Ja, aktuell"),
                    ("reduktion", "Die Behandlung wird derzeit schrittweise reduziert"),
                    ("ende_unter3m", "Vor weniger als 3 Monaten beendet"),
                    ("ende_ueber3m", "Vor mehr als 3 Monaten beendet"),
                ], show_if={"id": "seizure_ever", "in": ["yes"]}),
                _choice("syncope", "Sind Sie schon einmal plötzlich ohnmächtig geworden (kurze Bewusstlosigkeit)?", [
                    ("nie", "Noch nie"),
                    ("einmal", "Einmal"),
                    ("mehrmals", "Mehrmals"),
                ]),
                _yn("syncope_recent",
                    "Liegt Ihre letzte Ohnmacht weniger als 6 Monate zurück?",
                    show_if={"id": "syncope", "in": ["einmal", "mehrmals"]},
                    followup=_follow("syncope_desc",
                                     "In welcher Situation trat die Ohnmacht auf, und wurde eine Ursache "
                                     "gefunden (z.B. Kreislauf, Herzrhythmus, beim Wasserlassen)?")),
                _yn("syncope_prodromi",
                    "Kündigt sich eine Ohnmacht bei Ihnen vorher an (z.B. Schwitzen, Schwindel, "
                    "Übelkeit, Herzklopfen)?",
                    show_if={"id": "syncope", "in": ["einmal", "mehrmals"]}),
            ],
        },
        # ── 3 ─────────────────────────────────────────────────────────────
        {
            "id": "sehen_hoeren",
            "title": "Sehen & Hören",
            "subtitle": "Seh- und Hörfunktion",
            "questions": [
                _yn("glasses", "Tragen Sie beim Fahren eine Brille oder Kontaktlinsen?"),
                _yn("eye_disease",
                    "Ist bei Ihnen eine Augenerkrankung bekannt (z.B. Grauer Star, Grüner Star/Glaukom, "
                    "Netzhauterkrankung, Gesichtsfeldeinschränkung)?",
                    followup=_follow("eye_disease_desc", "Welche Erkrankung, und sind Sie in augenärztlicher Behandlung?")),
                _yn("one_eyed",
                    "Sehen Sie auf einem Auge deutlich schlechter oder sind Sie auf einem Auge blind?"),
                _yn("night_vision",
                    "Haben Sie Probleme beim Sehen in Dämmerung oder Dunkelheit, oder werden Sie durch "
                    "Gegenverkehr stark geblendet?",
                    followup=_follow("night_vision_desc", "In welchen Situationen treten die Probleme auf?")),
                _yn("hearing_impaired",
                    "Sind Sie hochgradig schwerhörig oder gehörlos?",
                    followup=_follow("hearing_desc", "Seit wann, und sind Sie in HNO-ärztlicher Behandlung?")),
                _yn("hearing_aid", "Tragen Sie ein Hörgerät oder Cochlea-Implantat?"),
            ],
        },
        # ── 4 ─────────────────────────────────────────────────────────────
        {
            "id": "herz",
            "title": "Herz & Kreislauf",
            "subtitle": "Herz- und Gefäßerkrankungen",
            "questions": [
                _yn("heart_disease",
                    "Ist bei Ihnen eine Herz- oder Gefäßerkrankung bekannt?",
                    hint="z.B. Rhythmusstörungen, Herzinfarkt, Herzschwäche, Klappenfehler, Durchblutungsstörungen",
                    followup=_follow("heart_disease_desc",
                                     "Welche Erkrankung(en), seit wann, und wie werden sie behandelt?")),
                _yn("cardio_checkup",
                    "Sind Sie deswegen regelmäßig bei einem Kardiologen in Kontrolle?",
                    show_if={"id": "heart_disease", "in": ["yes"]},
                    followup=_follow("cardio_checkup_desc", "Wann war die letzte Kontrolle?", "text")),
                _yn("heart_attack",
                    "Hatten Sie schon einmal einen Herzinfarkt, eine Stent-Behandlung oder eine "
                    "Bypass-Operation?",
                    followup=_follow("heart_attack_desc",
                                     "Wann war das Ereignis bzw. der Eingriff, und gab es Komplikationen "
                                     "(z.B. eingeschränkte Pumpleistung)?")),
                _yn("arrhythmia",
                    "Sind bei Ihnen Herzrhythmusstörungen bekannt (z.B. Herzstolpern, Herzrasen, "
                    "auffallend langsamer Puls, Vorhofflimmern, AV-Block)?",
                    followup=_follow("arrhythmia_desc", "Welche Diagnose, und wie wird behandelt?")),
                _choice("pacemaker_icd", "Tragen Sie einen Herzschrittmacher oder Defibrillator (ICD)?", [
                    ("nein", "Nein"),
                    ("schrittmacher", "Herzschrittmacher"),
                    ("icd", "Defibrillator (ICD)"),
                ], followup={"id": "device_desc", "type": "text",
                             "label": "Wann eingesetzt, und wann war die letzte Kontrolle?",
                             "when": "schrittmacher"}),
                _yn("icd_shock",
                    "Hat Ihr Defibrillator in den letzten 3 Monaten einen Schock abgegeben?",
                    show_if={"id": "pacemaker_icd", "in": ["icd"]},
                    followup=_follow("icd_shock_desc", "Wann, und was hat Ihr Kardiologe dazu gesagt?", "text")),
                _choice("exertion_symptoms",
                        "Bekommen Sie bei Belastung Luftnot, Brustschmerzen, Herzstolpern oder "
                        "ungewöhnliche Erschöpfung?", [
                    ("keine", "Nein, keine Beschwerden bei alltäglicher Belastung"),
                    ("stark", "Bei stärkerer Belastung (z.B. zügiges Treppensteigen)"),
                    ("leicht", "Schon bei leichter Belastung (z.B. langsames Gehen)"),
                    ("ruhe", "Bereits in Ruhe"),
                ], hint="Selbsteinschätzung entsprechend der NYHA-Stadien"),
                _yn("hypertension",
                    "Ist bei Ihnen Bluthochdruck bekannt?",
                    followup=_follow("hypertension_desc",
                                     "Seit wann, welche Medikamente, und welche Werte messen Sie üblicherweise?")),
                _yn("bp_dizziness",
                    "Kommt es unter Ihren Blutdruckmedikamenten zu Schwindel, Schwächegefühl oder "
                    "Schwarzwerden vor den Augen?",
                    show_if={"id": "hypertension", "in": ["yes"]}),
                _yn("heart_other",
                    "Ist bei Ihnen eine weitere Herz-/Gefäßerkrankung bekannt: Herzklappenfehler, "
                    "angeborener Herzfehler, Herzmuskelerkrankung (Kardiomyopathie), erbliche "
                    "Rhythmuserkrankung (z.B. Long-QT), Aortenaneurysma oder verengte Halsschlagader?",
                    followup=_follow("heart_other_desc", "Welche Diagnose, und wie wird sie kontrolliert/behandelt?")),
                _yn("family_sudden_death",
                    "Gab es in Ihrer engsten Familie (Eltern, Geschwister, Kinder) einen plötzlichen Herztod?"),
            ],
        },
        # ── 5 ─────────────────────────────────────────────────────────────
        {
            "id": "gehirn",
            "title": "Schlaganfall & Gehirn",
            "subtitle": "Durchblutungsstörungen, Verletzungen und Operationen des Gehirns",
            "questions": [
                _yn("stroke",
                    "Hatten Sie jemals einen Schlaganfall, eine Hirnblutung oder eine TIA "
                    "(vorübergehende Durchblutungsstörung mit kurzzeitigen Ausfällen)?",
                    followup=_follow("stroke_desc",
                                     "Wann war das Ereignis, und wurde eine Rehabilitation abgeschlossen?")),
                _yn("stroke_residuals",
                    "Bestehen seitdem noch Folgen wie Lähmungen, Sprachstörungen, Gedächtnisprobleme "
                    "oder Einschränkungen des Blickfelds?",
                    show_if={"id": "stroke", "in": ["yes"]},
                    followup=_follow("stroke_residuals_desc", "Welche Beschwerden bestehen aktuell noch?")),
                _yn("head_injury",
                    "Hatten Sie jemals eine schwere Kopfverletzung (mit Bewusstlosigkeit oder "
                    "Krankenhausaufenthalt) oder eine Operation am Gehirn?",
                    followup=_follow("head_injury_desc", "Wann, und was wurde behandelt?")),
                _yn("head_injury_recent",
                    "Liegt diese Verletzung oder Operation weniger als 3 Monate zurück?",
                    show_if={"id": "head_injury", "in": ["yes"]},
                    hint="Nach einer Hirnverletzung oder -operation besteht laut Leitlinie im Allgemeinen "
                         "für 3 Monate keine Fahreignung."),
                _yn("brain_residuals",
                    "Bestehen seit der Verletzung/Operation Beschwerden wie Konzentrations- oder "
                    "Gedächtnisstörungen, Wesensveränderung oder Krampfanfälle?",
                    show_if={"id": "head_injury", "in": ["yes"]},
                    followup=_follow("brain_residuals_desc", "Welche Beschwerden, und wie wirken sie sich aus?")),
            ],
        },
        # ── 6 ─────────────────────────────────────────────────────────────
        {
            "id": "neuro",
            "title": "Nervensystem",
            "subtitle": "Neurologische Erkrankungen",
            "questions": [
                _yn("parkinson",
                    "Wurde bei Ihnen die Parkinson-Krankheit oder eine andere Bewegungs- oder "
                    "Koordinationsstörung diagnostiziert?",
                    followup=_follow("parkinson_desc",
                                     "Seit wann, wie wird behandelt, und wann war die letzte neurologische Kontrolle?")),
                _yn("ms_spinal",
                    "Ist bei Ihnen eine Multiple Sklerose, eine Rückenmarkserkrankung oder eine "
                    "Rückenmarksverletzung bekannt?",
                    followup=_follow("ms_spinal_desc", "Welche Diagnose, und welche Beschwerden haben Sie aktuell?")),
                _yn("muscle_nerve",
                    "Ist bei Ihnen eine Muskel- oder Nervenerkrankung bekannt (z.B. Muskelschwund, "
                    "Myasthenie, Polyneuropathie)?",
                    followup=_follow("muscle_nerve_desc", "Welche Diagnose, und wie stark sind Sie eingeschränkt?")),
                _yn("paralysis_attacks",
                    "Kommt es bei Ihnen zu anfallsartigen Lähmungen oder plötzlicher starker Muskelschwäche?",
                    followup=_follow("paralysis_desc", "Wann trat der letzte Anfall auf, und wie schnell setzt er ein?")),
                _yn("motor_limits",
                    "Haben Sie Lähmungen, Muskelschwäche oder Gefühlsstörungen in Armen oder Beinen, "
                    "die Sie beim Bedienen eines Fahrzeugs einschränken könnten?",
                    followup=_follow("motor_limits_desc", "Welche Körperteile sind betroffen?")),
            ],
        },
        # ── 7 ─────────────────────────────────────────────────────────────
        {
            "id": "schwindel",
            "title": "Gleichgewicht & Schwindel",
            "subtitle": "Schwindelformen und Gleichgewichtsstörungen",
            "questions": [
                _yn("vertigo",
                    "Leiden Sie unter Schwindel oder Gleichgewichtsstörungen (z.B. Drehgefühl, "
                    "Schwanken, Unsicherheit beim Gehen)?",
                    followup=_follow("vertigo_desc",
                                     "Wie fühlt sich der Schwindel an, wie oft tritt er auf, wie lange dauert "
                                     "ein Anfall, und was löst ihn aus?")),
                _choice("vertigo_last", "Wie lange liegt Ihr letzter Schwindelanfall zurück?", [
                    ("unter3m", "Weniger als 3 Monate"),
                    ("3bis6m", "3 bis 6 Monate"),
                    ("6bis12m", "6 bis 12 Monate"),
                    ("1bis2j", "1 bis 2 Jahre"),
                    ("ueber2j", "Mehr als 2 Jahre"),
                ], show_if={"id": "vertigo", "in": ["yes"]}),
                _choice("vertigo_prodromi",
                        "Kündigen sich Ihre Schwindelanfälle vorher an (z.B. Ohrdruck, Ohrgeräusche, "
                        "Hörminderung), sodass Sie rechtzeitig anhalten könnten?", [
                    ("immer", "Ja, immer"),
                    ("manchmal", "Manchmal"),
                    ("nie", "Nein, sie kommen ohne Vorwarnung"),
                ], show_if={"id": "vertigo", "in": ["yes"]}),
                _yn("vertigo_positional",
                    "Wird der Schwindel durch bestimmte Kopfbewegungen oder Lageänderungen ausgelöst "
                    "(z.B. Umdrehen im Bett, Bücken)?",
                    show_if={"id": "vertigo", "in": ["yes"]}),
                _yn("vertigo_ear",
                    "Tritt der Schwindel zusammen mit Hörminderung, Ohrgeräuschen (Tinnitus) oder "
                    "Druckgefühl im Ohr auf?",
                    show_if={"id": "vertigo", "in": ["yes"]}),
                _yn("ear_disease",
                    "Wurde bei Ihnen eine Erkrankung des Gleichgewichtsorgans oder Innenohrs "
                    "festgestellt (z.B. Lagerungsschwindel, Morbus Menière)?",
                    followup=_follow("ear_disease_desc",
                                     "Welche Diagnose, wie wurde behandelt, und sind Sie seither beschwerdefrei?")),
            ],
        },
        # ── 8 ─────────────────────────────────────────────────────────────
        {
            "id": "bewegung",
            "title": "Bewegungsapparat",
            "subtitle": "Körperliche Einschränkungen und Hilfsmittel",
            "questions": [
                _yn("mobility_limits",
                    "Haben Sie eine dauerhafte Einschränkung der Beweglichkeit von Armen, Beinen, "
                    "Händen oder der Wirbelsäule (z.B. nach Unfall, Operation, Amputation)?",
                    followup=_follow("mobility_desc", "Welche Körperteile sind betroffen, und seit wann?")),
                _yn("prosthesis",
                    "Tragen Sie eine Prothese oder nutzen Sie orthopädische Hilfsmittel?",
                    followup=_follow("prosthesis_desc",
                                     "Welche Hilfsmittel, und haben Sie Beschwerden bei längerer Belastung?")),
                _yn("vehicle_modified",
                    "Ist Ihr Fahrzeug wegen einer körperlichen Einschränkung umgebaut "
                    "(z.B. Handbedienung, Lenkhilfe)?",
                    followup=_follow("vehicle_modified_desc",
                                     "Welche Umbauten, und sind sie im Führerschein eingetragen?")),
            ],
        },
        # ── 9 ─────────────────────────────────────────────────────────────
        {
            "id": "diabetes",
            "title": "Diabetes / Stoffwechsel",
            "subtitle": "Zuckerkrankheit und Unterzuckerungen",
            "questions": [
                _choice("diabetes_type", "Ist bei Ihnen ein Diabetes mellitus (Zuckerkrankheit) bekannt?", [
                    ("none", "Nein"),
                    ("type1", "Ja, Typ 1"),
                    ("type2", "Ja, Typ 2"),
                    ("other", "Ja, andere/unklare Form"),
                ]),
                _choice("diabetes_therapy", "Wie wird Ihr Diabetes derzeit behandelt?", [
                    ("lifestyle", "Nur Ernährung / Lebensstil"),
                    ("tabl_low", "Tabletten mit niedrigem Unterzuckerungsrisiko (z.B. Metformin)"),
                    ("tabl_high", "Tabletten mit Unterzuckerungsrisiko (Sulfonylharnstoffe, Glinide)"),
                    ("insulin", "Insulin"),
                    ("unknown", "Weiß ich nicht genau"),
                ], show_if={"id": "diabetes_type", "not_in": ["none"]}),
                _yn("hypoglycemia",
                    "Hatten Sie in den letzten 12 Monaten eine schwere Unterzuckerung, bei der Sie "
                    "auf fremde Hilfe angewiesen waren?",
                    show_if={"id": "diabetes_type", "not_in": ["none"]},
                    followup=_follow("hypoglycemia_desc",
                                     "Wie oft, wann war die letzte Episode, und trat sie im Wachzustand "
                                     "oder im Schlaf auf?")),
                _yn("hypo_awareness",
                    "Ist es vorgekommen, dass Sie eine Unterzuckerung nicht rechtzeitig selbst bemerkt "
                    "haben (fehlende Warnzeichen)?",
                    show_if={"id": "diabetes_type", "not_in": ["none"]},
                    followup=_follow("hypo_awareness_desc",
                                     "Wann zuletzt, und wurde etwas unternommen (z.B. Training, Therapieumstellung)?")),
                _choice("glucose_monitoring",
                        "Messen Sie Ihren Blutzucker regelmäßig selbst (oder tragen Sie einen Glukosesensor)?", [
                    ("2x", "Ja, mindestens zweimal täglich"),
                    ("seltener", "Ja, aber seltener"),
                    ("nein", "Nein"),
                    ("keine_med", "Betrifft mich nicht (keine blutzuckersenkenden Medikamente)"),
                ], show_if={"id": "diabetes_type", "not_in": ["none"]}),
                _yn("diabetes_derailment",
                    "Gab es in den letzten Monaten eine Neueinstellung der Therapie oder eine "
                    "Stoffwechselentgleisung (z.B. Krankenhausbehandlung wegen entgleister Werte)?",
                    show_if={"id": "diabetes_type", "not_in": ["none"]},
                    followup=_follow("derailment_desc", "Was ist passiert, und wann?")),
            ],
        },
        # ── 10 ────────────────────────────────────────────────────────────
        {
            "id": "organe",
            "title": "Innere Organe",
            "subtitle": "Nieren, Lunge und Transplantationen",
            "questions": [
                _yn("kidney_disease",
                    "Ist bei Ihnen eine chronische Nierenerkrankung oder Nierenschwäche bekannt?",
                    followup=_follow("kidney_desc",
                                     "Welche Erkrankung, und sind Sie in nephrologischer Behandlung?")),
                _yn("dialysis",
                    "Werden Sie regelmäßig mit einer Dialyse (Blutwäsche) behandelt?",
                    show_if={"id": "kidney_disease", "in": ["yes"]},
                    followup=_follow("dialysis_desc",
                                     "Seit wann und wie oft pro Woche? Fühlen Sie sich zwischen den "
                                     "Behandlungen leistungsfähig?")),
                _yn("transplant",
                    "Wurde bei Ihnen ein Organ transplantiert (z.B. Niere, Herz, Leber, Lunge)?",
                    followup=_follow("transplant_desc",
                                     "Welches Organ, wann, und sind Sie in regelmäßiger Nachsorge?")),
                _yn("lung_disease",
                    "Leiden Sie an einer chronischen Lungen- oder Bronchialerkrankung "
                    "(z.B. COPD, Asthma, Lungenfibrose)?",
                    followup=_follow("lung_desc", "Welche Erkrankung, und wie wird sie behandelt?")),
                _yn("dyspnea",
                    "Haben Sie Atemnot bereits bei leichter Belastung oder in Ruhe, oder benötigen "
                    "Sie eine Sauerstoff-Langzeittherapie?",
                    show_if={"id": "lung_disease", "in": ["yes"]}),
                _yn("cough_syncope",
                    "Kam es bei starken Hustenanfällen schon zu Schwindel, Schwarzwerden vor den "
                    "Augen oder kurzer Bewusstlosigkeit?",
                    show_if={"id": "lung_disease", "in": ["yes"]}),
            ],
        },
        # ── 11 ────────────────────────────────────────────────────────────
        {
            "id": "schlaf",
            "title": "Schlaf & Tagesschläfrigkeit",
            "subtitle": "Inkl. Epworth Sleepiness Scale (ESS)",
            "questions": [
                _yn("daytime_sleepiness",
                    "Fällt es Ihnen tagsüber schwer, wach und aufmerksam zu bleiben – besonders in "
                    "eintönigen Situationen (z.B. Lesen, Besprechungen, längere Autofahrten)?"),
                _yn("microsleep",
                    "Sind Sie in den letzten Monaten ungewollt eingeschlafen oder hatten Sie "
                    "Sekundenschlaf?",
                    followup=_follow("microsleep_desc",
                                     "In welchen Situationen? Ist es auch am Steuer passiert?")),
                _yn("snoring",
                    "Wurde Ihnen berichtet, dass Sie laut und unregelmäßig schnarchen oder nachts "
                    "Atempausen haben?"),
                _yn("osas",
                    "Wurde bei Ihnen ein Schlafapnoe-Syndrom (nächtliche Atemaussetzer) festgestellt?",
                    followup=_follow("osas_desc",
                                     "Wann wurde die Diagnose gestellt, und welcher Schweregrad bzw. "
                                     "AHI-Wert wurde festgestellt (falls bekannt)?")),
                _choice("cpap", "Werden Sie wegen der Schlafapnoe behandelt (z.B. CPAP-Atemmaske)?", [
                    ("regelmaessig", "Ja, regelmäßig (fast jede Nacht)"),
                    ("unregelmaessig", "Ja, aber unregelmäßig"),
                    ("abgebrochen", "Behandlung wurde abgebrochen"),
                    ("keine", "Nein, keine Behandlung"),
                ], show_if={"id": "osas", "in": ["yes"]}),
                {
                    "id": "ess",
                    "type": "ess_matrix",
                    "label": "Epworth Sleepiness Scale (ESS)",
                    "hint": "Wie wahrscheinlich ist es, dass Sie in den folgenden Situationen einnicken "
                            "würden? 0 = Nie · 1 = Gering · 2 = Mittel · 3 = Hoch",
                    "required": True,
                    "items": [
                        {"id": "ess_1", "label": "Beim Sitzen und Lesen"},
                        {"id": "ess_2", "label": "Beim Fernsehen"},
                        {"id": "ess_3", "label": "Wenn Sie passiv in der Öffentlichkeit sitzen (z.B. im Theater oder bei einer Besprechung)"},
                        {"id": "ess_4", "label": "Als Beifahrer im Auto während einer einstündigen Fahrt ohne Pause"},
                        {"id": "ess_5", "label": "Wenn Sie sich am Nachmittag hingelegt haben, um auszuruhen"},
                        {"id": "ess_6", "label": "Wenn Sie sitzen und sich mit jemandem unterhalten"},
                        {"id": "ess_7", "label": "Wenn Sie nach dem Mittagessen (ohne Alkohol) ruhig dasitzen"},
                        {"id": "ess_8", "label": "Wenn Sie als Fahrer eines Autos verkehrsbedingt einige Minuten halten müssen"},
                    ],
                },
            ],
            "pdf_note": "ESS ab 11/24 Punkten: auffällige Tagesschläfrigkeit, schlafmedizinische Abklärung "
                        "empfohlen (Begutachtungsleitlinien Kap. 3.11).",
        },
        # ── 12 ────────────────────────────────────────────────────────────
        {
            "id": "psyche",
            "title": "Psychische Gesundheit",
            "subtitle": "Psychische Erkrankungen und Gedächtnis",
            "questions": [
                _yn("psychiatric",
                    "Wurde bei Ihnen eine psychische Erkrankung diagnostiziert (z.B. Depression, "
                    "Angststörung, bipolare Störung)?",
                    followup=_follow("psychiatric_desc", "Welche Erkrankung, und wie wird sie behandelt?")),
                _yn("psychiatric_severe",
                    "Waren Sie deswegen schon einmal in stationärer Behandlung, hatten Sie eine "
                    "manische Phase oder Selbsttötungsgedanken?",
                    show_if={"id": "psychiatric", "in": ["yes"]},
                    followup=_follow("psychiatric_severe_desc", "Wann war das zuletzt?")),
                _yn("psychosis",
                    "Wurde bei Ihnen jemals eine Schizophrenie oder andere Psychose diagnostiziert "
                    "(Erkrankung mit Wahnvorstellungen oder Halluzinationen)?",
                    followup=_follow("psychosis_desc",
                                     "Wie viele akute Episoden hatten Sie, wann war die letzte, und sind "
                                     "Sie in fachärztlicher Behandlung?")),
                _yn("memory_problems",
                    "Haben Sie selbst oder Ihre Angehörigen in letzter Zeit zunehmende Gedächtnis- "
                    "oder Orientierungsprobleme bei Ihnen bemerkt?",
                    followup=_follow("memory_desc", "Seit wann, und wie wirken sie sich im Alltag aus?")),
                _yn("concentration",
                    "Haben Sie Konzentrations- oder Aufmerksamkeitsprobleme?"),
            ],
        },
        # ── 13 ────────────────────────────────────────────────────────────
        {
            "id": "substanzen",
            "title": "Alkohol, Drogen & Medikamente",
            "subtitle": "Konsum und Dauermedikation",
            "questions": [
                _choice("alcohol", "Wie häufig trinken Sie Alkohol?", [
                    ("nie", "Nie"),
                    ("selten", "Selten (höchstens 1-mal pro Monat)"),
                    ("woechentlich", "1- bis 2-mal pro Woche"),
                    ("mehrmals", "Mehrmals pro Woche"),
                    ("taeglich", "Täglich oder fast täglich"),
                ]),
                _yn("alcohol_control",
                    "Ist es vorgekommen, dass Sie mehr getrunken haben als beabsichtigt oder die "
                    "Kontrolle über Ihren Konsum verloren haben?",
                    show_if={"id": "alcohol", "not_in": ["nie"]}),
                _yn("alcohol_traffic",
                    "Sind Sie jemals im Straßenverkehr unter Alkoholeinfluss aufgefallen "
                    "(z.B. Trunkenheitsfahrt, Bußgeld, MPU)?",
                    followup=_follow("alcohol_traffic_desc",
                                     "Wann, und welcher Promillewert wurde festgestellt (falls bekannt)?")),
                _yn("alcohol_dependence",
                    "Wurde bei Ihnen jemals eine Alkoholabhängigkeit festgestellt oder haben Sie eine "
                    "Entgiftung bzw. Entwöhnungsbehandlung gemacht?",
                    followup=_follow("alcohol_dependence_desc",
                                     "Wann wurde die Behandlung abgeschlossen, und seit wann leben Sie abstinent?")),
                _yn("drugs",
                    "Nehmen Sie derzeit Drogen (z.B. Cannabis, Kokain, Amphetamine) oder haben Sie "
                    "früher regelmäßig Drogen konsumiert?",
                    followup=_follow("drugs_desc", "Welche Substanzen, wie häufig, und wann zuletzt?")),
                _choice("cannabis", "Wie häufig konsumieren Sie Cannabis?", [
                    ("nie", "Nie"),
                    ("gelegentlich", "Gelegentlich (nicht regelmäßig)"),
                    ("regelmaessig", "Regelmäßig (täglich oder gewohnheitsmäßig)"),
                ], show_if={"id": "drugs", "in": ["yes"]}),
                _yn("substitution",
                    "Erhalten Sie eine Substitutionsbehandlung (z.B. Methadon)?",
                    show_if={"id": "drugs", "in": ["yes"]},
                    followup=_follow("substitution_desc", "Seit wann?", "text")),
                _yn("regular_meds",
                    "Nehmen Sie regelmäßig Medikamente ein?",
                    followup=_follow("regular_meds_desc", "Welche Medikamente, und wogegen?")),
                _yn("sedating_meds",
                    "Sind darunter Medikamente, die müde machen oder das Reaktionsvermögen "
                    "beeinflussen können (z.B. starke Schmerzmittel/Opioide, Schlaf- oder "
                    "Beruhigungsmittel, Antidepressiva, Antiepileptika, Allergiemittel)?",
                    show_if={"id": "regular_meds", "in": ["yes"]},
                    followup=_follow("sedating_meds_desc", "Welche Medikamente, in welcher Dosierung?")),
                _yn("med_side_effects",
                    "Bemerken Sie unter Ihren Medikamenten Nebenwirkungen wie Müdigkeit, "
                    "Verlangsamung, Konzentrationsstörungen oder Schwindel?",
                    show_if={"id": "regular_meds", "in": ["yes"]},
                    followup=_follow("med_side_effects_desc", "Welche Nebenwirkungen, und wie stark?")),
                _yn("med_recent_change",
                    "Wurde in den letzten Wochen ein solches Medikament neu angesetzt oder die Dosis "
                    "deutlich verändert?",
                    show_if={"id": "regular_meds", "in": ["yes"]},
                    followup=_follow("med_change_desc", "Welches Medikament, und wann?", "text")),
                _yn("benzo_regular",
                    "Nehmen Sie seit mehreren Monaten regelmäßig – auch nur abends in kleiner Menge – "
                    "Schlaf- oder Beruhigungsmittel (z.B. Benzodiazepine) ein?",
                    show_if={"id": "regular_meds", "in": ["yes"]},
                    followup=_follow("benzo_desc",
                                     "Welches Mittel, wie lange schon, und bemerken Sie beim Weglassen "
                                     "Entzugserscheinungen?")),
            ],
        },
        # ── 14 ────────────────────────────────────────────────────────────
        # (Fortsetzung unten; Gateway-Logik siehe GATEWAY_SKIP am Dateiende)
        {
            "id": "allgemein",
            "title": "Allgemeines & Einwilligung",
            "subtitle": "Weitere Angaben und Erklärungen",
            "questions": [
                _yn("multiple_conditions",
                    "Bestehen bei Ihnen mehrere Erkrankungen oder gesundheitliche Einschränkungen "
                    "gleichzeitig?",
                    hint="Mehrere Auffälligkeiten können in ihrer Summe eignungsrelevant sein, auch wenn "
                         "jede einzelne unbedenklich wäre (Leitlinien Kap. 2.7).",
                    followup=_follow("multiple_conditions_desc",
                                     "Bitte zählen Sie alle bekannten Erkrankungen kurz auf.")),
                _yn("other_conditions",
                    "Gibt es weitere Erkrankungen, Beschwerden oder frühere Operationen, die bisher "
                    "nicht erwähnt wurden?",
                    followup=_follow("other_conditions_desc", "Welche?")),
                _yn("driving_adaptation",
                    "Verzichten Sie wegen gesundheitlicher Einschränkungen bewusst auf bestimmte "
                    "Fahrten (z.B. bei Dunkelheit, lange Strecken, Autobahn)?",
                    followup=_follow("driving_adaptation_desc", "Auf welche Fahrten, und warum?")),
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
                             "meiner Daten zu verkehrsmedizinischen Zwecken ein.",
                    "error": "Bitte akzeptieren Sie die Datenschutzhinweise.",
                    "required": True,
                },
            ],
            "pdf_note": "Zur wahrheitsgemäßen Beantwortung aller Fragen sind Sie verpflichtet (§ 11 FeV).",
        },
    ],
}


# ── Gateway-Logik ─────────────────────────────────────────────────────────────
# Verneint der Patient die Eingangsfrage has_conditions (keine Vorerkrankung,
# keine dauerhafte Einschränkung, keine laufende Behandlung), werden die
# DIAGNOSE-orientierten Einstiegsfragen übersprungen. Symptom-, Ereignis- und
# Verhaltens-Screening (Anfälle, Synkopen, Schlaganfall, Tagesschläfrigkeit/ESS,
# Schwindel, Sehsymptome, Belastungsbeschwerden, Alkohol/Drogen/Medikamente)
# bleibt bewusst für ALLE Patienten aktiv — "keine Vorerkrankung" schließt
# unerkannte Symptome nicht aus (BASt-Anamnese Stufe 1).
GATEWAY_SKIP = {
    "eye_disease",
    "heart_disease", "heart_attack", "arrhythmia", "pacemaker_icd",
    "hypertension", "heart_other",
    "parkinson", "ms_spinal", "muscle_nerve",
    "ear_disease",
    "mobility_limits", "prosthesis", "vehicle_modified",
    "diabetes_type",
    "kidney_disease", "transplant", "lung_disease",
    "osas",
    "psychiatric", "psychosis",
    "multiple_conditions",
}

for _section in CATALOG["sections"]:
    for _question in _section["questions"]:
        if _question["id"] in GATEWAY_SKIP:
            assert "show_if" not in _question, _question["id"]
            _question["show_if"] = {"id": "has_conditions", "in": ["yes"]}
