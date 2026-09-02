# -*- coding: utf-8 -*-
"""G 34 Fluor oder seine anorganischen Verbindungen – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016,
G 34 »Fluor oder seine anorganischen Verbindungen« (Fassung Oktober 2014),
S. 483–494."""

SLUG = "g34-fluor-2016"

CATALOG = {
    "version": 2,
    "title": "G 34 Fluor oder seine anorganischen Verbindungen (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 34 »Fluor oder seine anorganischen Verbindungen« "
             "(Fassung Oktober 2014), S. 483–494",
    "sections": [
        # ── 1 ─ Anlass der Untersuchung ────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "unt_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich heute?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt, "
                            "Nachuntersuchungen in der Regel nach 12 bis 24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich wurde deswegen schon einmal untersucht)"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Belastung ────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Belastung",
            "subtitle": "Ihre Arbeit mit Fluor und seinen anorganischen Verbindungen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "stoffe",
                    "type": "multi_choice",
                    "label": "Mit welchen dieser Stoffe haben Sie bei der Arbeit zu tun?",
                    "hint": "Mehrfachauswahl möglich. Die Angaben stehen meist im "
                            "Sicherheitsdatenblatt oder in der Betriebsanweisung.",
                    "required": True,
                    "options": [
                        {"value": "fluor_gas", "label": "Fluor (blassgelbes, sehr reaktionsfähiges Gas)"},
                        {"value": "hf_flusssaeure", "label": "Fluorwasserstoff oder Flusssäure (HF)"},
                        {"value": "saure_fluoride", "label": "Sauer reagierende Fluoride / Hydrogenfluoride (z. B. Ammoniumhydrogenfluorid)"},
                        {"value": "fluoride", "label": "Andere Fluoridsalze (z. B. Natriumfluorid, Kryolith)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "verfahren",
                    "type": "multi_choice",
                    "label": "Welche dieser Arbeiten führen Sie durch?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "herstellen_abfuellen", "label": "Herstellen, Um- oder Abfüllen von Fluorwasserstoff, Flusssäure oder Fluoriden"},
                        {"value": "glas_keramik", "label": "Säure-Politur, Ätzen oder Trübglasherstellung in der Glas-/Keramikindustrie"},
                        {"value": "aluminium_elektrolyse", "label": "Schmelzflusselektrolyse / Aluminiumherstellung"},
                        {"value": "holzschutz", "label": "Herstellen oder Anwenden fluoridhaltiger Holzschutzmittel"},
                        {"value": "metall_oberflaeche", "label": "Oberflächenbehandlung von Metallen (z. B. Edelstahl nach dem Schweißen reinigen)"},
                        {"value": "schweissen", "label": "Schweißen mit basisch umhüllten Elektroden oder Fülldrähten (über 6 % Fluoride)"},
                        {"value": "reiniger", "label": "Arbeiten mit flusssäurehaltigen Keramik- oder fluoridhaltigen Felgenreinigern"},
                        {"value": "sonstige", "label": "Andere Arbeiten mit Fluorverbindungen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit Fluor oder "
                             "Fluorverbindungen?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis10", "label": "1 bis 10 Jahre"},
                        {"value": "ueber10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kann es bei Ihrer Arbeit zu direktem Hautkontakt mit Flusssäure "
                             "oder flusssäurehaltigen Lösungen kommen (z. B. Spritzer)?",
                    "hint": "Flusssäure wird über die Haut in erheblichem Maß aufgenommen und "
                            "kann tiefe Gewebeschäden und Vergiftungen verursachen.",
                    "required": True,
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Unfälle oder Zwischenfälle mit "
                             "Fluorverbindungen (z. B. Hautspritzer, Verätzung, Einatmen von "
                             "Gasen oder Dämpfen)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Berufen oder Tätigkeiten Kontakt mit "
                             "Fluor, Flusssäure oder Fluoriden?",
                    "required": True,
                    "followup": {"id": "frueher_expo_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Persönliche Schutzausrüstung und Verhalten am Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_tragen",
                    "type": "multi_choice",
                    "label": "Welche persönliche Schutzausrüstung (PSA) benutzen Sie beim "
                             "Umgang mit diesen Stoffen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "atemschutz", "label": "Atemschutz (Maske, Filtergerät)"},
                        {"value": "handschuhe", "label": "Chemikalien-Schutzhandschuhe"},
                        {"value": "brille", "label": "Schutzbrille oder Gesichtsschutz"},
                        {"value": "kleidung", "label": "Schutzkleidung / Schürze"},
                        {"value": "keine", "label": "Keine Schutzausrüstung"},
                        {"value": "kein_umgang", "label": "Ich habe (noch) keinen direkten Umgang mit den Stoffen"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme beim Tragen der Schutzausrüstung "
                             "(z. B. Atemnot unter der Maske, Hautreizung durch Handschuhe)?",
                    "required": True,
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
                {
                    "id": "hygiene",
                    "type": "choice",
                    "label": "Können Sie die Hygieneregeln am Arbeitsplatz einhalten "
                             "(Hände waschen, Arbeitskleidung wechseln, nicht am Arbeitsplatz "
                             "essen/trinken/rauchen)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "teilweise", "label": "Nur teilweise"},
                        {"value": "nein", "label": "Nein / kaum möglich"},
                    ],
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, auf die bei diesem Untersuchungsanlass besonders "
                        "geachtet wird",
            "questions": [
                {
                    "id": "atemwege",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere dieser Atemwegs-Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Häufiger Husten"},
                        {"value": "auswurf", "label": "Vermehrter Auswurf (Schleim beim Husten)"},
                        {"value": "atemgeraeusche", "label": "Pfeifende oder rasselnde Atemgeräusche"},
                        {"value": "atemnot", "label": "Atemnot bei Bewegung oder Belastung"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "reizung",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit Reizungen der Augen, der Nase oder der "
                             "Atemwege (z. B. Tränenfluss, Nasenlaufen, Brennen, Hustenreiz)?",
                    "required": True,
                },
                {
                    "id": "obstipation",
                    "type": "yes_no",
                    "label": "Leiden Sie unter Verstopfung (Obstipation)?",
                    "required": True,
                },
                {
                    "id": "haut_symptome",
                    "type": "yes_no",
                    "label": "Haben Sie Hautveränderungen, die mit der Arbeit zusammenhängen "
                             "könnten (Rötung, Brennen, schlecht heilende oder schmerzende "
                             "Stellen – auch wenn Schmerzen erst Stunden später auftraten)?",
                    "required": True,
                    "followup": {"id": "haut_symptome_desc", "type": "text",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "skelett_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere dieser Beschwerden am "
                             "Bewegungsapparat?",
                    "hint": "Mehrfachauswahl möglich. Solche Beschwerden können auf eine "
                            "Fluorid-Einlagerung in den Knochen (Knochenfluorose) hinweisen.",
                    "required": True,
                    "options": [
                        {"value": "gelenkschmerzen", "label": "Rheuma-ähnliche Gelenk- oder Gliederschmerzen"},
                        {"value": "bleierne_schwere", "label": "»Bleierne Schwere« in Armen oder Beinen"},
                        {"value": "nacken", "label": "Schmerzen und Steifheit im Nacken"},
                        {"value": "ruecken", "label": "Rückenschmerzen, besonders bei Erschütterungen"},
                        {"value": "keine", "label": "Keine davon"},
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
                    "id": "lunge",
                    "type": "multi_choice",
                    "label": "Sind bei Ihnen Erkrankungen der Atemwege oder der Lunge bekannt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "copd", "label": "COPD oder chronische Bronchitis"},
                        {"value": "andere_lunge", "label": "Andere Lungenerkrankung (z. B. Lungenfibrose)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "lungen_frisch",
                    "type": "yes_no",
                    "label": "Hatten Sie in den letzten zwei Monaten eine inzwischen "
                             "ausgeheilte Erkrankung der Lunge oder des Rippenfells "
                             "(z. B. Lungenentzündung, Rippenfellentzündung)?",
                    "required": True,
                },
                {
                    "id": "herz_kreislauf",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Herz- oder Kreislauferkrankung bekannt, die "
                             "sich auf Ihren Kreislauf auswirkt (z. B. Herzschwäche, schwere "
                             "Herzrhythmusstörung)?",
                    "required": True,
                    "followup": {"id": "herz_kreislauf_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "ekzem",
                    "type": "yes_no",
                    "label": "Haben Sie Ekzeme (juckende, entzündliche Hautausschläge) – "
                             "aktuell oder immer wiederkehrend?",
                    "required": True,
                },
                {
                    "id": "skelett_erkrankung",
                    "type": "multi_choice",
                    "label": "Sind bei Ihnen Erkrankungen der Knochen, Gelenke oder der "
                             "Wirbelsäule bekannt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "knochen_tb", "label": "Knochentuberkulose (auch früher)"},
                        {"value": "rheumat_arthritis", "label": "Chronisch rheumatische Arthritis (Gelenkrheuma)"},
                        {"value": "bechterew", "label": "Morbus Bechterew (entzündliche Wirbelsäulenerkrankung)"},
                        {"value": "versteifung", "label": "Versteifungen der Wirbelsäule oder großer Gelenke"},
                        {"value": "andere_skelett", "label": "Andere Knochen- oder Gelenkerkrankung"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "unt_art", "in": ["nach"]},
                    "followup": {"id": "verdacht_zusammenhang_desc", "type": "textarea",
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
    # ── Dauernde gesundheitliche Bedenken (Abschnitt 2.1.1) ───────────────
    {"wenn": {"lunge": ["asthma", "copd", "andere_lunge"]},
     "schwere": "kritisch",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 2.1.1–2.1.3",
     "befund": "Atemwegs- oder Lungenerkrankung (Asthma bzw. mögliche obstruktive/"
               "restriktive Funktionseinschränkung) angegeben.",
     "konsequenz": "Ausprägung vor Aufnahme bzw. Fortsetzung der Tätigkeit klären: "
                   "Spirometrie durchführen, fachärztliche Vorbefunde einholen. Bei "
                   "Lungenerkrankung mit wesentlicher obstruktiver und/oder restriktiver "
                   "Funktionseinschränkung oder Asthma dauernde gesundheitliche Bedenken "
                   "(2.1.1); bei zu erwartender Wiederherstellung befristete Bedenken "
                   "(2.1.2); bei geringer Ausprägung keine Bedenken unter Voraussetzungen "
                   "(2.1.3: technische/organisatorische Schutzmaßnahmen, Einsatz mit "
                   "geringerer Exposition, PSA, verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"herz_kreislauf": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz/Kreislauf",
     "quelle": "Abschnitte 2.1.1–2.1.3",
     "befund": "Hämodynamisch wirksame Herz-/Kreislauferkrankung angegeben.",
     "konsequenz": "Vorbefunde einholen, ggf. kardiologische Abklärung veranlassen. Bei "
                   "hämodynamisch wirksamer Herz-/Kreislauferkrankung dauernde "
                   "gesundheitliche Bedenken (2.1.1); bei geringerer Ausprägung prüfen, ob "
                   "die Tätigkeit unter den Voraussetzungen nach 2.1.3 (Schutzmaßnahmen, "
                   "geringere Exposition, verkürzte Nachuntersuchungsfristen) möglich ist."},
    {"wenn": {"ekzem": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "Abschnitte 2.1.1–2.1.3",
     "befund": "Ekzeme angegeben.",
     "konsequenz": "Hautbefund erheben, ggf. dermatologisch abklären. Ekzeme zählen zu den "
                   "Erkrankungen mit dauernden gesundheitlichen Bedenken (2.1.1) – die "
                   "ätzenden, hautschädigenden Stoffe treffen auf vorgeschädigte Haut. Bei "
                   "weniger ausgeprägtem Befund Aufnahme/Fortsetzung nur unter den "
                   "Voraussetzungen nach 2.1.3 (insbesondere geeignete PSA unter Beachtung "
                   "des Hautzustands, verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"skelett_erkrankung": ["knochen_tb", "rheumat_arthritis", "bechterew", "versteifung"]},
     "schwere": "kritisch",
     "bereich": "Skelettsystem",
     "quelle": "Abschnitte 2.1.1–2.1.3",
     "befund": "Beurteilungsrelevante Skeletterkrankung angegeben (Knochentuberkulose, "
               "chronisch rheumatische Arthritis, Morbus Bechterew oder Versteifungen der "
               "Wirbelsäule/großer Gelenke).",
     "konsequenz": "Vorbefunde einholen, Beweglichkeit und Befund klären. Diese "
                   "Erkrankungen begründen dauernde gesundheitliche Bedenken (2.1.1), da "
                   "Fluoride das Skelettsystem zusätzlich schädigen (Osteosklerose). Bei "
                   "weniger ausgeprägten Formen prüfen, ob die Tätigkeit unter den "
                   "Voraussetzungen nach 2.1.3 möglich ist (Schutzmaßnahmen, geringere "
                   "Exposition, verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"lungen_frisch": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Rekonvaleszenz",
     "quelle": "Abschnitt 2.1.2 (befristete gesundheitliche Bedenken)",
     "befund": "Folgenlos abgeklungene Erkrankung der Lunge oder des Rippenfells in den "
               "letzten zwei Monaten angegeben.",
     "konsequenz": "Befristete gesundheitliche Bedenken für die Dauer von 1–2 Monaten nach "
                   "Abklingen der Erkrankung aussprechen (2.1.2); Aufnahme bzw. "
                   "Fortsetzung der Tätigkeit erst nach Fristablauf und erneuter "
                   "Beurteilung (Spirometrie kontrollieren)."},
    # ── Ergänzungsuntersuchung in unklaren Fällen (Abschnitt 1.2.3) ───────
    {"wenn": {"skelett_beschwerden": ["gelenkschmerzen", "bleierne_schwere", "nacken", "ruecken"]},
     "schwere": "pruefen",
     "bereich": "Verdacht Knochenfluorose",
     "quelle": "Abschnitte 1.2.1, 1.2.3 und 3.2.3",
     "befund": "Beschwerden am Bewegungsapparat angegeben (rheumatische Beschwerden, "
               "bleierne Schwere, Nackensteifheit oder Rückenschmerzen bei Erschütterung).",
     "konsequenz": "An eine Fluor-Osteosklerose (Knochenfluorose) denken: "
                   "Fluoridausscheidung im Urin bewerten (BGW 7,0 mg/g Kreatinin bei "
                   "Expositions-/Schichtende bzw. 4,0 mg/g Kreatinin vor der Folgeschicht). "
                   "Bei anamnestischem oder klinischem Verdacht Röntgendiagnostik des "
                   "Skelettsystems (Übersicht Becken und LWS, dorsolumbaler Übergang "
                   "seitlich, beide Unterarme), in unklaren Fällen ggf. Beckenkammpunktion "
                   "mit histologischer und mikroanalytischer Untersuchung (1.2.3)."},
    {"wenn": {"atemwege": ["husten", "auswurf", "atemgeraeusche", "atemnot"]},
     "schwere": "pruefen",
     "bereich": "Atemwegssymptome",
     "quelle": "Abschnitte 1.2.1–1.2.3",
     "befund": "Atemwegsbeschwerden (Husten, Auswurf, verschärfte Atemgeräusche oder "
               "Atemnot bei Bewegung) angegeben.",
     "konsequenz": "Spirometrie durchführen und bewerten; radiologische Diagnostik des "
                   "Thorax veranlassen, wenn das klinische Bild dies erfordert – "
                   "insbesondere nach Exposition gegenüber Fluor, Fluorwasserstoff, "
                   "Flusssäure oder sauer reagierenden Fluoriden (1.2.2/1.2.3)."},
    {"wenn": {"obstipation": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm",
     "quelle": "Abschnitt 1.2.1 (Zwischenanamnese)",
     "befund": "Obstipation (Verstopfung) angegeben.",
     "konsequenz": "Auf Obstipation ist bei diesem Anlass besonders zu achten: mögliche "
                   "chronische Fluoridwirkung bzw. orale Aufnahme (Hygiene!) klären, "
                   "Urinstatus und Fluorid-Biomonitoring bewerten; bei unklarem Befund "
                   "weitergehende ärztliche Abklärung."},
    {"wenn": {"reizung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Reizwirkung am Arbeitsplatz",
     "quelle": "Abschnitte 3.2.1 und 2.2",
     "befund": "Reizungen von Augen, Nase oder Atemwegen bei der Arbeit angegeben.",
     "konsequenz": "Hinweis auf relevante Exposition (örtlich ätzende Wirkung auf "
                   "Schleimhäute): Expositionssituation und Schutzmaßnahmen klären, "
                   "Spirometrie bewerten. Ergeben sich Hinweise, die eine Aktualisierung "
                   "der Gefährdungsbeurteilung notwendig machen, Mitteilung an den "
                   "Arbeitgeber unter Wahrung der schutzwürdigen Belange (2.2)."},
    {"wenn": {"haut_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 3.2.1 und 3.2.2",
     "befund": "Arbeitsbezogene Hautveränderungen angegeben (Rötung, Brennen, verzögert "
               "schmerzende Stellen).",
     "konsequenz": "An Flusssäure-Verätzungen denken – Schmerzen können erst Stunden nach "
                   "der Exposition auftreten, ohne dass zunächst Hautveränderungen sichtbar "
                   "sind. Haut ärztlich untersuchen, Expositionssituation klären; Beratung "
                   "zu Hautschutz und sofortiger Behandlung bei Kontakt."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle/Unfälle",
     "quelle": "Abschnitte 1.1, 1.2.3 und 4",
     "befund": "Unfall oder Zwischenfall mit Fluorverbindungen angegeben.",
     "konsequenz": "Hergang erfragen und dokumentieren; nach inhalativer Exposition "
                   "gegenüber Fluor, Fluorwasserstoff, Flusssäure oder sauer reagierenden "
                   "Fluoriden radiologische Diagnostik des Thorax erwägen (Fußnote zu "
                   "1.2.3). Vorzeitige Nachuntersuchung nach ärztlichem Ermessen (1.1); "
                   "bei Verdacht auf eine Erkrankung durch Fluor oder seine Verbindungen "
                   "BK-Anzeige prüfen (BK-Nr. 1308)."},
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenzeitliche Erkrankung",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen die Fortsetzung der "
                   "Tätigkeit geben könnte (1.1); Befunde und Behandlungsunterlagen "
                   "einholen und die Beurteilung nach 2.1 aktualisieren; ggf. verkürzte "
                   "Nachuntersuchungsfrist festlegen."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vermuteter Arbeitszusammenhang",
     "quelle": "Abschnitte 1.1 und 4",
     "befund": "Die versicherte Person vermutet einen Zusammenhang zwischen Beschwerden "
               "und der Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist hierfür ausdrücklich vorgesehen (1.1): "
                   "Beschwerden gezielt abklären (Spirometrie, Urinstatus, "
                   "Fluorid-Biomonitoring, ggf. Ergänzungsuntersuchung nach 1.2.3); bei "
                   "begründetem Verdacht auf eine Berufskrankheit Anzeige nach BK-Nr. 1308 "
                   "erstatten."},
    {"wenn": {"skelett_erkrankung": ["andere_skelett"]},
     "schwere": "pruefen",
     "bereich": "Skelettsystem",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Sonstige Knochen- oder Gelenkerkrankung angegeben.",
     "konsequenz": "Art und Ausmaß ärztlich klären (Vorbefunde, Beweglichkeit); prüfen, ob "
                   "ein Bedenkenstatbestand nach 2.1.1 (z. B. Versteifung) vorliegt oder "
                   "die Tätigkeit unter den Voraussetzungen nach 2.1.3 möglich ist."},
    {"wenn": {"psa_tragen": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Beim Umgang mit Fluorverbindungen wird keine Schutzausrüstung benutzt.",
     "konsequenz": "Eindringlich zu persönlicher Schutzausrüstung und allgemeinen "
                   "Hygienemaßnahmen beraten (2.2). Ergeben sich Hinweise, die eine "
                   "Aktualisierung der Gefährdungsbeurteilung zur Verbesserung des "
                   "Arbeitsschutzes notwendig machen, Mitteilung an den Arbeitgeber unter "
                   "Wahrung der schutzwürdigen Belange des Untersuchten."},
    # ── Hinweise und Beratung ─────────────────────────────────────────────
    {"wenn": {"psa_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 2.1.3 und 2.2",
     "befund": "Probleme beim Tragen der Schutzausrüstung angegeben.",
     "konsequenz": "PSA unter Beachtung des individuellen Gesundheitszustands auswählen "
                   "(2.1.3); Ursachen der Probleme klären und geeignete Alternativen "
                   "(z. B. anderes Handschuhmaterial, leichteres Atemschutzgerät) "
                   "empfehlen."},
    {"wenn": {"hygiene": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht oder nur teilweise eingehalten.",
     "konsequenz": "Auf allgemeine Hygienemaßnahmen hinweisen (2.2): Vermeiden oraler "
                   "Fluoridaufnahme, Händewaschen, Wechsel der Arbeitskleidung; Ursachen "
                   "klären und organisatorische Verbesserungen anregen."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Flusssäure-Gefährdung",
     "quelle": "Abschnitte 3.1.3 und 3.2",
     "befund": "Möglicher direkter Hautkontakt mit Flusssäure bzw. flusssäurehaltigen "
               "Lösungen angegeben.",
     "konsequenz": "Eingehend beraten: Flusssäure wird über die Haut erheblich resorbiert, "
                   "durchdringt die Haut und kann tiefe Gewebeschäden sowie bedrohliche "
                   "systemische Vergiftungen verursachen; auf konsequenten Hand-/Hautschutz "
                   "und sofortige Behandlung nach Kontakt hinweisen."},
    {"wenn": {"frueher_expo": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 1.2.2 und 3.1.4",
     "befund": "Frühere Tätigkeiten mit Fluorid-Exposition angegeben.",
     "konsequenz": "Frühere Expositionen in der Arbeitsanamnese dokumentieren und bei der "
                   "Bewertung des Fluorid-Basiswerts im Urin (Erstuntersuchung) sowie der "
                   "jährlichen Fluoridbestimmung (Nachuntersuchung, alle 12 Monate) "
                   "berücksichtigen."},
    {"wenn": {"expo_dauer": ["ueber10"]},
     "schwere": "hinweis",
     "bereich": "Langzeitexposition",
     "quelle": "Abschnitte 1.1, 1.2.2 und 3.2.3",
     "befund": "Mehr als 10 Jahre Tätigkeit mit Fluor bzw. Fluorverbindungen angegeben.",
     "konsequenz": "Bei langjähriger Exposition gezielt auf Zeichen einer Knochenfluorose "
                   "achten (rheumatische Beschwerden, Bewegungseinschränkung, erhöhte "
                   "Fluoridausscheidung); Nachuntersuchungsfrist von 12–24 Monaten und "
                   "jährliches Fluorid-Biomonitoring einhalten."},
]
