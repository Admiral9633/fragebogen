# -*- coding: utf-8 -*-
"""G 6 Kohlenstoffdisulfid (Schwefelkohlenstoff) – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016,
G 6 »Kohlenstoffdisulfid (Schwefelkohlenstoff)« (Fassung Oktober 2014), S. 165–175."""

SLUG = "g6-cs2-2016"

CATALOG = {
    "version": 2,
    "title": "G 6 Kohlenstoffdisulfid (Schwefelkohlenstoff) (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 6 »Kohlenstoffdisulfid (Schwefelkohlenstoff)« "
             "(Fassung Oktober 2014), S. 165–175",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchungsanlass",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "unt_art",
                    "type": "choice",
                    "label": "Ist dies Ihre erste Untersuchung wegen Kohlenstoffdisulfid "
                             "(Schwefelkohlenstoff)?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt, "
                            "Nachuntersuchungen in der Regel nach 6 bis 12 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Ja, Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nein, Nachuntersuchung (ich wurde schon einmal untersucht)"},
                    ],
                },
                {
                    "id": "laenger_krank",
                    "type": "yes_no",
                    "label": "Waren Sie seit der letzten Untersuchung mehrere Wochen am Stück "
                             "krank oder körperlich beeinträchtigt?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "followup": {"id": "laenger_krank_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wie lange?", "when": "yes"},
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
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Belastung",
            "subtitle": "Ihre Arbeit mit Kohlenstoffdisulfid (Schwefelkohlenstoff, CS2)",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
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
            "subtitle": "Persönliche Schutzausrüstung",
            "questions": [
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Tragen Sie bei der Arbeit die vorgesehene persönliche Schutzausrüstung "
                             "(z. B. Schutzhandschuhe, Schutzkleidung, ggf. Atemschutz)?",
                    "hint": "Wegen der Aufnahme über die Haut ist Schutzkleidung bei "
                            "Kohlenstoffdisulfid besonders wichtig.",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "Für meine Tätigkeit ist keine vorgesehen / "
                                                           "Tätigkeit beginnt erst"},
                    ],
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
                    "id": "beschwerden_chronisch",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine oder mehrere der folgenden Beschwerden "
                             "oder Veränderungen bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "inappetenz", "label": "Appetitlosigkeit (Inappetenz)"},
                        {"value": "gewicht", "label": "Ungewollte Gewichtsabnahme"},
                        {"value": "alkohol", "label": "Alkohol wird deutlich schlechter vertragen als früher"},
                        {"value": "schlaf", "label": "Schlafstörungen"},
                        {"value": "gedaechtnis", "label": "Gedächtnisschwäche (Vergesslichkeit)"},
                        {"value": "abstumpfung", "label": "Konzentrationsstörungen oder geistige Abstumpfung"},
                        {"value": "euphorie", "label": "Grundlose Hochstimmung (gelegentliche Euphorie)"},
                        {"value": "gereiztheit", "label": "Gereiztheit oder häufiger Streit (Streitsucht)"},
                        {"value": "depressiv", "label": "Niedergeschlagenheit, depressive Verstimmung"},
                        {"value": "verwirrtheit", "label": "Verwirrtheitszustände"},
                        {"value": "magen_darm", "label": "Häufige Magen-Darm-Beschwerden (z. B. Übelkeit, "
                                                         "Magenschmerzen, Verdauungsstörungen)"},
                        {"value": "keine", "label": "Nichts davon"},
                    ],
                },
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
                    "id": "farbsehen",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Farbsehen verschlechtert (Farben lassen sich schlechter "
                             "unterscheiden als früher)?",
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
                {
                    "id": "vergiftung",
                    "type": "yes_no",
                    "label": "Hatten Sie nach einem Stör- oder Unfall schon einmal Anzeichen einer "
                             "Vergiftung durch Schwefelkohlenstoff (z. B. starke Benommenheit, "
                             "Erregungszustand, Bewusstlosigkeit)?",
                    "required": True,
                    "followup": {"id": "vergiftung_desc", "type": "textarea",
                                 "label": "Wann war das, und sind die Beschwerden vollständig "
                                          "abgeklungen?", "when": "yes"},
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
                    "hint": "Kohlenstoffdisulfid kann möglicherweise die Fruchtbarkeit "
                            "beeinträchtigen oder das Kind im Mutterleib schädigen. "
                            "Die Angabe ist freiwillig.",
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
        # ── 6 ─ Vor der heutigen Untersuchung ──────────────────────────────
        {
            "id": "untersuchungstag",
            "title": "Vor der heutigen Untersuchung",
            "subtitle": "Wichtig für die Bewertung der Urinuntersuchung (Biomonitoring)",
            "questions": [
                {
                    "id": "kohlgemuese",
                    "type": "yes_no",
                    "label": "Haben Sie in den letzten Tagen rohes Kohlgemüse gegessen "
                             "(z. B. Weißkohl, Kohlrabi, Brokkoli, Blumenkohl, Rosenkohl)?",
                    "hint": "Rohes Kohlgemüse kann den Messwert TTCA im Urin erhöhen und so "
                            "das Ergebnis des Biomonitorings verfälschen.",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
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
    # ── Dauernde gesundheitliche Bedenken (Abschnitt 2.1.1) ───────────────
    {"wenn": {"vorerkrankungen": ["nerven", "psyche"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem/Psyche",
     "quelle": "Abschnitte 2.1.1, 2.1.3 und 1.2.3",
     "befund": "Erkrankung des peripheren/zentralen Nervensystems (z. B. Polyneuropathie) "
               "oder psychische Erkrankung angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken nach 2.1.1: Befund durch "
                   "Ergänzungsuntersuchung (fachneurologische und/oder psychiatrische "
                   "Untersuchung, evtl. EEG, Elektroneuro-/Elektromyographie) sichern, "
                   "Vorbefunde einholen. Nur bei weniger ausgeprägten Störungen prüfen, ob "
                   "unter Voraussetzungen nach 2.1.3 (Schutzmaßnahmen, geringere Exposition, "
                   "verkürzte Nachuntersuchungsfristen) keine Bedenken bestehen; bei zu "
                   "erwartender Wiederherstellung befristete Bedenken nach 2.1.2."},
    {"wenn": {"vorerkrankungen": ["herz", "gefaesse", "vegetativ", "hypertonie"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 2.1.1, 2.1.3 und 3.2.1",
     "befund": "Hämodynamisch wirksame Herzerkrankung, Arteriosklerose, ausgeprägte vegetative "
               "Labilität oder arterielle Hypertonie angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken nach 2.1.1 (kritische "
                   "Zielorgane von CS2 sind Herz-Kreislaufsystem und Nervensystem): "
                   "kardiovaskulären Status abklären (Ergometrie nach Anhang 2, Blutdruck, "
                   "kardiologische Vorbefunde). Bei weniger ausgeprägten Befunden Aufnahme/"
                   "Fortsetzung nur unter Voraussetzungen nach 2.1.3 mit verkürzten "
                   "Nachuntersuchungsfristen erwägen."},
    {"wenn": {"vorerkrankungen": ["anaemie", "magen_darm_geschwuer", "niere", "leber"]},
     "schwere": "kritisch",
     "bereich": "Innere Erkrankungen",
     "quelle": "Abschnitte 2.1.1, 2.1.3 und 1.2.2",
     "befund": "Anämie, Magen-Darm-Geschwüre, Nierenleiden oder Leberschädigung angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken nach 2.1.1: Laborstatus "
                   "erheben (kleines Blutbild, γ-GT, SGPT/ALAT, SGOT/ASAT, Cholesterin/"
                   "Triglyceride, Urinstatus mit ggf. Sediment), Vorbefunde einholen. Bei "
                   "weniger ausgeprägten Befunden Voraussetzungen nach 2.1.3 prüfen "
                   "(Schutzmaßnahmen, verkürzte Fristen); bei zu erwartender Wiederherstellung "
                   "befristete Bedenken nach 2.1.2."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Abhängigkeit",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Alkohol- oder Rauschmittelabhängigkeit angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken nach 2.1.1: Suchtanamnese "
                   "ärztlich vertiefen, Behandlungsstand klären. Nur bei stabiler Abstinenz/"
                   "Wiederherstellung befristete Bedenken nach 2.1.2 bzw. Voraussetzungen "
                   "nach 2.1.3 erwägen."},
    {"wenn": {"vergiftung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "CS2-Vergiftung",
     "quelle": "Abschnitt 2.1.2 (Nachuntersuchung)",
     "befund": "Anzeichen einer Kohlenstoffdisulfid-Vergiftung nach außergewöhnlich hoher "
               "Exposition (Stör-/Unfall) angegeben.",
     "konsequenz": "Befristete gesundheitliche Bedenken bis zur Normalisierung der klinischen "
                   "Befunde: klinische Abklärung und Verlaufskontrolle veranlassen. Zu "
                   "beachten: Bei erneutem Einsatz kann eine Überempfindlichkeit gegen "
                   "Kohlenstoffdisulfid bestehen – engmaschig nachuntersuchen."},
    # ── Zwischenanamnese-Symptome, Ergänzungsuntersuchung (1.2.1/1.2.3) ───
    {"wenn": {"beschwerden_chronisch": ["inappetenz", "gewicht", "alkohol", "schlaf",
                                        "gedaechtnis", "abstumpfung", "euphorie",
                                        "gereiztheit", "depressiv", "verwirrtheit",
                                        "magen_darm"]},
     "schwere": "pruefen",
     "bereich": "Chronische CS2-Einwirkung",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung), 1.2.3 und 3.2.3",
     "befund": "Beschwerden angegeben, auf die bei der Zwischenanamnese besonders zu achten "
               "ist (z. B. Inappetenz, Alkohol-Überempfindlichkeit, Schlafstörungen, "
               "Gedächtnisschwäche, Gereiztheit, Verwirrtheit, Gewichtsabnahme).",
     "konsequenz": "Als mögliche Zeichen chronischer CS2-Einwirkung ärztlich vertiefen (Beginn, "
                   "Verlauf, Expositionsbezug). Biomonitoring (TTCA im Urin, Probenahme bei "
                   "Expositions-/Schichtende, BGW 4 mg/g Kreatinin) durchführen. In nicht "
                   "abklärbaren Fällen Ergänzungsuntersuchung nach 1.2.3 (fachneurologische "
                   "und/oder psychiatrische Untersuchung mit evtl. EEG) veranlassen; ggf. "
                   "verkürzte Nachuntersuchungsfrist nach 2.1.3."},
    {"wenn": {"missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Periphere Nerven",
     "quelle": "Abschnitte 1.2.1, 1.2.2, 1.2.3 und 3.2.3",
     "befund": "Distale Missempfindungen (Kribbeln, Taubheit, Brennen) in Händen/Füßen angegeben.",
     "konsequenz": "Verdacht auf beginnende Polyneuropathie: Sensibilität und Reflexe gezielt "
                   "prüfen (Achillessehnenreflexe im Seiten-/Etagenvergleich), "
                   "Vibrationsempfinden mit 128-Hz-Stimmgabel. In unklaren Fällen "
                   "Ergänzungsuntersuchung nach 1.2.3 (fachneurologisch, Elektroneuro-/"
                   "Elektromyographie). Bei gesichertem Hinweis auf Polyneuropathie Bedenken "
                   "nach 2.1.1 prüfen."},
    {"wenn": {"tremor": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zentrales Nervensystem",
     "quelle": "Abschnitte 1.2.1 und 1.2.3",
     "befund": "Tremor der Extremitäten bzw. Parkinson-artige Beschwerden angegeben.",
     "konsequenz": "Neurologischen Status erheben; in Fällen, die durch die allgemeine "
                   "Untersuchung nicht abgeklärt werden können, Ergänzungsuntersuchung nach "
                   "1.2.3 (fachneurologische Untersuchung, evtl. EEG, Elektroneuro-/"
                   "Elektromyographie) veranlassen."},
    {"wenn": {"farbsehen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 1.2.1 und 1.2.2 (Nachuntersuchung)",
     "befund": "Verschlechterung des Farbsehens angegeben.",
     "konsequenz": "Erworbene Farbsehstörung mit geeignetem Testverfahren prüfen; "
                   "Augenhintergrundspiegelung (Bestandteil der speziellen Nachuntersuchung) "
                   "durchführen, ggf. augenärztliche Abklärung veranlassen."},
    {"wenn": {"herzbeschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 1.2.2 und 3.2.1",
     "befund": "Belastungsabhängige Brustschmerzen, Herzstolpern oder Luftnot angegeben.",
     "konsequenz": "Wegen der erhöhten Rate koronarer Herzerkrankungen bei chronischer "
                   "CS2-Exposition kardiologisch abklären: Ergometrie (Anhang 2, Leitfaden "
                   "»Ergometrie«) gezielt auswerten, ggf. fachkardiologische Vorstellung. "
                   "Je nach Befund Bedenken nach 2.1.1/2.1.2 prüfen."},
    {"wenn": {"beine_durchblutung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gefäße",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung) und 3.2.3",
     "befund": "Hinweise auf Durchblutungsstörung der Beine (Claudicatio, kalte/blasse Füße).",
     "konsequenz": "Palpation der Arteria dorsalis pedis und Arteria tibialis posterior, "
                   "Gefäßstatus erheben; bei Auffälligkeiten angiologische Abklärung "
                   "(CS2-bedingte Gefäßsklerose möglich). Je nach Befund Bedenken nach "
                   "2.1.1 (Arteriosklerose) prüfen."},
    # ── Haut und Exposition ───────────────────────────────────────────────
    {"wenn": {"haut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 1.2.1 und 2.2",
     "befund": "Großflächige Hautveränderungen (z. B. Psoriasis vulgaris) angegeben.",
     "konsequenz": "Auf großflächige Hautveränderungen ist besonders zu achten (erhöhte "
                   "Aufnahme über vorgeschädigte Haut): Hautbefund ärztlich beurteilen, "
                   "konsequenten Hautschutz und geeignete Schutzkleidung sicherstellen "
                   "(stoffspezifische Hinweise in GESTIS); Biomonitoring zur Kontrolle der "
                   "inneren Belastung."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Dermale Exposition",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung), 3.1.3 und 2.2",
     "befund": "Möglicher Hautkontakt mit flüssigem Kohlenstoffdisulfid angegeben.",
     "konsequenz": "Dermale Exposition in der Arbeitsanamnese dokumentieren und bewerten; "
                   "Biomonitoring (TTCA im Urin) durchführen, da es auch die Hautaufnahme "
                   "erfasst. Zu Schutzkleidung und Handschuhen beraten (hautresorptive "
                   "Eigenschaften von CS2); ggf. Aktualisierung der Gefährdungsbeurteilung "
                   "beim Arbeitgeber anregen."},
    {"wenn": {"stoerfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Expositionsspitzen",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung) und 2.2",
     "befund": "Störfall bzw. kurzzeitige Überschreitung des Luftgrenzwerts angegeben.",
     "konsequenz": "Intensität der Exposition klären (kurzzeitige Grenzwertüberschreitung?); "
                   "Biomonitoring durchführen und auf Vergiftungszeichen achten. Ergibt sich "
                   "Bedarf zur Verbesserung des Arbeitsschutzes, Mitteilung an den Arbeitgeber "
                   "unter Wahrung der schutzwürdigen Belange der untersuchten Person."},
    # ── Anlassbezogene Nachuntersuchung, BK-Verdacht ──────────────────────
    {"wenn": {"laenger_krank": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenzeitliche Erkrankung",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Mehrwöchige Erkrankung bzw. körperliche Beeinträchtigung seit der letzten "
               "Untersuchung angegeben.",
     "konsequenz": "Erkrankung daraufhin bewerten, ob sie Anlass zu Bedenken gegen die "
                   "Fortsetzung der Tätigkeit geben könnte (Kriterien nach 2.1.1); Befunde "
                   "der behandelnden Ärzte einholen, ggf. verkürzte Nachuntersuchungsfrist "
                   "festlegen."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbedingte Beschwerden",
     "quelle": "Abschnitte 1.1 und 4 (BK-Nr. 1305)",
     "befund": "Proband/in vermutet Zusammenhang zwischen Beschwerden und der Tätigkeit.",
     "konsequenz": "Beschwerden gezielt abklären (Anspruch auf vorzeitige Nachuntersuchung); "
                   "Expositionsbezug prüfen, Biomonitoring einbeziehen. Bei begründetem "
                   "Verdacht auf eine Erkrankung durch Schwefelkohlenstoff ärztliche Anzeige "
                   "wegen Berufskrankheit Nr. 1305 BKV erstatten."},
    # ── Schutzmaßnahmen und Beratung ──────────────────────────────────────
    {"wenn": {"psa_nutzung": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitt 2.2",
     "befund": "Persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Wegen der hautresorptiven Eigenschaften von CS2 kommt der Schutzkleidung "
                   "besondere Bedeutung zu: eindringlich zu Trageverhalten und Hygiene "
                   "beraten, Ursachen klären. Ergibt sich Bedarf zur Aktualisierung der "
                   "Gefährdungsbeurteilung, Mitteilung an den Arbeitgeber unter Wahrung der "
                   "schutzwürdigen Belange."},
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 3.1.1",
     "befund": "Tätigkeit mit CS2-Exposition in Lärmbereichen angegeben.",
     "konsequenz": "Kohlenstoffdisulfid ist ototoxisch: mögliche Kombinationswirkungen mit "
                   "Lärm bei der Gehöruntersuchung nach dem Grundsatz G 20 berücksichtigen; "
                   "beide Untersuchungen aufeinander abstimmen."},
    {"wenn": {"kohlgemuese": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 3.1.4 (Störfaktoren)",
     "befund": "Verzehr von rohem Kohlgemüse in den letzten Tagen angegeben.",
     "konsequenz": "Störfaktor beim Biomonitoring: Die TTCA-Ausscheidung im Urin kann durch "
                   "rohes Kohlgemüse erhöht sein. Bei der Bewertung des TTCA-Werts "
                   "(BGW 4 mg/g Kreatinin) berücksichtigen, ggf. Kontrolle nach "
                   "kohlgemüsefreien Tagen wiederholen."},
    {"wenn": {"schwangerschaft": ["schwanger", "kinderwunsch"]},
     "schwere": "pruefen",
     "bereich": "Fortpflanzung/Mutterschutz",
     "quelle": "Abschnitt 2.2",
     "befund": "Schwangerschaft angegeben/vermutet oder Kinderwunsch geäußert.",
     "konsequenz": "Hinsichtlich der möglichen fortpflanzungsgefährdenden und "
                   "fruchtschädigenden Wirkung von Kohlenstoffdisulfid beraten; bei "
                   "Schwangerschaft unverzüglich Mutterschutzregelungen beachten und auf "
                   "Expositionsvermeidung sowie eine angepasste Gefährdungsbeurteilung "
                   "durch den Arbeitgeber hinwirken."},
]
