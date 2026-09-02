# -*- coding: utf-8 -*-
"""Arsen und Arsenverbindungen – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen
für arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Arsen und Arsenverbindungen« (E ARS, Fassung Januar 2022, Grenzwerte
aktualisiert 2024), S. 74–97."""

SLUG = "arsen-2024"

CATALOG = {
    "version": 2,
    "title": "Arsen und Arsenverbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Arsen und Arsenverbindungen« (E ARS, Fassung Januar 2022, "
             "Grenzwerte aktualisiert 2024), S. 74–97",
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
                    "label": "Um welche arbeitsmedizinische Vorsorge handelt es sich heute?",
                    "hint": "Nachgehende Vorsorge: Untersuchung nach dem Ende der Tätigkeit "
                            "mit Arsen, weil viele Arsenverbindungen krebserzeugend sind.",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge wegen Arsen (Tätigkeit beginnt oder läuft bereits)"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich war schon einmal zur Arsen-Vorsorge)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (die Tätigkeit mit Arsen ist beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "not_in": ["nachgehend"]},
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
            "title": "Tätigkeit & Arsen-Belastung",
            "subtitle": "Ihre Arbeit und der mögliche Kontakt mit Arsen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "arsen_bereiche",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen kommen Sie mit Arsen oder Arsenverbindungen "
                             "in Kontakt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "metallurgie", "label": "Metallgewinnung/-hütte: arsenhaltige Erze mahlen, rösten oder "
                                                          "verhütten (z. B. Kupfer, Zink, Blei)"},
                        {"value": "filterreinigung", "label": "Reparatur oder Reinigung von Flugstaubanlagen und Filtern"},
                        {"value": "glas", "label": "Glasherstellung (Arsentrioxid als Läuterungsmittel, Spezialgläser)"},
                        {"value": "halbleiter", "label": "Halbleiter/Elektronik: Galliumarsenid, Arsin als Dotiergas, "
                                                         "Photovoltaik- oder Elektronik-Recycling"},
                        {"value": "abbruch", "label": "Abbruch- oder Restaurierungsarbeiten (alte arsenhaltige Farben, "
                                                      "z. B. Schweinfurter Grün, oder alte Produktionsanlagen)"},
                        {"value": "kulturgut", "label": "Museen/Kulturgüter: alte Tierpräparate, arsenhaltige Pigmente "
                                                        "oder Biozide"},
                        {"value": "kampfmittel", "label": "Kampfmittelbeseitigung (arsenhaltige Kampfstoffe)"},
                        {"value": "labor_sonstiges", "label": "Labor, Arzneimittelherstellung oder anderer Bereich"},
                        {"value": "keine", "label": "Keiner davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "blei_arsenat",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Bleiarsenat oder Bleihydrogenarsenat "
                             "(bleihaltige Arsenverbindungen)?",
                    "hint": "Diese Stoffe enthalten zusätzlich giftiges Blei und können die "
                            "Fortpflanzung schädigen.",
                    "required": True,
                },
                {
                    "id": "arsin_moeglich",
                    "type": "yes_no",
                    "label": "Kann bei Ihrer Arbeit Arsenwasserstoff (Arsin) entstehen oder "
                             "verwendet werden, z. B. als Dotiergas oder wenn starke Säuren auf "
                             "arsenhaltiges Material treffen?",
                    "required": True,
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit möglichem Arsen-Kontakt?",
                    "required": True,
                    "options": [
                        {"value": "beginnt", "label": "Noch gar nicht, die Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis15", "label": "5 bis 15 Jahre"},
                        {"value": "ueber15", "label": "Mehr als 15 Jahre"},
                    ],
                },
                {
                    "id": "frueher_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit Arsen oder anderen "
                             "krebserzeugenden Stoffen (z. B. Asbest, Benzol, Chromate)?",
                    "required": True,
                    "followup": {"id": "frueher_expo_desc", "type": "textarea",
                                 "label": "Welche Stoffe, welche Tätigkeiten, wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle, Unfälle oder ungewöhnliche "
                             "Betriebszustände mit möglicher erhöhter Arsen-Belastung "
                             "(z. B. Staubfreisetzung, Leckage, Filterdefekt)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "geruch",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit schon einmal einen knoblauchartigen Geruch "
                             "wahrgenommen?",
                    "hint": "Arsenwasserstoff und einige organische Arsenverbindungen riechen "
                            "nach Knoblauch.",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                    "followup": {"id": "geruch_desc", "type": "text",
                                 "label": "Wie oft und in welcher Situation?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Wie Sie sich bei der Arbeit schützen",
            "questions": [
                {
                    "id": "psa",
                    "type": "multi_choice",
                    "label": "Welche Schutzausrüstung benutzen Sie bei Tätigkeiten mit möglichem "
                             "Arsen-Kontakt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "not_in": ["nachgehend"]},
                    "options": [
                        {"value": "atemschutz", "label": "Atemschutz (Maske)"},
                        {"value": "handschuhe", "label": "Geeignete Schutzhandschuhe"},
                        {"value": "schutzkleidung", "label": "Schutzkleidung / Wechsel der Arbeitskleidung"},
                        {"value": "keine", "label": "Keine davon"},
                        {"value": "keine_noetig", "label": "Nicht nötig (kein direkter Kontakt möglich)"},
                    ],
                },
                {
                    "id": "hygiene",
                    "type": "choice",
                    "label": "Halten Sie die Hygieneregeln am Arbeitsplatz ein (nicht essen, "
                             "trinken oder rauchen am Arbeitsplatz, Hände waschen vor Pausen)?",
                    "hint": "Arsen kann über die Hände in den Mund und so in den Körper gelangen.",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "not_in": ["nachgehend"]},
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "teilweise", "label": "Nur teilweise"},
                        {"value": "nein", "label": "Nein / es gibt keine solchen Regeln"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit direkt mit arsenhaltigen Stoffen, "
                             "Stäuben oder Lösungen in Berührung?",
                    "hint": "Viele Arsenverbindungen können über die Haut aufgenommen werden "
                            "(hautresorptiv).",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "not_in": ["nachgehend"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, die mit Arsen zusammenhängen können",
            "questions": [
                {
                    "id": "haut_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie Veränderungen an der Haut bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "hyperkeratosen", "label": "Auffällige Hornhaut-Verdickungen, z. B. an Handflächen "
                                                             "oder Fußsohlen (Hyperkeratosen)"},
                        {"value": "pigment", "label": "Neue dunkle oder helle Flecken (Pigmentverschiebungen)"},
                        {"value": "ekzem", "label": "Ekzem, Hautausschlag oder anhaltende Hautreizung"},
                        {"value": "keine", "label": "Nein, keine davon"},
                    ],
                },
                {
                    "id": "reizung_augen",
                    "type": "yes_no",
                    "label": "Haben Sie gereizte Augen (Jucken, Brennen, Tränen, Lichtempfindlichkeit) "
                             "oder Reizungen in Nase und Rachen?",
                    "required": True,
                },
                {
                    "id": "atemwege",
                    "type": "yes_no",
                    "label": "Haben Sie Husten, Atemnot oder Schmerzen in der Brust?",
                    "required": True,
                },
                {
                    "id": "magen_darm",
                    "type": "yes_no",
                    "label": "Haben Sie Magen-Darm-Beschwerden wie Übelkeit, Erbrechen, Durchfall, "
                             "Bauchschmerzen oder einen metallischen bzw. knoblauchartigen Geschmack "
                             "im Mund?",
                    "required": True,
                },
                {
                    "id": "nerven",
                    "type": "yes_no",
                    "label": "Haben Sie Kribbeln, Taubheitsgefühl oder Schwäche in Händen oder Füßen "
                             "(Zeichen einer Nervenschädigung, sog. Polyneuropathie)?",
                    "required": True,
                },
                {
                    "id": "gefaesse",
                    "type": "yes_no",
                    "label": "Haben Sie Durchblutungsstörungen an den Fingern, z. B. weiße, kalte "
                             "oder schmerzende Finger?",
                    "required": True,
                },
                {
                    "id": "allgemein_einschraenkung",
                    "type": "yes_no",
                    "label": "Haben Sie sonstige gesundheitliche Einschränkungen oder Beschwerden?",
                    "required": True,
                    "followup": {"id": "allgemein_einschraenkung_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen und Medikamente ────────────────────────────
        {
            "id": "gesundheit",
            "title": "Vorerkrankungen & Medikamente",
            "subtitle": "Ihre Krankengeschichte",
            "questions": [
                {
                    "id": "vorerkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine der folgenden Erkrankungen festgestellt?",
                    "hint": "Mehrfachauswahl möglich. Diese Organe können durch Arsen zusätzlich "
                            "belastet werden.",
                    "required": True,
                    "options": [
                        {"value": "leber", "label": "Erkrankung der Leber"},
                        {"value": "niere", "label": "Erkrankung der Nieren"},
                        {"value": "magen_darm", "label": "Erkrankung des Magen-Darm-Trakts"},
                        {"value": "haut", "label": "Chronische Hauterkrankung (z. B. Ekzem, Schuppenflechte)"},
                        {"value": "gefaesse", "label": "Gefäßerkrankung (z. B. Durchblutungsstörungen)"},
                        {"value": "blut", "label": "Bluterkrankung (z. B. Blutarmut/Anämie)"},
                        {"value": "nerven", "label": "Erkrankung der Nerven oder des Gehirns"},
                        {"value": "bronchien", "label": "Erkrankung der Bronchien (z. B. chronische Bronchitis, Asthma)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Berufskrankheit anerkannt, oder läuft derzeit "
                             "ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Berufskrankheit bzw. welches Verfahren?",
                                 "when": "yes"},
                },
                {
                    "id": "medikamente_arsen",
                    "type": "yes_no",
                    "label": "Nehmen oder nahmen Sie arsenhaltige Medikamente oder Heilmittel ein?",
                    "hint": "Z. B. Arsentrioxid gegen Leukämie (Trisenox), Melarsoprol, oder "
                            "alternative bzw. homöopathische Mittel auf Arsenbasis "
                            "(arsenicum album).",
                    "required": True,
                    "followup": {"id": "medikamente_arsen_desc", "type": "text",
                                 "label": "Welche Mittel?", "when": "yes"},
                },
                {
                    "id": "alkohol",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Alkoholabhängigkeit?",
                    "required": True,
                },
                {
                    "id": "schwanger",
                    "type": "choice",
                    "label": "Sind Sie derzeit schwanger, oder stillen Sie?",
                    "hint": "Arsen kann auf das ungeborene Kind übergehen und wird in geringen "
                            "Mengen über die Muttermilch ausgeschieden. Für Schwangere und "
                            "Stillende gelten besondere Schutzvorschriften (Mutterschutzgesetz).",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein / trifft nicht auf mich zu"},
                        {"value": "schwanger", "label": "Ja, ich bin schwanger"},
                        {"value": "stillend", "label": "Ja, ich stille"},
                        {"value": "keine_angabe", "label": "Keine Angabe"},
                    ],
                },
            ],
        },
        # ── 6 ─ Ernährung und Rauchen ──────────────────────────────────────
        {
            "id": "lebensstil",
            "title": "Ernährung & Rauchen",
            "subtitle": "Wichtig für die Bewertung der Arsen-Messung im Urin (Biomonitoring)",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Rauchen und Arsen zusammen können die Lunge zusätzlich belasten.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "frueher", "label": "Früher, nicht mehr"},
                        {"value": "nie", "label": "Nein, nie"},
                    ],
                },
                {
                    "id": "fisch_konsum",
                    "type": "yes_no",
                    "label": "Essen Sie häufig (mehrmals pro Woche) Fisch, Meeresfrüchte oder Algen?",
                    "hint": "Diese Lebensmittel enthalten natürliche organische Arsenverbindungen "
                            "und können die Urin-Messwerte beeinflussen.",
                    "required": True,
                },
                {
                    "id": "reis_konsum",
                    "type": "yes_no",
                    "label": "Essen Sie häufig ungeschälte Reisprodukte (z. B. Naturreis, "
                             "Reiswaffeln, Reisflocken)?",
                    "hint": "Reis kann erhöhte Mengen anorganischer Arsenverbindungen enthalten.",
                    "required": True,
                },
                {
                    "id": "fisch_48h",
                    "type": "yes_no",
                    "label": "Haben Sie in den letzten 48 Stunden Fisch oder Meeresfrüchte gegessen?",
                    "hint": "Vor einer Arsen-Messung im Urin sollen 48 Stunden lang kein Fisch und "
                            "keine Meeresfrüchte gegessen werden (Fischkarenz).",
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
    # ── Zielorgan-Beschwerden → Abklärung/Untersuchung (Abschnitte 6.3, 7.2, 7.4) ──
    {"wenn": {"haut_beschwerden": ["hyperkeratosen", "pigment", "ekzem"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3.3, 7.2.2 und 7.4",
     "befund": "Hautveränderungen angegeben (Hyperkeratosen, Pigmentverschiebungen "
               "oder Ekzem).",
     "konsequenz": "Gezielte Untersuchung der Haut (7.2.2) mit besonderem Blick auf "
                   "Hyperkeratosen, Pigmentverschiebungen und Ekzeme; Biomonitoring "
                   "durchführen. Bei Verdacht auf arsenbedingte Hautschädigung Beurteilung "
                   "nach 7.4, Maßnahmen nach 7.4.2/7.4.3 prüfen und ärztliche "
                   "BK-Anzeige (BK-Nr. 1108) erwägen."},
    {"wenn": {"nerven": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 6.3.2/6.3.3 und 7.4",
     "befund": "Kribbeln, Taubheitsgefühl oder Schwäche in Händen/Füßen angegeben "
               "(mögliche periphere Neuropathie).",
     "konsequenz": "Neurologische Abklärung veranlassen und Biomonitoring durchführen. "
                   "Beurteilung nach 7.4 (Erkrankung des peripheren/zentralen Nerven-"
                   "systems); bei bestätigtem Befund Maßnahmen nach 7.4.2, verkürzte "
                   "Vorsorgefrist nach 7.4.3 bzw. Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 6.3.2/6.3.3 und 7.4",
     "befund": "Husten, Atemnot oder Brustschmerzen angegeben.",
     "konsequenz": "Ärztliche Abklärung der Atemwegssymptome (Arsenstäube reizen und "
                   "schädigen die Atemwege; Atemwegskarzinome sind beschrieben). "
                   "Beurteilung nach 7.4 (Erkrankung der Bronchien); Zusammenhang mit "
                   "der Exposition prüfen, ggf. Maßnahmen nach 7.4.2 vorschlagen."},
    {"wenn": {"magen_darm": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm-Trakt",
     "quelle": "Abschnitte 6.3.2 und 7.4",
     "befund": "Magen-Darm-Beschwerden bzw. metallisch-knoblauchartiger Geschmack "
               "angegeben.",
     "konsequenz": "An akute/subakute Arsenaufnahme denken (gastrointestinale Verlaufs-"
                   "form): zeitnahe ärztliche Abklärung, Biomonitoring, Leber- und "
                   "Nierenwerte sowie Blutbild kontrollieren (7.2.2); Expositions- und "
                   "Hygienesituation am Arbeitsplatz überprüfen."},
    {"wenn": {"gefaesse": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Gefäße",
     "quelle": "Abschnitte 6.3.3 und 7.4",
     "befund": "Durchblutungsstörungen an den Fingern angegeben.",
     "konsequenz": "Abklärung peripherer Gefäßschäden (v. a. Fingerarterien); Beurteilung "
                   "nach 7.4 (Erkrankung der Gefäße), ggf. angiologische Vorstellung und "
                   "Maßnahmen nach 7.4.2/7.4.3."},
    {"wenn": {"reizung_augen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Reizwirkungen",
     "quelle": "Abschnitte 6.3.2 und 8.2",
     "befund": "Reizungen der Augen bzw. der oberen Atemwege angegeben.",
     "konsequenz": "Lokale Reizwirkung durch arsenhaltige Stäube abklären; Expositions-"
                   "situation mit der Gefährdungsbeurteilung abgleichen. Reichen die "
                   "Schutzmaßnahmen erkennbar nicht aus, Mitteilung an das Unternehmen "
                   "und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    # ── Vorerkrankungen und besondere Personengruppen (Abschnitt 7.4) ─────
    {"wenn": {"vorerkrankungen": ["leber", "niere", "magen_darm", "haut", "gefaesse",
                                  "blut", "nerven", "bronchien"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankungen",
     "quelle": "Abschnitte 7.4.1–7.4.4",
     "befund": "Erkrankung eines Arsen-Zielorgans angegeben (Leber, Niere, Magen-Darm, "
               "Haut, Gefäße, Blut, Nervensystem oder Bronchien).",
     "konsequenz": "Ausmaß der Erkrankung ärztlich bewerten und prüfen, ob die Tätigkeit "
                   "ohne gesundheitliche Gefährdung möglich ist (7.4). Bei weniger "
                   "ausgeprägten Befunden Maßnahmen nach 7.4.2 empfehlen (Substitution, "
                   "technische/organisatorische/persönliche Schutzmaßnahmen, Arbeitsplatz "
                   "mit geringerer Exposition); bei zu erwartender Änderung des Schwere-"
                   "grads verkürzte Vorsorgefristen nach 7.4.3; ohne Aussicht auf Erfolg "
                   "Tätigkeitswechsel nach 7.4.4 erwägen (Mitteilung an den Arbeitgeber "
                   "nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"alkohol": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankungen",
     "quelle": "Abschnitt 7.4",
     "befund": "Alkoholabhängigkeit angegeben.",
     "konsequenz": "Alkoholabhängigkeit bei der Beurteilung nach 7.4 berücksichtigen "
                   "(erhöhte Empfindlichkeit von Leber und Nervensystem); Beratung und "
                   "ggf. Maßnahmen nach 7.4.2/7.4.3."},
    {"wenn": {"schwanger": ["schwanger", "stillend"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6.3.1 und 8.1 (Beratung), MuSchG",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben.",
     "konsequenz": "Beschäftigungsbeschränkungen nach dem Mutterschutzgesetz vor "
                   "(weiterer) Tätigkeit mit Arsen-Exposition klären: Arsen ist "
                   "plazentagängig und geht in die Muttermilch über, viele Arsen-"
                   "verbindungen sind krebserzeugend. Unverzügliche mutterschutz-"
                   "rechtliche Bewertung der Tätigkeit, Beratung der versicherten "
                   "Person; Fortsetzung der Exposition bis zur Klärung vermeiden."},
    {"wenn": {"blei_arsenat": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Mischexposition Blei",
     "quelle": "Abschnitte 2 und 8.1",
     "befund": "Tätigkeit mit Bleiarsenat bzw. Bleihydrogenarsenat angegeben.",
     "konsequenz": "Zusätzlich die DGUV Empfehlung »Blei und anorganische Blei-"
                   "verbindungen« heranziehen (Vorsorge um Blei-Programm erweitern). "
                   "Beratung zur krebserzeugenden und reproduktionstoxischen Wirkung "
                   "von Bleiarsenat/Bleihydrogenarsenat."},
    # ── Expositionsereignisse und Arbeitsschutz (Abschnitte 7.1, 8.2) ─────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitte 7.1 und 8.2",
     "befund": "Zwischenfall, Unfall oder ungewöhnlicher Betriebszustand mit möglicher "
               "erhöhter Arsen-Belastung angegeben.",
     "konsequenz": "Ereignis dokumentieren, Biomonitoring veranlassen (Parameter nach "
                   "Tabelle 2, Probenahme am Schichtende) und mit der Gefährdungs-"
                   "beurteilung abgleichen; dem Unternehmen Überprüfung der Schutz-"
                   "maßnahmen mitteilen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"geruch": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arsenwasserstoff",
     "quelle": "Abschnitte 7.1 (weitere Vorsorgen) und 8.1",
     "befund": "Knoblauchartige Geruchswahrnehmung bei der Arbeit angegeben.",
     "konsequenz": "Häufigkeit und Stärke der Geruchswahrnehmung dokumentieren – "
                   "möglicher Hinweis auf Freisetzung von Arsenwasserstoff oder "
                   "flüchtigen Arsenverbindungen. Beratung zur Giftigkeit und zum "
                   "möglichen Ausfall der Geruchswahrnehmung; Mitteilung an das "
                   "Unternehmen zur Überprüfung der Gefährdungsbeurteilung."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautschutz",
     "quelle": "Abschnitte 2 (Pflichtvorsorge) und 8.1",
     "befund": "Direkter Hautkontakt mit arsenhaltigen Stoffen angegeben.",
     "konsequenz": "Viele Arsenverbindungen sind hautresorptiv: Prüfen, ob der Tatbestand "
                   "der Pflichtvorsorge (Gesundheitsgefährdung durch Hautkontakt) erfüllt "
                   "ist. Beratung zu geeigneten Schutzhandschuhen, Vermeiden von Haut-"
                   "kontakt und Hautuntersuchung; ggf. Mitteilung an das Unternehmen "
                   "(§ 6 (4) ArbMedVV)."},
    {"wenn": {"psa": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Keine persönliche Schutzausrüstung bei Tätigkeiten mit möglichem "
               "Arsen-Kontakt.",
     "konsequenz": "Beratung zum richtigen Einsatz geeigneter PSA (Atemschutz, Schutz-"
                   "handschuhe, Wechsel der Arbeitskleidung). Ergeben sich Anhaltspunkte, "
                   "dass die Schutzmaßnahmen nicht ausreichen, Mitteilung an das "
                   "Unternehmen und Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"hygiene": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 6.2, 7.1 und 8.1",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht oder nur teilweise eingehalten.",
     "konsequenz": "Beratung zu Hygienemaßnahmen: orale Arsenaufnahme über Hand-zu-Mund-"
                   "Kontakt vermeiden (nicht essen/trinken/rauchen am Arbeitsplatz, "
                   "Händewaschen, getrennte Aufbewahrung und Wechsel der Arbeitskleidung)."},
    # ── Biomonitoring-Störgrößen (Abschnitt 6.4) ──────────────────────────
    {"wenn": {"fisch_48h": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 6.4",
     "befund": "Fisch- oder Meeresfrüchtekonsum in den letzten 48 Stunden angegeben.",
     "konsequenz": "Fischkarenz nicht eingehalten: Urin-Probenahme für das Biomonitoring "
                   "möglichst verschieben (48 Stunden vor Probenahme kein Fisch-/Meeres-"
                   "früchtekonsum) oder Ergebnis nur unter Berücksichtigung der ernährungs-"
                   "bedingten Hintergrundbelastung bewerten."},
    {"wenn": {"reis_konsum": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitte 6.1, 6.4 und 7.1",
     "befund": "Regelmäßig hoher Konsum ungeschälter Reisprodukte angegeben.",
     "konsequenz": "Mögliche Aufnahme anorganischer Arsenverbindungen über Reisprodukte "
                   "bei der Bewertung des Biomonitorings als Hintergrundbelastung "
                   "berücksichtigen; Ernährungsberatung anbieten."},
    {"wenn": {"medikamente_arsen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitte 6.4 und 7.1 (Medikamentenanamnese)",
     "befund": "Einnahme arsenhaltiger Medikamente oder Heilmittel angegeben "
               "(z. B. Trisenox, Melarsoprol, arsenicum album).",
     "konsequenz": "Medikamentenanamnese ärztlich vertiefen; arsenhaltige Arzneimittel "
                   "und Heilmittel als Störgröße des Biomonitorings berücksichtigen und "
                   "die behandelnde Ärztin/den behandelnden Arzt ggf. einbeziehen."},
    # ── Rauchen und nachgehende Vorsorge ──────────────────────────────────
    {"wenn": {"rauchen": ["ja"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitt 7.1 (allgemeine Beratung)",
     "befund": "Aktives Rauchen angegeben.",
     "konsequenz": "Beratung zu additiven Effekten von Rauchen und Arsen-Exposition "
                   "(z. B. Verschlechterung der Lungenfunktion, erhöhtes Krebsrisiko); "
                   "Tabakentwöhnung empfehlen."},
    {"wenn": {"frueher_expo": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 2 (nachgehende Vorsorge) und 7.1",
     "befund": "Frühere Exposition gegenüber Arsen oder anderen krebserzeugenden "
               "Gefahrstoffen angegeben.",
     "konsequenz": "Frühere Expositionen dokumentieren und bei der Beurteilung "
                   "berücksichtigen. Auf den Anspruch auf nachgehende Vorsorge hinweisen; "
                   "Anmeldung über das Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de) "
                   "prüfen bzw. anregen."},
]
