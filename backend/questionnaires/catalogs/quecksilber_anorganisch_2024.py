# -*- coding: utf-8 -*-
"""Quecksilber und anorganische Quecksilberverbindungen – DGUV Empfehlung 2024.
Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen,
1. Auflage 2024, »Quecksilber und anorganische Quecksilberverbindungen«
(E AHG, Fassung Januar 2022), S. 501–522."""

SLUG = "quecksilber-anorganisch-2024"

CATALOG = {
    "version": 2,
    "title": "Quecksilber und anorganische Quecksilberverbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Quecksilber und anorganische Quecksilberverbindungen« "
             "(E AHG, Fassung Januar 2022), S. 501–522",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen Quecksilber "
                             "oder anorganischer Quecksilberverbindungen?",
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
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert (derzeit 0,02 mg/m³) nicht eingehalten wird oder "
                            "eine Gefährdung durch Hautkontakt nicht ausgeschlossen werden kann. "
                            "Angebotsvorsorge: wenn eine Belastung nicht ausgeschlossen werden kann.",
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
            "title": "Tätigkeit & Umgang mit Quecksilber",
            "subtitle": "Ihre Arbeit mit Quecksilber oder seinen anorganischen Verbindungen",
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
                    "label": "In welchen Bereichen haben Sie mit Quecksilber oder anorganischen "
                             "Quecksilberverbindungen zu tun?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "herstellung", "label": "Herstellen oder Aufbereiten von Quecksilber und "
                                                          "seinen Verbindungen (z. B. Filtrieren, Destillieren)"},
                        {"value": "messgeraete", "label": "Wartung/Reparatur quecksilberhaltiger Mess- und "
                                                          "Regelgeräte (Barometer, Thermometer)"},
                        {"value": "entsorgung", "label": "Entsorgung, Recycling oder Transport "
                                                         "quecksilberhaltiger Materialien und Altteile"},
                        {"value": "leuchtmittel", "label": "Sammlung oder Recycling quecksilberhaltiger "
                                                           "Leuchtmittel (Energiesparlampen, Leuchtstoffröhren)"},
                        {"value": "flachbildschirme", "label": "Demontage von Flachbildschirmen"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an kontaminierten Gebäuden "
                                                      "(z. B. ehemalige Spiegelfabriken, Laboratorien)"},
                        {"value": "restauration", "label": "Spezielle Restaurationsarbeiten "
                                                           "(z. B. Feuervergoldung, amalgamierte Spiegel)"},
                        {"value": "labor", "label": "Labor/Elektrolyse (z. B. Sperrflüssigkeit, "
                                                    "Chloralkalielektrolyse)"},
                        {"value": "sonstige", "label": "Sonstige Bereiche"},
                        {"value": "keine", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "lampenbruch",
                    "type": "choice",
                    "label": "Falls Sie mit quecksilberhaltigen Leuchtmitteln zu tun haben: Kommt es "
                             "dabei zu Lampenbruch (zerbrochene Energiesparlampen oder Röhren)?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, es kommt zu Lampenbruch"},
                        {"value": "nein", "label": "Nein, die Leuchtmittel bleiben intakt"},
                        {"value": "nicht_zutreffend", "label": "Ich habe mit Leuchtmitteln nichts zu tun"},
                    ],
                },
                {
                    "id": "zwischenfall",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle oder Unfälle, bei denen "
                             "Quecksilber freigesetzt oder verschüttet wurde?",
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
                    "id": "psa",
                    "type": "choice",
                    "label": "Tragen Sie bei der Arbeit die vorgeschriebene persönliche "
                             "Schutzausrüstung (z. B. Handschuhe, Atemschutz)?",
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
                    "id": "kleidung_wechsel",
                    "type": "yes_no",
                    "label": "Wechseln Sie nach der Arbeit die Arbeitskleidung und bewahren sie "
                             "getrennt von Ihrer privaten Kleidung auf?",
                    "hint": "In der Kleidung gebundenes Quecksilber kann die Aufnahme über die Haut "
                            "deutlich erhöhen.",
                    "required": True,
                },
                {
                    "id": "hygiene_essen",
                    "type": "yes_no",
                    "label": "Essen, trinken oder rauchen Sie in Arbeitsbereichen, in denen mit "
                             "Quecksilber gearbeitet wird?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
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
                    "id": "atemwege",
                    "type": "yes_no",
                    "label": "Haben Sie nach der Arbeit Husten, Atemnot oder ein Reizgefühl in den "
                             "Atemwegen?",
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
        # ── 5 ─ Vorerkrankungen und Medikamente ────────────────────────────
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
                    "id": "schilddruese",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Schilddrüsenüberfunktion bekannt?",
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
                    "id": "amalgam",
                    "type": "yes_no",
                    "label": "Haben Sie Zahnfüllungen aus Amalgam?",
                    "hint": "Amalgamfüllungen enthalten Quecksilber; das ist für den Zahnstatus und "
                            "die Bewertung der Urinuntersuchung wichtig.",
                    "required": True,
                },
            ],
        },
        # ── 6 ─ Lebensweise und besondere Umstände ─────────────────────────
        {
            "id": "besonderes",
            "title": "Lebensweise & besondere Umstände",
            "subtitle": "Angaben, die die Bewertung Ihrer Belastung beeinflussen",
            "questions": [
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Trinken Sie Alkohol?",
                    "hint": "Regelmäßiger Alkoholkonsum kann dazu führen, dass sich Quecksilber "
                            "stärker im Körpergewebe anreichert.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein / sehr selten"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "regelmaessig", "label": "Regelmäßig (täglich oder fast täglich)"},
                    ],
                },
                {
                    "id": "fischkonsum",
                    "type": "choice",
                    "label": "Wie oft essen Sie Fisch oder Meeresfrüchte?",
                    "hint": "Fisch und Meeresfrüchte enthalten Quecksilber; das kann das Ergebnis "
                            "des Biomonitorings beeinflussen.",
                    "required": True,
                    "options": [
                        {"value": "selten", "label": "Selten (weniger als 1-mal pro Woche)"},
                        {"value": "regelmaessig", "label": "Etwa 1- bis 2-mal pro Woche"},
                        {"value": "haeufig", "label": "Mehr als 2-mal pro Woche"},
                    ],
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Nur für Frauen: Sind Sie schwanger, oder stillen Sie zurzeit?",
                    "hint": "Metallisches Quecksilber kann das Kind im Mutterleib schädigen "
                            "(fruchtschädigend, Kategorie 1B). Für Schwangere und Stillende gelten "
                            "besondere Beschäftigungsbeschränkungen nach dem Mutterschutzgesetz.",
                    "required": True,
                    "options": [
                        {"value": "schwanger", "label": "Ja, ich bin schwanger"},
                        {"value": "stillzeit", "label": "Ja, ich stille"},
                        {"value": "unsicher", "label": "Ich bin mir nicht sicher"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "nicht_zutreffend", "label": "Trifft nicht auf mich zu"},
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
    # ── Mutterschutz (Abschnitte 6, 7.1 und 8.1) ──────────────────────────
    {"wenn": {"schwangerschaft": ["schwanger", "stillzeit", "unsicher"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6 (Reproduktionstoxizität Kat. 1B, H360D), 7.1 und 8.1",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben oder nicht sicher auszuschließen.",
     "konsequenz": "Metallisches Quecksilber ist fruchtschädigend (Kategorie 1B): "
                   "Beschäftigungsbeschränkungen nach dem Mutterschutzgesetz unverzüglich und vor "
                   "(weiterer) Tätigkeit mit Exposition klären; Mitteilung an das Unternehmen zur "
                   "Anpassung der Gefährdungsbeurteilung; Beratung zur Reproduktionstoxizität "
                   "durchführen."},
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"hg_vergiftung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Schwere Quecksilbervergiftung in der Anamnese angegeben.",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Tätigkeit klären, ob eine Ausübung ohne "
                   "gesundheitliche Gefährdung möglich ist (Abschnitt 7.4). Vorbefunde einholen, "
                   "Biomonitoring Quecksilber im Urin und neurologische Untersuchung; Maßnahmen "
                   "nach 7.4.2, verkürzte Fristen nach 7.4.3, bei fehlender Erfolgsaussicht "
                   "Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"nierenerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Nierenerkrankung angegeben (Nierenleiden/tubuläre Schäden sind beurteilungsrelevant; "
               "Niere ist Hauptspeicherorgan).",
     "konsequenz": "Ergänzend α1-Mikroglobulin oder N-Acetyl-ß-D-Glucosaminidase im Urin sowie "
                   "Kreatinin im Serum bestimmen; Vorbefunde einholen. Beurteilung nach 7.4: "
                   "Maßnahmen nach 7.4.2 (z. B. Expositionsminderung) bzw. verkürzte "
                   "Vorsorgefristen nach 7.4.3 prüfen."},
    {"wenn": {"neuro_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Neurologische Erkrankung angegeben.",
     "konsequenz": "Fachneurologische Befunde einholen; da Nerven- und Nierentoxizität die "
                   "empfindlichsten Endpunkte sind, prüfen, ob die Tätigkeit ohne gesundheitliche "
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
    {"wenn": {"schilddruese": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Schilddrüsenüberfunktion angegeben.",
     "konsequenz": "Klären, ob eine manifeste Schilddrüsenüberfunktion vorliegt "
                   "(beurteilungsrelevante Erkrankung nach 7.4); aktuelle Befunde bzw. "
                   "internistische Abklärung veranlassen. Maßnahmen nach 7.4.2 bzw. verkürzte "
                   "Fristen nach 7.4.3 prüfen."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Alkohol-, Drogen- oder Medikamentenabhängigkeit angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Einzelfallprüfung, ob die Tätigkeit "
                   "ohne gesundheitliche Gefährdung möglich ist; Maßnahmen nach 7.4.2, verkürzte "
                   "Fristen nach 7.4.3, ggf. Tätigkeitswechsel nach 7.4.4 erwägen; Beratung und "
                   "Behandlungsangebote aufzeigen."},
    {"wenn": {"alkohol": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Lebensweise",
     "quelle": "Abschnitt 6.3.1",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung: Ethanol hemmt die Oxidation von Quecksilber, chronischer "
                   "Alkoholkonsum führt zu verstärkter Kumulation im Gewebe; Alkoholkonsum bei der "
                   "Bewertung des Biomonitorings berücksichtigen und ggf. engmaschigere Kontrolle "
                   "erwägen."},
    # ── Neurologische Symptome (Abschnitte 6.3.3 und 7.2.2) ───────────────
    {"wenn": {"tremor": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Zittern der Hände/Finger bzw. Schüttelbewegungen angegeben (möglicher Tremor "
               "mercurialis).",
     "konsequenz": "Schriftprobe durchführen und mit Voraufzeichnungen vergleichen (Trend zur "
                   "Zitterschrift), psychonervalen Fragebogen Q18 einsetzen, Biomonitoring "
                   "Quecksilber im Urin; bei auffälligem Befund neurologische Facharztvorstellung "
                   "und Überprüfung der Exposition."},
    {"wenn": {"sprache": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Sprechstörungen angegeben (möglicher Psellismus mercurialis).",
     "konsequenz": "Neurologischen Befund erheben, Schriftprobe und psychonervalen Fragebogen Q18 "
                   "durchführen, Biomonitoring Quecksilber im Urin; bei Auffälligkeiten "
                   "neurologische Abklärung veranlassen."},
    {"wenn": {"stimmung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Reizbarkeit, ängstliche Befangenheit oder Stimmungslabilität angegeben "
               "(möglicher Erethismus mercurialis).",
     "konsequenz": "Psychonervalen Fragebogen Q18 einsetzen, Biomonitoring Quecksilber im Urin; "
                   "Verlauf engmaschig kontrollieren, ggf. verkürzte Vorsorgefrist nach 7.4.3."},
    {"wenn": {"missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitt 6.3.3",
     "befund": "Kribbeln, Taubheitsgefühle oder Schwäche in Armen/Beinen angegeben "
               "(mögliche periphere Polyneuropathie).",
     "konsequenz": "Neurologische Abklärung (Polyneuropathie) veranlassen, andere Ursachen "
                   "ausschließen; Biomonitoring Quecksilber im Urin und Beurteilung nach 7.4."},
    # ── Mund, Atemwege, Haut (Abschnitte 6.3.2, 6.3.3, 7.2.1) ─────────────
    {"wenn": {"mund": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Mund/Zähne",
     "quelle": "Abschnitte 6.3.2 und 7.2.1",
     "befund": "Entzündung der Mundschleimhaut/des Zahnfleischs oder Zahnlockerung angegeben.",
     "konsequenz": "Inspektion der Zähne und des Zahnfleisches sowie Zahnstatus (einschließlich "
                   "Amalgamfüllungen) durchführen; Stomatitis/Gingivitis als mögliches Frühzeichen "
                   "einer Quecksilberaufnahme werten, Biomonitoring veranlassen, ggf. zahnärztliche "
                   "Vorstellung."},
    {"wenn": {"atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitt 6.3.2",
     "befund": "Husten, Atemnot oder Reizgefühl der Atemwege nach der Arbeit angegeben.",
     "konsequenz": "Mögliche Reizung der Luftwege durch Quecksilberdämpfe (Tracheobronchitis, "
                   "Bronchopneumonie) abklären; aktuelle Exposition prüfen (AGW 0,02 mg/m³), "
                   "Biomonitoring im Urin veranlassen; ergeben sich Anhaltspunkte für unzureichende "
                   "Schutzmaßnahmen, Mitteilung an das Unternehmen nach § 6 (4) ArbMedVV."},
    {"wenn": {"hautekzem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6 und 6.3.3",
     "befund": "Juckende Hautausschläge oder Ekzeme angegeben.",
     "konsequenz": "Abklärung eines allergischen Kontaktekzems (Quecksilber und anorganische "
                   "Verbindungen sind hautsensibilisierend): dermatologische Vorstellung, ggf. "
                   "Epikutantestung; Hautkontakt und Schutzausrüstung überprüfen."},
    # ── Schutzverhalten und Hygiene (Abschnitte 6.2, 7.1, 8.1) ────────────
    {"wenn": {"psa": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 7.1, 8.1 und 8.2",
     "befund": "Persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA und zum Vermeiden von Inhalation "
                   "und Hautkontakt; Ursachen der Nichtbenutzung klären. Ergeben sich Anhaltspunkte, "
                   "dass die Schutzmaßnahmen nicht ausreichen, Mitteilung an das Unternehmen und "
                   "Vorschlag von Maßnahmen nach § 6 (4) ArbMedVV."},
    {"wenn": {"kleidung_wechsel": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 6.2 und 8.1",
     "befund": "Arbeitskleidung wird nicht gewechselt bzw. nicht getrennt aufbewahrt.",
     "konsequenz": "Beratung: In der Kleidung adsorbiertes Quecksilber erhöht die Aufnahme über die "
                   "Haut (Konzentration unter der Kleidung bis zu 10-mal höher); auf Wechsel der "
                   "Arbeitskleidung und Hygiene am Arbeitsplatz hinweisen."},
    # ── Vorexposition und Zwischenfälle (Abschnitte 6.4 und 7.1) ──────────
    {"wenn": {"frueher_exposition": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorexposition",
     "quelle": "Abschnitte 6.4 und 7.1",
     "befund": "Frühere Exposition gegenüber Quecksilber(-verbindungen) angegeben.",
     "konsequenz": "Vorexposition dokumentieren und frühere Biomonitoring-Befunde einholen; wegen "
                   "Speicherung in verschiedenen Kompartimenten und langer Eliminationszeiträume "
                   "Verlaufs-Biomonitoring Quecksilber im Urin (BGW/BAT 25 µg/g Kreatinin bzw. "
                   "30 µg/l Urin) durchführen – auch nach Expositionsende empfohlen."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese)",
     "befund": "Zwischenfall/Unfall mit Freisetzung von Quecksilber angegeben.",
     "konsequenz": "Hergang dokumentieren, Biomonitoring aus besonderem Anlass veranlassen; "
                   "Erkenntnisse für die Gefährdungsbeurteilung nutzen und dem Unternehmen ggf. "
                   "Schutzmaßnahmen nach § 6 (4) ArbMedVV vorschlagen."},
    # ── Kombinationswirkung mit Lärm (Abschnitt 6.1.1) ────────────────────
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 6.1.1",
     "befund": "Tätigkeit mit Exposition wird auch in Lärmbereichen ausgeübt.",
     "konsequenz": "Wegen der ototoxischen Eigenschaft von Quecksilber und anorganischen "
                   "Quecksilberverbindungen mögliche Kombinationswirkungen mit Lärm bei der "
                   "Gehöruntersuchung nach der DGUV Empfehlung »Lärm« berücksichtigen."},
]
