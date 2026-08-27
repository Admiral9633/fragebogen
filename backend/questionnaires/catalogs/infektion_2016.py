# -*- coding: utf-8 -*-
"""G 42 Tätigkeiten mit Infektionsgefährdung – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 7. Auflage 2016
(Gentner Verlag), G 42 »Tätigkeiten mit Infektionsgefährdung«
(Fassung Oktober 2014), Elementarteil S. 635–644 (Spezieller Teil S. 645–844).

Anamnese-Fragen, die die zu untersuchende Person selbst beantworten kann
(Untersuchungsanlass/Fristen, Tätigkeit/Exposition, Beschwerden,
Vorerkrankungen mit Bezug zur Immunabwehr, Impfanamnese), plus
datengetriebene Auswertungsregeln nach Abschnitt 1 (Untersuchungsarten,
Fristen, Untersuchungsprogramm) und Abschnitt 2 (Beurteilungskriterien
2.1.1–2.1.4, Beratung 2.2). Keine Messwerte oder ärztlichen Befunde.
"""

SLUG = "g42-infektion-2016"

CATALOG = {
    "version": 2,
    "title": "G 42 Tätigkeiten mit Infektionsgefährdung (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 7. Auflage 2016, "
             "G 42 »Tätigkeiten mit Infektionsgefährdung« (Fassung Oktober 2014), "
             "Elementarteil S. 635–644",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Untersuchungsanlass",
            "subtitle": "Angaben zu Ihrer G-42-Untersuchung",
            "questions": [
                {
                    "id": "untersuchungsart",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich?",
                    "required": True,
                    "hint": "Steht meist auf der Einladung Ihres Arbeitgebers. "
                            "Wenn Sie es nicht wissen, wählen Sie »Weiß ich nicht«.",
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Regelmäßige Nachuntersuchung"},
                        {"value": "vorzeitig", "label": "Vorzeitige Nachuntersuchung (besonderer Anlass, z.B. nach Erkrankung oder Verletzung)"},
                        {"value": "ende", "label": "Untersuchung wegen Beendigung der Tätigkeit"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "letzte_g42",
                    "type": "choice",
                    "label": "Wie lange liegt Ihre letzte G-42-Untersuchung zurück?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "not_in": ["erst"]},
                    "options": [
                        {"value": "unter12", "label": "Weniger als 12 Monate"},
                        {"value": "12bis36", "label": "12 bis 36 Monate"},
                        {"value": "ueber36", "label": "Mehr als 36 Monate"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit & Exposition ─────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Erregerkontakt",
            "subtitle": "Wo und wie Sie mit Krankheitserregern in Kontakt kommen können",
            "questions": [
                {
                    "id": "bereich",
                    "type": "choice",
                    "label": "In welchem Bereich arbeiten Sie?",
                    "required": True,
                    "options": [
                        {"value": "gesundheit", "label": "Medizinische Untersuchung, Behandlung oder Pflege (z.B. Klinik, Praxis, Pflege)"},
                        {"value": "betreuung", "label": "Betreuung von Menschen (z.B. Heim, Wohlfahrtspflege, Behindertenhilfe)"},
                        {"value": "kita", "label": "Vorschulische Kinderbetreuung (z.B. Kita, Krippe, Kindergarten)"},
                        {"value": "labor", "label": "Labor oder Forschungseinrichtung"},
                        {"value": "rettung", "label": "Notfall- oder Rettungsdienst"},
                        {"value": "pathologie", "label": "Pathologie"},
                        {"value": "abwasser", "label": "Kläranlage oder Kanalisation (Abwasser)"},
                        {"value": "tiere", "label": "Arbeit mit Tieren (z.B. Geflügelhaltung, Schlachtung, Tiermedizin)"},
                        {"value": "natur", "label": "Arbeit im Freien (z.B. Wald, Park, Gartenanlagen, Zoo)"},
                        {"value": "andere", "label": "Anderer Bereich"},
                    ],
                    "followup": {"id": "bereich_sonst", "type": "text",
                                 "label": "In welchem Bereich arbeiten Sie?",
                                 "when": "andere", "required": False},
                },
                {
                    "id": "taetigkeit_konkret",
                    "type": "text",
                    "label": "Was ist Ihre konkrete Tätigkeit?",
                    "hint": "Zum Beispiel: Pflegefachkraft auf einer Infektionsstation, "
                            "MTA im Bakteriologie-Labor, Kanalarbeiter.",
                    "required": True,
                },
                {
                    "id": "erregerkontakt",
                    "type": "multi_choice",
                    "label": "Welche der folgenden Situationen kommen bei Ihrer Arbeit "
                             "regelmäßig vor? (Mehrfachauswahl möglich)",
                    "hint": "Krankheitserreger können durch Kontakt-, Tröpfchen- oder "
                            "Schmierinfektion übertragen werden.",
                    "required": True,
                    "options": [
                        {"value": "koerperfluessigkeiten", "label": "Kontakt mit Blut, Körperflüssigkeiten, Ausscheidungen oder Gewebe"},
                        {"value": "stichgefahr", "label": "Erhöhte Gefahr von Stich- oder Schnittverletzungen (z.B. Nadeln, Skalpelle)"},
                        {"value": "aerosol", "label": "Verspritzen von Flüssigkeiten oder Einatmen von Bioaerosolen (feinen Schwebeteilchen)"},
                        {"value": "direktkontakt", "label": "Direkter Kontakt zu erkrankten oder krankheitsverdächtigen Menschen"},
                        {"value": "tierkontakt", "label": "Kontakt zu Tieren, Tierprodukten oder tierischen Proben"},
                        {"value": "pneumokokken", "label": "Gezielter Umgang mit Pneumokokken (Streptococcus pneumoniae) im Labor"},
                        {"value": "keine", "label": "Nichts davon"},
                    ],
                },
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Steht Ihnen die nötige persönliche Schutzausrüstung (z.B. Handschuhe, "
                             "Mundschutz, Schutzbrille, Schürze) zur Verfügung, und nutzen Sie sie?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, vorhanden und ich nutze sie regelmäßig"},
                        {"value": "teilweise", "label": "Teilweise (nicht immer vorhanden oder nicht immer genutzt)"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "nicht_noetig", "label": "Für meine Tätigkeit nicht erforderlich"},
                    ],
                },
                {
                    "id": "unfall_verletzung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung (bzw. in den letzten "
                             "12 Monaten) eine Verletzung, bei der Krankheitserreger in den "
                             "Körper eindringen konnten (z.B. Nadelstich, Schnitt, Biss, "
                             "Blutspritzer auf verletzte Haut)?",
                    "required": True,
                    "followup": {"id": "unfall_verletzung_desc", "type": "textarea",
                                 "label": "Was ist passiert? Wurde der Vorfall gemeldet "
                                          "und ärztlich versorgt?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Wie es Ihnen zurzeit gesundheitlich geht",
            "questions": [
                {
                    "id": "beschwerden_any",
                    "type": "yes_no",
                    "label": "Haben Sie zurzeit oder hatten Sie in den letzten Monaten "
                             "gesundheitliche Beschwerden?",
                    "hint": "Zum Beispiel: häufige Infekte, anhaltender Husten, Fieber, "
                            "Nachtschweiß, starke Müdigkeit. Wenn nein, verkürzt sich "
                            "der Fragebogen.",
                    "required": True,
                },
                {
                    "id": "infekt_haeufig",
                    "type": "yes_no",
                    "label": "Sind Sie häufiger erkältet oder öfter von Infekten betroffen "
                             "als andere Menschen in Ihrem Umfeld?",
                    "required": True,
                    "show_if": {"id": "beschwerden_any", "in": ["yes"]},
                },
                {
                    "id": "fieber_nachtschweiss",
                    "type": "yes_no",
                    "label": "Haben Sie wiederkehrendes Fieber oder starken Nachtschweiß "
                             "(so dass Sie Wäsche oder Bettzeug wechseln müssen)?",
                    "required": True,
                    "show_if": {"id": "beschwerden_any", "in": ["yes"]},
                },
                {
                    "id": "husten",
                    "type": "yes_no",
                    "label": "Haben Sie seit mehr als 3 Wochen Husten oder Auswurf?",
                    "required": True,
                    "show_if": {"id": "beschwerden_any", "in": ["yes"]},
                    "followup": {"id": "husten_desc", "type": "text",
                                 "label": "Seit wann? War Blut im Auswurf?", "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen, Immunabwehr & Impfungen ───────────────────
        {
            "id": "gesundheit",
            "title": "Vorerkrankungen, Abwehrkräfte & Impfungen",
            "subtitle": "Angaben, die für die ärztliche Beurteilung wichtig sind",
            "questions": [
                {
                    "id": "akute_infektion",
                    "type": "yes_no",
                    "label": "Haben Sie zurzeit eine akute Infektionskrankheit "
                             "(z.B. fieberhafter Infekt, Magen-Darm-Infekt, Grippe)?",
                    "required": True,
                    "followup": {"id": "akute_infektion_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "chron_erkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Erkrankung, die Ihre "
                             "Abwehrkräfte (Ihr Immunsystem) schwächt?",
                    "hint": "Zum Beispiel: HIV, Leukämie oder andere Krebserkrankungen, "
                            "angeborene Immundefekte, chronische Leber- oder "
                            "Nierenerkrankung.",
                    "required": True,
                    "followup": {"id": "chron_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "immunsuppression",
                    "type": "yes_no",
                    "label": "Werden Sie mit Medikamenten oder Verfahren behandelt, die das "
                             "Immunsystem unterdrücken (z.B. Immunsuppressiva nach "
                             "Transplantation oder bei Rheuma, Zytostatika/Chemotherapie, "
                             "Bestrahlung)?",
                    "required": True,
                    "followup": {"id": "immunsuppression_desc", "type": "textarea",
                                 "label": "Welche Behandlung, seit wann?", "when": "yes"},
                },
                {
                    "id": "kortison_antibiotika",
                    "type": "yes_no",
                    "label": "Nehmen Sie dauerhaft Kortison (als Tabletten oder Spritzen) "
                             "oder dauerhaft Antibiotika ein?",
                    "hint": "Gemeint ist eine ständige Behandlung des ganzen Körpers, "
                            "nicht Salben oder Sprays.",
                    "required": True,
                    "followup": {"id": "kortison_antibiotika_desc", "type": "text",
                                 "label": "Welches Medikament, seit wann?", "when": "yes"},
                },
                {
                    "id": "milz",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen die Milz entfernt?",
                    "required": True,
                },
                {
                    "id": "diabetes",
                    "type": "choice",
                    "label": "Haben Sie Diabetes (Zuckerkrankheit)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ja_gut", "label": "Ja, mein Blutzucker ist gut eingestellt"},
                        {"value": "ja_schlecht", "label": "Ja, mein Blutzucker ist zurzeit schlecht eingestellt (entgleist)"},
                        {"value": "ja_unbekannt", "label": "Ja, aber ich weiß nicht, wie gut die Einstellung ist"},
                    ],
                },
                {
                    "id": "handekzem",
                    "type": "choice",
                    "label": "Haben Sie ein Ekzem oder eine andere Hauterkrankung an den "
                             "Händen (z.B. offene, rissige oder entzündete Haut)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "akut", "label": "Ja, zurzeit akut (neu aufgetreten oder gerade entzündet)"},
                        {"value": "chronisch", "label": "Ja, dauerhaft/immer wiederkehrend (chronisch)"},
                    ],
                    "followup": {"id": "handekzem_desc", "type": "textarea",
                                 "label": "Seit wann besteht die Hauterkrankung, sind Sie in "
                                          "Behandlung, und hilft die Behandlung?",
                                 "when": "chronisch"},
                },
                {
                    "id": "durchgemachte_infektionen",
                    "type": "yes_no",
                    "label": "Haben Sie früher eine schwere Infektionskrankheit durchgemacht "
                             "oder besteht bei Ihnen eine dauerhafte (chronische) Infektion?",
                    "hint": "Zum Beispiel: Hepatitis B oder C (Leberentzündung), Tuberkulose, "
                            "HIV. Auch Kinderkrankheiten wie Masern oder Windpocken sind "
                            "wichtig, weil sie eine lebenslange Immunität hinterlassen können.",
                    "required": True,
                    "followup": {"id": "durchgemachte_infektionen_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, wann?", "when": "yes"},
                },
                {
                    "id": "impfstatus",
                    "type": "choice",
                    "label": "Haben Sie einen Impfausweis, und ist Ihr Impfschutz nach "
                             "Ihrer Kenntnis vollständig?",
                    "hint": "Bitte bringen Sie Ihren Impfausweis zur Untersuchung mit. "
                            "Nach einer Schutzimpfung oder bei lebenslanger Immunität "
                            "können Nachuntersuchungen entfallen.",
                    "required": True,
                    "options": [
                        {"value": "aktuell", "label": "Ja, mein Impfschutz ist meines Wissens vollständig"},
                        {"value": "lueckenhaft", "label": "Mein Impfschutz hat Lücken oder ist nicht aufgefrischt"},
                        {"value": "unbekannt", "label": "Weiß ich nicht / kein Impfausweis vorhanden"},
                    ],
                },
                {
                    "id": "bk_verdacht",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung "
                             "bei Ihnen und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {"id": "bk_verdacht_desc", "type": "textarea",
                                 "label": "Um welche Erkrankung geht es, und warum vermuten "
                                          "Sie einen Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Einwilligung ───────────────────────────────────────────────
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
                    "label": "Ich habe die Datenschutzhinweise gelesen und willige in die "
                             "Verarbeitung meiner Daten zu arbeitsmedizinischen Zwecken ein.",
                    "error": "Bitte akzeptieren Sie die Datenschutzhinweise.",
                    "required": True,
                },
            ],
        },
    ],
}

RULES = [
    # ── Untersuchungsarten & Fristen (Abschnitt 1.1) ─────────────────────
    {"wenn": {"untersuchungsart": ["erst"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "G 42, Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Erstuntersuchung wegen Tätigkeit mit Infektionsgefährdung",
     "konsequenz": "Erstuntersuchung vor Aufnahme der Tätigkeit durchführen; erste "
                   "Nachuntersuchung vor Ablauf von 12 Monaten, weitere vor Ablauf von "
                   "36 Monaten einplanen. Nach Schutzimpfung richtet sich die Frist nach "
                   "der Impfschutzdauer; bei lebenslanger Immunität kann die "
                   "Nachuntersuchung entfallen."},
    {"wenn": {"letzte_g42": ["ueber36", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Fristen",
     "quelle": "G 42, Abschnitt 1.1 (Nachuntersuchungen: erste vor Ablauf von 12, "
               "weitere vor Ablauf von 36 Monaten)",
     "befund": "Letzte G-42-Untersuchung liegt mehr als 36 Monate zurück oder ist unbekannt",
     "konsequenz": "Nachuntersuchungsfrist ist überschritten bzw. nicht belegbar: "
                   "vollständige Nachuntersuchung (Zwischenanamnese und Untersuchungsumfang "
                   "wie Erstuntersuchung nach Abschnitt 1.2.1) jetzt durchführen und "
                   "künftige Fristen neu festlegen; Impfschutzdauer und lebenslange "
                   "Immunität dabei berücksichtigen."},
    {"wenn": {"untersuchungsart": ["ende"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "G 42, Abschnitt 1.1 (Nachuntersuchung bei Beendigung einer Tätigkeit) "
               "und 1.2.1",
     "befund": "Untersuchung wegen Beendigung der Tätigkeit mit Infektionsgefährdung",
     "konsequenz": "Nachuntersuchung bei Beendigung der Tätigkeit durchführen und zur "
                   "möglichen Krankheitsmanifestation nach Ablauf der Inkubationszeit "
                   "beraten (Abschnitt 1.2.1)."},
    # ── Exposition / Unfälle ─────────────────────────────────────────────
    {"wenn": {"unfall_verletzung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "G 42, Abschnitte 1.1 (vorzeitige Nachuntersuchung) und 2.2 "
               "(Sofortmaßnahmen bei Unfällen)",
     "befund": "Verletzung mit der Möglichkeit des Eindringens von Infektionserregern "
               "(z.B. Nadelstichverletzung)",
     "konsequenz": "Vorzeitige Nachuntersuchung veranlassen; Unfallhergang klären, Meldung "
                   "(Verbandbuch/Durchgangsarzt) und serologische Ausgangs- und "
                   "Verlaufsdiagnostik nach ärztlichem Ermessen (Abschnitt 1.2.1); über "
                   "Sofortmaßnahmen bei künftigen Unfällen beraten."},
    {"wenn": {"psa_nutzung": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "G 42, Abschnitt 2.2 (Beratung zum Schutz vor Infektionen) und Abschnitt 2 "
               "(Gefährdungsbeurteilung)",
     "befund": "Persönliche Schutzausrüstung nicht durchgehend vorhanden oder genutzt",
     "konsequenz": "Beratung zu Übertragungswegen (Kontakt-, Tröpfchen-, Schmierinfektion), "
                   "Hygienemaßnahmen und persönlicher Schutzausrüstung (Hautschutz, "
                   "Schutzhandschuhe, flüssigkeitsdichte Schürzen, Augenschutz, Mundschutz, "
                   "FFP2/FFP3); auf die Klärung der Schutzmaßnahmen im Rahmen der "
                   "Gefährdungsbeurteilung hinwirken."},
    # ── Beurteilungskriterien: dauernde Bedenken (2.1.1) ─────────────────
    {"wenn": {"chron_erkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Immunsystem",
     "quelle": "G 42, Abschnitte 2.1.1 (dauernde gesundheitliche Bedenken) und 2.1.3",
     "befund": "Chronische Erkrankung, die die Abwehrmechanismen des Körpers dauerhaft "
               "schwächen kann",
     "konsequenz": "Dauernde gesundheitliche Bedenken erwägen (dauernd verminderte "
                   "Immunabwehr); zuvor prüfen, ob bei weniger ausgeprägter Erkrankung "
                   "eine (Weiter-)Beschäftigung unter bestimmten Voraussetzungen vertretbar "
                   "ist: verbesserte Arbeitsplatzbedingungen, besondere persönliche "
                   "Schutzausrüstung, verkürzte Nachuntersuchungsfristen (Abschnitt 2.1.3)."},
    {"wenn": {"immunsuppression": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Immunsystem",
     "quelle": "G 42, Abschnitt 2.1.1 (veränderte Abwehrlage infolge Behandlung mit "
               "Immunsuppressiva, Zytostatika, ionisierenden Strahlen)",
     "befund": "Laufende immunsuppressive Behandlung (Immunsuppressiva, Zytostatika, "
               "Bestrahlung)",
     "konsequenz": "Dauernde gesundheitliche Bedenken erwägen; Rücksprache mit den "
                   "behandelnden Ärzten zu Art und Dauer der Therapie; bei "
                   "vorübergehender Behandlung befristete Bedenken bis Therapieende "
                   "(Abschnitt 2.1.2), sonst Maßnahmen nach Abschnitt 2.1.3 prüfen."},
    {"wenn": {"kortison_antibiotika": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Immunsystem",
     "quelle": "G 42, Abschnitte 2.1.1 (systemische Dauerbehandlung mit Kortikosteroiden "
               "oder Antibiotika) und 2.1.2",
     "befund": "Systemische Dauerbehandlung mit Kortison oder Antibiotika",
     "konsequenz": "Abklären, ob die Behandlung die Abwehrmechanismen nachhaltig schwächt "
                   "(dann dauernde Bedenken nach 2.1.1) oder nur vorübergehend wirkt "
                   "(dann befristete Bedenken nach 2.1.2); Dosis und Dauer bei den "
                   "behandelnden Ärzten erfragen; ggf. verkürzte Nachuntersuchungsfristen."},
    {"wenn": {"milz": ["yes"], "erregerkontakt": ["pneumokokken"]},
     "schwere": "kritisch",
     "bereich": "Immunsystem",
     "quelle": "G 42, Abschnitt 2.1.1 (Zustand nach Milzentfernung beim Umgang mit "
               "Streptococcus pneumoniae)",
     "befund": "Zustand nach Milzentfernung bei Umgang mit Pneumokokken "
               "(Streptococcus pneumoniae)",
     "konsequenz": "Dauernde gesundheitliche Bedenken gegen den Umgang mit Streptococcus "
                   "pneumoniae erwägen; Einsatz ohne Pneumokokken-Kontakt prüfen; "
                   "Pneumokokken-Impfschutz sicherstellen und Beratung zum erhöhten "
                   "Risiko schwerer Pneumokokken-Infektionen (OPSI) dokumentieren."},
    {"wenn": {"milz": ["yes"]},
     "wenn_nicht": {"erregerkontakt": ["pneumokokken"]},
     "schwere": "pruefen",
     "bereich": "Immunsystem",
     "quelle": "G 42, Abschnitt 2.1.1 und Spezieller Teil (Streptococcus pneumoniae)",
     "befund": "Zustand nach Milzentfernung (ohne angegebenen gezielten "
               "Pneumokokken-Umgang)",
     "konsequenz": "Tätigkeitsprofil auf möglichen Kontakt zu Streptococcus pneumoniae und "
                   "anderen bekapselten Erregern prüfen; Pneumokokken-Impfschutz prüfen "
                   "und ggf. anbieten; bei relevantem Erregerkontakt Bedenken nach "
                   "Abschnitt 2.1.1 erwägen."},
    # ── Beurteilungskriterien: befristete Bedenken (2.1.2) ───────────────
    {"wenn": {"akute_infektion": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Immunsystem",
     "quelle": "G 42, Abschnitt 2.1.2 (befristete gesundheitliche Bedenken: "
               "Infektionskrankheiten)",
     "befund": "Aktuell bestehende akute Infektionskrankheit",
     "konsequenz": "Befristete gesundheitliche Bedenken bis zur Ausheilung erwägen "
                   "(vorübergehend verminderte Immunabwehr); Aufnahme bzw. Fortsetzung "
                   "der Tätigkeit erst nach Abklingen der Erkrankung; Nachuntersuchung "
                   "nach Genesung nach ärztlichem Ermessen (Abschnitt 1.1, vorzeitig)."},
    {"wenn": {"diabetes": ["ja_schlecht"]},
     "schwere": "kritisch",
     "bereich": "Stoffwechsel",
     "quelle": "G 42, Abschnitt 2.1.2 (dekompensierter Diabetes mellitus)",
     "befund": "Schlecht eingestellter (dekompensierter) Diabetes mellitus",
     "konsequenz": "Befristete gesundheitliche Bedenken bis zur Stoffwechseleinstellung "
                   "erwägen; hausärztliche/diabetologische Einstellung veranlassen; "
                   "Wiedervorstellung mit verkürzter Frist nach erfolgter Einstellung."},
    {"wenn": {"diabetes": ["ja_unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechsel",
     "quelle": "G 42, Abschnitte 1.2.1 (allgemeine Untersuchung: Blutzucker) und 2.1.2",
     "befund": "Diabetes mellitus mit unklarer Stoffwechseleinstellung",
     "konsequenz": "Aktuelle Stoffwechsellage klären (Blutzucker ist Bestandteil der "
                   "allgemeinen Untersuchung nach Abschnitt 1.2.1, ggf. Befunde des "
                   "Hausarztes einholen); bei Dekompensation befristete Bedenken nach "
                   "Abschnitt 2.1.2."},
    {"wenn": {"handekzem": ["akut"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "G 42, Abschnitt 2.1.2 (akute Handekzeme)",
     "befund": "Akutes Handekzem, das die Schutzfunktion der Haut beeinträchtigen kann",
     "konsequenz": "Befristete gesundheitliche Bedenken bis zur Abheilung erwägen, wenn "
                   "das Ekzem die Schutzfunktion der Haut gegenüber Infektionserregern "
                   "beeinträchtigt oder die Dekontamination erschwert; Hautschutzberatung "
                   "und dermatologische Behandlung; Wiedervorstellung nach Abheilung."},
    {"wenn": {"handekzem": ["chronisch"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "G 42, Abschnitte 2.1.1 (chronische, therapieresistente Handekzeme) "
               "und 2.1.3",
     "befund": "Chronisches bzw. immer wiederkehrendes Handekzem",
     "konsequenz": "Dermatologisch abklären, ob das Ekzem therapieresistent ist und die "
                   "Schutzfunktion der Haut dauerhaft beeinträchtigt (dann dauernde "
                   "Bedenken nach 2.1.1); andernfalls prüfen, ob die Beschäftigung unter "
                   "Voraussetzungen nach 2.1.3 (Hautschutzplan, besondere Handschuhe, "
                   "verkürzte Nachuntersuchungsfristen) vertretbar ist."},
    # ── Beschwerden mit Abklärungsbedarf (1.2.1) ─────────────────────────
    {"wenn": {"husten": ["yes"], "fieber_nachtschweiss": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Beschwerden",
     "quelle": "G 42, Abschnitt 1.2.1 (bei Auffälligkeiten: Röntgenaufnahme des Thorax) "
               "und Spezieller Teil (Mycobacterium tuberculosis)",
     "befund": "Husten/Auswurf über 3 Wochen zusammen mit Fieber/Nachtschweiß "
               "(mögliche Zeichen einer Tuberkulose oder anderen schweren Infektion)",
     "konsequenz": "Abklärung vor Aufnahme bzw. Fortsetzung der Tätigkeit: erweiterte "
                   "Diagnostik nach Abschnitt 1.2.1 (Röntgenaufnahme des Thorax bzw. "
                   "Berücksichtigung eines Röntgenbefundes nicht älter als 12 Monate, "
                   "weitere serologische Diagnostik, Spirometrie); Ausschluss einer "
                   "ansteckungsfähigen Erkrankung, Meldepflichten nach IfSG beachten."},
    {"wenn": {"husten": ["yes"]},
     "wenn_nicht": {"fieber_nachtschweiss": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "G 42, Abschnitt 1.2.1 (bei Bedarf bzw. Auffälligkeiten: Spirometrie, "
               "Röntgenaufnahme des Thorax)",
     "befund": "Husten oder Auswurf seit mehr als 3 Wochen",
     "konsequenz": "Ursache abklären: Spirometrie und ggf. Röntgenaufnahme des Thorax "
                   "nach Abschnitt 1.2.1 (bzw. Röntgenbefund nicht älter als 12 Monate "
                   "berücksichtigen); hausärztliche Abklärung empfehlen."},
    {"wenn": {"infekt_haeufig": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Immunsystem",
     "quelle": "G 42, Abschnitte 1.2.1 (Blutstatus, Blutsenkung, weitere Diagnostik) "
               "und 2.1",
     "befund": "Erhöhte Infektanfälligkeit",
     "konsequenz": "Hinweis auf möglicherweise verminderte Immunabwehr: allgemeine "
                   "Untersuchung nach Abschnitt 1.2.1 (Blutstatus mit Differenzierung, "
                   "Blutsenkung, Blutzucker, Leberwerte, Urinstatus) auswerten, ggf. "
                   "weitere serologische Diagnostik; Beurteilung nach den Kriterien "
                   "in Abschnitt 2.1."},
    # ── Infektionen, Impfschutz, Berufskrankheit ─────────────────────────
    {"wenn": {"durchgemachte_infektionen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankungen",
     "quelle": "G 42, Abschnitte 1.1 (Nachuntersuchung kann bei lebenslanger Immunität "
               "entfallen) und 1.2.1 (weitere serologische Diagnostik)",
     "befund": "Durchgemachte schwere oder bestehende chronische Infektionskrankheit",
     "konsequenz": "Immunitätslage bzw. Aktivität der Infektion klären (serologische "
                   "Diagnostik nach ärztlichem Ermessen); bei nachgewiesener lebenslanger "
                   "Immunität können Nachuntersuchungen entfallen; bei bestehender "
                   "Infektion Bedenken nach Abschnitt 2.1 und Einsatzmöglichkeiten "
                   "prüfen."},
    {"wenn": {"impfstatus": ["lueckenhaft", "unbekannt"]},
     "schwere": "hinweis",
     "bereich": "Impfschutz",
     "quelle": "G 42, Abschnitte 1.2.1 (Impfanamnese, Impfangebot) und 2.2 "
               "(Immunisierung)",
     "befund": "Impfschutz lückenhaft oder unbekannt",
     "konsequenz": "Impfanamnese anhand des Impfausweises erheben; nach entsprechender "
                   "Beratung Impfangebot gegen die tätigkeitsrelevanten impfpräventablen "
                   "Erreger unterbreiten (aktive/passive Immunisierung, Kontraindikationen, "
                   "Impfkalender); Hinweis: Impfschäden bei beruflicher Indikation sind "
                   "durch die gesetzliche Unfallversicherung abgedeckt (§ 1 SGB VII). "
                   "Nach Schutzimpfung können Nachuntersuchungen entfallen, solange "
                   "ausreichender Impfschutz besteht."},
    {"wenn": {"bk_verdacht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Berufskrankheit",
     "quelle": "G 42, Abschnitte 1.1 (vorzeitige Nachuntersuchung) und 4 "
               "(Berufskrankheiten Nrn. 3101–3104 BKV)",
     "befund": "Vermuteter Zusammenhang zwischen Erkrankung und Tätigkeit",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen (Anlass: vermuteter "
                   "Zusammenhang zwischen Erkrankung und Tätigkeit); prüfen, ob ein "
                   "begründeter Verdacht auf eine Berufskrankheit (Nrn. 3101–3104 BKV) "
                   "vorliegt und ggf. ärztliche Anzeige an den Unfallversicherungsträger "
                   "erstatten; sonst an die Möglichkeit des Arbeitsunfalls (§ 8 SGB VII) "
                   "denken."},
]
