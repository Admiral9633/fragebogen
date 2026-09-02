# -*- coding: utf-8 -*-
"""G 9 Quecksilber oder seine Verbindungen – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016,
G 9 »Quecksilber oder seine Verbindungen« (Fassung Oktober 2014), S. 197–206."""

SLUG = "g9-quecksilber-2016"

CATALOG = {
    "version": 2,
    "title": "G 9 Quecksilber oder seine Verbindungen (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 9 »Quecksilber oder seine Verbindungen« (Fassung Oktober 2014), "
             "S. 197–206",
    "sections": [
        # ── 1 ─ Anlass der Untersuchung ────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Ist dies Ihre erste Untersuchung nach dem Grundsatz G 9 "
                             "(Quecksilber), oder eine Nachuntersuchung?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt. "
                            "Nachuntersuchungen sind nach 6–12 Monaten vorgesehen – vorzeitig "
                            "u. a. nach schwerer oder längerer Erkrankung oder wenn Sie einen "
                            "Zusammenhang zwischen Beschwerden und Ihrer Arbeit vermuten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Umgang mit Quecksilber",
            "subtitle": "Ihre Arbeit mit Quecksilber oder seinen Verbindungen",
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
                    "label": "In welchen Bereichen haben Sie mit Quecksilber oder seinen "
                             "Verbindungen zu tun?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "herstellung", "label": "Herstellen oder Aufbereiten von Quecksilber und "
                                                          "seinen Verbindungen (Filtrieren, Reinigen, Destillieren)"},
                        {"value": "messgeraete", "label": "Herstellung, Wartung oder Reparatur quecksilberhaltiger "
                                                          "Mess- und Regelgeräte (Barometer, Thermometer, Glasbläserei)"},
                        {"value": "elektro", "label": "Elektrotechnik (Gleichrichter, Unterbrecher, "
                                                      "Quecksilberdampflampen, Leuchtstoffröhren, Knopfzellen)"},
                        {"value": "labor", "label": "Labor / Hochvakuumtechnik (Quecksilberpumpen, "
                                                    "Sperrflüssigkeit in Gaslaboratorien)"},
                        {"value": "chemie", "label": "Chloralkalielektrolyse, Katalysator, Amalgamieren "
                                                     "oder Herstellen von Alkoholaten"},
                        {"value": "pyrotechnik", "label": "Pyrotechnische Gegenstände und Explosivstoffe "
                                                          "(z. B. Fulminate)"},
                        {"value": "antifouling", "label": "Quecksilberhaltige Antifoulingfarben "
                                                          "(z. B. Schiffsanstriche)"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an Gebäuden, die mit Quecksilber "
                                                      "belastet sind oder waren"},
                        {"value": "recycling", "label": "Recycling quecksilberhaltiger Materialien"},
                        {"value": "sonstige", "label": "Sonstige Bereiche"},
                        {"value": "keine", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "stoffart",
                    "type": "multi_choice",
                    "label": "Mit welcher Art von Quecksilber haben Sie zu tun?",
                    "hint": "Mehrfachauswahl möglich. Organische Quecksilberverbindungen "
                            "(z. B. Alkylquecksilber) können auch über die Haut aufgenommen werden.",
                    "required": True,
                    "options": [
                        {"value": "metallisch", "label": "Metallisches (flüssiges) Quecksilber"},
                        {"value": "anorganisch", "label": "Anorganische Quecksilberverbindungen (Salze)"},
                        {"value": "organisch", "label": "Organische Quecksilberverbindungen "
                                                        "(z. B. Alkylquecksilber)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "frueher_exposition",
                    "type": "yes_no",
                    "label": "Waren Sie schon früher – in anderen Tätigkeiten – Quecksilber oder "
                             "seinen Verbindungen ausgesetzt?",
                    "required": True,
                    "followup": {"id": "frueher_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, und wie lange?",
                                 "when": "yes"},
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
                    "id": "laermbereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie bei diesen Tätigkeiten auch in Lärmbereichen "
                             "(so laut, dass Gehörschutz vorgeschrieben ist)?",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
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
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, die auf eine Quecksilberbelastung hinweisen können",
            "questions": [
                {
                    "id": "mattigkeit",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich in letzter Zeit ungewöhnlich matt und erschöpft, "
                             "oder haben Sie häufig Kopf- und Gliederschmerzen?",
                    "required": True,
                },
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
                             "einen dunklen Saum am Zahnfleisch, wunde Stellen im Mund oder "
                             "gelockerte Zähne?",
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
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "hg_vergiftung",
                    "type": "yes_no",
                    "label": "Haben Sie schon einmal eine schwere Quecksilbervergiftung "
                             "durchgemacht?",
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
                    "id": "amalgam",
                    "type": "yes_no",
                    "label": "Haben Sie Zahnfüllungen aus Amalgam?",
                    "hint": "Amalgamfüllungen enthalten Quecksilber; das ist für die Beurteilung "
                            "des Gebisses und der Laborwerte wichtig.",
                    "required": True,
                },
                {
                    "id": "erkrankung_seit_letzter",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder länger "
                             "dauernde Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "erkrankung_seit_letzter_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {"id": "zusammenhang_vermutet_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
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
    # ── Bedenkenstatbestände nach Abschnitt 2.1.1 ─────────────────────────
    {"wenn": {"hg_vergiftung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitte 2.1.1 und 2.1.2",
     "befund": "Überstandene schwere Quecksilbervergiftung angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken nach 2.1.1; eine "
                   "Befristung nach 2.1.2 ist bei überstandener schwerer "
                   "Quecksilbervergiftung ausdrücklich ausgeschlossen. Vorbefunde einholen, "
                   "Biomonitoring und neurologischen Befund erheben; nur bei geringer "
                   "Ausprägung Prüfung nach 2.1.3, ob die Tätigkeit unter Voraussetzungen "
                   "(Schutzmaßnahmen, verkürzte Nachuntersuchungsfristen) möglich ist."},
    {"wenn": {"nierenerkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitte 1.2.2 und 2.1.1 (Nierenleiden, tubuläre Schäden)",
     "befund": "Nierenerkrankung angegeben.",
     "konsequenz": "Abklärung vor Beurteilung: Kreatinin im Serum, quantitative "
                   "Eiweißbestimmung im Urin, bei Verdacht auf Nierenerkrankung "
                   "α1-Mikroglobulin oder N-Acetyl-ß-D-Glucosaminidase im Urin (1.2.2). "
                   "Bei Nierenleiden mit tubulären Schäden dauernde Bedenken nach 2.1.1, "
                   "bei erwartbarer Wiederherstellung befristete Bedenken nach 2.1.2; bei "
                   "geringer Ausprägung Voraussetzungen nach 2.1.3 prüfen."},
    {"wenn": {"neuro_erkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 2.1.1 (neurologische Krankheiten)",
     "befund": "Neurologische Erkrankung angegeben.",
     "konsequenz": "Fachneurologische Befunde einholen; neurologische Krankheiten sind "
                   "Tatbestand für dauernde gesundheitliche Bedenken nach 2.1.1 (bei "
                   "erwartbarer Wiederherstellung befristet nach 2.1.2). Bei weniger "
                   "ausgeprägten Störungen prüfen, ob die Tätigkeit unter den "
                   "Voraussetzungen nach 2.1.3 (Schutzmaßnahmen, geringere Exposition, "
                   "verkürzte Nachuntersuchungsfristen) möglich ist."},
    {"wenn": {"psychovegetativ": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 2.1.1 (ausgeprägte psycho-vegetative Störungen)",
     "befund": "Psycho-vegetative Störungen angegeben.",
     "konsequenz": "Ausmaß ärztlich klären: ausgeprägte psycho-vegetative Störungen sind "
                   "Tatbestand für dauernde Bedenken nach 2.1.1, bei erwartbarer "
                   "Wiederherstellung befristet nach 2.1.2; bei geringer Ausprägung "
                   "Voraussetzungen nach 2.1.3 prüfen (z. B. verkürzte "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"schilddruese": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 2.1.1 (manifeste Schilddrüsenüberfunktion)",
     "befund": "Schilddrüsenüberfunktion angegeben.",
     "konsequenz": "Klären, ob eine manifeste Überfunktion vorliegt (aktuelle Befunde bzw. "
                   "internistische Abklärung): dann Bedenkenstatbestand nach 2.1.1, bei "
                   "erwartbarer Wiederherstellung (z. B. unter Therapie) befristete "
                   "Bedenken nach 2.1.2; bei gut eingestellter Stoffwechsellage "
                   "Voraussetzungen nach 2.1.3 prüfen."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitt 2.1.1 (Alkohol-, Drogen-, Medikamentenabhängigkeit)",
     "befund": "Alkohol-, Drogen- oder Medikamentenabhängigkeit angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken nach 2.1.1, bei "
                   "erwartbarer Wiederherstellung (erfolgreiche Entwöhnung) befristete "
                   "Bedenken nach 2.1.2; Behandlungs- und Beratungsangebote aufzeigen, "
                   "Verlauf vor erneuter Beurteilung dokumentieren."},
    # ── Beschwerden (Abschnitte 1.2.1, 1.2.3 und 3.2.3) ───────────────────
    {"wenn": {"tremor": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitte 1.2.1, 1.2.3 und 3.2.3",
     "befund": "Zittern der Hände/Finger bzw. Schüttelbewegungen angegeben (möglicher "
               "Tremor mercurialis).",
     "konsequenz": "Ergänzungsuntersuchung nach 1.2.3 durchführen: Schriftprobe unter "
                   "Beobachtung (Trend zur Zitterschrift), neurologischen Befund erheben, "
                   "Biomonitoring veranlassen; bei auffälligem Befund neurologische "
                   "Facharztvorstellung und Überprüfung der Exposition."},
    {"wenn": {"sprache": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitte 1.2.1 und 3.2.3",
     "befund": "Sprechstörungen angegeben (möglicher Psellismus mercurialis).",
     "konsequenz": "Neurologischen und psychischen Befund erheben, Schriftprobe unter "
                   "Beobachtung (1.2.3) und Biomonitoring durchführen; bei "
                   "Auffälligkeiten neurologische Abklärung veranlassen."},
    {"wenn": {"stimmung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitte 1.2.1 und 3.2.3",
     "befund": "Reizbarkeit, ängstliche Befangenheit oder Stimmungslabilität angegeben "
               "(möglicher Erethismus mercurialis).",
     "konsequenz": "Psychischen Befund vertieft erheben (Stimmungslabilität, Erethismus, "
                   "vegetative Störungen), Biomonitoring veranlassen; Verlauf engmaschig "
                   "kontrollieren, ggf. verkürzte Nachuntersuchungsfrist nach 2.1.3."},
    {"wenn": {"missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden Nervensystem",
     "quelle": "Abschnitt 3.2.3 (periphere Polyneuropathie)",
     "befund": "Kribbeln, Taubheitsgefühle oder Schwäche in Armen/Beinen angegeben "
               "(mögliche periphere Polyneuropathie).",
     "konsequenz": "Neurologische Abklärung (Polyneuropathie) veranlassen, andere Ursachen "
                   "ausschließen; Biomonitoring durchführen und Befund bei der Beurteilung "
                   "nach 2.1 berücksichtigen."},
    {"wenn": {"mattigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden allgemein",
     "quelle": "Abschnitt 1.2.1 (Zwischenanamnese)",
     "befund": "Mattigkeit bzw. Kopf- und Gliederschmerzen angegeben – auf solche Klagen "
               "ist bei der Nachuntersuchung besonders zu achten.",
     "konsequenz": "Vertiefte Zwischenanamnese und körperliche Untersuchung; Biomonitoring "
                   "veranlassen, andere Ursachen abklären; Beschwerden als mögliches "
                   "Frühzeichen einer chronischen Quecksilberbelastung dokumentieren."},
    {"wenn": {"mund": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Mund/Zähne",
     "quelle": "Abschnitte 1.2.1 und 3.2.2",
     "befund": "Entzündung der Mundschleimhaut/des Zahnfleischs, Zahnfleischsaum oder "
               "Zahnlockerung angegeben.",
     "konsequenz": "Inspektion der Mundhöhle (Stomatitis, Gingivitis, Quecksilbersaum am "
                   "Zahnfleisch) und Erhebung des Gebisszustands einschließlich "
                   "Amalgamfüllungen; als mögliches Zeichen einer Quecksilberaufnahme "
                   "werten, Biomonitoring veranlassen, ggf. zahnärztliche Vorstellung."},
    {"wenn": {"hautekzem": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 3.2.3 (allergisches Kontaktekzem)",
     "befund": "Juckende Hautausschläge oder Ekzeme angegeben.",
     "konsequenz": "Abklärung eines allergischen Kontaktekzems (dermatologische Vorstellung, "
                   "ggf. Epikutantestung); Hautkontakt – insbesondere zu organischen "
                   "Quecksilberverbindungen – und Schutzausrüstung überprüfen."},
    # ── Exposition und Biomonitoring (Abschnitte 1.2.2 und 3.1) ───────────
    {"wenn": {"stoffart": ["organisch"]},
     "schwere": "hinweis",
     "bereich": "Stoffart/Hautresorption",
     "quelle": "Abschnitte 3.1.3 und 3.1.4",
     "befund": "Umgang mit organischen Quecksilberverbindungen angegeben.",
     "konsequenz": "Beratung: Nur organische Quecksilberverbindungen werden auch über die "
                   "Haut aufgenommen – Hautkontakt strikt vermeiden, geeignete Handschuhe. "
                   "Beim Biomonitoring beachten: für organische Verbindungen ist kein "
                   "biologischer Grenzwert festgelegt (EKA nicht festgelegt), Untersuchung "
                   "im Vollblut."},
    {"wenn": {"frueher_exposition": ["yes"], "untersuchung_art": ["erst"]},
     "schwere": "pruefen",
     "bereich": "Vorexposition",
     "quelle": "Abschnitte 1.2.2 und 3.1.4",
     "befund": "Frühere Quecksilberexposition bei einer Erstuntersuchung angegeben.",
     "konsequenz": "Biomonitoring bereits bei der Erstuntersuchung durchführen – nach 1.2.2 "
                   "ist es dort nur bei früherer Quecksilberexposition angezeigt (BGW für "
                   "metallisches Quecksilber und anorganische Verbindungen: 25 µg/g "
                   "Kreatinin bzw. 30 µg/l Urin); frühere Befunde und Expositionsdaten "
                   "einholen."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitte 1.2.2 und 2.2",
     "befund": "Zwischenfall/Unfall mit Freisetzung von Quecksilber angegeben.",
     "konsequenz": "Hergang dokumentieren und Biomonitoring aus besonderem Anlass "
                   "veranlassen; ergeben sich Hinweise auf unzureichenden Arbeitsschutz, "
                   "Mitteilung an den Arbeitgeber zur Aktualisierung der "
                   "Gefährdungsbeurteilung (2.2) unter Wahrung der schutzwürdigen Belange "
                   "der untersuchten Person."},
    # ── Vorzeitige Nachuntersuchung und BK-Verdacht (Abschnitte 1.1, 4) ───
    {"wenn": {"erkrankung_seit_letzter": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenzeitliche Erkrankung",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder länger dauernde Erkrankung seit der letzten Untersuchung "
               "angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen die Fortsetzung der "
                   "Tätigkeit gibt (Kriterium für eine vorzeitige Nachuntersuchung nach "
                   "1.1); Befunde und Arztberichte einholen, Beurteilung nach 2.1 "
                   "aktualisieren."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 1.1 und 4 (BK-Nr. 1102)",
     "befund": "Die untersuchte Person vermutet einen Zusammenhang zwischen Erkrankung "
               "und Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist bei vermutetem Zusammenhang vorgesehen "
                   "(1.1): Beschwerden gezielt abklären (Biomonitoring, neurologischer "
                   "Befund, Schriftprobe); bei begründetem Verdacht auf eine Erkrankung "
                   "durch Quecksilber ärztliche Anzeige wegen BK-Nr. 1102 der Anlage 1 "
                   "zur BKV erstatten."},
    # ── Schutzverhalten und Kombinationswirkung (Abschnitte 2.2 und 3.1.1) ─
    {"wenn": {"psa": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Individuelle Aufklärung und Beratung zu Hygienemaßnahmen und "
                   "persönlicher Schutzausrüstung (2.2); Ursachen der Nichtbenutzung "
                   "klären. Ergeben sich Hinweise auf notwendige Verbesserungen des "
                   "Arbeitsschutzes, Mitteilung an den Arbeitgeber zur Aktualisierung "
                   "der Gefährdungsbeurteilung."},
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 3.1.1",
     "befund": "Tätigkeit mit höherer Exposition wird auch in Lärmbereichen ausgeübt.",
     "konsequenz": "Wegen der möglichen ototoxischen Eigenschaften von Quecksilber "
                   "Kombinationswirkungen mit Lärm bei der Gehöruntersuchung nach dem "
                   "Grundsatz G 20 berücksichtigen."},
]
