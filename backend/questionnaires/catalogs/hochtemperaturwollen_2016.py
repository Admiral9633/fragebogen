# -*- coding: utf-8 -*-
"""G 1.3 Mineralischer Staub, Teil 3: Künstlicher mineralischer Faserstaub der
Kategorie 1A oder 1B (z. B. Aluminiumsilikatwolle) – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016,
G 1.3 (Fassung Oktober 2014), S. 97–106."""

SLUG = "g1-3-hochtemperaturwollen-2016"

CATALOG = {
    "version": 2,
    "title": "G 1.3 Mineralischer Staub, Teil 3: Künstlicher mineralischer Faserstaub "
             "(Aluminiumsilikatwolle) (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 1.3 »Mineralischer Staub, Teil 3: Künstlicher mineralischer Faserstaub "
             "der Kategorie 1A oder 1B (z. B. Aluminiumsilikatwolle)« "
             "(Fassung Oktober 2014), S. 97–106",
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
                    "hint": "Nachgehende Untersuchung: Sie arbeiten nicht mehr mit diesen "
                            "Faserstäuben, werden aber weiterhin untersucht, weil "
                            "Erkrankungen erst nach vielen Jahren auftreten können.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich war schon einmal hier)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (Tätigkeit bereits beendet)"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Faserstaub-Belastung",
            "subtitle": "Ihre Arbeit mit künstlichem mineralischem Faserstaub",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "einsatzbereiche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie mit Faserwolle-Produkten "
                            "(Matten, Filzen, Platten, Formteilen)?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "ofen_feuerungsbau", "label": "Industrieller Ofen- und Feuerungsbau"},
                        {"value": "heizungsanlagen", "label": "Heizungsanlagen (Bereich des direkten Brennerflammenkontakts)"},
                        {"value": "abgasanlagen", "label": "Abgasanlagen in Kraftfahrzeugen (Lagermatten für Keramik-Substrate)"},
                        {"value": "hot_end", "label": "Wärmedämmung im Hot-End-Bereich"},
                        {"value": "rueckbau", "label": "Abbruch-, Sanierungs- oder Instandhaltungsarbeiten mit alter Mineralwolle"},
                        {"value": "sonstiges", "label": "Andere Bereiche mit Hochtemperaturwolle"},
                        {"value": "keine", "label": "Keine davon / Tätigkeit beginnt erst"},
                    ],
                },
                {
                    "id": "faserart",
                    "type": "multi_choice",
                    "label": "Mit welcher Art von Faserwolle haben Sie zu tun?",
                    "hint": "Die Angabe steht meist im Sicherheitsdatenblatt oder in Ihrer "
                            "Betriebsanweisung. Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "asw", "label": "Aluminiumsilikatwolle (ASW, »Keramikfasern«/RCF)"},
                        {"value": "aes", "label": "AES-Wolle (Erdalkalisilikatwolle, Hochtemperaturglaswolle)"},
                        {"value": "pcw", "label": "Polykristalline Wolle (PCW)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "expo_beginn",
                    "type": "choice",
                    "label": "Wie lange liegt der Beginn Ihrer Arbeit mit solchen Faserstäuben "
                            "zurück (auch frühere Arbeitsstellen mitzählen)?",
                    "hint": "Diese Angabe bestimmt mit, in welchen Abständen Sie untersucht "
                            "werden.",
                    "required": True,
                    "options": [
                        {"value": "beginnt_erst", "label": "Die Tätigkeit beginnt erst"},
                        {"value": "unter15", "label": "Weniger als 15 Jahre"},
                        {"value": "ueber15", "label": "15 Jahre oder länger"},
                    ],
                },
                {
                    "id": "alter_45",
                    "type": "yes_no",
                    "label": "Sind Sie 45 Jahre alt oder älter?",
                    "required": True,
                },
                {
                    "id": "expo_hoch",
                    "type": "yes_no",
                    "label": "Arbeiten Sie regelmäßig bei stark staubenden Arbeiten, z. B. "
                            "Ausbau alter Isolierungen, Zuschneiden oder Reparatur von "
                            "Faserwolle-Produkten?",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Frühere Staubbelastungen ───────────────────────────────────
        {
            "id": "fruehere_exposition",
            "title": "Frühere Staubbelastungen",
            "subtitle": "Andere Stäube, denen Sie früher oder zusätzlich ausgesetzt waren",
            "questions": [
                {
                    "id": "asbest",
                    "type": "yes_no",
                    "label": "Waren Sie jemals asbesthaltigen Stäuben ausgesetzt (z. B. "
                            "Asbestzement, Spritzasbest, alte Isolierungen, Bremsbeläge)?",
                    "required": True,
                    "followup": {"id": "asbest_desc", "type": "textarea",
                                 "label": "Bei welchen Tätigkeiten, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "quarz_fibrogen",
                    "type": "yes_no",
                    "label": "Waren Sie jemals quarzhaltigen oder anderen lungenbelastenden "
                            "(fibrogenen) Stäuben ausgesetzt (z. B. Sandstrahlen, Gießerei, "
                            "Steinbearbeitung, Bergbau)?",
                    "required": True,
                    "followup": {"id": "quarz_fibrogen_desc", "type": "textarea",
                                 "label": "Bei welchen Tätigkeiten, und wie lange?",
                                 "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Atemschutz bei staubenden Arbeiten",
            "questions": [
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei staubenden Arbeiten Atemschutz "
                            "(z. B. FFP-Maske)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_bedarf", "label": "Bei meiner Arbeit entsteht kein Staub / noch keine Tätigkeit"},
                    ],
                },
            ],
        },
        # ── 5 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Atemwegs-Beschwerden",
            "subtitle": "Aktuelle Beschwerden von Lunge und Atemwegen",
            "questions": [
                {
                    "id": "husten",
                    "type": "yes_no",
                    "label": "Haben Sie häufig oder anhaltend Husten?",
                    "required": True,
                    "followup": {"id": "husten_desc", "type": "text",
                                 "label": "Seit wann, und haben Sie dabei Auswurf (Schleim)?",
                                 "when": "yes"},
                },
                {
                    "id": "atemnot",
                    "type": "choice",
                    "label": "Haben Sie Atemnot (Luftnot)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "starke_belastung", "label": "Nur bei starker körperlicher Belastung"},
                        {"value": "leichte_belastung", "label": "Schon bei leichter Belastung (z. B. Treppensteigen)"},
                        {"value": "ruhe", "label": "Auch in Ruhe"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                            "mehrwöchige Erkrankung oder eine bleibende körperliche "
                            "Beeinträchtigung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                            "Beschwerden und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen von Lunge, Atemwegen, Herz und Kreislauf",
            "questions": [
                {
                    "id": "lunge_vorerkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Erkrankungen der Lunge oder "
                            "Atemwege festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "chron_bronchitis", "label": "Chronische (obstruktive) Bronchitis (dauerhafter Husten mit Auswurf)"},
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "emphysem", "label": "Lungenemphysem / COPD (Lungenüberblähung)"},
                        {"value": "staublunge", "label": "Staublunge, Lungenfibrose oder andere Vernarbung des Lungengewebes"},
                        {"value": "granulomatoes", "label": "Granulomatöse Lungenerkrankung (z. B. Sarkoidose)"},
                        {"value": "pleuritis", "label": "Rippenfellentzündung (Pleuritis), nicht sicher ausgeheilt"},
                        {"value": "tuberkulose", "label": "Tuberkulose (auch ausgeheilt)"},
                        {"value": "lungen_op", "label": "Operation oder Verletzung der Lunge (z. B. Teilentfernung)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "thorax_deform",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen eine Verformung des Brustkorbs oder der "
                            "Wirbelsäule, die das Atmen beeinträchtigt?",
                    "required": True,
                },
                {
                    "id": "herz_kreislauf",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Herz-Kreislauf-Erkrankungen "
                            "festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "herzinsuffizienz", "label": "Herzschwäche (Herzinsuffizienz)"},
                        {"value": "klappenfehler", "label": "Herzklappenfehler oder andere organische Herzerkrankung"},
                        {"value": "hypertonie_schlecht", "label": "Bluthochdruck, der trotz Behandlung schlecht einstellbar ist"},
                        {"value": "hypertonie_behandelt", "label": "Bluthochdruck, gut eingestellt"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "chronisch_sonstig",
                    "type": "yes_no",
                    "label": "Haben Sie sonstige chronische Erkrankungen, die Ihre "
                            "allgemeine Widerstandskraft herabsetzen (z. B. Zuckerkrankheit, "
                            "Immunschwäche, Tumorerkrankung)?",
                    "required": True,
                    "followup": {"id": "chronisch_sonstig_desc", "type": "textarea",
                                 "label": "Welche Erkrankung(en)?", "when": "yes"},
                },
            ],
        },
        # ── 7 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Ihr Tabakkonsum – wird nach dem Untersuchungsbogen "
                        "»Mineralischer Staub« detailliert erfasst",
            "questions": [
                {
                    "id": "raucher_status",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht (Nie-Raucher/in)"},
                        {"value": "ex", "label": "Früher ja, heute nicht mehr (Ex-Raucher/in)"},
                        {"value": "raucher", "label": "Ja, ich rauche (Raucher/in)"},
                    ],
                },
                {
                    "id": "rauch_waren",
                    "type": "multi_choice",
                    "label": "Was rauchen bzw. rauchten Sie?",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ex", "raucher"]},
                    "options": [
                        {"value": "zigaretten", "label": "Zigaretten"},
                        {"value": "zigarren", "label": "Zigarren/Zigarillos"},
                        {"value": "pfeife", "label": "Pfeife"},
                        {"value": "sonstiges", "label": "Sonstiges"},
                    ],
                },
                {
                    "id": "rauch_menge",
                    "type": "text",
                    "label": "Wie viel rauchen bzw. rauchten Sie ungefähr pro Tag, und seit "
                            "welchem Jahr (ggf. bis wann)?",
                    "hint": "Beispiel: »20 Zigaretten pro Tag, von 2000 bis 2014«.",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ex", "raucher"]},
                },
                {
                    "id": "packungsjahre",
                    "type": "choice",
                    "label": "Wie viele »Zigaretten-Packungsjahre« kommen ungefähr zusammen?",
                    "hint": "1 Packungsjahr = 1 Schachtel (20 Zigaretten) pro Tag über 1 Jahr.",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ex", "raucher"]},
                    "options": [
                        {"value": "unter10", "label": "Unter 10 Packungsjahre"},
                        {"value": "10bis20", "label": "10 bis 20 Packungsjahre"},
                        {"value": "ueber20", "label": "Mehr als 20 Packungsjahre"},
                        {"value": "unbekannt", "label": "Kann ich nicht einschätzen"},
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
    # ── Bedenkenstatbestände (Abschnitt 2.1.1) ────────────────────────────
    {"wenn": {"lunge_vorerkrankungen": ["chron_bronchitis", "asthma", "emphysem"]},
     "schwere": "kritisch",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 2.1.1 bis 2.1.3 (Kriterien)",
     "befund": "Chronische (obstruktive) Bronchitis, Asthma bronchiale oder "
               "Lungenemphysem/COPD angegeben.",
     "konsequenz": "Möglicher Tatbestand für dauernde gesundheitliche Bedenken (2.1.1): "
                   "Funktionsstörung durch Spirometrie objektivieren. Bei weniger "
                   "ausgeprägten Formen »keine Bedenken unter bestimmten Voraussetzungen« "
                   "(2.1.3) prüfen: Einsatz an Arbeitsplätzen mit nachgewiesen geringerer "
                   "Faserstaub-Konzentration, verkürzte Nachuntersuchungsfristen; im "
                   "Einzelfall messtechnische Überprüfung des Arbeitsplatzes veranlassen."},
    {"wenn": {"lunge_vorerkrankungen": ["staublunge", "granulomatoes"]},
     "schwere": "kritisch",
     "bereich": "Lungenfibrose/Staublunge",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Staublunge, Lungenfibrose bzw. granulomatöse Lungenveränderung angegeben.",
     "konsequenz": "Röntgenologisch fassbare Staublungen sowie fibrotische und "
                   "granulomatöse Veränderungen sind Bedenkenstatbestand: Vorbefunde und "
                   "Voraufnahmen (ILO-Klassifikation) beiziehen, Röntgen-Thorax p. a. "
                   "bewerten; dauernde oder befristete Bedenken (2.1.1/2.1.2) klären, "
                   "bevor die Tätigkeit aufgenommen oder fortgesetzt wird."},
    {"wenn": {"lunge_vorerkrankungen": ["tuberkulose", "pleuritis"]},
     "schwere": "kritisch",
     "bereich": "Tuberkulose/Pleuritis",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Tuberkulose bzw. nicht sicher ausgeheilte Pleuritis in der Vorgeschichte.",
     "konsequenz": "Aktive (auch geschlossene) und ausgedehnte inaktive Tuberkulose sowie "
                   "Zustand nach nicht sicher ausgeheilter Pleuritis sind "
                   "Bedenkenstatbestand: Aktivität und Ausheilung fachärztlich klären; "
                   "bei zu erwartender Wiederherstellung befristete Bedenken (2.1.2) "
                   "aussprechen und Nachuntersuchung vor Wiederaufnahme ansetzen."},
    {"wenn": {"lunge_vorerkrankungen": ["lungen_op"]},
     "schwere": "kritisch",
     "bereich": "Zustand nach Lungenresektion",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Operation oder Verletzung der Lunge in der Vorgeschichte.",
     "konsequenz": "Zustand nach Lungenresektion oder -verletzung mit "
                   "Funktionsbeeinträchtigung der Brustorgane ist Bedenkenstatbestand: "
                   "OP-Berichte einholen, Lungenfunktion prüfen; danach über dauernde, "
                   "befristete oder keine Bedenken unter Voraussetzungen entscheiden."},
    {"wenn": {"thorax_deform": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Thorax-/Wirbelsäulendeformität",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Verformung von Brustkorb oder Wirbelsäule mit Atembeeinträchtigung angegeben.",
     "konsequenz": "Bedenkenstatbestand nur, sofern die Atmung beeinträchtigt ist: "
                   "Spirometrie zur Objektivierung; bei relevanter Einschränkung Bedenken "
                   "nach 2.1.1/2.1.2 prüfen."},
    {"wenn": {"herz_kreislauf": ["herzinsuffizienz", "klappenfehler"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Herzinsuffizienz, Herzklappenfehler oder andere organische Herzerkrankung "
               "angegeben.",
     "konsequenz": "Manifeste oder vorzeitig zu erwartende Herzinsuffizienz (z. B. bei "
                   "gesichertem Herzklappenfehler) ist Bedenkenstatbestand: kardiologische "
                   "Vorbefunde einholen, Kreislauforgane untersuchen; erst danach "
                   "Beurteilung abschließen."},
    {"wenn": {"herz_kreislauf": ["hypertonie_schlecht"]},
     "schwere": "kritisch",
     "bereich": "Bluthochdruck",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Therapeutisch schlecht einstellbarer Bluthochdruck angegeben.",
     "konsequenz": "Bluthochdruck, insbesondere wenn therapeutisch nicht einstellbar, ist "
                   "Bedenkenstatbestand: aktuelle Blutdruckwerte erheben, "
                   "Therapieoptimierung veranlassen; bei zu erwartender Einstellung "
                   "befristete Bedenken (2.1.2) erwägen."},
    {"wenn": {"chronisch_sonstig": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allgemeine Widerstandskraft",
     "quelle": "Abschnitt 2.1.1 (dauernde gesundheitliche Bedenken)",
     "befund": "Sonstige chronische Erkrankung mit herabgesetzter Widerstandskraft angegeben.",
     "konsequenz": "Sonstige chronische Krankheiten, die die allgemeine Widerstandskraft "
                   "herabsetzen, können Bedenken begründen: Art und Schwere ärztlich "
                   "bewerten, ggf. Befunde der behandelnden Ärzte einholen."},
    # ── Beschwerden ───────────────────────────────────────────────────────
    {"wenn": {"husten": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Ablaufplan (In unklaren Fällen Ergänzungsuntersuchung) und Abschnitt 1.2.2",
     "befund": "Häufiger oder anhaltender Husten angegeben.",
     "konsequenz": "Im Rahmen der speziellen Untersuchung abklären (Spirometrie, "
                   "Röntgen-Thorax-Befund); in unklaren Fällen Ergänzungsuntersuchung "
                   "(z. B. Seitaufnahmen) nach Abschnitt 1.2.3 erwägen."},
    {"wenn": {"atemnot": ["leichte_belastung", "ruhe"]},
     "schwere": "kritisch",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 1.2.2, 1.2.3 und 2.1.1",
     "befund": "Atemnot bereits bei leichter Belastung oder in Ruhe angegeben.",
     "konsequenz": "Hinweis auf erhebliche Störung der Lungenfunktion oder des "
                   "Herz-Kreislauf-Systems (Bedenkenstatbestand 2.1.1): vollständige "
                   "Abklärung (Spirometrie, Röntgen-Thorax, ggf. Ergänzungsuntersuchung, "
                   "fachärztliche Vorstellung) vor Aufnahme bzw. Fortsetzung der Tätigkeit."},
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungen, vorzeitig)",
     "befund": "Schwere oder mehrwöchige Erkrankung bzw. körperliche Beeinträchtigung seit "
               "der letzten Untersuchung.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt: Erkrankung daraufhin "
                   "bewerten, ob sie Anlass zu Bedenken gegen die Fortsetzung der "
                   "Tätigkeit geben könnte; Umfang der Untersuchung nach ärztlichem "
                   "Ermessen erweitern."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Nachuntersuchungen, vorzeitig)",
     "befund": "Die versicherte Person vermutet einen Zusammenhang zwischen Erkrankung und "
               "Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen; Beschwerden dokumentieren und "
                   "arbeitsmedizinisch abklären. Ergibt sich der Verdacht auf einen "
                   "Arbeitsplatzbezug, Gefährdungsbeurteilung aktualisieren lassen "
                   "(Mitteilung an den Arbeitgeber unter Wahrung der schutzbedürftigen "
                   "Belange, Abschnitt 2.2)."},
    # ── Fristen, Latenz, nachgehende Untersuchungen ───────────────────────
    {"wenn": {"expo_beginn": ["ueber15"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist/Ergänzungsuntersuchung",
     "quelle": "Abschnitte 1.1 (Fristen) und 1.2.3 (Ergänzungsuntersuchung)",
     "befund": "Expositionsbeginn liegt 15 Jahre oder länger zurück.",
     "konsequenz": "Nachuntersuchungsfrist auf 36 Monate verkürzen (statt 60 Monate; "
                   "in Abhängigkeit von kumulativer Expositionshöhe, anderen "
                   "Faserexpositionen und Befund). Ergänzungsuntersuchung (Seitaufnahmen) "
                   "erwägen – Entscheidung abhängig von Latenzzeit ≥ 15 Jahre, Dauer und "
                   "Höhe der Exposition, Rauchgewohnheiten und Voraufnahmen. Erstmals "
                   "fällige nachgehende Untersuchungen beachten."},
    {"wenn": {"untersuchung_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitt 1.1 (Nachgehende Untersuchungen)",
     "befund": "Vorstellung zur nachgehenden Untersuchung nach Beendigung der Tätigkeit.",
     "konsequenz": "Nachgehende Untersuchungen erstmals 15 Jahre nach Expositionsbeginn "
                   "oder nach Vollendung des 45. Lebensjahres, danach alle 12–36 Monate "
                   "in Abhängigkeit von kumulativer Expositionshöhe und Befund. Die "
                   "Organisation erfolgt über die Gesundheitsvorsorge (GVS, "
                   "http://gvs.bgetem.de) – Anmeldung sicherstellen."},
    {"wenn": {"asbest": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Asbestexposition",
     "quelle": "Abschnitte 1.1 (Hinweis) und 1.2.1",
     "befund": "Frühere oder zusätzliche Exposition gegenüber asbesthaltigen Stäuben "
               "angegeben.",
     "konsequenz": "Eine wegen der (früheren) Asbestfaserstaub-Exposition vorgesehene "
                   "Untersuchung mit der Nachuntersuchung nach G 1.3 verbinden; "
                   "Asbestexposition in der Arbeitsanamnese differenziert dokumentieren "
                   "und bei Röntgenindikation/Seitaufnahmen berücksichtigen; nachgehende "
                   "Vorsorge über die GVS sicherstellen."},
    {"wenn": {"quarz_fibrogen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Quarz-/Staubexposition",
     "quelle": "Abschnitt 1.2.1 (Allgemeine Untersuchung)",
     "befund": "Frühere oder zusätzliche Exposition gegenüber quarzhaltigen oder anderen "
               "fibrogenen Stäuben angegeben.",
     "konsequenz": "Inhalative Vorbelastung differenziert erfassen und bei der Bewertung "
                   "von Röntgenbefunden und der Festlegung der Nachuntersuchungsfrist "
                   "(kumulative Belastung) berücksichtigen; ggf. Untersuchung nach G 1.1 "
                   "bzw. G 1.2 koordinieren."},
    # ── Faserart und Schutzmaßnahmen ──────────────────────────────────────
    {"wenn": {"faserart": ["aes", "pcw"]},
     "wenn_nicht": {"faserart": ["asw"]},
     "schwere": "hinweis",
     "bereich": "Faserart/Untersuchungsanlass",
     "quelle": "Abschnitt 3.1.1 (Vorkommen, Gefahrenquellen)",
     "befund": "Exposition (nur) gegenüber AES-Wolle bzw. polykristalliner Wolle angegeben.",
     "konsequenz": "AES-Wolle ist nicht als krebserzeugend eingestuft, polykristalline "
                   "Wolle gilt als krebsverdächtig (K3): Prüfen, ob statt G 1.3 eine "
                   "Untersuchung nach G 1.4 »Staubbelastung« ausreicht. Beachten: "
                   "AES-Fasern rekristallisieren bei Einsatztemperaturen über 900 °C zu "
                   "Cristobalit (Quarz-/Cristobalitfeinstäube Kategorie K1) – dann "
                   "Schutzmaßnahmen und ggf. G 1.1-Aspekte berücksichtigen."},
    {"wenn": {"faserart": ["unbekannt"]},
     "schwere": "hinweis",
     "bereich": "Faserart/Untersuchungsanlass",
     "quelle": "Vorbemerkungen und Abschnitt 3.1.1",
     "befund": "Faserart am Arbeitsplatz ist der untersuchten Person nicht bekannt.",
     "konsequenz": "Faserart über Gefährdungsbeurteilung, Sicherheitsdatenblätter bzw. die "
                   "Handlungsanleitung (DGUV Information 240-013) klären; davon hängt ab, "
                   "ob nach G 1.3 oder G 1.4 untersucht wird."},
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 2 und 2.2 (Beurteilung und Beratung)",
     "befund": "Atemschutz wird bei staubenden Arbeiten selten oder nie getragen.",
     "konsequenz": "Individuelle Aufklärung und Beratung zu Schutzmaßnahmen; ergeben sich "
                   "Hinweise, dass die Gefährdungsbeurteilung aktualisiert werden muss, "
                   "Mitteilung an den Arbeitgeber unter Wahrung der schutzbedürftigen "
                   "Belange der untersuchten Person."},
    # ── Rauchen ───────────────────────────────────────────────────────────
    {"wenn": {"raucher_status": ["raucher"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 1.2.1, 1.2.3 und 2.2 (Beratung)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung: Zigarettenrauchen ist die Hauptursache für Lungenkrebs; die "
                   "Kombination von Faserstäuben aus Aluminiumsilikatwolle und "
                   "Zigarettenrauchen hat vermutlich eine synergistische Wirkung. Auf die "
                   "Möglichkeit einer erfolgreichen Entwöhnungsbehandlung hinweisen; "
                   "Rauchgewohnheiten bei der Entscheidung über Ergänzungsuntersuchungen "
                   "(Seitaufnahmen) berücksichtigen."},
]
