# -*- coding: utf-8 -*-
"""Alkylquecksilberverbindungen – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen
für arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Alkylquecksilberverbindungen« (E OHG, Fassung Januar 2022), S. 31–49."""

SLUG = "quecksilber-alkyl-2024"

CATALOG = {
    "version": 2,
    "title": "Alkylquecksilberverbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Alkylquecksilberverbindungen« (E OHG, "
             "Fassung Januar 2022), S. 31–49",
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
                             "Alkylquecksilberverbindungen (organische Quecksilberverbindungen)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge zu diesem Stoff"},
                        {"value": "weitere", "label": "Nein, ich war deswegen schon einmal zur Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der Stoff über "
                            "die Haut aufgenommen werden kann und eine Gefährdung durch Hautkontakt "
                            "nicht ausgeschlossen ist – das trifft auf Alkylquecksilberverbindungen "
                            "in der Regel zu. Angebotsvorsorge: wenn eine Belastung nicht "
                            "ausgeschlossen werden kann.",
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
            "title": "Tätigkeit & Umgang mit dem Stoff",
            "subtitle": "Ihre Arbeit mit Alkylquecksilberverbindungen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "arbeitsbereiche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen haben Sie mit Alkylquecksilberverbindungen zu tun?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "thiomersal", "label": "Herstellung oder Verwendung von Thiomersal "
                                                         "(Konservierungsmittel, z. B. für Impfstoffe, Augentropfen)"},
                        {"value": "synthese", "label": "Chemische Industrie (metallorganisches Synthesereagenz)"},
                        {"value": "forschung", "label": "Biochemische oder biologische Forschung / Labor"},
                        {"value": "antifouling", "label": "Sanierung oder Verschrottung von Teilen mit "
                                                          "Antifoulingfarben (z. B. Schiffsanstriche)"},
                        {"value": "altlasten", "label": "Altlastenbeseitigung (z. B. alte Saatgutbeizen "
                                                        "in agrochemischen Betrieben)"},
                        {"value": "sonstige", "label": "Sonstige Bereiche"},
                        {"value": "keine", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "dimethyl",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Dimethylquecksilber oder anderen flüssigen "
                             "Dialkylquecksilberverbindungen?",
                    "hint": "Diese Stoffe sind extrem giftig: Schon wenige Tropfen auf der Haut "
                            "können tödlich sein. Es gelten besondere Anforderungen an die "
                            "Schutzhandschuhe.",
                    "required": True,
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Hatten Sie bei der Arbeit schon einmal direkten Hautkontakt mit "
                             "Alkylquecksilberverbindungen (z. B. Spritzer auf Haut oder Handschuh)?",
                    "required": True,
                    "followup": {"id": "hautkontakt_desc", "type": "textarea",
                                 "label": "Wann war das, um welchen Stoff ging es, und was wurde "
                                          "danach unternommen?", "when": "yes"},
                },
                {
                    "id": "zwischenfall",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle, Unfälle oder ungewöhnliche "
                             "Betriebszustände, bei denen der Stoff freigesetzt wurde?",
                    "required": True,
                    "followup": {"id": "zwischenfall_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_exposition",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Tätigkeiten Quecksilber oder "
                             "Quecksilberverbindungen ausgesetzt?",
                    "required": True,
                    "followup": {"id": "frueher_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "laermbereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie bei diesen Tätigkeiten auch in Lärmbereichen "
                             "(so laut, dass Gehörschutz vorgeschrieben ist)?",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Ihr Schutz am Arbeitsplatz",
            "questions": [
                {
                    "id": "handschuhe",
                    "type": "choice",
                    "label": "Tragen Sie beim Umgang mit den Stoffen die vorgeschriebenen "
                             "Schutzhandschuhe und die übrige Schutzausrüstung?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_umgang", "label": "Ich habe (noch) keinen direkten Umgang"},
                    ],
                },
                {
                    "id": "hygiene_essen",
                    "type": "yes_no",
                    "label": "Essen, trinken oder rauchen Sie in Arbeitsbereichen, in denen mit "
                             "Quecksilberverbindungen gearbeitet wird?",
                    "hint": "Über den Mund aufgenommene Alkylquecksilberverbindungen werden fast "
                            "vollständig vom Körper aufgenommen.",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Ernährung ──────────────────────────────────────────────────
        {
            "id": "ernaehrung",
            "title": "Ernährung",
            "subtitle": "Wichtig für die Bewertung der Blutuntersuchung",
            "questions": [
                {
                    "id": "fischkonsum",
                    "type": "choice",
                    "label": "Wie oft essen Sie Fisch oder Meeresfrüchte?",
                    "hint": "Fisch und Meeresfrüchte enthalten Methylquecksilber. Ein hoher Konsum "
                            "kann das Ergebnis der Quecksilber-Blutuntersuchung (Biomonitoring) "
                            "beeinflussen.",
                    "required": True,
                    "options": [
                        {"value": "selten", "label": "Selten (weniger als 1-mal pro Woche)"},
                        {"value": "regelmaessig", "label": "Etwa 1- bis 2-mal pro Woche"},
                        {"value": "haeufig", "label": "Mehr als 2-mal pro Woche"},
                    ],
                },
            ],
        },
        # ── 5 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, die auf eine Quecksilberbelastung hinweisen können",
            "questions": [
                {
                    "id": "tremor",
                    "type": "yes_no",
                    "label": "Zittern Ihre Hände oder Finger, oder haben Sie unwillkürliche "
                             "Schüttelbewegungen von Armen, Beinen oder Kopf?",
                    "required": True,
                },
                {
                    "id": "sprache",
                    "type": "yes_no",
                    "label": "Haben Sie neu aufgetretene Sprechstörungen (z. B. Stottern oder "
                             "verwaschene, undeutliche Sprache)?",
                    "required": True,
                },
                {
                    "id": "stimmung",
                    "type": "yes_no",
                    "label": "Sind Sie in letzter Zeit ungewöhnlich reizbar, ängstlich-befangen "
                             "oder stark stimmungslabil?",
                    "required": True,
                },
                {
                    "id": "schlaf",
                    "type": "yes_no",
                    "label": "Haben Sie Schlafstörungen?",
                    "required": True,
                },
                {
                    "id": "missempfindungen",
                    "type": "yes_no",
                    "label": "Haben Sie Kribbeln, Taubheitsgefühle oder Schwäche in Armen oder "
                             "Beinen (Missempfindungen)?",
                    "required": True,
                },
                {
                    "id": "mund",
                    "type": "yes_no",
                    "label": "Haben Sie eine Entzündung der Mundschleimhaut oder des Zahnfleischs, "
                             "wunde Stellen im Mund oder gelockerte Zähne?",
                    "required": True,
                },
                {
                    "id": "hautekzem",
                    "type": "yes_no",
                    "label": "Haben Sie juckende Hautausschläge oder Ekzeme?",
                    "required": True,
                },
            ],
        },
        # ── 6 ─ Vorerkrankungen und Medikamente ────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Medikamente",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "hg_vergiftung",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen schon einmal eine schwere Quecksilbervergiftung "
                             "festgestellt?",
                    "required": True,
                },
                {
                    "id": "nierenerkrankung",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Nierenerkrankung bekannt (z. B. eingeschränkte "
                             "Nierenfunktion, Eiweiß im Urin)?",
                    "required": True,
                    "followup": {"id": "nierenerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "neuro_erkrankung",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung des Nervensystems bekannt "
                             "(z. B. Polyneuropathie, Parkinson, Epilepsie, Multiple Sklerose)?",
                    "required": True,
                    "followup": {"id": "neuro_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "psychovegetativ",
                    "type": "yes_no",
                    "label": "Sind bei Ihnen ausgeprägte psycho-vegetative Störungen bekannt "
                             "(z. B. starke innere Unruhe, Herzrasen oder Schweißausbrüche ohne "
                             "körperliche Ursache)?",
                    "required": True,
                },
                {
                    "id": "abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Drogen oder Medikamenten?",
                    "required": True,
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein – auch Mittel der "
                             "alternativen Medizin oder pflanzliche Heilmittel?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "textarea",
                                 "label": "Welche Mittel?", "when": "yes"},
                },
                {
                    "id": "thiomersal_allergie",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Allergie gegen thiomersalhaltige Arzneimittel "
                             "bekannt (z. B. bestimmte Impfstoffe oder Augentropfen)?",
                    "required": True,
                },
                {
                    "id": "amalgam",
                    "type": "yes_no",
                    "label": "Haben Sie Zahnfüllungen aus Amalgam?",
                    "hint": "Amalgamfüllungen enthalten Quecksilber und können das Ergebnis der "
                            "Blutuntersuchung beeinflussen.",
                    "required": True,
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
    # ── Akute Gefährdung durch Hautkontakt (Abschnitte 6.2, 6.3.2, 8.1) ───
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Hautkontakt/Aufnahme",
     "quelle": "Abschnitte 6.2, 6.3.2 und 8.1",
     "befund": "Direkter Hautkontakt mit Alkylquecksilberverbindungen angegeben.",
     "konsequenz": "Hergang und Stoff (insbesondere Dimethylquecksilber: bereits wenige Tropfen "
                   "perkutan potenziell tödlich) vor weiterer Tätigkeit ärztlich klären. "
                   "Biomonitoring Quecksilber im Vollblut veranlassen, neurologischen Status "
                   "erheben; bei Verdacht auf relevante Aufnahme unverzügliche toxikologische "
                   "Abklärung. Mitteilung an das Unternehmen und Überprüfung der Schutzmaßnahmen "
                   "nach § 6 (4) ArbMedVV."},
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"hg_vergiftung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Schwere Quecksilbervergiftung in der Anamnese angegeben.",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Tätigkeit klären, ob eine Ausübung ohne "
                   "gesundheitliche Gefährdung möglich ist (Abschnitt 7.4). Vorbefunde einholen, "
                   "Biomonitoring und neurologische Untersuchung; Maßnahmen nach 7.4.2, verkürzte "
                   "Fristen nach 7.4.3, bei fehlender Erfolgsaussicht Tätigkeitswechsel nach "
                   "7.4.4 erwägen."},
    {"wenn": {"nierenerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Nierenerkrankung angegeben (Nierenleiden/tubuläre Schäden sind beurteilungsrelevant).",
     "konsequenz": "Ergänzend α1-Mikroglobulin oder N-Acetyl-ß-D-Glucosaminidase im Urin sowie "
                   "Kreatinin im Serum bestimmen; Vorbefunde einholen. Beurteilung nach 7.4: "
                   "Maßnahmen nach 7.4.2 (z. B. Expositionsminderung) bzw. verkürzte Vorsorgefristen "
                   "nach 7.4.3 prüfen."},
    {"wenn": {"neuro_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Neurologische Erkrankung angegeben.",
     "konsequenz": "Fachneurologische Befunde einholen; da Alkylquecksilberverbindungen primär das "
                   "Zentralnervensystem schädigen, prüfen, ob die Tätigkeit ohne gesundheitliche "
                   "Gefährdung möglich ist. Maßnahmen nach 7.4.2, verkürzte Fristen nach 7.4.3, "
                   "bei fehlender Erfolgsaussicht Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"psychovegetativ": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Ausgeprägte psycho-vegetative Störungen angegeben.",
     "konsequenz": "Ausmaß der Störung ärztlich klären (beurteilungsrelevante Erkrankung nach 7.4); "
                   "psychonervalen Fragebogen (z. B. Q18) einsetzen. Maßnahmen nach 7.4.2 bzw. "
                   "verkürzte Fristen nach 7.4.3 prüfen."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Alkohol-, Drogen- oder Medikamentenabhängigkeit angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Einzelfallprüfung, ob die Tätigkeit "
                   "ohne gesundheitliche Gefährdung möglich ist; Maßnahmen nach 7.4.2, verkürzte "
                   "Fristen nach 7.4.3, ggf. Tätigkeitswechsel nach 7.4.4 erwägen; Beratung und "
                   "Behandlungsangebote aufzeigen."},
    # ── Neurologische Symptome (Abschnitte 6.3.3 und 7.2.2) ───────────────
    {"wenn": {"tremor": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Zittern der Hände/Finger bzw. Schüttelbewegungen angegeben (möglicher Tremor "
               "mercurialis).",
     "konsequenz": "Schriftprobe durchführen und mit Voraufzeichnungen vergleichen (Trend zur "
                   "Zitterschrift), psychonervalen Fragebogen Q18 einsetzen, Biomonitoring "
                   "Quecksilber im Vollblut; bei auffälligem Befund neurologische Facharztvorstellung "
                   "und Überprüfung der Exposition."},
    {"wenn": {"sprache": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Sprechstörungen angegeben (möglicher Psellismus mercurialis).",
     "konsequenz": "Neurologischen Befund erheben, Schriftprobe und psychonervalen Fragebogen Q18 "
                   "durchführen, Biomonitoring Quecksilber im Vollblut; bei Auffälligkeiten "
                   "neurologische Abklärung veranlassen."},
    {"wenn": {"stimmung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Reizbarkeit, ängstliche Befangenheit oder Stimmungslabilität angegeben "
               "(möglicher Erethismus mercurialis).",
     "konsequenz": "Psychonervalen Fragebogen Q18 einsetzen, Schlafverhalten vertieft erfragen, "
                   "Biomonitoring Quecksilber im Vollblut; Verlauf engmaschig kontrollieren, ggf. "
                   "verkürzte Vorsorgefrist nach 7.4.3."},
    {"wenn": {"missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitt 6.3.3",
     "befund": "Kribbeln, Taubheitsgefühle oder Schwäche in Armen/Beinen angegeben "
               "(mögliche periphere Polyneuropathie).",
     "konsequenz": "Neurologische Abklärung (Polyneuropathie) veranlassen, andere Ursachen "
                   "ausschließen; Biomonitoring Quecksilber im Vollblut und Beurteilung nach 7.4."},
    # ── Mund/Zähne und Haut (Abschnitte 6.3.2, 6.3.3, 7.2.1) ──────────────
    {"wenn": {"mund": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Mund/Zähne",
     "quelle": "Abschnitte 6.3.2 und 7.2.1",
     "befund": "Entzündung der Mundschleimhaut/des Zahnfleischs oder Zahnlockerung angegeben.",
     "konsequenz": "Inspektion der Zähne und des Zahnfleisches sowie Zahnstatus (einschließlich "
                   "Amalgamfüllungen) durchführen; Stomatitis/Gingivitis als mögliches Frühzeichen "
                   "einer Quecksilberaufnahme werten, Biomonitoring veranlassen, ggf. zahnärztliche "
                   "Vorstellung."},
    {"wenn": {"hautekzem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 6.3.3",
     "befund": "Juckende Hautausschläge oder Ekzeme angegeben.",
     "konsequenz": "Abklärung eines allergischen Kontaktekzems (dermatologische Vorstellung, ggf. "
                   "Epikutantestung); Hautkontakt zum Stoff überprüfen und Schutzhandschuh-Auswahl "
                   "kontrollieren."},
    {"wenn": {"thiomersal_allergie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allergie",
     "quelle": "Abschnitte 7.1 (Medikamentenanamnese) und 6.3.3",
     "befund": "Allergie gegen thiomersalhaltige Arzneimittel angegeben.",
     "konsequenz": "Bei Tätigkeiten mit Thiomersal allergologische Abklärung veranlassen und "
                   "prüfen, ob die Exposition gemindert werden kann (Maßnahmen nach 7.4.2, z. B. "
                   "Substitution oder Einsatz an Arbeitsplätzen mit geringerer Exposition)."},
    # ── Schutzverhalten und Hygiene (Abschnitte 7.1 und 8.1) ──────────────
    {"wenn": {"handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 7.1, 8.1 und 8.2",
     "befund": "Schutzhandschuhe/Schutzausrüstung werden selten oder nie getragen.",
     "konsequenz": "Intensive Beratung: Hautkontakt ist unbedingt zu vermeiden; bei "
                   "Dimethylquecksilber spezielle Anforderungen an Handschuhe beachten. Ursachen "
                   "der Nichtbenutzung klären; ergeben sich Anhaltspunkte, dass die "
                   "Schutzmaßnahmen nicht ausreichen, Mitteilung an das Unternehmen und Vorschlag "
                   "von Maßnahmen nach § 6 (4) ArbMedVV."},
    {"wenn": {"hygiene_essen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 6.2 und 8.1",
     "befund": "Essen, Trinken oder Rauchen in Bereichen mit Exposition angegeben.",
     "konsequenz": "Beratung zur Hygiene am Arbeitsplatz: keine Nahrungs- und Genussmittel in "
                   "Expositionsbereichen (orale Resorption von Methylquecksilber 90–95 %); auf "
                   "Händereinigung und Wechsel der Arbeitskleidung hinweisen."},
    # ── Biomonitoring-Einflussgrößen (Abschnitte 6.4 und 7.2.2) ───────────
    {"wenn": {"fischkonsum": ["haeufig"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 7.2.2 (Fußnote) und 6.1",
     "befund": "Hoher Konsum von Fisch/Meeresfrüchten angegeben.",
     "konsequenz": "Ernährungsbedingte Methylquecksilber-Hintergrundbelastung bei der Bewertung des "
                   "Biomonitorings (Gesamtquecksilber im Vollblut, HBM-I 5 µg/l, HBM-II 15 µg/l) "
                   "berücksichtigen; Bestimmung eines Leerwerts vor Expositionsbeginn ist ratsam."},
    {"wenn": {"amalgam": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitte 6.4 und 7.2.1",
     "befund": "Amalgamfüllungen vorhanden.",
     "konsequenz": "Zahnstatus dokumentieren; Beitrag von anorganischem Quecksilber aus "
                   "Amalgamfüllungen zum Gesamtquecksilber im Vollblut bei der Bewertung des "
                   "Biomonitorings berücksichtigen."},
    # ── Vorexposition und Zwischenfälle (Abschnitte 6.4 und 7.1) ──────────
    {"wenn": {"frueher_exposition": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorexposition",
     "quelle": "Abschnitte 6.4 und 7.1",
     "befund": "Frühere Exposition gegenüber Quecksilber(-verbindungen) angegeben.",
     "konsequenz": "Vorexposition dokumentieren und frühere Biomonitoring-Befunde einholen; wegen "
                   "Kumulation und langer Halbwertszeit (Methylquecksilber im Blut 60–70 Tage) "
                   "Verlaufs-Biomonitoring im Vollblut durchführen – auch nach Expositionsende "
                   "empfohlen."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese)",
     "befund": "Zwischenfall/Unfall bzw. ungewöhnlicher Betriebszustand mit Stofffreisetzung "
               "angegeben.",
     "konsequenz": "Hergang dokumentieren, Biomonitoring aus besonderem Anlass veranlassen; "
                   "Erkenntnisse für die Gefährdungsbeurteilung nutzen und dem Unternehmen ggf. "
                   "Schutzmaßnahmen nach § 6 (4) ArbMedVV vorschlagen."},
    # ── Kombinationswirkung mit Lärm (Abschnitt 6.1) ──────────────────────
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 6.1",
     "befund": "Tätigkeit mit Exposition wird auch in Lärmbereichen ausgeübt.",
     "konsequenz": "Wegen der ototoxischen Eigenschaft von Quecksilberverbindungen mögliche "
                   "Kombinationswirkungen mit Lärm bei der Gehöruntersuchung nach der DGUV "
                   "Empfehlung »Lärm« berücksichtigen."},
]
