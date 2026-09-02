# -*- coding: utf-8 -*-
"""Kohlenstoffdisulfid (Schwefelkohlenstoff) – DGUV Empfehlung 2024.
Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen,
1. Auflage 2024, »Kohlenstoffdisulfid (Schwefelkohlenstoff)« (E CS2,
Fassung Januar 2022), S. 373–389."""

SLUG = "cs2-2024"

CATALOG = {
    "version": 2,
    "title": "Kohlenstoffdisulfid (Schwefelkohlenstoff) (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Kohlenstoffdisulfid (Schwefelkohlenstoff)« "
             "(E CS2, Fassung Januar 2022), S. 373–389",
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
                             "Kohlenstoffdisulfid (Schwefelkohlenstoff)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zu dieser Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert (30 mg/m³ bzw. 10 ppm) nicht eingehalten wird "
                            "oder Hautkontakt mit Kohlenstoffdisulfid nicht ausgeschlossen werden "
                            "kann. Angebotsvorsorge: wenn eine Belastung nicht ausgeschlossen "
                            "werden kann.",
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
            "title": "Tätigkeit & Belastung",
            "subtitle": "Ihre Arbeit mit Kohlenstoffdisulfid (Schwefelkohlenstoff, CS2)",
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
                    "label": "In welchen Bereichen kommen Sie mit Kohlenstoffdisulfid in Kontakt?",
                    "hint": "Mehrfachauswahl möglich. Kohlenstoffdisulfid ist eine leicht "
                            "verdunstende Flüssigkeit, die faulig nach Rettich riecht.",
                    "required": True,
                    "options": [
                        {"value": "viskose", "label": "Kunstseide-/Zellstoffindustrie (Viskosefasern, Cellophanfilm)"},
                        {"value": "gummi", "label": "Gummiindustrie (Extraktionsmittel für Fette, Öle, Harze)"},
                        {"value": "wartung", "label": "Reinigung, Wartung, Instandhaltung, Reparatur, Sanierung, "
                                                      "Abbruch oder Probenahme in Produktions-/Abfüllanlagen"},
                        {"value": "stoerung", "label": "Beheben von Betriebsstörungen in Herstellungs-, "
                                                       "Abfüll- oder Extraktionsanlagen"},
                        {"value": "kontaminiert", "label": "Arbeiten in verunreinigten (kontaminierten) Bereichen"},
                        {"value": "andere", "label": "Anderer Bereich"},
                        {"value": "keine", "label": "Keiner davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit Kohlenstoffdisulfid?",
                    "required": True,
                    "options": [
                        {"value": "beginnt", "label": "Noch gar nicht, die Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis10", "label": "5 bis 10 Jahre"},
                        {"value": "ueber10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kann Ihre Haut bei der Arbeit mit flüssigem Kohlenstoffdisulfid in "
                             "Berührung kommen (z. B. Spritzer, benetzte Kleidung, Arbeiten ohne "
                             "Handschuhe)?",
                    "hint": "Kohlenstoffdisulfid wird auch über die Haut in den Körper aufgenommen.",
                    "required": True,
                },
                {
                    "id": "stoerfall",
                    "type": "yes_no",
                    "label": "Gab es an Ihrem Arbeitsplatz Störfälle, Unfälle oder Situationen mit "
                             "kurzzeitig sehr hoher Dampfbelastung (z. B. Leckage, offene Anlage)?",
                    "required": True,
                    "followup": {"id": "stoerfall_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "akutbeschwerden",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich während oder direkt nach der Arbeit manchmal benommen, "
                             "schwindelig oder wie berauscht?",
                    "hint": "Solche Beschwerden können auf eine zu hohe Belastung mit "
                            "Kohlenstoffdisulfid-Dämpfen hinweisen.",
                    "required": True,
                },
                {
                    "id": "laermbereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Kohlenstoffdisulfid in Lärmbereichen "
                             "(Bereiche, in denen Gehörschutz vorgeschrieben ist)?",
                    "required": True,
                },
                {
                    "id": "frueher_cs2",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten bereits Kontakt mit "
                             "Kohlenstoffdisulfid (Schwefelkohlenstoff)?",
                    "required": True,
                    "followup": {"id": "frueher_cs2_desc", "type": "text",
                                 "label": "Wo, und wie lange?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Persönliche Schutzausrüstung und Hygiene",
            "questions": [
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Tragen Sie bei der Arbeit die vorgesehene persönliche Schutzausrüstung "
                             "(z. B. Schutzhandschuhe, Schutzkleidung, ggf. Atemschutz)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "Für meine Tätigkeit ist keine vorgesehen"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme mit der Schutzausrüstung (z. B. undichte oder "
                             "beschädigte Handschuhe, Hautreizungen, schlechter Sitz)?",
                    "required": True,
                    "show_if": {"id": "psa_nutzung", "not_in": ["nicht_noetig"]},
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
                {
                    "id": "hygiene",
                    "type": "yes_no",
                    "label": "Können Sie am Arbeitsplatz die Hygieneregeln einhalten (Arbeitskleidung "
                             "wechseln, Hände waschen vor Pausen, getrennte Aufbewahrung von "
                             "Arbeits- und Straßenkleidung)?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, die bei Belastung mit Kohlenstoffdisulfid auftreten können",
            "questions": [
                {
                    "id": "missempfindungen",
                    "type": "yes_no",
                    "label": "Haben Sie Missempfindungen in Händen oder Füßen, z. B. Kribbeln, "
                             "Taubheitsgefühl, Brennen oder ein pelziges Gefühl?",
                    "hint": "Solche Beschwerden können auf eine Nervenschädigung "
                            "(Polyneuropathie) hinweisen.",
                    "required": True,
                    "followup": {"id": "missempfindungen_desc", "type": "text",
                                 "label": "Wo genau, und seit wann?", "when": "yes"},
                },
                {
                    "id": "tremor",
                    "type": "yes_no",
                    "label": "Zittern Ihre Hände oder Arme (Tremor), oder sind Ihre Bewegungen "
                             "langsamer oder steifer geworden?",
                    "required": True,
                },
                {
                    "id": "psych_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine oder mehrere der folgenden Veränderungen "
                             "bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "schlaf", "label": "Schlafstörungen"},
                        {"value": "gedaechtnis", "label": "Gedächtnisschwäche (Vergesslichkeit)"},
                        {"value": "konzentration", "label": "Konzentrationsstörungen oder geistige Abstumpfung"},
                        {"value": "ermuedbarkeit", "label": "Schnelle Ermüdbarkeit, Leistungsknick"},
                        {"value": "reizbarkeit", "label": "Reizbarkeit oder häufiger Streit (Streitsucht)"},
                        {"value": "depressiv", "label": "Niedergeschlagenheit, depressive Verstimmung"},
                        {"value": "euphorie", "label": "Grundlose Hochstimmung (Euphorie)"},
                        {"value": "verwirrtheit", "label": "Verwirrtheitszustände"},
                        {"value": "keine", "label": "Nichts davon"},
                    ],
                },
                {
                    "id": "farbsehen",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Farbsehen verschlechtert (Farben lassen sich schlechter "
                             "unterscheiden als früher)?",
                    "required": True,
                },
                {
                    "id": "appetit_gewicht",
                    "type": "yes_no",
                    "label": "Haben Sie Appetitlosigkeit (Inappetenz) oder haben Sie ungewollt an "
                             "Gewicht abgenommen?",
                    "required": True,
                    "followup": {"id": "appetit_gewicht_desc", "type": "text",
                                 "label": "Wie viel Gewichtsverlust, in welchem Zeitraum?",
                                 "when": "yes"},
                },
                {
                    "id": "magen_darm",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Magen-Darm-Beschwerden (z. B. Übelkeit, "
                             "Magenschmerzen, Verdauungsstörungen)?",
                    "required": True,
                },
                {
                    "id": "alkohol_unvertraeglich",
                    "type": "yes_no",
                    "label": "Vertragen Sie Alkohol deutlich schlechter als früher "
                             "(Überempfindlichkeit gegenüber Alkohol)?",
                    "required": True,
                },
                {
                    "id": "herzbeschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei körperlicher Belastung Druck oder Schmerzen in der "
                             "Brust, Herzstolpern oder ungewöhnliche Luftnot?",
                    "required": True,
                },
                {
                    "id": "beine_durchblutung",
                    "type": "yes_no",
                    "label": "Haben Sie beim Gehen Schmerzen in den Waden oder Beinen, die Sie zum "
                             "Stehenbleiben zwingen, oder auffallend kalte, blasse Füße?",
                    "hint": "Das kann auf eine Durchblutungsstörung der Beine hinweisen "
                            "(»Schaufensterkrankheit«).",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "gesundheit",
            "title": "Vorerkrankungen & Gesundheit",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "haut",
                    "type": "yes_no",
                    "label": "Haben Sie großflächige Hautveränderungen, z. B. Schuppenflechte "
                             "(Psoriasis) oder ausgedehnte Ekzeme?",
                    "hint": "Über vorgeschädigte Haut kann Kohlenstoffdisulfid leichter in den "
                            "Körper gelangen.",
                    "required": True,
                },
                {
                    "id": "vorerkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Erkrankungen festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "nerven", "label": "Erkrankung des Nervensystems (z. B. Polyneuropathie, "
                                                     "Nervenschädigung)"},
                        {"value": "psyche", "label": "Psychische Erkrankung (z. B. Depression, Psychose)"},
                        {"value": "herz", "label": "Herzerkrankung (z. B. Herzschwäche, koronare Herzkrankheit)"},
                        {"value": "gefaesse", "label": "Gefäßverkalkung (Arteriosklerose, Durchblutungsstörungen)"},
                        {"value": "vegetativ", "label": "Ausgeprägte vegetative Beschwerden (z. B. starke "
                                                        "Kreislaufschwankungen, Herzrasen, Schweißausbrüche "
                                                        "ohne körperliche Ursache)"},
                        {"value": "hypertonie", "label": "Bluthochdruck (arterielle Hypertonie)"},
                        {"value": "anaemie", "label": "Blutarmut (Anämie)"},
                        {"value": "magen_darm_geschwuer", "label": "Magen- oder Darmgeschwüre"},
                        {"value": "niere", "label": "Nierenerkrankung"},
                        {"value": "leber", "label": "Lebererkrankung"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "vorerkrankung_details",
                    "type": "textarea",
                    "label": "Falls Sie oben etwas angekreuzt haben: Welche Erkrankung, seit wann, "
                             "und wie wird sie behandelt?",
                    "required": False,
                },
                {
                    "id": "sucht",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol oder "
                             "Drogen (Rauschmitteln)?",
                    "required": True,
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Sind Sie schwanger, oder besteht aktuell ein Kinderwunsch?",
                    "hint": "Kohlenstoffdisulfid kann vermutlich die Fruchtbarkeit beeinträchtigen "
                            "oder das Kind im Mutterleib schädigen. Die Angabe ist freiwillig.",
                    "required": True,
                    "options": [
                        {"value": "schwanger", "label": "Ja, ich bin schwanger (oder vermute es)"},
                        {"value": "kinderwunsch", "label": "Nein, aber es besteht ein Kinderwunsch"},
                        {"value": "nein", "label": "Nein, beides nicht"},
                        {"value": "keine_angabe", "label": "Keine Angabe"},
                    ],
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
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"vorerkrankungen": ["nerven", "psyche"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem/Psyche",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Erkrankung des Nervensystems (z. B. Polyneuropathie) oder psychische "
               "Erkrankung angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: prüfen, ob die Tätigkeit ohne "
                   "gesundheitliche Gefährdung möglich ist. Fachneurologische und/oder "
                   "psychiatrische Untersuchung (evtl. EEG, Elektroneuro-/Elektromyographie) "
                   "veranlassen. Maßnahmen nach 7.4.2 prüfen (Substitution, technische/"
                   "organisatorische Schutzmaßnahmen, Expositionsbegrenzung); bei zu erwartender "
                   "Änderung des Schweregrads verkürzte Fristen nach 7.4.3; ohne Erfolgsaussicht "
                   "Tätigkeitswechsel nach 7.4.4 erwägen (Mitteilung an den Arbeitgeber nur mit "
                   "Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"vorerkrankungen": ["herz", "gefaesse", "vegetativ", "hypertonie"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 7.4 und 6.3.1",
     "befund": "Hämodynamisch relevante Herzerkrankung, Arteriosklerose, ausgeprägte vegetative "
               "Labilität oder arterielle Hypertonie angegeben.",
     "konsequenz": "Kritische Zielorgane von CS2 sind Herz-Kreislaufsystem und Nervensystem: "
                   "kardiovaskulären Status abklären (Ergometrie nach Anhang 2, Blutdruck, "
                   "ggf. kardiologische Vorbefunde). Beurteilung nach 7.4; Maßnahmen nach 7.4.2 "
                   "bzw. verkürzte Fristen nach 7.4.3 prüfen."},
    {"wenn": {"vorerkrankungen": ["anaemie", "magen_darm_geschwuer", "niere", "leber"]},
     "schwere": "pruefen",
     "bereich": "Innere Erkrankungen",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Anämie, Magen-Darm-Geschwüre, Nieren- oder Lebererkrankung angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Laborstatus erheben bzw. "
                   "aktualisieren (kleines Blutbild, γ-GT, ALAT, ASAT, Cholesterin/Triglyceride, "
                   "Urinstatus mit ggf. Sediment), Vorbefunde einholen. Maßnahmen nach 7.4.2 "
                   "bzw. verkürzte Fristen nach 7.4.3 prüfen."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Abhängigkeit",
     "quelle": "Abschnitt 7.4",
     "befund": "Alkohol- oder Rauschmittelabhängigkeit angegeben.",
     "konsequenz": "Nach 7.4 beurteilungsrelevant: Suchtanamnese ärztlich vertiefen, "
                   "Behandlung/Beratung anbieten. Prüfen, ob die Tätigkeit ohne gesundheitliche "
                   "Gefährdung möglich ist; Maßnahmen nach 7.4.2, ggf. Tätigkeitswechsel nach "
                   "7.4.4 erwägen."},
    # ── Tätigkeitsspezifische Symptome (Abschnitte 7.1 und 6.3.3) ─────────
    {"wenn": {"missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Periphere Nerven",
     "quelle": "Abschnitte 7.1, 7.2.2 und 6.3.3",
     "befund": "Distale Missempfindungen (Kribbeln, Taubheit, Brennen) in Händen/Füßen angegeben.",
     "konsequenz": "Verdacht auf beginnende Polyneuropathie: Vibrationsempfinden mit "
                   "128-Hz-Stimmgabel prüfen, Reflexstatus erheben; bei nicht abklärbarem Befund "
                   "fachneurologische Untersuchung mit Elektroneuro-/Elektromyographie. "
                   "Biomonitoring (TTCA im Urin) durchführen und Exposition mit der "
                   "Gefährdungsbeurteilung abgleichen; verkürzte Vorsorgefrist nach 7.4.3 erwägen."},
    {"wenn": {"tremor": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zentrales Nervensystem",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Tremor der Extremitäten bzw. Parkinson-artige Beschwerden angegeben.",
     "konsequenz": "Fachneurologische Untersuchung (evtl. EEG, Elektroneuro-/Elektromyographie) "
                   "veranlassen, wenn die allgemeine ärztliche Untersuchung den Befund nicht "
                   "klärt; Expositionshöhe prüfen, Biomonitoring einbeziehen."},
    {"wenn": {"psych_symptome": ["schlaf", "gedaechtnis", "konzentration", "ermuedbarkeit",
                                 "reizbarkeit", "depressiv", "euphorie", "verwirrtheit"]},
     "schwere": "pruefen",
     "bereich": "Neuropsychiatrische Symptome",
     "quelle": "Abschnitte 7.1, 7.2.2 und 6.3.3",
     "befund": "Tätigkeitsspezifische neuropsychiatrische Symptome angegeben (z. B. "
               "Schlafstörungen, Gedächtnisschwäche, Reizbarkeit, depressive Verstimmung, "
               "Euphorie, Verwirrtheit).",
     "konsequenz": "Symptome ärztlich vertiefen (Beginn, Verlauf, Bezug zur Exposition). In "
                   "Fällen, die durch die allgemeinen Untersuchungen nicht abgeklärt werden "
                   "können, psychiatrische und/oder fachneurologische Untersuchung mit evtl. EEG "
                   "veranlassen. Biomonitoring durchführen; bei Anhaltspunkten für unzureichende "
                   "Schutzmaßnahmen Mitteilung an das Unternehmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"farbsehen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Verschlechterung des Farbsehens angegeben.",
     "konsequenz": "Erworbene Farbsinnstörung mit geeignetem Testverfahren prüfen; "
                   "Augenhintergrundspiegelung (Bestandteil der Nachuntersuchung) durchführen, "
                   "ggf. augenärztliche Abklärung veranlassen."},
    {"wenn": {"alkohol_unvertraeglich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Tätigkeitsspezifisches Symptom",
     "quelle": "Abschnitt 7.1 (Alle weiteren Vorsorgen)",
     "befund": "Überempfindlichkeit gegenüber Alkohol angegeben.",
     "konsequenz": "Typisches Symptom chronischer CS2-Einwirkung: Anamnese vertiefen, "
                   "Biomonitoring (TTCA im Urin, Probenahme bei Expositions-/Schichtende) "
                   "durchführen und mit dem BGW (4 mg/g Kreatinin) vergleichen; Exposition mit "
                   "der Gefährdungsbeurteilung abgleichen."},
    {"wenn": {"appetit_gewicht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allgemeinsymptome",
     "quelle": "Abschnitte 7.1 und 6.3.3",
     "befund": "Appetitlosigkeit (Inappetenz) oder ungewollte Gewichtsabnahme angegeben.",
     "konsequenz": "Als mögliches Zeichen chronischer CS2-Einwirkung abklären (Ausmaß, Verlauf, "
                   "andere Ursachen); Biomonitoring durchführen, ggf. verkürzte Vorsorgefrist "
                   "nach 7.4.3 erwägen."},
    {"wenn": {"herzbeschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 7.2.2 und 6.3.1",
     "befund": "Belastungsabhängige Brustschmerzen, Herzstolpern oder Luftnot angegeben.",
     "konsequenz": "Wegen der erhöhten Rate koronarer Herzerkrankungen bei chronischer "
                   "CS2-Exposition kardiologisch abklären: Ergometrie (Anhang 2, Leitfaden "
                   "»Ergometrie«), ggf. fachkardiologische Vorstellung vor Fortsetzung "
                   "hoher Exposition."},
    {"wenn": {"beine_durchblutung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gefäße",
     "quelle": "Abschnitte 7.1 und 6.3.3",
     "befund": "Hinweise auf Durchblutungsstörung der Beine (Claudicatio, kalte/blasse Füße).",
     "konsequenz": "Palpation der Arteria dorsalis pedis und Arteria tibialis posterior, "
                   "Gefäßstatus erheben; bei Auffälligkeiten angiologische Abklärung "
                   "(CS2-bedingte Gefäßsklerose möglich). Beurteilung nach 7.4."},
    # ── Haut und Exposition ───────────────────────────────────────────────
    {"wenn": {"haut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Großflächige Hautveränderungen (z. B. Psoriasis vulgaris) angegeben.",
     "konsequenz": "Erhöhte Aufnahme über die vorgeschädigte Haut möglich: Hautbefund ärztlich "
                   "beurteilen, konsequenten Hautschutz und geeignete Schutzhandschuhe sicher- "
                   "stellen (Materialauswahl nach Sicherheitsdatenblatt, GESTIS, GISCHEM, WINGIS); "
                   "Biomonitoring zur Kontrolle der inneren Belastung; ggf. Maßnahmen nach 7.4.2."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Dermale Exposition",
     "quelle": "Abschnitte 2, 6.2, 6.4 und 8.1",
     "befund": "Möglicher Hautkontakt mit flüssigem Kohlenstoffdisulfid angegeben.",
     "konsequenz": "Dermale Exposition ist Kriterium für Pflichtvorsorge: Expositionssituation "
                   "mit der Gefährdungsbeurteilung abgleichen. Biomonitoring (TTCA im Urin) ist "
                   "angezeigt, da es auch die Hautaufnahme erfasst; Beratung zu geeigneten "
                   "Handschuhmaterialien und Schutzkleidung (Sicherheitsdatenblatt, GESTIS, "
                   "GISCHEM, WINGIS)."},
    {"wenn": {"stoerfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Expositionsspitzen",
     "quelle": "Abschnitte 7.1 und 8.2",
     "befund": "Störfall bzw. kurzzeitig stark erhöhte Dampfbelastung angegeben.",
     "konsequenz": "Kurzzeitige Überschreitung des Luftgrenzwerts in der Arbeitsanamnese "
                   "dokumentieren und ärztlich bewerten; Biomonitoring durchführen. Ergeben sich "
                   "Anhaltspunkte für unzureichende Schutzmaßnahmen, Mitteilung an das "
                   "Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"akutbeschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Wirkung",
     "quelle": "Abschnitte 6.3.2 und 8.2",
     "befund": "Benommenheit, Schwindel oder Rauschgefühl während/nach der Arbeit angegeben.",
     "konsequenz": "Pränarkotische Symptome sprechen für relevante aktuelle Überexposition: "
                   "zeitnah Biomonitoring, Expositionsermittlung anstoßen und dem Unternehmen "
                   "Überprüfung der Gefährdungsbeurteilung sowie zusätzliche Schutzmaßnahmen "
                   "vorschlagen (§ 6 (4) ArbMedVV); bis zur Klärung Expositionsminderung anraten."},
    # ── Schutzmaßnahmen und Beratung ──────────────────────────────────────
    {"wenn": {"psa_nutzung": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Wegen der hautresorptiven Eigenschaften von CS2 kommt der PSA besondere "
                   "Bedeutung zu: intensiv zu Tragepflicht und geeigneten Materialien beraten, "
                   "Ursachen der Nichtbenutzung klären. Reichen die Schutzmaßnahmen erkennbar "
                   "nicht aus, Mitteilung an das Unternehmen und Vorschlag von Maßnahmen "
                   "(§ 6 (4) ArbMedVV)."},
    {"wenn": {"psa_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitt 8.1",
     "befund": "Probleme mit der Schutzausrüstung angegeben.",
     "konsequenz": "Individuelle PSA-Beratung: geeignete Handschuhmaterialien und Schutzkleidung "
                   "nach Sicherheitsdatenblatt bzw. GESTIS/GISCHEM/WINGIS auswählen, Sitz und "
                   "Zustand prüfen, defekte Ausrüstung ersetzen lassen."},
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 6.1",
     "befund": "Tätigkeit mit CS2-Exposition in Lärmbereichen angegeben.",
     "konsequenz": "Kohlenstoffdisulfid ist ototoxisch: mögliche Kombinationswirkungen mit Lärm "
                   "bei der Gehörvorsorge nach der DGUV Empfehlung »Lärm« berücksichtigen; "
                   "Abstimmung beider Vorsorgen."},
    {"wenn": {"schwangerschaft": ["schwanger"]},
     "schwere": "pruefen",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6.3.3, 7.1 und 8.1",
     "befund": "Schwangerschaft angegeben bzw. vermutet.",
     "konsequenz": "CS2 kann vermutlich das Kind im Mutterleib schädigen: unverzüglich zur "
                   "Fortsetzung der Tätigkeit beraten, Regelungen des Mutterschutzgesetzes "
                   "beachten und auf eine mutterschutzrechtliche Gefährdungsbeurteilung durch "
                   "den Arbeitgeber hinwirken; Expositionsvermeidung anstreben."},
]
