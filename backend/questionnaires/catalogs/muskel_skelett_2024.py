# -*- coding: utf-8 -*-
"""Belastungen des Muskel-Skelett-Systems einschließlich Vibrationen –
DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische
Beratungen und Untersuchungen, Empfehlung "Belastungen des Muskel-Skelett-
Systems einschließlich Vibrationen" (E MSB, Fassung Januar 2022),
Ausgabe 2024, S. 801–837.

Anlässe nach ArbMedVV: Pflichtvorsorge bei Vibrationsexposition ab den
Expositionsgrenzwerten (Hand-Arm A(8) = 5 m/s²; Ganzkörper A(8) = 1,15 m/s²
in X/Y bzw. 0,8 m/s² in Z), Angebotsvorsorge bei wesentlich erhöhten
körperlichen Belastungen (AMR 13.2) und ab den Auslösewerten (Hand-Arm
2,5 m/s²; Ganzkörper 0,5 m/s²), Wunschvorsorge. Fristen nach AMR 2.1.
Untersuchungen nur nach ärztlichem Ermessen und mit Einverständnis;
Stufenkonzept: Basisuntersuchung -> klinische/ergänzende Untersuchung ->
ggf. fachspezifische Untersuchung (Orthopädie, Neurologie); bei
Hand-Arm-Vibrationen ergänzende HAV-Anamnese (Abschnitt 7.2.3).
"""

SLUG = "muskel_skelett-2024"

CATALOG = {
    "version": 2,
    "title": "Belastungen des Muskel-Skelett-Systems einschließlich Vibrationen (DGUV Empfehlung 2024)",
    "basis": (
        "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
        "Empfehlung „Belastungen des Muskel-Skelett-Systems einschließlich "
        "Vibrationen“ (E MSB, Fassung Januar 2022), Ausgabe 2024, S. 801–837"
    ),
    "sections": [
        # ── 1 ─ Anlass ─────────────────────────────────────────────────────
        {
            "id": "vorsorge",
            "title": "Anlass der Vorsorge",
            "subtitle": "Angaben zu Ihrer arbeitsmedizinischen Vorsorge",
            "questions": [
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen "
                             "körperlicher Belastungen oder Vibrationen – oder eine weitere Vorsorge?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich übe die Tätigkeit bereits aus)"},
                    ],
                },
                {
                    "id": "vorsorge_typ",
                    "type": "choice",
                    "label": "Um welche Art von Vorsorge handelt es sich?",
                    "hint": "Das steht meist in der Einladung Ihres Arbeitgebers. "
                            "Wenn Sie es nicht wissen, wählen Sie „Weiß ich nicht“.",
                    "required": True,
                    "options": [
                        {"value": "pflicht", "label": "Pflichtvorsorge (starke Vibrationsbelastung)"},
                        {"value": "angebot", "label": "Angebotsvorsorge (Arbeitgeber hat sie angeboten)"},
                        {"value": "wunsch", "label": "Wunschvorsorge (auf meinen eigenen Wunsch)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit & Belastungen ────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & körperliche Belastungen",
            "subtitle": "Welche Belastungen kommen bei Ihrer Arbeit vor?",
            "questions": [
                {
                    "id": "belastungsarten",
                    "type": "multi_choice",
                    "label": "Welche körperlichen Belastungen kommen bei Ihrer Arbeit "
                             "regelmäßig vor?",
                    "hint": "Bitte alles ankreuzen, was zutrifft.",
                    "required": True,
                    "options": [
                        {"value": "heben_tragen", "label": "Schwere Lasten heben, halten oder tragen"},
                        {"value": "ziehen_schieben", "label": "Schwere Lasten ziehen oder schieben (z. B. Betten, Rollbehälter, Müllbehälter)"},
                        {"value": "repetitiv", "label": "Ständig gleiche Hand-Arm-Bewegungen (z. B. Fließband, Kommissionieren, Nähen, Fleischverarbeitung)"},
                        {"value": "stehen", "label": "Dauerhaftes Stehen ohne Bewegungsmöglichkeit"},
                        {"value": "sitzen_fixiert", "label": "Dauerhaftes Sitzen in fester, vorgegebener Haltung (z. B. Mikroskop, Kranführerkabine, Leitwarte)"},
                        {"value": "rumpfbeuge", "label": "Arbeiten mit stark vorgebeugtem oder verdrehtem Oberkörper"},
                        {"value": "ueberkopf", "label": "Arbeiten mit den Händen über Schulterhöhe oder über Kopf"},
                        {"value": "knien_hocken", "label": "Arbeiten im Knien, Hocken, Kriechen oder Liegen"},
                        {"value": "ganzkoerperkraefte", "label": "Aufbringen hoher Körperkräfte (z. B. Brechstange, schwere Hämmer, Absperrschieber)"},
                        {"value": "fortbewegung", "label": "Viel Klettern, Steigen, Treppensteigen oder Kriechen (z. B. Masten, Gerüste, Schächte)"},
                        {"value": "druckabstuetzen", "label": "Dauerndes Abstützen auf Handgelenke, Ellenbogen oder Knie"},
                        {"value": "keine", "label": "Keine dieser Belastungen"},
                    ],
                },
                {
                    "id": "belastung_haeufigkeit",
                    "type": "choice",
                    "label": "Wie oft kommen diese Belastungen vor?",
                    "required": True,
                    "show_if": {"id": "belastungsarten", "not_in": ["keine"]},
                    "options": [
                        {"value": "taeglich", "label": "Täglich, über weite Teile der Schicht"},
                        {"value": "mehrmals_woche", "label": "Mehrmals pro Woche"},
                        {"value": "seltener", "label": "Nur gelegentlich"},
                    ],
                },
                {
                    "id": "taetigkeit_dauer",
                    "type": "choice",
                    "label": "Wie lange üben Sie diese Tätigkeit bereits aus?",
                    "required": True,
                    "options": [
                        {"value": "neu", "label": "Ich fange gerade erst an"},
                        {"value": "unter5", "label": "Weniger als 5 Jahre"},
                        {"value": "5bis10", "label": "5 bis 10 Jahre"},
                        {"value": "ueber10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "vib_hand",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit vibrierenden Maschinen oder Werkzeugen, die Sie "
                             "mit den Händen führen oder halten (z. B. Presslufthammer, "
                             "Winkelschleifer, Meißelhammer, Motorsäge, Rüttelplatte)?",
                    "required": True,
                    "followup": {
                        "id": "vib_hand_geraete", "type": "text",
                        "label": "Mit welchen Geräten und ungefähr wie viele Stunden pro Tag?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "vib_ganz",
                    "type": "yes_no",
                    "label": "Fahren Sie regelmäßig Fahrzeuge oder Arbeitsmaschinen mit starken "
                             "Erschütterungen (z. B. Bagger, Raupe, Traktor, Forstmaschine, "
                             "Gabelstapler auf unebenem Boden)?",
                    "required": True,
                    "followup": {
                        "id": "vib_ganz_geraete", "type": "text",
                        "label": "Welche Fahrzeuge/Maschinen und ungefähr wie viele Stunden pro Tag?",
                        "when": "yes", "required": False,
                    },
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden am Bewegungsapparat in den letzten 12 Monaten",
            "questions": [
                {
                    "id": "beschwerden_12m",
                    "type": "yes_no",
                    "label": "Hatten Sie in den letzten 12 Monaten Schmerzen oder Beschwerden "
                             "am Bewegungsapparat (Rücken, Nacken, Schultern, Arme, Hände, "
                             "Hüfte, Knie oder Füße)?",
                    "required": True,
                },
                {
                    "id": "beschwerden_lokalisation",
                    "type": "multi_choice",
                    "label": "Wo hatten Sie Beschwerden?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                    "options": [
                        {"value": "nacken", "label": "Nacken / Halswirbelsäule"},
                        {"value": "schulter_oberarm", "label": "Schulter / Oberarm"},
                        {"value": "ellenbogen_unterarm", "label": "Ellenbogen / Unterarm"},
                        {"value": "hand_handgelenk", "label": "Hand / Handgelenk / Finger"},
                        {"value": "oberer_ruecken", "label": "Oberer Rücken (Brustwirbelsäule)"},
                        {"value": "unterer_ruecken", "label": "Unterer Rücken (Lendenwirbelsäule)"},
                        {"value": "huefte", "label": "Hüfte / Oberschenkel"},
                        {"value": "knie", "label": "Knie"},
                        {"value": "fuss", "label": "Sprunggelenk / Fuß"},
                    ],
                },
                {
                    "id": "beschwerden_dauer",
                    "type": "choice",
                    "label": "Wie lange halten die Beschwerden an (oder hielten sie an)?",
                    "hint": "Schmerzen bis 14 Tage gelten als akut; ab etwa 3 Monaten "
                            "spricht man von chronischen Schmerzen.",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                    "options": [
                        {"value": "unter14tage", "label": "Kurz: bis etwa 14 Tage"},
                        {"value": "bis3monate", "label": "Länger: mehrere Wochen bis 3 Monate"},
                        {"value": "ueber3monate", "label": "Dauerhaft: länger als 3 Monate"},
                    ],
                },
                {
                    "id": "beschwerden_belastung",
                    "type": "yes_no",
                    "label": "Werden die Beschwerden durch Ihre Arbeit ausgelöst oder deutlich "
                             "verstärkt?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                    "followup": {
                        "id": "beschwerden_belastung_detail", "type": "text",
                        "label": "Bei welchen Arbeiten oder Bewegungen?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "beschwerden_entlastung",
                    "type": "yes_no",
                    "label": "Bessern sich die Beschwerden, wenn Sie nicht arbeiten "
                             "(abends, am Wochenende, im Urlaub)?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                },
                {
                    "id": "ausstrahlung",
                    "type": "yes_no",
                    "label": "Strahlen die Schmerzen in ein Bein oder einen Arm aus, oder "
                             "haben Sie dabei Taubheitsgefühle oder Lähmungserscheinungen?",
                    "hint": "Das kann auf eine Reizung von Nerven hinweisen (z. B. durch "
                            "einen Bandscheibenschaden).",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                },
                {
                    "id": "arzt_beschwerden",
                    "type": "yes_no",
                    "label": "Waren Sie wegen dieser Beschwerden bei einer Ärztin / einem Arzt?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                    "followup": {
                        "id": "arzt_beschwerden_diagnose", "type": "text",
                        "label": "Welche Diagnose wurde gestellt (falls bekannt)?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "au_beschwerden",
                    "type": "yes_no",
                    "label": "Waren Sie in den letzten 12 Monaten wegen dieser Beschwerden "
                             "krankgeschrieben?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                    "followup": {
                        "id": "au_beschwerden_dauer", "type": "text",
                        "label": "Wie oft und insgesamt wie lange?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "kribbeln_haende",
                    "type": "yes_no",
                    "label": "Haben Sie Taubheitsgefühle oder Kribbeln in den Händen oder "
                             "Fingern – auch nachts?",
                    "hint": "Solche Beschwerden können z. B. auf ein Karpaltunnelsyndrom "
                            "(Einengung eines Handnervs) hinweisen.",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Hand-Arm-Vibrationen ───────────────────────────────────────
        {
            "id": "hand_arm",
            "title": "Beschwerden durch Hand-Arm-Vibrationen",
            "subtitle": "Nur relevant, wenn Sie mit vibrierenden Geräten arbeiten",
            "questions": [
                {
                    "id": "weissfinger",
                    "type": "yes_no",
                    "label": "Werden einzelne Finger bei Kälte anfallsartig weiß, taub oder "
                             "gefühllos („Weißfingerkrankheit“)?",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                    "followup": {
                        "id": "weissfinger_detail", "type": "text",
                        "label": "Welche Finger sind betroffen und wie oft passiert das?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "hand_gelenkschmerz",
                    "type": "yes_no",
                    "label": "Haben Sie Schmerzen oder Kraftlosigkeit in Handgelenken, "
                             "Ellenbogen oder Schultern – besonders bei Arbeitsbeginn oder "
                             "nachts in Ruhe?",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                },
                {
                    "id": "hand_geschicklichkeit",
                    "type": "yes_no",
                    "label": "Ist Ihr Tastgefühl oder Ihre Fingergeschicklichkeit vermindert "
                             "(z. B. Probleme beim Zuknöpfen oder Greifen kleiner Teile)?",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Behandlungen",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "behandlung_12m",
                    "type": "yes_no",
                    "label": "Waren Sie in den letzten 12 Monaten wegen des Bewegungsapparats "
                             "in ärztlicher, physiotherapeutischer oder sonstiger Behandlung "
                             "(z. B. Krankengymnastik, Massage, Spritzen)?",
                    "required": True,
                    "followup": {
                        "id": "behandlung_12m_detail", "type": "text",
                        "label": "Welche Behandlung und weswegen?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein (auch Schmerzmittel)?",
                    "required": True,
                    "followup": {
                        "id": "medikamente_detail", "type": "text",
                        "label": "Welche Medikamente?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "vorerkrankung_ruecken",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung der Wirbelsäule bekannt "
                             "(z. B. Bandscheibenvorfall, Wirbelgleiten, Wirbelkanal-Verengung, "
                             "Osteoporose/Knochenschwund, starke Skoliose, Morbus Bechterew, "
                             "Operation an der Wirbelsäule)?",
                    "required": True,
                    "followup": {
                        "id": "vorerkrankung_ruecken_detail", "type": "text",
                        "label": "Welche Erkrankung und seit wann?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "vorerkrankung_schulter_arm",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung an Schulter, Arm oder Hand bekannt "
                             "(z. B. Sehnenriss der Schulter, Schulterenge/Impingement, "
                             "Sehnenscheidenentzündung, Karpaltunnelsyndrom, Arthrose, "
                             "Durchblutungsstörung der Hände)?",
                    "required": True,
                    "followup": {
                        "id": "vorerkrankung_schulter_arm_detail", "type": "text",
                        "label": "Welche Erkrankung und seit wann?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "vorerkrankung_bein",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung an Hüfte, Knie oder Fuß bekannt "
                             "(z. B. Meniskusschaden, Kreuzbandriss, Arthrose/Gelenkverschleiß, "
                             "Hüftdysplasie, Fußfehlstellung)?",
                    "required": True,
                    "followup": {
                        "id": "vorerkrankung_bein_detail", "type": "text",
                        "label": "Welche Erkrankung und seit wann?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "unfall_op",
                    "type": "yes_no",
                    "label": "Hatten Sie Unfälle, Knochenbrüche oder Operationen am "
                             "Bewegungsapparat, deren Folgen Sie heute noch spüren?",
                    "required": True,
                    "followup": {
                        "id": "unfall_op_detail", "type": "text",
                        "label": "Was ist passiert und wann?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "rheuma",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine rheumatische Erkrankung bekannt "
                             "(z. B. rheumatoide Arthritis, Gicht, Psoriasis-Arthritis)?",
                    "required": True,
                },
                {
                    "id": "begleiterkrankungen",
                    "type": "multi_choice",
                    "label": "Haben Sie eine der folgenden weiteren Erkrankungen?",
                    "hint": "Diese Erkrankungen können die körperliche Belastbarkeit "
                            "zusätzlich einschränken.",
                    "required": True,
                    "options": [
                        {"value": "bluthochdruck", "label": "Bluthochdruck, der trotz Medikamenten schlecht eingestellt ist"},
                        {"value": "herz", "label": "Herzerkrankung (Durchblutungsstörung, Rhythmusstörung, Herzschwäche)"},
                        {"value": "gefaesse", "label": "Gefäßverkalkung (Arteriosklerose) mit Beschwerden, z. B. beim Gehen"},
                        {"value": "atemwege", "label": "Chronische Atemwegserkrankung (COPD) oder Asthma"},
                        {"value": "diabetes_insulin", "label": "Diabetes mellitus mit Insulinbehandlung"},
                        {"value": "niere", "label": "Nierenerkrankung mit eingeschränkter Nierenfunktion"},
                        {"value": "haut", "label": "Chronische Hauterkrankung"},
                        {"value": "keine", "label": "Keine dieser Erkrankungen"},
                    ],
                },
            ],
        },
        # ── 6 ─ Einwilligung ───────────────────────────────────────────────
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
    # ── kritisch: Klärung vor Aufnahme/Fortsetzung der Tätigkeit ──────────
    {"wenn": {"ausstrahlung": ["yes"], "beschwerden_dauer": ["ueber3monate"]},
     "schwere": "kritisch",
     "bereich": "Wirbelsäule / Nervensystem",
     "quelle": "E MSB 7.4 / 7.4.3–7.4.4",
     "befund": "Chronische Schmerzen (> 3 Monate) mit Ausstrahlung bzw. Taubheits-/"
               "Lähmungserscheinungen – Hinweis auf andauernde radikuläre Symptomatik.",
     "konsequenz": "Klärung VOR Aufnahme bzw. Fortsetzung der belastenden Tätigkeit: "
                   "ergänzende klinische Untersuchung und fachspezifische Vorstellung "
                   "(Orthopädie/Neurologie) veranlassen. Nach 7.4 prüfen, ob die Tätigkeit "
                   "ohne gesundheitliche Gefährdung möglich ist; ggf. Maßnahmen nach 7.4.2, "
                   "verkürzte Vorsorgefrist nach 7.4.3 oder Tätigkeitswechsel nach 7.4.4 "
                   "erwägen (Mitteilung an den Arbeitgeber nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"vorerkrankung_ruecken": ["yes"],
              "belastungsarten": ["heben_tragen", "ziehen_schieben", "rumpfbeuge", "ganzkoerperkraefte"]},
     "schwere": "kritisch",
     "bereich": "Wirbelsäule",
     "quelle": "E MSB 7.4 „Erkrankungen des Rückens“ / 7.4.2",
     "befund": "Bekannte Wirbelsäulenerkrankung bei Tätigkeit mit Lastenhandhabung, "
               "Rumpfbeuge oder hohen Ganzkörperkräften.",
     "konsequenz": "Vor (weiterem) Einsatz ergänzende Untersuchung der Wirbelsäule "
                   "durchführen. Prüfen, ob die Tätigkeit nur unter Voraussetzungen möglich "
                   "ist: Substitution belastender Tätigkeiten, technische/organisatorische "
                   "Schutzmaßnahmen (Begrenzung der Expositionszeit), Einsatz an Arbeitsplätzen "
                   "mit geringerer Belastung (7.4.2); ggf. verkürzte Frist (7.4.3)."},
    # ── pruefen: Ergänzungsuntersuchung / Abklärung ───────────────────────
    {"wenn": {"beschwerden_12m": ["yes"], "beschwerden_belastung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Muskel-Skelett-System",
     "quelle": "E MSB 7.2.1–7.2.2 (Stufenkonzept)",
     "befund": "Arbeitsbezogene Beschwerden am Muskel-Skelett-System in den letzten "
               "12 Monaten (durch die Arbeit ausgelöst oder verstärkt).",
     "konsequenz": "Auffällige Anamnese: körperliche Grunduntersuchung und ergänzende "
                   "klinische Untersuchung der betroffenen Körperregionen nach dem "
                   "Stufenkonzept durchführen (Leitfaden Anhang 4); Lokalisation, Ausprägung "
                   "und Belastungsabhängigkeit dokumentieren."},
    {"wenn": {"beschwerden_12m": ["yes"], "beschwerden_entlastung": ["no"]},
     "schwere": "pruefen",
     "bereich": "Chronifizierung",
     "quelle": "E MSB 6.3.1 / 8",
     "befund": "Beschwerden bilden sich bei Entlastung (Feierabend, Wochenende, Urlaub) "
               "nicht zurück – Hinweis auf beginnende belastungsunabhängige Chronifizierung.",
     "konsequenz": "Eingehende Abklärung veranlassen; sekundärpräventive Maßnahmen "
                   "rechtzeitig einleiten, bevor die Belastbarkeit krankheitsbedingt "
                   "herabgesetzt ist (Beratung nach Abschnitt 8)."},
    {"wenn": {"beschwerden_dauer": ["ueber3monate"]},
     "schwere": "pruefen",
     "bereich": "Chronische Schmerzen",
     "quelle": "E MSB 8 (Abschließende Beratung)",
     "befund": "Schmerzen am Bewegungsapparat seit mehr als 3 Monaten.",
     "konsequenz": "Bei Chronifizierung starker Schmerzen (> 3 Monate) Vorstellung in "
                   "einer Schmerzambulanz empfehlen; differenzialdiagnostische Klärung "
                   "der Befunde (Orthopädie, Neurologie o. a.) anstoßen."},
    {"wenn": {"weissfinger": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hand-Arm-Vibrationen",
     "quelle": "E MSB 6.3.3 / 7.2.3 (BK-Nr. 2104)",
     "befund": "Anfallsartiges Weißwerden/Taubwerden der Finger bei Kälte – Verdacht auf "
               "vibrationsbedingtes vasospastisches Syndrom (VVS, Weißfingerkrankheit).",
     "konsequenz": "Ergänzungsuntersuchung bei Hand-Arm-Vibrationsbelastung durchführen "
                   "(Formblatt „Ärztliche Anamnese für Hand-Arm-Vibrationsbelastungen“, "
                   "Anhang 5); angiologische Abklärung empfehlen; BK-Nr. 2104 beachten; "
                   "Beratung zu Kälteschutz und vibrationsmindernden Werkzeugen."},
    {"wenn": {"kribbeln_haende": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervenkompression",
     "quelle": "E MSB 6.3.3 / 7.4 (BK-Nr. 2113)",
     "befund": "Taubheitsgefühle oder Kribbeln in Händen/Fingern (auch nachts) – möglicher "
               "Hinweis auf ein Karpaltunnelsyndrom oder anderes Nervenkompressionssyndrom.",
     "konsequenz": "Neurologische Abklärung (fachspezifische Untersuchung) empfehlen; "
                   "bei repetitiven manuellen Tätigkeiten oder Hand-Arm-Vibrationen "
                   "BK-Nr. 2113 beachten; Belastungssituation (Kraftaufwand, "
                   "Handgelenksbeugung) in der Gefährdungsbeurteilung überprüfen lassen."},
    {"wenn": {"hand_gelenkschmerz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hand-Arm-Vibrationen",
     "quelle": "E MSB 6.3.3 (BK-Nr. 2103)",
     "befund": "Gelenkschmerzen/Kraftlosigkeit an Hand, Ellenbogen oder Schulter bei "
               "Arbeit mit vibrierenden Geräten – mögliche Knochen- oder Gelenkschäden "
               "durch niederfrequente Vibrationen.",
     "konsequenz": "Ergänzende klinische Untersuchung der oberen Extremitäten; bei "
                   "auffälligem Befund fachorthopädische Abklärung (Bildgebung über die "
                   "kurative Versorgung) empfehlen; BK-Nr. 2103 beachten."},
    {"wenn": {"vorerkrankung_bein": ["yes"], "belastungsarten": ["knien_hocken", "fortbewegung"]},
     "schwere": "pruefen",
     "bereich": "Kniegelenke",
     "quelle": "E MSB 7.4 / 8 (BK-Nr. 2112)",
     "befund": "Bekannte Knie-/Beinerkrankung bei Tätigkeit im Knien, Hocken oder mit "
               "häufiger Körperfortbewegung.",
     "konsequenz": "Ergänzende Untersuchung der unteren Extremitäten; Gonarthrose-Risiko "
                   "(BK-Nr. 2112) beachten; individualpräventive Maßnahmen empfehlen "
                   "(z. B. Kniekolleg der BG BAU), knieentlastende Arbeitsgestaltung und "
                   "Knieschutz ansprechen."},
    {"wenn": {"unfall_op": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Posttraumatische Zustände",
     "quelle": "E MSB 7.4 / 7.4.3",
     "befund": "Folgen von Unfällen oder Operationen am Bewegungsapparat mit noch "
               "spürbaren Beschwerden – zeitlich verminderte Belastbarkeit möglich.",
     "konsequenz": "Funktionsfähigkeit in der ergänzenden Untersuchung beurteilen; bei zu "
                   "erwartender Änderung des Schweregrads verkürzte Vorsorgefrist "
                   "vereinbaren (7.4.3); ggf. vorübergehende Einsatzanpassung vorschlagen."},
    {"wenn": {"rheuma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Rheumatischer Formenkreis",
     "quelle": "E MSB 7.4",
     "befund": "Erkrankung des rheumatischen Formenkreises bekannt.",
     "konsequenz": "Einfluss auf die muskuloskelettale Belastbarkeit prüfen; aktuellen "
                   "Behandlungsstatus erfragen und in die Beurteilung einbeziehen; ggf. "
                   "verkürzte Vorsorgefrist und Rücksprache mit der behandelnden "
                   "Rheumatologie (mit Einwilligung)."},
    {"wenn": {"begleiterkrankungen": ["bluthochdruck", "herz", "gefaesse", "atemwege",
                                      "diabetes_insulin", "niere", "haut"]},
     "schwere": "pruefen",
     "bereich": "Begleiterkrankungen",
     "quelle": "E MSB 7.4 (leistungsbegrenzende Erkrankungen)",
     "befund": "Begleiterkrankung, die die körperliche Belastbarkeit einschränken kann "
               "(Herz-Kreislauf, Atemwege, Stoffwechsel, Niere, Haut).",
     "konsequenz": "Bei der Beurteilung der Belastbarkeit berücksichtigen; Ausmaß und "
                   "Behandlungsstand klären, ggf. hausärztliche/fachärztliche Befunde "
                   "einholen (mit Einwilligung) und mit dem Belastungsprofil des "
                   "Arbeitsplatzes abgleichen."},
    {"wenn": {"au_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Verlauf / Fristen",
     "quelle": "E MSB 7.4.3",
     "befund": "Arbeitsunfähigkeit wegen Muskel-Skelett-Beschwerden in den letzten "
               "12 Monaten.",
     "konsequenz": "Verkürzte Vorsorgefrist erwägen (Erkenntnisse, bei denen verkürzte "
                   "Fristen empfohlen werden); Maßnahmen nach 7.4.2 prüfen und Rückmeldung "
                   "an das Unternehmen zu Schutzmaßnahmen erwägen (§ 6 (4) ArbMedVV, "
                   "AMR 6.4)."},
    # ── hinweis: Beratung / Verfahrenshinweise ────────────────────────────
    {"wenn": {"vib_hand": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hand-Arm-Vibrationen",
     "quelle": "E MSB 2 / 7.2.3",
     "befund": "Tätigkeit mit Hand-Arm-Vibrationen.",
     "konsequenz": "Im Rahmen der Basisuntersuchung ergänzende ärztliche HAV-Anamnese "
                   "durchführen (Anamnesebogen 3, Anhang 5). Expositionswerte aus der "
                   "Gefährdungsbeurteilung prüfen: Angebotsvorsorge ab Auslösewert "
                   "A(8) = 2,5 m/s², Pflichtvorsorge ab Expositionsgrenzwert A(8) = 5 m/s²; "
                   "Beratung zu vibrationsmindernden Maschinen und Expositionszeiten."},
    {"wenn": {"vib_ganz": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Ganzkörpervibrationen",
     "quelle": "E MSB 2 / 6.3.3 (BK-Nr. 2110)",
     "befund": "Tätigkeit mit Ganzkörpervibrationen (Fahrzeuge/Arbeitsmaschinen).",
     "konsequenz": "Expositionswerte prüfen: Angebotsvorsorge ab Auslösewert A(8) = 0,5 m/s², "
                   "Pflichtvorsorge ab A(8) = 1,15 m/s² (X/Y) bzw. 0,8 m/s² (Z). Auf "
                   "Rückenbeschwerden achten (BK-Nr. 2110); Beratung zu Sitzfederung, "
                   "Fahrweise und Expositionszeiten."},
    {"wenn": {"behandlung_12m": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Anamnese",
     "quelle": "E MSB 7.1",
     "befund": "Behandlungen am Muskel-Skelett-System innerhalb der letzten 12 Monate.",
     "konsequenz": "Behandlungen dokumentieren (Bestandteil der Eingangsberatung) und für "
                   "die Verlaufsbeurteilung bei weiteren Vorsorgen heranziehen."},
    {"wenn": {"medikamente": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Medikamente",
     "quelle": "E MSB 7.1",
     "befund": "Regelmäßige Medikamenteneinnahme.",
     "konsequenz": "Medikamentenanamnese vertiefen (u. a. Schmerzmittel-Dauergebrauch als "
                   "Hinweis auf unzureichend behandelte Beschwerden) und bei der "
                   "Beurteilung berücksichtigen."},
]
