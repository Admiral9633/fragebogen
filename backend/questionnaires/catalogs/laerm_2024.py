# -*- coding: utf-8 -*-
"""Lärm – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische
Beratungen und Untersuchungen, 1. Auflage 2024, Kapitel »Lärm« (E LRM,
Fassung Januar 2022), S. 924–951."""

SLUG = "laerm-2024"

CATALOG = {
    "version": 2,
    "title": "Lärm (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Lärm« (E LRM, Fassung Januar 2022), S. 924–951",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen Lärm?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Lärm-Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur Lärm-Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn am Arbeitsplatz "
                            "85 dB(A) (Tages-Lärmpegel) bzw. 137 dB(C) (Spitzenpegel) erreicht oder "
                            "überschritten werden. Angebotsvorsorge: ab 80 dB(A) bzw. 135 dB(C).",
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
        # ── 2 ─ Tätigkeit und Lärmbelastung ────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Lärmbelastung",
            "subtitle": "Ihre Arbeit und der Lärm, dem Sie ausgesetzt sind",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "laermquellen",
                    "type": "multi_choice",
                    "label": "Welche Lärmquellen gibt es an Ihrem Arbeitsplatz?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "druckluft", "label": "Druckluftwerkzeuge, -düsen oder -maschinen"},
                        {"value": "schleifen_schweissen", "label": "Schleifmaschinen oder Schweißgeräte"},
                        {"value": "haemmer_pressen", "label": "Hämmer, Pressen, Schlagschrauber oder Bolzensetzwerkzeuge"},
                        {"value": "saegen_stanzen", "label": "Sägen, Stanz- oder Nibbelmaschinen"},
                        {"value": "abfuell_textil", "label": "Abfüllmaschinen, Web- oder Spinnmaschinen"},
                        {"value": "transport", "label": "Transport mit Aufprall- oder Anschlaggeräuschen"},
                        {"value": "maschinen_sonstige", "label": "Andere laute Maschinen oder Anlagen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "impulslaerm",
                    "type": "yes_no",
                    "label": "Gibt es an Ihrem Arbeitsplatz Knalle oder sehr laute Einzelgeräusche "
                             "(Impulslärm), z. B. Schüsse, Explosionen, Schlaggeräusche?",
                    "required": True,
                },
                {
                    "id": "ultraschall",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Ultraschall-Geräten (z. B. Ultraschall-Schweißmaschinen) "
                             "oder in der Nähe großer Lüftungs- oder Verbrennungsanlagen?",
                    "hint": "Solche Anlagen können Ultraschall oder Infraschall abgeben – Schall, "
                            "den man kaum hört, der aber belasten kann.",
                    "required": True,
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt in Lärmbereichen?",
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
                    "id": "frueher_laerm",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Berufen oder Tätigkeiten Lärm ausgesetzt?",
                    "required": True,
                    "followup": {"id": "frueher_laerm_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
                {
                    "id": "freizeitlaerm",
                    "type": "yes_no",
                    "label": "Sind Sie in der Freizeit regelmäßig lautem Schall ausgesetzt "
                             "(z. B. laute Musik oder Kopfhörer, Konzerte, Schießsport, Motorrad, "
                             "laute Heimwerker-Maschinen)?",
                    "required": True,
                    "followup": {"id": "freizeitlaerm_desc", "type": "text",
                                 "label": "Was, und wie oft?", "when": "yes"},
                },
                {
                    "id": "ototox_stoffe",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Chemikalien wie Lösungsmitteln (z. B. Toluol, Styrol), "
                             "Schwermetallen oder Kohlenmonoxid?",
                    "hint": "Einige Arbeitsstoffe können das Innenohr zusätzlich belasten "
                            "(»ototoxische« = ohrschädigende Stoffe).",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Gehörschutz ────────────────────────────────────────────────
        {
            "id": "gehoerschutz",
            "title": "Gehörschutz",
            "subtitle": "Schutzmaßnahmen an Ihrem Arbeitsplatz",
            "questions": [
                {
                    "id": "gs_tragen",
                    "type": "choice",
                    "label": "Tragen Sie bei lauter Arbeit Gehörschutz (Stöpsel oder Kapseln)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_laermbereich", "label": "Ich arbeite (noch) nicht im Lärmbereich"},
                    ],
                },
                {
                    "id": "gs_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme mit Ihrem Gehörschutz (z. B. Druckstellen, Juckreiz, "
                             "schlechter Sitz, stört mit Brille oder Helm)?",
                    "required": True,
                    "show_if": {"id": "gs_tragen", "not_in": ["kein_laermbereich"]},
                    "followup": {"id": "gs_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
                {
                    "id": "kommunikation",
                    "type": "yes_no",
                    "label": "Überhören Sie bei der Arbeit Warnsignale, oder fällt es Ihnen schwer, "
                             "Kolleginnen/Kollegen oder Telefonate zu verstehen?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Hören und Beschwerden ──────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Hören & Beschwerden",
            "subtitle": "Ihr Hörvermögen und Beschwerden an den Ohren",
            "questions": [
                {
                    "id": "hoerminderung",
                    "type": "yes_no",
                    "label": "Haben Sie das Gefühl, schlechter zu hören als früher (Hörminderung)?",
                    "required": True,
                    "followup": {"id": "hoerminderung_desc", "type": "textarea",
                                 "label": "Seit wann, auf welchem Ohr, und wie wirkt es sich im "
                                          "Alltag aus (beruflich und privat)?", "when": "yes"},
                },
                {
                    "id": "verschlechterung",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Hörvermögen seit der letzten Lärm-Vorsorge spürbar "
                             "verschlechtert?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere"]},
                },
                {
                    "id": "tinnitus",
                    "type": "yes_no",
                    "label": "Haben Sie Ohrgeräusche wie Pfeifen, Rauschen oder Summen (Tinnitus)?",
                    "required": True,
                    "followup": {"id": "tinnitus_desc", "type": "text",
                                 "label": "Seit wann, dauerhaft oder zeitweise?", "when": "yes"},
                },
                {
                    "id": "schwindel_mit_ohr",
                    "type": "yes_no",
                    "label": "Treten bei Ihnen Hörprobleme oder Ohrgeräusche zusammen mit "
                             "Schwindelanfällen auf?",
                    "required": True,
                },
                {
                    "id": "ohrenschmerzen",
                    "type": "yes_no",
                    "label": "Haben Sie derzeit Ohrenschmerzen?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen der Ohren",
            "subtitle": "Frühere Erkrankungen, Verletzungen und Medikamente",
            "questions": [
                {
                    "id": "angeborene_schwerhoerigkeit",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen eine angeborene Schwerhörigkeit (Hörminderung "
                             "seit der Geburt)?",
                    "required": True,
                },
                {
                    "id": "mittelohrentzuendungen",
                    "type": "yes_no",
                    "label": "Hatten Sie entzündliche Erkrankungen der Ohren, z. B. wiederholte "
                             "Mittelohrentzündungen?",
                    "required": True,
                },
                {
                    "id": "akute_entzuendung",
                    "type": "yes_no",
                    "label": "Haben Sie zurzeit eine Entzündung, ein Ekzem (nässenden Ausschlag) "
                             "oder Ausfluss am Gehörgang oder an der Ohrmuschel?",
                    "required": True,
                },
                {
                    "id": "ohr_op",
                    "type": "yes_no",
                    "label": "Wurden Sie schon einmal am Ohr operiert (z. B. am Mittelohr oder "
                             "Innenohr)?",
                    "required": True,
                    "followup": {"id": "ohr_op_desc", "type": "text",
                                 "label": "Welche Operation, und wann?", "when": "yes"},
                },
                {
                    "id": "hoersturz",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal einen Hörsturz (plötzlicher Hörverlust auf "
                             "einem Ohr)?",
                    "required": True,
                },
                {
                    "id": "ohr_trauma",
                    "type": "yes_no",
                    "label": "Hatten Sie einen Unfall mit Verletzung des Trommelfells oder des "
                             "Schädels (z. B. Schädelbruch, Gehirnerschütterung mit Ohrbeteiligung)?",
                    "required": True,
                },
                {
                    "id": "ototox_med",
                    "type": "yes_no",
                    "label": "Nehmen oder nahmen Sie Medikamente ein, die das Gehör schädigen "
                             "können (ototoxische Medikamente)?",
                    "hint": "Dazu gehören z. B. bestimmte Antibiotika (Aminoglykoside), "
                            "Chemotherapie-Medikamente (z. B. Cisplatin), starke Entwässerungsmittel "
                            "oder dauerhaft hoch dosiertes Aspirin.",
                    "required": True,
                    "followup": {"id": "ototox_med_desc", "type": "text",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
                {
                    "id": "hoergeraet",
                    "type": "yes_no",
                    "label": "Tragen Sie ein Hörgerät?",
                    "required": True,
                },
            ],
        },
        # ── 6 ─ Vor der Hörprüfung ─────────────────────────────────────────
        {
            "id": "untersuchungstag",
            "title": "Vor der heutigen Hörprüfung",
            "subtitle": "Wichtig für ein unverfälschtes Ergebnis der Hörprüfung",
            "questions": [
                {
                    "id": "laerm_14h",
                    "type": "yes_no",
                    "label": "Waren Sie in den letzten 14 Stunden lautem Lärm ausgesetzt "
                             "(Arbeit oder Freizeit, z. B. laute Maschinen, Konzert, laute Musik) – "
                             "ohne dabei durchgehend Gehörschutz zu tragen?",
                    "hint": "Vor der Hörprüfung soll das Gehör mindestens 14 Stunden keinem "
                            "Dauerschall ab ca. 80 dB ausgesetzt gewesen sein, sonst kann das "
                            "Ergebnis vorübergehend schlechter ausfallen.",
                    "required": True,
                },
                {
                    "id": "knall_heute",
                    "type": "yes_no",
                    "label": "Gab es heute vor der Untersuchung ein Knallereignis in Ihrer Nähe "
                             "(z. B. Knall, Schuss, Explosion)?",
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
    # ── Anhaltspunkte für Ergänzungsuntersuchung Lärm II (Abschnitt 7.2.2) ─
    {"wenn": {"ohr_op": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ohr-Vorerkrankung",
     "quelle": "Abschnitt 7.2.2 (Ergänzungsuntersuchung Lärm II)",
     "befund": "Operation am Ohr (Mittel-/Innenohr) in der Vorgeschichte angegeben.",
     "konsequenz": "Ergänzungsuntersuchung Lärm II veranlassen: otoskopische Untersuchung, "
                   "WEBER-Test, Hörtest in Luft- (0,5–8 kHz) und Knochenleitung. OP-Berichte "
                   "bzw. HNO-Vorbefunde einbeziehen."},
    {"wenn": {"hoersturz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ohr-Vorerkrankung",
     "quelle": "Abschnitt 7.2.2 (Ergänzungsuntersuchung Lärm II)",
     "befund": "Hörsturz in der Vorgeschichte angegeben.",
     "konsequenz": "Ergänzungsuntersuchung Lärm II veranlassen (Otoskopie, WEBER-Test, "
                   "Tonaudiometrie in Luft- und Knochenleitung). Bei der Beurteilung nach "
                   "Abschnitt 7.4 berücksichtigen; ggf. verkürzte Vorsorgefrist nach 7.4.3."},
    {"wenn": {"schwindel_mit_ohr": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitt 7.2.2 (Ergänzungsuntersuchung Lärm II)",
     "befund": "Hörstörungen oder Ohrgeräusche in Verbindung mit Schwindelanfällen angegeben.",
     "konsequenz": "Ergänzungsuntersuchung Lärm II veranlassen; bei unklarem Befund "
                   "HNO-ärztliche Abklärung (z. B. Tympanometrie, Stapediusreflexschwelle) "
                   "empfehlen."},
    {"wenn": {"akute_entzuendung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Äußeres Ohr",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Aktuelle Entzündung/Ekzem/Sekretion am Gehörgang oder an der Ohrmuschel angegeben.",
     "konsequenz": "Otoskopische Abklärung; Ergänzungsuntersuchung Lärm II erwägen. Prüfen, ob "
                   "die Erkrankung des äußeren Ohrs die Benutzung von Gehörschutz einschränkt "
                   "(Beurteilungskriterium nach 7.4); ggf. alternative Gehörschutzform (z. B. "
                   "Kapselgehörschutz statt Stöpsel) und Behandlung veranlassen."},
    {"wenn": {"mittelohrentzuendungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ohr-Vorerkrankung",
     "quelle": "Abschnitt 7.1 (Anamnese) und 7.4",
     "befund": "Entzündliche Ohrerkrankungen (z. B. Mittelohrentzündungen) in der Vorgeschichte.",
     "konsequenz": "Otoskopische Untersuchung; auf Schallleitungsstörung achten (Differenz "
                   "Luft-/Knochenleitung ≥ 15 dB bei ≥ 2 Frequenzen). Bei Auffälligkeiten "
                   "Ergänzungsuntersuchung Lärm II."},
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"angeborene_schwerhoerigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Endogene Schwerhörigkeit",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Angeborene Schwerhörigkeit angegeben.",
     "konsequenz": "Endogene Schwerhörigkeit bei der Beurteilung berücksichtigen; Vorbefunde "
                   "einholen. Prüfen, ob Maßnahmen nach 7.4.2 (z. B. optische Warnsignale, "
                   "lärmbereichstaugliche Hörgeräte) oder verkürzte Vorsorgefristen nach 7.4.3 "
                   "(z. B. 24 oder 12 Monate) angezeigt sind."},
    {"wenn": {"ohr_trauma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Trauma",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Unfall mit Trommelfell- oder Schädelverletzung in der Vorgeschichte.",
     "konsequenz": "Traumatische Ereignisse mit möglichem Hörverlust abklären: Ergänzungs- "
                   "untersuchung Lärm II erwägen, Vergleich mit Voraudiogrammen; Beurteilung "
                   "nach Abschnitt 7.4."},
    {"wenn": {"hoerminderung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hörvermögen",
     "quelle": "Abschnitte 7.1 und 7.4",
     "befund": "Subjektive Hörminderung angegeben.",
     "konsequenz": "Dauer, zeitliche Entwicklung und Alltagsauswirkungen klären, frühere "
                   "Untersuchungsergebnisse einbeziehen. Tonaudiometrie (1–6 kHz) durchführen; "
                   "bei Überschreitung der Hörverlustgrenzwerte (Tabellen 1–3) "
                   "Ergänzungsuntersuchung Lärm II bzw. Lärm III."},
    {"wenn": {"verschlechterung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hörvermögen",
     "quelle": "Abschnitte 7.2.2 und 7.4.3",
     "befund": "Subjektive Verschlechterung des Hörvermögens seit der letzten Vorsorge.",
     "konsequenz": "Vergleich mit dem letzten Audiogramm: bei Zunahme der Hörverlustsumme "
                   "(2, 3, 4 kHz) um mehr als 30 dB innerhalb von höchstens 3 Jahren "
                   "Ergänzungsuntersuchung Lärm II. Verkürzte Vorsorgefrist (z. B. 24 oder "
                   "12 Monate) nach 7.4.3 erwägen."},
    {"wenn": {"tinnitus": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Ohrgeräusche (Tinnitus) angegeben.",
     "konsequenz": "Beratung zu Ursachen, Auswirkungen und Behandlung von Tinnitus; Dauer und "
                   "Entwicklung klären, ggf. HNO-ärztliche Abklärung empfehlen."},
    # ── Kombinationswirkungen (Abschnitt 6.4) ─────────────────────────────
    {"wenn": {"ototox_med": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ototoxische Belastung",
     "quelle": "Abschnitte 6.4 und 7.1",
     "befund": "Einnahme potenziell ototoxischer Medikamente angegeben.",
     "konsequenz": "Medikamentenanamnese ärztlich vertiefen; mögliche Kombinationswirkung mit "
                   "Lärm berücksichtigen. Engmaschigere audiometrische Kontrolle bzw. verkürzte "
                   "Vorsorgefrist erwägen; Beratung zur erschwerten Wahrnehmung von Warnsignalen."},
    {"wenn": {"ototox_stoffe": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ototoxische Belastung",
     "quelle": "Abschnitte 6.4 und 8.2",
     "befund": "Tätigkeit mit potenziell ototoxischen Arbeitsstoffen angegeben.",
     "konsequenz": "Kombinationswirkung Lärm + ototoxische Substanzen berücksichtigen "
                   "(DGUV-Positionspapier »Ototoxische Arbeitsstoffe«). Abgleich mit der "
                   "Gefährdungsbeurteilung; dem Unternehmen ggf. zusätzliche Schutzmaßnahmen "
                   "vorschlagen."},
    # ── Gehörschutz und Kommunikation ─────────────────────────────────────
    {"wenn": {"gs_tragen": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Gehörschutz",
     "quelle": "Abschnitte 7.1, 8.1 und 8.2",
     "befund": "Gehörschutz wird bei lauter Arbeit selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zu Trageverhalten und Gehörgefährdung; Ursachen der "
                   "Nichtbenutzung klären (Auswahl, Tragekomfort). Ergeben sich Anhaltspunkte, "
                   "dass Schutzmaßnahmen nicht ausreichen, Mitteilung an das Unternehmen und "
                   "Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"gs_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Gehörschutz",
     "quelle": "Abschnitt 8.1",
     "befund": "Probleme mit dem Gehörschutz (Sitz, Komfort, Kombination mit Brille/PSA).",
     "konsequenz": "Individuelle Gehörschutzberatung (DGUV Information 212-823): geeigneten "
                   "Gehörschutztyp auswählen, passende Schalldämmung (keine Über-/Unterprotektion), "
                   "Kombination mit Brille/PSA berücksichtigen; ggf. Bestimmung der individuellen "
                   "Schutzwirkung (DGUV Information 212-003)."},
    {"wenn": {"kommunikation": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kommunikation/Unfallgefahr",
     "quelle": "Abschnitte 7.1, 7.4.2 und 8.1",
     "befund": "Warnsignale werden überhört bzw. Kommunikationsprobleme bei der Arbeit.",
     "konsequenz": "Erhöhte Unfallgefahr durch Überhören von Warnsignalen beraten; Audiometrie "
                   "und Beurteilung nach 7.4. Dem Unternehmen technische/organisatorische "
                   "Maßnahmen vorschlagen (z. B. ergänzende optische Warnsignale, Abgrenzung "
                   "des Arbeitsplatzes vom Verkehrsweg)."},
    {"wenn": {"hoergeraet": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hörgerät",
     "quelle": "Abschnitte 7.4.2 und 8.1",
     "befund": "Hörgerät wird getragen.",
     "konsequenz": "Beratung zur Benutzung von Hörgeräten am Lärmarbeitsplatz: im Lärmbereich "
                   "nur geeignete, dafür zugelassene Hörgeräte verwenden; Auswahl geeigneten "
                   "Gehörschutzes für Personen mit Hörminderung (DGUV Information 212-686)."},
    # ── Untersuchungstag (Abschnitt 7.2.2, Zeitpunkt der Untersuchung) ────
    {"wenn": {"laerm_14h": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Durchführung Audiometrie",
     "quelle": "Abschnitt 7.2.2 (Zeitpunkt der Untersuchung)",
     "befund": "In den letzten 14 Stunden Schalleinwirkung ≥ 80 dB ohne durchgehenden Gehörschutz.",
     "konsequenz": "Gefahr einer vorübergehenden Hörschwellenverschiebung (TTS): Tonaudiometrie "
                   "möglichst verschieben oder sicherstellen, dass keine Hörschwellenverschiebung "
                   "vorliegt; Befund entsprechend werten."},
    {"wenn": {"knall_heute": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Durchführung Audiometrie",
     "quelle": "Abschnitt 7.2.2 (Zeitpunkt der Untersuchung)",
     "befund": "Knallereignis vor der heutigen Untersuchung angegeben.",
     "konsequenz": "Messwerte können verfälscht sein: Tonaudiometrie verschieben oder Ergebnis "
                   "nur unter Vorbehalt verwerten; bei Ohrsymptomen nach Knalltrauma zeitnahe "
                   "HNO-ärztliche Vorstellung empfehlen."},
    # ── Beratung ──────────────────────────────────────────────────────────
    {"wenn": {"freizeitlaerm": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Freizeitlärm",
     "quelle": "Abschnitte 6 und 8.1",
     "befund": "Regelmäßige Lärmbelastung in der Freizeit angegeben.",
     "konsequenz": "Beratung zu Freizeitlärm und Gehörerholung (Erholungszeit möglichst "
                   "≥ 10 Stunden bei ≤ 70 dB); auf Gehörschutz auch in der Freizeit hinweisen. "
                   "Freizeitanteil bei der Bewertung von Hörverlusten berücksichtigen."},
    {"wenn": {"ultraschall": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Ultraschall/Infraschall",
     "quelle": "Abschnitt 6 (Spezifische Hinweise)",
     "befund": "Tätigkeit mit möglicher Ultraschall-/Infraschall-Exposition angegeben.",
     "konsequenz": "Bei gesundheitlichen Beschwerden Überprüfung der Gefährdungsbeurteilung "
                   "durch speziell ausgebildete Fachkräfte anregen (Richtwerte nach VDI 2058 "
                   "Blatt 2 bzw. VDI 3766); Beschwerden dokumentieren."},
]
