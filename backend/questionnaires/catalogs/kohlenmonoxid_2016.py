# -*- coding: utf-8 -*-
"""G 7 Kohlenmonoxid – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 7 »Kohlenmonoxid«
(Fassung Oktober 2014), S. 177–186."""

SLUG = "g7-kohlenmonoxid-2016"

CATALOG = {
    "version": 2,
    "title": "G 7 Kohlenmonoxid (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 7 »Kohlenmonoxid« (Fassung Oktober 2014), S. 177–186",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "unt_art",
                    "type": "choice",
                    "label": "Ist dies Ihre erste Untersuchung nach dem Grundsatz G 7 "
                             "(Kohlenmonoxid)?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit "
                            "statt, Nachuntersuchungen in der Regel nach 24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Ja, Erstuntersuchung (vor Aufnahme "
                                                   "der Tätigkeit)"},
                        {"value": "nach", "label": "Nein, Nachuntersuchung"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und CO-Belastung ─────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kohlenmonoxid-Belastung",
            "subtitle": "Ihre Arbeit und mögliche Quellen von Kohlenmonoxid (CO)",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_bereiche",
                    "type": "multi_choice",
                    "label": "Arbeiten Sie in einem der folgenden Bereiche, in denen mit "
                             "Kohlenmonoxid zu rechnen ist?",
                    "hint": "Mehrfachauswahl möglich. Kohlenmonoxid ist ein farb-, "
                            "geruch- und geschmackloses, giftiges Gas, das bei "
                            "Verbrennungen entsteht.",
                    "required": True,
                    "options": [
                        {"value": "industriegase", "label": "Arbeitsplätze mit Generator-, "
                         "Kokerei-, Gicht- oder Rauchgas (z. B. Hüttenwerk, Kokerei)"},
                        {"value": "giesserei_ofen", "label": "Gießerei oder Ofenanlagen "
                         "(Abgießen/Abkühlstrecke, Kupolofen, Koksofen, Hochofen, "
                         "gichtgasbeheizte Glühöfen)"},
                        {"value": "feuerungsbau", "label": "Feuerungs- oder Schornsteinbau, "
                         "wenn unter laufendem Betrieb gearbeitet wird"},
                        {"value": "motorabgase_raum", "label": "Motorabgase in geschlossenen "
                         "Räumen mit schlechter Lüftung (z. B. Tiefgarage, Kfz-Werkstatt)"},
                        {"value": "fluessiggas_stapler", "label": "Lagerbereiche mit "
                         "flüssiggasbetriebenen Gabelstaplern (Flurförderzeugen)"},
                        {"value": "behaelter", "label": "Arbeiten in Behältern oder engen "
                         "Räumen, in denen CO entstehen kann (z. B. flüssiggasbetriebene "
                         "Lötbrenner, Löten mit »weißer Flamme«)"},
                        {"value": "baumaschinen", "label": "Benzinmotor-Maschinen in "
                         "geschlossenen Räumen oder in Gruben/Gräben (Flügelglätter, "
                         "Verdichter, Rüttler)"},
                        {"value": "roro", "label": "Geschlossene Ladedecks auf "
                         "RoRo-Schiffen mit Fahrzeugverkehr"},
                        {"value": "sonstige", "label": "Anderer Bereich mit spürbarer "
                         "Abgas- oder Rauchgas-Belastung"},
                        {"value": "keine", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt in Bereichen mit "
                             "Kohlenmonoxid-Belastung?",
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
                    "id": "zwischenfall",
                    "type": "yes_no",
                    "label": "Gab es an Ihrem Arbeitsplatz Zwischenfälle mit "
                             "Kohlenmonoxid (z. B. CO-Alarm, starke Abgas- oder "
                             "Rauchentwicklung, Vergiftungsverdacht)?",
                    "required": True,
                    "followup": {"id": "zwischenfall_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "laermbereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie zusätzlich in Lärmbereichen (sehr laute "
                             "Arbeitsumgebung, Gehörschutz erforderlich)?",
                    "hint": "Kohlenmonoxid kann das Innenohr zusätzlich belasten "
                            "(»ototoxische«, also ohrschädigende Wirkung).",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Persönliche Schutzausrüstung an Ihrem Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie den für Ihre Tätigkeit vorgesehenen Atemschutz "
                             "bzw. die vorgesehene persönliche Schutzausrüstung (PSA)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_erforderlich", "label": "Für meine Tätigkeit ist "
                                                                 "kein Atemschutz vorgesehen"},
                    ],
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die mit Kohlenmonoxid zusammenhängen können",
            "questions": [
                {
                    "id": "beschwerden_aktuell",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach der Arbeit Beschwerden wie "
                             "Kopfschmerzen, Schwindel, Übelkeit oder ungewöhnliche "
                             "Müdigkeit?",
                    "required": True,
                },
                {
                    "id": "symptome",
                    "type": "multi_choice",
                    "label": "Welche Beschwerden sind das?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "beschwerden_aktuell", "in": ["yes"]},
                    "options": [
                        {"value": "kopfschmerzen", "label": "Kopfschmerzen"},
                        {"value": "schwindel", "label": "Schwindel"},
                        {"value": "uebelkeit", "label": "Übelkeit oder Brechreiz"},
                        {"value": "mattigkeit", "label": "Allgemeine Mattigkeit oder "
                                                         "schnelle Ermüdbarkeit"},
                        {"value": "reizbarkeit", "label": "Ungewöhnliche Reizbarkeit"},
                        {"value": "schlaflosigkeit", "label": "Schlaflosigkeit oder "
                                                              "Schlafstörungen"},
                        {"value": "gedaechtnis", "label": "Nachlassendes Gedächtnis oder "
                                                          "Konzentrationsprobleme"},
                        {"value": "sonstige", "label": "Andere Beschwerden"},
                    ],
                },
                {
                    "id": "herz_symptome",
                    "type": "yes_no",
                    "label": "Haben Sie Herzbeschwerden wie Herzklopfen, Herzrasen, "
                             "Engegefühl in der Brust oder Luftnot bei Anstrengung?",
                    "required": True,
                    "followup": {"id": "herz_symptome_desc", "type": "text",
                                 "label": "Welche Beschwerden, und seit wann?",
                                 "when": "yes"},
                },
                {
                    "id": "co_vergiftung",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal eine Kohlenmonoxid-Vergiftung oder "
                             "den Verdacht darauf (z. B. mit Bewusstlosigkeit, ärztlicher "
                             "Behandlung)?",
                    "required": True,
                    "followup": {"id": "co_vergiftung_desc", "type": "textarea",
                                 "label": "Wann war das, und wie wurde es behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen Ihren Beschwerden "
                             "und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "beschwerden_aktuell", "in": ["yes"]},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "gesundheit",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, die bei Kohlenmonoxid-Belastung wichtig sind",
            "questions": [
                {
                    "id": "vorerkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Erkrankungen "
                             "festgestellt?",
                    "hint": "Mehrfachauswahl möglich. Kohlenmonoxid verringert den "
                            "Sauerstofftransport im Blut – diese Erkrankungen können "
                            "sich dadurch verschlimmern.",
                    "required": True,
                    "options": [
                        {"value": "herz", "label": "Herzerkrankung (z. B. koronare "
                         "Herzkrankheit, Herzschwäche, Herzrhythmusstörungen)"},
                        {"value": "gefaesse", "label": "Gefäßerkrankung / ausgeprägte "
                         "Arterienverkalkung (Arteriosklerose)"},
                        {"value": "lunge", "label": "Lungenerkrankung (z. B. Asthma, COPD)"},
                        {"value": "schilddruese", "label": "Schilddrüsenüberfunktion "
                         "(Hyperthyreose)"},
                        {"value": "anaemie", "label": "Blutarmut (Anämie)"},
                        {"value": "zns", "label": "Erkrankung des Gehirns oder "
                         "Nervensystems (z. B. Epilepsie, Folgen eines Schlaganfalls)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung (z. B. Krankenhausaufenthalt, längere "
                             "Krankschreibung)?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Sind Sie zurzeit schwanger, oder stillen Sie?",
                    "hint": "Kohlenmonoxid kann das ungeborene Kind schädigen. Diese "
                            "Angabe ist deshalb für Ihren Schutz besonders wichtig.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unsicher", "label": "Bin mir nicht sicher"},
                        {"value": "nicht_zutreffend", "label": "Trifft auf mich nicht zu"},
                    ],
                },
                {
                    "id": "sonstige_erkrankungen",
                    "type": "textarea",
                    "label": "Gibt es weitere Erkrankungen oder gesundheitliche "
                             "Einschränkungen, die wir kennen sollten?",
                    "required": False,
                },
            ],
        },
        # ── 6 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchgewohnheiten",
            "subtitle": "Rauchen erhöht die Kohlenmonoxid-Belastung zusätzlich",
            "questions": [
                {
                    "id": "raucher_status",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Auch durch Rauchen wird Kohlenmonoxid aufgenommen. Bei "
                            "Rauchern kann der CO-Gehalt im Blut deutlich erhöht sein – "
                            "das ist für die Blutuntersuchung (Biomonitoring) wichtig.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, nie geraucht"},
                        {"value": "frueher", "label": "Früher geraucht, jetzt nicht mehr"},
                        {"value": "gelegentlich", "label": "Ja, gelegentlich"},
                        {"value": "taeglich", "label": "Ja, täglich"},
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
                    "label": "Ich bestätige, dass meine Angaben vollständig und "
                             "wahrheitsgemäß sind.",
                    "error": "Bitte bestätigen Sie die Vollständigkeit Ihrer Angaben.",
                    "required": True,
                },
                {
                    "id": "consent_privacy",
                    "type": "consent",
                    "label": "Ich habe die Datenschutzhinweise gelesen und willige in die "
                             "Verarbeitung meiner Daten zu arbeitsmedizinischen Zwecken ein.",
                    "error": "Bitte akzeptieren Sie die Datenschutzhinweise.",
                    "required": True,
                },
            ],
        },
    ],
}

RULES = [
    # ── Bedenkenstatbestände (Abschnitt 2.1) ──────────────────────────────
    {"wenn": {"vorerkrankungen": ["herz", "gefaesse"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf-Vorerkrankung",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3",
     "befund": "Erkrankung des Herzens bzw. der Gefäße (ausgeprägte Arteriosklerose) "
               "angegeben.",
     "konsequenz": "Schweregrad vor Aufnahme bzw. Fortsetzung der Tätigkeit ärztlich "
                   "klären (Vorbefunde, EKG/Ergometrie): Bei schwerer Erkrankung "
                   "dauernde gesundheitliche Bedenken (2.1.1); ist eine "
                   "Wiederherstellung zu erwarten, befristete Bedenken (2.1.2). Bei "
                   "geringerer Ausprägung keine Bedenken unter Voraussetzungen (2.1.3): "
                   "technische/organisatorische Schutzmaßnahmen, Begrenzung der "
                   "Expositionszeit, Einsatz an Arbeitsplätzen mit geringerer "
                   "Exposition, PSA, verkürzte Nachuntersuchungsfristen."},
    {"wenn": {"vorerkrankungen": ["lunge", "schilddruese", "anaemie", "zns"]},
     "schwere": "kritisch",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3",
     "befund": "Erkrankung der Lunge, Schilddrüsenüberfunktion (Hyperthyreose), "
               "Blutarmut (Anämie) oder Erkrankung des Zentralnervensystems angegeben.",
     "konsequenz": "Schweregrad ärztlich klären (Spirometrie, Hämoglobin/Erythrozyten, "
                   "Vorbefunde): Schwere Erkrankungen begründen dauernde gesundheitliche "
                   "Bedenken (2.1.1), bei zu erwartender Wiederherstellung befristete "
                   "Bedenken (2.1.2). Bei geringerer Ausprägung Aufnahme/Fortsetzung "
                   "der Tätigkeit unter Voraussetzungen nach 2.1.3 prüfen (u. a. "
                   "geringere Exposition, PSA, verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"herz_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herzbefunde",
     "quelle": "Abschnitte 1.2.1 (besonders achten auf Herzbefunde) und 1.2.2",
     "befund": "Herzklopfen, Engegefühl in der Brust oder Belastungs-Luftnot angegeben.",
     "konsequenz": "Herzbefunde besonders sorgfältig erheben: Ergometrie nach Leitfaden "
                   "(Anhang 2) auswerten, ggf. EKG-Abklärung bzw. kardiologische "
                   "Vorstellung veranlassen; anschließend Beurteilung nach Abschnitt "
                   "2.1 (Bedenken-Systematik)."},
    # ── Akute Intoxikation, Zwischenfälle ─────────────────────────────────
    {"wenn": {"co_vergiftung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute CO-Vergiftung",
     "quelle": "Abschnitte 3.2.2 und 4 (BK-Nr. 1201)",
     "befund": "Frühere Kohlenmonoxid-Vergiftung oder Verdacht darauf angegeben.",
     "konsequenz": "Bei akuter Intoxikation nach G 7 vorgehen: sofortige CO-Bestimmung "
                   "in der Ausatemluft und/oder CO-Hb-Bestimmung, sofortiges EKG, "
                   "Kontroll-EKG spätestens vor Wiederaufnahme der Arbeit, in "
                   "besonderen Fällen EEG. Bei zurückliegender Vergiftung auf "
                   "Nachkrankheiten von Zentralnervensystem und Herz achten; Meldung "
                   "als Berufskrankheit Nr. 1201 prüfen – auch akute "
                   "CO-Vergiftungen sind zu melden."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "Abschnitte 2.2 und 3.1.4",
     "befund": "Zwischenfall mit Kohlenmonoxid am Arbeitsplatz angegeben.",
     "konsequenz": "Hergang dokumentieren, CO-Hb-Kontrolle (Biomonitoring) erwägen. "
                   "Ergeben sich Hinweise, die eine Aktualisierung der "
                   "Gefährdungsbeurteilung erfordern, Mitteilung an den Arbeitgeber "
                   "unter Wahrung der schutzwürdigen Belange des Untersuchten."},
    # ── Zwischenanamnese / chronische Belastung ───────────────────────────
    {"wenn": {"symptome": ["kopfschmerzen", "schwindel", "uebelkeit", "mattigkeit"]},
     "schwere": "pruefen",
     "bereich": "CO-typische Beschwerden",
     "quelle": "Abschnitte 1.2.1 (Zwischenanamnese) und 3.1.4 (Biomonitoring)",
     "befund": "CO-typische Beschwerden (Kopfschmerzen, Schwindel, Übelkeit, "
               "Mattigkeit/Ermüdbarkeit) angegeben.",
     "konsequenz": "Bei Verdacht auf chronische Kohlenmonoxid-Belastung wiederholte "
                   "Blutuntersuchungen auf CO-Hb: Blutentnahme am Arbeitsplatz gegen "
                   "Schichtende (Probe gekühlt, gasdicht verschlossen, Bestimmung "
                   "innerhalb von 24 Stunden); Raucherstatus bei der Bewertung "
                   "berücksichtigen (BGW 5 % CO-Hb, gesonderte Bewertung für Raucher)."},
    {"wenn": {"symptome": ["reizbarkeit", "schlaflosigkeit", "gedaechtnis"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 1.2.1 (neurasthenische Beschwerden)",
     "befund": "Neurasthenische Beschwerden angegeben (Reizbarkeit, Schlaflosigkeit, "
               "Gedächtnisschwäche).",
     "konsequenz": "Neurologische und psychische Auffälligkeiten gezielt abklären "
                   "(Suggestivfragen vermeiden); unter Umständen auf neurovegetative "
                   "und ataktische Störungen achten (vieldeutig). Bei auffälligem "
                   "Befund neurologische Facharztvorstellung erwägen."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung) und 4",
     "befund": "Proband vermutet Zusammenhang zwischen Erkrankung/Beschwerden und "
               "der Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt (unabhängig von der "
                   "24-Monats-Frist); Beschwerden objektivieren (CO-Hb-Biomonitoring, "
                   "Untersuchungsprogramm nach 1.2) und prüfen, ob ein begründeter "
                   "Verdacht auf eine Berufskrankheit Nr. 1201 zu melden ist."},
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung "
               "angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen die Fortsetzung "
                   "der Tätigkeit gibt; ggf. vorzeitige Nachuntersuchung mit dem "
                   "vollständigen Untersuchungsprogramm (1.2) durchführen und "
                   "Beurteilung nach 2.1 aktualisieren (ggf. befristete Bedenken bis "
                   "zur Wiederherstellung)."},
    # ── Mutterschutz, Lärm, PSA, Rauchen ──────────────────────────────────
    {"wenn": {"schwangerschaft": ["ja", "unsicher"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 2.2 (fruchtschädigende Wirkung)",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben oder nicht sicher "
               "auszuschließen.",
     "konsequenz": "Vor (weiterer) Tätigkeit mit CO-Exposition klären: auf die "
                   "fruchtschädigende Wirkung von Kohlenmonoxid hinweisen und "
                   "mutterschutzrechtliche Beschäftigungsbeschränkungen prüfen; "
                   "Beurteilung nach 2.1.4 nur, soweit keine "
                   "Beschäftigungsbeschränkungen bestehen."},
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombination CO + Lärm",
     "quelle": "Abschnitt 3.1.1 (Kombinationswirkung mit Lärm)",
     "befund": "Tätigkeit mit höherer CO-Exposition in Lärmbereichen angegeben.",
     "konsequenz": "Mögliche ototoxische Kombinationswirkung von Kohlenmonoxid und "
                   "Lärm bei der Gehöruntersuchung nach dem Grundsatz G 20 »Lärm« "
                   "berücksichtigen."},
    {"wenn": {"psa_atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Atemschutz/PSA",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Vorgesehener Atemschutz bzw. PSA wird selten oder nie getragen.",
     "konsequenz": "Auf allgemeine Hygienemaßnahmen und persönliche Schutzausrüstungen "
                   "hinweisen; Ursachen der Nichtbenutzung klären. Ergibt sich daraus "
                   "die Notwendigkeit, die Gefährdungsbeurteilung zu aktualisieren, "
                   "Mitteilung an den Arbeitgeber unter Wahrung der schutzwürdigen "
                   "Belange."},
    {"wenn": {"raucher_status": ["gelegentlich", "taeglich"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 2.2 und 3.1.4",
     "befund": "Aktives Rauchen angegeben.",
     "konsequenz": "Beratung: Auch durch Rauchen wird Kohlenmonoxid aufgenommen "
                   "(CO-Hb bei Rauchern durchschnittlich 10 %, bis zu 25 %; normal "
                   "ca. 1 %). Beim Biomonitoring gesonderte Bewertung für Raucher "
                   "beachten (BGW 5 % CO-Hb); Raucherstatus dokumentieren."},
]
