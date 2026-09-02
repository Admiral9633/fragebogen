# -*- coding: utf-8 -*-
"""Arbeitsaufenthalt im Ausland – DGUV Empfehlung 2024 (E AIA).

Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und
Untersuchungen, 1. Auflage 2024, "Arbeitsaufenthalt im Ausland unter
besonderen klimatischen oder gesundheitlichen Belastungen" (Kurzbezeichnung
E AIA, Fassung Januar 2022), S. 975–996.
"""

SLUG = "ausland-2024"

CATALOG = {
    "version": 2,
    "title": "Arbeitsaufenthalt im Ausland (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, E AIA „Arbeitsaufenthalt im Ausland unter besonderen "
             "klimatischen oder gesundheitlichen Belastungen“ (Fassung Januar 2022), S. 975–996",
    "sections": [
        # ── 1 ──────────────────────────────────────────────────────────────
        {
            "id": "einsatz",
            "title": "Tätigkeit & Auslandseinsatz",
            "subtitle": "Angaben zu Ihrem Arbeitsaufenthalt im Ausland",
            "questions": [
                {
                    "id": "anlass",
                    "type": "choice",
                    "label": "Zu welchem Zeitpunkt findet diese Vorsorge statt?",
                    "hint": "Vor der Ausreise ist die Vorsorge Pflicht (Pflichtvorsorge). "
                            "Nach der Rückkehr bzw. am Ende der Auslandstätigkeit wird sie "
                            "Ihnen angeboten (Angebotsvorsorge).",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge vor der Ausreise"},
                        {"value": "weitere", "label": "Weitere Vorsorge während der laufenden Auslandstätigkeit"},
                        {"value": "rueckkehr", "label": "Vorsorge nach Rückkehr bzw. am Ende der Auslandstätigkeit"},
                    ],
                },
                {
                    "id": "zielregion",
                    "type": "multi_choice",
                    "label": "In welche Region(en) führt bzw. führte Ihr Arbeitsaufenthalt?",
                    "hint": "Mehrfachauswahl möglich. Tropen = Gürtel beiderseits des Äquators, "
                            "Subtropen = angrenzende warme Länder, Polarregionen = Gebiete "
                            "jenseits der Polarkreise.",
                    "required": True,
                    "options": [
                        {"value": "tropen", "label": "Tropen (z.B. Zentralafrika, Südostasien, Amazonasgebiet)"},
                        {"value": "subtropen", "label": "Subtropen (z.B. Nordafrika, Naher Osten, Südchina)"},
                        {"value": "polar", "label": "Polarregionen (Arktis/Antarktis)"},
                        {"value": "sonstige", "label": "Sonstige Länder mit besonderen Belastungen "
                                                       "(z.B. starke Luftverschmutzung, schlechte Trinkwasserversorgung)"},
                    ],
                },
                {
                    "id": "einsatzdauer",
                    "type": "choice",
                    "label": "Wie lange dauert Ihr Auslandseinsatz insgesamt (geplant oder tatsächlich)?",
                    "required": True,
                    "options": [
                        {"value": "unter3m", "label": "Bis 3 Monate"},
                        {"value": "m3bis12", "label": "3 bis 12 Monate"},
                        {"value": "ueber12m", "label": "Länger als 12 Monate"},
                        {"value": "wechselnd", "label": "Wiederholte Kurzeinsätze / ständig wechselnde Einsatzorte"},
                    ],
                },
                {
                    "id": "taetigkeit_art",
                    "type": "textarea",
                    "label": "Welche Tätigkeit üben Sie im Ausland aus (Beruf, Arbeitsumgebung, "
                             "z.B. Baustelle, Büro, Gesundheitsdienst, ländliche Region)?",
                    "required": False,
                },
                {
                    "id": "medizinische_versorgung",
                    "type": "choice",
                    "label": "Wie schätzen Sie die medizinische Versorgung an Ihrem Einsatzort ein?",
                    "hint": "Gemeint sind Erreichbarkeit von Ärztinnen/Ärzten und Krankenhäusern "
                            "sowie die Verfügbarkeit von Medikamenten und Notfallversorgung.",
                    "required": True,
                    "options": [
                        {"value": "gut", "label": "Gut – Ärzte, Krankenhaus und Medikamente sind verfügbar"},
                        {"value": "eingeschraenkt", "label": "Eingeschränkt – lange Wege oder lückenhafte Versorgung"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "hoehenlage",
                    "type": "yes_no",
                    "label": "Halten Sie sich im Rahmen der Tätigkeit in großer Höhe auf "
                             "(über etwa 2.500 m)?",
                    "required": True,
                },
                {
                    "id": "rueckkehr_zeitpunkt",
                    "type": "choice",
                    "label": "Wann sind Sie aus dem Ausland zurückgekehrt?",
                    "hint": "Die Untersuchung nach Rückkehr soll frühestens 6 Wochen und "
                            "spätestens 3 Monate nach der Rückkehr stattfinden.",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["rueckkehr"]},
                    "options": [
                        {"value": "w6bis3m", "label": "Vor 6 Wochen bis 3 Monaten"},
                        {"value": "unter6w", "label": "Vor weniger als 6 Wochen"},
                        {"value": "ueber3m", "label": "Vor mehr als 3 Monaten"},
                    ],
                },
            ],
        },
        # ── 2 ──────────────────────────────────────────────────────────────
        {
            "id": "impfung",
            "title": "Impfschutz & Vorbeugung",
            "subtitle": "Impfungen und Malaria-Vorbeugung",
            "questions": [
                {
                    "id": "impfstatus",
                    "type": "choice",
                    "label": "Ist Ihr Impfschutz nach Ihrem Kenntnisstand vollständig "
                             "(Standardimpfungen und Reiseimpfungen für Ihr Zielland)?",
                    "hint": "Bitte bringen Sie Ihren Impfausweis zur Untersuchung mit.",
                    "required": True,
                    "options": [
                        {"value": "vollstaendig", "label": "Ja, vollständig"},
                        {"value": "unvollstaendig", "label": "Nein, es fehlen Impfungen"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "malaria_prophylaxe",
                    "type": "choice",
                    "label": "Haben Sie die für Ihr Einsatzgebiet empfohlene Malaria-Vorbeugung "
                             "durchgeführt (Tabletten zur Chemoprophylaxe und Mückenschutz)?",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                    "options": [
                        {"value": "regelmaessig", "label": "Ja, regelmäßig wie empfohlen"},
                        {"value": "unregelmaessig", "label": "Ja, aber unregelmäßig oder vorzeitig beendet"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "nicht_erforderlich", "label": "Für mein Einsatzgebiet nicht empfohlen"},
                    ],
                },
            ],
        },
        # ── 3 ──────────────────────────────────────────────────────────────
        {
            "id": "aufenthalt",
            "title": "Ereignisse während des Auslandsaufenthalts",
            "subtitle": "Erkrankungen und mögliche Ansteckungsquellen im Ausland",
            "questions": [
                {
                    "id": "erkrankungen_ausland",
                    "type": "yes_no",
                    "label": "Waren Sie während des Auslandsaufenthalts krank oder hatten Sie "
                             "einen Unfall?",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                    "followup": {
                        "id": "erkrankungen_ausland_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung/welcher Unfall, wann, und wie wurden Sie "
                                 "behandelt? Falls vorhanden: Unterlagen (z.B. „Medical Report“) bitte mitbringen.",
                        "when": "yes",
                    },
                },
                {
                    "id": "infekt_material",
                    "type": "yes_no",
                    "label": "Hatten Sie im Ausland Kontakt mit möglicherweise ansteckenden "
                             "Materialien oder riskanten Lebensmitteln?",
                    "hint": "z.B. Blut, Rohmilchprodukte, ungewaschene Salate, nicht "
                            "durchgegarter Fisch oder nicht durchgegartes Fleisch.",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                },
                {
                    "id": "medizinische_eingriffe",
                    "type": "yes_no",
                    "label": "Hatten Sie im Ausland Operationen, Spritzen, Zahnbehandlungen, "
                             "Tätowierungen oder Piercings?",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                },
                {
                    "id": "sexualkontakte",
                    "type": "yes_no",
                    "label": "Hatten Sie während des Auslandsaufenthalts neue Sexualkontakte?",
                    "hint": "Diese Angabe hilft, Ihnen gezielt Untersuchungen (z.B. auf HIV "
                            "oder Hepatitis) anzubieten. Sie wird vertraulich behandelt.",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                },
                {
                    "id": "suesswasser",
                    "type": "yes_no",
                    "label": "Hatten Sie Kontakt mit Süßwasser in Seen, Flüssen oder Bewässerungskanälen "
                             "(Baden, Waten, Arbeiten im Wasser)?",
                    "hint": "Über Süßwasserkontakt kann die Wurmerkrankung Bilharziose "
                            "(Schistosomiasis) übertragen werden.",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                },
                {
                    "id": "tierkontakt",
                    "type": "yes_no",
                    "label": "Wurden Sie im Ausland von einem Tier gebissen oder gekratzt, oder "
                             "hatten Sie engen Kontakt zu Tieren?",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                    "followup": {
                        "id": "tierkontakt_desc",
                        "type": "text",
                        "label": "Welches Tier, wann, und wurde die Wunde ärztlich versorgt "
                                 "(z.B. Tollwut-Impfung)?",
                        "when": "yes",
                    },
                },
            ],
        },
        # ── 4 ──────────────────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, die auf eine Erkrankung hinweisen können",
            "questions": [
                {
                    "id": "symptom_fieber",
                    "type": "yes_no",
                    "label": "Hatten Sie während des Auslandsaufenthalts oder danach Fieber "
                             "oder Fieberschübe?",
                    "hint": "Fieber nach Tropenaufenthalt muss immer rasch abgeklärt werden "
                            "(u.a. Ausschluss einer Malaria).",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                    "followup": {
                        "id": "symptom_fieber_desc",
                        "type": "text",
                        "label": "Wann traten die Fieberepisoden auf, und wurden sie bereits untersucht?",
                        "when": "yes",
                    },
                },
                {
                    "id": "symptom_durchfall",
                    "type": "yes_no",
                    "label": "Haben Sie anhaltenden oder immer wiederkehrenden Durchfall?",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                },
                {
                    "id": "symptom_haut",
                    "type": "yes_no",
                    "label": "Haben Sie neue Hautveränderungen bemerkt (z.B. juckende Quaddeln, "
                             "schlecht heilende Wunden oder Geschwüre, auffällige Sonnenschäden)?",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                },
                {
                    "id": "symptom_allgemein",
                    "type": "yes_no",
                    "label": "Haben Sie ungewollt stark an Gewicht verloren, geschwollene "
                             "Lymphknoten bemerkt oder länger anhaltenden Husten?",
                    "required": True,
                    "show_if": {"id": "anlass", "in": ["weitere", "rueckkehr"]},
                },
                {
                    "id": "psychische_belastung",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich seelisch stark belastet (z.B. Schlafstörungen, "
                             "gedrückte Stimmung, ständige Anspannung, Sorge um die eigene Sicherheit)?",
                    "hint": "Der Wechsel in ein fremdes Umfeld (Klima, Sprache, Kultur, "
                            "Sicherheitslage) kann psychisch belasten.",
                    "required": True,
                },
                {
                    "id": "aktuelle_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie derzeit sonstige Beschwerden?",
                    "required": True,
                    "followup": {
                        "id": "aktuelle_beschwerden_desc",
                        "type": "textarea",
                        "label": "Welche Beschwerden haben Sie, und seit wann?",
                        "when": "yes",
                    },
                },
            ],
        },
        # ── 5 ──────────────────────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Medikamente",
            "subtitle": "Erkrankungen und Behandlungen, die für den Auslandseinsatz wichtig sind",
            "questions": [
                {
                    "id": "herzkreislauf",
                    "type": "yes_no",
                    "label": "Haben Sie eine Herz-Kreislauf-Erkrankung (z.B. koronare Herzkrankheit, "
                             "Herzschwäche/Herzinsuffizienz, behandlungsbedürftiger Bluthochdruck)?",
                    "required": True,
                    "followup": {
                        "id": "herzkreislauf_desc",
                        "type": "text",
                        "label": "Welche Erkrankung, und wie wird sie behandelt?",
                        "when": "yes",
                    },
                },
                {
                    "id": "diabetes",
                    "type": "choice",
                    "label": "Haben Sie eine Zuckerkrankheit (Diabetes mellitus)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ohne_insulin", "label": "Ja, ohne Insulin behandelt (Tabletten/Ernährung)"},
                        {"value": "insulin", "label": "Ja, mit Insulin behandelt (auch Insulinpumpe)"},
                    ],
                },
                {
                    "id": "autoimmun",
                    "type": "yes_no",
                    "label": "Haben Sie eine Autoimmunerkrankung (z.B. rheumatoide Arthritis, "
                             "chronisch-entzündliche Darmerkrankung)?",
                    "required": True,
                    "followup": {
                        "id": "autoimmun_desc",
                        "type": "text",
                        "label": "Welche Erkrankung, und welche Medikamente nehmen Sie dafür?",
                        "when": "yes",
                    },
                },
                {
                    "id": "chronisch_sonstige",
                    "type": "yes_no",
                    "label": "Haben Sie andere chronische Erkrankungen (z.B. schweres Asthma, "
                             "Nieren-, Leber- oder psychische Erkrankungen)?",
                    "required": True,
                    "followup": {
                        "id": "chronisch_sonstige_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankungen sind das?",
                        "when": "yes",
                    },
                },
                {
                    "id": "staendige_betreuung",
                    "type": "yes_no",
                    "label": "Benötigen Sie wegen einer Erkrankung ständige ärztliche Betreuung "
                             "oder regelmäßige Kontrolluntersuchungen?",
                    "required": True,
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "hint": "Wichtig ist auch, ob Sie Ihre Medikamente im Ausland zuverlässig "
                            "beschaffen und lagern können (z.B. Insulin mit Kühlung, Insulinpumpe).",
                    "required": True,
                    "followup": {
                        "id": "medikamente_desc",
                        "type": "textarea",
                        "label": "Welche Medikamente, und ist die Versorgung am Einsatzort gesichert?",
                        "when": "yes",
                    },
                },
                {
                    "id": "immunsuppression",
                    "type": "yes_no",
                    "label": "Nehmen Sie Medikamente ein, die die Abwehrkräfte schwächen "
                             "(Immunsuppressiva, z.B. Kortison über längere Zeit, Biologika, "
                             "Medikamente nach Transplantation)?",
                    "required": True,
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Besteht bei Ihnen derzeit eine Schwangerschaft?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ja", "label": "Ja"},
                        {"value": "unsicher", "label": "Bin mir nicht sicher"},
                        {"value": "entfaellt", "label": "Entfällt"},
                    ],
                },
                {
                    "id": "sucht",
                    "type": "yes_no",
                    "label": "Gab oder gibt es bei Ihnen eine Suchterkrankung oder einen "
                             "problematischen Konsum von Alkohol, Tabak oder anderen Substanzen?",
                    "required": True,
                },
                {
                    "id": "behinderung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Behinderung oder eine dauerhafte körperliche "
                             "Einschränkung?",
                    "required": True,
                    "followup": {
                        "id": "behinderung_desc",
                        "type": "text",
                        "label": "Welche Einschränkung ist das?",
                        "when": "yes",
                    },
                },
            ],
        },
        # ── 6 ──────────────────────────────────────────────────────────────
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
    # ── Fristen ─────────────────────────────────────────────────────────────
    {"wenn": {"rueckkehr_zeitpunkt": ["unter6w", "ueber3m"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "E AIA Abschnitt 7.3 (Fristen)",
     "befund": "Rückkehruntersuchung außerhalb des empfohlenen Zeitfensters "
               "(frühestens 6 Wochen, spätestens 3 Monate nach Rückkehr)",
     "konsequenz": "Untersuchungszeitpunkt bewerten: Vor Ablauf von 6 Wochen können "
                   "serologische Befunde noch unauffällig sein – Kontrolle nach Fristablauf "
                   "einplanen; bei mehr als 3 Monaten gezielt nach Spätmanifestationen "
                   "(z.B. Malaria, Schistosomiasis, Tuberkulose) suchen."},
    # ── Impfschutz / Prophylaxe ─────────────────────────────────────────────
    {"wenn": {"impfstatus": ["unvollstaendig", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Impfschutz",
     "quelle": "E AIA Abschnitt 7.4 (unvollständiger Impfschutz), AMR 6.6",
     "befund": "Unvollständiger oder unbekannter Impfschutz",
     "konsequenz": "Impfstatus anhand des Impfausweises klären; fehlende Impfungen gemäß "
                   "AMR 6.6 mit ausreichendem zeitlichem Vorlauf vor der Ausreise "
                   "vervollständigen; Impfplan dokumentieren."},
    {"wenn": {"malaria_prophylaxe": ["unregelmaessig", "nein"]},
     "schwere": "pruefen",
     "bereich": "Malariaprophylaxe",
     "quelle": "E AIA Abschnitt 7.1/8.1, AMR 6.6",
     "befund": "Empfohlene Malariaprophylaxe nicht oder nur unregelmäßig durchgeführt",
     "konsequenz": "Beratung zu Chemoprophylaxe und Expositionsschutz (Repellentien, "
                   "imprägniertes Moskitonetz) wiederholen; bei jedem unklaren Fieber "
                   "unverzüglich Malariadiagnostik veranlassen."},
    # ── Symptome nach Aufenthalt ────────────────────────────────────────────
    {"wenn": {"symptom_fieber": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Infektionszeichen",
     "quelle": "E AIA Abschnitt 6.4 und 7.2.2",
     "befund": "Fieber während oder nach dem Auslandsaufenthalt",
     "konsequenz": "Unverzügliche Abklärung mit Malaria-Ausschlussdiagnostik; "
                   "Dengue-Serologie bei zurückliegenden typischen Symptomen im "
                   "Endemiegebiet; unmittelbare Einbindung der Tropenmedizin empfohlen. "
                   "Klärung vor Fortsetzung bzw. erneutem Einsatz."},
    {"wenn": {"symptom_durchfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm",
     "quelle": "E AIA Abschnitt 7.2.2",
     "befund": "Anhaltende oder rezidivierende Durchfälle nach Auslandsaufenthalt",
     "konsequenz": "Stuhluntersuchung auf Parasiten einschließlich Amöben und Lamblien "
                   "veranlassen (drei Stuhlproben); bei fehlender Klärung tropenmedizinische "
                   "Vorstellung."},
    {"wenn": {"symptom_haut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "E AIA Abschnitt 6 und 6.5 (BK-Nr. 5103)",
     "befund": "Neue Hautveränderungen nach Auslandsaufenthalt",
     "konsequenz": "Dermatologische bzw. tropenmedizinische Abklärung veranlassen; bei "
                   "auffälligen Sonnenschäden an UV-bedingte Hautveränderungen denken "
                   "(BK-Nr. 5103) und UV-Schutzberatung durchführen."},
    {"wenn": {"symptom_allgemein": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allgemeinsymptome",
     "quelle": "E AIA Abschnitt 6.4 und 7.2.2",
     "befund": "Gewichtsverlust, Lymphknotenschwellungen oder anhaltender Husten",
     "konsequenz": "Tuberkulosescreening (z.B. IGRA) und erweiterte Diagnostik veranlassen; "
                   "unmittelbare Einbindung anderer Fachdisziplinen (Tropenmedizin) "
                   "empfohlen."},
    # ── Expositionen ────────────────────────────────────────────────────────
    {"wenn": {"suesswasser": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Süßwasserexposition",
     "quelle": "E AIA Abschnitt 7.2.2",
     "befund": "Süßwasserkontakt im möglichen Endemiegebiet",
     "konsequenz": "Schistosomen-Antikörper bestimmen (bei möglicher Exposition bzw. "
                   "Langzeitaufenthalt im Endemiegebiet); Beratung zur Vermeidung von "
                   "Süßwasserkontakt."},
    {"wenn": {"sexualkontakte": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sexualanamnese",
     "quelle": "E AIA Abschnitt 7.1 und 7.2.2",
     "befund": "Neue Sexualkontakte während des Auslandsaufenthalts",
     "konsequenz": "HIV-Test und Hepatitis-Serologie (A, B, C) als Ergänzungsuntersuchung "
                   "anbieten; Beratung zu Schutzmaßnahmen und ggf. Verlaufskontrolle "
                   "(diagnostisches Fenster) einplanen."},
    {"wenn": {"medizinische_eingriffe": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Blutübertragbare Infektionen",
     "quelle": "E AIA Abschnitt 7.1 und 7.2.2",
     "befund": "Operation, Injektion, Zahnbehandlung, Tätowierung oder Piercing im Ausland",
     "konsequenz": "Hepatitis-Serologie und HIV-Test als Ergänzungsuntersuchung anbieten "
                   "(mögliche Übertragung über Blut/Instrumente)."},
    {"wenn": {"infekt_material": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Lebensmittel-/Materialkontakt",
     "quelle": "E AIA Abschnitt 7.1 und 8.1",
     "befund": "Kontakt mit infektiösen Materialien oder riskanten Lebensmitteln",
     "konsequenz": "Gezielte Diagnostik erwägen (z.B. Stuhluntersuchung, Serologie je nach "
                   "Exposition); Beratung zu Lebensmittel- und Trinkwasserhygiene."},
    {"wenn": {"tierkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Tierkontakt",
     "quelle": "E AIA Abschnitt 7.1 und 6.5 (BK-Nr. 3102)",
     "befund": "Tierbiss/-kratzer oder enger Tierkontakt im Ausland",
     "konsequenz": "Tollwutexposition und Impf-/Postexpositionsstatus klären; ggf. "
                   "tropenmedizinische Abklärung auf von Tieren übertragbare Erkrankungen "
                   "(Zoonosen, BK-Nr. 3102)."},
    {"wenn": {"erkrankungen_ausland": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Erkrankung im Ausland",
     "quelle": "E AIA Abschnitt 7.1, 8.2 und 6.5",
     "befund": "Erkrankung oder Unfall während des Auslandsaufenthalts",
     "konsequenz": "Behandlungsunterlagen (mehrsprachiges Formblatt „Medical Report“) "
                   "anfordern und auswerten; Zusammenhang mit der Tätigkeit prüfen und ggf. "
                   "BK-Anzeige erwägen (BK-Nrn. 3101, 3102, 3104)."},
    # ── Vorerkrankungen / Beurteilung ───────────────────────────────────────
    {"wenn": {"staendige_betreuung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Behandlungsbedürftige Grunderkrankung",
     "quelle": "E AIA Abschnitt 7.4.4",
     "befund": "Ständige ärztliche Betreuung erforderlich",
     "konsequenz": "Vor dem Einsatz klären, ob die Betreuung am Einsatzort gesichert ist; "
                   "ist dies nicht der Fall oder ist mit Verschlimmerung bzw. nicht "
                   "behandelbaren Komplikationen zu rechnen, Tätigkeitswechsel empfehlen. "
                   "Mitteilung an den Arbeitgeber nur mit Einwilligung der versicherten "
                   "Person (§ 6 (4) ArbMedVV)."},
    {"wenn": {"diabetes": ["insulin"]},
     "schwere": "pruefen",
     "bereich": "Diabetes mellitus",
     "quelle": "E AIA Abschnitt 7.4, 7.4.2 und 7.4.3",
     "befund": "Insulinpflichtiger Diabetes mellitus",
     "konsequenz": "Prüfen, ob ärztliche Betreuung und Medikamentenversorgung (Insulin, "
                   "Kühlkette, Pumpenzubehör) am Aufenthaltsort gesichert sind; verkürzte "
                   "Vorsorgefristen empfehlen, wenn eine Änderung des Schweregrades zu "
                   "erwarten ist."},
    {"wenn": {"diabetes": ["insulin"], "medizinische_versorgung": ["eingeschraenkt", "unbekannt"]},
     "schwere": "kritisch",
     "bereich": "Diabetes mellitus",
     "quelle": "E AIA Abschnitt 7.4.4",
     "befund": "Insulinpflichtiger Diabetes bei eingeschränkter oder unklarer medizinischer "
               "Versorgung am Einsatzort",
     "konsequenz": "Versorgungslage VOR dem Einsatz verbindlich klären; kann die Behandlung "
                   "typischer Komplikationen am Einsatzort nicht sichergestellt werden, "
                   "Tätigkeitswechsel empfehlen (Einwilligung nach § 6 (4) ArbMedVV "
                   "beachten)."},
    {"wenn": {"herzkreislauf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "E AIA Abschnitt 7.4 und 7.2.2",
     "befund": "Koronare/hypertensive Herzkrankheit bzw. Herzinsuffizienz angegeben",
     "konsequenz": "Kardiale Belastbarkeit prüfen (Ruhe-EKG, ergänzend Ergometrie); "
                   "Behandlungs- und Notfallversorgung am Einsatzort bewerten; bei zu "
                   "erwartender Änderung des Schweregrades verkürzte Fristen (7.4.3)."},
    {"wenn": {"autoimmun": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Autoimmunerkrankung",
     "quelle": "E AIA Abschnitt 7.4 und 7.4.2",
     "befund": "Autoimmunerkrankung (z.B. rheumatoide Arthritis) angegeben",
     "konsequenz": "Krankheitsaktivität und Therapie klären; Beschaffung und Lagerung der "
                   "Medikamente (z.B. Immunsuppressiva) am Einsatzort sicherstellen; "
                   "Aufnahme/Fortsetzung nur bei gesicherter Betreuung und Versorgung "
                   "(7.4.2)."},
    {"wenn": {"immunsuppression": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Immunsuppression",
     "quelle": "E AIA Abschnitt 7.2.2",
     "befund": "Einnahme immunsupprimierender Medikamente",
     "konsequenz": "Strongyloides-Antikörper bestimmen (Ergänzungsuntersuchung im "
                   "Zusammenhang mit Immunsuppression); Impffähigkeit prüfen "
                   "(Lebendimpfstoffe ggf. kontraindiziert); tropenmedizinische "
                   "Mitbeurteilung erwägen."},
    {"wenn": {"schwangerschaft": ["ja", "unsicher"]},
     "schwere": "pruefen",
     "bereich": "Schwangerschaft",
     "quelle": "E AIA Abschnitt 7.4",
     "befund": "Bestehende oder mögliche Schwangerschaft",
     "konsequenz": "Körperliche Anpassungsfähigkeit an Klima/Höhe bewerten; "
                   "Malariaprophylaxe und Impfungen (insbesondere Lebendimpfstoffe) auf "
                   "Vereinbarkeit mit der Schwangerschaft prüfen; Einsatzplanung und "
                   "medizinische Versorgung am Einsatzort vor der Ausreise klären."},
]
