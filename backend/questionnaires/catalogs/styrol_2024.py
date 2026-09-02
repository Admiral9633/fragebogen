# -*- coding: utf-8 -*-
"""Styrol – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische
Beratungen und Untersuchungen, 1. Auflage 2024, Kapitel »Styrol« (E STY,
Fassung Januar 2022), S. 634–656."""

SLUG = "styrol-2024"

CATALOG = {
    "version": 2,
    "title": "Styrol (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Styrol« (E STY, Fassung Januar 2022), S. 634–656",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen Styrol?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Styrol-Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur Styrol-Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert für Styrol (86 mg/m³ bzw. 20 ppm) nicht "
                            "eingehalten wird. Angebotsvorsorge: wenn eine Belastung nicht "
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
                        {"value": "schlauchliner", "label": "Herstellung oder Verarbeitung von GFK-Schlauchlinern "
                                                            "(Rohrsanierung)"},
                        {"value": "korrosionsschutz", "label": "Korrosionsschutz-Beschichtung "
                                                               "(Spritzauftrag in geschlossenen Räumen)"},
                        {"value": "kunststoff", "label": "Herstellung von Kunststoffformteilen, Heißschneiden "
                                                         "oder Heißpressen von Polystyrol"},
                        {"value": "beschichtung", "label": "Oberflächenbeschichtung mit Polyesterharz-Produkten "
                                                           "(UP-Harze)"},
                        {"value": "metallkleber", "label": "Arbeiten mit Metallklebern / im Metallbau"},
                        {"value": "wartung", "label": "Abbruch-, Wartungs-, Reinigungs- oder Sanierungsarbeiten, "
                                                      "Probenahme in Produktions-/Abfüllanlagen"},
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
                             "überschritten (z. B. laut Messungen oder Unterweisung)?",
                    "hint": "Arbeitsplatzgrenzwert nach TRGS 900: 86 mg/m³ (20 ppm). Bei "
                            "handwerklichem, offenem Umgang mit Harzen ist eine Überschreitung "
                            "häufig.",
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
                    "label": "Arbeiten Sie zusätzlich mit anderen Lösungsmitteln oder "
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
                             "das Konzentrieren schwer (z. B. Notizen nötig, Inhalt von Texten "
                             "schwer zu erfassen)?",
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
                        {"value": "ja_schlecht", "label": "Ja, schlecht eingestellt oder stark schwankend"},
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
        # ── 6 ─ Alkohol, Medikamente, Mutterschutz ─────────────────────────
        {
            "id": "noxen",
            "title": "Alkohol, Medikamente & Mutterschutz",
            "subtitle": "Diese Angaben sind für die Bewertung von Laborwerten und für "
                        "Ihren Schutz wichtig",
            "questions": [
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Alkohol verzögert den Abbau von Styrol im Körper und kann "
                            "Laborwerte (Biomonitoring) verfälschen.",
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
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Sind Sie schwanger, oder besteht die Möglichkeit einer "
                             "Schwangerschaft?",
                    "hint": "Styrol kann vermutlich das Kind im Mutterleib schädigen – "
                            "Ihre Angabe dient Ihrem Schutz (Mutterschutzgesetz).",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ja", "label": "Ja"},
                        {"value": "moeglich", "label": "Möglich / nicht sicher"},
                        {"value": "entfaellt", "label": "Entfällt"},
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
    # ── Mutterschutz ──────────────────────────────────────────────────────
    {"wenn": {"schwangerschaft": ["ja", "moeglich"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6.3.1 (Hinweis) und 7.1 (Erste Vorsorge, allgemeine Anamnese)",
     "befund": "Schwangerschaft angegeben bzw. nicht ausgeschlossen.",
     "konsequenz": "Styrol kann vermutlich das Kind im Mutterleib schädigen: vor "
                   "(weiterer) Tätigkeit mit Styrolexposition unverzüglich klären – "
                   "Mutterschutzgesetz beachten, mutterschutzrechtliche "
                   "Gefährdungsbeurteilung des Arbeitgebers anstoßen, Exposition bis zur "
                   "Klärung vermeiden (Umsetzung/Tätigkeitsanpassung)."},
    # ── Exposition und Biomonitoring ──────────────────────────────────────
    {"wenn": {"agw_ueberschritten": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Exposition/Biomonitoring",
     "quelle": "Abschnitte 6.4 und 7.2.2 (Hinweis)",
     "befund": "Arbeitsplatzgrenzwert für Styrol wird laut Angabe nicht eingehalten.",
     "konsequenz": "Biomonitoring in verkürzten Zeitabständen durchführen: Mandelsäure "
                   "plus Phenylglyoxylsäure im Urin (BGW 600 mg/g Kreatinin; Probenahme "
                   "am Expositions-/Schichtende, bei Langzeitexposition nach mehreren "
                   "Schichten). DGUV Information 213-081 (Merkblatt M 054) beachten; "
                   "reichen die Schutzmaßnahmen nicht aus, Mitteilung an das Unternehmen "
                   "und Maßnahmenvorschlag (§ 6 (4) ArbMedVV)."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Dermale Exposition",
     "quelle": "Abschnitte 6.2 und 7.1 (Arbeitsanamnese)",
     "befund": "Direkter Hautkontakt mit flüssigem Harz/Styrol angegeben.",
     "konsequenz": "Bei großflächigem Hautkontakt ist eine relevante Aufnahme über die "
                   "Haut nicht auszuschließen: dermale Exposition bewerten, Biomonitoring "
                   "erwägen (erfasst auch die Hautaufnahme); Beratung zu "
                   "Chemikalien-Schutzhandschuhen, Hautschutz und Hygiene; ggf. "
                   "Schutzmaßnahmen nach TRGS 401 beim Unternehmen anregen."},
    {"wenn": {"koexposition": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Mehrfachexposition",
     "quelle": "Abschnitte 6.1 und 6.3.1",
     "befund": "Zusätzliche Exposition gegenüber anderen Lösungsmitteln/Gefahrstoffen.",
     "konsequenz": "Koexpositionen (z. B. Ethylbenzol und Phenylglykol wirken ähnlich wie "
                   "Styrol) bei Beurteilung und Bewertung des Biomonitorings "
                   "berücksichtigen; Abgleich mit der Gefährdungsbeurteilung."},
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ototoxische Kombination",
     "quelle": "Abschnitt 6.1",
     "befund": "Tätigkeit mit Styrolexposition im Lärmbereich angegeben.",
     "konsequenz": "Styrol ist ototoxisch: mögliche Kombinationswirkungen mit Lärm bei "
                   "der Gehöruntersuchung nach der DGUV Empfehlung »Lärm« "
                   "berücksichtigen (DGUV-Positionspapier »Ototoxische Arbeitsstoffe«)."},
    # ── Tätigkeitsspezifische Symptome ────────────────────────────────────
    {"wenn": {"merkstoerungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Neurotoxische Symptome",
     "quelle": "Abschnitte 6.3.2/6.3.3, 7.1 und 6.6",
     "befund": "Aufmerksamkeits-, Konzentrations- bzw. Gedächtnisstörungen angegeben.",
     "konsequenz": "Tätigkeitsspezifisches Leitsymptom: Anamnese mit Fragebogen Q 18 "
                   "(bzw. PNF I/II) vertiefen und als Verlaufsbeobachtung dokumentieren; "
                   "orientierende neurologische Untersuchung inkl. Pallästhesiometrie; "
                   "zeitlichen Zusammenhang mit der Styrolexposition prüfen; in unklaren "
                   "Fällen zusätzliche fachärztliche Untersuchung (7.2.2)."},
    {"wenn": {"schwindel_benommen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Pränarkotische Symptome",
     "quelle": "Abschnitte 6.3.2 und 7.1",
     "befund": "Schwindel, Benommenheit, Übelkeit oder Trunkenheitsgefühl bei/nach der Arbeit.",
     "konsequenz": "Hinweis auf erhebliche Expositionsspitzen (Symptome ab ca. 50 ppm): "
                   "Expositionszusammenhang klären, Biomonitoring durchführen; ergeben "
                   "sich Anhaltspunkte, dass Schutzmaßnahmen nicht ausreichen, Mitteilung "
                   "an das Unternehmen und Maßnahmenvorschlag (§ 6 (4) ArbMedVV)."},
    {"wenn": {"missempfindungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Peripheres Nervensystem",
     "quelle": "Abschnitte 6.3.3, 6.5 und 7.2.2",
     "befund": "Taubheit/Pelzigkeit, Zittern oder Kraftlosigkeit angegeben.",
     "konsequenz": "Möglicher Hinweis auf Schädigung des peripheren Nervensystems "
                   "(vgl. BK-Nr. 1317): orientierende neurologische Untersuchung mit "
                   "Prüfung der Vibrationsempfindlichkeit (Pallästhesiometrie); in "
                   "unklaren Fällen fachärztlich-neurologische Untersuchung."},
    {"wenn": {"reizungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Irritative Wirkung",
     "quelle": "Abschnitte 6.3.2 und 7.1",
     "befund": "Reizungen von Augen, Nase oder Atemwegen bei der Arbeit angegeben.",
     "konsequenz": "Schleimhaut-/Atemwegsreizungen treten frühzeitig und nicht streng "
                   "dosisabhängig auf: Untersuchung mit Blick auf die irritative Wirkung, "
                   "ergänzend Spirometrie (Leitfaden »Lungenfunktionsprüfung«); "
                   "zeitlichen Zusammenhang mit der Exposition prüfen, ggf. "
                   "Maßnahmenvorschlag an das Unternehmen."},
    {"wenn": {"hautreizung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3.3 und 6.5",
     "befund": "Hautrötung, trockene/rissige oder entzündete Haut an Händen/Unterarmen.",
     "konsequenz": "Flüssiges Styrol kann bei wiederholtem Kontakt Entzündungen und "
                   "toxisch-degenerative Hautveränderungen verursachen (vgl. BK-Nr. 5101): "
                   "Hautbefund erheben, Hautschutzberatung; bei Verdacht auf "
                   "Hauterkrankung dermatologische Abklärung veranlassen."},
    {"wenn": {"beschwerden_verlauf": ["arbeitsfrei_besser"]},
     "schwere": "pruefen",
     "bereich": "Expositionszusammenhang",
     "quelle": "Abschnitt 7.1 (Hinweis) und Anlage »Q 18«",
     "befund": "Beschwerden bessern sich in arbeitsfreien Zeiten (Wochenende/Urlaub).",
     "konsequenz": "Besserung in arbeitsfreien Zeiten spricht für einen zeitlichen "
                   "Zusammenhang mit der Styrolexposition: gezielte Untersuchung "
                   "(neurologisch, Q 18-Verlauf), Biomonitoring; Schutzmaßnahmen "
                   "überprüfen und ggf. Mitteilung an das Unternehmen (§ 6 (4) ArbMedVV)."},
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"haut_haende_arme": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut-Vorerkrankung",
     "quelle": "Abschnitte 7.4 und 7.4.2–7.4.4",
     "befund": "Chronische Hauterkrankung mit Beteiligung von Händen/Armen angegeben.",
     "konsequenz": "Beurteilungsrelevant, da die Erkrankung wegen ihrer Lokalisation "
                   "durch Styrol negativ beeinflusst werden kann: prüfen, ob die "
                   "Tätigkeit ohne Gefährdung möglich ist; Maßnahmen nach 7.4.2 "
                   "(Substitution, technische/organisatorische Maßnahmen, Arbeitsplatz "
                   "mit geringerer Exposition, geeignete PSA) und verkürzte "
                   "Vorsorgefristen nach 7.4.3 erwägen; ohne Aussicht auf Erfolg "
                   "Tätigkeitswechsel erwägen (7.4.4, Mitteilung an den Arbeitgeber nur "
                   "mit Einwilligung)."},
    {"wenn": {"neuro_erkrankung": ["polyneuropathie", "anfallsleiden", "psychose"]},
     "schwere": "pruefen",
     "bereich": "Neurologisch-psychiatrische Vorerkrankung",
     "quelle": "Abschnitt 7.4",
     "befund": "Erhebliche neurologische/psychiatrische Vorerkrankung angegeben "
               "(Polyneuropathie, Anfallsleiden oder schwere psychische Erkrankung).",
     "konsequenz": "Beurteilungsrelevante Erkrankung: Vorbefunde einholen und prüfen, ob "
                   "die Tätigkeit mit dem neurotoxisch wirkenden Styrol ohne "
                   "Gefährdung möglich ist; bei weniger ausgeprägten Störungen Maßnahmen "
                   "nach 7.4.2 und verkürzte Fristen nach 7.4.3; ohne Aussicht auf "
                   "Erfolg Tätigkeitswechsel erwägen (7.4.4)."},
    {"wenn": {"diabetes": ["ja_schlecht"]},
     "schwere": "pruefen",
     "bereich": "Diabetes",
     "quelle": "Abschnitte 7.4 und 7.2.2 (ergänzendes Programm)",
     "befund": "Schlecht eingestellter bzw. stark schwankender Diabetes mellitus angegeben.",
     "konsequenz": "Beurteilungsrelevant: Blutzucker/HbA1c bestimmen (ergänzendes "
                   "Untersuchungsprogramm), Stoffwechseleinstellung über behandelnde "
                   "Ärztin/Arzt optimieren lassen; verkürzte Vorsorgefristen nach 7.4.3 "
                   "und Maßnahmen nach 7.4.2 erwägen."},
    {"wenn": {"atemwegserkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 7.4 und 7.2.2 (ergänzendes Programm)",
     "befund": "Chronisch obstruktive Atemwegserkrankung angegeben.",
     "konsequenz": "Beurteilungsrelevant (Styrol reizt die Atemwege): Spirometrie "
                   "durchführen (Leitfaden »Lungenfunktionsprüfung«); prüfen, ob die "
                   "Tätigkeit ohne Gefährdung möglich ist; Maßnahmen nach 7.4.2 bzw. "
                   "verkürzte Fristen nach 7.4.3 erwägen."},
    {"wenn": {"lebererkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 7.4, 6.3.1 und 7.2.2 (ergänzendes Programm)",
     "befund": "Lebererkrankung bzw. erhöhte Leberwerte angegeben.",
     "konsequenz": "Beurteilungsrelevant, da Styrol in der Leber metabolisiert wird: "
                   "Transaminasen bestimmen (γ-GT, ALAT/SGPT, ASAT/SGOT); Befunde der "
                   "behandelnden Ärztin/des Arztes einbeziehen; Beurteilung nach 7.4, "
                   "ggf. verkürzte Fristen (7.4.3)."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Abhängigkeitserkrankung",
     "quelle": "Abschnitt 7.4",
     "befund": "Abhängigkeit von Alkohol, Drogen oder Medikamenten angegeben "
               "(aktuell oder früher).",
     "konsequenz": "Beurteilungsrelevante Erkrankung: aktuellen Status klären "
                   "(behandelt/abstinent?), Beratungs- und Behandlungsangebote "
                   "aufzeigen; prüfen, ob die Tätigkeit ohne Gefährdung möglich ist; "
                   "Maßnahmen nach 7.4.2/7.4.3, ohne Aussicht auf Erfolg "
                   "Tätigkeitswechsel erwägen (7.4.4)."},
    # ── Schutzmaßnahmen und Beratung ──────────────────────────────────────
    {"wenn": {"psa": ["keine"]},
     "wenn_nicht": {"arbeitsverfahren": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Trotz Tätigkeit mit Styrol wird keine persönliche Schutzausrüstung benutzt.",
     "konsequenz": "Intensive Beratung zu geeigneter PSA (Atemschutz, "
                   "Chemikalien-Schutzhandschuhe) und Hygienemaßnahmen; prüfen, ob die "
                   "Maßnahmen des Arbeitsschutzes ausreichen – falls nicht, Mitteilung "
                   "an das Unternehmen und Vorschlag von Schutzmaßnahmen "
                   "(§ 6 (4) ArbMedVV, GESTIS »Sicherer Umgang«)."},
    {"wenn": {"alkohol": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 6.4 (Störfaktoren) und 8.1",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung zum stoffwirkungsverstärkenden Einfluss von Alkohol "
                   "(Ethanol hemmt die Biotransformation des Styrols; die "
                   "Mandelsäure-Ausscheidung wird schon bei tolerablen Mengen um etwa "
                   "3–4 Stunden verschoben); bei der Bewertung des Biomonitorings "
                   "berücksichtigen."},
    {"wenn": {"medikamente": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring-Störfaktoren",
     "quelle": "Abschnitt 6.4 (Störfaktoren)",
     "befund": "Regelmäßige Einnahme von Analgetika, Spasmolytika, Psychopharmaka oder "
               "Muskelrelaxantien angegeben.",
     "konsequenz": "Mögliche Störfaktoren des Biomonitorings (u. a. "
                   "Mandelsäurederivate): bei der Bewertung der Urinwerte "
                   "berücksichtigen; in begründeten Fällen Leerwert vor Beginn der "
                   "Exposition bestimmen."},
]
