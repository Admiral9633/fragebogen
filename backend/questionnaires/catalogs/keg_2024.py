# -*- coding: utf-8 -*-
"""Krebserzeugende und keimzellmutagene Gefahrstoffe – allgemein – DGUV Empfehlung 2024.
Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen,
1. Auflage 2024, »Krebserzeugende und keimzellmutagene Gefahrstoffe – allgemein«
(E KEG, Fassung Januar 2022), S. 390–413."""

SLUG = "keg-2024"

CATALOG = {
    "version": 2,
    "title": "Krebserzeugende und keimzellmutagene Gefahrstoffe – allgemein (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Krebserzeugende und keimzellmutagene Gefahrstoffe – "
             "allgemein« (E KEG, Fassung Januar 2022), S. 390–413",
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
                    "label": "Um welche arbeitsmedizinische Vorsorge wegen krebserzeugender "
                             "Stoffe handelt es sich heute?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge (vor oder kurz nach Beginn der Tätigkeit)"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich war schon einmal zur Vorsorge)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (die Tätigkeit mit diesen "
                                                         "Stoffen ist bereits beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Bei Tätigkeiten mit krebserzeugenden oder keimzellmutagenen "
                            "(erbgutverändernden) Stoffen der Kategorie 1A/1B muss der Betrieb "
                            "je nach Belastung eine Pflicht- oder Angebotsvorsorge veranlassen.",
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
            "title": "Tätigkeit & Umgang mit Gefahrstoffen",
            "subtitle": "Ihre Arbeit und die Stoffe, mit denen Sie zu tun haben",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "stoffe",
                    "type": "multi_choice",
                    "label": "Mit welchen krebserzeugenden oder keimzellmutagenen Stoffen haben "
                             "Sie bei der Arbeit Kontakt oder Umgang?",
                    "hint": "Mehrfachauswahl möglich. Die Angaben stehen meist in Ihrer "
                            "Unterweisung oder im Sicherheitsdatenblatt.",
                    "required": True,
                    "options": [
                        {"value": "acrylnitril", "label": "Acrylnitril"},
                        {"value": "beryllium", "label": "Beryllium oder seine Verbindungen"},
                        {"value": "butadien", "label": "1,3-Butadien"},
                        {"value": "cobalt", "label": "Cobalt (Kobalt) oder seine Verbindungen"},
                        {"value": "dieselabgase", "label": "Dieselmotor-Abgase (Dieselruß)"},
                        {"value": "dimethylsulfat", "label": "Dimethylsulfat"},
                        {"value": "epichlorhydrin", "label": "Epichlorhydrin"},
                        {"value": "hydrazin", "label": "Hydrazin"},
                        {"value": "zytostatika", "label": "Zytostatika oder andere krebserzeugende "
                                                          "Arzneimittel (z. B. in Apotheke, Klinik, Pflege)"},
                        {"value": "andere", "label": "Andere krebserzeugende Stoffe"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "stoffe_desc",
                    "type": "text",
                    "label": "Falls Sie »Andere krebserzeugende Stoffe« angekreuzt haben: "
                             "Welche Stoffe sind das?",
                    "required": False,
                },
                {
                    "id": "expo_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Führen Sie Arbeiten aus, bei denen die Belastung erhöht sein kann?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "reinigung", "label": "Reinigung von Anlagen, Werkzeugen, Geräten oder Behältern"},
                        {"value": "instandhaltung", "label": "Instandhaltung, Wartung oder Reparatur an Anlagen"},
                        {"value": "stoerungen", "label": "Beseitigung von Betriebsstörungen"},
                        {"value": "probennahme", "label": "Offene Probennahme, Kontroll- oder Überwachungstätigkeiten"},
                        {"value": "abfuellen", "label": "Ab- und Umfüllen von Stoffen"},
                        {"value": "sanierung", "label": "Abbruch- oder Sanierungsarbeiten an belasteten Anlagen"},
                        {"value": "abfall", "label": "Beseitigung von belasteten (kontaminierten) Abfällen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle oder Unfälle mit diesen Stoffen "
                             "(z. B. Verschütten, Leckage, Einatmen von Dämpfen, Hautkontakt)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "betriebszustaende",
                    "type": "yes_no",
                    "label": "Gab es ungewöhnliche Betriebszustände (z. B. Störungen, offene Anlagen, "
                             "starke Staub- oder Dampfentwicklung)?",
                    "required": True,
                    "followup": {"id": "betriebszustaende_desc", "type": "text",
                                 "label": "Welche, und wie oft?", "when": "yes"},
                },
                {
                    "id": "psa",
                    "type": "choice",
                    "label": "Tragen Sie die vorgesehene persönliche Schutzausrüstung "
                             "(z. B. Schutzhandschuhe, Atemschutz, Schutzkleidung)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "keine_vorgesehen", "label": "Für meine Arbeit ist keine vorgesehen"},
                    ],
                },
                {
                    "id": "hygiene",
                    "type": "choice",
                    "label": "Halten Sie die Hygieneregeln am Arbeitsplatz ein (kein Essen und "
                             "Trinken am Arbeitsplatz, gründliches Händewaschen vor Pausen – auch "
                             "vor Raucherpausen –, Wechsel der Arbeitskleidung)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "teilweise", "label": "Teilweise"},
                        {"value": "selten_nie", "label": "Selten oder nie"},
                    ],
                },
                {
                    "id": "fruehere_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit krebserzeugenden "
                             "Gefahrstoffen (z. B. Asbest, Benzol, Schweißrauche, Holzstaub)?",
                    "required": True,
                    "followup": {"id": "fruehere_expo_desc", "type": "textarea",
                                 "label": "Welche Stoffe, welche Tätigkeiten, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "ausserberuflich",
                    "type": "yes_no",
                    "label": "Sind oder waren Sie außerhalb der Arbeit krebserzeugenden Stoffen "
                             "ausgesetzt (z. B. Hobby-Werkstatt, Umgang mit Altöl oder Teer)?",
                    "required": True,
                    "followup": {"id": "ausserberuflich_desc", "type": "text",
                                 "label": "Wodurch?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Nur bei weiteren / nachgehenden Vorsorgen ──────────────────
        {
            "id": "weitere_vorsorge",
            "title": "Seit der letzten Vorsorge",
            "subtitle": "Nur bei weiteren oder nachgehenden Vorsorgen",
            "questions": [
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Läuft bei Ihnen derzeit ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                },
                {
                    "id": "aehnliche_erkrankungen",
                    "type": "yes_no",
                    "label": "Sind bei Kolleginnen oder Kollegen an vergleichbaren Arbeitsplätzen "
                             "gehäuft ähnliche Erkrankungen aufgetreten?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden & Warnzeichen",
            "subtitle": "Beschwerden, auf die bei diesen Stoffen besonders geachtet wird",
            "questions": [
                {
                    "id": "warnzeichen_allgemein",
                    "type": "multi_choice",
                    "label": "Haben Sie eines der folgenden allgemeinen Warnzeichen bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "infekte", "label": "Wiederholt schwere Infektionskrankheiten"},
                        {"value": "wunden", "label": "Schlecht heilende Wunden"},
                        {"value": "gewicht", "label": "Ungewollte starke Gewichtsabnahme"},
                        {"value": "lymphknoten", "label": "Geschwollene Lymphknoten (z. B. am Hals, "
                                                          "in der Achsel oder Leiste)"},
                        {"value": "keine", "label": "Nein, keines davon"},
                    ],
                },
                {
                    "id": "beschwerden_koerper",
                    "type": "multi_choice",
                    "label": "Haben Sie eine der folgenden Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "reizhusten", "label": "Chronischer Reizhusten (dauerhafter trockener Husten)"},
                        {"value": "heiserkeit", "label": "Länger andauernde Heiserkeit"},
                        {"value": "auswurf_blut", "label": "Auswurf (Schleim beim Husten) mit Blutbeimengungen"},
                        {"value": "blut_urin", "label": "Blut im Urin"},
                        {"value": "stuhl_auffaellig", "label": "Stuhlgang von wechselnder Beschaffenheit "
                                                               "mit Blut- oder Schleimbeimengungen"},
                        {"value": "keine", "label": "Nein, keine davon"},
                    ],
                },
                {
                    "id": "haut_schleimhaut",
                    "type": "multi_choice",
                    "label": "Haben Sie Veränderungen an Haut oder Schleimhäuten bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "hautveraenderungen", "label": "Hautveränderungen (z. B. Ekzeme, starke "
                                                                 "Verhornungen, Geschwüre, Pigmentflecken, "
                                                                 "auffällige oder veränderte Muttermale)"},
                        {"value": "schleimhaut", "label": "Veränderungen der Schleimhaut in Mund, Rachen "
                                                          "oder Nase (z. B. weiße Flecken, wunde Stellen)"},
                        {"value": "keine", "label": "Nein, keine davon"},
                    ],
                },
            ],
        },
        # ── 5 ─ Vorgeschichte ──────────────────────────────────────────────
        {
            "id": "vorgeschichte",
            "title": "Vorerkrankungen & Vorgeschichte",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "krebs",
                    "type": "yes_no",
                    "label": "Hatten oder haben Sie eine Krebserkrankung?",
                    "required": True,
                    "followup": {"id": "krebs_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, wann, und wie wurde sie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "praekanzerose",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Krebsvorstufe festgestellt (Präkanzerose, z. B. "
                             "auffällige Gewebeveränderung, die ärztlich als Vorstufe von Krebs "
                             "bezeichnet wurde)?",
                    "required": True,
                    "followup": {"id": "praekanzerose_desc", "type": "text",
                                 "label": "Welche, und wo?", "when": "yes"},
                },
                {
                    "id": "patho_labor",
                    "type": "yes_no",
                    "label": "Wurden bei Ihnen dauerhaft deutlich auffällige Laborwerte festgestellt "
                             "(z. B. Blutbild- oder Leberwerte), die bis heute bestehen?",
                    "required": True,
                    "followup": {"id": "patho_labor_desc", "type": "text",
                                 "label": "Welche Werte, falls bekannt?", "when": "yes"},
                },
                {
                    "id": "immundefekt",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen ein schwerer Immundefekt (stark geschwächte "
                             "körpereigene Abwehr)?",
                    "required": True,
                },
                {
                    "id": "immunsuppression",
                    "type": "yes_no",
                    "label": "Erhalten oder erhielten Sie eine Behandlung, die das Immunsystem "
                             "dauerhaft schwächt (z. B. Immunsuppressiva nach Transplantation, "
                             "Chemotherapie, Kortison in hoher Dauerdosis)?",
                    "required": True,
                    "followup": {"id": "immunsuppression_desc", "type": "text",
                                 "label": "Welche Behandlung, und wann?", "when": "yes"},
                },
                {
                    "id": "strahlen",
                    "type": "yes_no",
                    "label": "Waren Sie früher einer erheblichen Belastung durch ionisierende "
                             "Strahlen ausgesetzt (z. B. Strahlentherapie, häufige Röntgen-"
                             "untersuchungen, beruflicher Strahlenkontakt)?",
                    "required": True,
                    "followup": {"id": "strahlen_desc", "type": "text",
                                 "label": "Wodurch, und wann?", "when": "yes"},
                },
                {
                    "id": "familie",
                    "type": "yes_no",
                    "label": "Kommen in Ihrer Familie gehäuft bösartige Tumorerkrankungen (Krebs) "
                             "oder Erkrankungen des Immunsystems vor?",
                    "required": True,
                },
                {
                    "id": "bk_anerkannt",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen schon einmal eine Berufskrankheit anerkannt?",
                    "required": True,
                    "followup": {"id": "bk_anerkannt_desc", "type": "text",
                                 "label": "Welche?", "when": "yes"},
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
                    "id": "schwanger_stillend",
                    "type": "choice",
                    "label": "Sind Sie derzeit schwanger, oder stillen Sie? "
                             "(Diese Frage betrifft nur Frauen.)",
                    "hint": "Für Schwangere und Stillende gelten beim Umgang mit krebserzeugenden "
                            "Stoffen besondere Beschäftigungsbeschränkungen (Mutterschutzgesetz).",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ja_schwanger", "label": "Ja, ich bin schwanger"},
                        {"value": "ja_stillend", "label": "Ja, ich stille"},
                        {"value": "entfaellt", "label": "Trifft auf mich nicht zu"},
                    ],
                },
            ],
        },
        # ── 6 ─ Rauchen & Alkohol ──────────────────────────────────────────
        {
            "id": "noxen",
            "title": "Rauchen & Alkohol",
            "subtitle": "Angaben laut DGUV Empfehlung (Rauch- und Alkoholanamnese)",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "frueher", "label": "Früher, ich habe aufgehört"},
                        {"value": "ja", "label": "Ja, ich rauche"},
                    ],
                },
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Trinken Sie Alkohol?",
                    "required": True,
                    "options": [
                        {"value": "nie_selten", "label": "Nie oder sehr selten"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche)"},
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
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"krebs": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Krebserkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Durchgemachte oder bestehende Krebserkrankung angegeben.",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Tätigkeit im Einzelfall klären, ob die "
                   "Tätigkeit ohne gesundheitliche Gefährdung möglich ist (7.4). Maßnahmen nach "
                   "7.4.2 prüfen (Substitution, technische/organisatorische Schutzmaßnahmen, "
                   "Einsatz an Arbeitsplätzen mit geringerer Exposition, PSA), verkürzte "
                   "Vorsorgefristen nach 7.4.3; ohne Aussicht auf Erfolg Tätigkeitswechsel nach "
                   "7.4.4 erwägen (Mitteilung an den Arbeitgeber nur mit Einwilligung, "
                   "§ 6 (4) ArbMedVV)."},
    {"wenn": {"immundefekt": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Immunsystem",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Schwerer Immundefekt angegeben.",
     "konsequenz": "Einzelfallprüfung nach 7.4, ob die Tätigkeit ohne gesundheitliche Gefährdung "
                   "ausgeübt werden kann; Vorbefunde einholen. Maßnahmen nach 7.4.2 und "
                   "verkürzte Vorsorgefristen nach 7.4.3 prüfen; ggf. Tätigkeitswechsel nach "
                   "7.4.4 erwägen."},
    {"wenn": {"praekanzerose": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Präkanzerose",
     "quelle": "Abschnitte 7.4 und 8.1",
     "befund": "Krebsvorstufe (Präkanzerose) in der Vorgeschichte angegeben.",
     "konsequenz": "Befunde und Vorbefunde einholen, fachärztliche Abklärung bzw. Verlaufs-"
                   "kontrolle sicherstellen (8.1). Beurteilung nach 7.4: Maßnahmen nach 7.4.2 "
                   "und verkürzte Vorsorgefristen nach 7.4.3 prüfen."},
    {"wenn": {"immunsuppression": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Immunsystem",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Therapie, die das Immunsystem nachhaltig schwächt, angegeben.",
     "konsequenz": "Medikamenten- und Therapieanamnese ärztlich vertiefen; Beurteilung nach 7.4, "
                   "ob die Tätigkeit ohne gesundheitliche Gefährdung möglich ist. Maßnahmen nach "
                   "7.4.2 bzw. verkürzte Vorsorgefristen nach 7.4.3 prüfen."},
    {"wenn": {"patho_labor": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Laborbefunde",
     "quelle": "Abschnitte 7.4 und 8.1",
     "befund": "Fortbestehende, deutlich auffällige Laborwerte angegeben.",
     "konsequenz": "Vorbefunde anfordern und Laborkontrolle veranlassen (7.2.2). Bei fortbestehend "
                   "eindeutig pathologischen Werten weiterführende fachärztliche Untersuchungen "
                   "(z. B. hämatologisch, biochemisch, sonographisch, endoskopisch) nach 8.1; "
                   "Beurteilung nach 7.4."},
    # ── Mutterschutz (Abschnitt 8.1, Beratung) ────────────────────────────
    {"wenn": {"schwanger_stillend": ["ja_schwanger", "ja_stillend"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 8.1 (Beschäftigungsbeschränkungen nach MuSchG)",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben.",
     "konsequenz": "Beschäftigungsbeschränkungen für werdende und stillende Mütter beim Umgang "
                   "mit krebserzeugenden/keimzellmutagenen Gefahrstoffen unverzüglich klären "
                   "(Mutterschutzgesetz i. V. m. angrenzendem Regelwerk); Tätigkeits- bzw. "
                   "Arbeitsplatzanpassung vor weiterer Exposition veranlassen und die "
                   "versicherte Person entsprechend beraten."},
    # ── Beschwerden / Warnzeichen (Abschnitte 7.1, 7.2.2, 8.1) ────────────
    {"wenn": {"warnzeichen_allgemein": ["infekte", "wunden", "gewicht", "lymphknoten"]},
     "schwere": "pruefen",
     "bereich": "Allgemeine Warnzeichen",
     "quelle": "Abschnitte 7.1 (Beschwerden), 7.2.2 und 8.1",
     "befund": "Allgemeine Warnzeichen angegeben (schwere Infekte, schlecht heilende Wunden, "
               "ungewollte Gewichtsabnahme oder Lymphknotenschwellung).",
     "konsequenz": "Ärztliche Abklärung veranlassen: zielorganspezifische Untersuchungen nach "
                   "7.2.2 (z. B. großes Blutbild, BSG oder CRP); in unklaren Fällen "
                   "weiterführende fachärztliche Untersuchungen nach 8.1."},
    {"wenn": {"beschwerden_koerper": ["reizhusten", "heiserkeit", "auswurf_blut"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 7.2.2",
     "befund": "Chronischer Reizhusten, länger andauernde Heiserkeit oder blutiger Auswurf "
               "angegeben.",
     "konsequenz": "Zielorganbezogene Abklärung: Spirometrie; ggf. radiologische Diagnostik des "
                   "Thorax bei rechtfertigender Indikation (7.2.2); bei anhaltenden Beschwerden "
                   "fachärztliche (pneumologische/HNO-ärztliche) Vorstellung nach 8.1."},
    {"wenn": {"beschwerden_koerper": ["blut_urin", "stuhl_auffaellig"]},
     "schwere": "pruefen",
     "bereich": "Harnwege/Verdauungstrakt",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 8.1",
     "befund": "Blut im Urin bzw. Stuhlveränderungen mit Blut- oder Schleimbeimengungen "
               "angegeben.",
     "konsequenz": "Gezielte fachärztliche Abklärung veranlassen (z. B. urologisch bzw. "
                   "endoskopisch) nach 8.1; Ergebnis bei der Beurteilung nach 7.4 "
                   "berücksichtigen."},
    {"wenn": {"haut_schleimhaut": ["hautveraenderungen", "schleimhaut"]},
     "schwere": "pruefen",
     "bereich": "Haut/Schleimhaut",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 8.1",
     "befund": "Haut- oder Schleimhautveränderungen angegeben (z. B. Ekzeme, Hyperkeratosen, "
               "Ulzerationen, Pigmentstörungen, Naevi, Schleimhautveränderungen in Mund, "
               "Rachen oder Nase).",
     "konsequenz": "Inspektion und dermatologische bzw. HNO-ärztliche Abklärung auf Präkanzerosen "
                   "veranlassen (8.1); Ergebnis bei der Beurteilung nach 7.4 berücksichtigen."},
    # ── Exposition und Arbeitsschutz (Abschnitte 6.4, 7.1, 8.2) ───────────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Expositionsereignis",
     "quelle": "Abschnitte 7.1 (Arbeitsanamnese), 6.4 und 8.2",
     "befund": "Zwischenfall oder Unfall mit krebserzeugenden/keimzellmutagenen Stoffen "
               "angegeben.",
     "konsequenz": "Ereignis dokumentieren und mit der Gefährdungsbeurteilung abgleichen; "
                   "Biomonitoring nach 6.4 erwägen (Äquivalenzwerte TRGS 910, BAT/EKA/BLW). "
                   "Ergeben sich Anhaltspunkte für unzureichende Schutzmaßnahmen, Mitteilung an "
                   "das Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV, 8.2)."},
    {"wenn": {"betriebszustaende": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Betriebszustände",
     "quelle": "Abschnitte 7.1 (Arbeitsanamnese) und 8.2",
     "befund": "Ungewöhnliche Betriebszustände angegeben.",
     "konsequenz": "Angaben dokumentieren (7.1); Überprüfung der Gefährdungsbeurteilung durch "
                   "das Unternehmen anregen und ggf. Schutzmaßnahmen vorschlagen (8.2)."},
    {"wenn": {"aehnliche_erkrankungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Erkrankungshäufung",
     "quelle": "Abschnitte 7.1 (weitere Vorsorgen) und 8.2",
     "befund": "Gehäuftes Auftreten ähnlicher Erkrankungen an vergleichbaren Arbeitsplätzen "
               "angegeben.",
     "konsequenz": "Anhaltspunkt für unzureichende Maßnahmen des Arbeitsschutzes: Häufung "
                   "dokumentieren, dem Unternehmen mitteilen und Schutzmaßnahmen vorschlagen "
                   "(§ 6 (4) ArbMedVV, 8.2); Überprüfung der Gefährdungsbeurteilung veranlassen."},
    {"wenn": {"psa": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzausrüstung",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA und zu den krebserzeugenden "
                   "Wirkungen der Arbeitsstoffe (8.1); Ursachen klären. Reichen die Maßnahmen "
                   "des Arbeitsschutzes erkennbar nicht aus, Mitteilung an das Unternehmen und "
                   "Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV, 8.2)."},
    {"wenn": {"hygiene": ["teilweise", "selten_nie"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 (Beratung) und 8.1",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht durchgehend eingehalten.",
     "konsequenz": "Beratung zu Hygienemaßnahmen: kein Essen und Trinken am Arbeitsplatz, "
                   "gründliches Händewaschen vor den Pausen – besonders vor Raucherpausen –, "
                   "Wechsel der Arbeitskleidung (7.1, 8.1)."},
    {"wenn": {"fruehere_expo": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 2 (nachgehende Vorsorge) und 7.1 (Arbeitsanamnese)",
     "befund": "Frühere berufliche Belastung durch krebserzeugende Gefahrstoffe angegeben.",
     "konsequenz": "Frühere Expositionen dokumentieren und bei der Beurteilung berücksichtigen; "
                   "Anspruch auf nachgehende Vorsorge klären und Anmeldung über das Meldeportal "
                   "»DGUV Vorsorge« (www.dguv-vorsorge.de) anregen; auf das "
                   "Expositionsverzeichnis nach TRGS 410 hinweisen."},
    {"wenn": {"rauchen": ["ja"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 7.1 (Rauchverhalten) und 8.1",
     "befund": "Aktives Rauchen angegeben.",
     "konsequenz": "Beratung zum Rauchverhalten und zum kombinierten Krebsrisiko mit den "
                   "Arbeitsstoffen; auf gründliches Händewaschen besonders vor Raucherpausen "
                   "hinweisen (Verschleppungsgefahr von Gefahrstoffen); Tabakentwöhnung "
                   "empfehlen."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "BK-Verfahren",
     "quelle": "Abschnitte 7.1 (weitere Vorsorgen) und 6.5",
     "befund": "Laufendes Berufskrankheiten-Verfahren angegeben.",
     "konsequenz": "Verfahren dokumentieren, vorhandene Befunde mit Einwilligung einbeziehen; "
                   "Meldepflichten und Informationen über das DGUV Portal »BK-Info« beachten "
                   "(6.5)."},
    {"wenn": {"strahlen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Strahlenexposition",
     "quelle": "Abschnitt 7.1 (Allgemeine Anamnese)",
     "befund": "Frühere therapeutische oder sonstige erhebliche Exposition gegenüber "
               "ionisierenden Strahlen angegeben.",
     "konsequenz": "Strahlenanamnese dokumentieren und als zusätzlichen Risikofaktor bei "
                   "Beurteilung (7.4) und Beratung (8.1) berücksichtigen; Zurückhaltung bei "
                   "zusätzlicher radiologischer Diagnostik (rechtfertigende Indikation, 7.2.2)."},
]
