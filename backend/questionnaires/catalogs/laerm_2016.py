# -*- coding: utf-8 -*-
"""G 20 Lärm – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für arbeitsmedizinische
Untersuchungen, 7. Auflage 2016 (Gentner Verlag), G 20 »Lärm«
(Fassung Oktober 2014), S. 321–339."""

SLUG = "g20-laerm-2016"

CATALOG = {
    "version": 2,
    "title": "G 20 Lärm (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 7. Auflage 2016, "
             "G 20 »Lärm« (Fassung Oktober 2014), S. 321–339",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Untersuchungsanlass",
            "subtitle": "Angaben zu Ihrer G-20-Untersuchung",
            "questions": [
                {
                    "id": "untersuchungsart",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich?",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der lauten Tätigkeit)"},
                        {"value": "nach_erste", "label": "Erste Nachuntersuchung"},
                        {"value": "nach_weitere", "label": "Weitere Nachuntersuchung"},
                    ],
                },
                {
                    "id": "letzte_g20",
                    "type": "choice",
                    "label": "Wie lange liegt Ihre letzte G-20-Untersuchung (Hörtest) zurück?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach_erste", "nach_weitere"]},
                    "options": [
                        {"value": "unter12", "label": "Weniger als 12 Monate"},
                        {"value": "12bis36", "label": "12 bis 36 Monate"},
                        {"value": "36bis60", "label": "36 bis 60 Monate"},
                        {"value": "ueber60", "label": "Mehr als 60 Monate"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "laermpegel",
                    "type": "choice",
                    "label": "Wie laut ist es an Ihrem Arbeitsplatz?",
                    "hint": "Lärmbereich: ab ca. 85 dB(A) Tages-Lärmpegel – man kann sich auch aus "
                            "der Nähe nur noch mit lauter Stimme verständigen. Ihr Betrieb kann "
                            "Ihnen die Messwerte nennen.",
                    "required": True,
                    "options": [
                        {"value": "ab90", "label": "Sehr laut – man muss rufen (ca. 90 dB(A) oder mehr)"},
                        {"value": "85bis89", "label": "Laut – Lärmbereich mit Gehörschutz (ca. 85–89 dB(A))"},
                        {"value": "unter85", "label": "Weniger laut oder unbekannt"},
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
                        {"value": "druckluft", "label": "Druckluftwerkzeuge oder -maschinen"},
                        {"value": "metall", "label": "Metallbearbeitung (Schleifen, Schweißen, Hämmern, Pressen)"},
                        {"value": "holz_saegen", "label": "Sägen oder Holzbearbeitung"},
                        {"value": "bau", "label": "Baustellenmaschinen und -geräte"},
                        {"value": "textil", "label": "Web-, Spinn- oder Abfüllmaschinen"},
                        {"value": "knall", "label": "Knalle oder Schläge (z. B. Bolzensetzer, Schüsse)"},
                        {"value": "maschinen_sonstige", "label": "Andere laute Maschinen oder Anlagen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
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
            ],
        },
        # ── 3 ─ Gehörschutz ────────────────────────────────────────────────
        {
            "id": "gehoerschutz",
            "title": "Gehörschutz",
            "subtitle": "Ihr Gehörschutz am Arbeitsplatz",
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
                    "id": "gs_mitgebracht",
                    "type": "yes_no",
                    "label": "Haben Sie Ihren eigenen Gehörschützer heute zur Untersuchung "
                             "mitgebracht?",
                    "hint": "Der Grundsatz G 20 empfiehlt, den eigenen Gehörschützer zur "
                            "Untersuchung mitzubringen, damit Sitz und Schalldämmung individuell "
                            "beurteilt werden können.",
                    "required": True,
                    "show_if": {"id": "gs_tragen", "not_in": ["kein_laermbereich"]},
                },
                {
                    "id": "gs_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme mit Ihrem Gehörschutz (z. B. Druckstellen, "
                             "Juckreiz, schlechter Sitz, stört mit Brille oder Helm)?",
                    "required": True,
                    "show_if": {"id": "gs_tragen", "not_in": ["kein_laermbereich"]},
                    "followup": {"id": "gs_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
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
                                 "label": "Seit wann, und auf welchem Ohr?", "when": "yes"},
                },
                {
                    "id": "verschlechterung",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Hörvermögen seit der letzten G-20-Untersuchung spürbar "
                             "verschlechtert?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach_erste", "nach_weitere"]},
                },
                {
                    "id": "ohrgeraeusche",
                    "type": "yes_no",
                    "label": "Haben Sie Ohrgeräusche wie Pfeifen, Rauschen oder Summen (Tinnitus)?",
                    "required": True,
                    "followup": {"id": "ohrgeraeusche_desc", "type": "text",
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
                    "id": "meniere",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Menière-Krankheit oder eine andere "
                             "Gleichgewichts-Erkrankung des Innenohrs (vestibuläre "
                             "Schwindelerkrankung) festgestellt?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen der Ohren",
            "subtitle": "Frühere Erkrankungen, Operationen und Verletzungen",
            "questions": [
                {
                    "id": "hoersturz",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal einen Hörsturz (plötzlicher Hörverlust auf "
                             "einem Ohr)?",
                    "required": True,
                },
                {
                    "id": "ohr_op",
                    "type": "yes_no",
                    "label": "Wurden Sie schon einmal am Mittelohr oder Innenohr operiert?",
                    "required": True,
                    "followup": {"id": "ohr_op_desc", "type": "text",
                                 "label": "Welche Operation, und wann?", "when": "yes"},
                },
                {
                    "id": "otosklerose_op",
                    "type": "yes_no",
                    "label": "Wurden Sie wegen einer Otosklerose operiert (Versteifung der "
                             "Gehörknöchelchen im Mittelohr)?",
                    "required": True,
                },
                {
                    "id": "schaedeltrauma",
                    "type": "yes_no",
                    "label": "Hatten Sie eine Schädelverletzung (z. B. Schädelbruch, schweres "
                             "Schädel-Hirn-Trauma), nach der sich Ihr Hörvermögen verschlechtert "
                             "hat?",
                    "required": True,
                },
                {
                    "id": "gehoergang_ekzem",
                    "type": "yes_no",
                    "label": "Haben Sie ein dauerhaftes, schwer behandelbares Ekzem (nässenden "
                             "Ausschlag) im Gehörgang, ständigen Ausfluss aus dem Ohr oder "
                             "wiederkehrende Entzündungen an der Ohrmuschel?",
                    "required": True,
                },
                {
                    "id": "akute_entzuendung",
                    "type": "yes_no",
                    "label": "Haben Sie zurzeit eine akute Entzündung am Gehörgang oder an der "
                             "Ohrmuschel?",
                    "required": True,
                },
                {
                    "id": "mittelohrentzuendungen",
                    "type": "yes_no",
                    "label": "Hatten Sie wiederholt Mittelohrentzündungen?",
                    "required": True,
                },
                {
                    "id": "gehoerlos",
                    "type": "choice",
                    "label": "Sind Sie auf einem oder beiden Ohren gehörlos (praktisch ohne "
                             "Hörvermögen)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "einseitig", "label": "Ja, auf einem Ohr"},
                        {"value": "beidseitig", "label": "Ja, auf beiden Ohren"},
                    ],
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
                    "id": "laerm_30min",
                    "type": "yes_no",
                    "label": "Waren Sie in der letzten halben Stunde vor dieser Untersuchung "
                             "starkem Lärm ausgesetzt (z. B. laute Maschinen ohne Gehörschutz)?",
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
    # ── Dauernde gesundheitliche Bedenken (Abschnitt 2.1.1) ───────────────
    {"wenn": {"meniere": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Innenohr-Erkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Vestibuläre Schwindelerkrankung (Morbus Menière) angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken sind zu prüfen – nach dem Grundsatz auch "
                   "ohne Überschreitung der Hörverlustgrenzwerte (Tabelle 1/2). HNO-Befunde "
                   "beiziehen; keine Aufnahme/Fortsetzung der Lärmtätigkeit vor ärztlicher "
                   "Klärung."},
    {"wenn": {"hoersturz": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Innenohr-Erkrankung",
     "quelle": "Abschnitte 2.1.1 und 1.2.2",
     "befund": "Hörsturz in der Vorgeschichte angegeben.",
     "konsequenz": "Vorerkrankung des Innenohrs: dauernde gesundheitliche Bedenken sind auch "
                   "ohne Grenzwertüberschreitung zu prüfen. Ergänzungsuntersuchung Lärm II "
                   "durchführen (Otoskopie, WEBER-Test, Luft- und Knochenleitung); Klärung vor "
                   "Einsatz im Lärmbereich."},
    {"wenn": {"otosklerose_op": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Ohr-Operation",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Zustand nach Otosklerose-Operation angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken sind zu prüfen – auch ohne Überschreitung "
                   "der Hörverlustgrenzwerte. OP-Berichte/HNO-Befunde einholen; Klärung vor "
                   "Aufnahme bzw. Fortsetzung der Lärmtätigkeit."},
    {"wenn": {"gehoergang_ekzem": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Äußeres Ohr / Gehörschutz",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Therapieresistentes Gehörgangsekzem, Sekretion aus dem Mittelohr oder "
               "entzündliche Hautreaktionen an der Ohrmuschel angegeben.",
     "konsequenz": "Hautbefund erheben: machen die Veränderungen die Benutzung von "
                   "Gehörschützern dauerhaft unmöglich, sind dauernde gesundheitliche Bedenken "
                   "auszusprechen. Alternativ dermatologische/HNO-ärztliche Behandlung und "
                   "andere Gehörschutzform prüfen."},
    # ── Befristete gesundheitliche Bedenken (Abschnitt 2.1.2) ─────────────
    {"wenn": {"akute_entzuendung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Äußeres Ohr / Gehörschutz",
     "quelle": "Abschnitt 2.1.2 (Befristete gesundheitliche Bedenken)",
     "befund": "Akute Entzündung des Gehörgangs oder der Ohrmuschel angegeben.",
     "konsequenz": "Befristete gesundheitliche Bedenken: solange die Entzündung das Benutzen "
                   "von Gehörschützern nicht möglich macht, keine Tätigkeit im Lärmbereich. "
                   "Behandlung veranlassen, Nachuntersuchung nach Abheilung."},
    # ── Anhaltspunkte für Ergänzungsuntersuchung Lärm II (Abschnitt 1.2.2) ─
    {"wenn": {"ohr_op": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ohr-Operation",
     "quelle": "Abschnitt 1.2.2 (Ergänzungsuntersuchung)",
     "befund": "Operation am Mittel- und/oder Innenohr angegeben.",
     "konsequenz": "Ergänzungsuntersuchung Lärm II erforderlich: ärztliche Anamnese, Otoskopie, "
                   "WEBER-Test, Hörtest in Luftleitung (0,5–8 kHz) und Knochenleitung."},
    {"wenn": {"schwindel_mit_ohr": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitt 1.2.2 (Ergänzungsuntersuchung)",
     "befund": "Hörstörungen oder Ohrgeräusche in Verbindung mit Schwindelanfällen angegeben.",
     "konsequenz": "Ergänzungsuntersuchung Lärm II erforderlich; bei unklarem Befund ggf. "
                   "Impedanzmessungen bzw. HNO-ärztliche Abklärung (Abschnitt 1.2.3.1) "
                   "veranlassen."},
    {"wenn": {"schaedeltrauma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Trauma",
     "quelle": "Abschnitte 2.1.1 und 1.2.2",
     "befund": "Schädelverletzung mit anschließender Hörverschlechterung angegeben.",
     "konsequenz": "Innenohr-/Hörnervenschwerhörigkeit als Traumafolge abklären: "
                   "Ergänzungsuntersuchung Lärm II, Vergleich mit Voraudiogrammen. Bei "
                   "überschrittenen Grenzwerten (Tabelle 1) oder sekundärer Zunahme der "
                   "Schwerhörigkeit nach dem Unfall sind dauernde gesundheitliche Bedenken zu "
                   "prüfen."},
    {"wenn": {"mittelohrentzuendungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Ohr-Vorerkrankung",
     "quelle": "Abschnitte 1.2.2 und 2.1.1",
     "befund": "Wiederholte Mittelohrentzündungen angegeben.",
     "konsequenz": "Otoskopische Abklärung im Siebtest; auf Schallleitungsstörung achten "
                   "(Differenz Luft-/Knochenleitung ≥ 15 dB bei ≥ 2 Frequenzen, Abschnitt 3.4.5). "
                   "Bei anhaltender Sekretion aus dem Mittelohr Kriterien nach 2.1.1 prüfen."},
    {"wenn": {"hoerminderung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hörvermögen",
     "quelle": "Abschnitte 1.2.1 und 1.2.2",
     "befund": "Subjektive Hörminderung angegeben.",
     "konsequenz": "Siebtest Lärm I sorgfältig durchführen (Tonaudiometrie Luftleitung 1–6 kHz). "
                   "Bei Überschreitung der Hörverlustgrenzwerte nach Tabelle 1/2 oder 40 dB bei "
                   "2 kHz Ergänzungsuntersuchung Lärm II veranlassen."},
    {"wenn": {"verschlechterung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hörvermögen",
     "quelle": "Abschnitte 1.2.2 und 2.1.3",
     "befund": "Subjektive Hörverschlechterung seit der letzten Untersuchung.",
     "konsequenz": "Vergleich mit dem letzten Audiogramm: bei Zunahme der Hörverlustsumme "
                   "(2, 3, 4 kHz) um mehr als 30 dB innerhalb von höchstens 3 Jahren "
                   "Ergänzungsuntersuchung Lärm II. Ggf. Auflagen nach 2.1.3: verkürzte "
                   "Nachuntersuchungsfrist (vorzugsweise 12 oder 24 Monate), speziell "
                   "ausgewählte Gehörschützer, Kontrolle der Benutzung."},
    {"wenn": {"ohrgeraeusche": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 1.1 und 2.2",
     "befund": "Ohrgeräusche (Tinnitus) angegeben.",
     "konsequenz": "Beratung zu Ursachen, Auswirkungen und Behandlung von Tinnitus. Bei neu "
                   "aufgetretenen Ohrgeräuschen ist eine vorzeitige Nachuntersuchung nach "
                   "Abschnitt 1.1 angezeigt."},
    # ── Anwendungsbereich (Vorbemerkungen) ────────────────────────────────
    {"wenn": {"gehoerlos": ["beidseitig"]},
     "schwere": "pruefen",
     "bereich": "Anwendungsbereich G 20",
     "quelle": "Vorbemerkungen",
     "befund": "Beidseitige Gehörlosigkeit angegeben.",
     "konsequenz": "Der Grundsatz G 20 findet bei fehlenden nutzbaren Hörresten keine Anwendung. "
                   "Beschäftigung im Lärmbereich ist möglich, sofern kein erhöhtes Unfallrisiko "
                   "besteht – Vorgehen nach dem »Leitfaden für Betriebsärzte zur Beschäftigung "
                   "von Schwerhörigen und Gehörlosen in Lärmbereichen« (DGUV); Unfallrisiko am "
                   "Arbeitsplatz klären."},
    # ── Gehörschutz (Abschnitte 2.1.3 und 2.2) ────────────────────────────
    {"wenn": {"gs_tragen": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Gehörschutz",
     "quelle": "Abschnitte 2.1.3 und 2.2",
     "befund": "Gehörschutz wird bei lauter Arbeit selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zur Benutzung von Gehörschützern (DGUV Regel 112-194); "
                   "Ursachen klären, geeigneten Gehörschutz auswählen. Besondere Kontrolle der "
                   "Benutzung am Arbeitsplatz; bei Gefährdungsschwerpunkten Arbeitgeber unter "
                   "Wahrung der Schweigepflicht hinweisen und beraten."},
    {"wenn": {"gs_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Gehörschutz",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Probleme mit dem Gehörschutz (Sitz, Komfort, Kombination mit Brille/PSA).",
     "konsequenz": "Individuelle Gehörschutzberatung: geeigneten Typ auswählen, passende "
                   "Schalldämmung (keine Über-/Unterprotektion), Hörbarkeit von Warnsignalen "
                   "und Kombination mit Brille oder anderer PSA berücksichtigen "
                   "(DGUV Information 212-823)."},
    # ── Untersuchungstag (Abschnitt 3.4.3) ────────────────────────────────
    {"wenn": {"laerm_14h": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Durchführung Audiometrie",
     "quelle": "Abschnitt 3.4.3 (Zeitpunkt der Untersuchung)",
     "befund": "In den letzten 14 Stunden Schalleinwirkung ≥ 80 dB ohne durchgehenden Gehörschutz.",
     "konsequenz": "Gefahr einer vorübergehenden Hörschwellenverschiebung (TTS): Audiometrie "
                   "möglichst verschieben oder Ergebnis nur unter Vorbehalt werten."},
    {"wenn": {"laerm_30min": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Durchführung Audiometrie",
     "quelle": "Abschnitt 3.4.3 (Zeitpunkt der Untersuchung)",
     "befund": "Starke Lärmeinwirkung unmittelbar (unter 30 Minuten) vor der Untersuchung.",
     "konsequenz": "Die audiometrische Untersuchung soll nicht durchgeführt werden, wenn nach "
                   "Lärmeinwirkung ≥ 85 dB(A) die Gehörerholungszeit (Lärmpause < 75 dB(A)) "
                   "30 Minuten unterschreitet: Lärmpause abwarten oder Termin verschieben."},
    # ── Fristen (Abschnitt 1.1) ───────────────────────────────────────────
    {"wenn": {"untersuchungsart": ["erst"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Erstuntersuchung vor Aufnahme der Tätigkeit.",
     "konsequenz": "Erste Nachuntersuchung nach 12 Monaten einplanen; weitere Nachuntersuchungen "
                   "nach 36 Monaten (bzw. nach 60 Monaten bei Tages-Lärmexpositionspegeln unter "
                   "90 dB(A)); außerdem Nachuntersuchung bei Beendigung der Tätigkeit."},
    {"wenn": {"letzte_g20": ["ueber60"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Letzte G-20-Untersuchung liegt mehr als 60 Monate zurück.",
     "konsequenz": "Auch die längste Nachuntersuchungsfrist (60 Monate) ist überschritten: "
                   "Untersuchung vollständig durchführen und künftige Fristen (12/36/60 Monate "
                   "je nach Exposition) neu festlegen."},
    {"wenn": {"letzte_g20": ["36bis60"], "laermpegel": ["ab90"]},
     "schwere": "hinweis",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Letzte Untersuchung über 36 Monate her bei Tages-Lärmexpositionspegel ab 90 dB(A).",
     "konsequenz": "Bei Pegeln ab 90 dB(A) gilt die 36-Monats-Frist (60 Monate nur unter "
                   "90 dB(A)): Nachuntersuchungsfrist ist überschritten, Untersuchung zeitnah "
                   "vollständig durchführen und Frist neu setzen."},
]
