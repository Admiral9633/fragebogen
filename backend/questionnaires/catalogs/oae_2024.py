# -*- coding: utf-8 -*-
"""Tätigkeiten mit Stoffen, die obstruktive Atemwegserkrankungen auslösen können –
DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen
und Untersuchungen, 1. Auflage 2024, »Tätigkeiten mit Stoffen, die obstruktive
Atemwegserkrankungen auslösen können« (E OAE, Fassung Januar 2022), S. 680–697."""

SLUG = "oae-2024"

CATALOG = {
    "version": 2,
    "title": "Stoffe mit Gefahr obstruktiver Atemwegserkrankungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Tätigkeiten mit Stoffen, die obstruktive Atemwegs"
             "erkrankungen auslösen können« (E OAE, Fassung Januar 2022), S. 680–697",
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
                             "atemwegsbelastender Stoffe (z. B. Mehlstaub, Tierstaub, "
                             "Reizstoffe)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge zu diesem Anlass"},
                        {"value": "weitere", "label": "Nein, ich war deswegen schon einmal zur Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge muss der Betrieb z. B. veranlassen bei Mehlstaub "
                            "oder Getreide-/Futtermittelstaub über 4 mg je Kubikmeter Luft, "
                            "bei Labortierstaub in Tierhaltungsräumen, bei proteinreichen "
                            "Naturgummilatex-Handschuhen oder beim Versprühen unausgehärteter "
                            "Epoxidharze.",
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
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Arbeitsstoffe",
            "subtitle": "Ihre Arbeit und die Stoffe, mit denen Sie umgehen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "stoffgruppen",
                    "type": "multi_choice",
                    "label": "Mit welchen Stäuben, Dämpfen oder Stoffen haben Sie bei der "
                             "Arbeit zu tun?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "mehl_backmittel", "label": "Mehlstaub, Backmittel oder enzymhaltige Stäube (Bäckerei, Konditorei, Mühle)"},
                        {"value": "getreide_futter", "label": "Getreide- oder Futtermittelstäube (Landwirtschaft, Futtermittel)"},
                        {"value": "tierstaub", "label": "Stäube von Tieren (Labor- oder Nutztiere, Tierhaltung)"},
                        {"value": "latex", "label": "Naturgummilatex-Handschuhe (gepudert / proteinreich)"},
                        {"value": "pflanzen_holz", "label": "Pflanzenbestandteile, Pollen oder Holzstäube (Gärtnerei, Floristik, Tischlerei)"},
                        {"value": "schimmel_milben", "label": "Schimmelpilz- oder milbenhaltiger Staub"},
                        {"value": "friseur", "label": "Haarfärbe- oder Blondiermittel (Persulfate), Haarstaub (Friseurhandwerk)"},
                        {"value": "desinfektion", "label": "Desinfektionsmittel (z. B. Pflege, Praxis, Labor)"},
                        {"value": "epoxid", "label": "Unausgehärtete Epoxidharze (z. B. Beschichten, Kleben, Versprühen)"},
                        {"value": "isocyanate", "label": "Isocyanate (z. B. PU-Schäume, 2K-Lacke, Klebstoffe)"},
                        {"value": "platinsalze", "label": "Platinsalze (z. B. Katalysatoren, Galvanik)"},
                        {"value": "haerter_kolophonium", "label": "Kunstharz-Härter, Metallkleber (Säureanhydride) oder Lötrauch (Kolophonium)"},
                        {"value": "metall", "label": "Metallstäube oder -rauche (z. B. Kobalt, Nickel)"},
                        {"value": "saeuren_reizgase", "label": "Säure-/Laugen-Nebel, Formaldehyd oder Reizgase (z. B. Ammoniak, Chlor, Schwefeldioxid)"},
                        {"value": "andere", "label": "Andere Stäube, Dämpfe oder Rauche"},
                        {"value": "unbekannt", "label": "Keiner davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie mit solchen Stoffen?",
                    "required": True,
                    "options": [
                        {"value": "beginnt", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis15", "label": "5 bis 15 Jahre"},
                        {"value": "ueber15", "label": "Mehr als 15 Jahre"},
                    ],
                },
                {
                    "id": "frueher_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt zu Stäuben, "
                             "Dämpfen oder reizenden Stoffen?",
                    "required": True,
                    "followup": {"id": "frueher_expo_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "schutzmassnahmen",
                    "type": "multi_choice",
                    "label": "Welche Schutzmaßnahmen gibt es an Ihrem Arbeitsplatz?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "absaugung", "label": "Absaugung oder Lüftung an der Staub-/Dampfquelle"},
                        {"value": "atemschutz", "label": "Atemschutz (z. B. FFP-Maske)"},
                        {"value": "handschuhe", "label": "Schutzhandschuhe"},
                        {"value": "kleidung", "label": "Arbeitskleidung wird regelmäßig gewechselt"},
                        {"value": "keine", "label": "Keine besonderen Schutzmaßnahmen"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden an Augen, Nase, Atemwegen und Haut",
            "questions": [
                {
                    "id": "beschwerden_vorhanden",
                    "type": "yes_no",
                    "label": "Haben Sie Beschwerden wie Fließschnupfen, Niesanfälle, "
                             "brennende Augen, Hustenreiz, Atemnot oder juckende Quaddeln "
                             "auf der Haut?",
                    "required": True,
                },
                {
                    "id": "beschwerden_art",
                    "type": "multi_choice",
                    "label": "Welche Beschwerden haben Sie?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "beschwerden_vorhanden", "in": ["yes"]},
                    "options": [
                        {"value": "fliessschnupfen", "label": "Fließschnupfen (laufende Nase)"},
                        {"value": "niesanfaelle", "label": "Niesanfälle (Niessalven)"},
                        {"value": "augenbrennen", "label": "Brennende, juckende oder gerötete Augen"},
                        {"value": "hustenreiz", "label": "Hustenreiz oder Husten"},
                        {"value": "atemnot", "label": "Atemnot oder Kurzatmigkeit"},
                        {"value": "pfeifen", "label": "Pfeifende Atmung oder Engegefühl in der Brust"},
                        {"value": "urtikaria", "label": "Juckende Quaddeln auf der Haut (Nesselsucht/Urtikaria)"},
                        {"value": "andere", "label": "Andere Beschwerden"},
                    ],
                },
                {
                    "id": "beschwerden_zeitmuster",
                    "type": "choice",
                    "label": "Wann treten die Beschwerden auf?",
                    "required": True,
                    "show_if": {"id": "beschwerden_vorhanden", "in": ["yes"]},
                    "options": [
                        {"value": "ganzjaehrig", "label": "Das ganze Jahr über"},
                        {"value": "saisonal", "label": "Nur zu bestimmten Jahreszeiten (z. B. Pollenflug)"},
                        {"value": "unregelmaessig", "label": "Unregelmäßig / kann ich nicht sagen"},
                    ],
                },
                {
                    "id": "beschwerden_arbeit",
                    "type": "yes_no",
                    "label": "Treten die Beschwerden vermehrt am Arbeitsplatz oder während "
                             "der Arbeit auf?",
                    "required": True,
                    "show_if": {"id": "beschwerden_vorhanden", "in": ["yes"]},
                },
                {
                    "id": "besserung_karenz",
                    "type": "yes_no",
                    "label": "Werden die Beschwerden besser, wenn Sie nicht arbeiten "
                             "(z. B. am arbeitsfreien Wochenende oder im Urlaub)?",
                    "required": True,
                    "show_if": {"id": "beschwerden_vorhanden", "in": ["yes"]},
                },
                {
                    "id": "infekt_husten",
                    "type": "yes_no",
                    "label": "Hatten Sie in den letzten Monaten einen Atemwegsinfekt "
                             "(z. B. Erkältung, Bronchitis), nach dem der Husten über "
                             "Wochen angehalten hat?",
                    "required": True,
                },
                {
                    "id": "kollegen_beschwerden",
                    "type": "yes_no",
                    "label": "Haben auch Kolleginnen oder Kollegen an Ihrem Arbeitsplatz "
                             "ähnliche Atemwegs- oder Augenbeschwerden?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Allergien und Vorerkrankungen ──────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Allergien & Vorerkrankungen",
            "subtitle": "Bekannte Allergien und Erkrankungen der Atemwege",
            "questions": [
                {
                    "id": "allergie_diagnosen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen ärztlich eine der folgenden Erkrankungen "
                             "festgestellt?",
                    "hint": "Mehrfachauswahl möglich. Auch Erkrankungen, die schon länger "
                            "zurückliegen, bitte angeben (ggf. Allergiepass mitbringen).",
                    "required": True,
                    "options": [
                        {"value": "heuschnupfen", "label": "Heuschnupfen / allergischer Schnupfen oder allergische Bindehautentzündung"},
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "neurodermitis", "label": "Neurodermitis (atopisches Ekzem)"},
                        {"value": "sonstige_allergie", "label": "Andere Allergie (z. B. gegen Tiere, Hausstaubmilben, Nahrungsmittel)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "allergie_beruflich",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Allergie gegen Stoffe aus Ihrem "
                             "Arbeitsbereich festgestellt (z. B. Mehl, Tierhaare, Latex), "
                             "oder haben Sie allergische Beschwerden durch Arbeitsstoffe?",
                    "required": True,
                    "followup": {"id": "allergie_beruflich_desc", "type": "text",
                                 "label": "Gegen welche Stoffe?", "when": "yes"},
                },
                {
                    "id": "copd",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine chronische Bronchitis, COPD "
                             "(dauerhafte Verengung der Atemwege) oder ein Lungenemphysem "
                             "(Überblähung der Lunge) festgestellt?",
                    "required": True,
                },
                {
                    "id": "lunge_sonstig",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine andere Erkrankung der Lunge "
                             "(z. B. Lungenfibrose, Sarkoidose, Tuberkulose)?",
                    "required": True,
                    "followup": {"id": "lunge_sonstig_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "familie_allergie",
                    "type": "yes_no",
                    "label": "Gibt es in Ihrer Familie (Eltern, Geschwister, Kinder) "
                             "allergische Erkrankungen wie Heuschnupfen, Asthma oder "
                             "Neurodermitis?",
                    "required": True,
                },
                {
                    "id": "tierkontakt_hobby",
                    "type": "yes_no",
                    "label": "Haben Sie privat regelmäßig Kontakt zu Tieren, Hobbys mit "
                             "Staub- oder Allergenkontakt, oder Schimmel/Feuchtigkeit in "
                             "der Wohnung?",
                    "required": True,
                    "followup": {"id": "tierkontakt_hobby_desc", "type": "text",
                                 "label": "Was genau (Tiere, Hobby, Wohnumfeld)?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Tabakkonsum kann die Atemwege zusätzlich belasten",
            "questions": [
                {
                    "id": "rauchstatus",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "frueher", "label": "Früher geraucht, jetzt nicht mehr"},
                        {"value": "aktuell", "label": "Ja, ich rauche zurzeit"},
                    ],
                    "followup": {"id": "rauchstatus_desc", "type": "text",
                                 "label": "Wie viel etwa pro Tag, und seit wann?",
                                 "when": "aktuell"},
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
    # ── Arbeitsbezug der Beschwerden (Abschnitte 6.3, 7.2.2) ──────────────
    {"wenn": {"beschwerden_arbeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezogene Beschwerden",
     "quelle": "Abschnitte 6.3.1, 7.1 und 7.2.2",
     "befund": "Beschwerden treten vermehrt am Arbeitsplatz auf.",
     "konsequenz": "Verdacht auf arbeitsbedingte Atemwegs-/Schleimhautreaktion: "
                   "Ergänzungsuntersuchungen nach 7.2.2 veranlassen (erweiterte "
                   "Lungenfunktionsdiagnostik, bei sensibilisierenden Stoffen Prick-Test "
                   "und/oder spezifisches IgE auf Arbeitsstoffe). Bei anhaltender "
                   "Exposition kurzfristige weitere Vorsorge ansetzen (6.3.1); frühzeitige "
                   "Expositionskarenz verbessert die Prognose."},
    {"wenn": {"besserung_karenz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezogene Beschwerden",
     "quelle": "Abschnitte 6.3.2 und 7.4",
     "befund": "Besserung der Beschwerden bei Arbeitskarenz (Wochenende/Urlaub) angegeben.",
     "konsequenz": "Expositionsabhängigkeit spricht für eine berufsbedingte "
                   "Inhalationsallergie: allergologische Stufendiagnostik (Prick-Test, "
                   "spezifisches IgE) durchführen. Bei allergischer Rhinitis oder "
                   "allergischem Asthma auf berufsspezifische Allergene "
                   "BK-Anzeige prüfen (7.4)."},
    {"wenn": {"beschwerden_art": ["hustenreiz", "atemnot", "pfeifen"]},
     "schwere": "pruefen",
     "bereich": "Untere Atemwege",
     "quelle": "Abschnitt 7.2.2 (Ergänzende Untersuchungen)",
     "befund": "Husten, Atemnot oder pfeifende Atmung/Engegefühl angegeben.",
     "konsequenz": "Über die Basis-Spirometrie hinaus erweiterte Lungenfunktions"
                   "diagnostik erwägen: Bronchospasmolysetest, Ganzkörperplethysmographie, "
                   "Methacholintest (bronchiale Überempfindlichkeit)."},
    {"wenn": {"beschwerden_art": ["fliessschnupfen", "niesanfaelle", "augenbrennen", "urtikaria"]},
     "schwere": "pruefen",
     "bereich": "Frühsymptome Allergie",
     "quelle": "Abschnitte 6.3.2, 7.2.2 und 7.4.2",
     "befund": "Rhinokonjunktivale Beschwerden bzw. Urtikaria angegeben.",
     "konsequenz": "Mögliche Frühsymptome einer allergischen Atemwegserkrankung: bei "
                   "Exposition gegenüber sensibilisierenden Stoffen Prick-Test und/oder "
                   "spezifisches IgE auf Arbeitsstoffe. Bei bestätigten Frühsymptomen "
                   "Maßnahmen nach 7.4.2 prüfen (Substitution, technische/organisatorische/"
                   "individuelle Schutzmaßnahmen)."},
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"allergie_beruflich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Berufsallergie",
     "quelle": "Abschnitte 7.4, 7.4.2–7.4.4",
     "befund": "Allergie bzw. allergische Beschwerden gegenüber Arbeitsstoffen angegeben.",
     "konsequenz": "Ärztlich prüfen, ob die Tätigkeit ohne gesundheitliche Gefährdung "
                   "ausgeübt werden kann: Maßnahmen nach 7.4.2 (Substitution, "
                   "Expositionsminderung, PSA), verkürzte Vorsorgefristen nach 7.4.3. "
                   "Bleiben die Maßnahmen erfolglos, Tätigkeitswechsel erwägen (7.4.4; "
                   "Mitteilung an den Arbeitgeber nur mit Einwilligung). BK-Anzeige "
                   "prüfen (7.4)."},
    {"wenn": {"allergie_diagnosen": ["asthma"]},
     "schwere": "pruefen",
     "bereich": "Obstruktive Atemwegserkrankung",
     "quelle": "Abschnitte 7.4 und 7.4.2–7.4.4",
     "befund": "Ärztlich festgestelltes Asthma bronchiale angegeben.",
     "konsequenz": "Manifeste obstruktive Atemwegserkrankung ist beurteilungsrelevant: "
                   "aktuellen Schweregrad und Symptomkontrolle klären (erweiterte "
                   "Lungenfunktionsdiagnostik nach 7.2.2). Maßnahmen nach 7.4.2 und "
                   "verkürzte Fristen nach 7.4.3 prüfen; bei Erfolglosigkeit "
                   "Tätigkeitswechsel erwägen (7.4.4)."},
    {"wenn": {"copd": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Obstruktive Atemwegserkrankung",
     "quelle": "Abschnitte 7.4 und 7.4.2–7.4.4",
     "befund": "Chronische Bronchitis, COPD oder Lungenemphysem angegeben.",
     "konsequenz": "Manifeste obstruktive Lungenerkrankung bzw. Lungenemphysem ist "
                   "beurteilungsrelevant (7.4): Lungenfunktion objektivieren, Maßnahmen "
                   "nach 7.4.2 und verkürzte Fristen nach 7.4.3 prüfen; bei erwartbarer "
                   "Änderung des Schweregrads engmaschig kontrollieren, ggf. "
                   "Tätigkeitswechsel erwägen (7.4.4)."},
    {"wenn": {"lunge_sonstig": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lungenerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Sonstige Lungenerkrankung (z. B. Lungengerüsterkrankung) angegeben.",
     "konsequenz": "Erhebliche Erkrankungen der Lunge (z. B. Lungengerüsterkrankungen) "
                   "sind beurteilungsrelevant: Vorbefunde einholen, Lungenfunktion prüfen, "
                   "Beurteilung nach 7.4 mit ggf. Maßnahmen (7.4.2) oder verkürzten "
                   "Fristen (7.4.3)."},
    {"wenn": {"infekt_husten": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bronchiale Überempfindlichkeit",
     "quelle": "Abschnitte 6.4 und 7.4",
     "befund": "Wochenlang anhaltender Husten nach Atemwegsinfekt angegeben.",
     "konsequenz": "Passagere bronchiale Überempfindlichkeit nach Infekt möglich (6.4): "
                   "differenzierte Anamnese zur Abgrenzung von einer beruflich bedingten "
                   "Atemwegserkrankung, Kontrolle nach Abklingen des Infekts. "
                   "Überempfindlichkeit der Bronchien ist beurteilungsrelevant (7.4), da "
                   "schon niedrige Konzentrationen inhalativer Agentien verschlimmern "
                   "können."},
    # ── Betriebliche Häufung, Schutzmaßnahmen (6.4, 8.2) ──────────────────
    {"wenn": {"kollegen_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Betriebliche Häufung",
     "quelle": "Abschnitte 6.4 und 8.2",
     "befund": "Mehrere Beschäftigte am Arbeitsplatz haben ähnliche Beschwerden.",
     "konsequenz": "Verdacht auf relevante atemwegswirksame Exposition erhärtet sich: "
                   "Mitteilung an das Unternehmen, Überprüfung der Gefährdungsbeurteilung "
                   "anregen; neben individualpräventiven auch erweiterte allgemein"
                   "präventive Maßnahmen ergreifen und deren Wirksamkeit engmaschig "
                   "überprüfen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"schutzmassnahmen": ["keine", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Keine besonderen Schutzmaßnahmen bekannt bzw. vorhanden.",
     "konsequenz": "Abgleich mit der Gefährdungsbeurteilung; Beratung zu Vermeidung/"
                   "Minimierung von Inhalation und Hautkontakt, Arbeitshygiene und "
                   "geeigneter PSA (8.1). Reichen die Maßnahmen nicht aus, Mitteilung an "
                   "das Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    # ── Stoffspezifische Zusatzempfehlungen (Abschnitte 2, 6.1) ───────────
    {"wenn": {"stoffgruppen": ["isocyanate", "platinsalze"]},
     "schwere": "hinweis",
     "bereich": "Stoffspezifische Empfehlung",
     "quelle": "Abschnitte 2 und 6.1",
     "befund": "Tätigkeit mit Isocyanaten bzw. Platinsalzen angegeben.",
     "konsequenz": "Zusätzlich die stoffspezifische DGUV Empfehlung »Isocyanate« bzw. "
                   "»Platinverbindungen« anwenden (inkl. dort vorgesehener spezifischer "
                   "Diagnostik)."},
    # ── Disposition und außerberufliche Faktoren (6.3.1, 7.1, 8.1) ────────
    {"wenn": {"allergie_diagnosen": ["heuschnupfen", "neurodermitis", "sonstige_allergie"]},
     "schwere": "hinweis",
     "bereich": "Atopische Disposition",
     "quelle": "Abschnitte 6.1, 6.3.1 und 8.1",
     "befund": "Atopische Erkrankung (Heuschnupfen, Neurodermitis, andere Allergie) angegeben.",
     "konsequenz": "Erhöhtes Erkrankungsrisiko insbesondere bei hochmolekularen Allergenen: "
                   "Beratung zur Bedeutung der Atopie bei der Entstehung allergischer "
                   "Erkrankungen (8.1); bei Exposition gegenüber sensibilisierenden "
                   "Stoffen niederschwellig Prick-Test/spezifisches IgE nach 7.2.2 "
                   "anbieten."},
    {"wenn": {"familie_allergie": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Familiäre Disposition",
     "quelle": "Abschnitt 7.1 (Allergologische Anamnese)",
     "befund": "Allergische Erkrankungen in der Familie angegeben.",
     "konsequenz": "Familiäre Allergieneigung in der allergologischen Anamnese "
                   "berücksichtigen; Beratung zu Frühsymptomen und zum Verhalten bei "
                   "ersten arbeitsplatzbezogenen Beschwerden."},
    {"wenn": {"tierkontakt_hobby": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Außerberufliche Allergenquellen",
     "quelle": "Abschnitt 7.1 (Allergologische Anamnese)",
     "befund": "Private Tierkontakte, Hobbys mit Allergenkontakt oder belastetes Wohnumfeld.",
     "konsequenz": "Außerberufliche Allergenquellen (Tierkontakte, Hobbys, Wohnumfeld) bei "
                   "der Beurteilung und Differenzialdiagnose arbeitsplatzbezogener "
                   "Beschwerden berücksichtigen."},
    {"wenn": {"rauchstatus": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 8.1 (Beratung der versicherten Person)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung zum Rauchverhalten im Rahmen der abschließenden Beratung; "
                   "auf das Zusammenwirken von Tabakrauch und beruflicher "
                   "Atemwegsbelastung sowie Entwöhnungsangebote hinweisen."},
]
