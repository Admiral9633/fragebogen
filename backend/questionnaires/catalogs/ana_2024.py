# -*- coding: utf-8 -*-
"""Aromatische Nitro- und Aminoverbindungen – DGUV Empfehlung 2024.
Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen,
1. Auflage 2024, »Aromatische Nitro- und Aminoverbindungen« (E ANA,
Fassung Januar 2022), S. 50–73."""

SLUG = "ana-2024"

CATALOG = {
    "version": 2,
    "title": "Aromatische Nitro- und Aminoverbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Aromatische Nitro- und Aminoverbindungen« (E ANA, "
             "Fassung Januar 2022), S. 50–73",
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
                    "hint": "Nachgehende Vorsorge: Untersuchung nach dem Ende einer Tätigkeit "
                            "mit krebserzeugenden Stoffen.",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge wegen dieser Stoffe"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich war schon einmal hier)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (Tätigkeit ist beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, z. B. bei "
                            "krebserzeugenden Stoffen oder wenn die Stoffe über die Haut "
                            "aufgenommen werden können. Angebotsvorsorge: Ihr Betrieb bietet "
                            "sie an. Wunschvorsorge: auf Ihren eigenen Wunsch.",
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
            "title": "Tätigkeit & Kontakt mit den Stoffen",
            "subtitle": "Ihre Arbeit mit aromatischen Nitro- und Aminoverbindungen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "arbeitsbereich",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie mit diesen Stoffen?",
                    "hint": "Aromatische Nitro- und Aminoverbindungen stecken z. B. in "
                            "Farbmitteln, Sprengstoffen oder Gummi-Zusätzen. Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "farbmittel", "label": "Herstellen/Verarbeiten von Farbmitteln oder Haarfärbemitteln"},
                        {"value": "explosivstoffe", "label": "Herstellen/Verarbeiten von Explosivstoffen (z. B. TNT)"},
                        {"value": "pflanzenschutz", "label": "Schädlingsbekämpfungs- oder Unkrautvernichtungsmittel"},
                        {"value": "arzneimittel", "label": "Arzneimittel- oder Foto-Chemikalien-Herstellung"},
                        {"value": "gummi", "label": "Gummiindustrie (Reaktionsbeschleuniger, Oxidationshemmer)"},
                        {"value": "abbruch", "label": "Abbruch-/Sanierungsarbeiten an alten Produktionsanlagen"},
                        {"value": "labor", "label": "Labor (laborübliche Mengen)"},
                        {"value": "lager", "label": "Nur Lagerung/Transport in geschlossenen Gebinden oder Messwarte"},
                        {"value": "sonstiges", "label": "Anderer Bereich"},
                    ],
                },
                {
                    "id": "stoffe_krebs",
                    "type": "choice",
                    "label": "Arbeiten Sie nach Ihrer Kenntnis mit krebserzeugenden Stoffen "
                             "dieser Gruppe (z. B. Benzidin, 2-Naphthylamin, o-Toluidin, "
                             "Dinitrotoluol)?",
                    "hint": "Diese Angabe steht auch in der Betriebsanweisung oder im "
                            "Sicherheitsdatenblatt Ihres Arbeitsplatzes.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt es bei Ihrer Arbeit zu Hautkontakt mit den Stoffen oder zu "
                             "Verunreinigungen von Haut oder Kleidung?",
                    "hint": "Diese Stoffe werden auch über die Haut aufgenommen. Verunreinigte "
                            "Haut und Kleidung sind eine häufige Ursache von Vergiftungen.",
                    "required": True,
                },
                {
                    "id": "zwischenfall",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle oder Unfälle mit diesen "
                             "Stoffen oder ungewöhnliche Betriebszustände (z. B. Verschütten, "
                             "Leckage, Störung)?",
                    "required": True,
                    "followup": {"id": "zwischenfall_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_exposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit aromatischen "
                             "Nitro- oder Aminoverbindungen oder ähnlichen Gefahrstoffen?",
                    "required": True,
                    "followup": {"id": "frueher_exposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "psa",
                    "type": "choice",
                    "label": "Tragen Sie beim Umgang mit den Stoffen die vorgesehene "
                             "Schutzausrüstung (z. B. Schutzhandschuhe, Schutzkleidung, "
                             "Atemschutz)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "kein_kontakt", "label": "Ich habe (noch) keinen direkten Umgang mit den Stoffen"},
                    ],
                },
                {
                    "id": "hygiene",
                    "type": "yes_no",
                    "label": "Halten Sie die Hygieneregeln am Arbeitsplatz ein (Hände waschen, "
                             "Kleidung wechseln, nicht am Arbeitsplatz essen, trinken oder "
                             "rauchen)?",
                    "required": True,
                    "show_if": {"id": "psa", "not_in": ["kein_kontakt"]},
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die mit diesen Stoffen zusammenhängen können",
            "questions": [
                {
                    "id": "zyanose",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach der Arbeit eine grau-bläuliche Verfärbung "
                             "von Lippen, Wangen, Ohren oder Fingernägeln bemerkt (Zyanose)?",
                    "hint": "Das kann ein Zeichen für Methämoglobin-Bildung sein – der "
                            "Blutfarbstoff kann dann weniger Sauerstoff transportieren.",
                    "required": True,
                },
                {
                    "id": "herz_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit Beklemmungsgefühl, Herzklopfen, "
                             "Schweißausbrüche oder Kurzatmigkeit?",
                    "required": True,
                },
                {
                    "id": "zns_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach der Arbeit Kopfschmerzen, Schwäche, "
                             "Schwindel, Übelkeit, Benommenheit oder ein rauschartiges Gefühl?",
                    "required": True,
                },
                {
                    "id": "reizung_augen_atemwege",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit gereizte Augen oder Atemwege (Brennen, "
                             "Tränen, Husten) oder anfallsartige Atemnot?",
                    "hint": "Einige dieser Stoffe reizen die Schleimhäute; bei Veranlagung "
                            "kann ein allergisches Asthma entstehen.",
                    "required": True,
                },
                {
                    "id": "hautbeschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Hautveränderungen durch die Arbeit, z. B. Verfärbungen, "
                             "Rötung, Juckreiz, Ekzem (nässenden Ausschlag) oder Blasen?",
                    "required": True,
                    "followup": {"id": "hautbeschwerden_desc", "type": "text",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "haematurie",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Blut im Urin (rötliche oder bräunliche "
                             "Verfärbung des Urins, Hämaturie)?",
                    "required": True,
                    "followup": {"id": "haematurie_desc", "type": "text",
                                 "label": "Wann, wie oft, und wurde das schon ärztlich "
                                          "abgeklärt?", "when": "yes"},
                },
                {
                    "id": "blasenbeschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Beschwerden beim Wasserlassen, z. B. Brennen, Schmerzen "
                             "oder sehr häufigen Harndrang (Hinweis auf Blasenentzündung)?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, die für die Beurteilung wichtig sind",
            "questions": [
                {
                    "id": "vorerkrankung_blut",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung des Blutes oder der "
                             "Blutbildung (z. B. Blutarmut/Anämie, Sichelzellenanämie)?",
                    "required": True,
                    "followup": {"id": "vorerkrankung_blut_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "favismus_g6pd",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen ein Favismus oder ein G6PD-Mangel bekannt "
                             "(angeborener Enzymmangel, oft mit Unverträglichkeit von "
                             "Saubohnen/dicken Bohnen)?",
                    "hint": "Menschen mit diesem Enzymmangel reagieren besonders empfindlich "
                            "auf aromatische Nitro- und Aminoverbindungen.",
                    "required": True,
                },
                {
                    "id": "vorerkrankung_leber",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Lebererkrankung (z. B. Hepatitis, "
                             "Fettleber, erhöhte Leberwerte)?",
                    "required": True,
                },
                {
                    "id": "vorerkrankung_niere",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Nierenerkrankung?",
                    "required": True,
                },
                {
                    "id": "vorerkrankung_blase",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine dauerhafte (chronische) Erkrankung der "
                             "Blase oder der Harnwege, z. B. wiederkehrende Blasenentzündungen, "
                             "Polypen, Geschwulste oder Tumoren?",
                    "required": True,
                    "followup": {"id": "vorerkrankung_blase_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, wann, und wie wurde sie "
                                          "behandelt?", "when": "yes"},
                },
                {
                    "id": "vorerkrankung_herz",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung des Herzens oder des "
                             "Kreislaufs?",
                    "required": True,
                },
                {
                    "id": "vorerkrankung_nerven_psyche",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung des Nervensystems (z. B. "
                             "Krampfanfälle, Lähmungen) oder eine seelische (psychische) "
                             "Erkrankung?",
                    "required": True,
                },
                {
                    "id": "allergie",
                    "type": "yes_no",
                    "label": "Reagieren Sie allergisch auf bestimmte Chemikalien, z. B. "
                             "Haarfärbemittel oder Gummi-Inhaltsstoffe (etwa p-Phenylendiamin)?",
                    "required": True,
                    "followup": {"id": "allergie_desc", "type": "text",
                                 "label": "Auf welche Stoffe, und mit welchen Beschwerden?",
                                 "when": "yes"},
                },
                {
                    "id": "vorerkrankung_haut",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Hauterkrankung, z. B. "
                             "Ekzeme, Neurodermitis oder sehr trockene, rissige Haut?",
                    "hint": "Bei gestörter Hautbarriere können die Stoffe leichter über die "
                            "Haut aufgenommen werden.",
                    "required": True,
                },
                {
                    "id": "abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Drogen oder Medikamenten?",
                    "required": True,
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "text",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Läuft bei Ihnen ein Berufskrankheiten-Verfahren, oder wurde bei "
                             "Ihnen eine Berufskrankheit anerkannt?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                },
            ],
        },
        # ── 5 ─ Rauchen und Alkohol ────────────────────────────────────────
        {
            "id": "genussmittel",
            "title": "Rauchen & Alkohol",
            "subtitle": "Beides kann die Wirkung dieser Stoffe verstärken",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Nikotin kann die Gesundheitsgefährdung durch diese Stoffe "
                            "verstärken. Der Raucherstatus ist auch für die Bewertung von "
                            "Laborwerten (Biomonitoring) wichtig.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, nie geraucht"},
                        {"value": "frueher", "label": "Früher geraucht, jetzt nicht mehr"},
                        {"value": "ja", "label": "Ja, ich rauche"},
                    ],
                },
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Trinken Sie Alkohol?",
                    "hint": "Schon kleine Alkoholmengen können die Giftwirkung dieser Stoffe "
                            "um ein Vielfaches steigern.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, gar nicht"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "regelmaessig", "label": "Regelmäßig"},
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
    # ── Akute Beschwerden / Zwischenfälle ─────────────────────────────────
    {"wenn": {"zyanose": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Akute Intoxikation",
     "quelle": "Abschnitte 6.3.2 und 7.2.2",
     "befund": "Grau-bläuliche Verfärbung von Lippen/Wangen/Ohren/Nägeln (Zyanose) "
               "bei oder nach der Arbeit angegeben.",
     "konsequenz": "Verdacht auf Methämoglobinämie vor Fortsetzung der Tätigkeit klären: "
                   "Met-Hb bestimmen (Indikator akuter Exposition), Blutbild und "
                   "Differentialblutbild, Biomonitoring nach Abschnitt 6.4. Bei bestätigter "
                   "Überschreitung Mitteilung an das Unternehmen und Vorschlag von "
                   "Schutzmaßnahmen (§ 6 (4) ArbMedVV); Gefährdungsbeurteilung überprüfen "
                   "lassen."},
    {"wenn": {"herz_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Beschwerden",
     "quelle": "Abschnitte 6.3.2 und 7.1",
     "befund": "Beklemmung, Herzklopfen, Schweißausbrüche oder Kurzatmigkeit bei der Arbeit.",
     "konsequenz": "Zielorgan-Symptomatik ärztlich abklären: Met-Hb und Blutbild bestimmen, "
                   "Abgleich der geschilderten Arbeitssituation mit der Gefährdungs- "
                   "beurteilung; kardiale Ursachen differentialdiagnostisch bedenken."},
    {"wenn": {"zns_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Beschwerden",
     "quelle": "Abschnitte 6.3.1, 6.3.2 und 7.1",
     "befund": "Kopfschmerzen, Schwindel, Übelkeit, Benommenheit oder rauschartiger Zustand "
               "(»Anilinpips«) bei oder nach der Arbeit.",
     "konsequenz": "Hinweis auf zentralnervöse Wirkung: Expositionssituation klären, Met-Hb "
                   "und Biomonitoring veranlassen; ungewöhnliche Betriebszustände erfragen "
                   "und dokumentieren. Bei Anhaltspunkten für unzureichende Schutzmaßnahmen "
                   "Mitteilung an das Unternehmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle/Unfälle",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Zwischenfall, Unfall oder ungewöhnlicher Betriebszustand mit den Stoffen "
               "angegeben.",
     "konsequenz": "Hergang dokumentieren; Methämoglobin als Indikator einer (akuten) "
                   "Exposition bestimmen und Biomonitoring (Urin bzw. Hämoglobin-Konjugat, "
                   "Abschnitt 6.4) durchführen. Erkenntnisse dem Unternehmen für die "
                   "Überprüfung der Gefährdungsbeurteilung mitteilen."},
    # ── Harnwege ──────────────────────────────────────────────────────────
    {"wenn": {"haematurie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Harnwege",
     "quelle": "Abschnitte 7.1 (Beschwerden: Hämaturie) und 7.2.2",
     "befund": "Blut im Urin (Hämaturie) angegeben.",
     "konsequenz": "Urinstatus (Mehrfachteststreifen, Sediment) erheben; in unklaren Fällen "
                   "ergänzend weitere Blasen- und Nierendiagnostik veranlassen und "
                   "urologische Abklärung empfehlen. Bei Exposition gegenüber "
                   "krebserzeugenden aromatischen Aminen an Harnwegstumoren denken "
                   "(BK-Nr. 1301)."},
    {"wenn": {"blasenbeschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Harnwege",
     "quelle": "Abschnitte 6.3.2/6.3.3 und 7.2.2",
     "befund": "Beschwerden beim Wasserlassen (Hinweis auf Zystitis) angegeben.",
     "konsequenz": "Urinstatus erheben; Abklärung und Behandlung einer (hämorrhagischen) "
                   "Zystitis veranlassen. In unklaren Fällen weitere Blasen- und "
                   "Nierendiagnostik; Verlaufskontrolle vor der nächsten Vorsorge."},
    {"wenn": {"vorerkrankung_blase": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Harnwege",
     "quelle": "Abschnitte 7.4, 7.4.2–7.4.4",
     "befund": "Chronische Erkrankung der Blase/ableitenden Harnwege bzw. Neubildung in der "
               "Vorgeschichte.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Ausmaß klären, Vorbefunde "
                   "einholen; prüfen, ob die Tätigkeit ohne gesundheitliche Gefährdung "
                   "möglich ist. Maßnahmen nach 7.4.2 (Substitution, technische/ "
                   "organisatorische Schutzmaßnahmen, Einsatz mit geringerer Exposition) "
                   "und verkürzte Vorsorgefristen nach 7.4.3 empfehlen; bleiben diese ohne "
                   "Erfolgsaussicht, Tätigkeitswechsel nach 7.4.4 erwägen (Mitteilung an "
                   "den Arbeitgeber nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    # ── Weitere beurteilungsrelevante Vorerkrankungen (7.4) ───────────────
    {"wenn": {"vorerkrankung_blut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Blut",
     "quelle": "Abschnitte 6.3.1 und 7.4",
     "befund": "Erkrankung des Blutes oder der Blutbildung (z. B. Anämie, Sichelzellenanämie) "
               "angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Blutbild/Differentialblutbild "
                   "bewerten, erhöhte Empfindlichkeit gegenüber Methämoglobinbildnern "
                   "berücksichtigen. Maßnahmen nach 7.4.2 bzw. verkürzte Fristen nach 7.4.3 "
                   "prüfen; ggf. Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"favismus_g6pd": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Enzymdefekt",
     "quelle": "Abschnitte 6.3.1, 7.1, 7.2.2 und 7.4 (G6PDH-Mangel)",
     "befund": "Favismus bzw. G6PD-Mangel (Glukose-6-Phosphatdehydrogenase) angegeben.",
     "konsequenz": "Erhöhte Empfindlichkeit gegenüber aromatischen Nitro- und "
                   "Aminoverbindungen: G6PD-Bestimmung anbieten (nur freiwillig, Aufklärung "
                   "nach Gendiagnostikgesetz). Beurteilung nach 7.4; Maßnahmen nach 7.4.2 "
                   "(z. B. Einsatz mit geringerer Exposition) und verkürzte Vorsorgefristen "
                   "nach 7.4.3 empfehlen."},
    {"wenn": {"vorerkrankung_leber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Leber",
     "quelle": "Abschnitte 6.3.1, 7.2.2 und 7.4",
     "befund": "Lebererkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Leberwerte (SGPT/ALAT, SGOT/ASAT, γ-GT) bewerten; in unklaren Fällen "
                   "weitere Leberdiagnostik. Beurteilung nach 7.4 (Leberschäden); Maßnahmen "
                   "nach 7.4.2 bzw. verkürzte Fristen nach 7.4.3 prüfen – bestimmte "
                   "Verbindungen (z. B. 4,4'-Diaminodiphenylmethan, TNT) können "
                   "Leberstörungen bis zur toxischen Hepatitis verursachen."},
    {"wenn": {"vorerkrankung_niere": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Niere",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Nierenerkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Kreatinin im Serum und Urinstatus bewerten; in unklaren Fällen weitere "
                   "Nierendiagnostik. Beurteilung nach 7.4 (Nierenschäden); Maßnahmen nach "
                   "7.4.2 bzw. verkürzte Fristen nach 7.4.3 prüfen."},
    {"wenn": {"allergie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allergie",
     "quelle": "Abschnitte 6.3.1 und 7.4",
     "befund": "Substanzbezogene Allergie (z. B. gegen p-Phenylendiamin) angegeben.",
     "konsequenz": "Auslösende Stoffe klären und mit den Arbeitsstoffen abgleichen "
                   "(kontaktallergische Dermatose mit Rückfallgefahr, ggf. allergisches "
                   "Bronchialasthma). Beurteilung nach 7.4; vorrangig Substitution bzw. "
                   "Expositionsvermeidung nach 7.4.2 empfehlen, sonst Tätigkeitswechsel "
                   "nach 7.4.4 erwägen."},
    {"wenn": {"vorerkrankung_haut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.2, 6.3.1 und 7.4",
     "befund": "Chronische Hauterkrankung mit möglicherweise gestörter Hautbarriere angegeben.",
     "konsequenz": "Erleichterte Hautresorption berücksichtigen (Aufnahme über die Haut, "
                   "TRGS 401): Hautzustand beurteilen, Hautschutzplan und geeignete "
                   "Schutzhandschuhe beraten. Maßnahmen nach 7.4.2 bzw. verkürzte Fristen "
                   "nach 7.4.3 prüfen."},
    {"wenn": {"vorerkrankung_nerven_psyche": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem/Psyche",
     "quelle": "Abschnitte 6.3.1 und 7.4",
     "befund": "Erkrankung des Nervensystems oder der Psyche angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4 (ZNS-depressive Wirkung der "
                   "Stoffe): Ausmaß klären, ggf. fachärztliche Befunde einholen. Maßnahmen "
                   "nach 7.4.2 bzw. verkürzte Fristen nach 7.4.3 prüfen."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Abhängigkeit",
     "quelle": "Abschnitte 6.3.1, 7.4 und 8.1",
     "befund": "Alkohol-, Rauschmittel- oder Medikamentenabhängigkeit angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4; Wechselwirkungen beachten "
                   "(schon kleine Alkoholmengen steigern die Giftwirkung um das Vielfache). "
                   "Beratung und ggf. Behandlungsangebote; Maßnahmen nach 7.4.2 bzw. "
                   "verkürzte Fristen nach 7.4.3 prüfen."},
    # ── Exposition, Krebserzeuger, PSA ────────────────────────────────────
    {"wenn": {"frueher_exposition": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorexposition",
     "quelle": "Abschnitte 7.1 und 7.2.2 (Erstuntersuchung)",
     "befund": "Frühere Exposition gegenüber aromatischen Nitro-/Aminoverbindungen oder "
               "vergleichbaren Gefahrstoffen angegeben.",
     "konsequenz": "Bei Verdacht auf Vorexposition bereits bei der ersten Vorsorge "
                   "Biomonitoring durchführen (Nachweis im Urin oder Hämoglobin-Konjugat, "
                   "Abschnitt 6.4). Frühere Tätigkeiten dokumentieren; bei krebserzeugenden "
                   "Stoffen Anspruch auf nachgehende Vorsorge prüfen und Anmeldung über das "
                   "Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de) veranlassen."},
    {"wenn": {"stoffe_krebs": ["ja", "unbekannt"]},
     "schwere": "hinweis",
     "bereich": "Krebserzeugende Stoffe",
     "quelle": "Abschnitte 2 (Angebotsvorsorge/nachgehende Vorsorge), 6, 7.1 und 8.1",
     "befund": "Tätigkeit mit krebserzeugenden aromatischen Nitro-/Aminoverbindungen "
               "angegeben bzw. Einstufung dem Probanden unbekannt.",
     "konsequenz": "Einstufung anhand Gefährdungsbeurteilung/Sicherheitsdatenblatt klären "
                   "(auch krebserzeugende Verunreinigungen wie 2-Naphthylamin in "
                   "1-Naphthylamin beachten). Beratung zur krebserzeugenden und "
                   "keimzellmutagenen Wirkung (Harnwegstumoren auch Jahrzehnte nach "
                   "Expositionsende möglich, BK-Nr. 1301); AMR 11.1 beachten. Auf die "
                   "nachgehende Vorsorge nach dem Ausscheiden hinweisen und Anmeldung über "
                   "das Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de) sicherstellen."},
    {"wenn": {"psa": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen/PSA",
     "quelle": "Abschnitte 6.2, 8.1 und 8.2",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Eindringliche Beratung zum Tragen geeigneter PSA und zu "
                   "Hygienemaßnahmen (Aufnahme über Haut und Atemwege; kontaminierte Haut/ "
                   "Kleidung ist häufige Vergiftungsursache). Ursachen klären; ergeben sich "
                   "Anhaltspunkte, dass die Schutzmaßnahmen nicht ausreichen, Mitteilung an "
                   "das Unternehmen und Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV)."},
    # ── Genussmittel ──────────────────────────────────────────────────────
    {"wenn": {"rauchen": ["ja"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Aktueller Nikotinkonsum angegeben.",
     "konsequenz": "Beratung zur potenzierenden Wirkung des Nikotinkonsums auf die "
                   "Gesundheitsgefährdung durch aromatische Nitro- und Aminoverbindungen; "
                   "Tabakentwöhnung empfehlen. Raucherstatus bei der Bewertung des "
                   "Biomonitorings berücksichtigen (BAR-Werte gelten für Nichtrauchende)."},
    {"wenn": {"alkohol": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 6.3.1, 7.1 und 8.1",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung: Schon kleine Alkoholmengen steigern die Giftwirkung "
                   "aromatischer Nitro- und Aminoverbindungen bzw. ihrer Metabolite um das "
                   "Vielfache; Wechselwirkungen mit Alkohol/Rauschmitteln/Medikamenten "
                   "ansprechen und Konsumreduktion empfehlen."},
]
