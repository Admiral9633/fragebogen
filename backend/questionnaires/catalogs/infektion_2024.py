# -*- coding: utf-8 -*-
"""
Tätigkeiten mit Infektionsgefährdung – DGUV Empfehlung 2024 (E INF).

Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und
Untersuchungen, 1. Auflage 2024, "Tätigkeiten mit Infektionsgefährdung"
(Kurzbezeichnung E INF, Fassung Januar 2022), S. 773–797.

Anamnese-Fragen, die die versicherte Person selbst beantworten kann
(Tätigkeit/Exposition, Schutzmaßnahmen, Beschwerden, Vorerkrankungen,
Impfanamnese), plus datengetriebene Auswertungsregeln nach Abschnitt 2
(Vorsorgeanlässe), Abschnitt 7 (Eingangsberatung, Untersuchung, Fristen,
Beurteilungskriterien) und Abschnitt 8 (abschließende Beratung).
Keine Messwerte oder ärztlichen Befunde.
"""

SLUG = "infektion-2024"

CATALOG = {
    "version": 2,
    "title": "Tätigkeiten mit Infektionsgefährdung (DGUV Empfehlung 2024)",
    "basis": (
        "DGUV Empfehlungen für arbeitsmedizinische Beratungen und "
        "Untersuchungen, 1. Auflage 2024, „Tätigkeiten mit "
        "Infektionsgefährdung“ (E INF, Fassung Januar 2022), S. 773–797"
    ),
    "sections": [
        # ── 1 ─────────────────────────────────────────────────────────────
        {
            "id": "anlass",
            "title": "Anlass der Vorsorge",
            "subtitle": "Warum Sie heute hier sind",
            "questions": [
                {
                    "id": "vorsorge_art",
                    "type": "choice",
                    "label": "Waren Sie wegen Infektionsgefährdung bei der Arbeit schon "
                             "einmal bei einer arbeitsmedizinischen Vorsorge?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Nein, dies ist meine erste Vorsorge"},
                        {"value": "weitere", "label": "Ja, ich war schon einmal oder mehrmals dort"},
                    ],
                },
                {
                    "id": "vorsorge_typ",
                    "type": "choice",
                    "label": "Wissen Sie, um welche Art der Vorsorge es sich heute handelt?",
                    "required": True,
                    "hint": "Steht meist auf der Einladung Ihres Arbeitgebers. "
                            "Wenn Sie es nicht wissen, ist das kein Problem.",
                    "options": [
                        {"value": "pflicht", "label": "Pflichtvorsorge (vom Arbeitgeber veranlasst)"},
                        {"value": "angebot", "label": "Angebotsvorsorge (vom Arbeitgeber angeboten)"},
                        {"value": "wunsch", "label": "Wunschvorsorge (auf meinen eigenen Wunsch)"},
                        {"value": "ende", "label": "Vorsorge am Ende der Tätigkeit"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 2 ─────────────────────────────────────────────────────────────
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
                    "hint": "Zum Beispiel: Pflegefachkraft auf einer Intensivstation, "
                            "Erzieherin in einer Krippe, MTA im Bakteriologie-Labor.",
                    "required": True,
                },
                {
                    "id": "erregerkontakt",
                    "type": "multi_choice",
                    "label": "Welche der folgenden Situationen kommen bei Ihrer Arbeit "
                             "regelmäßig vor? (Mehrfachauswahl möglich)",
                    "required": True,
                    "options": [
                        {"value": "koerperfluessigkeiten", "label": "Kontakt mit Blut, Körperflüssigkeiten, Ausscheidungen oder Gewebe in größerem Umfang"},
                        {"value": "stichgefahr", "label": "Erhöhte Gefahr von Stich- oder Schnittverletzungen (z.B. Nadeln, Skalpelle)"},
                        {"value": "aerosol", "label": "Verspritzen von Flüssigkeiten oder Einatmen von Bioaerosolen (feinen Schwebeteilchen)"},
                        {"value": "direktkontakt", "label": "Direkter Kontakt zu erkrankten oder krankheitsverdächtigen Menschen"},
                        {"value": "tierkontakt", "label": "Kontakt zu Tieren, Tierprodukten oder tierischen Proben"},
                        {"value": "vegetation", "label": "Arbeiten in niederer Vegetation (Gras, Gebüsch) – Zeckengefahr"},
                        {"value": "keine", "label": "Nichts davon"},
                    ],
                },
                {
                    "id": "expo_haeufigkeit",
                    "type": "choice",
                    "label": "Wie häufig haben Sie solchen Kontakt zu möglicherweise "
                             "infektiösem Material oder erkrankten Personen?",
                    "required": True,
                    "options": [
                        {"value": "taeglich", "label": "Täglich"},
                        {"value": "mehrmals_woche", "label": "Mehrmals pro Woche"},
                        {"value": "seltener", "label": "Seltener"},
                        {"value": "nie", "label": "Praktisch nie"},
                    ],
                },
                {
                    "id": "risiko_gruppen",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Personengruppen, bei denen Infektionskrankheiten "
                             "häufiger vorkommen (z.B. Drogenhilfe, Justizvollzug, "
                             "Geflüchteten-Unterkünfte, Tuberkulose-Abteilung)?",
                    "required": True,
                },
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Steht Ihnen die nötige persönliche Schutzausrüstung (z.B. Handschuhe, "
                             "Maske, Schutzbrille, Schürze) zur Verfügung, und nutzen Sie sie?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, vorhanden und ich nutze sie regelmäßig"},
                        {"value": "teilweise", "label": "Teilweise (nicht immer vorhanden oder nicht immer genutzt)"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "nicht_noetig", "label": "Für meine Tätigkeit nicht erforderlich"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme beim Tragen der Schutzausrüstung "
                             "(z.B. Hautprobleme unter den Handschuhen, Beschwerden "
                             "unter der Atemschutzmaske)?",
                    "required": True,
                    "followup": {"id": "psa_probleme_desc", "type": "textarea",
                                 "label": "Welche Probleme haben Sie?", "when": "yes"},
                },
                {
                    "id": "nadelstich",
                    "type": "yes_no",
                    "label": "Hatten Sie in den letzten 12 Monaten eine Stich- oder "
                             "Schnittverletzung oder anderen ungeschützten Kontakt mit "
                             "möglicherweise infektiösem Material (z.B. Nadelstichverletzung, "
                             "Blutspritzer ins Auge oder auf verletzte Haut)?",
                    "required": True,
                    "followup": {"id": "nadelstich_desc", "type": "textarea",
                                 "label": "Was ist passiert? Wurde der Vorfall gemeldet "
                                          "und ärztlich versorgt?", "when": "yes"},
                },
                {
                    "id": "psych_belastung",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich durch die Infektionsgefahr bei Ihrer Arbeit "
                             "seelisch belastet (z.B. Angst vor Ansteckung, Anspannung)?",
                    "required": True,
                },
            ],
        },
        # ── 3 ─────────────────────────────────────────────────────────────
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
                            "Nachtschweiß, starke Müdigkeit, ungewollter Gewichtsverlust, "
                            "Schmerzen. Wenn nein, verkürzt sich der Fragebogen.",
                    "required": True,
                },
                {
                    "id": "infektanfaelligkeit",
                    "type": "yes_no",
                    "label": "Sind Sie häufiger erkältet oder öfter von Infekten betroffen "
                             "als andere Menschen in Ihrem Umfeld?",
                    "required": True,
                    "show_if": {"id": "beschwerden_any", "in": ["yes"]},
                },
                {
                    "id": "abgeschlagenheit",
                    "type": "yes_no",
                    "label": "Leiden Sie unter anhaltender Abgeschlagenheit, Müdigkeit "
                             "oder Erschöpfung?",
                    "required": True,
                    "show_if": {"id": "beschwerden_any", "in": ["yes"]},
                },
                {
                    "id": "nachtschweiss",
                    "type": "yes_no",
                    "label": "Schwitzen Sie nachts so stark, dass Sie Wäsche oder "
                             "Bettzeug wechseln müssen (Nachtschweiß)?",
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
                {
                    "id": "gewichtsverlust",
                    "type": "yes_no",
                    "label": "Haben Sie in den letzten Monaten ungewollt an Gewicht verloren?",
                    "required": True,
                    "show_if": {"id": "beschwerden_any", "in": ["yes"]},
                },
                {
                    "id": "schmerzen_einschraenkung",
                    "type": "yes_no",
                    "label": "Schränken Schmerzen (z.B. Gelenk- oder Bauchschmerzen) "
                             "Sie bei Ihrer Arbeit ein?",
                    "required": True,
                    "show_if": {"id": "beschwerden_any", "in": ["yes"]},
                },
            ],
        },
        # ── 4 ─────────────────────────────────────────────────────────────
        {
            "id": "gesundheit",
            "title": "Vorerkrankungen, Abwehrkräfte & Impfungen",
            "subtitle": "Angaben zu Ihrem Immunsystem und Ihrem Impfschutz",
            "questions": [
                {
                    "id": "immunerkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung, die Ihr Immunsystem (Ihre "
                             "Abwehrkräfte) schwächt?",
                    "hint": "Zum Beispiel: HIV, Leukämie oder andere Krebserkrankungen, "
                            "angeborene Immundefekte, fehlende Milz, chronische Leber- "
                            "oder Nierenerkrankung, Diabetes.",
                    "required": True,
                    "followup": {"id": "immunerkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "immunmedikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie Medikamente ein, die das Immunsystem schwächen, "
                             "oder erhalten Sie eine solche Behandlung?",
                    "hint": "Zum Beispiel: Kortison als Dauertherapie, Immunsuppressiva "
                            "(z.B. nach Transplantation oder bei Rheuma), Chemotherapie, "
                            "Biologika, Strahlentherapie.",
                    "required": True,
                    "followup": {"id": "immunmedikamente_desc", "type": "textarea",
                                 "label": "Welche Medikamente/Behandlung?", "when": "yes"},
                },
                {
                    "id": "infektionskrankheiten",
                    "type": "yes_no",
                    "label": "Haben Sie früher eine schwere Infektionskrankheit durchgemacht "
                             "oder besteht bei Ihnen eine dauerhafte (chronische) Infektion?",
                    "hint": "Zum Beispiel: Hepatitis B oder C (Leberentzündung), Tuberkulose, "
                            "HIV, Pfeiffersches Drüsenfieber mit langem Verlauf.",
                    "required": True,
                    "followup": {"id": "infektionskrankheiten_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, wann?", "when": "yes"},
                },
                {
                    "id": "zwischenzeitlich",
                    "type": "yes_no",
                    "label": "Gab es seit Ihrer letzten Vorsorge Infektionen, Erkrankungen "
                             "oder Unfälle mit Kontakt zu möglicherweise infektiösem Material?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere"]},
                    "followup": {"id": "zwischenzeitlich_desc", "type": "textarea",
                                 "label": "Was ist passiert?", "when": "yes"},
                },
                {
                    "id": "hauterkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie ein Handekzem oder eine andere Hauterkrankung an "
                             "Händen oder Unterarmen (z.B. offene, rissige oder entzündete Haut)?",
                    "required": True,
                    "followup": {"id": "hauterkrankung_desc", "type": "textarea",
                                 "label": "Seit wann, wie ausgeprägt, sind Sie in Behandlung?",
                                 "when": "yes"},
                },
                {
                    "id": "schwanger",
                    "type": "choice",
                    "label": "Sind Sie schwanger oder stillen Sie zurzeit?",
                    "hint": "Die Angabe ist freiwillig. Sie ist wichtig, weil manche "
                            "Infektionen dem ungeborenen Kind schaden können und besondere "
                            "Schutzmaßnahmen möglich sind.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unsicher", "label": "Bin mir nicht sicher"},
                        {"value": "keine_angabe", "label": "Keine Angabe"},
                    ],
                },
                {
                    "id": "impfstatus",
                    "type": "choice",
                    "label": "Haben Sie einen Impfausweis, und ist Ihr Impfschutz nach "
                             "Ihrer Kenntnis vollständig?",
                    "hint": "Bitte bringen Sie Ihren Impfausweis zur Vorsorge mit. "
                            "Ihr Arbeitgeber erfährt Ihren Impf- und Immunstatus nicht.",
                    "required": True,
                    "options": [
                        {"value": "aktuell", "label": "Ja, mein Impfschutz ist meines Wissens vollständig"},
                        {"value": "lueckenhaft", "label": "Mein Impfschutz hat Lücken oder ist nicht aufgefrischt"},
                        {"value": "unbekannt", "label": "Weiß ich nicht / kein Impfausweis vorhanden"},
                    ],
                },
                {
                    "id": "impfallergie",
                    "type": "yes_no",
                    "label": "Haben Sie eine Allergie gegen Impfstoff-Bestandteile (z.B. "
                             "Hühnereiweiß) oder hatten Sie schon einmal eine schwere "
                             "allergische Reaktion (anaphylaktischer Schock)?",
                    "required": True,
                    "followup": {"id": "impfallergie_desc", "type": "textarea",
                                 "label": "Wogegen sind Sie allergisch, was ist passiert?",
                                 "when": "yes"},
                },
                {
                    "id": "lebendimpfung",
                    "type": "yes_no",
                    "label": "Haben Sie in den letzten 4 Wochen eine Lebendimpfung "
                             "(z.B. Masern-Mumps-Röteln, Windpocken) oder eine "
                             "Immunglobulin-Gabe (Antikörper-Spritze) erhalten?",
                    "required": True,
                },
                {
                    "id": "blutspende_op",
                    "type": "yes_no",
                    "label": "Planen Sie in nächster Zeit eine Blutspende oder ist eine "
                             "Operation geplant?",
                    "required": True,
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
        # ── 5 ─────────────────────────────────────────────────────────────
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
    # ── Fristen / Vorsorgeanlass (Abschnitte 2 und 7.3) ──────────────────
    {"wenn": {"vorsorge_art": ["erste"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "E INF, Abschnitte 2 und 7.3 (AMR 2.1)",
     "befund": "Erste Vorsorge wegen Tätigkeiten mit Infektionsgefährdung",
     "konsequenz": "Erste Vorsorge vor Aufnahme der Tätigkeit durchführen; weitere Vorsorgen "
                   "fristgerecht nach AMR 2.1 veranlassen bzw. anbieten. Die Fristen für "
                   "Pflicht- und Angebotsvorsorge gelten unabhängig von Impfungen und "
                   "lebenslanger Immunität."},
    {"wenn": {"vorsorge_typ": ["ende"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "E INF, Abschnitt 2 (Angebotsvorsorge Nr. 3)",
     "befund": "Vorsorge am Ende einer Tätigkeit mit Pflichtvorsorge-Anlass",
     "konsequenz": "Angebotsvorsorge am Ende der Tätigkeit durchführen; über mögliche "
                   "Krankheitsmanifestation nach Ablauf der Inkubationszeit sowie über "
                   "nachgehende Ansprüche (Berufskrankheiten-Verfahren) beraten."},
    {"wenn": {"zwischenzeitlich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Fristen",
     "quelle": "E INF, Abschnitte 7.1 und 7.4.3",
     "befund": "Zwischenzeitliche Infektion, Erkrankung oder Unfall mit infektiösem Material "
               "seit der letzten Vorsorge",
     "konsequenz": "Ereignis ärztlich abklären; nach ärztlichem Ermessen Serostatus/Blutbild "
                   "bestimmen (Abschnitt 7.2.2). Bei auffälligem Serostatus verkürzte "
                   "Vorsorgefrist bis zu dessen Klärung ansetzen (Abschnitt 7.4.3)."},
    # ── Exposition / Unfälle ─────────────────────────────────────────────
    {"wenn": {"nadelstich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "E INF, Abschnitt 2 (Angebotsvorsorge Nr. 2) und Abschnitt 7.1",
     "befund": "Stich-/Schnittverletzung oder ungeschützter Kontakt mit möglicherweise "
               "infektiösem Material in den letzten 12 Monaten",
     "konsequenz": "Vorgehen nach Exposition prüfen: Meldung als Arbeitsunfall (Verbandbuch/"
                   "D-Arzt), Angebotsvorsorge nach § 5 Abs. 2 ArbMedVV veranlassen, wenn mit "
                   "einer schweren Infektionskrankheit gerechnet werden muss und "
                   "postexpositionelle Prophylaxe (z.B. HBV-Immunprophylaxe, HIV-PEP) möglich "
                   "ist oder eine Infektion erfolgt ist; Serostatus nach ärztlichem Ermessen; "
                   "Beratung zu Sofortmaßnahmen und stichsicheren Produkten."},
    {"wenn": {"erregerkontakt": ["vegetation"]},
     "schwere": "hinweis",
     "bereich": "Exposition",
     "quelle": "E INF, Abschnitt 2 (Pflichtvorsorge Nr. 3 m)",
     "befund": "Regelmäßige Tätigkeiten in niederer Vegetation bzw. mit Zeckenexposition",
     "konsequenz": "Beratung zu Borreliose und FSME (Zeckenschutz, Absuchen der Haut, "
                   "Verhalten nach Zeckenstich); in FSME-Endemiegebieten Impfangebot gegen "
                   "FSME im Rahmen der Vorsorge unterbreiten (AMR 6.5)."},
    {"wenn": {"psa_nutzung": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "E INF, Abschnitte 7.1 und 8.2 (§ 6 Abs. 4 ArbMedVV)",
     "befund": "Persönliche Schutzausrüstung nicht durchgehend vorhanden oder genutzt",
     "konsequenz": "Beratung zu Schutzmaßnahmen und Hygiene (PSA nach TRBA 250: Handschuhe, "
                   "FFP2/FFP3, Augenschutz, flüssigkeitsdichte Schürzen). Ergeben sich "
                   "Anhaltspunkte für unzureichende Arbeitsschutzmaßnahmen, Mitteilung an "
                   "den Unternehmer/die Unternehmerin mit Vorschlag von Schutzmaßnahmen."},
    {"wenn": {"psa_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "E INF, Abschnitt 7.1 (weitere Vorsorgen)",
     "befund": "Probleme mit der persönlichen Schutzausrüstung (z.B. Hautprobleme unter "
               "Handschuhen, Beschwerden unter Atemschutz)",
     "konsequenz": "Beratung zu Hautschutzplan, Handschuhauswahl und Tragezeitbegrenzung; "
                   "bei Handekzemen dermatologische Abklärung erwägen; Akzeptanz der PSA "
                   "bei der Auswahl berücksichtigen."},
    {"wenn": {"psych_belastung": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Psychische Belastung",
     "quelle": "E INF, Abschnitte 7.1 und 7.1 (allgemeine Beratung)",
     "befund": "Psychische Belastung durch Infektionsgefährdung (z.B. Angst vor Ansteckung)",
     "konsequenz": "Beratung zu psychischen Belastungsfaktoren, die mit erhöhten "
                   "Infektionsgefahren verbunden sind; ggf. weitergehende Unterstützung "
                   "(z.B. betriebliches Gesundheitsmanagement) anbieten."},
    # ── Immunsystem / Beurteilung (Abschnitt 7.4) ────────────────────────
    {"wenn": {"immunerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Immunsystem",
     "quelle": "E INF, Abschnitte 7.2.2, 7.4, 7.4.2 und 7.4.3",
     "befund": "Erkrankung mit möglicherweise verminderter Immunabwehr",
     "konsequenz": "Verminderte Immunabwehr bei der Beurteilung berücksichtigen: klinische "
                   "Untersuchung (z.B. Serostatus, Blutbild) nach ärztlichem Ermessen; "
                   "Schutzmaßnahmen nach Abschnitt 7.4.2 prüfen (expositionsärmerer Einsatz, "
                   "PSA, Schutzimpfung); verkürzte Vorsorgefristen nach Abschnitt 7.4.3 "
                   "erwägen. Haben die Maßnahmen keine Aussicht auf Erfolg, Tätigkeitswechsel "
                   "erwägen (7.4.4; Mitteilung an den Arbeitgeber nur mit Einwilligung, "
                   "§ 6 Abs. 4 ArbMedVV)."},
    {"wenn": {"immunmedikamente": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Immunsystem",
     "quelle": "E INF, Abschnitte 7.4, 7.4.2, 7.4.3 und Literatur „Impfen bei Immundefizienz“",
     "befund": "Immunschwächende Medikamente oder Behandlung (Immunsuppressiva, Kortison-"
               "Dauertherapie, Chemo-/Strahlentherapie, Biologika)",
     "konsequenz": "Wie bei verminderter Immunabwehr verfahren (Maßnahmen 7.4.2, verkürzte "
                   "Fristen 7.4.3, ggf. Tätigkeitswechsel 7.4.4). Bei Impfberatung Hinweise "
                   "„Impfen bei Immundefizienz“ beachten; Lebendimpfstoffe auf "
                   "Kontraindikationen prüfen."},
    {"wenn": {"infektanfaelligkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Immunsystem",
     "quelle": "E INF, Abschnitte 7.1 (Beschwerden) und 7.2.2",
     "befund": "Erhöhte Infektanfälligkeit",
     "konsequenz": "Ursachen ärztlich abklären (nach Ermessen Blutbild, Serostatus, "
                   "hausärztliche Mitbehandlung); Beurteilung nach Abschnitt 7.4 "
                   "unter Berücksichtigung einer möglichen verminderten Immunabwehr."},
    {"wenn": {"hauterkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "E INF, Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Handekzem oder Hauterkrankung an Händen/Unterarmen",
     "konsequenz": "Prüfen, ob die Hautveränderungen die Schutzfunktion der Haut gegenüber "
                   "Infektionserregern beeinträchtigen oder die Dekontamination erschweren; "
                   "Hautschutzberatung, ggf. dermatologische Vorstellung; ist eine Änderung "
                   "des Schweregrades zu erwarten, verkürzte Vorsorgefristen (7.4.3)."},
    # ── Beschwerden mit Abklärungsbedarf ─────────────────────────────────
    {"wenn": {"husten": ["yes"], "nachtschweiss": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Beschwerden",
     "quelle": "E INF, Abschnitte 6.3.2, 7.2.2 und 7.4",
     "befund": "Husten/Auswurf über 3 Wochen zusammen mit Nachtschweiß "
               "(mögliche Zeichen einer Tuberkulose oder anderen schweren Infektion)",
     "konsequenz": "Ärztliche Abklärung vor Aufnahme bzw. Fortsetzung der Tätigkeit "
                   "veranlassen (Ausschluss einer ansteckungsfähigen Erkrankung); "
                   "Röntgenaufnahme des Thorax nur bei rechtfertigender Indikation, z.B. "
                   "nach erstmalig positivem IGRA-Test nach Tuberkulosekontakt (7.2.2); "
                   "ggf. Meldepflichten nach IfSG beachten."},
    {"wenn": {"infektionskrankheiten": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankungen",
     "quelle": "E INF, Abschnitte 7.1, 7.4 und 8.1",
     "befund": "Durchgemachte schwere oder bestehende chronische Infektionskrankheit",
     "konsequenz": "Immunitätslage bzw. Aktivität der Infektion klären (Serostatus nach "
                   "ärztlichem Ermessen); bei auffälligem Serostatus verkürzte Frist bis "
                   "zur Klärung (7.4.3); über haus-/fachärztliche Kontrollen beraten; bei "
                   "Verdacht auf beruflichen Zusammenhang BK-Meldepflicht beachten (8.1)."},
    {"wenn": {"bk_verdacht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Berufskrankheit",
     "quelle": "E INF, Abschnitte 6.5 und 8.1",
     "befund": "Vermuteter Zusammenhang zwischen Erkrankung und Tätigkeit",
     "konsequenz": "Prüfen, ob ein begründeter Verdacht auf eine Berufskrankheit "
                   "(BK-Nrn. 3101–3104 BKV) vorliegt; ggf. ärztliche BK-Anzeige an den "
                   "Unfallversicherungsträger erstatten; Wunschvorsorge ermöglichen."},
    # ── Impfungen / besondere Situationen ────────────────────────────────
    {"wenn": {"impfstatus": ["lueckenhaft", "unbekannt"]},
     "schwere": "hinweis",
     "bereich": "Impfschutz",
     "quelle": "E INF, Abschnitte 6.4, 7.1 (Impfberatung) und AMR 6.5",
     "befund": "Impfschutz lückenhaft oder unbekannt",
     "konsequenz": "Impfausweis prüfen, Impfberatung nach STIKO-Empfehlungen durchführen "
                   "und tätigkeitsbezogen Impfangebot als Bestandteil der Vorsorge "
                   "unterbreiten (AMR 6.5); Freiwilligkeit betonen. Impf- und Serostatus "
                   "dürfen dem Arbeitgeber nicht mitgeteilt werden (Abschnitt 6.4)."},
    {"wenn": {"impfallergie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Impfschutz",
     "quelle": "E INF, Abschnitt 7.1 (Impfberatung: Kontraindikationen)",
     "befund": "Allergie gegen Impfstoff-Bestandteile oder frühere anaphylaktische Reaktion",
     "konsequenz": "Kontraindikationen vor jedem Impfangebot sorgfältig prüfen; ggf. "
                   "allergologische Abklärung bzw. Auswahl eines alternativen Impfstoffs; "
                   "Impfung nur unter geeigneten Überwachungsbedingungen."},
    {"wenn": {"lebendimpfung": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Impfschutz",
     "quelle": "E INF, Abschnitt 7.1 (Impfberatung: Mindestabstände)",
     "befund": "Lebendimpfung oder Immunglobulin-Gabe in den letzten 4 Wochen",
     "konsequenz": "Mindestabstände beachten: weitere Lebendimpfungen frühestens 4 Wochen "
                   "nach der letzten Lebendimpfung; nach Immunglobulingabe verzögerte "
                   "Wirksamkeit von Lebendimpfstoffen berücksichtigen, Impftermine "
                   "entsprechend planen."},
    {"wenn": {"blutspende_op": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Impfschutz",
     "quelle": "E INF, Abschnitt 7.1 (Anamnese: geplante Blutspenden, geplante Operationen)",
     "befund": "Geplante Blutspende oder Operation",
     "konsequenz": "Impftermine mit geplanten Blutspenden und Operationen abstimmen "
                   "(Rückstellfristen der Blutspendedienste, perioperative Planung); "
                   "Beratung dazu dokumentieren."},
    {"wenn": {"schwanger": ["ja", "unsicher"]},
     "schwere": "pruefen",
     "bereich": "Mutterschutz",
     "quelle": "E INF, Abschnitt 7.1 (Beratung: Fetopathien, präventiver Mutterschutz) und MuSchG",
     "befund": "Schwangerschaft/Stillzeit angegeben oder möglich",
     "konsequenz": "Beratung zu möglichen Fetopathien (z.B. Röteln, Varizellen, CMV, "
                   "Parvovirus B19) und Schutzmaßnahmen in Schwangerschaft und Stillzeit; "
                   "Immunitätslage klären; auf mutterschutzrechtliche Gefährdungsbeurteilung "
                   "und ggf. Umsetzung auf expositionsarme Tätigkeiten hinwirken; "
                   "Lebendimpfungen in der Schwangerschaft kontraindiziert."},
]
