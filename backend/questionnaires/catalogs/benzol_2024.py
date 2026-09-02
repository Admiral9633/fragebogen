# -*- coding: utf-8 -*-
"""Benzol – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für arbeitsmedizinische
Beratungen und Untersuchungen, 1. Auflage 2024, Kapitel »Benzol« (E BNZ,
Fassung Januar 2022), S. 123–138."""

SLUG = "benzol-2024"

CATALOG = {
    "version": 2,
    "title": "Benzol (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Benzol« (E BNZ, Fassung Januar 2022), S. 123–138",
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
                    "label": "Um welche Vorsorge handelt es sich heute?",
                    "hint": "Nachgehende Vorsorge: Sie arbeiten nicht mehr mit Benzol, werden aber "
                            "wegen der früheren Belastung weiter untersucht.",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge wegen Benzol"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich war schon einmal zur Benzol-Vorsorge)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (Tätigkeit mit Benzol ist beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn eine wiederholte "
                            "Benzol-Belastung oder eine Gesundheitsgefährdung durch Hautkontakt nicht "
                            "ausgeschlossen werden kann.",
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
        # ── 2 ─ Tätigkeit und Benzol-Belastung ─────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Benzol-Belastung",
            "subtitle": "Ihre Arbeit und der mögliche Kontakt mit Benzol",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "benzol_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Bei welchen dieser Arbeiten können Sie mit Benzol oder benzolhaltigen "
                             "Gemischen in Kontakt kommen?",
                    "hint": "Mehrfachauswahl möglich. Benzol steckt z. B. auch in Benzin (Ottokraftstoff).",
                    "required": True,
                    "options": [
                        {"value": "herstellen_abfuellen",
                         "label": "Herstellen, Weiterverarbeiten oder Transport von Benzol; Füllen, "
                                  "Entleeren oder Abfüllen von Fässern/Behältern"},
                        {"value": "ottokraftstoff", "label": "Umfüllen oder Abfüllen von Benzin (Kraftstoff für Ottomotoren)"},
                        {"value": "kfz", "label": "Arbeiten an benzinführenden Teilen von Fahrzeugen (z. B. KFZ-Werkstatt)"},
                        {"value": "zweitakt", "label": "Herstellen/Verwenden von Zweitaktmischungen (z. B. Rasenmäher, Kettensäge)"},
                        {"value": "kleinflugzeuge", "label": "Betanken von Kleinflugzeugen"},
                        {"value": "giesserei", "label": "Abgießen in Sandgießereien mit organischen Bindersystemen"},
                        {"value": "filter_probenahme", "label": "Filter- oder Katalysatorwechsel, Probenahme in Benzol-Anlagen"},
                        {"value": "tankreinigung", "label": "Reinigen von/in Tanks oder Behältern, Tankstellensanierung"},
                        {"value": "wartung_sanierung",
                         "label": "Reinigungs-, Wartungs-, Instandsetzungs-, Sanierungs- oder "
                                  "Abbrucharbeiten in Produktions- oder Abfüllanlagen"},
                        {"value": "kontaminiert", "label": "Arbeiten in verunreinigten Bereichen (z. B. Sondermüll, Altlasten)"},
                        {"value": "sonstige", "label": "Andere Arbeiten mit Benzol oder benzolhaltigen Gemischen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit mit Benzol, Benzin oder benzolhaltigen "
                             "Flüssigkeiten in Berührung?",
                    "hint": "Benzol wird auch über die Haut in den Körper aufgenommen "
                            "(»hautresorptiv«). Auch benetzte Kleidung zählt.",
                    "required": True,
                    "followup": {"id": "hautkontakt_desc", "type": "text",
                                 "label": "Bei welchen Arbeiten, und wie oft?", "when": "yes"},
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit möglichem Benzol-Kontakt?",
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
                    "id": "grenzwert_ueberschreitung",
                    "type": "choice",
                    "label": "Wurde Ihnen mitgeteilt, dass an Ihrem Arbeitsplatz die Benzol-Grenzwerte "
                             "(Akzeptanz- oder Toleranzkonzentration) überschritten werden?",
                    "hint": "Diese Information stammt aus der Gefährdungsbeurteilung Ihres Betriebs.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, es gab eine Überschreitung"},
                        {"value": "nein", "label": "Nein, keine Überschreitung bekannt"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "fruehere_exposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Berufen oder Tätigkeiten Kontakt mit Benzol "
                             "oder benzolhaltigen Gemischen?",
                    "required": True,
                    "followup": {"id": "fruehere_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, in welchem Zeitraum?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Wie Sie sich bei der Arbeit schützen",
            "questions": [
                {
                    "id": "psa_benutzung",
                    "type": "multi_choice",
                    "label": "Welche persönliche Schutzausrüstung (PSA) benutzen Sie bei Arbeiten "
                             "mit möglichem Benzol-Kontakt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "show_if": {"id": "benzol_taetigkeiten", "not_in": ["keine"]},
                    "options": [
                        {"value": "handschuhe", "label": "Geeignete Schutzhandschuhe"},
                        {"value": "schutzkleidung", "label": "Schutzkleidung"},
                        {"value": "atemschutz", "label": "Atemschutz"},
                        {"value": "schutzbrille", "label": "Schutzbrille"},
                        {"value": "keine", "label": "Keine Schutzausrüstung"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme mit der Schutzausrüstung (z. B. undichte oder "
                             "beschädigte Handschuhe, Hautprobleme, schlechter Sitz)?",
                    "required": True,
                    "show_if": {"id": "benzol_taetigkeiten", "not_in": ["keine"]},
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
                {
                    "id": "kleidung_wechsel",
                    "type": "yes_no",
                    "label": "Wechseln Sie mit Benzol oder Benzin benetzte Arbeitskleidung sofort "
                             "und waschen Sie betroffene Hautstellen gleich ab?",
                    "hint": "Hygiene am Arbeitsplatz und Kleidungswechsel verringern die Aufnahme "
                            "über die Haut.",
                    "required": True,
                    "show_if": {"id": "benzol_taetigkeiten", "not_in": ["keine"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Anzeichen, auf die bei Benzol besonders geachtet wird",
            "questions": [
                {
                    "id": "blutungsneigung",
                    "type": "yes_no",
                    "label": "Haben Sie eine erhöhte Blutungsneigung bemerkt – z. B. Zahnfleischbluten, "
                             "blaue Flecken (Blutergüsse) schon bei leichten Stößen oder eine "
                             "verstärkte/verlängerte Monatsblutung?",
                    "required": True,
                    "followup": {"id": "blutungsneigung_desc", "type": "textarea",
                                 "label": "Was genau, und seit wann?", "when": "yes"},
                },
                {
                    "id": "infektneigung",
                    "type": "yes_no",
                    "label": "Sind Sie in letzter Zeit auffällig oft krank, z. B. häufige Infekte "
                             "oder Entzündungen (vermehrte Infektneigung)?",
                    "required": True,
                },
                {
                    "id": "anaemie_symptome",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich ungewöhnlich müde, blass oder schnell erschöpft, "
                             "oder bekommen Sie bei Belastung schlecht Luft?",
                    "hint": "Solche Beschwerden können auf eine Blutarmut (Anämie) hinweisen.",
                    "required": True,
                },
                {
                    "id": "akutbeschwerden",
                    "type": "multi_choice",
                    "label": "Treten bei oder kurz nach der Arbeit folgende Beschwerden auf?",
                    "hint": "Mehrfachauswahl möglich. Benzol kann Haut und Schleimhäute reizen und "
                            "auf das Nervensystem wirken.",
                    "required": True,
                    "options": [
                        {"value": "kopfschmerzen", "label": "Kopfschmerzen"},
                        {"value": "uebelkeit", "label": "Übelkeit"},
                        {"value": "schwindel", "label": "Schwindel oder Benommenheit"},
                        {"value": "reizung", "label": "Gereizte Haut, Augen oder Atemwege (Brennen, Rötung)"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen und Alkohol ────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Alkohol",
            "subtitle": "Erkrankungen, die bei Benzol-Belastung besonders wichtig sind",
            "questions": [
                {
                    "id": "blut_erkrankung",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung des Blutes oder der blutbildenden Organe "
                             "(Knochenmark) bekannt – z. B. Blutarmut (Anämie), Mangel an weißen "
                             "Blutkörperchen oder Blutplättchen, Leukämie oder Lymphom?",
                    "required": True,
                    "followup": {"id": "blut_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, wie behandelt?", "when": "yes"},
                },
                {
                    "id": "chron_infektionen",
                    "type": "yes_no",
                    "label": "Haben Sie eine chronische oder immer wiederkehrende bakterielle "
                             "Infektion (dauerhafte Entzündung durch Bakterien)?",
                    "required": True,
                    "followup": {"id": "chron_infektionen_desc", "type": "text",
                                 "label": "Welche Infektion?", "when": "yes"},
                },
                {
                    "id": "alkohol_konsum",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Alkohol kann die Laborwerte des Biomonitorings (Benzol-Messwerte im "
                            "Urin) beeinflussen.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "selten", "label": "Selten (höchstens 1-mal pro Woche)"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche)"},
                        {"value": "taeglich", "label": "Täglich"},
                    ],
                },
                {
                    "id": "alkohol_abhaengigkeit",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen jemals eine Alkoholabhängigkeit festgestellt oder "
                             "behandelt?",
                    "required": True,
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
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"blut_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hämatologische Erkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4 (Beurteilungskriterien)",
     "befund": "Erkrankung des Blutes bzw. der blutbildenden Organe angegeben.",
     "konsequenz": "Großes Blutbild veranlassen, Vorbefunde einholen; in unklaren Fällen "
                   "ergänzende hämatologische Diagnostik. Beurteilung nach 7.4: prüfen, ob die "
                   "Tätigkeit ohne gesundheitliche Gefährdung möglich ist – Maßnahmen nach 7.4.2 "
                   "(Substitution, technische/organisatorische Schutzmaßnahmen, Expositions-"
                   "begrenzung, Einsatz an Arbeitsplätzen mit geringerer Exposition, PSA), bei zu "
                   "erwartender Zunahme des Schweregrads verkürzte Vorsorgefristen nach 7.4.3; "
                   "bleiben Maßnahmen ohne Erfolg, Tätigkeitswechsel nach 7.4.4 erwägen "
                   "(Mitteilung an den Arbeitgeber nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"chron_infektionen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Infektionen",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Chronische bzw. bakterielle Infektion angegeben.",
     "konsequenz": "Chronische/bakterielle Infektionen sind nach 7.4 beurteilungsrelevant: "
                   "Ausprägung ärztlich klären (großes Blutbild, ggf. hämatologische Diagnostik); "
                   "Maßnahmen nach 7.4.2 bzw. verkürzte Vorsorgefristen nach 7.4.3 prüfen."},
    {"wenn": {"alkohol_abhaengigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 6.4 und 7.4",
     "befund": "Alkoholabhängigkeit angegeben.",
     "konsequenz": "Alkoholabhängigkeit ist nach 7.4 beurteilungsrelevant: Beurteilung, ob die "
                   "Tätigkeit ohne gesundheitliche Gefährdung möglich ist; Maßnahmen nach 7.4.2 "
                   "bzw. verkürzte Fristen nach 7.4.3 prüfen. Beratung und Vermittlung von "
                   "Hilfsangeboten; Alkoholkonsum als Störfaktor (Confounder) bei der "
                   "Interpretation des Biomonitorings berücksichtigen."},
    # ── Zielorgan-Symptome (Abschnitt 7.1, »besonders achten auf«) ────────
    {"wenn": {"blutungsneigung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Blutungsneigung",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Erhöhte Blutungsneigung angegeben (z. B. Zahnfleischbluten, Sugillationen bei "
               "geringfügigen Traumen, verstärkte Monatsblutung).",
     "konsequenz": "Vertiefte Anamnese mit validiertem Blutungsfragebogen (Luxembourg et al. "
                   "2007); großes Blutbild veranlassen; in unklaren Fällen ergänzende "
                   "hämatologische Diagnostik. Ergebnis bei der Beurteilung nach 7.4 "
                   "berücksichtigen, ggf. verkürzte Vorsorgefrist nach 7.4.3."},
    {"wenn": {"infektneigung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Infektneigung",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Vermehrte Infektneigung angegeben.",
     "konsequenz": "Großes Blutbild (mit Differenzialblutbild) veranlassen; in unklaren Fällen "
                   "ergänzende hämatologische Diagnostik zur Abklärung einer möglichen "
                   "Knochenmarksschädigung durch Benzol."},
    {"wenn": {"anaemie_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Anämie-Symptome",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Müdigkeit, Blässe bzw. Belastungsluftnot angegeben (mögliche Anämie-Zeichen).",
     "konsequenz": "Großes Blutbild veranlassen (chronische Benzolwirkung kann das "
                   "hämatopoetische System schädigen, z. B. aplastische Anämie, Panzytopenie); "
                   "in unklaren Fällen hämatologische Diagnostik."},
    {"wenn": {"akutbeschwerden": ["kopfschmerzen", "uebelkeit", "schwindel", "reizung"]},
     "schwere": "pruefen",
     "bereich": "Akutbeschwerden",
     "quelle": "Abschnitte 6.3.2 und 8.2",
     "befund": "Arbeitsplatzbezogene Beschwerden angegeben (ZNS-Symptome bzw. Reizung von "
               "Haut/Schleimhäuten).",
     "konsequenz": "Expositionssituation klären (Arbeitsplatzverhältnisse, Expositionsspitzen); "
                   "Biomonitoring zum Expositions-/Schichtende erwägen (Benzol im Urin, "
                   "S-Phenylmercaptursäure, t,t-Muconsäure). Ergeben sich Anhaltspunkte für "
                   "unzureichende Schutzmaßnahmen, Mitteilung an das Unternehmen und Vorschlag "
                   "von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    # ── Exposition und Schutzmaßnahmen (Abschnitte 2, 6.2, 8) ─────────────
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautkontakt",
     "quelle": "Abschnitte 2, 6.2 und 8.1",
     "befund": "Regelmäßiger Hautkontakt mit Benzol bzw. benzolhaltigen Gemischen angegeben.",
     "konsequenz": "Signifikante Aufnahme über die Haut möglich: prüfen, ob der "
                   "Pflichtvorsorge-Tatbestand (Gesundheitsgefährdung durch Hautkontakt) erfüllt "
                   "ist. Biomonitoring erwägen, da es auch die dermale Aufnahme erfasst. Beratung "
                   "zu PSA (geeignete Handschuhmaterialien nach Sicherheitsdatenblatt bzw. "
                   "GESTIS/GISCHEM/WINGIS); dem Unternehmen ggf. zusätzliche Schutzmaßnahmen "
                   "vorschlagen (§ 6 (4) ArbMedVV, TRGS 401)."},
    {"wenn": {"psa_benutzung": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Schutzausrüstung",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Keine persönliche Schutzausrüstung bei Tätigkeiten mit möglichem Benzol-Kontakt.",
     "konsequenz": "Intensive Beratung: wegen der hautresorptiven Eigenschaften von Benzol hat "
                   "PSA besondere Bedeutung (Vermeiden von Inhalation und Hautkontakt). "
                   "Anhaltspunkt für unzureichende Schutzmaßnahmen: Mitteilung an das Unternehmen "
                   "und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV); Überprüfung der "
                   "Gefährdungsbeurteilung anregen."},
    {"wenn": {"psa_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Schutzausrüstung",
     "quelle": "Abschnitt 8.1",
     "befund": "Probleme mit der Schutzausrüstung angegeben.",
     "konsequenz": "Individuelle PSA-Beratung: geeignete Handschuhmaterialien nach "
                   "Sicherheitsdatenblatt und den Portalen GESTIS, GISCHEM und WINGIS auswählen; "
                   "beschädigte/undichte PSA ersetzen lassen."},
    {"wenn": {"kleidung_wechsel": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Benetzte Arbeitskleidung wird nicht sofort gewechselt bzw. Haut nicht gereinigt.",
     "konsequenz": "Beratung zu Hygienemaßnahmen am Arbeitsplatz: benetzte Kleidung sofort "
                   "wechseln, Haut reinigen, Vermeiden von Hautkontakt und Inhalation – wichtig "
                   "wegen der Hautresorption von Benzol."},
    {"wenn": {"grenzwert_ueberschreitung": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "Abschnitte 6 (TRGS 910), 7.1 und 7.2.2",
     "befund": "Überschreitung der Akzeptanz- bzw. Toleranzkonzentration am Arbeitsplatz "
               "angegeben.",
     "konsequenz": "Gefährdungsbeurteilung einsehen; Biomonitoring durchführen (Urinprobe zum "
                   "Expositions-/Schichtende: Benzol, S-Phenylmercaptursäure, t,t-Muconsäure; "
                   "Äquivalenzwerte zur Toleranz-/Akzeptanzkonzentration nach TRGS 910 "
                   "heranziehen; S-Phenylmercaptursäure ist am spezifischsten). Bei "
                   "Überschreitungen Mitteilung an das Unternehmen und Vorschlag von "
                   "Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    # ── Krebserzeugender Stoff: nachgehende Vorsorge ──────────────────────
    {"wenn": {"vorsorge_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2 und 7.2.2",
     "befund": "Termin im Rahmen der nachgehenden Vorsorge (Tätigkeit mit Benzol beendet).",
     "konsequenz": "Untersuchungsumfang der nachgehenden Vorsorge: großes Blutbild; das "
                   "Biomonitoring kann in der Regel entfallen. In unklaren Fällen hämatologische "
                   "Diagnostik. Fortführung der nachgehenden Vorsorge über das Meldeportal "
                   "»DGUV Vorsorge« (www.dguv-vorsorge.de) sicherstellen."},
    {"wenn": {"fruehere_exposition": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2 und 8.1",
     "befund": "Frühere Tätigkeiten mit Benzol-Exposition angegeben.",
     "konsequenz": "Frühere Expositionen dokumentieren. Beratung zur nachgehenden Vorsorge: "
                   "Benzol ist krebserzeugend (Kategorie 1A), nach dem Ausscheiden aus der "
                   "Tätigkeit besteht Anspruch auf nachgehende Vorsorge; Anmeldung über das "
                   "Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de) prüfen bzw. anregen."},
    # ── Beratung ──────────────────────────────────────────────────────────
    {"wenn": {"alkohol_konsum": ["regelmaessig", "taeglich"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitt 6.4 (Störfaktoren)",
     "befund": "Regelmäßiger bzw. täglicher Alkoholkonsum angegeben.",
     "konsequenz": "Alkoholkonsum als Störfaktor (Confounder) bei der Interpretation der "
                   "Biomonitoring-Ergebnisse berücksichtigen; Beratung zum Alkoholkonsum."},
]
