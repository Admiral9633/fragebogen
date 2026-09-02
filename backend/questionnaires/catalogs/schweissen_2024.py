# -*- coding: utf-8 -*-
"""Schweißen und Trennen von Metallen – DGUV Empfehlung 2024. Quelle: DGUV
Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen,
1. Auflage 2024, Kapitel »Schweißen und Trennen von Metallen« (E STM,
Fassung Januar 2022), S. 540–565."""

SLUG = "schweissen-2024"

CATALOG = {
    "version": 2,
    "title": "Schweißen und Trennen von Metallen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Schweißen und Trennen von Metallen« (E STM, "
             "Fassung Januar 2022), S. 540–565",
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
                             "Schweißrauchen (Schweißen und Trennen von Metallen)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zu dieser Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn am "
                            "Arbeitsplatz mehr als 3 Milligramm Schweißrauch pro Kubikmeter "
                            "Luft auftreten. Angebotsvorsorge: wenn dieser Wert eingehalten "
                            "wird. Wunschvorsorge: auf Ihren eigenen Wunsch.",
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
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Belastung",
            "subtitle": "Ihre Arbeit mit Schweiß-, Löt- und Schneidverfahren",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
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
                        {"value": "mig_mag", "label": "MIG-/MAG-Schweißen (Schutzgas, auch Fülldraht)"},
                        {"value": "wig", "label": "WIG-Schweißen"},
                        {"value": "autogen", "label": "Gasschweißen oder Brennschneiden (Autogenverfahren)"},
                        {"value": "laser_plasma", "label": "Laser- oder Plasmaschweißen/-schneiden"},
                        {"value": "spritzen", "label": "Thermisches Spritzen (Flamm-/Lichtbogenspritzen)"},
                        {"value": "loeten", "label": "Löten (Weich-, Hart- oder Hochtemperaturlöten)"},
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
                        {"value": "stahl_hochlegiert", "label": "Hochlegierter Stahl/Edelstahl (chrom-/nickelhaltig)"},
                        {"value": "aluminium", "label": "Aluminium oder Aluminiumlegierungen"},
                        {"value": "manganhaltig", "label": "Manganhaltige Werkstoffe oder Zusätze"},
                        {"value": "beschichtet", "label": "Beschichtete oder verunreinigte Teile (verzinkt, "
                                                          "lackiert, kunststoffbeschichtet, ölig)"},
                        {"value": "blei_cadmium", "label": "Blei- oder cadmiumhaltige Lote/Werkstoffe"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "schweissanteil",
                    "type": "choice",
                    "label": "Wie viel Ihrer täglichen Arbeitszeit entfällt auf Schweißen, "
                             "Löten oder thermisches Schneiden?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "gelegentlich", "label": "Gelegentlich (bis ca. 20 %, etwa 1,5 Stunden pro Schicht)"},
                        {"value": "haeufig", "label": "Häufig (ca. 20–85 % der Arbeitszeit)"},
                        {"value": "vollzeit", "label": "Fast durchgehend (mehr als 85 % der Arbeitszeit)"},
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
                    "label": "Tragen Sie beim Schweißen Atemschutz (z. B. belüfteten "
                             "Schweißerhelm, FFP-Maske, Gebläseatemschutz)?",
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
                             "wie bei einer Grippe (»Metallrauchfieber«)?",
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
            "subtitle": "Tabak- und Nikotinkonsum",
            "questions": [
                {
                    "id": "rauchstatus",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "ehemals", "label": "Früher ja, heute nicht mehr"},
                        {"value": "regelmaessig", "label": "Ja, regelmäßig"},
                    ],
                },
                {
                    "id": "rauchen_art",
                    "type": "multi_choice",
                    "label": "Was rauchen bzw. rauchten Sie?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "rauchstatus", "in": ["ehemals", "regelmaessig"]},
                    "options": [
                        {"value": "zigaretten", "label": "Zigaretten"},
                        {"value": "zigarren", "label": "Zigarren/Zigarillos"},
                        {"value": "pfeife", "label": "Pfeife"},
                        {"value": "ezigarette", "label": "E-Zigarette"},
                        {"value": "shisha", "label": "Shisha/Wasserpfeife"},
                    ],
                },
                {
                    "id": "rauchen_menge",
                    "type": "text",
                    "label": "Wie viel pro Tag, seit welchem Jahr, und ggf. bis wann? "
                             "(z. B. »20 Zigaretten täglich seit 2010«)",
                    "required": False,
                    "show_if": {"id": "rauchstatus", "in": ["ehemals", "regelmaessig"]},
                },
            ],
        },
        # ── 6 ─ Impfschutz ─────────────────────────────────────────────────
        {
            "id": "impfschutz",
            "title": "Impfschutz",
            "subtitle": "Pneumokokken-Impfung für Schweißerinnen und Schweißer",
            "questions": [
                {
                    "id": "pneumokokken",
                    "type": "choice",
                    "label": "Sind Sie gegen Pneumokokken (bakterielle Lungenentzündung) "
                             "geimpft?",
                    "hint": "Für Personen, die schweißen oder Metalle trennen, ist eine "
                            "Pneumokokken-Impfung Bestandteil der arbeitsmedizinischen "
                            "Vorsorge (AMR 6.7).",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
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
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"asthma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 7.4 und 7.4.2/7.4.4",
     "befund": "Asthma bronchiale angegeben (beurteilungsrelevante Erkrankung nach 7.4).",
     "konsequenz": "Erkrankung objektivieren (Spirometrie, in begründeten Fällen "
                   "Bodyplethysmographie); Vorbefunde einholen. Prüfen, ob die Tätigkeit "
                   "ohne gesundheitliche Gefährdung möglich ist; Maßnahmen nach 7.4.2 "
                   "erwägen (Substitution, technische/organisatorische Schutzmaßnahmen, "
                   "Expositionsbegrenzung, Einsatz an Arbeitsplätzen mit geringerer "
                   "Exposition). Ohne Aussicht auf Erfolg Tätigkeitswechsel nach 7.4.4 "
                   "erwägen (Mitteilung an den Arbeitgeber nur mit Einwilligung)."},
    {"wenn": {"copd": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 6.3.2, 7.4 und 7.4.2",
     "befund": "Chronische Bronchitis/COPD/Emphysem angegeben; Schweißrauche können eine "
               "vorbestehende Bronchialerkrankung akut verschlimmern.",
     "konsequenz": "Lungenfunktion sorgfältig bewerten (Verlust von FEV1/VC > 30 ml/Jahr "
                   "über dem Altersgang ist beurteilungsrelevant); Höhe und Dauer der "
                   "Exposition ermitteln. Maßnahmen nach 7.4.2 prüfen, bei fehlendem "
                   "Erfolg Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"hyperreagibel": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Hinweis auf bronchiale Überempfindlichkeit (länger als 6 Monate).",
     "konsequenz": "Erweiterte Lungenfunktionsdiagnostik veranlassen (z. B. "
                   "Bodyplethysmographie, unspezifischer Inhalationstest zur Abklärung "
                   "der bronchialen Überempfindlichkeit). Bei klinisch manifester, "
                   "irreversibler Hyperreagibilität Beurteilung nach 7.4 mit Maßnahmen "
                   "nach 7.4.2/7.4.4."},
    {"wenn": {"staublunge": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Pneumokoniose",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Staublunge/Silikose/Asbestose/Lungenfibrose in der Vorgeschichte angegeben.",
     "konsequenz": "Vorbefunde und Voraufnahmen anfordern; Röntgen-Thorax p. a. bei "
                   "spezieller Indikation (Aufnahmen bis 1 Jahr alt können berücksichtigt "
                   "werden), ggf. Seitaufnahme. Beurteilung nach 7.4 (Silikose ab 1/1, "
                   "Asbestose ab 1/0–1/1 beurteilungsrelevant); Maßnahmen nach "
                   "7.4.2/7.4.4 prüfen."},
    {"wenn": {"herz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 7.4",
     "befund": "Herzinsuffizienz bzw. Erkrankung mit Risiko einer Herzinsuffizienz angegeben.",
     "konsequenz": "Kardiale Vorbefunde einholen und Ausmaß klären; beurteilungsrelevante "
                   "Erkrankung nach 7.4. Prüfen, ob die Tätigkeit ohne gesundheitliche "
                   "Gefährdung möglich ist; ggf. Maßnahmen nach 7.4.2."},
    {"wenn": {"akute_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Atemwegserkrankung",
     "quelle": "Abschnitte 7.4 und 7.4.3",
     "befund": "Aktuell akute Erkrankung der Atemwege (z. B. akute Bronchitis, "
               "Lungenentzündung, TBC) angegeben.",
     "konsequenz": "Verkürzte Vorsorgefrist nach 7.4.3 empfehlen, da eine Änderung des "
                   "Schweregrades zu erwarten ist; Untersuchung (Spirometrie) ggf. erst "
                   "nach Ausheilung sinnvoll bewerten. Nächsten Vorsorgetermin auf der "
                   "Bescheinigung entsprechend früher ansetzen."},
    {"wenn": {"atemnot": ["ruhe"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 6.3.3 und 7.4",
     "befund": "Atemnot bereits in Ruhe angegeben.",
     "konsequenz": "Hinweis auf fortgeschrittene Lungen- oder Herzerkrankung: erweiterte "
                   "Lungenfunktionsdiagnostik und ärztliche Abklärung vor Fortsetzung der "
                   "Tätigkeit; Beurteilung nach 7.4, Maßnahmen nach 7.4.2/7.4.4 prüfen."},
    {"wenn": {"husten_auswurf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 6.3.2/6.3.3 und 7.2.2",
     "befund": "Chronischer Husten/Auswurf angegeben (mögliches Frühzeichen einer "
               "chronischen Bronchitis oder Pneumokoniose).",
     "konsequenz": "Spirometrie sorgfältig bewerten; in begründeten Fällen erweiterte "
                   "Lungenfunktionsdiagnostik. Rechtfertigende Indikation für eine "
                   "Röntgenaufnahme des Thorax anhand der Anamnese im Einzelfall prüfen."},
    {"wenn": {"arbeitsbezug": ["besser"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug der Beschwerden",
     "quelle": "Abschnitte 6.3.2 und 8.2",
     "befund": "Atembeschwerden bessern sich in arbeitsfreien Zeiten – Hinweis auf "
               "chemisch-irritative Wirkung der Schweißrauche.",
     "konsequenz": "Arbeitsplatzbezug klären (Verfahren, Werkstoffe, Lüftung); ergeben "
                   "sich Anhaltspunkte, dass die Schutzmaßnahmen nicht ausreichen, "
                   "Mitteilung an das Unternehmen und Vorschlag von Schutzmaßnahmen "
                   "(§ 6 (4) ArbMedVV)."},
    {"wenn": {"metallfieber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Metallrauchfieber",
     "quelle": "Abschnitte 6.3.2 und 6.3.2.1",
     "befund": "Grippeähnliche Beschwerden Stunden nach dem Schweißen (V. a. "
               "Metallrauchfieber, z. B. durch Zink- oder Kupferoxide).",
     "konsequenz": "Auslösende Tätigkeit und Werkstoffe (verzinkte/kupferhaltige Teile) "
                   "klären; über Krankheitsbild und das Wiederaufleben der Beschwerden "
                   "nach längerer Arbeitskarenz aufklären. Expositionsminderung mit dem "
                   "Unternehmen besprechen (Absaugung, Atemschutz)."},
    {"wenn": {"neuro": ["yes"], "werkstoffe": ["manganhaltig"]},
     "schwere": "pruefen",
     "bereich": "Neurotoxizität (Mangan)",
     "quelle": "Abschnitte 6.3.1 und 6.3.3.3",
     "befund": "Neurologische Symptome (Zittern, Bewegungs-, Konzentrations- oder "
               "Gedächtnisstörungen) bei Arbeit mit manganhaltigen Werkstoffen/Zusätzen.",
     "konsequenz": "Bei Lichtbogenverfahren mit Mangananteilen > 5 % sind neurotoxische "
                   "Effekte möglich: neurologische Abklärung veranlassen und "
                   "Manganexposition über die Gefährdungsbeurteilung klären."},
    # ── Biomonitoring (Abschnitte 6.4 und 7.2.2) ──────────────────────────
    {"wenn": {"werkstoffe": ["aluminium"]},
     "schwere": "pruefen",
     "bereich": "Biomonitoring Aluminium",
     "quelle": "Abschnitte 7.2.2, 7.4.2 und 7.4.3",
     "befund": "Exposition gegenüber aluminiumhaltigen Schweißrauchen angegeben.",
     "konsequenz": "Bei Nachuntersuchungen Biomonitoring von Aluminium im Urin. Bei "
                   "Überschreitung des BGW von 200 µg Aluminium/l Urin (60 µg/g Kreatinin) "
                   "engmaschige Kontrolle der Aluminiumkonzentration und verkürzte "
                   "Vorsorgefrist nach 7.4.3; bei längerfristiger BGW-Überschreitung "
                   "HRCT zur Aluminose-Frühdiagnose im Einzelfall erwägen."},
    {"wenn": {"werkstoffe": ["stahl_hochlegiert"]},
     "schwere": "pruefen",
     "bereich": "Biomonitoring Chrom/Nickel",
     "quelle": "Abschnitte 6.3.3.2, 6.4 und 7.2.2",
     "befund": "Arbeiten an hochlegiertem (chrom-/nickelhaltigem) Stahl angegeben – "
               "Rauche können kanzerogene Chrom(VI)-Verbindungen und Nickeloxide enthalten.",
     "konsequenz": "Bei Nachuntersuchungen Biomonitoring von Chrom und Nickel "
                   "durchführen (TRGS 903, EKA-Werte); über Art, Umfang und Prozedere "
                   "aufklären. Bei mehrjähriger höherer Exposition (DGUV Information "
                   "250-415) erhöhtes Lungenkrebsrisiko (Latenz ca. 20 Jahre) in der "
                   "Beratung berücksichtigen; strenge Expositionsminimierung anmahnen."},
    {"wenn": {"werkstoffe": ["blei_cadmium"]},
     "schwere": "pruefen",
     "bereich": "Biomonitoring Blei/Cadmium",
     "quelle": "Abschnitte 6 (Löten) und 7.2.2",
     "befund": "Arbeiten mit blei- oder cadmiumhaltigen Loten/Werkstoffen angegeben.",
     "konsequenz": "Bei Nachuntersuchungen Biomonitoring von Blei bzw. Cadmium "
                   "durchführen; Hygienemaßnahmen (kein Essen/Trinken am Arbeitsplatz, "
                   "Händereinigung, Wechsel der Arbeitskleidung) beraten."},
    # ── Expositionsbedingungen und Schutzmaßnahmen ────────────────────────
    {"wenn": {"enge_raeume": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeiten in engen Räumen",
     "quelle": "Abschnitte 6.3.2 und 8.2",
     "befund": "Schweißen/Schneiden in engen oder schlecht belüfteten Räumen angegeben.",
     "konsequenz": "Erhöhte Gefahr durch Stickstoffoxide bis hin zum toxischen "
                   "Lungenödem (Latenzzeit 1–2 Tage nach Exposition) beachten und die "
                   "versicherte Person darüber aufklären. Lüftungs-/Absaugmaßnahmen und "
                   "Atemschutz über die Gefährdungsbeurteilung prüfen; bei unzureichenden "
                   "Maßnahmen Mitteilung an das Unternehmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"absaugung": ["nein", "teilweise"]},
     "wenn_nicht": {"schweissanteil": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 7.1 und 8.2",
     "befund": "Keine oder nur teilweise genutzte Absaugung/Lüftung am Schweißarbeitsplatz.",
     "konsequenz": "Anhaltspunkt, dass die Maßnahmen des Arbeitsschutzes nicht "
                   "ausreichen: dem Unternehmen mitteilen und Schutzmaßnahmen vorschlagen "
                   "(§ 6 (4) ArbMedVV); versicherte Person zu Erfassung des Rauchs an der "
                   "Entstehungsstelle und zum Atemschutz beraten."},
    {"wenn": {"atemschutz": ["nie"]},
     "wenn_nicht": {"schweissanteil": ["keine"]},
     "schwere": "hinweis",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Beim Schweißen wird kein Atemschutz getragen.",
     "konsequenz": "Beratung zum Tragen geeigneter PSA unter Beachtung des individuellen "
                   "Gesundheitszustandes; Auswahl geeigneten Atemschutzes mit dem "
                   "Unternehmen abstimmen, insbesondere bei Verfahren mit hoher "
                   "Emissionsrate (z. B. Lichtbogenhandschweißen, Fülldraht, Brennschneiden)."},
    {"wenn": {"frueher_staub": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Staubexposition",
     "quelle": "Abschnitte 6.3.3.2, 7.2.2 und 7.4",
     "befund": "Frühere Exposition gegenüber Asbest oder Quarzstaub angegeben.",
     "konsequenz": "Rechtfertigende Indikation für Röntgen-Thorax anhand der Anamnese "
                   "prüfen (Anhang zur radiologischen Diagnostik der DGUV Empfehlung "
                   "»Silikogener Staub« beachten); Silikose/Asbestose sind "
                   "beurteilungsrelevant nach 7.4. Kombinationswirkung mit kanzerogenen "
                   "Schweißrauchbestandteilen in der Beratung berücksichtigen."},
    # ── Beratung ──────────────────────────────────────────────────────────
    {"wenn": {"rauchstatus": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Tabakkonsum",
     "quelle": "Abschnitte 6.3.2.2 und 8.1",
     "befund": "Regelmäßiger Tabak-/Nikotinkonsum angegeben.",
     "konsequenz": "Beratung zum Rauchverzicht: Tabakrauch und Schweißrauche belasten "
                   "die Atemwege gemeinsam (chronische Bronchitis, Lungenkrebsrisiko); "
                   "Packungsjahre dokumentieren und Entwöhnungsangebote aufzeigen."},
    {"wenn": {"pneumokokken": ["nein", "unbekannt"]},
     "schwere": "hinweis",
     "bereich": "Impfschutz",
     "quelle": "Abschnitt 7.1 (AMR 6.7)",
     "befund": "Kein bzw. unklarer Impfschutz gegen Pneumokokken.",
     "konsequenz": "Pneumokokken-Impfung gemäß AMR 6.7 als Bestandteil der "
                   "arbeitsmedizinischen Vorsorge bei Tätigkeiten mit Gefahrstoffen "
                   "durch Schweißen und Trennen von Metallen anbieten; ggf. Impfstatus "
                   "über die Hausarztpraxis klären."},
]
