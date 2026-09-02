# -*- coding: utf-8 -*-
"""G 33 Aromatische Nitro- oder Aminoverbindungen – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016,
G 33 »Aromatische Nitro- oder Aminoverbindungen« (Fassung Oktober 2014),
S. 471–482."""

SLUG = "g33-ana-2016"

CATALOG = {
    "version": 2,
    "title": "G 33 Aromatische Nitro- oder Aminoverbindungen (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 33 »Aromatische Nitro- oder Aminoverbindungen« (Fassung Oktober 2014), "
             "S. 471–482",
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
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. Nachuntersuchung: "
                            "in der Regel nach 6–12 Monaten. Nachgehende Untersuchung: nach "
                            "dem Ende der Tätigkeit (Organisation über ODIN).",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich wurde schon einmal untersucht)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (Tätigkeit ist beendet)"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kontakt mit den Stoffen",
            "subtitle": "Ihre Arbeit mit aromatischen Nitro- oder Aminoverbindungen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "arbeitsbereich",
                    "type": "multi_choice",
                    "label": "In welchen Bereichen arbeiten Sie mit diesen Stoffen?",
                    "hint": "Aromatische Nitro- oder Aminoverbindungen stecken z. B. in "
                            "Farbstoffen, Sprengstoffen oder Gummi-Zusätzen. "
                            "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "farbstoffe", "label": "Herstellen/Verarbeiten von Farbstoffen oder Haarfärbemitteln"},
                        {"value": "explosivstoffe", "label": "Herstellen/Verarbeiten von Explosivstoffen"},
                        {"value": "pflanzenschutz", "label": "Schädlingsbekämpfungs- oder Unkrautvernichtungsmittel"},
                        {"value": "arzneimittel", "label": "Arzneimittel- oder Fotoentwickler-Herstellung"},
                        {"value": "gummi", "label": "Gummiindustrie (Reaktionsbeschleuniger, Oxidationshemmer)"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an alten Produktionsanlagen"},
                        {"value": "sonstiges", "label": "Anderer Bereich"},
                    ],
                },
                {
                    "id": "krebs_amine",
                    "type": "choice",
                    "label": "Arbeiten Sie nach Ihrer Kenntnis mit krebserzeugenden "
                             "aromatischen Aminen (z. B. Benzidin, 2-Naphthylamin, "
                             "4-Aminodiphenyl, 4-Chlor-o-toluidin)?",
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
                             "Stoffen (z. B. Verschütten, Leckage, erhöhte Belastung)?",
                    "required": True,
                    "followup": {"id": "zwischenfall_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_exposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit aromatischen "
                             "Nitro- oder Aminoverbindungen?",
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
                                 "label": "Wann, wie oft, und wurde die Ursache schon "
                                          "urologisch geklärt?", "when": "yes"},
                },
                {
                    "id": "blasenbeschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie derzeit eine Blasenentzündung oder Beschwerden beim "
                             "Wasserlassen (Brennen, Schmerzen, sehr häufiger Harndrang)?",
                    "required": True,
                },
                {
                    "id": "akute_vergiftung",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal eine akute Vergiftung durch aromatische "
                             "Nitro- oder Aminoverbindungen (z. B. mit Blaufärbung der Haut, "
                             "Bewusstseinsstörung, Krankenhausbehandlung)?",
                    "required": True,
                    "followup": {"id": "akute_vergiftung_desc", "type": "textarea",
                                 "label": "Wann, wodurch, und sind Sie wieder vollständig "
                                          "gesund?", "when": "yes"},
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
                            "auf aromatische Nitro- oder Aminoverbindungen.",
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
            ],
        },
        # ── 5 ─ Seit der letzten Untersuchung ──────────────────────────────
        {
            "id": "zwischenanamnese",
            "title": "Seit der letzten Untersuchung",
            "subtitle": "Nur bei Nachuntersuchung",
            "questions": [
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder "
                             "längere Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung von "
                             "Ihnen und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                },
            ],
        },
        # ── 6 ─ Alkohol ────────────────────────────────────────────────────
        {
            "id": "genussmittel",
            "title": "Alkohol",
            "subtitle": "Alkohol kann die Wirkung dieser Stoffe stark verstärken",
            "questions": [
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Trinken Sie Alkohol?",
                    "hint": "Schon kleine Alkoholmengen können die Giftwirkung aromatischer "
                            "Nitro- oder Aminoverbindungen um ein Vielfaches steigern.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, gar nicht"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "regelmaessig", "label": "Regelmäßig"},
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
    # ── Befristete Bedenken (2.1.2) ───────────────────────────────────────
    {"wenn": {"haematurie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Harnwege",
     "quelle": "Abschnitte 2.1.2 und 1.2.3",
     "befund": "Blut im Urin (Hämaturie) angegeben.",
     "konsequenz": "Bei wiederholter Mikrohämaturie befristete gesundheitliche Bedenken bis "
                   "zur endgültigen urologischen Klärung der Blutungsquelle. "
                   "Ergänzungsuntersuchung veranlassen: zytologische Untersuchung des "
                   "Urinsediments nach Papanicolaou (Morgen-Mittelstrahlurin), bei "
                   "wiederholter Mikrohämaturie oder pathologischen Zellen urologische "
                   "Untersuchung (Zystoskopie, Ultraschalldiagnostik)."},
    {"wenn": {"blasenbeschwerden": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Harnwege",
     "quelle": "Abschnitt 2.1.2",
     "befund": "Aktuelle Blasenentzündung bzw. Beschwerden beim Wasserlassen angegeben.",
     "konsequenz": "Bei akuter oder chronischer Zystitis befristete gesundheitliche Bedenken "
                   "bis zur Ausheilung aussprechen; Urinstatus (Mehrfachteststreifen, "
                   "Sediment) erheben, Behandlung veranlassen und Ausheilung vor "
                   "(Wieder-)Aufnahme der Tätigkeit kontrollieren."},
    {"wenn": {"akute_vergiftung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Akute Intoxikation",
     "quelle": "Abschnitte 2.1.2 und 1.2.2",
     "befund": "Akute Intoxikation durch aromatische Nitro-/Aminoverbindungen in der "
               "Vorgeschichte angegeben.",
     "konsequenz": "Nach akuter Intoxikation befristete gesundheitliche Bedenken bis zur "
                   "Normalisierung des klinischen Befundes und der Laborwerte: großes "
                   "Blutbild, Leberwerte (SGPT/SGOT/γ-GT), Kreatinin, Urinstatus und "
                   "Methämoglobin kontrollieren; erst danach Fortsetzung der Tätigkeit "
                   "beurteilen."},
    {"wenn": {"zyanose": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Akute Beschwerden",
     "quelle": "Abschnitte 3.2.2, 1.2.2 und 2.1.2",
     "befund": "Grau-bläuliche Verfärbung von Lippen/Wangen/Ohren/Nägeln (Zyanose) bei oder "
               "nach der Arbeit angegeben.",
     "konsequenz": "Verdacht auf Methämoglobinämie: Methämoglobin als Indikator akuter "
                   "Exposition bestimmen, großes Blutbild; bis zur Klärung bzw. "
                   "Normalisierung Bedenken gegen die Fortsetzung der Tätigkeit erwägen. "
                   "Arbeitgeber-Hinweis zur Aktualisierung der Gefährdungsbeurteilung "
                   "(Abschnitt 2.2) unter Wahrung der schutzwürdigen Belange."},
    # ── Dauernde Bedenken (2.1.1) – Schweregrad ärztlich klären ───────────
    {"wenn": {"vorerkrankung_blase": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Harnwege",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Chronische Erkrankung der Blase/ableitenden Harnwege bzw. Neubildung in der "
               "Vorgeschichte.",
     "konsequenz": "Bei schwerer Ausprägung (insbesondere Neubildungen) dauernde "
                   "gesundheitliche Bedenken gegen die Tätigkeit. Vorbefunde einholen, "
                   "Ergänzungsuntersuchung (Blasen-/Nierendiagnostik, Urinzytologie nach "
                   "Papanicolaou); nur bei weniger ausgeprägten Störungen Aufnahme/ "
                   "Fortsetzung unter Voraussetzungen nach 2.1.3 (Schutzmaßnahmen, "
                   "geringere Exposition, verkürzte Nachuntersuchungsfristen) prüfen."},
    {"wenn": {"vorerkrankung_blut": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Blut",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Erkrankung des Blutes oder der Blutbildung (z. B. Sichelzellenanämie) "
               "angegeben.",
     "konsequenz": "Bei schwerer Gesundheitsstörung dauernde gesundheitliche Bedenken "
                   "(erhöhte Empfindlichkeit gegenüber Methämoglobinbildnern). Großes "
                   "Blutbild und ggf. Differentialblutbild bewerten; bei weniger "
                   "ausgeprägten Störungen Voraussetzungen nach 2.1.3 und verkürzte "
                   "Nachuntersuchungsfristen prüfen."},
    {"wenn": {"vorerkrankung_leber": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Leber",
     "quelle": "Abschnitte 2.1.1, 2.1.3 und 1.2.2/1.2.3",
     "befund": "Lebererkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Bei schweren Leberschäden dauernde gesundheitliche Bedenken. Leberwerte "
                   "(SGPT/ALAT, SGOT/ASAT, γ-GT) bewerten, in unklaren Fällen "
                   "Ergänzungsuntersuchung mit weiterer Leberdiagnostik; bei "
                   "grenzwertigen Befunden ohne Symptome Vorgehen nach 2.1.3 "
                   "(Schutzmaßnahmen, verkürzte Fristen)."},
    {"wenn": {"vorerkrankung_niere": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Niere",
     "quelle": "Abschnitte 2.1.1, 2.1.3 und 1.2.2/1.2.3",
     "befund": "Nierenerkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Bei schweren Nierenschäden dauernde gesundheitliche Bedenken. Kreatinin "
                   "im Serum und Urinstatus bewerten, in unklaren Fällen "
                   "Ergänzungsuntersuchung mit weiterer Nierendiagnostik; bei weniger "
                   "ausgeprägten Störungen Voraussetzungen nach 2.1.3 prüfen."},
    {"wenn": {"allergie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Allergie",
     "quelle": "Abschnitte 2.1.1 und 3.2.1",
     "befund": "Substanzbezogene Allergie (z. B. gegen p-Phenylendiamin) angegeben.",
     "konsequenz": "Bei nachgewiesener Allergie gegen die Arbeitsstoffe dauernde "
                   "gesundheitliche Bedenken erwägen (kontaktallergische Dermatose mit "
                   "Rückfallgefahr, allergisches Bronchialasthma möglich). Auslösende "
                   "Stoffe mit den Arbeitsstoffen abgleichen; nur bei fehlender Relevanz "
                   "für den Arbeitsplatz keine Bedenken."},
    {"wenn": {"vorerkrankung_haut": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Haut",
     "quelle": "Abschnitte 2.1.1, 2.1.3 und 3.1.3",
     "befund": "Chronische Hauterkrankung mit möglicherweise gestörter Hautbarriere "
               "angegeben.",
     "konsequenz": "Bei schwerer chronischer Hauterkrankung mit gestörter Hautbarriere "
                   "dauernde gesundheitliche Bedenken (erleichterte Hautresorption). "
                   "Hautzustand beurteilen; bei weniger ausgeprägten Störungen "
                   "Voraussetzungen nach 2.1.3 (PSA unter Beachtung des Hautzustands, "
                   "verkürzte Nachuntersuchungsfristen) prüfen."},
    {"wenn": {"vorerkrankung_nerven_psyche": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem/Psyche",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Erkrankung des Nervensystems oder der Psyche angegeben.",
     "konsequenz": "Bei schweren Erkrankungen des peripheren/zentralen Nervensystems oder "
                   "der Psyche dauernde gesundheitliche Bedenken (ZNS-depressive Wirkung "
                   "der Stoffe). Ausmaß klären, fachärztliche Befunde einholen; bei "
                   "weniger ausgeprägten Störungen Voraussetzungen nach 2.1.3 prüfen."},
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Abhängigkeit",
     "quelle": "Abschnitte 2.1.1 und 2.2",
     "befund": "Alkohol-, Rauschmittel- oder Medikamentenabhängigkeit angegeben.",
     "konsequenz": "Bei bestehender Abhängigkeit dauernde gesundheitliche Bedenken erwägen "
                   "(Alkohol steigert die Giftwirkung der Stoffe erheblich). "
                   "Suchtanamnese vertiefen, Behandlung empfehlen; bei stabiler Abstinenz "
                   "Vorgehen nach 2.1.3 mit verkürzten Nachuntersuchungsfristen prüfen."},
    # ── Keine Bedenken unter Voraussetzungen (2.1.3) / Beratung (2.2) ─────
    {"wenn": {"favismus_g6pd": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Enzymdefekt",
     "quelle": "Abschnitte 1.2.2, 2.1.3 und 2.2",
     "befund": "Favismus bzw. G6PD-Mangel (Glukose-6-Phosphatdehydrogenase) angegeben.",
     "konsequenz": "G6PD-Bestimmung anbieten (nur freiwillig, Aufklärung nach "
                   "Gendiagnostikgesetz). Bei bestätigtem G6PD-Mangel von einer Tätigkeit "
                   "mit aromatischen Nitro- oder Aminoverbindungen abraten; wird die "
                   "Beschäftigung dennoch gewünscht: keine Bedenken nur unter "
                   "Voraussetzungen nach 2.1.3 mit verkürzten Nachuntersuchungsfristen."},
    {"wenn": {"krebs_amine": ["ja", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Krebserzeugende Amine",
     "quelle": "Abschnitte 1.2.3, 1.1 und 2.2",
     "befund": "Tätigkeit mit krebserzeugenden aromatischen Aminen angegeben bzw. "
               "Einstufung dem Probanden unbekannt.",
     "konsequenz": "Einstufung klären (auch Verunreinigungen wie 2-Naphthylamin in "
                   "1-Naphthylamin beachten). Bei krebserzeugenden aromatischen Aminen "
                   "Ergänzungsuntersuchung: Urinstatus, je nach Vorbefund alle 6–12 Monate "
                   "zytologische Untersuchung des Urinsediments nach Papanicolaou. "
                   "Beratung zur krebserzeugenden Wirkung (Harnwegstumoren u. U. "
                   "Jahrzehnte nach Expositionsende, BK-Nr. 1301); nachgehende "
                   "Untersuchungen nach Ausscheiden über ODIN (www.odin-info.de) "
                   "sicherstellen."},
    {"wenn": {"frueher_exposition": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorexposition",
     "quelle": "Abschnitte 1.2.3, 3.1.4 und 1.1",
     "befund": "Frühere Exposition gegenüber aromatischen Nitro-/Aminoverbindungen "
               "angegeben.",
     "konsequenz": "Prüfung auf Exposition gegen aromatische Amine durch Biomonitoring "
                   "(Nachweis im Urin oder im Hämoglobin-Konjugat, Abschnitt 3.1.4). "
                   "Frühere Tätigkeiten dokumentieren; Anspruch auf nachgehende "
                   "Untersuchungen (ODIN) prüfen."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle/Unfälle",
     "quelle": "Abschnitte 1.2.2 und 1.1",
     "befund": "Zwischenfall/Unfall mit erhöhter Belastung durch die Stoffe angegeben.",
     "konsequenz": "Methämoglobin als Indikator einer (akuten) Exposition bestimmen (z. B. "
                   "nach erhöhter Belastung durch Unfälle) und Biomonitoring durchführen; "
                   "nach ärztlichem Ermessen vorzeitige Nachuntersuchung ansetzen."},
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenanamnese",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen eine Fortsetzung der "
                   "Tätigkeit gibt; vorzeitige Nachuntersuchung mit vollständigem "
                   "Untersuchungsprogramm (Blutbild, Leberwerte, Kreatinin, Urinstatus, "
                   "ggf. Met-Hb und Biomonitoring) durchführen."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenanamnese",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Proband vermutet Zusammenhang zwischen eigener Erkrankung und der "
               "Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung veranlassen; Verdacht ärztlich abklären und "
                   "bei begründetem Verdacht auf eine Berufskrankheit (BK-Nr. 1301/1304) "
                   "Meldung an den Unfallversicherungsträger erwägen."},
    {"wenn": {"psa": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen/PSA",
     "quelle": "Abschnitte 2.2 und 3.1.3",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Eindringliche Beratung zu Hygienemaßnahmen und zum Tragen der PSA "
                   "(Aufnahme über Haut und Atemwege; kontaminierte Haut/Kleidung ist "
                   "häufige Vergiftungsursache). Ergibt sich Hinweis auf notwendige "
                   "Verbesserung des Arbeitsschutzes, Mitteilung an den Arbeitgeber zur "
                   "Aktualisierung der Gefährdungsbeurteilung – unter Wahrung der "
                   "schutzwürdigen Belange des Untersuchten."},
    {"wenn": {"alkohol": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 2.2 und 3.2.1",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung: Schon kleine Alkoholmengen können die Giftwirkung "
                   "aromatischer Nitro- oder Aminoverbindungen erheblich steigern; "
                   "Konsumreduktion empfehlen."},
]
