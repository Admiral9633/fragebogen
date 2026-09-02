# -*- coding: utf-8 -*-
"""G 46 Belastungen des Muskel- und Skelettsystems einschließlich Vibrationen –
DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für arbeitsmedizinische
Untersuchungen, 7. Auflage 2016 (Gentner Verlag), G 46 »Belastungen des
Muskel- und Skelettsystems einschließlich Vibrationen« (Fassung Oktober 2014),
S. 869–888, sowie Anhang 4 »Leitfaden zur Diagnostik von Muskel-Skelett-
Erkrankungen«, S. 959–972.

Fristen nach G 46 (ersatzweise, wenn keine staatlichen Vorgaben):
Erstuntersuchung vor Aufnahme der Tätigkeit; Nachuntersuchung nach
60 Monaten, ab 40 Jahren nach 36 Monaten; vorzeitig bei auffälligen
Befunden, bei vermutetem Zusammenhang zwischen Erkrankung und Tätigkeit
sowie zur Beurteilung der individuellen Belastbarkeit (z. B.
Wiedereingliederung nach längerer Erkrankung oder Operation).
Aufbau: Basisuntersuchung (Anamnese 1/2, klinische Untersuchung) ->
Ergänzungsuntersuchung bei Auffälligkeiten; Spezieller Teil zu
Hand-Arm-Vibrationen (BK 2103 Knochen-/Gelenkschäden, BK 2104 VVS)
mit gesondertem Anamnesebogen und Stockholm Scale.
"""

SLUG = "g46-muskel_skelett-2016"

CATALOG = {
    "version": 2,
    "title": "G 46 Belastungen des Muskel- und Skelettsystems einschließlich Vibrationen (DGUV Grundsatz 2016)",
    "basis": (
        "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 7. Auflage 2016, "
        "G 46 »Belastungen des Muskel- und Skelettsystems einschließlich Vibrationen« "
        "(Fassung Oktober 2014), S. 869–888, und Anhang 4 »Leitfaden zur Diagnostik "
        "von Muskel-Skelett-Erkrankungen«, S. 959–972"
    ),
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Untersuchungsanlass",
            "subtitle": "Angaben zu Ihrer G-46-Untersuchung",
            "questions": [
                {
                    "id": "untersuchungsart",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich?",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der belastenden Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich übe die Tätigkeit bereits aus)"},
                    ],
                },
                {
                    "id": "alter_ab40",
                    "type": "yes_no",
                    "label": "Sind Sie 40 Jahre oder älter?",
                    "hint": "Ab 40 Jahren gilt eine kürzere Nachuntersuchungsfrist "
                            "(36 statt 60 Monate).",
                    "required": True,
                },
                {
                    "id": "letzte_untersuchung",
                    "type": "choice",
                    "label": "Wann war Ihre letzte G-46-Untersuchung?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach"]},
                    "options": [
                        {"value": "unter3jahre", "label": "Vor weniger als 3 Jahren"},
                        {"value": "3bis5jahre", "label": "Vor 3 bis 5 Jahren"},
                        {"value": "ueber5jahre", "label": "Vor mehr als 5 Jahren"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "wiedereingliederung",
                    "type": "yes_no",
                    "label": "Kehren Sie gerade nach einer längeren Erkrankung oder Operation "
                             "an Ihren Arbeitsplatz zurück (Wiedereingliederung)?",
                    "required": True,
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {
                        "id": "zusammenhang_detail", "type": "text",
                        "label": "Welche Beschwerden und welcher Zusammenhang?",
                        "when": "yes", "required": False,
                    },
                },
            ],
        },
        # ── 2 ─ Tätigkeit & Belastungen ────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Belastungen",
            "subtitle": "Arbeitsbedingte Belastungen des Muskel- und Skelettsystems",
            "questions": [
                {
                    "id": "belastungen",
                    "type": "multi_choice",
                    "label": "Welche Belastungen kommen bei Ihrer Arbeit regelmäßig vor?",
                    "hint": "Bitte alles ankreuzen, was zutrifft.",
                    "required": True,
                    "options": [
                        {"value": "heben_tragen", "label": "Schwere Lasten heben, halten oder tragen"},
                        {"value": "ziehen_schieben", "label": "Schwere Lasten ziehen oder schieben"},
                        {"value": "stehen", "label": "Dauerndes Stehen"},
                        {"value": "sitzen", "label": "Dauerndes Sitzen in erzwungener Haltung"},
                        {"value": "rumpfbeuge", "label": "Arbeiten mit gebeugtem oder verdrehtem Oberkörper"},
                        {"value": "knien_hocken", "label": "Arbeiten im Hocken, Knien oder Liegen"},
                        {"value": "ueberkopf", "label": "Arbeiten mit den Armen über Schulterhöhe"},
                        {"value": "kraft", "label": "Arbeiten mit hoher Kraftanstrengung oder Krafteinwirkung"},
                        {"value": "steigen_klettern", "label": "Schwer zugängliche Arbeitsstellen (Steigen, Klettern)"},
                        {"value": "hand_werkzeug", "label": "Einsatz der Hände als »Werkzeug« (Klopfen, Hämmern, Drehen, Drücken)"},
                        {"value": "repetitiv", "label": "Sich ständig wiederholende Handgriffe mit hoher Frequenz"},
                        {"value": "keine", "label": "Keine dieser Belastungen"},
                    ],
                },
                {
                    "id": "vib_hand",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit vibrierenden Geräten oder Maschinen, die Sie mit "
                             "den Händen führen oder halten?",
                    "required": True,
                },
                {
                    "id": "vib_hand_art",
                    "type": "multi_choice",
                    "label": "Mit welcher Art von vibrierenden Geräten arbeiten Sie?",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                    "options": [
                        {"value": "druckluft", "label": "Schlagende Druckluft- oder Elektrowerkzeuge (Presslufthammer/-meißel, Schlaghammer, Schlagbohrer, Aufbruchhammer, Schlagschrauber)"},
                        {"value": "hochfrequent", "label": "Hochtourige Geräte (Bohrer, Meißel, Fräsen, Schneide-, Schleif- und Poliermaschinen, Motorkettensäge)"},
                        {"value": "sonstige", "label": "Andere / weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "vib_ganz",
                    "type": "yes_no",
                    "label": "Sitzen Sie bei der Arbeit regelmäßig auf Fahrzeugen oder Maschinen "
                             "mit spürbaren Erschütterungen (Ganzkörperschwingungen, z. B. "
                             "Bagger, Traktor, Stapler auf unebenem Boden)?",
                    "required": True,
                },
                {
                    "id": "kaelte_arbeit",
                    "type": "yes_no",
                    "label": "Arbeiten Sie häufig in Kälte oder im Winter im Freien?",
                    "hint": "Kälte kann Durchblutungsstörungen der Finger auslösen oder "
                            "verstärken.",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                },
            ],
        },
        # ── 3 ─ Beschwerden (Anamnese 1) ───────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden bei der Arbeit",
            "subtitle": "Eigene Angaben zu Muskel-Skelett-Beschwerden (letzte 12 Monate)",
            "questions": [
                {
                    "id": "beschwerden_12m",
                    "type": "yes_no",
                    "label": "Hatten Sie in den letzten 12 Monaten Schmerzen oder Beschwerden "
                             "am Muskel- und Skelettsystem (Rücken, Nacken, Schultern, Arme, "
                             "Hände, Hüfte, Knie oder Füße)?",
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
                        {"value": "unterer_ruecken", "label": "Unterer Rücken (Lendenwirbelsäule / Kreuz)"},
                        {"value": "huefte", "label": "Hüfte / Oberschenkel"},
                        {"value": "knie", "label": "Knie"},
                        {"value": "fuss", "label": "Sprunggelenk / Fuß"},
                    ],
                },
                {
                    "id": "beschwerden_verstaerker",
                    "type": "multi_choice",
                    "label": "Welche Belastungen bei der Arbeit verstärken Ihre Beschwerden "
                             "besonders?",
                    "hint": "Diese Zuordnung hilft bei der Bewertung, ob die Beschwerden "
                            "arbeitsbedingt sind.",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                    "options": [
                        {"value": "heben_tragen", "label": "Schwere Lasten heben oder tragen"},
                        {"value": "gebueckt_verdreht", "label": "Gebückte oder verdrehte Körperhaltung"},
                        {"value": "knien_hocken", "label": "Knien oder Hocken"},
                        {"value": "stehen", "label": "Dauerndes Stehen"},
                        {"value": "ueberkopf", "label": "Arbeit mit den Händen über Schulterhöhe"},
                        {"value": "vib_hand", "label": "Schwingungen am Hand-Arm-System (Werkzeuge, vibrierende Maschinen)"},
                        {"value": "vib_ganz", "label": "Ganzkörperschwingungen beim Sitzen auf Fahrzeugen oder Maschinen"},
                        {"value": "keine_zuordnung", "label": "Keine eindeutige Zuordnung möglich"},
                    ],
                },
                {
                    "id": "entlastung_besserung",
                    "type": "yes_no",
                    "label": "Bessern sich die Beschwerden in belastungsarmen Zeiten "
                             "(nachts, am Wochenende, im Urlaub)?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                },
                {
                    "id": "ausstrahlung",
                    "type": "yes_no",
                    "label": "Strahlen die Schmerzen in ein Bein oder einen Arm aus, oder haben "
                             "Sie dabei Taubheitsgefühle oder Lähmungserscheinungen?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                },
                {
                    "id": "schmerz_dauer3m",
                    "type": "yes_no",
                    "label": "Bestehen die starken Schmerzen seit mehr als 3 Monaten?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                },
                {
                    "id": "arzt_wegen_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie wegen dieser Beschwerden eine Ärztin / einen Arzt "
                             "aufgesucht?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                    "followup": {
                        "id": "arzt_diagnose", "type": "text",
                        "label": "Welche Diagnose wurde gestellt (falls bekannt)?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "au_12m",
                    "type": "yes_no",
                    "label": "Waren Sie in den letzten 12 Monaten wegen dieser Beschwerden "
                             "arbeitsunfähig (krankgeschrieben)?",
                    "required": True,
                    "show_if": {"id": "beschwerden_12m", "in": ["yes"]},
                    "followup": {
                        "id": "au_12m_detail", "type": "text",
                        "label": "Wie oft und insgesamt wie lange?",
                        "when": "yes", "required": False,
                    },
                },
            ],
        },
        # ── 4 ─ Hand-Arm-Vibrationen (Spezieller Teil) ─────────────────────
        {
            "id": "hand_arm",
            "title": "Hand-Arm-Vibrationen",
            "subtitle": "Fragen für Beschäftigte mit vibrierenden Geräten (Spezieller Teil G 46)",
            "questions": [
                {
                    "id": "weissfinger",
                    "type": "yes_no",
                    "label": "Werden einzelne Finger – vor allem bei Kälte – anfallsartig weiß "
                             "und gefühllos (»Weißfingerkrankheit«, Absterbe- oder Kältegefühl)?",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                    "followup": {
                        "id": "weissfinger_detail", "type": "text",
                        "label": "Welche Finger sind betroffen und wie oft treten die Anfälle auf?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "weissfinger_freizeit",
                    "type": "yes_no",
                    "label": "Treten diese Anfälle auch außerhalb der Arbeit auf "
                             "(z. B. beim Radfahren ohne Handschuhe oder beim Autowaschen)?",
                    "hint": "Anfälle unabhängig von der Arbeit sprechen für ein "
                            "fortgeschrittenes Stadium.",
                    "required": True,
                    "show_if": {"id": "weissfinger", "in": ["yes"]},
                },
                {
                    "id": "taubheit_finger",
                    "type": "yes_no",
                    "label": "Haben Sie anfallsweise oder andauernd Taubheitsgefühle oder "
                             "Kribbeln in den Fingern?",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                },
                {
                    "id": "geschicklichkeit",
                    "type": "yes_no",
                    "label": "Sind Ihr Tastgefühl oder Ihre Handgeschicklichkeit vermindert "
                             "(z. B. Probleme beim Greifen kleiner Teile oder beim Zuknöpfen)?",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                },
                {
                    "id": "gelenk_beschwerden_arm",
                    "type": "yes_no",
                    "label": "Haben Sie Kraftlosigkeit, Schmerzen bei Arbeitsbeginn oder "
                             "Schmerzen in Ruhe (besonders nachts) in Handgelenken, Ellenbogen "
                             "oder Schultern?",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                },
                {
                    "id": "raucher",
                    "type": "yes_no",
                    "label": "Rauchen Sie?",
                    "hint": "Nikotin verengt die Blutgefäße und kann Durchblutungsstörungen "
                            "der Finger verstärken.",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                },
                {
                    "id": "medikamente_gefaess",
                    "type": "yes_no",
                    "label": "Nehmen Sie Medikamente ein, die die Durchblutung beeinflussen "
                             "können (z. B. Betablocker gegen Bluthochdruck oder "
                             "Migränemittel mit Ergotamin)?",
                    "required": True,
                    "show_if": {"id": "vib_hand", "in": ["yes"]},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Behandlungen",
            "subtitle": "Frühere Erkrankungen, Operationen und Unfälle",
            "questions": [
                {
                    "id": "vorerkrankung_wirbelsaeule",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung der Wirbelsäule bekannt "
                             "(z. B. Bandscheibenvorfall, Wirbelgleiten, Wirbelkanal-Verengung, "
                             "Osteoporose/Knochenschwund, starke Skoliose, Morbus Bechterew, "
                             "Wirbelsäulen-Operation)?",
                    "required": True,
                    "followup": {
                        "id": "vorerkrankung_wirbelsaeule_detail", "type": "text",
                        "label": "Welche Erkrankung und seit wann?",
                        "when": "yes", "required": False,
                    },
                },
                {
                    "id": "vorerkrankung_schulter_arm",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung an Schulter, Arm oder Hand bekannt "
                             "(z. B. Schulterenge/Impingement, Sehnenriss, Sehnenscheiden-"
                             "entzündung, Karpaltunnelsyndrom, Arthrose, Erkrankung der "
                             "Handwurzelknochen)?",
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
                             "Hüftdysplasie, ausgeprägte Fußfehlstellung)?",
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
                    "label": "Hatten Sie frühere Erkrankungen, Operationen oder schwere Unfälle "
                             "am Bewegungsapparat, deren Folgen Sie heute noch spüren?",
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
                            "zusätzlich begrenzen.",
                    "required": True,
                    "options": [
                        {"value": "bluthochdruck", "label": "Bluthochdruck, der mit Medikamenten schlecht einstellbar ist"},
                        {"value": "herz", "label": "Herzerkrankung (Durchblutungsstörung des Herzens, nicht ausreichend behandelbare Rhythmusstörungen)"},
                        {"value": "arteriosklerose", "label": "Gefäßverkalkung (Arteriosklerose) mit Beschwerden, z. B. in den Beinen"},
                        {"value": "atemwege", "label": "Chronische Atemwegserkrankung mit deutlicher Einschränkung oder Asthma mit häufigen Anfällen"},
                        {"value": "diabetes_insulin", "label": "Diabetes mellitus mit Insulinbehandlung"},
                        {"value": "niere", "label": "Nierenerkrankung mit eingeschränkter Nierenfunktion"},
                        {"value": "keine", "label": "Keine dieser Erkrankungen"},
                    ],
                },
                {
                    "id": "behandlung_12m",
                    "type": "yes_no",
                    "label": "Waren Sie in den letzten 12 Monaten wegen des Bewegungsapparats "
                             "in ärztlicher oder physiotherapeutischer Behandlung "
                             "(z. B. Krankengymnastik, Massage, Spritzen)?",
                    "required": True,
                    "followup": {
                        "id": "behandlung_12m_detail", "type": "text",
                        "label": "Welche Behandlung und weswegen?",
                        "when": "yes", "required": False,
                    },
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
    # ── kritisch: gesundheitliche Bedenken erwägen / Klärung vor Einsatz ──
    {"wenn": {"ausstrahlung": ["yes"], "schmerz_dauer3m": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Wirbelsäule / Nervensystem",
     "quelle": "G 46 2.1 / 3.2 »Erkrankungen der Wirbelsäule«",
     "befund": "Chronische Schmerzen (> 3 Monate) mit Ausstrahlung bzw. Taubheits-/"
               "Lähmungserscheinungen – Hinweis auf Bandscheibenschaden mit andauernden "
               "radikulären Symptomen.",
     "konsequenz": "Ergänzungsuntersuchung vor (weiterer) Aufnahme der Tätigkeit; "
                   "fachspezifische Untersuchung (Orthopädie/Neurologie) empfehlen. "
                   "Befristete oder dauernde gesundheitliche Bedenken nach 2.1.1/2.1.2 "
                   "prüfen; sonst Voraussetzungen nach 2.1.3 festlegen (zeitliche "
                   "Begrenzung der Einwirkung, ergonomische Gestaltung, Individualmaßnahmen)."},
    {"wenn": {"weissfinger": ["yes"], "weissfinger_freizeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Hand-Arm-Vibrationen",
     "quelle": "G 46 Spezieller Teil 2.4 / 2.7 (BK 2104)",
     "befund": "Weißfinger-Anfälle auch außerhalb der Arbeit – fortgeschrittenes Stadium "
               "eines vibrationsbedingten vasospastischen Syndroms (VVS).",
     "konsequenz": "Vor weiterer Vibrationsexposition klären: Ergänzungsuntersuchung "
                   "Hand-Arm mit ausführlichem HAV-Fragebogen, Einstufung nach Stockholm "
                   "Scale, ggf. Kälteprovokationstest/Pallästhesiometrie. BK-2104-Verdacht "
                   "prüfen (ggf. BK-Anzeige); befristete oder dauernde gesundheitliche "
                   "Bedenken gegen die weitere Tätigkeit mit vibrierenden Geräten erwägen."},
    {"wenn": {"vorerkrankung_wirbelsaeule": ["yes"],
              "belastungen": ["heben_tragen", "ziehen_schieben", "rumpfbeuge", "kraft"]},
     "schwere": "kritisch",
     "bereich": "Wirbelsäule",
     "quelle": "G 46 2.1 / 3.2 »Erkrankungen der Wirbelsäule«",
     "befund": "Bekannte Wirbelsäulenerkrankung bei Tätigkeit mit Lastenhandhabung, "
               "Rumpfbeuge oder hoher Krafteinwirkung.",
     "konsequenz": "Ergänzungsuntersuchung der Wirbelsäule vor (weiterem) Einsatz; "
                   "Beurteilung nach 2.1 unter Berücksichtigung von Arbeitsplatz-"
                   "anforderungen, Behandlungs- und Kompensationsmöglichkeiten sowie "
                   "verbleibendem Berufsleben; ggf. keine Bedenken nur unter bestimmten "
                   "Voraussetzungen (2.1.3) oder befristete Bedenken (2.1.2)."},
    # ── pruefen: Ergänzungsuntersuchung / Abklärung ───────────────────────
    {"wenn": {"weissfinger": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hand-Arm-Vibrationen",
     "quelle": "G 46 Spezieller Teil 2.7 (BK 2104)",
     "befund": "Kälteinduziertes anfallsartiges Weißwerden/Absterben der Finger – "
               "Verdacht auf vibrationsbedingtes vasospastisches Syndrom (VVS).",
     "konsequenz": "Ergänzungsuntersuchung mit dem umfangreicheren HAV-Fragebogen "
                   "durchführen und die Angaben durch ärztliche Nachfragen validieren; "
                   "Stockholm Scale anwenden; Kälteprovokationstest mit Messung von "
                   "Hauttemperatur und Wiedererwärmungszeit sowie Pallästhesiometrie "
                   "erwägen; prüfen, ob die Symptomatik erst nach Beginn der "
                   "Vibrationstätigkeit auftrat."},
    {"wenn": {"gelenk_beschwerden_arm": ["yes"], "vib_hand_art": ["druckluft", "sonstige"]},
     "schwere": "pruefen",
     "bereich": "Hand-Arm-Vibrationen",
     "quelle": "G 46 Spezieller Teil 1.4 / 1.5 (BK 2103)",
     "befund": "Kraftlosigkeit, Anlauf- und Ruheschmerzen (nachts) der Arm-/Handgelenke "
               "bei Arbeit mit schlagenden Druckluft- oder gleichartigen Werkzeugen – "
               "Verdacht auf vibrationsbedingte Knochen- und Gelenkschäden.",
     "konsequenz": "Ergänzungsuntersuchung der oberen Extremitäten (Seitenvergleich "
                   "beachten); bei Verdacht spezielle Untersuchung über die kurative "
                   "Versorgung empfehlen (Röntgen-Spezialaufnahmen, Knochenszintigramm "
                   "oder MRT zur Früherkennung von Mond-/Kahnbeinschäden); BK 2103 "
                   "beachten."},
    {"wenn": {"taubheit_finger": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hand-Arm-Vibrationen / Nerven",
     "quelle": "G 46 Anhang 4 (Stockholm Scale, neurologische Beurteilung)",
     "befund": "Anfallsweise oder andauernde Taubheitsgefühle/Kribbeln der Finger – "
               "sensorineurale Störungen möglich.",
     "konsequenz": "Orientierende neurologische Untersuchung (z. B. Tinel-Zeichen, "
                   "Phalen-Test) und klinischen Gefäßstatus (z. B. Allen-Test) erheben; "
                   "Einstufung nach Stockholm Scale (sensorineurale Symptome); Abgrenzung "
                   "zu Karpaltunnelsyndrom und anderen Nervenkompressionssyndromen "
                   "(BK 2113) – ggf. fachneurologische Abklärung."},
    {"wenn": {"geschicklichkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hand-Arm-Vibrationen / Nerven",
     "quelle": "G 46 Anhang 4 (Stockholm Scale Stadium 3 SN)",
     "befund": "Vermindertes Tastgefühl bzw. verminderte Handgeschicklichkeit – "
               "fortgeschrittene sensorineurale Störung (Stockholm Scale Stadium 3 SN) "
               "möglich.",
     "konsequenz": "Ergänzungsuntersuchung Hand-Arm mit neurologischer Abklärung "
                   "veranlassen; Belastungsreduktion prüfen und Verlaufskontrolle in "
                   "verkürzter Frist vereinbaren."},
    {"wenn": {"beschwerden_12m": ["yes"], "arzt_wegen_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Muskel-Skelett-System",
     "quelle": "G 46 1.2.1 / 1.2.2",
     "befund": "Behandlungsbedürftige Beschwerden am Muskel-Skelett-System in den "
               "letzten 12 Monaten (Arztbesuch erfolgt).",
     "konsequenz": "Auffällige Anamnese: nach dem Ablaufschema der Basisuntersuchung "
                   "eine Ergänzungsuntersuchung durchführen (Funktionsdiagnostik bezogen "
                   "auf die betroffenen Körperregionen und die ausgeübte Tätigkeit, "
                   "erprobtes Verfahren nach Anhang 4)."},
    {"wenn": {"au_12m": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Muskel-Skelett-System",
     "quelle": "G 46 1.2.1 / Anhang 4 (Anamnese 1)",
     "befund": "Arbeitsunfähigkeit wegen Muskel-Skelett-Beschwerden in den letzten "
               "12 Monaten.",
     "konsequenz": "Häufigkeit und Gesamtdauer der Arbeitsunfähigkeit dokumentieren; "
                   "Ergänzungsuntersuchung durchführen; vorzeitige Nachuntersuchung mit "
                   "arztbestimmter kürzerer Frist erwägen (1.1)."},
    {"wenn": {"beschwerden_12m": ["yes"], "entlastung_besserung": ["no"]},
     "schwere": "pruefen",
     "bereich": "Chronifizierung",
     "quelle": "G 46 Anhang 4 (Anamnese 2)",
     "befund": "Keine Schmerzlinderung in belastungsarmen Zeiten (Nacht, Wochenende, "
               "Urlaub) – mit dem Eintritt einer belastungsunabhängigen "
               "Schmerzchronifizierung ist zu rechnen.",
     "konsequenz": "Eingehende Abklärung veranlassen; sekundärpräventive Maßnahmen "
                   "rechtzeitig einleiten, bevor die Belastbarkeit krankheitsbedingt "
                   "herabgesetzt ist (2.2.1)."},
    {"wenn": {"schmerz_dauer3m": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Chronische Schmerzen",
     "quelle": "G 46 2.2.1",
     "befund": "Starke Schmerzen seit mehr als 3 Monaten (Chronifizierung).",
     "konsequenz": "Vorstellung in einer Schmerzambulanz empfehlen; "
                   "differenzialdiagnostische Klärung der Befunde durch Orthopädie, "
                   "Neurologie o. a. veranlassen."},
    {"wenn": {"wiedereingliederung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Wiedereingliederung",
     "quelle": "G 46 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Rückkehr nach längerer Erkrankung oder Operation "
               "(Wiedereingliederung).",
     "konsequenz": "Untersuchung zur Beurteilung der individuellen Belastbarkeit "
                   "durchführen; Einsatzbedingungen und stufenweise Wiedereingliederung "
                   "(Arbeitsunfähigkeits-Richtlinie) mit Betrieb und behandelnden "
                   "Ärztinnen/Ärzten abstimmen."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zusammenhangsbeurteilung",
     "quelle": "G 46 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Die/der Beschäftigte vermutet einen ursächlichen Zusammenhang zwischen "
               "Erkrankung und Tätigkeit.",
     "konsequenz": "Vorzeitige (Nach-)Untersuchung ist begründet; Zusammenhang anhand "
                   "von Gefährdungsbeurteilung und Befunden bewerten; bei begründetem "
                   "BK-Verdacht Anzeige erstatten und Beratung zu Schutzmaßnahmen."},
    {"wenn": {"unfall_op": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Posttraumatische Zustände",
     "quelle": "G 46 3.2 / 2.1.2",
     "befund": "Folgen früherer Erkrankungen, Operationen oder schwerer Unfälle am "
               "Bewegungsapparat (z. B. befristete Zustände nach Fraktur oder Luxation).",
     "konsequenz": "Funktionelle Wiederherstellung in der Ergänzungsuntersuchung prüfen; "
                   "bis dahin ggf. befristete gesundheitliche Bedenken (2.1.2) und "
                   "Anpassung des Einsatzes; Verlaufskontrolle vereinbaren."},
    {"wenn": {"rheuma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Rheumatischer Formenkreis",
     "quelle": "G 46 3.2",
     "befund": "Erkrankung des rheumatischen Formenkreises bekannt.",
     "konsequenz": "Auswirkung auf die muskuloskelettale Belastbarkeit besonders "
                   "berücksichtigen; Behandlungsstatus klären und in die Beurteilung "
                   "nach 2.1 einbeziehen."},
    {"wenn": {"begleiterkrankungen": ["bluthochdruck", "herz", "arteriosklerose",
                                      "atemwege", "diabetes_insulin", "niere"]},
     "schwere": "pruefen",
     "bereich": "Begleiterkrankungen",
     "quelle": "G 46 3.2 (leistungsbegrenzende Erkrankungen)",
     "befund": "Leistungsbegrenzende Begleiterkrankung (Herz-Kreislauf, Atemwege, "
               "Stoffwechsel oder Niere).",
     "konsequenz": "Bei der Einschätzung von Belastbarkeit und Prognose beachten; "
                   "Ausmaß und Behandlungsstand klären (ggf. Befunde der behandelnden "
                   "Ärztinnen/Ärzte mit Einwilligung einholen) und mit den konkreten "
                   "Arbeitsanforderungen abgleichen."},
    # ── hinweis: Fristen & Beratung ───────────────────────────────────────
    {"wenn": {"alter_ab40": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "G 46 1.1",
     "befund": "Alter 40 Jahre oder älter.",
     "konsequenz": "Nachuntersuchungsfrist von 36 Monaten (statt 60 Monaten) beachten "
                   "und den nächsten Termin entsprechend planen."},
    {"wenn": {"letzte_untersuchung": ["ueber5jahre"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "G 46 1.1",
     "befund": "Letzte G-46-Untersuchung vor mehr als 5 Jahren – die Regelfrist von "
               "60 Monaten ist überschritten.",
     "konsequenz": "Untersuchung zeitnah vollständig durchführen und künftig die "
                   "reguläre Frist (60 Monate, ab 40 Jahren 36 Monate) einhalten."},
    {"wenn": {"alter_ab40": ["yes"], "letzte_untersuchung": ["3bis5jahre"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "G 46 1.1",
     "befund": "Ab 40 Jahren gilt die 36-Monats-Frist – die letzte Untersuchung liegt "
               "bereits mehr als 3 Jahre zurück.",
     "konsequenz": "Nachuntersuchung jetzt durchführen und den nächsten Termin nach "
                   "36 Monaten einplanen."},
    {"wenn": {"kaelte_arbeit": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kälteschutz",
     "quelle": "G 46 Spezieller Teil 2.6",
     "befund": "Arbeit mit vibrierenden Geräten in kalter Umgebung.",
     "konsequenz": "Unterweisung/Beratung zu Kälteschutz: zweckmäßige warme Bekleidung, "
                   "spezielle Handschuhe, Warmhalten der Hände, heiße Getränke; "
                   "Griffheizungen (z. B. bei Motorkettensägen) empfehlen."},
    {"wenn": {"raucher": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Nikotin",
     "quelle": "G 46 Spezieller Teil 2.4 / 2.6",
     "befund": "Rauchen bei Tätigkeit mit Hand-Arm-Vibrationen.",
     "konsequenz": "Zur Nikotinabstinenz beraten – Nikotin begünstigt vasospastische "
                   "Anfälle und Durchblutungsstörungen der Finger."},
    {"wenn": {"medikamente_gefaess": ["yes"], "weissfinger": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Differenzialdiagnose",
     "quelle": "G 46 Spezieller Teil 2.4",
     "befund": "Einnahme gefäßwirksamer Medikamente (z. B. Ergotamin, Betablocker) bei "
               "Weißfinger-Symptomatik.",
     "konsequenz": "Differenzialdiagnostisch medikamentös bedingte Vasospasmen und "
                   "andere Ursachen (M. Raynaud, systemische Erkrankungen, chemische "
                   "Expositionen) abgrenzen, bevor ein VVS angenommen wird."},
]
