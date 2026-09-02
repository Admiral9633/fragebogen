# -*- coding: utf-8 -*-
"""Polycyclische aromatische Kohlenwasserstoffe (Pyrolyseprodukte aus organischem
Material) – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische
Beratungen und Untersuchungen, 1. Auflage 2024, »Polycyclische aromatische
Kohlenwasserstoffe (Pyrolyseprodukte aus organischem Material)« (E PAK,
Fassung Januar 2022), S. 477–500."""

SLUG = "pak-2024"

CATALOG = {
    "version": 2,
    "title": "Polycyclische aromatische Kohlenwasserstoffe (Pyrolyseprodukte aus "
             "organischem Material) (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Polycyclische aromatische Kohlenwasserstoffe "
             "(Pyrolyseprodukte aus organischem Material)« (E PAK, Fassung Januar 2022), "
             "S. 477–500",
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
                             "PAK (Teer, Pech, Ruß und ähnliche Pyrolyseprodukte)?",
                    "hint": "PAK = polycyclische aromatische Kohlenwasserstoffe. Sie stecken "
                            "z. B. in Steinkohlenteer, Pech, Ruß und Verbrennungsrückständen. "
                            "Nachgehende Vorsorge: Untersuchung nach dem Ende der Tätigkeit "
                            "mit diesen Stoffen.",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge wegen PAK"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur PAK-Vorsorge"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge – ich arbeite nicht mehr mit diesen Stoffen"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn Sie "
                            "wiederholt krebserzeugenden PAK ausgesetzt sind oder eine "
                            "Gefährdung durch Hautkontakt nicht ausgeschlossen werden kann.",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "not_in": ["nachgehend"]},
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
            "subtitle": "Ihre Arbeit mit Teer, Pech, Ruß oder Verbrennungsprodukten",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "taetigkeitsbereiche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie (oder haben Sie gearbeitet)?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "kokerei", "label": "Ofenarbeiten in einer Steinkohlekokerei"},
                        {"value": "teer_pech", "label": "Verarbeiten von Steinkohlenteer oder Pech "
                                                        "(z. B. Abdichten, Imprägnieren, Bindemittel)"},
                        {"value": "elektroden", "label": "Festpech/Elektroden: Herstellung oder Verarbeitung von "
                                                         "Elektroden, Elektrographit oder Söderberg-Elektroden (Aluminium)"},
                        {"value": "metall", "label": "Eisen-/Stahl-/Metallerzeugung: Hochofen-Abstich, Pfannenfeuerplatz, "
                                                     "Feuerfestmaterial mit Teerpechbindung"},
                        {"value": "sanierung", "label": "Abtragen/Entfernen teer- oder pechhaltiger Materialien "
                                                        "(alte Straßenbeläge, Beschichtungen, Holzpflaster, Kork-Teer-Dämmung)"},
                        {"value": "brand_kontamination", "label": "Brandsanierung oder Reinigung PAK-belasteter "
                                                                  "(kontaminierter) Bereiche"},
                        {"value": "schornstein", "label": "Schornsteinreinigung von Kohle- oder Holzfeuerungen"},
                        {"value": "brennschneiden", "label": "Brennschneiden oder Schweißen an teerbehafteten Teilen"},
                        {"value": "kreosot", "label": "Arbeiten mit Teerölen (Kreosot), z. B. imprägniertes Holz "
                                                      "(Bahnschwellen, Masten)"},
                        {"value": "sonstige", "label": "Andere Tätigkeit mit Teer, Pech, Ruß oder Verbrennungsrückständen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit diesen Stoffen?",
                    "required": True,
                    "options": [
                        {"value": "beginnt", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis15", "label": "5 bis 15 Jahre"},
                        {"value": "ueber15", "label": "Mehr als 15 Jahre"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit direkt mit Teer, Pech, Ruß "
                             "oder deren Dämpfen in Kontakt?",
                    "hint": "PAK können auch über die Haut in den Körper gelangen – schon "
                            "bei kleinflächigem oder kurzem Kontakt. Bei heißen Produkten "
                            "auch über Dämpfe oder Nebel (Aerosole).",
                    "required": True,
                },
                {
                    "id": "heisse_verarbeitung",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit heißen oder erhitzten Teer-/Pechprodukten, "
                             "bei denen Rauch oder Dämpfe entstehen?",
                    "required": True,
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es Zwischenfälle, Unfälle oder ungewöhnliche Betriebszustände, "
                             "bei denen Sie diesen Stoffen besonders stark ausgesetzt waren?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_exposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Berufen oder Tätigkeiten Kontakt mit Teer, "
                             "Pech, Ruß oder anderen krebserzeugenden Stoffen?",
                    "required": True,
                    "followup": {"id": "frueher_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, und wie lange?", "when": "yes"},
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Läuft bei Ihnen ein Berufskrankheiten-Verfahren, oder wurde schon "
                             "einmal eine Berufskrankheit anerkannt?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Erkrankung bzw. welches Verfahren?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Ihre Schutzausrüstung und Arbeitshygiene",
            "questions": [
                {
                    "id": "psa",
                    "type": "multi_choice",
                    "label": "Welche Schutzausrüstung benutzen Sie bei diesen Arbeiten?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "handschuhe", "label": "Geeignete Schutzhandschuhe"},
                        {"value": "atemschutz", "label": "Atemschutz (Maske)"},
                        {"value": "schutzkleidung", "label": "Schutzkleidung / regelmäßiger Wechsel der Arbeitskleidung"},
                        {"value": "hautschutz", "label": "Hautschutz- und Hautpflegemittel"},
                        {"value": "keine", "label": "Keine Schutzausrüstung"},
                    ],
                },
                {
                    "id": "hygiene",
                    "type": "choice",
                    "label": "Können Sie die Hygieneregeln am Arbeitsplatz einhalten "
                             "(Hände/Haut reinigen, Arbeits- und Straßenkleidung trennen, "
                             "am Arbeitsplatz nicht essen, trinken oder rauchen)?",
                    "hint": "PAK können sonst verschleppt oder über den Mund aufgenommen werden.",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "teilweise", "label": "Nur teilweise"},
                        {"value": "nein", "label": "Nein / kaum möglich"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie gesundheitliche Probleme mit der Schutzausrüstung "
                             "(z. B. Hautprobleme unter Handschuhen, Beschwerden unter Atemschutz)?",
                    "required": True,
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Haut ───────────────────────────────────────────────────────
        {
            "id": "haut",
            "title": "Haut",
            "subtitle": "Beschwerden und Vorerkrankungen der Haut",
            "questions": [
                {
                    "id": "haut_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie derzeit Hautbeschwerden?",
                    "required": True,
                    "options": [
                        {"value": "juckreiz", "label": "Juckreiz"},
                        {"value": "roetung", "label": "Örtliche Hautrötungen oder Entzündungen"},
                        {"value": "keine", "label": "Nein, keine Hautbeschwerden"},
                    ],
                },
                {
                    "id": "hautveraenderungen",
                    "type": "yes_no",
                    "label": "Haben Sie neue oder veränderte Hautstellen bemerkt – z. B. Warzen, "
                             "raue verhornte Stellen, dunkle Flecken oder schlecht heilende Stellen?",
                    "hint": "Besonders wichtig sind Gesicht, Ohren, Handrücken, Unterarme, "
                            "Unterbauch und Genitalbereich – dort treten sogenannte Teer- oder "
                            "Pechwarzen bevorzugt auf.",
                    "required": True,
                    "followup": {"id": "hautveraenderungen_desc", "type": "textarea",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "sonnenempfindlichkeit",
                    "type": "yes_no",
                    "label": "Ist Ihre Haut besonders empfindlich gegen Sonnenlicht "
                             "(schnelle Rötung, Sonnenbrand, Lichtreaktionen)?",
                    "hint": "PAK können die Haut lichtempfindlicher machen (Photosensibilisierung).",
                    "required": True,
                },
                {
                    "id": "hautkrebs_vorgeschichte",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal Hautkrebs oder eine Vorstufe davon "
                             "(z. B. aktinische Keratose, Basaliom) – auch wenn er erfolgreich "
                             "behandelt wurde?",
                    "required": True,
                    "followup": {"id": "hautkrebs_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "hauterkrankungen",
                    "type": "multi_choice",
                    "label": "Bestehen bei Ihnen Hauterkrankungen oder besondere Hautzustände?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "ekzemneigung", "label": "Neigung zu Ekzemen (juckende, entzündete Hautausschläge)"},
                        {"value": "akne", "label": "Schwere Akne"},
                        {"value": "seborrhoe", "label": "Ausgeprägte Seborrhoe (sehr fettige Haut)"},
                        {"value": "vitiligo", "label": "Ausgedehnte Vitiligo (Weißfleckenkrankheit)"},
                        {"value": "ichthyose", "label": "Ausgeprägte Ichthyose (Fischschuppenkrankheit)"},
                        {"value": "porphyrie", "label": "Porphyria cutanea tarda (Stoffwechselerkrankung mit Blasenbildung "
                                                        "an lichtausgesetzter Haut)"},
                        {"value": "lichtschaeden", "label": "Deutliche Lichtschäden der Haut "
                                                            "(»Seemanns-« oder »Landmannshaut«)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
            ],
        },
        # ── 5 ─ Atemwege ───────────────────────────────────────────────────
        {
            "id": "atemwege",
            "title": "Atemwege & Lunge",
            "subtitle": "Beschwerden und Erkrankungen der Atemwege",
            "questions": [
                {
                    "id": "atem_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie derzeit Beschwerden der Atemwege?",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Husten"},
                        {"value": "heiserkeit", "label": "Heiserkeit"},
                        {"value": "auswurf", "label": "Auswurf (Schleim beim Husten)"},
                        {"value": "atemnot", "label": "Atemnot / Luftnot"},
                        {"value": "keine", "label": "Nein, keine Beschwerden"},
                    ],
                },
                {
                    "id": "atemwegserkrankung",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen eine chronische Erkrankung der Atemwege oder "
                             "der Lunge (z. B. Asthma, COPD, chronische Bronchitis)?",
                    "required": True,
                    "followup": {"id": "atemwegserkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Harnwege ───────────────────────────────────────────────────
        {
            "id": "harnwege",
            "title": "Blase & Harnwege",
            "subtitle": "PAK können nach langjähriger Einwirkung die Harnwege schädigen",
            "questions": [
                {
                    "id": "blut_urin",
                    "type": "yes_no",
                    "label": "Haben Sie Blut im Urin bemerkt (auch nur einmal, z. B. rötliche "
                             "oder bräunliche Verfärbung)?",
                    "required": True,
                },
                {
                    "id": "wasserlassen",
                    "type": "yes_no",
                    "label": "Müssen Sie auffallend häufig Wasser lassen, oder ist das "
                             "Wasserlassen schmerzhaft?",
                    "required": True,
                },
                {
                    "id": "harnwegserkrankung",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine chronische Erkrankung der "
                             "Blase oder der Harnwege, insbesondere ein Tumor (Neubildung)?",
                    "required": True,
                    "followup": {"id": "harnwegserkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
            ],
        },
        # ── 7 ─ Allgemeines ────────────────────────────────────────────────
        {
            "id": "allgemein",
            "title": "Allgemeine Gesundheit & Rauchen",
            "subtitle": "Weitere Angaben zu Ihrer Gesundheit",
            "questions": [
                {
                    "id": "allgemein_einschraenkungen",
                    "type": "yes_no",
                    "label": "Haben Sie sonstige chronische Erkrankungen oder gesundheitliche "
                             "Einschränkungen?",
                    "required": True,
                    "followup": {"id": "allgemein_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
                },
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Wichtig für die Bewertung der Urinwerte: Auch Tabakrauch enthält "
                            "PAK und erhöht den Messwert 1-Hydroxypyren im Urin.",
                    "required": True,
                    "options": [
                        {"value": "taeglich", "label": "Ja, täglich"},
                        {"value": "gelegentlich", "label": "Ja, gelegentlich"},
                        {"value": "frueher", "label": "Früher, nicht mehr"},
                        {"value": "nie", "label": "Nein, nie"},
                    ],
                },
                {
                    "id": "schwanger",
                    "type": "choice",
                    "label": "Sind Sie schwanger, oder stillen Sie derzeit?",
                    "hint": "PAK sind krebserzeugend, erbgutverändernd und fortpflanzungs-"
                            "gefährdend. Für werdende und stillende Mütter gelten besondere "
                            "Beschäftigungsbeschränkungen (Mutterschutzgesetz).",
                    "required": True,
                    "options": [
                        {"value": "schwanger", "label": "Ja, ich bin schwanger"},
                        {"value": "stillend", "label": "Ja, ich stille"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "entfaellt", "label": "Trifft auf mich nicht zu / keine Angabe"},
                    ],
                },
            ],
        },
        # ── 8 ─ Einwilligung ───────────────────────────────────────────────
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
    # ── Beschäftigungsbeschränkungen (Abschnitt 7.1, MuSchG) ──────────────
    {"wenn": {"schwanger": ["schwanger", "stillend"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 7.1 (Beratung) i. V. m. MuSchG; Abschnitt 6 (PAK: krebserzeugend, "
               "keimzellmutagen, reproduktionstoxisch Kat. 1B)",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben.",
     "konsequenz": "VOR (weiterer) Tätigkeit klären: Beschäftigungsbeschränkungen nach dem "
                   "Mutterschutzgesetz für Tätigkeiten mit krebserzeugenden, keimzellmutagenen "
                   "und reproduktionstoxischen Stoffen (Kat. 1B) prüfen; unverzügliche "
                   "Information an den Arbeitgeber zur mutterschutzrechtlichen "
                   "Gefährdungsbeurteilung; bis zur Klärung keine Tätigkeit mit PAK-Exposition."},
    # ── Haut (Abschnitte 6.3, 7.2.2, 7.4) ─────────────────────────────────
    {"wenn": {"hautkrebs_vorgeschichte": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien Haut), 7.4.2–7.4.4",
     "befund": "Hautkrebserkrankung und/oder deren Vorstufen (auch nach erfolgreicher "
               "Behandlung) angegeben.",
     "konsequenz": "Hautfachärztliche Befunde einholen, Ganzkörperinspektion durchführen. "
                   "Prüfen, ob die Tätigkeit ohne gesundheitliche Gefährdung möglich ist "
                   "(7.4): Maßnahmen nach 7.4.2 (Substitution, technische/organisatorische/"
                   "persönliche Schutzmaßnahmen), verkürzte Vorsorgefristen nach 7.4.3; bei "
                   "fehlender Erfolgsaussicht Tätigkeitswechsel nach 7.4.4 erwägen (Mitteilung "
                   "an den Arbeitgeber nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"hauterkrankungen": ["ekzemneigung", "akne", "seborrhoe", "vitiligo",
                                   "ichthyose", "porphyrie", "lichtschaeden"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien Haut), 7.4.2–7.4.3",
     "befund": "Beurteilungsrelevante Hauterkrankung angegeben (Ekzemneigung, schwere Akne, "
               "ausgeprägte Seborrhoe, Vitiligo, Ichthyose, Porphyria cutanea tarda oder "
               "Seemanns-/Landmannshaut).",
     "konsequenz": "Ausprägung ärztlich beurteilen (Hautstatus, ggf. hautfachärztlich). Bei "
                   "geringer Ausprägung Aufnahme/Fortsetzung unter Maßnahmen nach 7.4.2 "
                   "prüfen; bei zu erwartender Änderung des Schweregrads verkürzte "
                   "Vorsorgefristen nach 7.4.3 festlegen."},
    {"wenn": {"sonnenempfindlichkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3.1, 7.4 und 8.1",
     "befund": "Empfindlichkeit der Haut gegenüber UV-Strahlen/Sonnenlicht angegeben.",
     "konsequenz": "UV-Empfindlichkeit als beurteilungsrelevant nach 7.4 werten: Maßnahmen "
                   "nach 7.4.2 bzw. verkürzte Fristen nach 7.4.3 prüfen. Beratung zur "
                   "möglichen Photosensibilisierung durch PAK, Anleitung zum Lichtschutz "
                   "und zur Selbstbeobachtung der Haut."},
    {"wenn": {"hautveraenderungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 7.2.2 (Nachuntersuchung/nachgehende Untersuchung)",
     "befund": "Neue oder veränderte Hautstellen (Warzen, Verhornungen, Flecken, schlecht "
               "heilende Stellen) angegeben.",
     "konsequenz": "Ganzkörperinspektion (einschließlich Skrotalbereich) mit besonderem "
                   "Augenmerk auf suspekte Veränderungen (Keratosen, Teer-/Pechwarzen, "
                   "Basaliome, Plattenepithelkarzinome u. a.). Bei Vorhandensein von Warzen "
                   "hautfachärztliche Untersuchung veranlassen; ggf. Fotodokumentation des "
                   "Hautbefundes zur Vergleichskontrolle."},
    {"wenn": {"haut_beschwerden": ["juckreiz", "roetung"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3.1 und 7.2.2",
     "befund": "Aktuelle Hautbeschwerden (Juckreiz, örtliche Rötungen/Entzündungen) angegeben.",
     "konsequenz": "Hautstatus gezielt erfassen: Dermatitis, Photosensibilisierung, beginnende "
                   "Hyperpigmentierung/Melanose oder Follikulitiden abklären; bei unklarem "
                   "Befund hautfachärztliche Vorstellung. Zusammenhang mit der Exposition "
                   "prüfen und Hautschutzberatung intensivieren."},
    # ── Atemwege (Abschnitte 6.3, 7.2.2, 7.4) ─────────────────────────────
    {"wenn": {"atemwegserkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien Atemwege)",
     "befund": "Chronische Erkrankung der Atemwege oder Lunge angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung die Funktion der Luftwege/Lunge wesentlich "
                   "beeinträchtigt oder bronchopulmonale Erkrankungen begünstigt: Spirometrie-"
                   "Befund gezielt bewerten, in unklaren Fällen pulmologische Abklärung. "
                   "Maßnahmen nach 7.4.2 (z. B. expositionsärmerer Einsatz, Atemschutz unter "
                   "Beachtung des Gesundheitszustands) und Fristverkürzung nach 7.4.3 erwägen."},
    {"wenn": {"atem_beschwerden": ["husten", "heiserkeit", "auswurf", "atemnot"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 7.2.2",
     "befund": "Atemwegsbeschwerden (Husten, Heiserkeit, Auswurf oder Atemnot) angegeben.",
     "konsequenz": "Anamnese vertiefen und Spirometrie gezielt auswerten; in unklaren Fällen "
                   "pulmologische Abklärung veranlassen. Bei Auffälligkeiten besteht die "
                   "rechtfertigende Indikation für bildgebende Diagnostik des Thorax "
                   "(insbesondere im Rahmen der nachgehenden Vorsorge)."},
    # ── Harnwege (Abschnitte 6.3, 6.5, 7.2.2, 7.4) ────────────────────────
    {"wenn": {"blut_urin": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Harnwege",
     "quelle": "Abschnitte 6.3.1 (Harnwege), 6.5 (BK-Nr. 1321) und 7.2.2",
     "befund": "Blut im Urin (Hämaturie) angegeben.",
     "konsequenz": "Urinstatus mit Mehrfachteststreifen, Sediment und Urinzytologie "
                   "durchführen; zeitnahe urologische Abklärung veranlassen (PAK können "
                   "Schleimhautveränderungen, Krebs oder andere Neubildungen der Harnwege "
                   "verursachen, BK-Nr. 1321). Bei begründetem Verdacht BK-Anzeige prüfen."},
    {"wenn": {"wasserlassen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Harnwege",
     "quelle": "Abschnitte 7.1 (Beschwerden Harnwege) und 7.2.2",
     "befund": "Vermehrtes oder schmerzhaftes Wasserlassen angegeben.",
     "konsequenz": "Urinstatus (Mehrfachteststreifen, Sediment, bei Nachuntersuchung "
                   "zusätzlich Zytologie) gezielt auswerten; bei auffälligem oder unklarem "
                   "Befund urologische Abklärung veranlassen."},
    {"wenn": {"harnwegserkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Harnwege",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien Harnwege), 7.4.2–7.4.4",
     "befund": "Chronische Erkrankung der Blase/Harnwege bzw. Neubildung angegeben.",
     "konsequenz": "Urologische Vorbefunde einholen, Urinstatus einschließlich Zytologie. "
                   "Prüfen, ob die Tätigkeit ohne gesundheitliche Gefährdung möglich ist: "
                   "Maßnahmen nach 7.4.2, verkürzte Fristen nach 7.4.3; bei fehlender "
                   "Erfolgsaussicht Tätigkeitswechsel nach 7.4.4 erwägen."},
    # ── Schutzmaßnahmen und Hygiene (Abschnitte 6.2, 8.1, 8.2) ────────────
    {"wenn": {"psa": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitt 8.2 und § 6 (4) ArbMedVV",
     "befund": "Keine persönliche Schutzausrüstung bei Tätigkeiten mit PAK angegeben.",
     "konsequenz": "Anhaltspunkt für unzureichende Arbeitsschutzmaßnahmen: dem Unternehmer "
                   "bzw. der Unternehmerin mitteilen und Schutzmaßnahmen vorschlagen "
                   "(§ 6 (4) ArbMedVV; TRGS 551 bzw. TRGS 524). Beschäftigte Person zu "
                   "geeigneten Schutzhandschuhen, Hautschutz und Arbeitskleidungswechsel "
                   "beraten."},
    {"wenn": {"hygiene": ["teilweise", "nein"]},
     "schwere": "pruefen",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 6.2, 7.1 (Hygieneregime) und 8.1",
     "befund": "Hygieneregeln am Arbeitsplatz werden nur teilweise oder nicht eingehalten.",
     "konsequenz": "Beratung zu Hygienemaßnahmen und persönlicher Arbeitshygiene (Vermeidung "
                   "der Verschleppung PAK-haltiger Gefahrstoffe, keine Aufnahme über den "
                   "Magen-Darm-Trakt). Ursachen klären; ergeben sich Anhaltspunkte für "
                   "unzureichende betriebliche Hygieneorganisation, Mitteilung an das "
                   "Unternehmen nach § 6 (4) ArbMedVV."},
    {"wenn": {"psa_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 7.4.2 und 8.1",
     "befund": "Gesundheitliche Probleme mit der persönlichen Schutzausrüstung angegeben.",
     "konsequenz": "Persönliche Schutzausrüstung unter Beachtung des individuellen "
                   "Gesundheitszustands anpassen (7.4.2); geeignete Handschuh- und "
                   "Hautschutzauswahl beraten, ggf. Rückmeldung an das Unternehmen."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitt 6 (TRGS 401) und Abschnitt 2 (Pflichtvorsorge)",
     "befund": "Direkter Hautkontakt mit PAK-haltigen Produkten oder deren Dämpfen angegeben.",
     "konsequenz": "Beratung: PAK sind hautresorptiv; schon kleinflächiger, kurzfristiger "
                   "Kontakt kann eine hohe Gefährdung im Sinn der TRGS 401 bedeuten. Mit der "
                   "Gefährdungsbeurteilung abgleichen und prüfen, ob Pflichtvorsorge "
                   "veranlasst ist; konsequente Hautschutzmaßnahmen und Handschuhbenutzung "
                   "vermitteln."},
    # ── Besondere Expositionen (Abschnitte 6.4, 7.1) ──────────────────────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "Abschnitte 6.4 und 7.1 (Zwischenfälle, ungewöhnliche Betriebszustände)",
     "befund": "Zwischenfall, Unfall oder ungewöhnlicher Betriebszustand mit erhöhter "
               "PAK-Exposition angegeben.",
     "konsequenz": "Ereignis dokumentieren; Biomonitoring (1-Hydroxypyren im Urin, "
                   "Probennahme am Schichtende) zur Objektivierung der inneren Belastung "
                   "durchführen (§ 6 (2) ArbMedVV, BAR 0,3 µg/g Kreatinin für Nichtrauchende). "
                   "Abgleich mit der Gefährdungsbeurteilung; ggf. Mitteilung an das "
                   "Unternehmen nach § 6 (4) ArbMedVV."},
    {"wenn": {"rauchen": ["taeglich", "gelegentlich"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring/Rauchen",
     "quelle": "Abschnitte 6.4 (BAR für Nichtrauchende) und 7.1 (Rauchverhalten)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Bei der Bewertung des Biomonitorings berücksichtigen: Der BAR-Wert für "
                   "1-Hydroxypyren (0,3 µg/g Kreatinin) ist für Nichtrauchende abgeleitet; "
                   "Tabakrauch erhöht die PAK-Belastung zusätzlich. Beratung zum Rauchverzicht "
                   "wegen des kombinierten Krebsrisikos anbieten."},
    {"wenn": {"frueher_exposition": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 2 (nachgehende Vorsorge), 6.5 und 7.1 (Arbeitsanamnese)",
     "befund": "Frühere Tätigkeiten mit PAK- oder anderer Karzinogen-Exposition angegeben.",
     "konsequenz": "Frühere Expositionszeiten und -umstände dokumentieren (relevant für die "
                   "kumulative BaP-Dosis, BK-Nrn. 1321 und 4113). Prüfen, ob eine Anmeldung "
                   "zur nachgehenden Vorsorge über das Meldeportal »DGUV Vorsorge« "
                   "(www.dguv-vorsorge.de) erfolgt ist bzw. nachzuholen ist."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 6.5 und 7.1 (laufendes BK-Verfahren)",
     "befund": "Laufendes oder abgeschlossenes Berufskrankheiten-Verfahren angegeben.",
     "konsequenz": "BK-Verfahren und zugrunde liegende Diagnosen dokumentieren, Vorbefunde "
                   "einbeziehen; Erkenntnisse bei Beurteilung (7.4) und Festlegung der "
                   "Vorsorgeinhalte berücksichtigen."},
    {"wenn": {"vorsorge_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2 und 7.2.2 (Nachgehende Untersuchung)",
     "befund": "Termin im Rahmen der nachgehenden Vorsorge (nach Ende der Tätigkeit).",
     "konsequenz": "Programm der nachgehenden Untersuchung anwenden: Urinstatus "
                   "(Mehrfachteststreifen, Sediment, Zytologie), spezielle Anamnese zu "
                   "Hautveränderungen/Sonnenlichtempfindlichkeit, Ganzkörperinspektion; "
                   "bildgebende Diagnostik des Thorax und Spirometrie nur bei Auffälligkeiten "
                   "(rechtfertigende Indikation). Registrierung im Meldeportal »DGUV Vorsorge« "
                   "(www.dguv-vorsorge.de) sicherstellen."},
]
