# -*- coding: utf-8 -*-
"""G 45 Styrol – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 45 »Styrol«
(Fassung Oktober 2014), S. 855–868."""

SLUG = "g45-styrol-2016"

CATALOG = {
    "version": 2,
    "title": "G 45 Styrol (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 45 »Styrol« (Fassung Oktober 2014), S. 855–868",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchungs_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich heute?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit mit Styrol. "
                            "Nachuntersuchung: regelmäßig nach 24 Monaten, in bestimmten "
                            "Fällen auch vorzeitig.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich wurde schon einmal nach G 45 untersucht)"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung (z. B. Krankenhausaufenthalt, längere "
                             "Krankschreibung)?",
                    "required": True,
                    "show_if": {"id": "untersuchungs_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchungs_art", "in": ["nach"]},
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Styrol-Belastung ─────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Styrol-Belastung",
            "subtitle": "Ihre Arbeit und der Kontakt mit Styrol",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "arbeitsverfahren",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten haben Sie mit Styrol oder styrolhaltigen "
                             "Harzen zu tun?",
                    "hint": "Mehrfachauswahl möglich. Styrol steckt z. B. in ungesättigten "
                            "Polyesterharzen (UP-Harzen) und Vinylester-Harzen.",
                    "required": True,
                    "options": [
                        {"value": "gfk_laminieren", "label": "Laminieren oder Spachteln mit styrolhaltigen "
                                                            "Harzen (GFK, z. B. Boots-/Karosseriebau, "
                                                            "Behälterbau, Faserspritzen)"},
                        {"value": "saeurebau", "label": "Streichen, Spachteln oder Laminieren im Säurebau / "
                                                        "Herstellung von Polymerbeton"},
                        {"value": "korrosionsschutz", "label": "Korrosionsschutz-Beschichtung "
                                                               "(Spritzauftrag in geschlossenen Räumen)"},
                        {"value": "kunststoff", "label": "Herstellung von Kunststoffformteilen, Heißschneiden "
                                                         "oder Heißpressen von Polystyrol"},
                        {"value": "beschichtung", "label": "Oberflächenbeschichtung mit Kunstharzlacken auf "
                                                           "Polyesterharz-Basis"},
                        {"value": "metallkleber", "label": "Arbeiten mit Metallklebern / im Metallbau"},
                        {"value": "wartung", "label": "Abbruch-, Wartungs-, Reinigungs- oder Sanierungsarbeiten, "
                                                      "Probenahme in Produktions-/Abfüllanlagen"},
                        {"value": "kontaminiert", "label": "Arbeiten in kontaminierten Bereichen"},
                        {"value": "sonstige", "label": "Andere Tätigkeit mit Styrol"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt mit Styrol oder styrolhaltigen "
                             "Produkten?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis15", "label": "5 bis 15 Jahre"},
                        {"value": "ueber15", "label": "Mehr als 15 Jahre"},
                    ],
                },
                {
                    "id": "agw_ueberschritten",
                    "type": "choice",
                    "label": "Wird an Ihrem Arbeitsplatz der Styrol-Grenzwert in der Luft "
                             "(Arbeitsplatzgrenzwert) überschritten, z. B. laut Messungen "
                             "oder Unterweisung?",
                    "hint": "Bei handwerklichen Verfahren mit offenem, großflächigem Umgang "
                            "mit styrolhaltigen Harzen ist eine Überschreitung häufig.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "weiss_nicht", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit direkt mit flüssigem Harz oder "
                             "Styrol in Kontakt (z. B. Spritzer, durchnässte Handschuhe oder "
                             "Kleidung)?",
                    "required": True,
                    "followup": {"id": "hautkontakt_desc", "type": "text",
                                 "label": "An welchen Körperstellen, und wie oft?", "when": "yes"},
                },
                {
                    "id": "koexposition",
                    "type": "yes_no",
                    "label": "Arbeiten Sie zusätzlich mit anderen Lösemitteln oder "
                             "Gefahrstoffen (z. B. Ethylbenzol, Aceton, Stäuben)?",
                    "required": True,
                },
                {
                    "id": "laermbereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie in einem Lärmbereich (Gehörschutz vorgeschrieben)?",
                    "hint": "Styrol kann das Gehör zusätzlich belasten (ototoxischer = "
                            "ohrschädigender Stoff).",
                    "required": True,
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
                    "id": "psa",
                    "type": "multi_choice",
                    "label": "Welche persönliche Schutzausrüstung benutzen Sie bei Arbeiten "
                             "mit Styrol?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "atemschutz", "label": "Atemschutz (Maske mit Filter oder Gebläse)"},
                        {"value": "handschuhe", "label": "Chemikalien-Schutzhandschuhe"},
                        {"value": "brille", "label": "Schutzbrille"},
                        {"value": "kleidung", "label": "Schutzkleidung / Schutzanzug"},
                        {"value": "keine", "label": "Keine Schutzausrüstung"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme mit der Schutzausrüstung (z. B. schlechter "
                             "Sitz, Hautreizung, Atemnot unter der Maske)?",
                    "required": True,
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
                {
                    "id": "hygiene",
                    "type": "yes_no",
                    "label": "Können Sie am Arbeitsplatz die Hygieneregeln einhalten "
                             "(Hände waschen, verschmutzte Arbeitskleidung wechseln, Straßen- "
                             "und Arbeitskleidung getrennt aufbewahren)?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Bitte denken Sie an die letzten Wochen und Monate",
            "questions": [
                {
                    "id": "merkstoerungen",
                    "type": "yes_no",
                    "label": "Sind Sie in letzter Zeit auffällig vergesslich, oder fällt Ihnen "
                             "das Konzentrieren schwer (z. B. Notizen nötig, Inhalt von "
                             "Zeitungen und Büchern schwer zu erfassen)?",
                    "required": True,
                },
                {
                    "id": "muedigkeit",
                    "type": "yes_no",
                    "label": "Leiden Sie unter außergewöhnlicher Müdigkeit oder schneller "
                             "Ermüdbarkeit?",
                    "required": True,
                },
                {
                    "id": "kopfschmerzen",
                    "type": "yes_no",
                    "label": "Hatten Sie in letzter Zeit gehäuft Kopfschmerzen (mindestens "
                             "einmal pro Woche)?",
                    "required": True,
                },
                {
                    "id": "schwindel_benommen",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach der Arbeit Schwindel, Benommenheit, "
                             "Übelkeit oder ein Gefühl wie leicht betrunken?",
                    "required": True,
                },
                {
                    "id": "missempfindungen",
                    "type": "yes_no",
                    "label": "Sind Ihre Hände oder Füße taub oder pelzig, zittern Ihre Hände, "
                             "oder bemerken Sie Kraftlosigkeit in Armen oder Beinen?",
                    "required": True,
                },
                {
                    "id": "reizungen",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit gereizte, brennende oder tränende "
                             "Augen, eine gereizte Nase oder Reizhusten?",
                    "required": True,
                },
                {
                    "id": "hautreizung",
                    "type": "yes_no",
                    "label": "Haben Sie an Händen oder Unterarmen gerötete, trockene, rissige "
                             "oder entzündete Haut?",
                    "required": True,
                },
                {
                    "id": "beschwerden_verlauf",
                    "type": "choice",
                    "label": "Falls Sie solche Beschwerden haben: Bessern sie sich an "
                             "arbeitsfreien Tagen, am Wochenende oder im Urlaub?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Ich habe keine dieser Beschwerden"},
                        {"value": "arbeitsfrei_besser", "label": "Ja, in arbeitsfreien Zeiten wird es besser"},
                        {"value": "unveraendert", "label": "Nein, die Beschwerden bleiben gleich"},
                        {"value": "unklar", "label": "Kann ich nicht beurteilen"},
                    ],
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, die für die Beurteilung wichtig sind",
            "questions": [
                {
                    "id": "hauterkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine chronische (dauerhafte) Hauterkrankung, z. B. "
                             "Ekzem, Neurodermitis, Schuppenflechte oder Akne?",
                    "required": True,
                    "followup": {"id": "hauterkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "haut_haende_arme",
                    "type": "yes_no",
                    "label": "Sind dabei Ihre Hände oder Arme betroffen?",
                    "required": True,
                    "show_if": {"id": "hauterkrankung", "in": ["yes"]},
                },
                {
                    "id": "neuro_erkrankung",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Erkrankungen festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "polyneuropathie", "label": "Polyneuropathie (Nervenerkrankung mit "
                                                              "Gefühlsstörungen an Händen/Füßen)"},
                        {"value": "anfallsleiden", "label": "Epilepsie / Krampfanfälle"},
                        {"value": "psychose", "label": "Schwere psychische Erkrankung (z. B. Psychose)"},
                        {"value": "andere", "label": "Andere neurologische Erkrankung"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "diabetes",
                    "type": "choice",
                    "label": "Haben Sie Diabetes mellitus (Zuckerkrankheit)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ja_gut", "label": "Ja, gut eingestellt"},
                        {"value": "ja_schlecht", "label": "Ja, schlecht einstellbar oder stark schwankend"},
                        {"value": "ja_unklar", "label": "Ja, Einstellung kenne ich nicht"},
                    ],
                },
                {
                    "id": "atemwegserkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine chronische Atemwegserkrankung mit verengten "
                             "Bronchien (z. B. COPD, chronische Bronchitis, Asthma)?",
                    "required": True,
                },
                {
                    "id": "lebererkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Lebererkrankung, oder wurden bei Ihnen erhöhte "
                             "Leberwerte festgestellt?",
                    "required": True,
                },
                {
                    "id": "abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Drogen oder Medikamenten?",
                    "required": True,
                },
            ],
        },
        # ── 6 ─ Alkohol und Medikamente ────────────────────────────────────
        {
            "id": "noxen",
            "title": "Alkohol & Medikamente",
            "subtitle": "Diese Angaben sind für die Bewertung der Urin-Laborwerte "
                        "(Biomonitoring) wichtig",
            "questions": [
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Alkohol verzögert den Abbau von Styrol im Körper und kann "
                            "die Laborwerte des Biomonitorings verfälschen.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie oder sehr selten"},
                        {"value": "gelegentlich", "label": "Gelegentlich (z. B. am Wochenende)"},
                        {"value": "regelmaessig", "label": "Regelmäßig / fast täglich"},
                    ],
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Schmerzmittel, krampflösende Mittel, "
                             "Medikamente für die Psyche (Psychopharmaka) oder "
                             "muskelentspannende Mittel ein?",
                    "hint": "Solche Medikamente können die Urin-Laborwerte des "
                            "Biomonitorings beeinflussen.",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "text",
                                 "label": "Welche Medikamente?", "when": "yes"},
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
    # ── Bedenkenstatbestände (Abschnitt 2.1.1) ────────────────────────────
    {"wenn": {"haut_haende_arme": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Haut-Vorerkrankung",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Chronische Hauterkrankung mit Beteiligung von Händen/Armen angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken, wenn die Erkrankung "
                   "wegen ihrer Lokalisation durch Styrol negativ beeinflusst werden kann: "
                   "Hautbefund erheben, ggf. dermatologische Vorbefunde einholen. Bei "
                   "weniger ausgeprägter Erkrankung prüfen, ob nach 2.1.3 »keine Bedenken "
                   "unter bestimmten Voraussetzungen« möglich sind (technische/"
                   "organisatorische Maßnahmen, geringere Exposition, geeignete PSA, "
                   "verkürzte Nachuntersuchungsfristen); bei erwartbarer Wiederherstellung "
                   "befristete Bedenken (2.1.2)."},
    {"wenn": {"neuro_erkrankung": ["polyneuropathie", "anfallsleiden", "psychose"]},
     "schwere": "kritisch",
     "bereich": "Neurologisch-psychiatrische Vorerkrankung",
     "quelle": "Abschnitte 2.1.1–2.1.3",
     "befund": "Erhebliche neurologische/psychiatrische Vorerkrankung angegeben "
               "(Polyneuropathie, Anfallsleiden oder schwere psychische Erkrankung).",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken (Styrol wirkt "
                   "neurotoxisch): Vorbefunde einholen, Ausprägung klären. Bei weniger "
                   "ausgeprägten Störungen prüfen, ob Aufnahme/Fortsetzung der Tätigkeit "
                   "unter den Voraussetzungen nach 2.1.3 möglich ist (Schutzmaßnahmen, "
                   "verkürzte Nachuntersuchungsfristen); sonst Bedenken aussprechen."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Abhängigkeitserkrankung",
     "quelle": "Abschnitte 2.1.1 und 2.1.2",
     "befund": "Abhängigkeit von Alkohol, Drogen oder Medikamenten angegeben "
               "(aktuell oder früher).",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken: aktuellen Status "
                   "klären (behandelt/abstinent?). Ist eine Wiederherstellung zu erwarten, "
                   "befristete gesundheitliche Bedenken (2.1.2) mit erneuter Beurteilung; "
                   "Behandlungs- und Beratungsangebote aufzeigen."},
    {"wenn": {"diabetes": ["ja_schlecht"]},
     "schwere": "kritisch",
     "bereich": "Diabetes",
     "quelle": "Abschnitte 2.1.1–2.1.3 und 1.2.2 (Erwünscht: Blutzucker)",
     "befund": "Schlecht einstellbarer bzw. stark schwankender Diabetes mellitus angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken: Blutzucker bestimmen "
                   "(erwünschter Untersuchungsumfang), Befunde der behandelnden "
                   "Ärztin/des Arztes einholen. Bei besserer Einstellbarkeit befristete "
                   "Bedenken bzw. keine Bedenken unter Voraussetzungen (2.1.3) mit "
                   "verkürzten Nachuntersuchungsfristen erwägen."},
    {"wenn": {"atemwegserkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 2.1.1–2.1.3 und 1.2.2 (Erwünscht: Spirometrie)",
     "befund": "Chronisch obstruktive Atemwegserkrankung angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken (Styrol reizt "
                   "Schleimhäute und Atemwege): Spirometrie durchführen (Anhang 1, "
                   "Leitfaden »Lungenfunktionsprüfung«), Schweregrad klären. Bei weniger "
                   "ausgeprägter Erkrankung Voraussetzungen nach 2.1.3 prüfen "
                   "(Expositionsminderung, PSA, verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"lebererkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 2.1.1 und 1.2.2 (Erwünscht: Leberwerte)",
     "befund": "Lebererkrankung bzw. erhöhte Leberwerte angegeben.",
     "konsequenz": "Leberschädigungen sind Bedenkenstatbestand nach 2.1.1 – Bestimmung "
                   "der Transaminasen (γ-GT, SGPT/ALAT, SGOT/ASAT) veranlassen, Befunde "
                   "der behandelnden Ärztin/des Arztes einbeziehen; bei bestätigter "
                   "Leberschädigung gesundheitliche Bedenken erwägen, sonst Verlauf mit "
                   "verkürzten Nachuntersuchungsfristen kontrollieren."},
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungen, vorzeitig)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Konstellation für eine vorzeitige Nachuntersuchung: klären, ob die "
                   "Erkrankung Anlass zu Bedenken gegen die Fortsetzung der Tätigkeit "
                   "geben könnte; Befunde/Entlassungsberichte einholen und vollständiges "
                   "Untersuchungsprogramm nach 1.2 durchführen."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungen, vorzeitig)",
     "befund": "Die versicherte Person vermutet einen Zusammenhang zwischen Erkrankung "
               "und Tätigkeit.",
     "konsequenz": "Anspruch auf vorzeitige Nachuntersuchung: Beschwerden gezielt "
                   "abklären (spezielle Untersuchung nach 1.2.2, Biomonitoring), "
                   "zeitlichen Zusammenhang mit der Styrolexposition dokumentieren; bei "
                   "begründetem Verdacht auf eine Berufskrankheit (BK-Nr. 1303/1317) "
                   "Anzeige erstatten."},
    # ── Exposition und Biomonitoring ──────────────────────────────────────
    {"wenn": {"agw_ueberschritten": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Exposition/Biomonitoring",
     "quelle": "Abschnitte 1.2.2 und 3.1.4",
     "befund": "Arbeitsplatzgrenzwert für Styrol wird laut Angabe nicht eingehalten.",
     "konsequenz": "Biomonitoring in verkürzten Zeitabständen durchführen: Mandelsäure "
                   "plus Phenylglyoxylsäure im Urin (BGW 600 mg/g Kreatinin; Probenahme "
                   "am Expositions-/Schichtende, bei Langzeitexposition nach mehreren "
                   "Schichten; TRGS 903 beachten). Merkblatt M 054 »Styrol« heranziehen; "
                   "Hinweise zur Aktualisierung der Gefährdungsbeurteilung dem "
                   "Arbeitgeber mitteilen."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Dermale Exposition",
     "quelle": "Abschnitt 3.1.3",
     "befund": "Direkter Hautkontakt mit flüssigem Harz/Styrol angegeben.",
     "konsequenz": "Bei großflächigem Hautkontakt ist eine relevante Aufnahme über die "
                   "Haut nicht auszuschließen: dermale Exposition bewerten, Biomonitoring "
                   "erwägen (erfasst auch die Hautaufnahme); Beratung zu "
                   "Chemikalien-Schutzhandschuhen, Hautschutz und Hygiene."},
    {"wenn": {"koexposition": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Mehrfachexposition",
     "quelle": "Abschnitte 3.1.1 und 3.2.1",
     "befund": "Zusätzliche Exposition gegenüber anderen Lösemitteln/Gefahrstoffen.",
     "konsequenz": "Zusätzliche exogene Einflussfaktoren (z. B. Ethylbenzol und "
                   "Phenylglykol wirken ähnlich wie Styrol) bei Beurteilung und "
                   "Bewertung des Biomonitorings berücksichtigen; Abgleich mit der "
                   "Gefährdungsbeurteilung."},
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ototoxische Kombination",
     "quelle": "Abschnitt 3.1.1",
     "befund": "Tätigkeit mit Styrolexposition im Lärmbereich angegeben.",
     "konsequenz": "Styrol ist ototoxisch: mögliche Kombinationswirkungen mit Lärm bei "
                   "der Gehöruntersuchung nach dem DGUV Grundsatz G 20 berücksichtigen."},
    # ── Tätigkeitsspezifische Symptome (Abschnitte 1.2.2 und 3.2) ─────────
    {"wenn": {"merkstoerungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Neurotoxische Symptome",
     "quelle": "Abschnitte 1.2.2, 3.3.1/3.3.2 und 3.2",
     "befund": "Aufmerksamkeits-, Konzentrations- bzw. Gedächtnisstörungen angegeben.",
     "konsequenz": "Leitsymptom der neurotoxischen Styrolwirkung: Anamnese mit Fragebogen "
                   "Q 18 (bzw. PNF I/II) vertiefen und bei jeder Nachuntersuchung als "
                   "Verlaufsbeobachtung wiederholen; orientierende neurologische "
                   "Untersuchung; zeitlichen Zusammenhang mit der Styrolexposition "
                   "prüfen; in unklaren Fällen ergänzende fachärztliche Untersuchung "
                   "(1.2.3)."},
    {"wenn": {"schwindel_benommen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Pränarkotische Symptome",
     "quelle": "Abschnitte 1.2.2 und 3.2.2",
     "befund": "Schwindel, Benommenheit, Übelkeit oder Trunkenheitsgefühl bei/nach der Arbeit.",
     "konsequenz": "Hinweis auf erhebliche Expositionsspitzen (pränarkotische Symptome ab "
                   "ca. 50 ppm): Expositionszusammenhang klären, Biomonitoring "
                   "durchführen; Hinweise zur Aktualisierung der Gefährdungsbeurteilung "
                   "dem Arbeitgeber mitteilen (schutzwürdige Belange wahren)."},
    {"wenn": {"missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Peripheres Nervensystem",
     "quelle": "Abschnitte 1.2.2, 3.2.3 und 4",
     "befund": "Taubheit/Pelzigkeit, Zittern oder Kraftlosigkeit angegeben.",
     "konsequenz": "Möglicher Hinweis auf Schädigung des peripheren Nervensystems "
                   "(vgl. BK-Nr. 1317): orientierende neurologische Untersuchung, "
                   "ergänzend Prüfung der Vibrationsempfindung am Innenknöchel beidseits "
                   "(Pallästhesiometrie); in unklaren Fällen fachärztlich-neurologische "
                   "Ergänzungsuntersuchung (1.2.3)."},
    {"wenn": {"reizungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Irritative Wirkung",
     "quelle": "Abschnitte 1.2.2 und 3.2.2",
     "befund": "Reizungen von Augen, Nase oder Atemwegen bei der Arbeit angegeben.",
     "konsequenz": "Schleimhaut-/Atemwegsreizungen treten frühzeitig und nicht streng "
                   "dosisabhängig auf: Untersuchung mit Blick auf die irritative Wirkung, "
                   "ergänzend Spirometrie (Anhang 1, Leitfaden »Lungenfunktionsprüfung«); "
                   "zeitlichen Zusammenhang mit der Exposition prüfen."},
    {"wenn": {"hautreizung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 3.2.3",
     "befund": "Hautrötung, trockene/rissige oder entzündete Haut an Händen/Unterarmen.",
     "konsequenz": "Flüssiges Styrol kann bei wiederholtem Kontakt Entzündungen und "
                   "toxisch-degenerative Hautveränderungen verursachen: Hautbefund "
                   "erheben, Hautschutzberatung; bei Verdacht auf beginnende "
                   "Hauterkrankung dermatologische Abklärung und Beurteilung nach 2.1 "
                   "(Hände/Arme!)."},
    {"wenn": {"beschwerden_verlauf": ["arbeitsfrei_besser"]},
     "schwere": "pruefen",
     "bereich": "Expositionszusammenhang",
     "quelle": "Abschnitte 1.2.2 (Hinweis) und 7 (Anlage Q 18)",
     "befund": "Beschwerden bessern sich in arbeitsfreien Zeiten (Wochenende/Urlaub).",
     "konsequenz": "Besserung in arbeitsfreien Zeiten spricht für einen zeitlichen "
                   "Zusammenhang mit der Styrolexposition: gezielte Untersuchung "
                   "(neurologisch, Q 18-Verlauf), Biomonitoring; Verlaufsbeurteilung in "
                   "kürzeren Zeitabständen bzw. vorgezogene Nachuntersuchung erwägen."},
    # ── Störfaktoren und Beratung ─────────────────────────────────────────
    {"wenn": {"alkohol": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 2.2 und 3.1.4 (Störfaktoren)",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung zum stoffwirkungsverstärkenden Einfluss von Alkohol "
                   "(Ethanol hemmt die Biotransformation des Styrols; die "
                   "Mandelsäure-Ausscheidung wird schon bei tolerablen Mengen um etwa "
                   "3–4 Stunden verschoben); bei der Bewertung des Biomonitorings "
                   "berücksichtigen."},
    {"wenn": {"medikamente": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring-Störfaktoren",
     "quelle": "Abschnitt 3.1.4 (Störfaktoren)",
     "befund": "Regelmäßige Einnahme von Analgetika, Spasmolytika, Psychopharmaka oder "
               "Muskelrelaxantien angegeben.",
     "konsequenz": "Mögliche Störfaktoren des Biomonitorings (u. a. Mandelsäurederivate): "
                   "bei der Bewertung der Urinwerte berücksichtigen; in begründeten "
                   "Fällen Leerwert vor Beginn der Exposition bestimmen."},
]
