# -*- coding: utf-8 -*-
"""G 26 Atemschutzgeräte – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 7. Auflage 2016 (Gentner Verlag),
G 26 »Atemschutzgeräte« (Fassung Oktober 2014), S. 391–400.

Der Grundsatz prüft, ob gesundheitliche Bedenken gegen das Tragen von
Atemschutzgeräten (Gruppen 1–3 nach AMR 14.2) bestehen. Feste
Nachuntersuchungsfristen: bis 50 Jahre 36 Monate; über 50 Jahre 24 Monate
(Gerät bis 5 kg) bzw. 12 Monate (über 5 kg). Vorzeitige Nachuntersuchung
u.a. nach mehrwöchiger Erkrankung."""

SLUG = "g26-atemschutz-2016"

CATALOG = {
    "version": 2,
    "title": "G 26 Atemschutzgeräte (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 7. Auflage 2016, "
             "G 26 »Atemschutzgeräte« (Fassung Oktober 2014), S. 391–400",
    "sections": [
        # ── 1 ─ Untersuchungsanlass & Fristen ──────────────────────────────
        {
            "id": "untersuchung",
            "title": "Untersuchungsanlass",
            "subtitle": "Angaben zu Ihrer G-26-Untersuchung",
            "questions": [
                {
                    "id": "untersuchungsart",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich?",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit mit Atemschutz)"},
                        {"value": "nach", "label": "Nachuntersuchung"},
                    ],
                },
                {
                    "id": "alter_gruppe",
                    "type": "choice",
                    "label": "Wie alt sind Sie?",
                    "hint": "Das Alter ist wichtig für die Untersuchungsfristen und für Einsätze "
                            "im Rettungswesen (z.B. Feuerwehr) sowie mit schweren Geräten der "
                            "Gruppe 3.",
                    "required": True,
                    "options": [
                        {"value": "unter18", "label": "Unter 18 Jahre"},
                        {"value": "18bis49", "label": "18 bis 49 Jahre"},
                        {"value": "ab50", "label": "50 Jahre oder älter"},
                    ],
                },
                {
                    "id": "letzte_g26",
                    "type": "choice",
                    "label": "Wie lange liegt Ihre letzte G-26-Untersuchung zurück?",
                    "hint": "Richtwerte des G 26: bis 50 Jahre Nachuntersuchung vor Ablauf von "
                            "36 Monaten; über 50 Jahre bei Gerätegewicht bis 5 kg vor Ablauf von "
                            "24 Monaten, über 5 kg vor Ablauf von 12 Monaten.",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach"]},
                    "options": [
                        {"value": "unter12", "label": "Weniger als 12 Monate"},
                        {"value": "12bis24", "label": "12 bis 24 Monate"},
                        {"value": "24bis36", "label": "24 bis 36 Monate"},
                        {"value": "ueber36", "label": "Mehr als 36 Monate"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "seit_letzter",
                    "type": "yes_no",
                    "label": "Waren Sie seit der letzten Untersuchung mehrere Wochen krank, "
                             "hatten Sie gesundheitliche Probleme beim Tragen des "
                             "Atemschutzgeräts, oder vermuten Sie einen Zusammenhang zwischen "
                             "Beschwerden und Ihrer Arbeit?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach"]},
                    "followup": {"id": "seit_letzter_desc", "type": "textarea",
                                 "label": "Was ist aufgetreten – welche Erkrankung oder "
                                          "welche Probleme, wann?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Tätigkeit & Gerät ──────────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Atemschutzgerät",
            "subtitle": "Angaben zu Arbeitsplatz, Arbeitsaufgabe und Gerät",
            "questions": [
                {
                    "id": "geraetegruppe",
                    "type": "choice",
                    "label": "Zu welcher Gruppe gehört das Atemschutzgerät, das Sie tragen (sollen)?",
                    "hint": "Die Einteilung richtet sich nach Gewicht und Atemwiderstand "
                            "(AMR 14.2). Gruppe 1: leichte Filtergeräte (z.B. Filtermasken), "
                            "Gruppe 3: schwere, von der Umgebungsluft unabhängige Geräte wie "
                            "Pressluftatmer. Ihr Arbeitgeber oder die Atemschutzwerkstatt kann "
                            "Ihnen die Gruppe nennen.",
                    "required": True,
                    "options": [
                        {"value": "gruppe1", "label": "Gruppe 1 – leichte Filtergeräte"},
                        {"value": "gruppe2", "label": "Gruppe 2 – mittelschwere Geräte"},
                        {"value": "gruppe3", "label": "Gruppe 3 – schwere Geräte (z.B. Pressluftatmer)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "geraetegewicht",
                    "type": "choice",
                    "label": "Wie schwer ist das Atemschutzgerät?",
                    "hint": "Bei Personen über 50 Jahren hängt die Nachuntersuchungsfrist vom "
                            "Gerätegewicht ab (bis 5 kg: 24 Monate, über 5 kg: 12 Monate). "
                            "Ein Pressluftatmer wiegt deutlich über 5 kg.",
                    "required": True,
                    "options": [
                        {"value": "bis5kg", "label": "Bis 5 kg"},
                        {"value": "ueber5kg", "label": "Über 5 kg"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "mundstueck",
                    "type": "choice",
                    "label": "Hat Ihr Gerät einen Mundstück-Anschluss (Sie beißen auf ein "
                             "Mundstück, statt eine Maske über Nase und Mund zu tragen)?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein, Halb- oder Vollmaske / Haube"},
                        {"value": "weiss_nicht", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "warneinrichtung",
                    "type": "choice",
                    "label": "Hat Ihr Gerät eine akustische Warneinrichtung (Warn-Pfeifton, "
                             "z.B. bei niedrigem Flaschendruck)?",
                    "hint": "Für Geräte der Gruppe 2 und 3 mit Pfeifton gehört ein Hörtest "
                            "(Luftleitung 1–6 kHz) zur Untersuchung.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "weiss_nicht", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "rettungswesen",
                    "type": "yes_no",
                    "label": "Tragen Sie Atemschutz im Rettungswesen – z.B. bei Feuerwehr, "
                             "Grubenwehr oder Gasschutzwehr?",
                    "hint": "Für Rettungskräfte ist eine hohe körperliche Belastbarkeit "
                            "unumgänglich, weil Menschen in Notsituationen auf ihre Hilfe "
                            "angewiesen sind. Die Belastbarkeit wird u.a. mit einer "
                            "Fahrrad-Belastungsuntersuchung (Ergometrie) geprüft.",
                    "required": True,
                },
                {
                    "id": "gase_gehoergang",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Gasen oder Dämpfen, die über den Gehörgang "
                             "(das Ohr) in den Körper aufgenommen werden können?",
                    "hint": "Wenn ja, wird bei der Untersuchung zusätzlich der Gehörgang "
                            "untersucht (Otoskopie). Wenn Sie unsicher sind, besprechen Sie "
                            "das bei der Untersuchung.",
                    "required": True,
                },
                {
                    "id": "zusatz_schutzkleidung",
                    "type": "yes_no",
                    "label": "Tragen Sie zusätzlich zum Atemschutz isolierende Schutzkleidung "
                             "(z.B. Chemikalien- oder Hitzeschutzanzug)?",
                    "hint": "Die Kombination mit anderer Schutzausrüstung bedeutet eine "
                            "zusätzliche Belastung.",
                    "required": True,
                },
                {
                    "id": "belastungen",
                    "type": "multi_choice",
                    "label": "Welche zusätzlichen Belastungen treten bei Ihrer Tätigkeit auf?",
                    "hint": "Klima, Schwere der Arbeit und Benutzungsdauer des Geräts werden "
                            "bei der Beurteilung berücksichtigt.",
                    "required": True,
                    "options": [
                        {"value": "schwere_arbeit", "label": "Schwere körperliche Arbeit"},
                        {"value": "hitze_klima", "label": "Hitze oder ungünstiges Klima"},
                        {"value": "lange_tragezeit", "label": "Lange Tragezeiten (über 30 Minuten am Stück)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
            ],
        },
        # ── 3 ─ Herz, Kreislauf & Belastbarkeit ────────────────────────────
        {
            "id": "koerper",
            "title": "Herz, Kreislauf & körperliche Belastbarkeit",
            "subtitle": "Vorerkrankungen und Belastbarkeit",
            "questions": [
                {
                    "id": "herz_kreislauf",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung des Herzens oder des "
                             "Kreislaufs (z.B. Herzinfarkt, Herzschwäche, "
                             "Herzrhythmusstörungen, stark erhöhter Blutdruck)?",
                    "required": True,
                    "followup": {"id": "herz_kreislauf_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, wie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "koerperschwaeche",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich allgemein körperlich schwach oder sind Sie bei "
                             "Belastung schnell erschöpft?",
                    "required": True,
                },
                {
                    "id": "bewegungsapparat",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung oder Verletzung des Stütz- und "
                             "Bewegungsapparats (Rücken, Gelenke, Muskeln) mit deutlicher "
                             "Einschränkung?",
                    "required": True,
                    "followup": {"id": "bewegungsapparat_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, welche Einschränkung?",
                                 "when": "yes"},
                },
                {
                    "id": "stoffwechsel_gewicht",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Zuckerkrankheit (Diabetes), eine Erkrankung "
                             "der Schilddrüse oder anderer Hormondrüsen oder starkes "
                             "Übergewicht (BMI über 30) festgestellt?",
                    "hint": "Der G 26 nennt auch Störungen der Drüsen mit innerer Sekretion "
                            "(z.B. Schilddrüse, Nebennieren), soweit sie die Belastbarkeit "
                            "stärker einschränken.",
                    "required": True,
                    "followup": {"id": "stoffwechsel_gewicht_desc", "type": "textarea",
                                 "label": "Was wurde festgestellt, wie wird es behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "hernie",
                    "type": "yes_no",
                    "label": "Haben Sie einen Eingeweidebruch (z.B. Leistenbruch, Nabelbruch, "
                             "Narbenbruch), der nicht operiert wurde?",
                    "required": True,
                    "followup": {"id": "hernie_desc", "type": "textarea",
                                 "label": "Wo befindet sich der Bruch, seit wann besteht er?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Atmung & Lunge ─────────────────────────────────────────────
        {
            "id": "atmung",
            "title": "Atmung & Lunge",
            "questions": [
                {
                    "id": "lunge",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung der Atemwege, der Lunge "
                             "oder des Brustkorbs (z.B. Asthma bronchiale, COPD/chronische "
                             "Bronchitis, Lungenemphysem, Brustkorbverletzung oder "
                             "-operation)?",
                    "required": True,
                    "followup": {"id": "lunge_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, wie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "atem_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei körperlicher Belastung oder beim Tragen von "
                             "Atemschutz Beschwerden – z.B. Atemnot, Engegefühl in der Brust, "
                             "Schwindel oder Herzrasen?",
                    "required": True,
                    "followup": {"id": "atem_beschwerden_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, in welchen Situationen?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Nervensystem & Psyche ──────────────────────────────────────
        {
            "id": "nerven_psyche",
            "title": "Nervensystem & Psyche",
            "questions": [
                {
                    "id": "anfallsleiden",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie ein Anfallsleiden (Epilepsie, Krampfanfälle)?",
                    "required": True,
                    "followup": {"id": "anfallsleiden_desc", "type": "textarea",
                                 "label": "Wann war der letzte Anfall, welche Behandlung?",
                                 "when": "yes"},
                },
                {
                    "id": "nerven_bewusstsein",
                    "type": "yes_no",
                    "label": "Hatten Sie Bewusstseins- oder Gleichgewichtsstörungen (z.B. "
                             "Ohnmachtsanfälle, ausgeprägten Schwindel) oder eine Erkrankung "
                             "des Nervensystems (z.B. Schlaganfall, Schädel-Hirn-Verletzung, "
                             "Lähmungen)?",
                    "required": True,
                    "followup": {"id": "nerven_bewusstsein_desc", "type": "textarea",
                                 "label": "Was genau, wann, mit welchen Folgen?",
                                 "when": "yes"},
                },
                {
                    "id": "gemuet",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine seelische (psychische) Erkrankung "
                             "(z.B. Depression, Psychose) – auch wenn sie abgeklungen ist?",
                    "hint": "Wichtig ist, ob ein Rückfall sicher ausgeschlossen werden kann.",
                    "required": True,
                    "followup": {"id": "gemuet_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, wann, wie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "klaustrophobie",
                    "type": "yes_no",
                    "label": "Haben Sie Platzangst (Klaustrophobie) oder starke Beklemmung in "
                             "engen Räumen oder unter einer eng anliegenden Maske?",
                    "required": True,
                },
                {
                    "id": "sucht",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Drogen oder Medikamenten?",
                    "required": True,
                },
            ],
        },
        # ── 6 ─ Augen, Ohren, Haut & Zähne ─────────────────────────────────
        {
            "id": "sinne_haut",
            "title": "Augen, Ohren, Haut & Zähne",
            "questions": [
                {
                    "id": "sehen",
                    "type": "yes_no",
                    "label": "Haben Sie eine Augenerkrankung, die Ihr Sehen plötzlich "
                             "verschlechtern kann (z.B. gestörte Lidfunktion, wiederkehrende "
                             "Entzündungen)?",
                    "required": True,
                    "followup": {"id": "sehen_desc", "type": "textarea",
                                 "label": "Welche Erkrankung?",
                                 "when": "yes"},
                },
                {
                    "id": "sehhilfe",
                    "type": "yes_no",
                    "label": "Tragen Sie eine Brille oder Kontaktlinsen?",
                    "hint": "Unter einer Vollmaske kann keine normale Brille getragen werden – "
                            "ggf. ist eine Maskenbrille erforderlich. Bei der Untersuchung "
                            "wird die korrigierte Sehschärfe für Nähe und Ferne geprüft.",
                    "required": True,
                },
                {
                    "id": "hoeren",
                    "type": "yes_no",
                    "label": "Hören Sie schlecht oder tragen Sie ein Hörgerät?",
                    "required": True,
                    "followup": {"id": "hoeren_desc", "type": "textarea",
                                 "label": "Seit wann, auf welchem Ohr, mit/ohne Hörgerät?",
                                 "when": "yes"},
                },
                {
                    "id": "haut",
                    "type": "yes_no",
                    "label": "Haben Sie eine Hauterkrankung – besonders im Gesicht –, die sich "
                             "verschlimmern kann (z.B. Ekzem, Neurodermitis, Allergie)?",
                    "required": True,
                    "followup": {"id": "haut_desc", "type": "textarea",
                                 "label": "Welche Hauterkrankung, an welchen Stellen?",
                                 "when": "yes"},
                },
                {
                    "id": "dichtsitz",
                    "type": "yes_no",
                    "label": "Gibt es an Ihrem Gesicht Veränderungen, die den dichten Sitz der "
                             "Maske stören könnten (z.B. Narben, auch Bartwuchs im Bereich "
                             "der Dichtlinie)?",
                    "required": True,
                },
                {
                    "id": "zahnprothese",
                    "type": "yes_no",
                    "label": "Tragen Sie eine vollständige Zahnprothese (Vollprothese)?",
                    "hint": "Für Geräte mit Mundstück-Anschluss ist eine Vollprothese ein "
                            "Ausschlussgrund.",
                    "required": True,
                    "show_if": {"id": "mundstueck", "in": ["ja", "weiss_nicht"]},
                },
            ],
        },
        # ── 7 ─ Einwilligung ───────────────────────────────────────────────
        {
            "id": "einwilligung",
            "title": "Einwilligung",
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
    # ── kritisch: dauernde gesundheitliche Bedenken / Klärung vor Einsatz ──
    {"wenn": {"alter_gruppe": ["unter18"]},
     "schwere": "kritisch",
     "bereich": "Jugendarbeitsschutz",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Person ist jünger als 18 Jahre",
     "konsequenz": "Dauernde gesundheitliche Bedenken für das Tragen von Atemschutzgeräten "
                   "im Rettungswesen und für Geräte der Gruppe 3; Einsatzplanung entsprechend "
                   "beschränken."},
    {"wenn": {"alter_gruppe": ["ab50"], "rettungswesen": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Alter/Rettungswesen",
     "quelle": "Abschnitt 2.1.1 und 2.1.3",
     "befund": "Person über 50 Jahre mit Einsatz im Rettungswesen",
     "konsequenz": "In der Regel dauernde gesundheitliche Bedenken für Rettungswesen und "
                   "Geräte der Gruppe 3. Ausnahme nach 2.1.3 prüfen: bei langjähriger "
                   "Berufserfahrung und/oder fehlender Gefährdung für sich oder Dritte können "
                   "die Bedenken durch verkürzte Nachuntersuchungsfristen zurückgestellt "
                   "werden; alternativ weniger belastende Gerätegruppe oder "
                   "Überwachungstätigkeit zuweisen."},
    {"wenn": {"anfallsleiden": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 2.1.1 (Anfallsleiden)",
     "befund": "Anfallsleiden (Epilepsie/Krampfanfälle) angegeben",
     "konsequenz": "Klärung vor Einsatz: Beurteilung nach Art, Häufigkeit, Prognose und "
                   "Behandlungsstand gemäß DGUV Information 250-001 (Empfehlungen zur "
                   "Beurteilung beruflicher Möglichkeiten von Personen mit Epilepsie); "
                   "neurologische Unterlagen anfordern. Für Gruppe 2/3 Ausschlussgrund, bei "
                   "Gruppe 1 abhängig von den Expositionsbedingungen."},
    {"wenn": {"nerven_bewusstsein": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 2.1.1 (Bewusstseins-/Gleichgewichtsstörungen, ZNS/PNS-Erkrankungen)",
     "befund": "Bewusstseins-/Gleichgewichtsstörung oder Erkrankung des Nervensystems angegeben",
     "konsequenz": "Ausschlussgrund in allen Gerätegruppen: neurologische Abklärung "
                   "(Ergänzungsuntersuchung) veranlassen; bis zur Klärung keine Tätigkeit "
                   "unter Atemschutz."},
    {"wenn": {"gemuet": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Psyche",
     "quelle": "Abschnitt 2.1.1 (Gemüts- oder Geisteskrankheiten)",
     "befund": "Seelische (psychische) Erkrankung angegeben (auch abgeklungen)",
     "konsequenz": "Ausschlussgrund in allen Gerätegruppen, solange ein Rückfall nicht "
                   "hinreichend sicher ausgeschlossen werden kann: fachärztliche "
                   "(psychiatrische) Abklärung vor Einsatz veranlassen."},
    {"wenn": {"klaustrophobie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Psyche",
     "quelle": "Abschnitt 2.1.1 (abnorme Verhaltensweisen, z.B. Klaustrophobie)",
     "befund": "Platzangst/Beklemmung in engen Räumen oder unter Maske angegeben",
     "konsequenz": "Bei erheblichem Grad Ausschlussgrund in allen Gerätegruppen: Ausprägung "
                   "ärztlich bewerten, ggf. Belastungserprobung mit Gerät unter Aufsicht und "
                   "fachärztliche Abklärung vor Einsatz."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Sucht",
     "quelle": "Abschnitt 2.1.1 (Alkohol-, Suchtmittel-, Medikamentenabhängigkeit)",
     "befund": "Abhängigkeit von Alkohol, Drogen oder Medikamenten angegeben",
     "konsequenz": "Ausschlussgrund in allen Gerätegruppen: Abstinenz/Behandlungsstand klären, "
                   "suchtmedizinische Unterlagen anfordern; bis zur Klärung keine Tätigkeit "
                   "unter Atemschutz."},
    {"wenn": {"lunge": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atmungsorgane",
     "quelle": "Abschnitt 2.1.1 (Atmungsorgane, Brustkorb); 1.2.2 (Spirometrie, Röntgen-Thorax)",
     "befund": "Erkrankung der Atemwege, der Lunge oder des Brustkorbs angegeben",
     "konsequenz": "Klärung vor Einsatz: Spirometrie nach Anhang 1 „Leitfaden "
                   "Lungenfunktionsprüfung“ durchführen; bei medizinischer Indikation "
                   "Röntgenaufnahme des Thorax (p.a.); bei stärkerer Funktionsbeeinträchtigung "
                   "(z.B. Asthma, COPD, Emphysem, verminderte Vital-/Einsekundenkapazität) "
                   "Ausschlussgrund in allen Gerätegruppen – pneumologische "
                   "Ergänzungsuntersuchung."},
    {"wenn": {"herz_kreislauf": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 2.1.1 (Herz-/Kreislauferkrankungen); 1.2.2 (Ruhe-EKG, Ergometrie)",
     "befund": "Herz-/Kreislauferkrankung angegeben (z.B. Z.n. Herzinfarkt, "
               "Blutdruckveränderungen stärkeren Grades)",
     "konsequenz": "Klärung vor Einsatz: Ruhe-EKG und Ergometrie unter "
                   "leistungsphysiologischer Indikation nach Anhang 2 „Leitfaden Ergometrie“ "
                   "durchführen (bei Gruppe 2 abhängig von Befund, Belastung und Alter, bei "
                   "Gruppe 3 obligat); ggf. kardiologische Ergänzungsuntersuchung. Für "
                   "Gruppe 2/3 Ausschlussgrund, bei Gruppe 1 abhängig von den "
                   "Expositionsbedingungen."},
    {"wenn": {"koerperschwaeche": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Belastbarkeit",
     "quelle": "Abschnitt 2.1.1 (allgemeine Körperschwäche); 1.2.2 (Ergometrie)",
     "befund": "Allgemeine Körperschwäche / rasche Erschöpfbarkeit angegeben",
     "konsequenz": "Ausschlussgrund in allen Gerätegruppen: Belastbarkeit mittels Ergometrie "
                   "prüfen. Sollwerte bei hochbelastenden Tätigkeiten (z.B. Feuerwehr): bis "
                   "39 Jahre Männer 3,0 W/kg, Frauen 2,5 W/kg (W170); ab 40 Jahren Männer "
                   "2,1 W/kg, Frauen 1,8 W/kg (W150)."},
    {"wenn": {"sehen": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Augen",
     "quelle": "Abschnitt 2.1.1 (Erkrankungen der Augen); 1.2.2 (korrigierte Sehschärfe)",
     "befund": "Augenerkrankung mit möglicher akuter Beeinträchtigung der Sehfunktion angegeben",
     "konsequenz": "Ausschlussgrund in allen Gerätegruppen: augenärztliche Abklärung vor "
                   "Einsatz; korrigierte Sehschärfe Nähe und Ferne prüfen (für Gruppe 2/3 "
                   "relevant: Ferne unter 0,7/0,7 bzw. 0,8 bei langjähriger Einäugigkeit, "
                   "Nähe unter 0,5/0,5 bzw. 0,6)."},
    {"wenn": {"dichtsitz": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemanschluss",
     "quelle": "Abschnitt 2.1.1 (Veränderungen, die den Dichtsitz beeinträchtigen)",
     "befund": "Veränderungen im Gesicht, die den Dichtsitz des Atemanschlusses stören können",
     "konsequenz": "Ausschlussgrund in allen Gerätegruppen: Dichtsitz vor Einsatz prüfen "
                   "(Trageversuch); ggf. anderen Atemanschluss wählen oder Ursache (z.B. Bart "
                   "im Dichtbereich) beseitigen lassen."},
    {"wenn": {"zahnprothese": ["yes"], "mundstueck": ["ja", "weiss_nicht"]},
     "schwere": "kritisch",
     "bereich": "Atemanschluss",
     "quelle": "Abschnitt 2.1.1 (Zahnvollprothesen bei Mundstückatemanschluss)",
     "befund": "Vollprothese bei (möglichem) Mundstück-Atemanschluss",
     "konsequenz": "Kein Einsatz mit Mundstückatemanschluss; Gerätetyp klären und auf "
                   "Atemanschluss ohne Mundstück (z.B. Vollmaske) ausweichen."},
    {"wenn": {"hernie": ["yes"], "geraetegruppe": ["gruppe2", "gruppe3", "unbekannt"]},
     "schwere": "kritisch",
     "bereich": "Eingeweidebruch",
     "quelle": "Abschnitt 2.1.1 (Eingeweidebrüche; Ausschlussgrund Gruppe 2/3)",
     "befund": "Nicht versorgter Eingeweidebruch bei Gerätegruppe 2/3",
     "konsequenz": "Ausschlussgrund für Geräte der Gruppe 2 und 3 (für Gruppe 1 kein "
                   "Ausschlussgrund): chirurgische Vorstellung/Versorgung veranlassen; bis "
                   "dahin nur Tätigkeit mit Gruppe-1-Gerät oder Überwachungstätigkeit "
                   "erwägen."},
    # ── pruefen: Ergänzungsuntersuchung / Abklärung ────────────────────────
    {"wenn": {"bewegungsapparat": ["yes"],
              "geraetegruppe": ["gruppe2", "gruppe3", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Bewegungsapparat",
     "quelle": "Abschnitt 2.1.1 (Stütz-/Bewegungsapparat; Ausschlussgrund Gruppe 2/3)",
     "befund": "Einschränkung des Stütz-/Bewegungsapparats bei Gerätegruppe 2/3",
     "konsequenz": "Ausmaß der Funktionsstörung prüfen (Untersuchung, ggf. orthopädische "
                   "Abklärung); bei stärkerer Funktionsstörung Ausschlussgrund für "
                   "Gruppe 2/3 – nach 2.1.3 weniger belastende Gerätegruppe oder "
                   "Überwachungstätigkeit erwägen."},
    {"wenn": {"haut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 2.1.1 (zur Verschlimmerung neigende Hautkrankheiten)",
     "befund": "Zur Verschlimmerung neigende Hauterkrankung angegeben",
     "konsequenz": "Dermatologische Abklärung veranlassen; Hautzustand im Dichtbereich des "
                   "Atemanschlusses beurteilen. Für Gruppe 2/3 Ausschlussgrund, bei Gruppe 1 "
                   "abhängig von den Expositionsbedingungen."},
    {"wenn": {"hoeren": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gehör",
     "quelle": "Abschnitt 2.1.1 (Hörverlust, Schwerhörigkeit); 1.2.2 (Hörtest 1–6 kHz, Otoskopie)",
     "befund": "Schwerhörigkeit bzw. Hörgerät angegeben",
     "konsequenz": "Hörtest Luftleitung 1–6 kHz durchführen (für Geräte der Gruppe 2/3 mit "
                   "Pfeifton). Hörverlust über 40 dB bei 2 kHz auf dem besseren Ohr ist "
                   "Ausschlussgrund für den Einsatz im Rettungswesen; sicherstellen, dass die "
                   "akustische Warneinrichtung (Pfeifton) wahrgenommen wird. Bei möglicher "
                   "Aufnahme von Gasen/Dämpfen über den Gehörgang zusätzlich Otoskopie."},
    {"wenn": {"stoffwechsel_gewicht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechsel/Gewicht",
     "quelle": "Abschnitt 2.1.1 (Stoffwechselkrankheiten, Übergewicht); 1.2.2 (Blutzucker)",
     "befund": "Stoffwechsel-/Hormonerkrankung oder starkes Übergewicht angegeben",
     "konsequenz": "Nüchtern-Blutzucker bestimmen (bei auffälligem Gelegenheits-Blutzucker); "
                   "ggf. endokrinologische Abklärung (Schilddrüse, Nebennieren). Übergewicht "
                   "über 30 % nach Broca bzw. BMI über 30 sowie belastbarkeitseinschränkende "
                   "Stoffwechselkrankheiten sind Ausschlussgrund für Gruppe 2/3; Belastbarkeit "
                   "mittels Ergometrie prüfen."},
    {"wenn": {"seit_letzter": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenanamnese",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung); 1.2.1 (Zwischenanamnese)",
     "befund": "Mehrwöchige Erkrankung, Probleme beim Tragen des Geräts oder vermuteter "
               "Zusammenhang zwischen Beschwerden und Tätigkeit seit letzter Untersuchung",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt: kardiale und pulmonale "
                   "Zwischenanamnese gezielt abklären (Spirometrie, Ruhe-EKG, ggf. "
                   "Ergometrie); bis zur Klärung Bedenken gegen Weiterbeschäftigung unter "
                   "Atemschutz erwägen."},
    # ── hinweis: Fristen ───────────────────────────────────────────────────
    {"wenn": {"alter_gruppe": ["ab50"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfristen",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Person ist 50 Jahre oder älter",
     "konsequenz": "Verkürzte Nachuntersuchungsfrist einplanen: bei Gerätegewicht bis 5 kg "
                   "Nachuntersuchung vor Ablauf von 24 Monaten, über 5 kg vor Ablauf von "
                   "12 Monaten (bis 50 Jahre gilt: vor Ablauf von 36 Monaten); nächsten "
                   "Termin auf der Bescheinigung entsprechend festlegen."},
]
