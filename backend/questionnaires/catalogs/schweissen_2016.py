# -*- coding: utf-8 -*-
"""G 39 Schweißrauche – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 39 »Schweißrauche«
(Fassung Oktober 2014), S. 541–559."""

SLUG = "g39-schweissen-2016"

CATALOG = {
    "version": 2,
    "title": "G 39 Schweißrauche (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 39 »Schweißrauche« (Fassung Oktober 2014), S. 541–559",
    "sections": [
        # ── 1 ─ Anlass der Untersuchung ────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Erst- oder Nachuntersuchung nach G 39",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. "
                            "Nachuntersuchung: in der Regel nach 36 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung"},
                    ],
                },
                {
                    "id": "laengere_erkrankung",
                    "type": "yes_no",
                    "label": "Waren Sie seit der letzten Untersuchung mehrere Wochen am "
                             "Stück krank oder körperlich beeinträchtigt (z. B. durch eine "
                             "Bronchitis oder Lungenerkrankung)?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "laengere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wie lange?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung "
                             "bei Ihnen und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden bringen Sie mit der Arbeit "
                                          "in Verbindung?", "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Belastung",
            "subtitle": "Ihre Arbeit mit Schweiß-, Löt- und Schneidverfahren",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "verfahren",
                    "type": "multi_choice",
                    "label": "Mit welchen Verfahren arbeiten Sie (auch gelegentlich)?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "lbh", "label": "Lichtbogenhandschweißen (Stabelektroden)"},
                        {"value": "mig_mag", "label": "MIG-/MAG-Schutzgasschweißen (auch Fülldraht)"},
                        {"value": "wig", "label": "WIG-Schweißen"},
                        {"value": "autogen", "label": "Gasschweißen oder Brennschneiden (Autogenverfahren)"},
                        {"value": "laser_plasma", "label": "Laser- oder Plasmaschweißen/-schneiden"},
                        {"value": "spritzen", "label": "Thermisches Spritzen (Flamm-/Lichtbogen-/Plasmaspritzen)"},
                        {"value": "loeten", "label": "Löten (Weich- oder Hartlöten)"},
                        {"value": "widerstand", "label": "Punkt-/Widerstandsschweißen"},
                        {"value": "sonstige", "label": "Anderes Verfahren / weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "werkstoffe",
                    "type": "multi_choice",
                    "label": "Welche Werkstoffe bearbeiten Sie dabei?",
                    "hint": "Mehrfachauswahl möglich. Schauen Sie ggf. auf die Angaben "
                            "zu Ihren Zusatzwerkstoffen (Elektroden, Drähte, Lote).",
                    "required": True,
                    "options": [
                        {"value": "stahl_unlegiert", "label": "Unlegierter oder niedriglegierter Stahl (Baustahl)"},
                        {"value": "stahl_hochlegiert", "label": "Hochlegierter Stahl/Edelstahl "
                                                                "(Chrom-/Nickelanteil ab 5 %)"},
                        {"value": "aluminium", "label": "Aluminium oder Aluminiumlegierungen"},
                        {"value": "manganhaltig", "label": "Manganhaltige Werkstoffe oder Zusätze"},
                        {"value": "beschichtet", "label": "Beschichtete oder verunreinigte Teile (verzinkt, "
                                                          "lackiert, kunststoffbeschichtet, ölig)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "schweissanteil",
                    "type": "choice",
                    "label": "Wie viel Ihrer täglichen Arbeitszeit entfällt auf "
                             "Schweißarbeiten?",
                    "hint": "Der Grundsatz unterscheidet Vollzeitschweißer, Schweißer mit "
                            "erhöhtem Anteil an Nebenarbeiten und Gelegenheitsschweißer.",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "gelegentlich", "label": "Gelegenheitsschweißer: im Mittel bis 20 % "
                                                           "(ca. 1,5 Stunden pro Schicht)"},
                        {"value": "haeufig", "label": "Schweißen mit Nebenarbeiten: ca. 20–85 % der Arbeitszeit"},
                        {"value": "vollzeit", "label": "Vollzeitschweißer: mehr als 85 % der Arbeitszeit"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wie vielen Jahren arbeiten Sie insgesamt mit Schweiß-, "
                             "Löt- oder Schneidverfahren?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis10", "label": "1 bis 10 Jahre"},
                        {"value": "10bis20", "label": "10 bis 20 Jahre"},
                        {"value": "ueber20", "label": "Mehr als 20 Jahre"},
                    ],
                },
                {
                    "id": "enge_raeume",
                    "type": "yes_no",
                    "label": "Schweißen oder schneiden Sie in engen oder schlecht belüfteten "
                             "Räumen (z. B. Behälter, Silos, Doppelböden)?",
                    "required": True,
                },
                {
                    "id": "absaugung",
                    "type": "choice",
                    "label": "Gibt es an Ihrem Arbeitsplatz eine Absaugung oder Lüftung, "
                             "die den Rauch direkt an der Entstehungsstelle erfasst?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, und sie wird immer benutzt"},
                        {"value": "teilweise", "label": "Ja, aber nicht immer nutzbar/benutzt"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie beim Schweißen Atemschutzgeräte (z. B. belüfteten "
                             "Schweißerhelm, Maske, Gebläseatemschutz)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "teilweise", "label": "Nur bei bestimmten Arbeiten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_einsatz", "label": "Ich schweiße (noch) nicht"},
                    ],
                },
                {
                    "id": "frueher_schweissrauch",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Tätigkeiten bereits Schweiß- oder "
                             "Lötrauchen ausgesetzt?",
                    "required": True,
                    "followup": {"id": "frueher_schweissrauch_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Werkstoffe, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "frueher_aluminium",
                    "type": "yes_no",
                    "label": "Waren Sie früher gegenüber Aluminiumstaub oder "
                             "Aluminium-Schweißrauchen belastet (z. B. Aluminiumschweißen, "
                             "Arbeit mit Aluminiumpulver)?",
                    "required": True,
                    "followup": {"id": "frueher_aluminium_desc", "type": "text",
                                 "label": "Wo, und wie lange?", "when": "yes"},
                },
                {
                    "id": "frueher_staub",
                    "type": "yes_no",
                    "label": "Hatten Sie früher beruflich mit Asbest oder Quarzstaub zu tun "
                             "(z. B. Sandstrahlen, Bergbau, Abbrucharbeiten, alte Isolierungen)?",
                    "required": True,
                    "followup": {"id": "frueher_staub_desc", "type": "text",
                                 "label": "Was genau, und wie lange?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Atemwege & Beschwerden",
            "subtitle": "Beschwerden, die mit Schweißrauchen zusammenhängen können",
            "questions": [
                {
                    "id": "husten_auswurf",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Husten oder Auswurf (abgehusteter Schleim), "
                             "auch außerhalb von Erkältungen?",
                    "required": True,
                },
                {
                    "id": "atemnot",
                    "type": "choice",
                    "label": "Haben Sie Atemnot (Luftnot, Kurzatmigkeit)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "belastung", "label": "Ja, bei körperlicher Belastung (z. B. Treppensteigen)"},
                        {"value": "ruhe", "label": "Ja, schon in Ruhe"},
                    ],
                },
                {
                    "id": "pfeifen",
                    "type": "yes_no",
                    "label": "Haben Sie pfeifende oder brummende Atemgeräusche oder ein "
                             "Engegefühl in der Brust?",
                    "required": True,
                },
                {
                    "id": "reizung",
                    "type": "yes_no",
                    "label": "Haben Sie während oder nach dem Schweißen gereizte Augen, "
                             "eine gereizte Nase, Kratzen im Hals oder Hustenreiz?",
                    "required": True,
                },
                {
                    "id": "arbeitsbezug",
                    "type": "choice",
                    "label": "Falls Sie Atembeschwerden haben: Bessern sie sich an "
                             "arbeitsfreien Tagen, am Wochenende oder im Urlaub?",
                    "required": True,
                    "options": [
                        {"value": "keine_beschwerden", "label": "Ich habe keine Atembeschwerden"},
                        {"value": "besser", "label": "Ja, dann geht es mir besser"},
                        {"value": "gleich", "label": "Nein, die Beschwerden bleiben gleich"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "metallfieber",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal einige Stunden nach dem Schweißen "
                             "Fieber, Schüttelfrost, Gliederschmerzen oder Abgeschlagenheit "
                             "wie bei einer Grippe (»Metalldampffieber«)?",
                    "hint": "Typisch z. B. nach Arbeiten an verzinkten oder kupferhaltigen "
                            "Teilen; die Beschwerden klingen meist nach Stunden bis Tagen ab.",
                    "required": True,
                },
                {
                    "id": "neuro",
                    "type": "yes_no",
                    "label": "Haben Sie Zittern der Hände, Bewegungsstörungen oder auffällige "
                             "Vergesslichkeits- bzw. Konzentrationsprobleme bemerkt?",
                    "required": True,
                    "followup": {"id": "neuro_desc", "type": "text",
                                 "label": "Was genau, und seit wann?", "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen von Lunge, Atemwegen und Herz",
            "questions": [
                {
                    "id": "asthma",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Asthma bronchiale?",
                    "required": True,
                },
                {
                    "id": "copd",
                    "type": "yes_no",
                    "label": "Haben Sie eine chronische Bronchitis, COPD oder ein "
                             "Lungenemphysem (überblähte Lunge)?",
                    "required": True,
                },
                {
                    "id": "hyperreagibel",
                    "type": "yes_no",
                    "label": "Reagieren Ihre Atemwege seit mehr als 6 Monaten überempfindlich "
                             "(z. B. Husten- oder Atemnotanfälle durch kalte Luft, Staub, "
                             "Rauch oder Gerüche)?",
                    "required": True,
                },
                {
                    "id": "staublunge",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Staublunge, Silikose, Asbestose, "
                             "Lungenfibrose oder eine andere Vernarbung der Lunge "
                             "festgestellt?",
                    "required": True,
                    "followup": {"id": "staublunge_desc", "type": "text",
                                 "label": "Welche Diagnose, und wann?", "when": "yes"},
                },
                {
                    "id": "herz",
                    "type": "yes_no",
                    "label": "Haben Sie eine Herzschwäche (Herzinsuffizienz) oder eine "
                             "Herzerkrankung, die dazu führen kann (z. B. Herzinfarkt, "
                             "Herzklappenfehler)?",
                    "required": True,
                },
                {
                    "id": "akute_erkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie zurzeit eine akute Erkrankung der Atemwege "
                             "(z. B. akute Bronchitis, Lungenentzündung, Tuberkulose)?",
                    "required": True,
                },
                {
                    "id": "metallallergie",
                    "type": "yes_no",
                    "label": "Haben Sie eine bekannte Allergie gegen Metalle wie Chrom, "
                             "Nickel oder Cobalt (z. B. Hautausschlag, Atembeschwerden)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchgewohnheiten",
            "subtitle": "Detaillierte Erfassung des Tabakkonsums",
            "questions": [
                {
                    "id": "rauchstatus",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht (Nie-Raucher)"},
                        {"value": "ehemals", "label": "Früher ja, heute nicht mehr (Ex-Raucher)"},
                        {"value": "raucher", "label": "Ja (Raucher)"},
                    ],
                },
                {
                    "id": "rauchen_art",
                    "type": "multi_choice",
                    "label": "Was rauchen bzw. rauchten Sie?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "rauchstatus", "in": ["ehemals", "raucher"]},
                    "options": [
                        {"value": "zigaretten", "label": "Zigaretten"},
                        {"value": "zigarren", "label": "Zigarren/Zigarillos"},
                        {"value": "pfeife", "label": "Pfeife"},
                    ],
                },
                {
                    "id": "rauchen_menge",
                    "type": "text",
                    "label": "Wie viel pro Tag, seit welchem Jahr, und ggf. bis wann? "
                             "(z. B. »20 Zigaretten täglich seit 2005« – daraus werden die "
                             "Packungsjahre berechnet)",
                    "required": False,
                    "show_if": {"id": "rauchstatus", "in": ["ehemals", "raucher"]},
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
    # ── Bedenkenstatbestände nach 2.1.1 (dauernde gesundheitliche Bedenken) ─
    {"wenn": {"asthma": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Asthma bronchiale angegeben – bei manifester obstruktiver "
               "Atemwegserkrankung dauernde gesundheitliche Bedenken.",
     "konsequenz": "Erkrankung vor Beurteilung objektivieren (Spirometrie, ggf. "
                   "Bodyplethysmographie, Vorbefunde). Bei manifester Erkrankung dauernde "
                   "gesundheitliche Bedenken (2.1.1); bei geringer Ausprägung nach 2.1.3 "
                   "prüfen, ob unter bestimmten Voraussetzungen keine Bedenken bestehen – "
                   "dazu Höhe und Dauer der Exposition ermitteln und berücksichtigen."},
    {"wenn": {"copd": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 2.1.1, 2.1.3 und 3.2.2",
     "befund": "Chronische Bronchitis/COPD/Emphysem angegeben – Schweißrauche können eine "
               "vorbestehende Bronchialerkrankung akut und dauerhaft verschlimmern.",
     "konsequenz": "Lungenfunktion objektivieren; fortgesetzter Verlust von FEV1 oder VC "
                   "um mehr als 30 ml/Jahr über dem Altersgang begründet dauernde Bedenken "
                   "(2.1.1). Bei weniger ausgeprägtem Befund Vorgehen nach 2.1.3 "
                   "(Expositionshöhe/-dauer ermitteln, engmaschige Verlaufskontrolle)."},
    {"wenn": {"hyperreagibel": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Bronchiale Hyperreagibilität",
     "quelle": "Abschnitte 1.2.3 und 2.1.1",
     "befund": "Hinweis auf bronchiale Überempfindlichkeit über mehr als 6 Monate.",
     "konsequenz": "Ergänzungsuntersuchung veranlassen (erweiterte Lungenfunktions"
                   "diagnostik, unspezifischer Inhalationstest). Bei klinisch manifester, "
                   "irreversibler Hyperreagibilität länger als 6 Monate dauernde "
                   "gesundheitliche Bedenken (2.1.1)."},
    {"wenn": {"staublunge": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Pneumokoniose",
     "quelle": "Abschnitte 1.2.2, 1.2.3 und 2.1.1",
     "befund": "Staublunge/Silikose/Asbestose/Lungenfibrose in der Vorgeschichte angegeben.",
     "konsequenz": "Röntgen-Thorax p. a. (bei Erstuntersuchung Standardprogramm) mit "
                   "Voraufnahmen vergleichen; ggf. Seitaufnahme als Ergänzungs"
                   "untersuchung. Bei objektivierbarer Staublunge, Silikose (1/1 und "
                   "mehr), Asbestose (1/0–1/1 und mehr) oder anderen fibrotischen "
                   "Veränderungen dauernde gesundheitliche Bedenken (2.1.1)."},
    {"wenn": {"herz": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 2.1.1",
     "befund": "Herzinsuffizienz bzw. Erkrankung mit Risiko einer Herzinsuffizienz angegeben.",
     "konsequenz": "Kardiale Vorbefunde einholen und Schweregrad klären. Bei bestehender "
                   "Herzinsuffizienz oder Krankheiten, die häufig dazu führen, dauernde "
                   "gesundheitliche Bedenken (2.1.1); bei geringer Ausprägung Vorgehen "
                   "nach 2.1.3."},
    # ── Befristete Bedenken / Fristen (2.1.2 und 1.1) ─────────────────────
    {"wenn": {"akute_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Atemwegserkrankung",
     "quelle": "Abschnitt 2.1.2",
     "befund": "Aktuell akute Erkrankung der Atemwege (z. B. akute Bronchitis, "
               "Lungenentzündung, TBC) angegeben.",
     "konsequenz": "Befristete gesundheitliche Bedenken bis zur Ausheilung aussprechen; "
                   "Untersuchung (insbesondere Spirometrie) nach Abklingen wiederholen "
                   "und erst dann abschließend beurteilen."},
    {"wenn": {"laengere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Mehrwöchige Erkrankung bzw. körperliche Beeinträchtigung seit der letzten "
               "Untersuchung angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt (insbesondere bei "
                   "Beschwerden, die auf eine Bronchial- oder Lungenerkrankung hindeuten); "
                   "Krankheitsverlauf dokumentieren und prüfen, ob Bedenken gegen die "
                   "Fortsetzung der Tätigkeit bestehen."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Die untersuchte Person vermutet einen Zusammenhang zwischen Erkrankung "
               "und Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen; Beschwerden und "
                   "Arbeitsplatzbezug dokumentieren, ggf. Berufskrankheiten-Verdacht "
                   "(BK 1103, 4106, 4109, 4115, 4301, 4302) prüfen und melden."},
    # ── Aluminium (1.1, 1.2.2, 2.1.2/2.1.3) ───────────────────────────────
    {"wenn": {"werkstoffe": ["aluminium"]},
     "schwere": "pruefen",
     "bereich": "Aluminium-Biomonitoring",
     "quelle": "Abschnitte 1.1, 1.2.3 und 2.1.2",
     "befund": "Exposition gegenüber aluminiumhaltigen Schweißrauchen angegeben.",
     "konsequenz": "Aluminiumkonzentration im Urin bestimmen. Bei Überschreitung des BGW "
                   "von 200 µg Aluminium/l Urin (60 µg/g Kreatinin) befristete "
                   "gesundheitliche Bedenken (2.1.2), engmaschige Kontrolle der "
                   "Aluminiumkonzentration und vorzeitige Nachuntersuchung spätestens "
                   "binnen 3 Monaten; bei längerer BGW-Überschreitung HRCT zur "
                   "Aluminose-Frühdiagnose im Einzelfall erwägen."},
    {"wenn": {"frueher_aluminium": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Aluminiumbelastung",
     "quelle": "Abschnitt 1.2.2 (Spezielle Untersuchung, Erstuntersuchung)",
     "befund": "Anamnestische Hinweise auf eine vorausgegangene Aluminiumbelastung.",
     "konsequenz": "Bereits bei der Erstuntersuchung die Aluminiumkonzentration im Urin "
                   "bestimmen; bei auffälligen Werten weitere Abklärung (ggf. HRCT) und "
                   "engmaschige Kontrolle."},
    {"wenn": {"enge_raeume": ["yes"], "werkstoffe": ["aluminium"]},
     "schwere": "pruefen",
     "bereich": "Ungünstige Expositionsbedingungen",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Aluminiumschweißen unter ungünstigen Expositionsbedingungen "
               "(enge Räume) – rascher Anstieg der Aluminiumbelastung möglich.",
     "konsequenz": "Vorzeitige Nachuntersuchung spätestens binnen 3 Monaten einplanen; "
                   "engmaschiges Biomonitoring des Aluminiums im Urin."},
    # ── Chrom/Nickel, weitere Grundsätze (1.2.2, 3.1.4, 3.3) ──────────────
    {"wenn": {"werkstoffe": ["stahl_hochlegiert"]},
     "schwere": "pruefen",
     "bereich": "Biomonitoring Chrom/Nickel",
     "quelle": "Abschnitte 1.2.2, 3.1.4 und 3.3",
     "befund": "Arbeiten an hochlegiertem (chrom-/nickelhaltigem) Stahl angegeben – "
               "Rauche können kanzerogene Chrom(VI)-Verbindungen und Nickeloxide enthalten.",
     "konsequenz": "Biomonitoring von Chrom und Nickel durchführen (erwünscht bei "
                   "Nachuntersuchungen; EKA-Werte der MAK-/BAT-Liste). Grundsätze G 15 "
                   "»Chrom-VI-Verbindungen« und G 38 »Nickel« einbeziehen (DGUV "
                   "Information 250-415); erhöhtes Lungenkrebsrisiko bei mehrjähriger "
                   "höherer Exposition (Latenz ca. 20 Jahre) in der Beratung berücksichtigen."},
    {"wenn": {"frueher_staub": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Staubexposition",
     "quelle": "Abschnitte 2.1.1 und 3.3",
     "befund": "Frühere Exposition gegenüber Asbest oder Quarzstaub angegeben.",
     "konsequenz": "Grundsätze G 1.1 »Mineralischer Staub, Teil 1: Silikogener Staub« "
                   "bzw. G 1.4 einbeziehen; Röntgenbefund gezielt auf Silikose/Asbestose "
                   "prüfen (Bedenkenstatbestände nach 2.1.1). Mehrfachuntersuchungen "
                   "durch Kombination der Grundsätze vermeiden."},
    {"wenn": {"atemschutz": ["immer", "teilweise"]},
     "schwere": "hinweis",
     "bereich": "Atemschutzgeräte",
     "quelle": "Abschnitt 3.3 (Bemerkungen)",
     "befund": "Beim Schweißen werden Atemschutzgeräte getragen.",
     "konsequenz": "Prüfen, ob zusätzlich eine Untersuchung nach G 26 »Atemschutzgeräte« "
                   "erforderlich ist; zur Vermeidung von Mehrfachuntersuchungen mit dieser "
                   "Untersuchung kombinieren."},
    # ── Beschwerden und Schutzmaßnahmen ───────────────────────────────────
    {"wenn": {"husten_auswurf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 1.2.3 und 3.2.2/3.2.3",
     "befund": "Chronischer Husten/Auswurf angegeben (mögliches Frühzeichen einer "
               "chronischen Bronchitis oder Pneumokoniose).",
     "konsequenz": "Spirometrie sorgfältig bewerten; in begründeten Fällen "
                   "Ergänzungsuntersuchung (Bodyplethysmographie, ggf. vorgezogene "
                   "Röntgenuntersuchung bei spezieller Indikation)."},
    {"wenn": {"atemnot": ["ruhe"]},
     "schwere": "kritisch",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 2.1.1 und 3.2.3",
     "befund": "Atemnot bereits in Ruhe angegeben – Hinweis auf fortgeschrittene Lungen- "
               "oder Herzerkrankung.",
     "konsequenz": "Vor einer Beurteilung ohne Bedenken vollständige Abklärung "
                   "(Lungenfunktion, Röntgen, kardiale Diagnostik); je nach Befund "
                   "dauernde oder befristete gesundheitliche Bedenken nach 2.1.1/2.1.2."},
    {"wenn": {"arbeitsbezug": ["besser"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug der Beschwerden",
     "quelle": "Abschnitte 2 und 3.2.2",
     "befund": "Atembeschwerden bessern sich in arbeitsfreien Zeiten – Hinweis auf "
               "chemisch-irritative Wirkung der Schweißrauche.",
     "konsequenz": "Arbeitsplatzverhältnisse und Schutzmaßnahmen anhand der "
                   "Gefährdungsbeurteilung klären (technisch, organisatorisch, "
                   "personenbezogen); Beschwerdeverlauf dokumentieren, ggf. vorgezogene "
                   "Nachuntersuchung."},
    {"wenn": {"metallfieber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Metalldampffieber",
     "quelle": "Abschnitte 3.2.2 und 3.2.2.1",
     "befund": "Grippeähnliche Beschwerden Stunden nach dem Schweißen (V. a. "
               "Metalldampffieber, z. B. durch Zink- oder Kupferoxide).",
     "konsequenz": "Auslösende Tätigkeit und Werkstoffe klären; darüber aufklären, dass "
                   "nach längerer Arbeitskarenz mit dem Wiederaufleben der Beschwerden "
                   "bei erneuter Exposition zu rechnen ist. Expositionsminderung "
                   "(Absaugung, Atemschutz) veranlassen."},
    {"wenn": {"neuro": ["yes"], "werkstoffe": ["manganhaltig"]},
     "schwere": "pruefen",
     "bereich": "Neurotoxizität (Mangan)",
     "quelle": "Abschnitte 3.2.1, 3.2.3.3 und 3.3",
     "befund": "Neurologische Symptome (Zittern, Bewegungs-, Konzentrations- oder "
               "Gedächtnisstörungen) bei Arbeit mit manganhaltigen Werkstoffen/Zusätzen.",
     "konsequenz": "Weitere Untersuchungen wegen möglicher Symptome durch "
                   "Manganbelastung veranlassen (neurologische Abklärung); "
                   "Manganexposition über die Gefährdungsbeurteilung klären."},
    # ── Beratung (2.2) ────────────────────────────────────────────────────
    {"wenn": {"rauchstatus": ["raucher"]},
     "schwere": "hinweis",
     "bereich": "Tabakkonsum",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung nach 2.2: Zigarettenrauchen ist die Hauptursache für "
                   "Lungenkrebs und chronisch-obstruktive Atemwegserkrankungen; auf die "
                   "Verbesserung der Lungenfunktion und die Senkung des Krebsrisikos "
                   "durch Rauchverzicht sowie auf die Möglichkeit einer erfolgreichen "
                   "Entwöhnungsbehandlung hinweisen; Packungsjahre dokumentieren."},
]
