# -*- coding: utf-8 -*-
"""
Atemschutzgeräte – DGUV Empfehlung 2024.

Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und
Untersuchungen (2024), Kapitel „Atemschutzgeräte“:
Arbeitsmedizinische Vorsorge S. 997–1013 und Eignungsbeurteilung
S. 1065–1081 (jeweils Fassung Januar 2022).

Hinweis: Die Empfehlung trennt strikt zwischen arbeitsmedizinischer
Vorsorge nach ArbMedVV (Pflichtvorsorge bei Gerätegruppe 2/3,
Angebotsvorsorge bei Gruppe 1) und Eignungsbeurteilung (eigene
Rechtsgrundlage erforderlich, z.B. GesBergV/Offshore-BergV). Feste
G-26-Nachuntersuchungsfristen gibt es nicht mehr; für die Vorsorge gilt
die AMR 2.1, für Eignungsbeurteilungen die jeweilige Rechtsgrundlage.
"""

SLUG = "atemschutz-2024"

CATALOG = {
    "version": 2,
    "title": "Atemschutzgeräte (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen "
             "(2024), Kapitel „Atemschutzgeräte“: Arbeitsmedizinische Vorsorge "
             "S. 997–1013 und Eignungsbeurteilung S. 1065–1081 (Fassung Januar 2022)",
    "sections": [
        # ── 1 ─────────────────────────────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Atemschutzgerät",
            "subtitle": "Angaben zu Ihrem Einsatz mit Atemschutz (Arbeitsanamnese)",
            "questions": [
                {
                    "id": "untersuchungsanlass",
                    "type": "choice",
                    "label": "Aus welchem Anlass sind Sie heute hier?",
                    "hint": "Arbeitsmedizinische Vorsorge (ArbMedVV) und Eignungsbeurteilung "
                            "sind getrennte Verfahren. Wenn Sie unsicher sind, fragen Sie Ihren "
                            "Arbeitgeber oder das Praxisteam.",
                    "required": True,
                    "options": [
                        {"value": "vorsorge_erst", "label": "Erste arbeitsmedizinische Vorsorge"},
                        {"value": "vorsorge_weitere", "label": "Weitere (wiederholte) arbeitsmedizinische Vorsorge"},
                        {"value": "eignung_erst", "label": "Erste Eignungsbeurteilung"},
                        {"value": "eignung_weitere", "label": "Erneute (anlassbezogene) Eignungsbeurteilung"},
                    ],
                },
                {
                    "id": "geraetegruppe",
                    "type": "choice",
                    "label": "Zu welcher Gruppe gehört das Atemschutzgerät, das Sie tragen (sollen)?",
                    "hint": "Die Einteilung richtet sich nach Gewicht und Atemwiderstand des Geräts "
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
                    "id": "geraet_typ",
                    "type": "multi_choice",
                    "label": "Welche Art von Atemschutz benutzen Sie (voraussichtlich)?",
                    "required": True,
                    "options": [
                        {"value": "filtergeraet", "label": "Filtergerät / Maske mit Filter (abhängig von der Umgebungsluft)"},
                        {"value": "pressluftatmer", "label": "Pressluftatmer (Druckluftflasche auf dem Rücken)"},
                        {"value": "regenerationsgeraet", "label": "Regenerationsgerät (Kreislaufgerät)"},
                        {"value": "schlauchgeraet", "label": "Schlauchgerät (Luftzufuhr über Schlauch)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "mundstueck",
                    "type": "choice",
                    "label": "Hat Ihr Gerät einen Mundstück-Anschluss (Sie beißen auf ein Mundstück, "
                             "statt eine Maske über Nase und Mund zu tragen)?",
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
                    "hint": "Für Geräte der Gruppe 2 und 3 mit Pfeifton ist ein Hörtest "
                            "(Luftleitung 1–6 kHz) Teil der Untersuchung.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "weiss_nicht", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "einsatz_bereiche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen setzen Sie Atemschutz ein (oder sollen Sie ihn einsetzen)?",
                    "required": True,
                    "options": [
                        {"value": "enge_raeume", "label": "Behälter und enge Räume (z.B. Tankreinigung)"},
                        {"value": "hoehen_tiefen", "label": "Arbeiten in Höhen oder Tiefen"},
                        {"value": "hitze", "label": "Hohe Umgebungstemperatur / Wärmestrahlung"},
                        {"value": "schlechte_sicht", "label": "Bereiche mit schlechter Sicht"},
                        {"value": "keine", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "rettung",
                    "type": "yes_no",
                    "label": "Gehören Rettungseinsätze zu Ihren Aufgaben (z.B. Feuerwehr, "
                             "Grubenwehr, Gasschutzwehr)?",
                    "hint": "Bei Rettungskräften ist eine hohe körperliche Belastung unumgänglich. "
                            "Zur Prüfung der Belastbarkeit werden Ergometrie oder Spiroergometrie "
                            "(Belastungsuntersuchungen) empfohlen.",
                    "required": True,
                },
                {
                    "id": "tragedauer",
                    "type": "choice",
                    "label": "Wie lange tragen Sie das Atemschutzgerät üblicherweise am Stück?",
                    "hint": "Tätigkeiten mit Atemschutz über 30 Minuten Dauer gelten als "
                            "höher belastend.",
                    "required": True,
                    "options": [
                        {"value": "bis30", "label": "Bis 30 Minuten"},
                        {"value": "ueber30", "label": "Mehr als 30 Minuten"},
                        {"value": "unbekannt", "label": "Noch unklar / wechselnd"},
                    ],
                },
                {
                    "id": "zusatz_schutzkleidung",
                    "type": "yes_no",
                    "label": "Tragen Sie zusätzlich zum Atemschutz besondere Schutzkleidung "
                             "(z.B. Chemikalien- oder Hitzeschutzanzug)?",
                    "hint": "Zusätzliche Schutzkleidung bedeutet eine zusätzliche Belastung "
                            "durch Wärme und Flüssigkeitsverlust.",
                    "required": True,
                },
            ],
        },
        # ── 2 ─────────────────────────────────────────────────────────────
        {
            "id": "person",
            "title": "Angaben zur Person",
            "questions": [
                {
                    "id": "alter_unter_18",
                    "type": "yes_no",
                    "label": "Sind Sie jünger als 18 Jahre?",
                    "hint": "Für Jugendliche unter 18 Jahren besteht ein Beschäftigungsverbot "
                            "für Atemschutz im Rettungswesen und für Geräte der Gruppe 3.",
                    "required": True,
                },
                {
                    "id": "schwanger",
                    "type": "choice",
                    "label": "Besteht bei Ihnen aktuell eine Schwangerschaft?",
                    "hint": "Für Schwangere besteht ein Beschäftigungsverbot für das Tragen "
                            "von belastendem Atemschutz.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "entfaellt", "label": "Entfällt"},
                    ],
                },
                {
                    "id": "raucher",
                    "type": "yes_no",
                    "label": "Rauchen Sie?",
                    "hint": "Diese Angabe fließt in die Ermittlung Ihres individuellen "
                            "Herz-Kreislauf-Risikos ein (Risiko-Score, z.B. JBS3, PROCAM, "
                            "ESC-Score, Framingham).",
                    "required": True,
                },
            ],
        },
        # ── 3 ─────────────────────────────────────────────────────────────
        {
            "id": "koerper",
            "title": "Herz, Kreislauf & körperliche Belastbarkeit",
            "subtitle": "Vorerkrankungen und Belastbarkeit",
            "questions": [
                {
                    "id": "herz_kreislauf",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung des Herzens oder des "
                             "Kreislaufs (z.B. Herzinfarkt, Herzschwäche, Herzrhythmusstörungen, "
                             "stark erhöhter Blutdruck)?",
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
                    "label": "Wurde bei Ihnen eine Stoffwechselerkrankung (z.B. Zuckerkrankheit/"
                             "Diabetes) oder starkes Übergewicht (BMI über 30) festgestellt?",
                    "required": True,
                    "followup": {"id": "stoffwechsel_gewicht_desc", "type": "textarea",
                                 "label": "Was wurde festgestellt, wie wird es behandelt?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 4 ─────────────────────────────────────────────────────────────
        {
            "id": "atmung",
            "title": "Atmung & Lunge",
            "questions": [
                {
                    "id": "lunge",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung der Atemwege, der Lunge "
                             "oder des Brustkorbs (z.B. Asthma bronchiale, COPD/chronische "
                             "Bronchitis, Lungenemphysem, Brustkorbverletzung oder -operation)?",
                    "required": True,
                    "followup": {"id": "lunge_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, wie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "beschwerden_belastung",
                    "type": "yes_no",
                    "label": "Haben Sie bei körperlicher Belastung oder beim Tragen von "
                             "Atemschutz Beschwerden – z.B. Atemnot, Kreislaufprobleme "
                             "(Schwindel, Herzrasen) oder Schmerzen im Bewegungsapparat?",
                    "required": True,
                    "followup": {"id": "beschwerden_belastung_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, in welchen Situationen?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 5 ─────────────────────────────────────────────────────────────
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
                    "id": "psych",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine psychische Erkrankung (z.B. Depression, "
                             "Angststörung, Psychose) – auch wenn sie ausgeheilt ist?",
                    "hint": "Relevant ist, ob ein Rückfall sicher ausgeschlossen werden kann.",
                    "required": True,
                    "followup": {"id": "psych_desc", "type": "textarea",
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
        # ── 6 ─────────────────────────────────────────────────────────────
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
                            "ggf. ist eine Maskenbrille erforderlich. Bei der Untersuchung wird "
                            "die korrigierte Sehschärfe für Nähe und Ferne geprüft.",
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
                             "Maske stören könnten (z.B. Narben, auch Bartwuchs im Bereich der "
                             "Dichtlinie)?",
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
        # ── 7 ─────────────────────────────────────────────────────────────
        {
            "id": "verlauf",
            "title": "Bisherige Erfahrungen mit Atemschutz",
            "questions": [
                {
                    "id": "frueher_probleme",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Vorsorge bzw. Beurteilung "
                             "gesundheitliche Probleme beim Tragen von Atemschutzgeräten "
                             "(z.B. Atemnot, Kreislaufprobleme, Panikgefühl, Hautreaktionen)?",
                    "required": True,
                    "show_if": {"id": "untersuchungsanlass",
                                "in": ["vorsorge_weitere", "eignung_weitere"]},
                    "followup": {"id": "frueher_probleme_desc", "type": "textarea",
                                 "label": "Welche Probleme, in welcher Situation?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 8 ─────────────────────────────────────────────────────────────
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
    # ── kritisch: Klärung vor Einsatz / spricht i.d.R. gegen die Tätigkeit ──
    {"wenn": {"anfallsleiden": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien, Anfallsleiden)",
     "befund": "Anfallsleiden (Epilepsie/Krampfanfälle) angegeben",
     "konsequenz": "Klärung vor Einsatz: Beurteilung nach Art, Häufigkeit, Prognose und "
                   "Behandlungsstand gemäß DGUV Information 250-001; neurologische Unterlagen "
                   "anfordern. Bei Gerätegruppe 2/3 hohe Relevanz – i.d.R. keine Eignung "
                   "(7.4.4); bei Gruppe 1 Relevanz abhängig von den Expositionsbedingungen."},
    {"wenn": {"nerven_bewusstsein": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 7.4 (Bewusstseins-/Gleichgewichtsstörungen, ZNS/PNS-Erkrankungen)",
     "befund": "Bewusstseins-/Gleichgewichtsstörung oder Erkrankung des Nervensystems angegeben",
     "konsequenz": "Klärung vor Einsatz: neurologische Abklärung (Ergänzungsuntersuchung) "
                   "veranlassen; hohe Relevanz in allen Gerätegruppen. Bis zur Klärung keine "
                   "Tätigkeit unter Atemschutz."},
    {"wenn": {"psych": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Psyche",
     "quelle": "Abschnitt 7.4 (psychische Erkrankungen)",
     "befund": "Psychische Erkrankung angegeben (auch abgeklungen)",
     "konsequenz": "Klärung vor Einsatz: fachärztlich (psychiatrisch/psychotherapeutisch) "
                   "abklären, ob ein Rückfall hinreichend sicher ausgeschlossen werden kann; "
                   "hohe Relevanz in allen Gerätegruppen."},
    {"wenn": {"klaustrophobie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Psyche",
     "quelle": "Abschnitt 7.4 (abnorme Verhaltensweisen, z.B. Klaustrophobie)",
     "befund": "Platzangst/Beklemmung in engen Räumen oder unter Maske angegeben",
     "konsequenz": "Klärung vor Einsatz: Ausprägung ärztlich bewerten (erheblicher Grad = hohe "
                   "Relevanz in allen Gruppen); ggf. Belastungserprobung mit Gerät unter "
                   "Aufsicht und psychologische/fachärztliche Abklärung."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Sucht",
     "quelle": "Abschnitt 7.4 (Alkohol-, Suchtmittel-, Medikamentenabhängigkeit)",
     "befund": "Abhängigkeit von Alkohol, Drogen oder Medikamenten angegeben",
     "konsequenz": "Klärung vor Einsatz: Abstinenz/Behandlungsstand klären, suchtmedizinische "
                   "Unterlagen anfordern; hohe Relevanz in allen Gerätegruppen."},
    {"wenn": {"lunge": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atmungsorgane",
     "quelle": "Abschnitt 7.4 (Erkrankungen der Atmungsorgane/des Brustkorbs); 7.2.2 Spirometrie",
     "befund": "Erkrankung der Atemwege, der Lunge oder des Brustkorbs angegeben",
     "konsequenz": "Klärung vor Einsatz: Spirometrie einschließlich Fluss-Volumen-Kurve "
                   "(Anhang 1 „Leitfaden Lungenfunktionsprüfung“) durchführen; bei stärkerer "
                   "Funktionsbeeinträchtigung (z.B. Asthma, COPD, Emphysem) pneumologische "
                   "Ergänzungsuntersuchung – hohe Relevanz in allen Gerätegruppen."},
    {"wenn": {"herz_kreislauf": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 7.4 (Herz-/Kreislauferkrankungen); 7.2.2 (EKG, Ergometrie/Spiroergometrie)",
     "befund": "Herz-/Kreislauferkrankung angegeben (z.B. Z.n. Herzinfarkt, Blutdruckveränderungen "
               "stärkeren Grades)",
     "konsequenz": "Klärung vor Einsatz: Ruhe-EKG und Leistungsdiagnostik (Ergometrie, bei "
                   "schwerem Atemschutz Gruppe 2/3 bevorzugt Spiroergometrie) durchführen; "
                   "kardiovaskulären Risiko-Score (JBS3/PROCAM/ESC/Framingham) bestimmen. Bei "
                   "erhöhtem Risiko Prozess unterbrechen und fachärztliche (kardiologische) "
                   "Untersuchung einleiten (7.2.2 „Ergänzend“). Bei Gruppe 1 Relevanz abhängig "
                   "von den Expositionsbedingungen."},
    {"wenn": {"koerperschwaeche": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Belastbarkeit",
     "quelle": "Abschnitt 7.4 (allgemeine Körperschwäche)",
     "befund": "Allgemeine Körperschwäche / rasche Erschöpfbarkeit angegeben",
     "konsequenz": "Klärung vor Einsatz: Leistungsdiagnostik (Ergometrie/Spiroergometrie nach "
                   "Anhang 2 „Leitfaden Ergometrie“) durchführen; hohe Relevanz in allen "
                   "Gerätegruppen."},
    {"wenn": {"dichtsitz": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemanschluss",
     "quelle": "Abschnitt 7.4 (Veränderungen, die den Dichtsitz beeinträchtigen)",
     "befund": "Veränderungen im Gesicht, die den Dichtsitz des Atemanschlusses stören können",
     "konsequenz": "Vor Einsatz Dichtsitz prüfen (z.B. Trageversuch/Fit-Test); hohe Relevanz in "
                   "allen Gerätegruppen. Ggf. anderen Atemanschluss wählen oder Ursache "
                   "(z.B. Bart im Dichtbereich) beseitigen lassen."},
    {"wenn": {"zahnprothese": ["yes"], "mundstueck": ["ja", "weiss_nicht"]},
     "schwere": "kritisch",
     "bereich": "Atemanschluss",
     "quelle": "Abschnitt 7.4 (Zahnvollprothesen bei Mundstückatemanschluss)",
     "befund": "Vollprothese bei (möglichem) Mundstück-Atemanschluss",
     "konsequenz": "Kein Einsatz mit Mundstückatemanschluss; Gerätetyp klären und auf "
                   "Atemanschluss ohne Mundstück (z.B. Vollmaske) ausweichen."},
    {"wenn": {"sehen": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Augen",
     "quelle": "Abschnitt 7.4 (Erkrankungen der Augen); 7.2.2 (Sehschärfe Nähe/Ferne)",
     "befund": "Augenerkrankung mit möglicher akuter Beeinträchtigung der Sehfunktion angegeben",
     "konsequenz": "Klärung vor Einsatz: augenärztliche Abklärung; Sehschärfe Nähe und Ferne "
                   "prüfen (Grenzwerte für Gruppe 2/3: Ferne unter 0,7/0,7 bzw. Nähe unter "
                   "0,5/0,5 relevant)."},
    {"wenn": {"schwanger": ["ja"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 6.4 (Besondere gesundheitliche Aspekte)",
     "befund": "Schwangerschaft angegeben",
     "konsequenz": "Beschäftigungsverbot für das Tragen von belastendem Atemschutz; Arbeitgeber "
                   "über erforderliche Umsetzung informieren (mit Einwilligung der Person)."},
    {"wenn": {"alter_unter_18": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Jugendarbeitsschutz",
     "quelle": "Abschnitt 6.4 (Besondere gesundheitliche Aspekte)",
     "befund": "Person ist jünger als 18 Jahre",
     "konsequenz": "Beschäftigungsverbot für das Tragen von Atemschutzgeräten im Rettungswesen "
                   "und für Geräte der Gruppe 3 beachten; Einsatzplanung entsprechend "
                   "beschränken."},
    # ── pruefen: Ergänzungsuntersuchung / Abklärung ────────────────────────
    {"wenn": {"beschwerden_belastung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitt 7.1 (Beschwerden: Kreislauf, pulmonal, Bewegungsapparat)",
     "befund": "Beschwerden bei Belastung bzw. unter Atemschutz angegeben",
     "konsequenz": "Beschwerden gezielt abklären (Spirometrie, Ruhe-EKG, ggf. Ergometrie/"
                   "Spiroergometrie); Arbeitsplatzbedingungen und Tragezeiten berücksichtigen, "
                   "ggf. Rückmeldung an das Unternehmen zu Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"bewegungsapparat": ["yes"],
              "geraetegruppe": ["gruppe2", "gruppe3", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Bewegungsapparat",
     "quelle": "Abschnitt 7.4 (Stütz-/Bewegungsapparat; Relevanz Gruppe 2/3)",
     "befund": "Einschränkung des Stütz-/Bewegungsapparats bei Gerätegruppe 2/3",
     "konsequenz": "Ausmaß der Funktionsstörung prüfen (Untersuchung, ggf. orthopädische "
                   "Abklärung); bei stärkerer Funktionsstörung Relevanz für Gruppe 2/3 – "
                   "Maßnahmen nach 7.4.2 (z.B. Begrenzung der Expositionszeit, weniger "
                   "belastende Gerätegruppe) oder Tätigkeitswechsel (7.4.4) erwägen."},
    {"wenn": {"haut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 7.4 (zur Verschlimmerung neigende Hautkrankheiten)",
     "befund": "Zur Verschlimmerung neigende Hauterkrankung angegeben",
     "konsequenz": "Dermatologische Abklärung veranlassen; Hautzustand im Dichtbereich des "
                   "Atemanschlusses beurteilen. Relevanz bei Gruppe 2/3 hoch, bei Gruppe 1 "
                   "abhängig von den Expositionsbedingungen."},
    {"wenn": {"hoeren": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gehör",
     "quelle": "Abschnitt 7.4 (Hörverlust/Schwerhörigkeit); 7.2.2 (Hörtest 1–6 kHz)",
     "befund": "Schwerhörigkeit bzw. Hörgerät angegeben",
     "konsequenz": "Hörtest Luftleitung 1–6 kHz durchführen. Relevant: Hörverlust über 40 dB "
                   "bei 2 kHz auf dem besseren Ohr bei erforderlicher Kommunikation sowie "
                   "Wahrnehmbarkeit der akustischen Warneinrichtung (Pfeifton) bei Geräten der "
                   "Gruppe 2/3 – sicherstellen, dass das Warnsignal wahrgenommen wird."},
    {"wenn": {"stoffwechsel_gewicht": ["yes"],
              "geraetegruppe": ["gruppe2", "gruppe3", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechsel/Gewicht",
     "quelle": "Abschnitt 7.4 (Stoffwechselkrankheiten; Übergewicht BMI > 30); 7.2.2 (Blutzucker)",
     "befund": "Stoffwechselerkrankung oder starkes Übergewicht bei Gerätegruppe 2/3",
     "konsequenz": "Gelegenheits- bzw. Nüchtern-Blutzucker, ggf. HbA1c bestimmen; BMI ermitteln "
                   "(Grenzwert BMI > 30 bzw. Broca +30 %); Belastbarkeit mittels Ergometrie/"
                   "Spiroergometrie prüfen und Beratung zu Ernährung und Fitness anbieten."},
    {"wenn": {"frueher_probleme": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Verlauf",
     "quelle": "Abschnitt 7.1 (weitere Vorsorgen/anlassbezogene erneute Beurteilung)",
     "befund": "Gesundheitliche Probleme beim Tragen von Atemschutz seit letzter Vorsorge/Beurteilung",
     "konsequenz": "Ursache vor weiterem Einsatz abklären (gezielte Untersuchung nach "
                   "Beschwerdebild); ggf. Maßnahmen nach 7.4.2 vorschlagen und verkürzte "
                   "Wiedervorstellung (7.4.3) vereinbaren."},
    # ── hinweis: Verfahren/Beratung ────────────────────────────────────────
    {"wenn": {"geraetegruppe": ["gruppe2", "gruppe3"]},
     "schwere": "hinweis",
     "bereich": "Verfahren/Fristen",
     "quelle": "Abschnitt 2 (Pflichtvorsorge), 7.2.2 (Spiroergometrie), 7.3 (Fristen)",
     "befund": "Tätigkeit mit Atemschutzgerät der Gruppe 2 oder 3",
     "konsequenz": "Pflichtvorsorge nach ArbMedVV erforderlich (Fristen nach AMR 2.1; bei "
                   "Eignungsbeurteilungen gelten vorrangig die Fristen der jeweiligen "
                   "Rechtsgrundlage, z.B. GesBergV). Für Träger von schwerem Atemschutz wird "
                   "die Spiroergometrie als Leistungsdiagnostik empfohlen; Untersuchungsumfang "
                   "nach Tabelle 7.2.2 (u.a. Blutbild, Urinstatus, ALAT, Gamma-GT, Kreatinin, "
                   "Blutzucker, Ruhe-EKG, Seh- und Hörtest)."},
]
