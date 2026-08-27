# -*- coding: utf-8 -*-
"""
G 24 Hauterkrankungen (mit Ausnahme von Hautkrebs) – DGUV Grundsatz 2016.

Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen,
6. Auflage 2016, G 24 (Fassung Oktober 2014), S. 367–376.

Anamnese-Fragen, die die untersuchte Person selbst beantworten kann
(Tätigkeit/Exposition, Präventionsmaßnahmen, Beschwerden, Vorerkrankungen),
plus datengetriebene Auswertungsregeln nach Abschnitt 1 (Untersuchungen,
Fristen), Abschnitt 2 (Beurteilung: dauernde/befristete gesundheitliche
Bedenken, Hautarztverfahren) und Abschnitt 3 (Ergänzende Hinweise).
"""

SLUG = "g24-haut-2016"

CATALOG = {
    "version": 2,
    "title": "G 24 Hauterkrankungen (DGUV Grundsatz 2016)",
    "basis": (
        "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, "
        "6. Auflage 2016, G 24 „Hauterkrankungen (mit Ausnahme von "
        "Hautkrebs)“ (Fassung Oktober 2014), S. 367–376"
    ),
    "sections": [
        # ── 1 ─────────────────────────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Untersuchungsanlass",
            "subtitle": "Erst- oder Nachuntersuchung nach G 24",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich heute?",
                    "required": True,
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der hautbelastenden "
                            "Tätigkeit statt.",
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach1", "label": "Erste Nachuntersuchung"},
                        {"value": "nach_weitere", "label": "Weitere Nachuntersuchung"},
                    ],
                },
                {
                    "id": "beschwerden_anlass",
                    "type": "yes_no",
                    "label": "Kommen Sie vorzeitig zur Untersuchung, weil Hautveränderungen "
                             "oder Beschwerden aufgetreten sind?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach1", "nach_weitere"]},
                },
            ],
        },
        # ── 2 ─────────────────────────────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Exposition",
            "subtitle": "Womit Ihre Haut bei der Arbeit in Kontakt kommt",
            "questions": [
                {
                    "id": "feuchtarbeit",
                    "type": "yes_no",
                    "label": "Arbeiten Sie regelmäßig mit nassen oder feuchten Händen, oder "
                             "müssen Sie Ihre Hände bei der Arbeit häufig waschen oder "
                             "desinfizieren (Feuchtarbeit)?",
                    "required": True,
                },
                {
                    "id": "handschuhe_dicht",
                    "type": "yes_no",
                    "label": "Tragen Sie bei der Arbeit regelmäßig Gummihandschuhe, "
                             "flüssigkeitsdichte Schutzhandschuhe oder Gummistiefel?",
                    "required": True,
                    "hint": "Darunter stauen sich Wärme und Feuchtigkeit – das belastet die Haut.",
                },
                {
                    "id": "stoffe_irritativ",
                    "type": "multi_choice",
                    "label": "Mit welchen hautreizenden (irritativ wirkenden) Stoffen kommen "
                             "Ihre Hände bei der Arbeit in Kontakt?",
                    "required": True,
                    "options": [
                        {"value": "loesemittel", "label": "Lösemittel, Benzine, Petroleum"},
                        {"value": "alkalisch", "label": "Alkalische Substanzen (Laugen, Zement, starke Reiniger)"},
                        {"value": "kss", "label": "Kühlschmierstoffe (Bohr-/Schneidwasser)"},
                        {"value": "oele", "label": "Technische Öle und Fette"},
                        {"value": "detergenzien", "label": "Detergenzien (Wasch- und Spülmittel, Tenside)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "stoffe_sens",
                    "type": "multi_choice",
                    "label": "Mit welchen dieser Stoffe, die Allergien auslösen können "
                             "(sensibilisierende Stoffe), haben Sie bei der Arbeit Kontakt?",
                    "required": True,
                    "options": [
                        {"value": "kunstharze", "label": "Nicht ausgehärtete Kunstharze (Acrylat-/Epoxidharze, Aminhärter, Isocyanate)"},
                        {"value": "latex_gummi", "label": "Latex oder Gummi-Inhaltsstoffe"},
                        {"value": "biozide", "label": "Konservierungsstoffe / Desinfektionsmittel (Biozide)"},
                        {"value": "duft", "label": "Aroma- und Duftstoffe"},
                        {"value": "metalle", "label": "Metalle wie Chrom, Kobalt, Nickel"},
                        {"value": "friseurchemie", "label": "Friseurchemikalien (z.B. Haarfarben)"},
                        {"value": "sonstige", "label": "Kühlschmierstoff-Zusätze, Pflanzen, tropische Hölzer, Proteine"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "physikalisch",
                    "type": "multi_choice",
                    "label": "Welche mechanischen oder physikalischen Belastungen wirken bei "
                             "der Arbeit auf Ihre Haut?",
                    "required": True,
                    "options": [
                        {"value": "fasern", "label": "Mineral- oder Keramikfasern (z.B. Dämmwolle)"},
                        {"value": "spaene", "label": "Metallspäne"},
                        {"value": "abrasiv", "label": "Scheuernde Partikel (z.B. Handwaschpaste mit Reibekörpern)"},
                        {"value": "rau", "label": "Raue Oberflächen, starke Reibung"},
                        {"value": "haare", "label": "Haare (z.B. Friseurhandwerk, Tierhaltung)"},
                        {"value": "strahlen", "label": "Strahlung (z.B. UV-Licht, Schweißen)"},
                        {"value": "hitze_kaelte", "label": "Hitze oder Kälte"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "aknegen",
                    "type": "yes_no",
                    "label": "Haben Sie Kontakt mit Stoffen, die Akne auslösen können "
                             "(z.B. chlorierte Kohlenwasserstoffe, Teeröle)?",
                    "required": True,
                },
                {
                    "id": "mikroorganismen",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit Kontakt mit möglicherweise "
                             "ansteckendem Material (z.B. Pflege, Abwasser, Abfall, Tiere)?",
                    "required": True,
                    "hint": "Manche Krankheitserreger können die Haut direkt angreifen.",
                },
            ],
        },
        # ── 3 ─────────────────────────────────────────────────────────────
        {
            "id": "praevention",
            "title": "Hautschutz im Arbeitsalltag",
            "subtitle": "Zwischenanamnese: tatsächlich durchgeführte Präventionsmaßnahmen",
            "questions": [
                {
                    "id": "schutz_nutzung",
                    "type": "multi_choice",
                    "label": "Welche Hautschutzmaßnahmen nutzen Sie bei der Arbeit "
                             "tatsächlich regelmäßig?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach1", "nach_weitere"]},
                    "options": [
                        {"value": "schutzhandschuhe", "label": "Schutzhandschuhe"},
                        {"value": "hautschutz", "label": "Hautschutzmittel (Creme vor der Arbeit)"},
                        {"value": "reinigung", "label": "Schonende Hautreinigungsmittel"},
                        {"value": "desinfektion", "label": "Händedesinfektion statt häufigem Waschen"},
                        {"value": "pflege", "label": "Hautpflegemittel (Creme nach der Arbeit)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "schutz_probleme",
                    "type": "yes_no",
                    "label": "Vertragen Sie Ihre Schutzhandschuhe oder die Hautmittel "
                             "schlecht, oder kommen Sie damit bei der Arbeit nicht zurecht?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach1", "nach_weitere"]},
                    "followup": {"id": "schutz_probleme_desc", "type": "textarea",
                                 "label": "Was vertragen Sie nicht bzw. was stört Sie?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 4 ─────────────────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Hautbeschwerden",
            "subtitle": "Aktuelle und frühere Hautveränderungen",
            "questions": [
                {
                    "id": "haut_aktuell",
                    "type": "yes_no",
                    "label": "Haben Sie zurzeit Hautveränderungen an Händen, Unterarmen "
                             "oder im Gesicht (z.B. Rötung, Juckreiz, Bläschen, Schuppung, "
                             "Risse, sehr trockene raue Haut)?",
                    "required": True,
                    "followup": {"id": "haut_aktuell_desc", "type": "textarea",
                                 "label": "Wo genau, und seit wann?",
                                 "when": "yes"},
                },
                {
                    "id": "arbeitsbezug",
                    "type": "choice",
                    "label": "Bessern sich diese Hautveränderungen an freien Tagen, am "
                             "Wochenende oder im Urlaub?",
                    "required": True,
                    "show_if": {"id": "haut_aktuell", "in": ["yes"]},
                    "options": [
                        {"value": "ja", "label": "Ja, deutlich"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "weiss_nicht", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "handekzem",
                    "type": "yes_no",
                    "label": "Hatten Sie jemals ein Handekzem (juckenden, geröteten, "
                             "nässenden oder schuppenden Hautausschlag an den Händen)?",
                    "required": True,
                },
                {
                    "id": "ekzem_verlauf",
                    "type": "choice",
                    "label": "Wie ist das Handekzem verlaufen?",
                    "required": True,
                    "show_if": {"id": "handekzem", "in": ["yes"]},
                    "options": [
                        {"value": "einmalig", "label": "Einmalig und wieder abgeheilt"},
                        {"value": "wiederholt", "label": "Mehrmals aufgetreten (immer wieder zurückgekommen)"},
                        {"value": "schwer", "label": "Schwer oder lang anhaltend (z.B. mit Krankschreibung oder Klinikbehandlung)"},
                    ],
                },
                {
                    "id": "beugeekzem",
                    "type": "yes_no",
                    "label": "Hatten Sie Ekzeme auf beiden Seiten in den Ellenbeugen oder "
                             "Kniekehlen (symmetrische Beugeekzeme)?",
                    "required": True,
                    "hint": "Beugeekzeme sind ein typisches Zeichen für Neurodermitis-Veranlagung.",
                },
                {
                    "id": "dyshidrose",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal kleine, stark juckende Bläschen an "
                             "Handflächen, Fingerseiten oder Fußsohlen (Dyshidrose)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─────────────────────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Veranlagung",
            "subtitle": "Allergien, Hauterkrankungen und Hautempfindlichkeit",
            "questions": [
                {
                    "id": "kontaktallergie",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Kontaktallergie bekannt (z.B. auf Nickel, "
                             "Duftstoffe, Gummizusätze, Epoxidharz, Haarfarbe)?",
                    "required": True,
                    "followup": {"id": "kontaktallergie_desc", "type": "text",
                                 "label": "Auf welche Stoffe reagieren Sie allergisch?",
                                 "when": "yes"},
                },
                {
                    "id": "allergie_arbeit",
                    "type": "yes_no",
                    "label": "Kommen Sie bei der Arbeit mit einem Stoff in Kontakt, auf den "
                             "Sie allergisch sind – ohne dass sich dieser Kontakt vermeiden "
                             "lässt?",
                    "required": True,
                    "show_if": {"id": "kontaktallergie", "in": ["yes"]},
                },
                {
                    "id": "atopisches_ekzem",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Neurodermitis (atopisches Ekzem) – auch "
                             "als Kind oder Jugendliche/r?",
                    "required": True,
                },
                {
                    "id": "atopie_sonst",
                    "type": "yes_no",
                    "label": "Haben Sie Heuschnupfen, allergischen Schnupfen oder "
                             "allergisches Asthma?",
                    "required": True,
                    "hint": "Diese Angaben fließen in den Atopie-Score ein (Veranlagung zu "
                            "empfindlicher Haut).",
                },
                {
                    "id": "trockene_haut",
                    "type": "yes_no",
                    "label": "Haben Sie von Natur aus auffallend trockene, empfindliche "
                             "Haut (Xerosis cutis)?",
                    "required": True,
                },
                {
                    "id": "lichtempfindlich",
                    "type": "yes_no",
                    "label": "Ist Ihre Haut besonders lichtempfindlich, oder bekommen Sie "
                             "schnell Hautausschläge durch Sonne?",
                    "required": True,
                },
                {
                    "id": "psoriasis",
                    "type": "yes_no",
                    "label": "Haben Sie Schuppenflechte (Psoriasis)?",
                    "required": True,
                },
                {
                    "id": "psoriasis_haende",
                    "type": "yes_no",
                    "label": "Tritt die Schuppenflechte auch an den Händen oder an "
                             "Hautstellen auf, die bei der Arbeit gedrückt oder gerieben "
                             "werden?",
                    "required": True,
                    "show_if": {"id": "psoriasis", "in": ["yes"]},
                },
                {
                    "id": "haut_sonstige",
                    "type": "yes_no",
                    "label": "Haben Sie eine andere Hauterkrankung (z.B. Ichthyose / "
                             "erbliche Verhornungsstörung)?",
                    "required": True,
                    "followup": {"id": "haut_sonstige_desc", "type": "text",
                                 "label": "Welche Hauterkrankung?",
                                 "when": "yes"},
                },
                {
                    "id": "beruf_hauterkrankung",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen schon einmal eine berufsbedingte "
                             "Hauterkrankung festgestellt oder gemeldet, oder haben Sie "
                             "hautbelastende Tätigkeiten früher schlecht vertragen?",
                    "required": True,
                    "followup": {"id": "beruf_hauterkrankung_desc", "type": "textarea",
                                 "label": "Was war das, und wann?",
                                 "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie selbst einen Zusammenhang zwischen Ihren "
                             "Hautproblemen und Ihrer Arbeit?",
                    "required": True,
                },
            ],
        },
        # ── 6 ─────────────────────────────────────────────────────────────
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
    # ── Fristen (Abschnitt 1.1) ──────────────────────────────────────────
    {"wenn": {"untersuchung_art": ["erst"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "G 24, Abschnitt 1.1",
     "befund": "Erstuntersuchung vor Aufnahme der Tätigkeit",
     "konsequenz": "Erste Nachuntersuchung innerhalb von 24 Monaten veranlassen. Vorzeitige "
                   "Nachuntersuchung bei arbeitsplatzbezogenen Hautveränderungen/Beschwerden, "
                   "nach ärztlichem Ermessen oder wenn Beschäftigte einen Zusammenhang mit "
                   "der Tätigkeit vermuten."},
    {"wenn": {"untersuchung_art": ["nach1", "nach_weitere"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "G 24, Abschnitt 1.1",
     "befund": "Nachuntersuchung",
     "konsequenz": "Weitere Nachuntersuchung innerhalb von 60 Monaten veranlassen; bei "
                   "auffälligem Befund verkürzte Nachuntersuchungsfristen festlegen (2.1.3). "
                   "Vorzeitig bei Hautveränderungen/Beschwerden oder vermutetem "
                   "Zusammenhang mit der Tätigkeit."},
    {"wenn": {"beschwerden_anlass": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Fristen",
     "quelle": "G 24, Abschnitt 1.1 / Abschnitt 2",
     "befund": "Vorzeitige Nachuntersuchung wegen Hautveränderungen/Beschwerden",
     "konsequenz": "Gezielte Untersuchung der exponierten Hautareale; bei Möglichkeit einer "
                   "beruflichen Verursachung Hautarztverfahren (F 6050) bzw. "
                   "Betriebsärztlichen Gefährdungsbericht Haut (F 6060/5101) einleiten."},
    # ── Befund / Untersuchung (Abschnitte 1.2, 2) ────────────────────────
    {"wenn": {"haut_aktuell": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautbefund",
     "quelle": "G 24, Abschnitt 1.2.2 / Abschnitt 2",
     "befund": "Aktuelle Hautveränderungen an Händen, Unterarmen oder Gesicht",
     "konsequenz": "Spezielle Untersuchung der exponierten Hautareale (Hände, Unterarme, "
                   "Gesicht) – Augenmerk auf trockene Haut, Hyperhidrose, Ekzemherde. In "
                   "unklaren Fällen: Erweiterung der körperlichen Untersuchung, Vorbefunde "
                   "und Expositionsdaten heranziehen, gezielte dermatologische Diagnostik "
                   "(Ergänzungsuntersuchung) veranlassen. Bei möglicher beruflicher "
                   "Verursachung Hautarztverfahren (F 6050) einleiten."},
    {"wenn": {"arbeitsbezug": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug",
     "quelle": "G 24, Abschnitt 2 / DGUV Information 250-005",
     "befund": "Hautveränderungen bessern sich in arbeitsfreier Zeit",
     "konsequenz": "Hinweis auf berufliche Verursachung: Hautarztverfahren (F 6050) bzw. "
                   "Betriebsärztlichen Gefährdungsbericht Haut (F 6060/5101) veranlassen; "
                   "dem Arbeitgeber die Aktualisierung der Gefährdungsbeurteilung "
                   "mitteilen (Wahrung der schutzwürdigen Belange beachten, 2.2)."},
    {"wenn": {"ekzem_verlauf": ["wiederholt", "schwer"]},
     "schwere": "kritisch",
     "bereich": "Ekzem",
     "quelle": "G 24, Abschnitt 2.1.1 / 2.1.3 / Abschnitt 4",
     "befund": "Schwere oder wiederholt rückfällige Ekzeme der exponierten Hautareale "
               "(auch anamnestisch)",
     "konsequenz": "Dauernde gesundheitliche Bedenken prüfen (2.1.1). Bei weniger "
                   "ausgeprägtem Befund: keine Bedenken nur unter bestimmten "
                   "Voraussetzungen – technische/organisatorische und persönliche "
                   "Schutzmaßnahmen plus verkürzte Nachuntersuchungsfristen (2.1.3). "
                   "Bei Zwang zur Tätigkeitsaufgabe nach Ausschöpfung aller Präventions- "
                   "und Therapiemaßnahmen BK-Anzeige (F 6000) erstatten – BK-Nr. 5101."},
    {"wenn": {"dyshidrose": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ekzem",
     "quelle": "G 24, Abschnitt 1.2.1 / 1.2.2",
     "befund": "Dyshidrose (Bläschen im Palmoplantarbereich) angegeben",
     "konsequenz": "Untersuchung der Hände; in unklaren Fällen gezielte dermatologische "
                   "Diagnostik als Ergänzungsuntersuchung veranlassen."},
    {"wenn": {"beugeekzem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Disposition",
     "quelle": "G 24, Abschnitt 1.2.1 (Atopie-Score)",
     "befund": "Symmetrische Beugeekzeme (Hinweis auf atopische Hautdiathese)",
     "konsequenz": "Atopische Hautdiathese gemäß Atopie-Score bewerten; Disposition bei "
                   "Beurteilung und Beratung berücksichtigen, ggf. dermatologische "
                   "Abklärung in unklaren Fällen."},
    # ── Allergie (Abschnitt 2.1) ─────────────────────────────────────────
    {"wenn": {"allergie_arbeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Allergie",
     "quelle": "G 24, Abschnitt 2.1.1 / 2.1.3",
     "befund": "Allergische Hauterkrankung, berufliche Allergenexposition nicht vermeidbar",
     "konsequenz": "Dauernde gesundheitliche Bedenken (2.1.1). Bei weniger ausgeprägter "
                   "Erkrankung prüfen, ob Aufnahme/Fortsetzung der Tätigkeit unter "
                   "besonderen Schutzmaßnahmen und verkürzten Nachuntersuchungsfristen "
                   "möglich ist (2.1.3); Hautarztverfahren (F 6050) einleiten."},
    {"wenn": {"kontaktallergie": ["yes"]},
     "wenn_nicht": {"allergie_arbeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allergie",
     "quelle": "G 24, Abschnitt 1.2.1",
     "befund": "Bekannte Kontaktallergie ohne (bekannten) unvermeidbaren Arbeitskontakt",
     "konsequenz": "Auslösendes Allergen dokumentieren und mit den Arbeitsstoffen "
                   "abgleichen; bei relevantem beruflichem Kontakt Karenz und "
                   "Schutzmaßnahmen festlegen. Prophetische Allergietestungen sind nicht "
                   "indiziert (1.2.1)."},
    # ── Disposition (Abschnitte 1.2.1, 2.1) ──────────────────────────────
    {"wenn": {"atopisches_ekzem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Disposition",
     "quelle": "G 24, Abschnitt 2.1.1 / 2.1.3",
     "befund": "Atopisches Ekzem (Neurodermitis), auch anamnestisch",
     "konsequenz": "Erhebliche Minderbelastbarkeit der Haut prüfen: bei atopischem Ekzem "
                   "der exponierten Hautareale dauernde gesundheitliche Bedenken möglich "
                   "(2.1.1); bei geringer Ausprägung keine Bedenken nur unter "
                   "Schutzmaßnahmen und verkürzten Nachuntersuchungsfristen (2.1.3)."},
    {"wenn": {"psoriasis_haende": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Disposition",
     "quelle": "G 24, Abschnitt 2.1.1 / 2.1.2",
     "befund": "Psoriasis an den Händen bzw. an mechanisch belasteten Hautstellen "
               "(möglicher Köbner-Effekt)",
     "konsequenz": "Bei floridem Befund an belasteten Arealen befristete gesundheitliche "
                   "Bedenken (2.1.2): erneute arbeitsmedizinische Beurteilung nach "
                   "Abheilung. Bei erheblicher Minderbelastbarkeit (rezidivierende "
                   "Psoriasis mit Köbner-Effekt) dauernde Bedenken prüfen (2.1.1)."},
    {"wenn": {"trockene_haut": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Disposition",
     "quelle": "G 24, Abschnitt 1.2.1 / 2.2",
     "befund": "Xerosis cutis (auffallend trockene, empfindliche Haut)",
     "konsequenz": "Disposition dokumentieren; individuelle Beratung zu Hautschutz und "
                   "Hautpflege entsprechend der Hautkonstitution (2.2)."},
    {"wenn": {"lichtempfindlich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Disposition",
     "quelle": "G 24, Abschnitt 1.2.1 / 2.1.1",
     "befund": "Erhöhte Lichtempfindlichkeit angegeben",
     "konsequenz": "Bei Beschäftigung mit unvermeidbarer UV-Exposition an UV-induzierte "
                   "Dermatosen denken (dauernde Bedenken nach 2.1.1 möglich); Beratung "
                   "zum Lichtschutz."},
    {"wenn": {"aknegen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Exposition",
     "quelle": "G 24, Abschnitt 3.1.1 (Sonstige Einwirkungen)",
     "befund": "Kontakt mit Stoffen mit aknegener Potenz (z.B. chlorierte polycyklische "
               "Kohlenwasserstoffe)",
     "konsequenz": "Bei der Untersuchung auf Öl-/Chlorakne achten; Expositionsminderung "
                   "und Hautschutz beraten."},
    {"wenn": {"mikroorganismen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Exposition",
     "quelle": "G 24, Abschnitt 3.1.1 (Sonstige Einwirkungen)",
     "befund": "Kontakt mit hautpathogenen Mikroorganismen möglich",
     "konsequenz": "Hygiene- und Schutzmaßnahmen beraten; an BK-Nrn. 3101/3102 denken."},
    # ── Prävention / Beratung (Abschnitte 1.2.1, 2.2) ────────────────────
    {"wenn": {"schutz_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautschutz",
     "quelle": "G 24, Abschnitt 1.2.1 (Zwischenanamnese) / 2.2",
     "befund": "Unverträglichkeit oder Probleme mit Schutzhandschuhen/Hautmitteln",
     "konsequenz": "Schutzhandschuhe und Hautmittel anpassen (2.2): Austausch bei "
                   "Unverträglichkeit, Tragezeiten beachten, saugfähige "
                   "Unterziehhandschuhe bzw. Baumwollinnenfutter bei längeren Tragezeiten; "
                   "DGUV Information 212-017 und 212-007, DGUV Regel 112-195 beachten."},
    {"wenn": {"schutz_nutzung": ["keine"]},
     "schwere": "hinweis",
     "bereich": "Hautschutz",
     "quelle": "G 24, Abschnitt 1.2.1 (Zwischenanamnese) / 2.2",
     "befund": "Es werden keine Präventionsmaßnahmen (Handschuhe, Hautschutz-, "
               "Reinigungs-, Pflegemittel) durchgeführt",
     "konsequenz": "Präventionsmaßnahmen erfragen und dokumentieren (1.2.1); Beratung zum "
                   "Hautschutzplan, zu Schutzhandschuhen sowie Hautschutz-, Reinigungs- "
                   "und Pflegemitteln einschließlich Anwendungsschulung (2.2)."},
    # ── Vorgeschichte ────────────────────────────────────────────────────
    {"wenn": {"beruf_hauterkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsanamnese",
     "quelle": "G 24, Abschnitt 1.2.1 / 2.1.3",
     "befund": "Frühere berufsbedingte Hauterkrankung bzw. Unverträglichkeit "
               "hautbelastender Tätigkeiten",
     "konsequenz": "Vorbefunde und ggf. Unterlagen aus einem früheren Hautarztverfahren "
                   "heranziehen; Wirksamkeit der Schutzmaßnahmen prüfen und verkürzte "
                   "Nachuntersuchungsfristen erwägen (2.1.3)."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug",
     "quelle": "G 24, Abschnitt 1.1 / Abschnitt 2",
     "befund": "Untersuchte Person vermutet Zusammenhang zwischen Hautproblemen und Arbeit",
     "konsequenz": "Anspruch auf vorzeitige Nachuntersuchung (1.1); Zusammenhang abklären, "
                   "bei möglicher beruflicher Verursachung Hautarztverfahren (F 6050) "
                   "einleiten."},
]
