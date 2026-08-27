# -*- coding: utf-8 -*-
"""
Gefährdung der Haut – DGUV Empfehlung 2024 (E GHA).

Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und
Untersuchungen, 1. Auflage 2024, "Gefährdung der Haut" (Kurzbezeichnung
E GHA, Fassung Januar 2022), S. 267–286.

Anamnese-Fragen, die die versicherte Person selbst beantworten kann
(Tätigkeit/Exposition, Schutzmaßnahmen, Beschwerden, Vorerkrankungen),
plus datengetriebene Auswertungsregeln nach den Abschnitten 2, 6, 7 und 8
der Empfehlung. Keine Messwerte oder ärztlichen Befunde.
"""

SLUG = "haut-2024"

CATALOG = {
    "version": 2,
    "title": "Gefährdung der Haut (DGUV Empfehlung 2024)",
    "basis": (
        "DGUV Empfehlungen für arbeitsmedizinische Beratungen und "
        "Untersuchungen, 1. Auflage 2024, „Gefährdung der Haut“ "
        "(E GHA, Fassung Januar 2022), S. 267–286"
    ),
    "sections": [
        # ── 1 ─────────────────────────────────────────────────────────────
        {
            "id": "anlass",
            "title": "Anlass der Vorsorge",
            "subtitle": "Warum Sie heute hier sind",
            "questions": [
                {
                    "id": "vorsorge_folge",
                    "type": "choice",
                    "label": "Waren Sie wegen Hautbelastungen bei der Arbeit schon einmal "
                             "bei einer arbeitsmedizinischen Vorsorge?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Nein, dies ist meine erste Vorsorge"},
                        {"value": "weitere", "label": "Ja, ich war schon einmal oder mehrmals dort"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wissen Sie, um welche Art der Vorsorge es sich heute handelt?",
                    "required": True,
                    "hint": "Steht meist auf der Einladung Ihres Arbeitgebers. "
                            "Wenn Sie es nicht wissen, ist das kein Problem.",
                    "options": [
                        {"value": "pflicht", "label": "Pflichtvorsorge (vom Arbeitgeber veranlasst)"},
                        {"value": "angebot", "label": "Angebotsvorsorge (vom Arbeitgeber angeboten)"},
                        {"value": "wunsch", "label": "Wunschvorsorge (auf meinen eigenen Wunsch)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 2 ─────────────────────────────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Hautbelastung",
            "subtitle": "Womit Ihre Haut bei der Arbeit in Kontakt kommt",
            "questions": [
                {
                    "id": "branche",
                    "type": "choice",
                    "label": "In welchem Bereich arbeiten Sie?",
                    "required": True,
                    "options": [
                        {"value": "gesundheit", "label": "Gesundheits- oder Pflegeberuf"},
                        {"value": "nahrung", "label": "Nahrungsmittel, Küche, Gastgewerbe"},
                        {"value": "metall", "label": "Metallbranche"},
                        {"value": "reinigung", "label": "Reinigungsberuf"},
                        {"value": "friseur", "label": "Friseur- oder Kosmetikbranche"},
                        {"value": "bau", "label": "Baugewerbe"},
                        {"value": "andere", "label": "Anderer Bereich"},
                    ],
                    "followup": {"id": "branche_sonst", "type": "text",
                                 "label": "In welchem Bereich arbeiten Sie?",
                                 "when": "andere"},
                },
                {
                    "id": "feuchtarbeit",
                    "type": "yes_no",
                    "label": "Arbeiten Sie regelmäßig mit nassen oder feuchten Händen, "
                             "oder müssen Sie Ihre Hände bei der Arbeit häufig waschen "
                             "oder desinfizieren?",
                    "required": True,
                    "hint": "Das nennt man Feuchtarbeit. Auch Arbeiten in flüssigkeitsdichten "
                            "Handschuhen zählt dazu, weil die Haut darunter feucht wird.",
                },
                {
                    "id": "feuchtarbeit_dauer",
                    "type": "choice",
                    "label": "Wie viele Stunden pro Arbeitstag sind Ihre Hände insgesamt "
                             "feucht, in dichten Handschuhen oder werden gewaschen/desinfiziert?",
                    "required": True,
                    "show_if": {"id": "feuchtarbeit", "in": ["yes"]},
                    "options": [
                        {"value": "unter2", "label": "Bis zu 2 Stunden pro Tag"},
                        {"value": "2bis4", "label": "Mehr als 2, aber weniger als 4 Stunden pro Tag"},
                        {"value": "ab4", "label": "4 Stunden oder mehr pro Tag"},
                    ],
                    "hint": "Ab mehr als 2 Stunden muss Ihnen Vorsorge angeboten werden, "
                            "ab 4 Stunden ist sie Pflicht.",
                },
                {
                    "id": "handschuhe_dicht",
                    "type": "yes_no",
                    "label": "Tragen Sie bei der Arbeit regelmäßig flüssigkeitsdichte "
                             "Schutzhandschuhe oder Gummistiefel?",
                    "required": True,
                    "hint": "Unter dichten Handschuhen und Stiefeln stauen sich Wärme und "
                            "Feuchtigkeit – das belastet die Haut.",
                },
                {
                    "id": "latexhandschuhe",
                    "type": "yes_no",
                    "label": "Benutzen Sie Handschuhe aus Naturgummilatex (Latexhandschuhe)?",
                    "required": True,
                },
                {
                    "id": "iso_epoxid",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Isocyanaten oder mit nicht ausgehärteten "
                             "Epoxidharzen (z.B. 2-Komponenten-Kleber, -Lacke, -Schäume, "
                             "Bodenbeschichtungen)?",
                    "required": True,
                    "followup": {"id": "iso_epoxid_desc", "type": "text",
                                 "label": "Mit welchen Produkten, und wie oft?",
                                 "when": "yes"},
                },
                {
                    "id": "stoffe_irritativ",
                    "type": "multi_choice",
                    "label": "Mit welchen hautreizenden Stoffen kommen Ihre Hände bei der "
                             "Arbeit in Kontakt?",
                    "required": True,
                    "options": [
                        {"value": "reinigung", "label": "Reinigungslösungen, Tenside, Spülmittel"},
                        {"value": "desinfektion", "label": "Desinfektionsmittel"},
                        {"value": "kss", "label": "Wassergemischte Kühlschmierstoffe (Bohr-/Schneidwasser)"},
                        {"value": "loesemittel", "label": "Entfettende Lösemittel (z.B. Verdünnung, Aceton)"},
                        {"value": "alkalisch_sauer", "label": "Alkalische oder saure Gemische (Laugen, Säuren, Zement)"},
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
                        {"value": "acrylate", "label": "Nicht ausgehärtete Kunstharze (Acrylate, z.B. Nagelmodellage, Dental, Klebstoffe)"},
                        {"value": "gummi", "label": "Gummi-Inhaltsstoffe (z.B. Gummiartikel, Reifen)"},
                        {"value": "biozide", "label": "Konservierungsstoffe / Biozide"},
                        {"value": "duft", "label": "Aroma- und Duftstoffe"},
                        {"value": "metalle", "label": "Metalle wie Chrom, Kobalt, Nickel (auch Zement, Galvanik)"},
                        {"value": "friseurchemie", "label": "Friseurchemikalien (z.B. Haarfarben, Blondiermittel)"},
                        {"value": "pflanzen_nahrung", "label": "Pflanzen, tropische Hölzer oder Nahrungsmittel (rohe Lebensmittel)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "physikalisch",
                    "type": "multi_choice",
                    "label": "Welche mechanischen oder physikalischen Belastungen wirken "
                             "bei der Arbeit auf Ihre Haut?",
                    "required": True,
                    "options": [
                        {"value": "fasern", "label": "Mineral- oder Keramikfasern (z.B. Dämmwolle)"},
                        {"value": "spaene", "label": "Metallspäne"},
                        {"value": "abrasiv", "label": "Scheuernde Partikel (z.B. Handwaschpaste mit Reibekörpern)"},
                        {"value": "rau", "label": "Raue Oberflächen, starke Reibung"},
                        {"value": "hitze_kaelte", "label": "Hitze oder Kälte"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
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
            "id": "schutz",
            "title": "Hautschutz im Arbeitsalltag",
            "subtitle": "Welche Schutzmaßnahmen Sie tatsächlich nutzen",
            "questions": [
                {
                    "id": "schutz_nutzung",
                    "type": "multi_choice",
                    "label": "Welche Hautschutzmaßnahmen nutzen Sie bei der Arbeit "
                             "tatsächlich regelmäßig?",
                    "required": True,
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
                    "id": "hautschutzplan",
                    "type": "yes_no",
                    "label": "Gibt es an Ihrem Arbeitsplatz einen Hautschutzplan, und "
                             "kennen Sie ihn?",
                    "required": True,
                    "hint": "Ein Hautschutzplan zeigt, welches Schutz-, Reinigungs- und "
                            "Pflegemittel wann benutzt werden soll.",
                },
                {
                    "id": "schutz_probleme",
                    "type": "yes_no",
                    "label": "Vertragen Sie Ihre Schutzhandschuhe oder die Hautmittel "
                             "schlecht, oder kommen Sie damit bei der Arbeit nicht zurecht?",
                    "required": True,
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
                    "hint": "Auch abgeheilte Neurodermitis in der Kindheit ist wichtig: Die "
                            "Haut der Hände bleibt oft empfindlicher.",
                },
                {
                    "id": "atopie_sonst",
                    "type": "yes_no",
                    "label": "Haben Sie Heuschnupfen, allergischen Schnupfen oder "
                             "allergisches Asthma?",
                    "required": True,
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
    # ── Vorsorgeanlass / Fristen ─────────────────────────────────────────
    {"wenn": {"feuchtarbeit_dauer": ["ab4"]},
     "schwere": "hinweis",
     "bereich": "Vorsorgeanlass",
     "quelle": "Abschnitt 2 (Anwendungsbereich, ArbMedVV-Tabelle)",
     "befund": "Feuchtarbeit von regelmäßig 4 Stunden oder mehr je Tag",
     "konsequenz": "Pflichtvorsorge-Anlass nach ArbMedVV: Pflichtvorsorge sicherstellen und "
                   "Folgevorsorge fristgerecht nach AMR 2.1 veranlassen (Abschnitt 7.3); "
                   "Vorsorgebescheinigung mit Anlass und nächstem Termin ausstellen (AMR 6.3)."},
    {"wenn": {"feuchtarbeit_dauer": ["2bis4"]},
     "schwere": "hinweis",
     "bereich": "Vorsorgeanlass",
     "quelle": "Abschnitt 2 (Anwendungsbereich, ArbMedVV-Tabelle)",
     "befund": "Feuchtarbeit von regelmäßig mehr als 2 Stunden je Tag",
     "konsequenz": "Angebotsvorsorge-Anlass: dem Unternehmen die Angebotspflicht bestätigen; "
                   "Fristen nach AMR 2.1 (Abschnitt 7.3)."},
    {"wenn": {"latexhandschuhe": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Vorsorgeanlass",
     "quelle": "Abschnitt 2 (ArbMedVV-Tabelle) / Abschnitt 8.1",
     "befund": "Benutzung von Naturgummilatexhandschuhen",
     "konsequenz": "Klären, ob Handschuhe mit mehr als 30 Mikrogramm Protein je Gramm "
                   "verwendet werden – dann Pflichtvorsorge-Anlass. Beratung: puderfreie, "
                   "proteinarme Handschuhe bzw. Austausch der Handschuhe (Abschnitt 8.1)."},
    {"wenn": {"iso_epoxid": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Vorsorgeanlass",
     "quelle": "Abschnitt 2 (ArbMedVV-Tabelle) / Abschnitt 6.1",
     "befund": "Tätigkeiten mit Isocyanaten bzw. unausgehärteten Epoxidharzen",
     "konsequenz": "Vorsorgeanlass prüfen: Pflichtvorsorge bei regelmäßigem Hautkontakt mit "
                   "Isocyanaten oder Luftkonzentration über 0,05 mg/m³ sowie bei dermaler "
                   "Gefährdung durch unausgehärtete Epoxidharze (insbesondere Versprühen); "
                   "sonst Angebotsvorsorge. Ergänzend DGUV Empfehlung „Isocyanate“ heranziehen."},
    {"wenn": {"mikroorganismen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Exposition",
     "quelle": "Abschnitt 6.1 (Sonstige Einwirkungen) / Abschnitt 8.1",
     "befund": "Kontakt mit hautpathogenen Mikroorganismen möglich",
     "konsequenz": "Hygiene- und Schutzmaßnahmen beraten; Händedesinfektion der tensidischen "
                   "Hautreinigung vorziehen, da weniger hautbelastend (Abschnitt 8.1). "
                   "An BK-Nrn. 3101/3102 denken."},
    # ── Beschwerden / Untersuchung ───────────────────────────────────────
    {"wenn": {"haut_aktuell": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautbefund",
     "quelle": "Abschnitt 7.2.1",
     "befund": "Aktuelle Hautveränderungen an Händen, Unterarmen oder Gesicht",
     "konsequenz": "Körperliche Untersuchung der exponierten Hautareale (Hände, Unterarme, "
                   "Gesicht) anbieten – Augenmerk auf trockene Haut, Hyperhidrose, "
                   "Ekzemherde und Fingerzwischenräume. In unklaren Fällen Vorbefunde und "
                   "Expositionsdaten heranziehen und gezielte dermatologische Diagnostik "
                   "veranlassen."},
    {"wenn": {"arbeitsbezug": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug",
     "quelle": "Abschnitt 8 / DGUV Information 250-005",
     "befund": "Hautveränderungen bessern sich in arbeitsfreier Zeit",
     "konsequenz": "Verdacht auf arbeitsbedingte Hauterkrankung: Verfahrensablauf nach "
                   "DGUV Information 250-005 einleiten; Erkenntnisse auswerten und dem "
                   "Unternehmen ggf. zusätzliche Schutzmaßnahmen vorschlagen "
                   "(§ 6 (4) ArbMedVV, Überprüfung der Gefährdungsbeurteilung)."},
    {"wenn": {"ekzem_verlauf": ["wiederholt", "schwer"]},
     "schwere": "kritisch",
     "bereich": "Ekzem",
     "quelle": "Abschnitt 7.4 / 7.4.4",
     "befund": "Schwere oder wiederholt rückfällige Ekzeme der exponierten Hautareale "
               "(auch anamnestisch)",
     "konsequenz": "Vor (weiterem) Einsatz klären: Maßnahmen nach 7.4.2 (Substitution, "
                   "technische/organisatorische Schutzmaßnahmen, Expositionsbegrenzung, "
                   "PSA, Hautschutzplan) und verkürzte Fristen nach 7.4.3 prüfen; führen "
                   "sie nicht zum Erfolg, Tätigkeitswechsel erwägen (7.4.4 – Mitteilung an "
                   "den Arbeitgeber nur mit Einwilligung, § 6 (4) ArbMedVV). Dermatologische "
                   "Mitbehandlung sicherstellen; an BK-Nr. 5101 denken."},
    {"wenn": {"dyshidrose": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ekzem",
     "quelle": "Abschnitt 7.1 (Beschwerden) / 7.2.1",
     "befund": "Dyshidrose (Bläschen im Palmoplantarbereich) angegeben",
     "konsequenz": "Untersuchung der Hände anbieten; in unklaren Fällen gezielte "
                   "dermatologische Diagnostik veranlassen (7.2.1)."},
    # ── Allergie ─────────────────────────────────────────────────────────
    {"wenn": {"allergie_arbeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Allergie",
     "quelle": "Abschnitt 7.4 / 7.4.4",
     "befund": "Allergische Hauterkrankung, berufliche Allergenexposition nicht vermeidbar",
     "konsequenz": "Vor (weiterem) Einsatz klären: zunächst Substitution des Allergens und "
                   "Schutzmaßnahmen nach 7.4.2 prüfen; ist die Exposition nicht hinreichend "
                   "zu vermeiden, Tätigkeitswechsel erwägen (7.4.4). Mitteilung an den "
                   "Arbeitgeber nur mit Einwilligung der versicherten Person (§ 6 (4) ArbMedVV)."},
    {"wenn": {"kontaktallergie": ["yes"]},
     "wenn_nicht": {"allergie_arbeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allergie",
     "quelle": "Abschnitt 7.1 (Beschwerden: vorbestehende Allergien)",
     "befund": "Bekannte Kontaktallergie ohne (bekannten) unvermeidbaren Arbeitskontakt",
     "konsequenz": "Auslösendes Allergen dokumentieren und mit den Arbeitsstoffen bzw. "
                   "Sicherheitsdatenblättern abgleichen; bei relevantem beruflichem Kontakt "
                   "Karenz und Schutzmaßnahmen festlegen. Prophetische Allergietestungen "
                   "sind nicht indiziert (7.1)."},
    # ── Disposition ──────────────────────────────────────────────────────
    {"wenn": {"atopisches_ekzem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Disposition",
     "quelle": "Abschnitt 6.3.4 / 7.4.2 / 7.4.3",
     "befund": "Atopisches Ekzem (Neurodermitis), auch anamnestisch in Kindheit/Jugend",
     "konsequenz": "Erhöhte Hautempfindlichkeit der Hände einkalkulieren: bei atopischem "
                   "Ekzem der exponierten Areale Maßnahmen nach 7.4.2 und verkürzte "
                   "Vorsorgefristen (7.4.3) empfehlen, erneuter Vorsorgetermin nach "
                   "Abheilung; bei erheblicher Minderbelastbarkeit Tätigkeitswechsel "
                   "erwägen (7.4.4). Intensivierte Hautschutzberatung (8.1)."},
    {"wenn": {"psoriasis_haende": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Disposition",
     "quelle": "Abschnitt 6.4 / 7.4.3",
     "befund": "Psoriasis an den Händen bzw. an mechanisch belasteten Hautstellen "
               "(mögliches Köbner-Phänomen)",
     "konsequenz": "Maßnahmen nach 7.4.2 und verkürzte Fristen (7.4.3): erneuter "
                   "Vorsorgetermin nach Abheilung; bei floridem Befund beachten, dass die "
                   "Belastung am Arbeitsplatz die Heilung behindern kann; bei erheblicher "
                   "Minderbelastbarkeit Tätigkeitswechsel erwägen (7.4.4)."},
    {"wenn": {"trockene_haut": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Disposition",
     "quelle": "Abschnitt 7.1 (Dispositionen) / 8.1",
     "befund": "Xerosis cutis (auffallend trockene, empfindliche Haut)",
     "konsequenz": "Intensivierte Beratung zu Hautschutz und Hautpflege; Hautmittel an die "
                   "individuelle Hautkonstitution anpassen (8.1)."},
    {"wenn": {"lichtempfindlich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Disposition",
     "quelle": "Abschnitt 7.1 / 7.4 (UV-induzierte Dermatosen)",
     "befund": "Erhöhte Lichtempfindlichkeit angegeben",
     "konsequenz": "Bei Tätigkeiten mit unvermeidbarer UV-Exposition die DGUV Empfehlungen "
                   "„Künstliche optische Strahlung“ und „Natürliche optische Strahlung“ "
                   "heranziehen; Beratung zum Lichtschutz."},
    # ── Prävention / Beratung ────────────────────────────────────────────
    {"wenn": {"schutz_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautschutz",
     "quelle": "Abschnitt 7.1 (weitere Vorsorgen) / 8.1",
     "befund": "Unverträglichkeit oder Probleme mit Schutzhandschuhen/Hautmitteln",
     "konsequenz": "Schutzhandschuhe und Hautmittel individuell anpassen (8.1): Austausch "
                   "bei Unverträglichkeit, Tragezeiten beachten, saugfähige "
                   "Unterziehhandschuhe bzw. Baumwollinnenfutter bei längeren Tragezeiten; "
                   "DGUV Information 212-017 und 212-007, DGUV Regel 112-195 beachten."},
    {"wenn": {"hautschutzplan": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hautschutz",
     "quelle": "Abschnitt 8.1 / 8.2",
     "befund": "Hautschutzplan nicht vorhanden oder nicht bekannt",
     "konsequenz": "Beratung zum Hautschutzplan und seiner Anwendung (8.1); fehlt ein "
                   "Hautschutzplan, dem Unternehmen Schutzmaßnahmen vorschlagen und "
                   "Überprüfung der Gefährdungsbeurteilung anstoßen (8.2, § 6 (4) ArbMedVV)."},
    {"wenn": {"schutz_nutzung": ["keine"]},
     "schwere": "hinweis",
     "bereich": "Hautschutz",
     "quelle": "Abschnitt 7.1 (weitere Vorsorgen) / 8.1",
     "befund": "Es werden keine Präventionsmaßnahmen (Handschuhe, Hautschutz-, "
               "Reinigungs-, Pflegemittel) durchgeführt",
     "konsequenz": "Durchgeführte Präventionsmaßnahmen erfragen und dokumentieren (7.1); "
                   "Beratung zu Schutzhandschuhen, Hautschutz-, Hautreinigungs- und "
                   "Hautpflegemitteln einschließlich Anwendungsschulung (8.1)."},
    # ── Vorgeschichte ────────────────────────────────────────────────────
    {"wenn": {"beruf_hauterkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsanamnese",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese)",
     "befund": "Frühere berufsbedingte Hauterkrankung bzw. Unverträglichkeit "
               "hautbelastender Tätigkeiten",
     "konsequenz": "Arbeitsanamnese vertiefen, Vorbefunde anfordern; Wirksamkeit der "
                   "aktuellen Schutzmaßnahmen kritisch prüfen und ggf. verkürzte "
                   "Vorsorgefristen empfehlen (7.4.3)."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug",
     "quelle": "Abschnitt 2 (Wunschvorsorge) / DGUV Information 250-005",
     "befund": "Versicherte Person vermutet Zusammenhang zwischen Hautproblemen und Arbeit",
     "konsequenz": "Anliegen abklären (Beratung, ggf. Untersuchung); Wunschvorsorge ist zu "
                   "ermöglichen. Bei begründetem Verdacht Verfahrensablauf nach "
                   "DGUV Information 250-005 einleiten."},
]
