# -*- coding: utf-8 -*-
"""Kohlenmonoxid – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
Kapitel »Kohlenmonoxid« (E KMO, Fassung Januar 2022, Grenzwerte
aktualisiert 2024), S. 352–372."""

SLUG = "kohlenmonoxid-2024"

CATALOG = {
    "version": 2,
    "title": "Kohlenmonoxid (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Kohlenmonoxid« (E KMO, Fassung Januar 2022, "
             "Grenzwerte aktualisiert 2024), S. 352–372",
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
                             "Kohlenmonoxid?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Kohlenmonoxid-Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur "
                                                      "Kohlenmonoxid-Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert für Kohlenmonoxid (20 ppm) nicht "
                            "eingehalten wird. Angebotsvorsorge: wenn eine Belastung "
                            "nicht ausgeschlossen werden kann.",
                    "required": True,
                    "options": [
                        {"value": "pflicht", "label": "Vom Betrieb verpflichtend veranlasst "
                                                      "(Pflichtvorsorge)"},
                        {"value": "angebot", "label": "Vom Betrieb angeboten (Angebotsvorsorge)"},
                        {"value": "wunsch", "label": "Auf meinen eigenen Wunsch (Wunschvorsorge)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
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
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_bereiche",
                    "type": "multi_choice",
                    "label": "Arbeiten Sie in einem der folgenden Bereiche mit höherer "
                             "Kohlenmonoxid-Belastung?",
                    "hint": "Mehrfachauswahl möglich. Kohlenmonoxid ist ein farb-, geruch- "
                            "und geschmackloses, sehr giftiges Gas, das bei fast allen "
                            "Verbrennungen entsteht.",
                    "required": True,
                    "options": [
                        {"value": "schwerindustrie", "label": "Schwerindustrie oder Kokerei "
                         "(z. B. Generatorgas, Kokereigas, Gichtgas, Rauchgas)"},
                        {"value": "giesserei_ofen", "label": "Gießerei oder Ofenanlagen "
                         "(Abgießen/Abkühlstrecke, Kupolofen, Koksofen, Hochofen, "
                         "gichtgasbeheizte Glühöfen)"},
                        {"value": "feuerungsbau", "label": "Feuerungs- oder Schornsteinbau, "
                         "wenn unter laufendem Betrieb gearbeitet wird"},
                        {"value": "motorabgase_raum", "label": "Motorabgase in geschlossenen "
                         "Räumen (z. B. Kfz-Werkstatt, Tiefgarage mit viel Verkehr, Tunnelbau)"},
                        {"value": "fluessiggas_stapler", "label": "Lagerbereiche mit "
                         "flüssiggasbetriebenen Gabelstaplern (Flurförderzeugen)"},
                        {"value": "behaelter", "label": "Arbeiten in Behältern oder engen "
                         "Räumen, in denen CO entstehen kann (z. B. flüssiggasbetriebene "
                         "Lötbrenner)"},
                        {"value": "baumaschinen", "label": "Benzinmotor-Maschinen in Räumen "
                         "oder in Gruben/Gräben (z. B. Flügelglätter, Verdichter, Rüttler)"},
                        {"value": "roro", "label": "Geschlossene Ladedecks auf RoRo-Schiffen "
                         "mit Fahrzeugverkehr"},
                        {"value": "sonstige", "label": "Anderer Bereich mit spürbarer "
                         "Abgas- oder Rauchgas-Belastung"},
                        {"value": "keine", "label": "Keiner dieser Bereiche"},
                    ],
                },
                {
                    "id": "expo_weitere",
                    "type": "multi_choice",
                    "label": "Üben Sie eine der folgenden Tätigkeiten mit nicht geringer "
                             "Kohlenmonoxid-Belastung aus?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "schweissen", "label": "Autogenschweißen oder Brennschneiden "
                         "in geschlossenen Räumen"},
                        {"value": "verkehr", "label": "Tätigkeit mit Kfz-Abgasen (z. B. "
                         "Linienverkehr, Müllsammlung, Kfz-Kontrollen, PKW-Waschanlage, "
                         "Tiefgarage)"},
                        {"value": "huettenlabor", "label": "Tätigkeit im Hüttenlabor oder "
                         "Wartung auf Härteöfen"},
                        {"value": "holzpellets", "label": "Lagerung von Holzpellets in "
                         "kleinen, schlecht gelüfteten Räumen"},
                        {"value": "shisha", "label": "Shisha-Betrieb mit Wasserpfeifen auf "
                         "Holzkohlebasis"},
                        {"value": "kunststoff", "label": "Extrudieren von Kunststoffabfällen "
                         "bei hoher Temperatur ohne Absaugung"},
                        {"value": "keine", "label": "Keine davon"},
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
                    "label": "Gab es an Ihrem Arbeitsplatz Zwischenfälle oder ungewöhnliche "
                             "Betriebszustände mit Kohlenmonoxid (z. B. CO-Alarm, starke "
                             "Abgas- oder Rauchentwicklung, Unfall)?",
                    "required": True,
                    "followup": {"id": "zwischenfall_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Berufskrankheit anerkannt, oder läuft "
                             "derzeit ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Erkrankung bzw. welches Verfahren?",
                                 "when": "yes"},
                },
                {
                    "id": "laermbereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie zusätzlich in Lärmbereichen (sehr laute "
                             "Arbeitsumgebung, Gehörschutz erforderlich)?",
                    "hint": "Kohlenmonoxid kann das Innenohr zusätzlich belasten "
                            "(»ototoxische«, also ohrschädigende Wirkung) – zusammen mit "
                            "Lärm ist das besonders wichtig.",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Atemschutz und Schutzmaßnahmen an Ihrem Arbeitsplatz",
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
                             "Kopfschmerzen, Schwindel, Übelkeit, Herzklopfen oder "
                             "ungewöhnliche Müdigkeit?",
                    "required": True,
                },
                {
                    "id": "symptome_arbeit",
                    "type": "multi_choice",
                    "label": "Welche Beschwerden sind das?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "beschwerden_aktuell", "in": ["yes"]},
                    "options": [
                        {"value": "kopfschmerzen", "label": "Kopfschmerzen"},
                        {"value": "schwindel", "label": "Schwindel"},
                        {"value": "uebelkeit", "label": "Übelkeit oder Brechreiz"},
                        {"value": "muedigkeit", "label": "Allgemeine Mattigkeit oder "
                                                         "schnelle Ermüdbarkeit"},
                        {"value": "herzklopfen", "label": "Herzklopfen oder Herzrasen"},
                        {"value": "brustschmerz", "label": "Engegefühl oder Schmerzen in "
                                                           "der Brust"},
                        {"value": "atemnot", "label": "Kurzatmigkeit bei Anstrengung"},
                        {"value": "sonstige", "label": "Andere Beschwerden"},
                    ],
                },
                {
                    "id": "symptome_bezug",
                    "type": "choice",
                    "label": "Bessern sich diese Beschwerden, wenn Sie länger nicht am "
                             "Arbeitsplatz sind (z. B. am Wochenende oder im Urlaub)?",
                    "required": True,
                    "show_if": {"id": "beschwerden_aktuell", "in": ["yes"]},
                    "options": [
                        {"value": "ja", "label": "Ja, deutlich"},
                        {"value": "nein", "label": "Nein, sie bleiben gleich"},
                        {"value": "unklar", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "neuro_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine der folgenden Beschwerden "
                             "bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "reizbarkeit", "label": "Ungewöhnliche Reizbarkeit"},
                        {"value": "schlaflosigkeit", "label": "Schlaflosigkeit oder "
                                                              "Schlafstörungen"},
                        {"value": "gedaechtnis", "label": "Nachlassendes Gedächtnis oder "
                                                          "Konzentrationsprobleme"},
                        {"value": "gangunsicherheit", "label": "Gangunsicherheit oder "
                                                               "Gleichgewichtsstörungen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
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
                            "Sauerstofftransport im Blut – diese Erkrankungen können sich "
                            "dadurch verschlimmern.",
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
                    "id": "gehoer_vorschaden",
                    "type": "yes_no",
                    "label": "Ist Ihr Gehör vorgeschädigt (z. B. bekannte "
                             "Lärmschwerhörigkeit, Hörminderung, Hörgerät)?",
                    "required": True,
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
            "title": "Rauchen",
            "subtitle": "Rauchen erhöht die Kohlenmonoxid-Belastung zusätzlich",
            "questions": [
                {
                    "id": "raucher_status",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Auch durch Rauchen wird Kohlenmonoxid aufgenommen. Bei "
                            "Rauchenden kann der CO-Gehalt im Blut deutlich erhöht sein – "
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
    # ── Reproduktionstoxizität / Mutterschutz ─────────────────────────────
    {"wenn": {"schwangerschaft": ["ja", "unsicher"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6 (Reproduktionstoxizität, Repr. 1A), 7.1 und 8.1",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben oder nicht sicher "
               "auszuschließen.",
     "konsequenz": "Vor (weiterer) Tätigkeit mit CO-Exposition klären: Kohlenmonoxid ist "
                   "reproduktionstoxisch Kategorie Repr. 1A (kann das Kind im Mutterleib "
                   "schädigen); ein Risiko der Fruchtschädigung ist auch bei Einhaltung "
                   "von AGW und BGW nicht auszuschließen. Beschäftigungsbeschränkungen "
                   "nach Mutterschutzgesetz prüfen, über die fruchtschädigende Wirkung "
                   "aufklären und die Gefährdungsbeurteilung für werdende/stillende "
                   "Mütter einfordern."},
    # ── Zwischenfälle, akute Vergiftung ───────────────────────────────────
    {"wenn": {"co_vergiftung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute CO-Vergiftung",
     "quelle": "Abschnitte 6.3.2 und 6.5 (BK-Nr. 1201)",
     "befund": "Frühere Kohlenmonoxid-Vergiftung oder Verdacht darauf angegeben.",
     "konsequenz": "Hergang und Behandlung dokumentieren; gezielt auf Nachkrankheiten "
                   "von Zentralnervensystem und Herz achten (Anamnese, ggf. "
                   "neurologische/kardiologische Abklärung). Prüfen, ob der Vorfall als "
                   "Berufskrankheit Nr. 1201 »Erkrankungen durch Kohlenmonoxid« "
                   "angezeigt wurde – auch akute CO-Vergiftungen am Arbeitsplatz sind "
                   "anzuzeigen."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "Abschnitte 7.1 (Zwischenfälle, ungewöhnliche Betriebszustände) und 8.2",
     "befund": "Zwischenfall bzw. ungewöhnlicher Betriebszustand mit Kohlenmonoxid "
               "angegeben.",
     "konsequenz": "Zwischenfall dokumentieren und mit der Gefährdungsbeurteilung "
                   "abgleichen; Biomonitoring CO-Hb veranlassen. Ergeben sich "
                   "Anhaltspunkte, dass die Schutzmaßnahmen nicht ausreichen, Mitteilung "
                   "an das Unternehmen und Vorschlag von Schutzmaßnahmen "
                   "(§ 6 (4) ArbMedVV)."},
    # ── Beschwerden ───────────────────────────────────────────────────────
    {"wenn": {"symptome_arbeit": ["kopfschmerzen", "schwindel", "uebelkeit",
                                  "muedigkeit"]},
     "schwere": "pruefen",
     "bereich": "CO-typische Beschwerden",
     "quelle": "Abschnitte 6.3.3 und 6.4 (Biomonitoring)",
     "befund": "CO-typische Allgemeinbeschwerden (Kopfschmerzen, Schwindel, Übelkeit, "
               "Mattigkeit) bei oder nach der Arbeit angegeben.",
     "konsequenz": "Verdacht auf (sub-)akute bzw. chronische CO-Belastung abklären: "
                   "wiederholte Blutuntersuchungen auf CO-Hb, Blutentnahme jeweils am "
                   "Arbeitsplatz gegen Schichtende (Probe gekühlt, gasdicht "
                   "verschlossen, Bestimmung innerhalb von 24 Stunden). Abgleich mit "
                   "der Gefährdungsbeurteilung."},
    {"wenn": {"symptome_arbeit": ["herzklopfen", "brustschmerz", "atemnot"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf-Beschwerden",
     "quelle": "Abschnitte 6.3.2, 7.2.2 und 7.4",
     "befund": "Herzklopfen, Brustenge/-schmerz oder Belastungs-Kurzatmigkeit "
               "angegeben.",
     "konsequenz": "Kardiale Symptomatik abklären: Ergometrie nach Leitfaden (Anhang 2) "
                   "sorgfältig auswerten, auf Zeichen einer Myokardischämie achten "
                   "(bei Herzkranken schon ab 3–5 % CO-Hb Leistungseinschränkung "
                   "möglich); ggf. kardiologische Vorstellung. Beurteilung nach "
                   "Abschnitt 7.4 (Erkrankungen des Herzens)."},
    {"wenn": {"symptome_bezug": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsplatzbezug",
     "quelle": "Abschnitte 6.4 und 8.2",
     "befund": "Beschwerden bessern sich deutlich bei längerer Abwesenheit vom "
               "Arbeitsplatz (Wochenende/Urlaub).",
     "konsequenz": "Deutlicher Arbeitsplatzbezug: Biomonitoring CO-Hb gegen Schichtende "
                   "veranlassen und Expositionssituation prüfen; dem Unternehmen ggf. "
                   "Überprüfung der Gefährdungsbeurteilung und zusätzliche "
                   "Schutzmaßnahmen vorschlagen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"neuro_beschwerden": ["reizbarkeit", "schlaflosigkeit", "gedaechtnis",
                                    "gangunsicherheit"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 7.1 (Beschwerden, neurovegetative/ataktische Störungen)",
     "befund": "Neurasthenische bzw. neurologische Beschwerden angegeben (Reizbarkeit, "
               "Schlaflosigkeit, Gedächtnisschwäche, Gangunsicherheit).",
     "konsequenz": "Vertiefte neurologisch-psychische Anamnese (Suggestivfragen "
                   "vermeiden); auf neurovegetative und ataktische Störungen achten "
                   "(unspezifisch). Bei auffälligem Befund neurologische "
                   "Facharztvorstellung; Verlauf bei der nächsten Vorsorge "
                   "kontrollieren."},
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"vorerkrankungen": ["herz", "gefaesse"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf-Vorerkrankung",
     "quelle": "Abschnitte 7.4, 7.4.2–7.4.4",
     "befund": "Erkrankung des Herzens bzw. der Gefäße (ausgeprägte Arteriosklerose) "
               "angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung: Ausprägung klären (Vorbefunde, "
                   "Ergometrie), prüfen, ob die Tätigkeit ohne gesundheitliche "
                   "Gefährdung möglich ist. Bei geringerer Ausprägung Maßnahmen nach "
                   "7.4.2 empfehlen (Substitution, technische/organisatorische "
                   "Schutzmaßnahmen, Begrenzung der Expositionszeit, Einsatz an "
                   "Arbeitsplätzen mit geringerer Exposition, PSA); bei zu erwartender "
                   "Änderung des Schweregrads verkürzte Vorsorgefristen nach 7.4.3; "
                   "ohne Aussicht auf Erfolg Tätigkeitswechsel nach 7.4.4 erwägen "
                   "(Mitteilung an den Arbeitgeber nur mit Einwilligung)."},
    {"wenn": {"vorerkrankungen": ["lunge", "schilddruese", "anaemie", "zns"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung",
     "quelle": "Abschnitte 7.4, 7.4.2–7.4.4",
     "befund": "Erkrankung der Lunge, Schilddrüsenüberfunktion, Blutarmut (Anämie) "
               "oder Erkrankung des Zentralnervensystems angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung: Ausprägung und Verlauf klären "
                   "(Spirometrie, Hämoglobin/Erythrozyten, Vorbefunde). Prüfen, ob "
                   "Maßnahmen nach 7.4.2 (z. B. Expositionsbegrenzung, geringere "
                   "Exposition, PSA) ausreichen; ggf. verkürzte Vorsorgefristen nach "
                   "7.4.3, bei fehlender Aussicht auf Erfolg Tätigkeitswechsel nach "
                   "7.4.4 erwägen."},
    {"wenn": {"gehoer_vorschaden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gehör",
     "quelle": "Abschnitte 7.4 (Vorschädigung des Gehörs) und 8.1",
     "befund": "Vorschädigung des Gehörs angegeben.",
     "konsequenz": "Ototoxische Wirkung von Kohlenmonoxid bei der Beurteilung "
                   "berücksichtigen; über die zusätzliche Gefährdung des Gehörs "
                   "beraten. Bei gleichzeitiger Lärmarbeit Gehöruntersuchung nach der "
                   "DGUV Empfehlung »Lärm« einbeziehen."},
    {"wenn": {"laermbereich": ["yes"]},
     "wenn_nicht": {"gehoer_vorschaden": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombination CO + Lärm",
     "quelle": "Abschnitt 6.1.1 (Kombinationswirkung mit Lärm)",
     "befund": "Tätigkeit mit CO-Exposition in Lärmbereichen angegeben.",
     "konsequenz": "Mögliche Kombinationswirkung von Kohlenmonoxid (ototoxisch) und "
                   "Lärm bei der Gehöruntersuchung nach der DGUV Empfehlung »Lärm« "
                   "berücksichtigen; Beratung zum konsequenten Gehörschutz."},
    # ── Schutzmaßnahmen, Rauchen, BK-Verfahren ────────────────────────────
    {"wenn": {"psa_atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Atemschutz/PSA",
     "quelle": "Abschnitte 8.1 und 8.2; DGUV Regel 112-190",
     "befund": "Vorgesehener Atemschutz bzw. PSA wird selten oder nie getragen.",
     "konsequenz": "Beratung zum Tragen geeigneter PSA, insbesondere Atemschutz "
                   "(individuellen Gesundheitszustand beachten); Ursachen der "
                   "Nichtbenutzung klären. Reichen die Schutzmaßnahmen nicht aus, "
                   "Mitteilung an das Unternehmen und Vorschlag von Maßnahmen "
                   "(§ 6 (4) ArbMedVV)."},
    {"wenn": {"raucher_status": ["gelegentlich", "taeglich"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 6.4 und 8.1",
     "befund": "Aktives Rauchen angegeben.",
     "konsequenz": "Beratung: Auch durch Rauchen wird zusätzlich Kohlenmonoxid "
                   "aufgenommen (CO-Hb bei Rauchenden durchschnittlich 10 %, bis zu "
                   "25 %). Beim Biomonitoring berücksichtigen, dass BGW und BAT-Wert "
                   "(5 % CO-Hb) für Nichtrauchende abgeleitet sind; Raucherstatus "
                   "dokumentieren und Tabakentwöhnung anbieten."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 6.5 und 7.1 (laufendes BK-Verfahren)",
     "befund": "Anerkannte Berufskrankheit oder laufendes BK-Verfahren angegeben.",
     "konsequenz": "Laufendes BK-Verfahren dokumentieren, vorhandene Befunde und "
                   "Bescheide in die Beurteilung einbeziehen; Relevanz für die "
                   "aktuelle Tätigkeit prüfen."},
]
