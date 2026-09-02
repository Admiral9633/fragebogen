# -*- coding: utf-8 -*-
"""G 2 Blei oder seine Verbindungen (mit Ausnahme der Bleialkyle) – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016,
G 2 (Fassung Oktober 2014), S. 119–131."""

SLUG = "g2-blei-2016"

CATALOG = {
    "version": 2,
    "title": "G 2 Blei oder seine Verbindungen (ohne Bleialkyle) (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 2 »Blei oder seine Verbindungen (mit Ausnahme der Bleialkyle)« "
             "(Fassung Oktober 2014), S. 119–131",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "unt_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt, "
                            "die Nachuntersuchung regelmäßig nach 12 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "länger dauernde Erkrankung?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Bleibelastung ────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Bleibelastung",
            "subtitle": "Ihre Arbeit und der Kontakt mit Blei",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "blei_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Bei welchen Tätigkeiten haben Sie Kontakt mit Blei oder "
                             "bleihaltigen Materialien?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "huette", "label": "Bleihütte: Verhütten, Einschmelzen oder Raffinieren von Blei"},
                        {"value": "recycling", "label": "Recycling bleihaltiger Abfälle und Altmaterialien"},
                        {"value": "akku", "label": "Herstellung von Akkumulatoren (Batterien) oder "
                                                   "bleistabilisierten Kunststoffen"},
                        {"value": "entschichten", "label": "Entfernen bleihaltiger Farben/Beschichtungen "
                                                           "(Abbrennen, Schleifen, Strahlen, Abbeizen – z. B. "
                                                           "Stahlbauten, Brücken, Masten)"},
                        {"value": "schweissen", "label": "Schweißen oder Brennschneiden an Teilen mit "
                                                         "bleihaltigen Anstrichen (z. B. Abbruch)"},
                        {"value": "loeten", "label": "Löten bleihaltiger Materialien (mit offener Flamme)"},
                        {"value": "farben", "label": "Bleipigmente, Bleiglasuren, bleihaltige Farben oder "
                                                     "keramischer Siebdruck"},
                        {"value": "dach_glas", "label": "Dacheindeckung mit Blei, Glasmalerei oder "
                                                        "Bleiverglasung (z. B. Restaurierung von Kirchenfenstern)"},
                        {"value": "draht", "label": "Drahtindustrie (Bleipatentieranlagen) oder bleihaltige "
                                                    "Automatenstähle/Lagerwerkstoffe"},
                        {"value": "munition", "label": "Bleihaltige Munition/Sprengmaterial oder Reinigen "
                                                       "von Schießständen"},
                        {"value": "reinigung", "label": "Instandsetzung, Reinigung oder Revision in "
                                                        "bleierzeugenden/-verarbeitenden Bereichen"},
                        {"value": "andere", "label": "Andere Tätigkeit mit Blei"},
                        {"value": "keine", "label": "Keine davon / weiß nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit Blei oder "
                             "bleihaltigen Materialien?",
                    "required": True,
                    "options": [
                        {"value": "beginnt", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis10", "label": "1 bis 10 Jahre"},
                        {"value": "ueber10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "fruehere_blei",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten (auch privat, z. B. Schießsport, "
                             "Restaurieren) Kontakt mit Blei?",
                    "required": True,
                    "followup": {"id": "fruehere_blei_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
                {
                    "id": "laermbereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie zusätzlich in einem Lärmbereich "
                             "(Bereich, in dem Gehörschutz getragen werden muss)?",
                    "hint": "Blei kann das Gehör zusätzlich belasten (»ototoxisch« = ohrschädigend).",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Ein erheblicher Teil des Bleis wird über den Mund aufgenommen – "
                        "Hygiene am Arbeitsplatz ist deshalb besonders wichtig.",
            "questions": [
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Tragen Sie die vorgesehene persönliche Schutzausrüstung "
                             "(z. B. Atemschutz, Schutzkleidung, Handschuhe)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_erforderlich", "label": "An meinem Arbeitsplatz nicht erforderlich"},
                    ],
                },
                {
                    "id": "essen_rauchen",
                    "type": "yes_no",
                    "label": "Essen, trinken oder rauchen Sie am Arbeitsplatz?",
                    "required": True,
                },
                {
                    "id": "haende_waschen",
                    "type": "yes_no",
                    "label": "Waschen Sie sich vor dem Essen, Trinken oder Rauchen gründlich "
                             "Hände und Gesicht?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Bleitypische Beschwerden",
            "questions": [
                {
                    "id": "beschwerden_allgemein",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine oder mehrere dieser Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "abgeschlagenheit", "label": "Allgemeine Abgeschlagenheit oder Müdigkeit"},
                        {"value": "appetitlosigkeit", "label": "Appetitlosigkeit"},
                        {"value": "kopfschmerzen", "label": "Häufige Kopfschmerzen"},
                        {"value": "schwaeche", "label": "Schwächegefühl"},
                        {"value": "glieder", "label": "Schmerzen in Gliedern oder Gelenken"},
                        {"value": "blaesse", "label": "Auffällige Blässe von Haut oder Schleimhäuten"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "magen_darm_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie Magen-Darm-Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "stoerungen", "label": "Magen- oder Darmstörungen (z. B. Übelkeit, Druckgefühl)"},
                        {"value": "verstopfung", "label": "Anhaltende Verstopfung (Obstipation)"},
                        {"value": "koliken", "label": "Heftige, krampfartige Bauchschmerzen (Koliken)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "nerven_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie Beschwerden, die das Nervensystem betreffen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "konzentration", "label": "Probleme mit Konzentration, Aufmerksamkeit "
                                                            "oder Gedächtnis"},
                        {"value": "missempfindungen", "label": "Kribbeln, Taubheitsgefühl oder Schwäche "
                                                               "in Armen oder Beinen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "bleisaum",
                    "type": "yes_no",
                    "label": "Ist Ihnen ein dunkler, gräulich-schwarzer Saum am Zahnfleisch "
                             "aufgefallen (»Bleisaum«)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen_sektion",
            "title": "Vorerkrankungen & Vorgeschichte",
            "subtitle": "Erkrankungen, die für die Beurteilung wichtig sind",
            "questions": [
                {
                    "id": "vorerkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine dieser Erkrankungen festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "leber", "label": "Erkrankung der Leber"},
                        {"value": "niere", "label": "Erkrankung der Nieren"},
                        {"value": "blut", "label": "Erkrankung des Blutes (z. B. Blutarmut/Anämie, Thalassämie)"},
                        {"value": "nerven_erkr", "label": "Erkrankung des Nervensystems "
                                                          "(Gehirn, Rückenmark oder Nerven)"},
                        {"value": "diabetes", "label": "Zuckerkrankheit (Diabetes)"},
                        {"value": "schilddruese", "label": "Ausgeprägte Schilddrüsenüberfunktion"},
                        {"value": "verdauung", "label": "Erkrankung des Magen-Darm-Trakts"},
                        {"value": "gefaesse", "label": "Erkrankung der Blutgefäße "
                                                       "(z. B. Durchblutungsstörungen, Arteriosklerose)"},
                        {"value": "bluthochdruck", "label": "Ausgeprägter Bluthochdruck (Hypertonie)"},
                        {"value": "tuberkulose", "label": "Tuberkulose"},
                        {"value": "koerperschwaeche", "label": "Allgemeine Körperschwäche"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "vorerkrankungen_details",
                    "type": "textarea",
                    "label": "Falls Sie eine Erkrankung angekreuzt haben: Welche genau, seit wann, "
                             "und wie wird sie behandelt?",
                    "required": False,
                },
                {
                    "id": "schwanger_still",
                    "type": "choice",
                    "label": "Sind Sie zurzeit schwanger, oder stillen Sie?",
                    "hint": "Blei kann das ungeborene Kind schädigen. Für Schwangere und "
                            "Stillende gelten besondere Schutzvorschriften.",
                    "required": True,
                    "options": [
                        {"value": "ja_schwanger", "label": "Ja, ich bin schwanger"},
                        {"value": "ja_stillt", "label": "Ja, ich stille"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "nicht_zutreffend", "label": "Trifft auf mich nicht zu"},
                    ],
                },
                {
                    "id": "kinderwunsch",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen aktuell ein Kinderwunsch (Familienplanung)?",
                    "hint": "Blei kann die Fruchtbarkeit beeinträchtigen.",
                    "required": True,
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
    # ── Bedenkenstatbestände (Abschnitt 2.1.1) ────────────────────────────
    {"wenn": {"vorerkrankungen": ["leber", "niere", "nerven_erkr", "diabetes",
                                   "schilddruese", "verdauung", "gefaesse",
                                   "bluthochdruck", "tuberkulose", "koerperschwaeche"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankungen (Bedenkenstatbestand)",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3",
     "befund": "Erkrankung aus dem Katalog der Bedenkenstatbestände nach 2.1.1 angegeben.",
     "konsequenz": "Bei schweren Gesundheitsstörungen dauernde gesundheitliche Bedenken "
                   "gegen Aufnahme bzw. Fortsetzung der Tätigkeit prüfen (2.1.1). Bei weniger "
                   "ausgeprägten Störungen prüfen, ob »keine Bedenken unter bestimmten "
                   "Voraussetzungen« möglich sind (2.1.3: technische/organisatorische Schutz-"
                   "maßnahmen, Begrenzung der Expositionszeit, Einsatz mit geringerer "
                   "Exposition, PSA, verkürzte Nachuntersuchungsfristen). Ist eine Wieder-"
                   "herstellung zu erwarten: befristete Bedenken (2.1.2)."},
    {"wenn": {"vorerkrankungen": ["blut"]},
     "schwere": "kritisch",
     "bereich": "Bluterkrankung/Anämie",
     "quelle": "Abschnitte 2.1.1 und 1.2.2 (Wichtiger Hinweis)",
     "befund": "Erkrankung des Blutes (z. B. Anämie, Thalassämie) angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1 prüfen. Zusätzlich beachten: Bei Anämie "
                   "sind die Erythrozyten bei gleichem Blutbleispiegel wesentlich stärker mit "
                   "Blei beladen – höhere Belastung und Gefährdung. Blutbild und Blutblei-"
                   "bestimmung vor Einsatzentscheidung; im Zweifel dauernde Bedenken."},
    {"wenn": {"schwanger_still": ["ja_schwanger", "ja_stillt"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 2.2 (fruchtschädigende Wirkung); Mutterschutzrecht",
     "befund": "Schwangerschaft oder Stillzeit bei Tätigkeit mit Bleiexposition angegeben.",
     "konsequenz": "Vor (weiterem) Einsatz klären: Blei hat eine fruchtschädigende Wirkung. "
                   "Beschäftigungsbeschränkungen nach Mutterschutzrecht unverzüglich prüfen; "
                   "bis zur Klärung keine Tätigkeit mit Bleiexposition; Blutbleibestimmung "
                   "und Beratung veranlassen."},
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Schwere oder länger dauernde Erkrankung seit der letzten Untersuchung.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt; ärztlich prüfen, ob die "
                   "Erkrankung Anlass zu Bedenken gegen die Fortsetzung der Tätigkeit gibt "
                   "(Kriterien nach 2.1); Befunde der behandelnden Ärzte einholen."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitte 1.1 und 4 (BK-Nr. 1101)",
     "befund": "Proband vermutet einen Zusammenhang zwischen Beschwerden und der Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung veranlassen; Beschwerden dokumentieren, "
                   "Blutbleibestimmung durchführen. Bei begründetem Verdacht auf eine "
                   "Erkrankung durch Blei BK-Anzeige (Nr. 1101 BKV) prüfen."},
    # ── Frühere Exposition (Abschnitt 1.2.2) ──────────────────────────────
    {"wenn": {"fruehere_blei": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitt 1.2.2 (Erstuntersuchung, »Erwünscht«)",
     "befund": "Anamnestische Hinweise auf eine vorausgegangene Bleibelastung.",
     "konsequenz": "Bereits bei der Erstuntersuchung bleispezifische Untersuchungen "
                   "durchführen: Biomonitoring (Blutbleibestimmung nach 3.1.4) zusätzlich "
                   "zum allgemeinen Programm; frühere Expositionen dokumentieren."},
    # ── Bleitypische Beschwerden (Abschnitt 3.2.3) ────────────────────────
    {"wenn": {"beschwerden_allgemein": ["abgeschlagenheit", "appetitlosigkeit",
                                         "kopfschmerzen", "schwaeche", "glieder",
                                         "blaesse"]},
     "schwere": "pruefen",
     "bereich": "Bleitypische Beschwerden",
     "quelle": "Abschnitte 3.2.3 (kritisches Anfangsstadium) und 1.2.2",
     "befund": "Bleitypische Allgemeinbeschwerden angegeben (Abgeschlagenheit, Appetit-"
               "losigkeit, Kopfschmerzen, Schwächegefühl, Glieder-/Gelenkschmerzen, Blässe).",
     "konsequenz": "Spezielle Untersuchung veranlassen: großes Blutbild, Kreatinin im Serum, "
                   "SGPT, SGOT, γ-GT, β2-Mikroglobulin im Harn sowie qualitätsgesicherte "
                   "Blutbleibestimmung. Arbeitsmedizinisch-toxikologische Beratung; "
                   "vorzeitige Nachuntersuchung erwägen."},
    {"wenn": {"magen_darm_beschwerden": ["stoerungen", "verstopfung"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm-Beschwerden",
     "quelle": "Abschnitte 3.2.3 und 1.2.2",
     "befund": "Magen-Darm-Störungen bzw. Obstipation angegeben (mögliches kritisches "
               "Anfangsstadium einer Bleieinwirkung).",
     "konsequenz": "Blutbleibestimmung und spezielle Untersuchung nach 1.2.2; Beschwerde-"
                   "verlauf dokumentieren; vorzeitige Nachuntersuchung erwägen."},
    {"wenn": {"magen_darm_beschwerden": ["koliken"]},
     "schwere": "kritisch",
     "bereich": "Verdacht auf Bleikolik",
     "quelle": "Abschnitte 3.2.3 (ausgeprägte Bleikrankheit) und 4",
     "befund": "Heftige, krampfartige Bauchschmerzen (Koliken) angegeben.",
     "konsequenz": "Verdacht auf ausgeprägte Bleikrankheit (Bleikolik): unverzügliche "
                   "ärztliche Abklärung mit qualitätsgesicherter Blutbleibestimmung vor "
                   "Fortsetzung der Tätigkeit; gesundheitliche Bedenken prüfen, BK-Anzeige "
                   "(Nr. 1101 BKV) erwägen. Hinweis: Chelattherapie (EDTA) ist bei beruf-"
                   "licher Bleivergiftung in aller Regel kontraindiziert."},
    {"wenn": {"nerven_beschwerden": ["konzentration", "missempfindungen"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 3.2.3 und 2.1.1",
     "befund": "Kognitive Beschwerden (Konzentration, Aufmerksamkeit, Gedächtnis) oder "
               "Missempfindungen/Schwäche in Armen/Beinen angegeben.",
     "konsequenz": "Blutbleibestimmung (der Biologische Grenzwert von 400 µg/l wurde wegen "
                   "ZNS-Effekten festgesetzt) und neurologische Abklärung veranlassen; "
                   "prüfen, ob eine Erkrankung des Nervensystems als Bedenkenstatbestand "
                   "nach 2.1.1 vorliegt; vorzeitige Nachuntersuchung erwägen."},
    {"wenn": {"bleisaum": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bleisaum",
     "quelle": "Abschnitt 3.2.3",
     "befund": "Dunkler Saum am Zahnfleisch (möglicher Bleisaum) angegeben.",
     "konsequenz": "Als Zeichen relevanter Bleiaufnahme werten: Blutbleibestimmung "
                   "durchführen; Beratung zu Mund-/Zahnhygiene und Arbeitshygiene."},
    # ── Hygiene und Schutzmaßnahmen (Abschnitte 2.2, 3.1.1, 2.1.1) ────────
    {"wenn": {"essen_rauchen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitshygiene",
     "quelle": "Abschnitte 2.2, 3.1.1 und 2.1.1 (Nachuntersuchung)",
     "befund": "Essen, Trinken oder Rauchen am Arbeitsplatz angegeben.",
     "konsequenz": "Eindringliche Beratung: Ein erheblicher Teil der Bleibelastung entsteht "
                   "durch orale Aufnahme (Hand-Mund-Kontakt, Essen/Trinken/Rauchen am "
                   "Arbeitsplatz). Blutbleispiegel kontrollieren. Bei wiederholt übermäßig "
                   "hoher Bleiaufnahme (z. B. durch Ernährungsgewohnheiten oder mangelnde "
                   "persönliche Hygiene) dauernde Bedenken möglich; häufig genügt die "
                   "Versetzung an einen Arbeitsplatz mit geringerer Bleiexposition mit "
                   "Blutbleikontrolle in kürzeren Abständen (2.1.1)."},
    {"wenn": {"haende_waschen": ["no"]},
     "schwere": "pruefen",
     "bereich": "Arbeitshygiene",
     "quelle": "Abschnitte 2.2 und 3.1.1",
     "befund": "Hände/Gesicht werden vor dem Essen, Trinken oder Rauchen nicht gewaschen.",
     "konsequenz": "Hygieneberatung (2.2): vor Essen, Trinken und Rauchen gründlich Hände "
                   "und Gesicht waschen; Bedeutung der oralen Bleiaufnahme erläutern. "
                   "Blutbleikontrolle in kürzeren Abständen erwägen."},
    {"wenn": {"psa_nutzung": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Beratung zu Hygienemaßnahmen und persönlicher Schutzausrüstung (2.2). "
                   "Ergeben sich Hinweise, dass die Gefährdungsbeurteilung aktualisiert und "
                   "der Arbeitsschutz verbessert werden muss, Mitteilung an den Arbeitgeber "
                   "unter Wahrung der schutzwürdigen Belange des Untersuchten."},
    # ── Beratung ──────────────────────────────────────────────────────────
    {"wenn": {"kinderwunsch": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Fortpflanzung",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Aktueller Kinderwunsch angegeben.",
     "konsequenz": "Beratung über die mögliche fruchtschädigende sowie die Fortpflanzungs-"
                   "fähigkeit beeinträchtigende Wirkung von Blei und seinen Verbindungen; "
                   "Blutbleiwert besprechen und Schutzmaßnahmen bzw. expositionsärmeren "
                   "Einsatz erörtern."},
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 3.1.1",
     "befund": "Tätigkeit mit Bleiexposition in einem Lärmbereich angegeben.",
     "konsequenz": "Wegen der ototoxischen Eigenschaft von Blei mögliche Kombinations-"
                   "wirkungen mit Lärm bei der Gehöruntersuchung nach dem DGUV Grundsatz "
                   "G 20 berücksichtigen."},
]
