# -*- coding: utf-8 -*-
"""G 15 Chrom(VI)-Verbindungen – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Vorsorgeuntersuchungen, 6. Auflage 2016, G 15
»Chrom-VI-Verbindungen« (Fassung Oktober 2014), S. 267–278."""

SLUG = "g15-chrom6-2016"

CATALOG = {
    "version": 2,
    "title": "G 15 Chrom(VI)-Verbindungen (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Vorsorgeuntersuchungen, "
             "6. Auflage 2016, G 15 »Chrom-VI-Verbindungen« (Fassung Oktober 2014), "
             "S. 267–278",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich heute?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Erste "
                            "Nachuntersuchung: nach 6–12 Monaten, weitere nach 12–24 Monaten. "
                            "Nachgehende Untersuchung: nach dem Ende der Tätigkeit mit "
                            "Chrom(VI)-Verbindungen.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich war schon einmal hier)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (Tätigkeit ist beendet)"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Chrom-Belastung",
            "subtitle": "Ihre Arbeit mit Chrom(VI)-Verbindungen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Welche dieser Arbeiten führen Sie durch?",
                    "hint": "Bei diesen Arbeiten ist mit einer Belastung durch Chrom(VI)-"
                            "Verbindungen zu rechnen. Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "galvanik", "label": "Galvanik / Hartverchromen (z. B. an offenen Bädern)"},
                        {"value": "schweissen_schneiden", "label": "Schweißen oder thermisches Schneiden von "
                                                                   "Chrom-Nickel-Stahl (Edelstahl)"},
                        {"value": "enge_raeume", "label": "Schweißen in engen Räumen (z. B. Tanks, Kessel, "
                                                          "Behälter, Schächte, Rohrleitungen)"},
                        {"value": "thermisch_spritzen", "label": "Thermisches Spritzen (Flamm-, Lichtbogen-, "
                                                                 "Plasmaspritzen) mit chromhaltigen Werkstoffen"},
                        {"value": "anstriche", "label": "Spritzlackieren mit chromathaltigen Farben oder "
                                                        "Entfernen/Abschleifen chromathaltiger Anstriche"},
                        {"value": "herstellen", "label": "Herstellen oder Verarbeiten von Chrom(VI)-Verbindungen "
                                                         "(auch Wartung, Reinigung, Instandhaltung)"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an Anlagen, in denen Chrom(VI)-"
                                                      "Verbindungen hergestellt wurden"},
                        {"value": "sonstige", "label": "Andere Arbeiten mit Chrom(VI)-Verbindungen"},
                        {"value": "keine", "label": "Keine davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit möglichem Kontakt zu "
                             "Chrom(VI)-Verbindungen?",
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
                    "id": "vorexposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt zu Chrom(VI)-Verbindungen "
                             "oder eine vergleichbare Gefahrstoff-Belastung?",
                    "required": True,
                    "followup": {"id": "vorexposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, und wie lange?", "when": "yes"},
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Unfälle oder Zwischenfälle mit besonders "
                             "hoher Chrom-Belastung (z. B. Verschütten, Absaugung ausgefallen)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Atemschutz, Handschuhe und Hygiene am Arbeitsplatz",
            "questions": [
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit Chrom-Belastung Atemschutz?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "Für meine Tätigkeit nicht vorgesehen"},
                    ],
                },
                {
                    "id": "handschuhe",
                    "type": "choice",
                    "label": "Tragen Sie bei möglichem Hautkontakt geeignete Schutzhandschuhe?",
                    "hint": "Chrom(VI)-Verbindungen können die Haut sensibilisieren "
                            "(Allergie auslösen).",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_kontakt", "label": "Ich habe keinen Hautkontakt"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit trotzdem direkt mit chromhaltigen "
                             "Flüssigkeiten, Stäuben oder Nebeln in Kontakt?",
                    "required": True,
                },
                {
                    "id": "hygiene",
                    "type": "yes_no",
                    "label": "Können Sie die Hygieneregeln am Arbeitsplatz einhalten (nicht essen/"
                             "trinken/rauchen im Arbeitsbereich, Hände reinigen, Arbeitskleidung "
                             "wechseln)?",
                    "required": True,
                    "followup": {"id": "hygiene_desc", "type": "text",
                                 "label": "Was funktioniert nicht?", "when": "no"},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Nase, Atemwege, Haut und Augen",
            "questions": [
                {
                    "id": "nase_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Beschwerden an der Nase: ständige Absonderung (laufende "
                             "Nase), Borken/Krusten, häufiges Nasenbluten oder wunde Stellen in "
                             "der Nase?",
                    "hint": "Chrom(VI)-Verbindungen können die Nasenscheidewand schädigen – oft "
                            "ohne Schmerzen.",
                    "required": True,
                    "followup": {"id": "nase_beschwerden_desc", "type": "text",
                                 "label": "Welche Beschwerden, seit wann?", "when": "yes"},
                },
                {
                    "id": "atemwege_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Husten, Auswurf, Atembeschwerden oder Kurzatmigkeit?",
                    "required": True,
                    "followup": {"id": "atemwege_beschwerden_desc", "type": "text",
                                 "label": "Welche Beschwerden, seit wann?", "when": "yes"},
                },
                {
                    "id": "haut_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Hautbeschwerden: Rötung, Juckreiz, Ausschlag oder Ekzem "
                             "(entzündete, nässende oder schuppende Haut), besonders an den Händen?",
                    "required": True,
                    "followup": {"id": "haut_beschwerden_desc", "type": "text",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "haut_wunden",
                    "type": "yes_no",
                    "label": "Haben Sie schlecht heilende Wunden, kleine Geschwüre oder tiefe, "
                             "schmerzhafte Hautrisse (Rhagaden), z. B. an Händen oder Unterarmen?",
                    "required": True,
                },
                {
                    "id": "augen_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit gereizte Augen (Brennen, Tränen, Rötung)?",
                    "required": True,
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder längere "
                             "Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang_vermutet",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen Ihren Beschwerden oder "
                             "einer Erkrankung und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Allergien",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "vorerkr_nnh",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie chronische Entzündungen, Polypen, Geschwülste "
                             "oder andere Erkrankungen der Nasennebenhöhlen oder des Rachens?",
                    "required": True,
                    "followup": {"id": "vorerkr_nnh_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vorerkr_atemwege",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Erkrankungen der Atemwege oder der Lunge "
                             "(z. B. chronische Bronchitis, Asthma, Verwachsungen des Rippenfells "
                             "nach Rippenfellentzündung)?",
                    "required": True,
                    "followup": {"id": "vorerkr_atemwege_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, in Behandlung?", "when": "yes"},
                },
                {
                    "id": "varizen",
                    "type": "yes_no",
                    "label": "Haben Sie ausgeprägte Krampfadern (Varizen) mit "
                             "Durchblutungsstörungen, z. B. Schwellungen, Hautverfärbungen oder "
                             "offenen Stellen an den Beinen?",
                    "required": True,
                },
                {
                    "id": "vorerkr_haut",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine chronische Hauterkrankung (z. B. "
                             "chronisches Ekzem, Neurodermitis, sehr trockene rissige Haut)?",
                    "required": True,
                    "followup": {"id": "vorerkr_haut_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "allergie",
                    "type": "yes_no",
                    "label": "Haben Sie Allergien, insbesondere eine Kontaktallergie gegen Chromat "
                             "(z. B. »Zementekzem«) oder immer wiederkehrende allergische "
                             "Beschwerden?",
                    "required": True,
                    "followup": {"id": "allergie_desc", "type": "text",
                                 "label": "Welche Allergien?", "when": "yes"},
                },
                {
                    "id": "allgemein_erkrankungen",
                    "type": "yes_no",
                    "label": "Haben Sie sonstige Erkrankungen oder gesundheitliche Einschränkungen, "
                             "die hier noch nicht genannt wurden?",
                    "required": True,
                    "followup": {"id": "allgemein_erkrankungen_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen_sektion",
            "title": "Rauchen",
            "subtitle": "Wichtig für die Beratung",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Rauchen und das Einatmen von Chrom(VI)-Verbindungen können sich in "
                            "ihrer krebserzeugenden Wirkung gegenseitig verstärken.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "frueher", "label": "Früher, jetzt nicht mehr"},
                        {"value": "nie", "label": "Nein, nie"},
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
    # ── Bedenkenstatbestände (Abschnitt 2.1.1) ────────────────────────────
    {"wenn": {"vorerkr_nnh": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nasennebenhöhlen/Rachen",
     "quelle": "Abschnitte 2.1.1–2.1.3 und 1.2.3",
     "befund": "Chronische Erkrankung, Entzündung oder Geschwulst der Nasennebenhöhlen "
               "oder des Rachens angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1: vor Aufnahme bzw. Fortsetzung der "
                   "Tätigkeit ärztlich klären, ob dauernde (2.1.1) oder befristete (2.1.2) "
                   "gesundheitliche Bedenken bestehen. In unklaren Fällen "
                   "Ergänzungsuntersuchung (HNO-ärztliche Untersuchung). Bei weniger "
                   "ausgeprägtem Befund Voraussetzungen nach 2.1.3 prüfen (Schutzmaßnahmen, "
                   "expositionsärmerer Einsatz, verkürzte Nachuntersuchungsfristen)."},
    {"wenn": {"vorerkr_atemwege": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 2.1.1–2.1.3 und 1.2.3",
     "befund": "Erkrankung der Atemwege oder der Lunge (ggf. Pleuraschwarten) in der "
               "Vorgeschichte angegeben.",
     "konsequenz": "Prüfen, ob eine wesentliche Beeinträchtigung der Luftwege/Lunge oder "
                   "eine Begünstigung bronchopulmonaler Erkrankungen vorliegt "
                   "(Bedenkenstatbestand 2.1.1). Spirometrie besonders gewichten; in "
                   "unklaren Fällen radiologische Diagnostik des Thorax bzw. HNO-ärztliche "
                   "Ergänzungsuntersuchung. Bei Grenzbefunden der Lungenfunktion keine "
                   "Bedenken nur unter Voraussetzungen nach 2.1.3 (inkl. verkürzter "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"varizen": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Venen/Haut",
     "quelle": "Abschnitte 2.1.1 und 1.2.2 (Untersuchung der Haut)",
     "befund": "Oberflächliche Varizen mit venösen Durchblutungsstörungen angegeben.",
     "konsequenz": "Bedenkenstatbestand nach 2.1.1 (venöse Durchblutungsstörungen bei "
                   "oberflächlichen Varizen): Haut und Venenstatus ärztlich untersuchen und "
                   "klären, ob dauernde oder befristete Bedenken bestehen; bei weniger "
                   "ausgeprägtem Befund Voraussetzungen nach 2.1.3 prüfen."},
    {"wenn": {"vorerkr_haut": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "Abschnitte 2.1.1–2.1.3 und 1.2.2",
     "befund": "Chronische Hauterkrankung (z. B. chronisches Ekzem) angegeben.",
     "konsequenz": "Chronisches Ekzem und starke Rhagadenbildung sind Bedenkenstatbestände "
                   "nach 2.1.1: Hautuntersuchung (Ekzeme, Rhagaden, allergische "
                   "Manifestationen) durchführen und Bedenken klären. Bei weniger "
                   "ausgeprägtem Befund Aufnahme/Fortsetzung nur unter Voraussetzungen nach "
                   "2.1.3 (Hautschutz, geeignete Schutzhandschuhe, verkürzte "
                   "Nachuntersuchungsfristen)."},
    {"wenn": {"allergie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Allergie",
     "quelle": "Abschnitte 2.1.1, 2.2 und 3.2",
     "befund": "Allergie bzw. wiederkehrende allergische Beschwerden angegeben "
               "(ggf. Chromat-Kontaktallergie).",
     "konsequenz": "Rezidivierende allergische Manifestationen sind Bedenkenstatbestand nach "
                   "2.1.1: allergologisch-dermatologische Abklärung erwägen (Bestimmung von "
                   "Immunglobulin E ist im Untersuchungsprogramm erwünscht); besondere "
                   "Rezidivneigung des Chromatekzems beachten. Bedenken bzw. Voraussetzungen "
                   "nach 2.1.3 klären."},
    {"wenn": {"haut_wunden": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "Abschnitte 2.1.1, 3.2.2, 3.2.3 und 4",
     "befund": "Schlecht heilende Wunden, Geschwüre oder tiefe Rhagaden angegeben.",
     "konsequenz": "Auf chromattypische, schlecht heilende »Chromatgeschwüre« und starke "
                   "Rhagadenbildung (Bedenkenstatbestand 2.1.1) untersuchen; Behandlung "
                   "einleiten und Hautkontakt unterbinden. Bei Verdacht auf beruflich "
                   "verursachte Erkrankung BK-Anzeige prüfen (BK-Nr. 1103)."},
    # ── Zielorgan-Beschwerden (Abschnitte 1.2.1/1.2.2 und 3.2) ────────────
    {"wenn": {"nase_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nase",
     "quelle": "Abschnitte 1.2.1, 1.2.2, 1.2.3 und 3.2.3",
     "befund": "Sekretabsonderung, Borkenbildung, Nasenbluten oder wunde Stellen der Nase "
               "angegeben.",
     "konsequenz": "Spekulumuntersuchung der Nase durchführen (im Programm erwünscht, "
                   "Indikation z. B. Aerosolbelastung); auf Septumveränderungen der Stadien "
                   "A–C (Rötung, Ulzeration, Perforation) achten. In unklaren Fällen "
                   "Ergänzungsuntersuchung (HNO-ärztliche Untersuchung). Hinweis auf ggf. "
                   "unzureichende Schutzmaßnahmen: Mitteilung an den Arbeitgeber zur "
                   "Aktualisierung der Gefährdungsbeurteilung (Abschnitt 2.2)."},
    {"wenn": {"atemwege_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 1.2.1, 1.2.2, 1.2.3 und 3.2.3",
     "befund": "Husten, Auswurf, Atembeschwerden oder Kurzatmigkeit angegeben.",
     "konsequenz": "Spirometrie besonders gewichten (Anhang 1, Leitfaden "
                   "»Lungenfunktionsprüfung«); an chronische Bronchitis mit spastischer "
                   "Komponente und Bronchialasthma denken. In unklaren Fällen radiologische "
                   "Diagnostik des Thorax bzw. weiterführende Abklärung; bei Grenzbefunden "
                   "verkürzte Nachuntersuchungsfristen nach 2.1.3 erwägen."},
    {"wenn": {"haut_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 1.2.2, 2.2 und 3.2.3",
     "befund": "Hautrötung, Juckreiz, Ausschlag oder Ekzem angegeben.",
     "konsequenz": "Untersuchung der Haut (Ekzeme, Rhagaden, allergische Manifestationen); "
                   "an allergisches Kontaktekzem durch Chromat denken (besondere "
                   "Rezidivneigung, bevorzugt an den Händen). Beratung zu Hautschutz, "
                   "Hautreinigung, Hautpflege und geeigneten Schutzhandschuhen; bei Verdacht "
                   "auf Berufsdermatose BK-Verfahren prüfen."},
    {"wenn": {"augen_beschwerden": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Augen",
     "quelle": "Abschnitt 3.2.2",
     "befund": "Augenreizung (Brennen, Tränen, Rötung) bei der Arbeit angegeben.",
     "konsequenz": "Hinweis auf akute Reizwirkung von Chromat-Stäuben/-Dämpfen "
                   "(Konjunktivitis, Hornhautschäden möglich): Exposition und Augenschutz "
                   "prüfen; bei anhaltenden Beschwerden augenärztliche Vorstellung "
                   "empfehlen."},
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt (nach schwerer oder längerer "
                   "Erkrankung, die Anlass zu Bedenken gegen eine Fortsetzung der Tätigkeit "
                   "geben könnte): vollständiges Untersuchungsprogramm durchführen und "
                   "Bedenken nach Abschnitt 2.1 neu beurteilen."},
    {"wenn": {"zusammenhang_vermutet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitte 1.1 und 2.2",
     "befund": "Proband vermutet einen Zusammenhang zwischen Erkrankung/Beschwerden und "
               "der Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung ermöglichen (Fristenregelung 1.1); "
                   "Beschwerden gezielt abklären (ggf. Ergänzungsuntersuchung) und bei "
                   "begründetem Verdacht auf eine Berufskrankheit Anzeige nach BK-Nr. 1103 "
                   "erstatten."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "Abschnitte 1.1, 3.1.4 und 2.2",
     "befund": "Unfall oder Zwischenfall mit erhöhter Chrom-Exposition angegeben.",
     "konsequenz": "Nach ärztlichem Ermessen vorgezogene Untersuchung bzw. Biomonitoring "
                   "veranlassen (Chrombestimmung in Urin und Erythrozyten, Bewertung über "
                   "die EKA-Korrelation, BAR Gesamt-Chrom 0,6 µg/l Urin). Arbeitgeber auf "
                   "die Aktualisierung der Gefährdungsbeurteilung hinweisen (Abschnitt 2.2)."},
    # ── Schutzmaßnahmen und Hygiene (Abschnitt 2.2) ───────────────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Atemschutz",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Atemschutz wird bei chrombelasteten Arbeiten selten oder nie getragen.",
     "konsequenz": "Beratung zur Atemwegsexposition gegenüber Chrom(VI)-Verbindungen; "
                   "ergeben sich Hinweise auf unzureichenden Arbeitsschutz, Mitteilung an "
                   "den Arbeitgeber zur Aktualisierung der Gefährdungsbeurteilung "
                   "(unter Wahrung der schutzwürdigen Belange des Untersuchten)."},
    {"wenn": {"handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Hautschutz",
     "quelle": "Abschnitte 2.2 und 3.2.2",
     "befund": "Bei möglichem Hautkontakt werden selten oder nie Schutzhandschuhe getragen.",
     "konsequenz": "Beratung zur Möglichkeit der Hautsensibilisierung und zu den "
                   "erforderlichen Hautschutzmaßnahmen (Hautschutz, Hautreinigung, "
                   "Hautpflege) sowie zum richtigen Einsatz geeigneter Schutzhandschuhe "
                   "(stoffspezifische Hinweise: GESTIS). Bei fortbestehenden Defiziten "
                   "Mitteilung an den Arbeitgeber (Abschnitt 2.2)."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautschutz",
     "quelle": "Abschnitte 2.2, 3.2.2 und 3.2.3",
     "befund": "Direkter Hautkontakt zu chromhaltigen Flüssigkeiten/Stäuben trotz "
               "Schutzmaßnahmen angegeben.",
     "konsequenz": "Beratung zu Sensibilisierung und Chromatgeschwüren (Eindringen in "
                   "Hautverletzungen, Schürfstellen, Rhagaden); Haut auf Wunden und Rhagaden "
                   "kontrollieren und Überprüfung der Schutzmaßnahmen anregen."},
    {"wenn": {"hygiene": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Hygieneregeln am Arbeitsplatz können nicht eingehalten werden.",
     "konsequenz": "Einhaltung allgemeiner Hygienemaßnahmen empfehlen (nicht essen/trinken/"
                   "rauchen im Arbeitsbereich, Hautreinigung, Kleidungswechsel); "
                   "organisatorische Defizite dem Arbeitgeber mitteilen (Abschnitt 2.2)."},
    # ── Beratung, nachgehende Untersuchungen ──────────────────────────────
    {"wenn": {"rauchen": ["ja"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 2.2 und 3.2.1",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Auf die Schädlichkeit des Zigarettenrauchens hinweisen, insbesondere in "
                   "Verbindung mit der Atemwegsexposition gegenüber Chrom(VI)-Verbindungen "
                   "(Synkarzinogenität, erhöhtes Bronchialkarzinom-Risiko); Tabakentwöhnung "
                   "empfehlen."},
    {"wenn": {"untersuchung_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Untersuchung",
     "quelle": "Abschnitte 1.1, 1.2.2 und 1.2.3",
     "befund": "Termin im Rahmen der nachgehenden Untersuchung nach Ende der Tätigkeit.",
     "konsequenz": "Programm der nachgehenden Untersuchung anwenden (wie Erstuntersuchung, "
                   "ggf. radiologische Diagnostik des Thorax; in unklaren Fällen HNO-"
                   "ärztliche Ergänzungsuntersuchung). Organisation über den "
                   "Organisationsdienst für nachgehende Untersuchungen (ODIN, "
                   "www.odin-info.de) sicherstellen."},
]
