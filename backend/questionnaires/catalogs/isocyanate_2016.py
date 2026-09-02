# -*- coding: utf-8 -*-
"""G 27 Isocyanate – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 27 »Isocyanate«
(Fassung Oktober 2014), S. 401–417."""

SLUG = "g27-isocyanate-2016"

CATALOG = {
    "version": 2,
    "title": "G 27 Isocyanate (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 27 »Isocyanate« (Fassung Oktober 2014), S. 401–417",
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
                    "label": "Um welche Untersuchung handelt es sich heute?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt. "
                            "Die erste Nachuntersuchung folgt nach 3–12 Monaten, weitere "
                            "Nachuntersuchungen nach 12–24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erstuntersuchung", "label": "Erstuntersuchung "
                                                              "(vor Aufnahme der Tätigkeit)"},
                        {"value": "nachuntersuchung", "label": "Nachuntersuchung "
                                                               "(ich arbeite bereits mit "
                                                               "Isocyanaten)"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nachuntersuchung"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutung",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung "
                             "oder Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nachuntersuchung"]},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Umgang mit Isocyanaten",
            "subtitle": "Ihre Arbeit mit Isocyanaten (z. B. in Polyurethan-Produkten, "
                        "Lacken, Klebstoffen, Schäumen)",
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
                    "label": "Bei welchen Arbeiten haben Sie mit Isocyanaten oder "
                             "Polyurethan-Produkten (PU/PUR) zu tun?",
                    "hint": "Mehrfachauswahl möglich. Isocyanate stecken z. B. in "
                            "2-Komponenten-Lacken, Montageschaum, Klebstoffen und "
                            "Dichtmassen.",
                    "required": True,
                    "options": [
                        {"value": "herstellung", "label": "Herstellung von Isocyanaten oder "
                                                          "Polyurethanen (PUR/PU) und deren "
                                                          "Verarbeitung"},
                        {"value": "pur_schaeume", "label": "Herstellung von PUR-Schäumen "
                                                           "(z. B. Dämmplatten, Weich-/"
                                                           "Hartschaum)"},
                        {"value": "kleber_beschichtung", "label": "Herstellung/Verarbeitung von "
                                                                  "isocyanathaltigen Beschichtungen, "
                                                                  "Klebstoffen, Dichtmassen, Bindern"},
                        {"value": "isolierung", "label": "Herstellung thermischer Isolierungen "
                                                         "mit PUR-Systemen (Bau, Elektro, Auto)"},
                        {"value": "formenbau", "label": "Herstellen von technischen Kunststoffen "
                                                        "(Formenbau)"},
                        {"value": "umfuellen", "label": "Abwiegen oder manuelles Umfüllen von "
                                                        "Isocyanaten (Staub- oder "
                                                        "Dampfentwicklung)"},
                        {"value": "montageschaum", "label": "Regelmäßiges Ausschäumen mit "
                                                            "Montageschaum"},
                        {"value": "giesserei", "label": "Gießerei-Arbeiten mit isocyanathaltigen "
                                                        "Bindersystemen (Cold-Box-Kerne)"},
                        {"value": "thermolyse", "label": "Schweißen, Löten oder starkes Erhitzen "
                                                         "an polyurethanhaltigem Material "
                                                         "(Isolierungen, Beschichtungen)"},
                        {"value": "spritzen", "label": "Beschichten/Lackieren durch Spritzen "
                                                       "(auch Sportplätze, Behälter)"},
                        {"value": "sonstiges", "label": "Andere Tätigkeit mit Isocyanaten"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit Isocyanaten?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "ueber5", "label": "Mehr als 5 Jahre"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "choice",
                    "label": "Kommt Ihre Haut bei der Arbeit mit flüssigen Isocyanaten oder "
                             "nicht ausgehärteten Produkten (z. B. frischem Schaum, Lack, "
                             "Kleber) in Berührung?",
                    "hint": "Auch intensiver Hautkontakt kann eine Allergie der Atemwege "
                            "auslösen – schon ein einmaliger großflächiger Kontakt kann "
                            "ausreichen.",
                    "required": True,
                    "options": [
                        {"value": "regelmaessig", "label": "Ja, regelmäßig"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "nein", "label": "Nein, praktisch nie"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "frueher_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten mit Isocyanaten oder "
                             "anderen Gefahrstoffen (z. B. Lösungsmitteln, Stäuben) zu tun?",
                    "required": True,
                    "followup": {"id": "frueher_expo_desc", "type": "textarea",
                                 "label": "Welche Stoffe/Tätigkeiten, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "psa",
                    "type": "multi_choice",
                    "label": "Welche Schutzausrüstung benutzen Sie beim Umgang mit "
                             "Isocyanaten?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "atemschutz", "label": "Atemschutz (Maske, Gebläsehaube)"},
                        {"value": "handschuhe", "label": "Geeignete Schutzhandschuhe"},
                        {"value": "brille", "label": "Schutzbrille / Gesichtsschutz"},
                        {"value": "schutzkleidung", "label": "Schutzkleidung / Schutzanzug"},
                        {"value": "keine", "label": "Keine Schutzausrüstung"},
                        {"value": "nicht_noetig", "label": "Bei meiner Tätigkeit ist keine "
                                                           "Schutzausrüstung erforderlich"},
                    ],
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden an Augen, Atemwegen und Haut",
            "questions": [
                {
                    "id": "reiz_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie bei oder nach der Arbeit Reizbeschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "augen", "label": "Brennende oder tränende Augen"},
                        {"value": "nase", "label": "Laufende oder verstopfte Nase, Niesreiz"},
                        {"value": "hals", "label": "Kratzen im Hals, Heiserkeit, belegte "
                                                   "Stimme"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "atem_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere der folgenden Atembeschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Husten oder Hustenreiz"},
                        {"value": "auswurf", "label": "Vermehrter Auswurf (Schleim beim "
                                                      "Husten)"},
                        {"value": "kurzatmigkeit", "label": "Kurzatmigkeit bei Belastung"},
                        {"value": "atemgeraeusche", "label": "Pfeifende oder verstärkte "
                                                             "Atemgeräusche"},
                        {"value": "asthma_anfall", "label": "Anfallsartige Atemnot oder "
                                                            "Asthmaanfälle"},
                        {"value": "brustenge", "label": "Engegefühl oder Schmerzen in der "
                                                        "Brust"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "naechtlich",
                    "type": "yes_no",
                    "label": "Wachen Sie nachts mit Husten oder Atemnot auf?",
                    "required": True,
                },
                {
                    "id": "arbeitsbezug",
                    "type": "choice",
                    "label": "Falls Sie solche Beschwerden haben: Wie hängen sie mit der "
                             "Arbeit zusammen?",
                    "required": True,
                    "options": [
                        {"value": "bei_arbeit", "label": "Sie treten während der Arbeit auf "
                                                         "oder werden dort schlimmer"},
                        {"value": "verzoegert", "label": "Sie treten erst Stunden nach der "
                                                         "Arbeit oder abends/nachts auf"},
                        {"value": "besser_frei", "label": "Am Wochenende oder im Urlaub werden "
                                                          "sie deutlich besser"},
                        {"value": "kein_bezug", "label": "Kein Zusammenhang mit der Arbeit "
                                                         "erkennbar"},
                        {"value": "keine_beschwerden", "label": "Ich habe keine solchen "
                                                                "Beschwerden"},
                    ],
                },
                {
                    "id": "grippe_gefuehl",
                    "type": "yes_no",
                    "label": "Bekommen Sie einige Stunden nach der Arbeit manchmal Fieber, "
                             "Schüttelfrost oder Gliederschmerzen wie bei einer Grippe?",
                    "hint": "Das kann ein Hinweis auf eine allergische Entzündung der "
                            "Lungenbläschen (Alveolitis) sein.",
                    "required": True,
                },
                {
                    "id": "haut_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie Hautveränderungen, besonders an Händen oder "
                             "Unterarmen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "roetung", "label": "Rötung, Juckreiz oder trockene, "
                                                      "rissige Haut"},
                        {"value": "quaddeln", "label": "Quaddeln / Nesselsucht (Urtikaria)"},
                        {"value": "ekzem", "label": "Ekzem (entzündeter, ggf. nässender "
                                                    "Ausschlag)"},
                        {"value": "verfaerbung", "label": "Bräunliche Verfärbungen nach "
                                                          "Kontakt mit dem Produkt"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Allergien",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "atemwegserkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Erkrankungen der Atemwege "
                             "oder der Lunge festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "copd", "label": "COPD oder chronische Bronchitis"},
                        {"value": "emphysem", "label": "Lungenemphysem (überblähte Lunge)"},
                        {"value": "tuberkulose", "label": "Tuberkulose"},
                        {"value": "pneumokoniose", "label": "Staublunge (Pneumokoniose)"},
                        {"value": "andere_lunge", "label": "Andere Lungenerkrankung"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "hyperreagibilitaet",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen wiederholt festgestellt, dass Ihre Atemwege "
                             "überempfindlich reagieren (bronchiale Hyperreagibilität), "
                             "z. B. Hustenreiz bei kalter Luft, Rauch oder Duftstoffen?",
                    "required": True,
                },
                {
                    "id": "herzerkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Herzerkrankung (z. B. Herzschwäche, koronare "
                             "Herzkrankheit, Herzklappenfehler)?",
                    "required": True,
                    "followup": {"id": "herzerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "allergien",
                    "type": "multi_choice",
                    "label": "Haben Sie Allergien, allergische Erkrankungen oder eine "
                             "empfindliche Haut?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "heuschnupfen", "label": "Heuschnupfen / allergischer "
                                                           "Schnupfen"},
                        {"value": "hausstaub_tier", "label": "Allergie gegen Hausstaubmilben "
                                                             "oder Tiere"},
                        {"value": "neurodermitis", "label": "Neurodermitis (endogenes Ekzem)"},
                        {"value": "kontaktallergie", "label": "Kontaktallergie der Haut "
                                                              "(z. B. gegen Nickel, "
                                                              "Duftstoffe)"},
                        {"value": "trockene_haut", "label": "Sehr trockene, schuppende Haut "
                                                            "(sebostatisches Ekzem)"},
                        {"value": "andere", "label": "Andere Allergie"},
                        {"value": "keine", "label": "Keine Allergien bekannt"},
                    ],
                },
                {
                    "id": "iso_sensibilisierung",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen schon einmal eine Allergie oder "
                             "Überempfindlichkeit gegen Isocyanate festgestellt – oder "
                             "hatten Sie bei früherer Isocyanat-Arbeit Atemnot, Husten oder "
                             "Hautausschlag?",
                    "required": True,
                    "followup": {"id": "iso_sensibilisierung_desc", "type": "textarea",
                                 "label": "Was wurde festgestellt bzw. welche Beschwerden "
                                          "hatten Sie, und wann?", "when": "yes"},
                },
                {
                    "id": "rekonvaleszenz",
                    "type": "yes_no",
                    "label": "Hatten Sie in den letzten 2 Monaten eine Erkrankung der Lunge "
                             "oder des Rippenfells (z. B. Lungenentzündung, "
                             "Rippenfellentzündung)?",
                    "required": True,
                },
                {
                    "id": "akute_atemwegserkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie zurzeit oder hatten Sie in den letzten Wochen eine "
                             "akute Atemwegserkrankung (z. B. Bronchitis, starke Erkältung)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Rauchen belastet die Lunge zusätzlich zu Isocyanaten",
            "questions": [
                {
                    "id": "raucher_status",
                    "type": "choice",
                    "label": "Rauchen Sie (Zigaretten, E-Zigaretten, Tabakerhitzer o. Ä.)?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, nie geraucht"},
                        {"value": "frueher", "label": "Früher geraucht, jetzt nicht mehr"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "taeglich", "label": "Ja, täglich"},
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
    # ── Bedenkentatbestände nach Abschnitt 2.1.1 (dauernde Bedenken) ──────
    {"wenn": {"iso_sensibilisierung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Isocyanat-Sensibilisierung",
     "quelle": "Abschnitte 1.2.3, 2.1.1 und 3.2.2/3.2.3",
     "befund": "Bekannte Isocyanat-Allergie bzw. Beschwerden bei früherer "
               "Isocyanat-Exposition angegeben.",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Tätigkeit Ergänzungsuntersuchung: "
                   "Bestimmung spezifischer IgE- (ggf. IgG-) Antikörper gegen Isocyanate "
                   "(nach Exposition zwingend), Spirometrie, ggf. unspezifische inhalative "
                   "Provokation. Sensibilisierte können schon unterhalb des "
                   "Arbeitsplatzgrenzwerts mit Bronchospasmus reagieren – bei bestätigter "
                   "Überempfindlichkeit dauernde gesundheitliche Bedenken nach 2.1.1 "
                   "erwägen."},
    {"wenn": {"atemwegserkrankungen": ["asthma", "copd", "emphysem", "tuberkulose",
                                       "pneumokoniose", "andere_lunge"]},
     "schwere": "kritisch",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Erkrankung der Atemwege bzw. der Lunge in der Vorgeschichte angegeben.",
     "konsequenz": "Bedenkentatbestand nach 2.1.1 (Lungenerkrankung mit oder ohne "
                   "Einschränkung der Lungenfunktion, COPD, Asthma): Schweregrad "
                   "objektivieren (Spirometrie, ggf. Röntgen-Thorax, erweiterte "
                   "Lungenfunktionsdiagnostik, Vorbefunde). Bei schwerer Ausprägung "
                   "dauernde gesundheitliche Bedenken; bei geringer Ausprägung »keine "
                   "Bedenken unter bestimmten Voraussetzungen« nach 2.1.3 prüfen "
                   "(technische/organisatorische Schutzmaßnahmen, Begrenzung der "
                   "Expositionszeit, expositionsärmerer Arbeitsplatz, PSA, verkürzte "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"hyperreagibilitaet": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Bronchiale Hyperreagibilität",
     "quelle": "Abschnitte 2.1.1 und 3.2.2",
     "befund": "Wiederholt festgestellte überempfindliche Atemwege (bronchiale "
               "Hyperreagibilität) angegeben.",
     "konsequenz": "Wiederholt nachgewiesene symptomatische oder behandlungsbedürftige "
                   "bronchiale Hyperreagibilität ist Bedenkentatbestand nach 2.1.1 – "
                   "Betroffene können schon unterhalb des Arbeitsplatzgrenzwerts mit "
                   "Bronchospasmus reagieren. Befunde objektivieren (erweiterte "
                   "Lungenfunktionsdiagnostik, ggf. unspezifische inhalative Provokation); "
                   "sonst Vorgehen nach 2.1.3 mit verkürzten Nachuntersuchungsfristen."},
    {"wenn": {"herzerkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 1.2.2 und 2.1.1",
     "befund": "Herzerkrankung angegeben.",
     "konsequenz": "Herzkrankheiten sind Bedenkentatbestand nach 2.1.1: kardiale Befunde "
                   "einholen, bei gegebener Indikation Ergometrie (Anhang 2, Leitfaden "
                   "»Ergometrie«). Bei geringer Ausprägung Vorgehen nach 2.1.3 "
                   "(Schutzmaßnahmen, verkürzte Nachuntersuchungsfristen) prüfen."},
    {"wenn": {"allergien": ["neurodermitis"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Neurodermitis (endogenes Ekzem) angegeben.",
     "konsequenz": "Endogenes Ekzem ist Bedenkentatbestand nach 2.1.1: Hautzustand "
                   "erheben, dermatologische Vorbefunde einbeziehen; bei geringer "
                   "Ausprägung Vorgehen nach 2.1.3 mit optimalem Hautschutz und "
                   "verkürzten Nachuntersuchungsfristen prüfen."},
    # ── Befristete Bedenken nach Abschnitt 2.1.2 ──────────────────────────
    {"wenn": {"rekonvaleszenz": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Rekonvaleszenz",
     "quelle": "Abschnitt 2.1.2",
     "befund": "Erkrankung der Lunge oder des Rippenfells in den letzten 2 Monaten "
               "angegeben.",
     "konsequenz": "Für Rekonvaleszenten nach folgenlos abgeklungener Erkrankung der "
                   "Lunge oder des Rippenfells gelten befristete gesundheitliche Bedenken "
                   "für die Dauer von 1 bis 2 Monaten; Aufnahme bzw. Fortsetzung der "
                   "Tätigkeit erst danach, Nachuntersuchung ansetzen."},
    {"wenn": {"akute_atemwegserkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Akute Atemwegserkrankung",
     "quelle": "Abschnitt 2.1.2 (Nachuntersuchung)",
     "befund": "Aktuelle oder kurz zurückliegende akute Atemwegserkrankung angegeben.",
     "konsequenz": "Bei Personen mit oder kurzfristig nach akuten Erkrankungen der "
                   "Atemwege befristete gesundheitliche Bedenken erwägen; Spirometrie "
                   "ggf. erst nach Abklingen durchführen und Beurteilung bis dahin "
                   "zurückstellen."},
    # ── Atopie und Hautschutz (Abschnitt 2.1.3) ───────────────────────────
    {"wenn": {"allergien": ["heuschnupfen", "hausstaub_tier", "kontaktallergie", "andere"]},
     "schwere": "pruefen",
     "bereich": "Atopie/Allergie",
     "quelle": "Abschnitte 1.2.2 und 2.1.3",
     "befund": "Allergische Erkrankung bzw. atopische Disposition angegeben.",
     "konsequenz": "Atopiker neigen stärker zur Isocyanat-Sensibilisierung: Vorgehen "
                   "analog 2.1.3 (»keine Bedenken unter bestimmten Voraussetzungen«) mit "
                   "verkürzten Nachuntersuchungsfristen erwägen; ggf. Gesamt-IgE bestimmen "
                   "und bei Allergieanamnese unspezifische inhalative Provokation im "
                   "Rahmen der erweiterten Lungenfunktionsdiagnostik."},
    {"wenn": {"allergien": ["trockene_haut"]},
     "schwere": "hinweis",
     "bereich": "Haut",
     "quelle": "Abschnitt 2.1.3",
     "befund": "Sehr trockene, schuppende Haut (sebostatisches Ekzem) angegeben.",
     "konsequenz": "Für das sebostatische Ekzem analoges Vorgehen nach 2.1.3: optimalen "
                   "Hautschutz empfehlen und Hautzustand bei den Nachuntersuchungen "
                   "kontrollieren."},
    # ── Aktuelle Beschwerden ──────────────────────────────────────────────
    {"wenn": {"atem_symptome": ["husten", "auswurf", "kurzatmigkeit", "atemgeraeusche",
                                "asthma_anfall", "brustenge"]},
     "schwere": "pruefen",
     "bereich": "Atembeschwerden",
     "quelle": "Abschnitte 1.2.1, 1.2.2 und 1.2.3",
     "befund": "Atembeschwerden (Husten, Auswurf, Kurzatmigkeit, Atemgeräusche, "
               "asthmatische Zustände oder Brustenge) angegeben.",
     "konsequenz": "Anamnestischer Verdacht auf eine Erkrankung nach 2.1.1: erweiterte "
                   "Lungenfunktionsdiagnostik (Ganzkörperplethysmographie, Untersuchung "
                   "vor und nach einer Arbeitsschicht mit Exposition, Peak-flow-"
                   "Messungen); in unklaren Fällen Ergänzungsuntersuchung mit Bestimmung "
                   "spezifischer IgE- (ggf. IgG-) Antikörper – nach Exposition zwingend – "
                   "und unspezifischer inhalativer Provokation. Bedenken nach 2.1 prüfen."},
    {"wenn": {"naechtlich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atembeschwerden",
     "quelle": "Abschnitte 1.2.1 (Zwischenanamnese) und 3.2.3",
     "befund": "Nächtlicher Husten bzw. nächtliche Atemnot angegeben.",
     "konsequenz": "Warnsymptom für Isocyanat-Asthma vom verzögerten oder dualen Typ: "
                   "erweiterte Lungenfunktionsdiagnostik mit Peak-flow-Messungen über "
                   "Arbeits- und arbeitsfreie Tage; in unklaren Fällen "
                   "Ergänzungsuntersuchung (spezifische Antikörper)."},
    {"wenn": {"arbeitsbezug": ["bei_arbeit", "verzoegert", "besser_frei"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug der Beschwerden",
     "quelle": "Abschnitte 1.1, 2.2 und 4",
     "befund": "Beschwerden mit erkennbarem Bezug zur Arbeit (während der Arbeit, "
               "verzögert danach oder Besserung an freien Tagen).",
     "konsequenz": "Verdacht auf arbeitsbedingte Atemwegserkrankung: Untersuchung vor und "
                   "nach einer Arbeitsschicht, Peak-flow-Verlauf, spezifische Antikörper. "
                   "Bei begründetem Verdacht ärztliche Anzeige einer Berufskrankheit "
                   "(BK-Nr. 1315) prüfen; Hinweise zur Aktualisierung der "
                   "Gefährdungsbeurteilung dem Arbeitgeber mitteilen (Abschnitt 2.2)."},
    {"wenn": {"grippe_gefuehl": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Alveolitis-Verdacht",
     "quelle": "Abschnitte 3.2.2 und 3.2.3",
     "befund": "Grippeartige Beschwerden (Fieber, Schüttelfrost, Gliederschmerzen) "
               "Stunden nach der Arbeit angegeben.",
     "konsequenz": "An eine exogen-allergische Alveolitis denken: erweiterte "
                   "Lungenfunktionsdiagnostik, Bestimmung spezifischer IgG-Antikörper, "
                   "zeitnahe pneumologische Abklärung; bis zur Klärung Bedenken gegen die "
                   "Fortsetzung der Exposition erwägen."},
    {"wenn": {"haut_symptome": ["roetung", "quaddeln", "ekzem", "verfaerbung"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 1.2.1 (Zwischenanamnese) und 3.2.2",
     "befund": "Hautveränderungen (Rötung/Juckreiz, Quaddeln, Ekzem oder bräunliche "
               "Kontaktverfärbungen) angegeben.",
     "konsequenz": "Isocyanate können Reizzustände (Dermatitis artificialis) und "
                   "Sensibilisierungen (Urtikaria, Kontaktekzem) verursachen; bräunliche "
                   "Verfärbungen zeigen direkten Hautkontakt an. Dermatologische "
                   "Abklärung, Hautschutzberatung (TRGS 401); Schutzmaßnahmen und "
                   "Trageverhalten der PSA überprüfen."},
    {"wenn": {"reiz_symptome": ["augen", "nase", "hals"]},
     "schwere": "pruefen",
     "bereich": "Reizsymptome",
     "quelle": "Abschnitte 2.2 und 3.2.2",
     "befund": "Reizbeschwerden an Augen, Nase oder Rachen bei bzw. nach der Arbeit "
               "angegeben.",
     "konsequenz": "Mögliche Frühzeichen einer relevanten Isocyanat-Exposition "
                   "(Konjunktivitis, Rhinitis, Pharyngitis/Laryngitis): "
                   "Expositionssituation klären; ergeben sich Hinweise auf notwendige "
                   "Verbesserungen des Arbeitsschutzes, Mitteilung an den Arbeitgeber "
                   "(Abschnitt 2.2); Verlauf bei der Nachuntersuchung kontrollieren."},
    # ── Exposition, Biomonitoring, Fristen ────────────────────────────────
    {"wenn": {"hautkontakt": ["regelmaessig"]},
     "schwere": "pruefen",
     "bereich": "Hautkontakt/Biomonitoring",
     "quelle": "Abschnitte 1.2.2, 3.1.3 und 3.1.4",
     "befund": "Regelmäßiger Hautkontakt mit Isocyanaten bzw. nicht ausgehärteten "
               "Produkten angegeben.",
     "konsequenz": "Biomonitoring nach Exposition durchführen (Urin, Probennahme zum "
                   "Expositions- bzw. Schichtende): z. B. 4,4'-Diaminodiphenylmethan "
                   "(MDA) für MDI (BLW 10 µg/g Kreatinin) oder Hexamethylendiamin für HDI "
                   "(BGW 15 µg/g Kreatinin) – die biologischen Werte erfassen auch die "
                   "Aufnahme über die Haut. Hautschutz beraten; intensiver Hautkontakt "
                   "kann eine Sensibilisierung der Atemwege verursachen."},
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt: prüfen, ob die Erkrankung "
                   "Anlass zu Bedenken gegen eine Fortsetzung der Tätigkeit geben könnte; "
                   "Befunde und Behandlungsunterlagen einholen."},
    {"wenn": {"zusammenhang_vermutung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitte 1.1 und 4",
     "befund": "Die Person vermutet einen Zusammenhang zwischen Erkrankung/Beschwerden "
               "und der Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen; Beschwerden und "
                   "Expositionssituation dokumentieren, gezielte Diagnostik veranlassen; "
                   "bei begründetem Verdacht BK-Anzeige (BK-Nr. 1315) prüfen."},
    # ── Schutzmaßnahmen und Beratung ──────────────────────────────────────
    {"wenn": {"psa": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen/PSA",
     "quelle": "Abschnitt 2.2",
     "befund": "Umgang mit Isocyanaten ohne persönliche Schutzausrüstung angegeben.",
     "konsequenz": "Auf allgemeine Hygienemaßnahmen und persönliche Schutzausrüstung "
                   "hinweisen; Abgleich mit der Gefährdungsbeurteilung. Ergeben sich "
                   "Hinweise, dass die Gefährdungsbeurteilung zur Verbesserung des "
                   "Arbeitsschutzes aktualisiert werden muss, Mitteilung an den "
                   "Arbeitgeber unter Wahrung der schutzwürdigen Belange der "
                   "untersuchten Person."},
    {"wenn": {"raucher_status": ["taeglich", "gelegentlich"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 2.2",
     "befund": "Aktuelles Rauchen angegeben.",
     "konsequenz": "Beratung: durch inhalatives Rauchen wird u. a. die Lungenfunktion "
                   "verschlechtert – zusätzlich zur Isocyanat-Belastung; "
                   "Rauchstopp empfehlen."},
]
