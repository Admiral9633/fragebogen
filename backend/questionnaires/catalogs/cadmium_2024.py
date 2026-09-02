# -*- coding: utf-8 -*-
"""Cadmium und Cadmiumverbindungen – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen
für arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Cadmium und Cadmiumverbindungen« (E CAD, Fassung Januar 2022, Grenzwerte
aktualisiert 2024), S. 181–206."""

SLUG = "cadmium-2024"

CATALOG = {
    "version": 2,
    "title": "Cadmium und Cadmiumverbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Cadmium und Cadmiumverbindungen« (E CAD, Fassung "
             "Januar 2022, Grenzwerte aktualisiert 2024), S. 181–206",
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
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge wegen Cadmium (Tätigkeit beginnt oder läuft bereits)"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich war schon einmal zur Cadmium-Vorsorge)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (die Tätigkeit mit Cadmium ist beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Der Betrieb muss sie veranlassen, z. B. wenn der "
                            "Arbeitsplatzgrenzwert nicht eingehalten wird oder eine wiederholte "
                            "Exposition gegenüber krebserzeugenden Cadmiumverbindungen nicht "
                            "ausgeschlossen werden kann. Angebotsvorsorge: Der Betrieb bietet sie an.",
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
            "title": "Tätigkeit & Cadmium-Kontakt",
            "subtitle": "Ihre Arbeit und der Umgang mit Cadmium",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_verfahren",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten haben Sie Kontakt mit Cadmium oder "
                             "Cadmiumverbindungen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "herstellen_cd", "label": "Herstellen von Cadmium oder Cadmium-Legierungen (Rösten, Schmelzen, Gießen, Glühen, Staubfilter)"},
                        {"value": "verhuetten", "label": "Verhütten von Blei-, Zink- oder Kupfererzen"},
                        {"value": "cd_verbindungen", "label": "Herstellen von Cadmiumverbindungen oder Cadmium-Pigmenten (Farbstoffen)"},
                        {"value": "akkus", "label": "Herstellen von Nickel-Cadmium-Akkus (z. B. für Notbeleuchtung, Alarm- oder Medizintechnik)"},
                        {"value": "recycling", "label": "Recycling oder Verarbeiten cadmiumhaltiger Abfälle/Altmaterialien, Entfernen cadmiumhaltiger Anstriche"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an Anlagen, in denen Cadmium hergestellt oder verarbeitet wurde"},
                        {"value": "halbleiter_solar", "label": "Produktion von Halbleitern oder Solarpaneelen"},
                        {"value": "pigmente_farben", "label": "Arbeiten mit Cadmiumfarben, Emaillen, keramischen Farben oder Glasuren (auch Künstlerfarben/Restaurierung)"},
                        {"value": "loesliche_verbindungen", "label": "Lösliche Cadmiumverbindungen in der Foto-, Glas-, Gummi- oder Schmuckindustrie"},
                        {"value": "mechanisch", "label": "Trockenes mechanisches Bearbeiten cadmiumhaltiger Materialien (Staubentwicklung)"},
                        {"value": "labor_lager", "label": "Nur Labor, Lagerung oder Transport in dicht geschlossenen Gebinden"},
                        {"value": "andere", "label": "Andere Arbeiten mit Cadmium"},
                        {"value": "keine", "label": "Keine davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "heissverfahren",
                    "type": "yes_no",
                    "label": "Führen Sie Heißarbeiten an cadmiumhaltigen oder cadmiumbeschichteten "
                             "Materialien durch, z. B. Schweißen, thermisches Schneiden, Löten "
                             "(Hartlote), Glühen oder Bedampfen?",
                    "hint": "Dabei kann Cadmiumoxidrauch entstehen – das ist besonders belastend "
                            "für Atemwege und Lunge.",
                    "required": True,
                    "followup": {"id": "heissverfahren_desc", "type": "text",
                                 "label": "Welche Heißarbeiten, und wie oft?", "when": "yes"},
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit Cadmium oder "
                             "Cadmiumverbindungen (alle Tätigkeiten zusammengerechnet)?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis5", "label": "1 bis 5 Jahre"},
                        {"value": "5bis10", "label": "5 bis 10 Jahre"},
                        {"value": "ueber10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "frueher_cadmium",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit Cadmium oder anderen "
                             "Gefahrstoffen mit vergleichbarer Gefährdung (z. B. andere "
                             "krebserzeugende Metalle)?",
                    "required": True,
                    "followup": {"id": "frueher_cadmium_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, wie lange, und gab es "
                                          "dort arbeitsmedizinische Untersuchungen?", "when": "yes"},
                },
                {
                    "id": "zwischenfall",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Zwischenfälle, Unfälle oder ungewöhnliche "
                             "Betriebszustände, bei denen Sie viel cadmiumhaltigen Staub oder "
                             "Rauch eingeatmet haben könnten?",
                    "required": True,
                    "followup": {"id": "zwischenfall_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Schutzausrüstung und Verhalten am Arbeitsplatz",
            "questions": [
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei staub- oder rauchintensiven Arbeiten mit Cadmium "
                             "Atemschutz?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "Für meine Tätigkeit nicht vorgesehen / noch keine Tätigkeit"},
                    ],
                },
                {
                    "id": "hygiene",
                    "type": "multi_choice",
                    "label": "Welche Punkte treffen auf Ihren Arbeitsalltag zu?",
                    "hint": "Mehrfachauswahl möglich. Bitte antworten Sie ehrlich – das hilft "
                            "bei der Beratung.",
                    "required": True,
                    "options": [
                        {"value": "essen_am_platz", "label": "Ich esse, trinke oder rauche manchmal direkt am Arbeitsplatz"},
                        {"value": "haende_selten", "label": "Ich wasche mir vor Pausen (auch Raucherpausen) nicht immer gründlich die Hände"},
                        {"value": "kein_kleidungswechsel", "label": "Ich trage Arbeitskleidung auch nach Feierabend weiter / wechsle sie nicht"},
                        {"value": "alles_beachtet", "label": "Nichts davon – ich beachte die Hygieneregeln"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme mit Ihrer Schutzausrüstung (z. B. Atemschutzmaske "
                             "drückt, schlechter Sitz, Atemnot unter der Maske)?",
                    "required": True,
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die mit Cadmium zusammenhängen können",
            "questions": [
                {
                    "id": "geruchssinn",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Geruchssinn verschlechtert (Sie riechen schlechter "
                             "als früher oder gar nicht mehr)?",
                    "required": True,
                },
                {
                    "id": "atemwege_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere der folgenden Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Häufiger Husten"},
                        {"value": "auswurf", "label": "Auswurf (Schleim beim Husten)"},
                        {"value": "heiserkeit", "label": "Heiserkeit"},
                        {"value": "atemnot", "label": "Atemnot oder Kurzatmigkeit"},
                        {"value": "brustschmerzen", "label": "Schmerzen im Brustkorb"},
                        {"value": "nase_behindert", "label": "Behinderte Nasenatmung oder ständiger Schnupfen"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "metalldampffieber",
                    "type": "yes_no",
                    "label": "Hatten Sie nach Arbeiten mit Metallrauch (z. B. Schweißen, Löten) "
                             "schon einmal grippeartige Beschwerden wie Fieber, Frösteln, "
                             "Schweißausbruch oder Herzrasen (»Metalldampffieber«)?",
                    "hint": "Solche Beschwerden können erst mehrere Stunden bis 3 Tage nach dem "
                            "Einatmen von Cadmiumrauch auftreten.",
                    "required": True,
                    "followup": {"id": "metalldampffieber_desc", "type": "text",
                                 "label": "Wann zuletzt, und nach welcher Arbeit?", "when": "yes"},
                },
                {
                    "id": "allgemein_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine der folgenden Veränderungen bemerkt?",
                    "required": True,
                    "options": [
                        {"value": "gewichtsabnahme", "label": "Ungewollte Gewichtsabnahme"},
                        {"value": "muedigkeit", "label": "Auffallende Müdigkeit oder Abgeschlagenheit"},
                        {"value": "keine", "label": "Nichts davon"},
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
                    "id": "vorerkr_atemwege",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Erkrankungen der Atemwege oder der Lunge "
                             "(z. B. chronische Bronchitis, Asthma, COPD, Lungenemphysem, häufige "
                             "Nasennebenhöhlen-Entzündungen)?",
                    "required": True,
                    "followup": {"id": "vorerkr_atemwege_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, und sind Sie in Behandlung?",
                                 "when": "yes"},
                },
                {
                    "id": "vorerkr_niere",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Nierenerkrankung oder eine eingeschränkte "
                             "Nierenfunktion (z. B. Eiweiß im Urin, erhöhte Nierenwerte)?",
                    "hint": "Die Niere ist das wichtigste Zielorgan von Cadmium.",
                    "required": True,
                    "followup": {"id": "vorerkr_niere_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vorerkr_leber",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Lebererkrankung (z. B. Hepatitis, "
                             "Fettleber mit erhöhten Leberwerten, Leberzirrhose)?",
                    "required": True,
                    "followup": {"id": "vorerkr_leber_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vorerkr_diabetes",
                    "type": "yes_no",
                    "label": "Haben Sie einen Diabetes mellitus (Zuckerkrankheit)?",
                    "required": True,
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Berufskrankheit anerkannt oder läuft derzeit ein "
                             "Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Berufskrankheit bzw. welches Verfahren?", "when": "yes"},
                },
                {
                    "id": "gesundheit_sonstige",
                    "type": "yes_no",
                    "label": "Gibt es sonstige gesundheitliche Einschränkungen oder Erkrankungen, "
                             "die wir kennen sollten?",
                    "required": True,
                    "followup": {"id": "gesundheit_sonstige_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
                },
                {
                    "id": "schwanger",
                    "type": "choice",
                    "label": "Sind Sie zurzeit schwanger oder stillen Sie?",
                    "hint": "Cadmium kann das Kind im Mutterleib schädigen. Für Schwangere und "
                            "Stillende gelten besondere Schutzvorschriften (Mutterschutzgesetz).",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "entfaellt", "label": "Trifft auf mich nicht zu"},
                        {"value": "keine_angabe", "label": "Keine Angabe"},
                    ],
                },
            ],
        },
        # ── 6 ─ Rauchen, Alkohol, Ernährung ────────────────────────────────
        {
            "id": "genussmittel",
            "title": "Rauchen, Alkohol & Ernährung",
            "subtitle": "Wichtig für die Bewertung der Cadmium-Belastung (Biomonitoring)",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Tabakrauch enthält Cadmium: Rauchen führt zu einer zusätzlichen "
                            "Aufnahme von 1–3 µg Cadmium pro Tag und verstärkt die Belastung "
                            "durch die Arbeit.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "ex", "label": "Früher, aber nicht mehr"},
                        {"value": "bis10", "label": "Ja, bis etwa 10 Zigaretten pro Tag"},
                        {"value": "10bis20", "label": "Ja, etwa 10 bis 20 Zigaretten pro Tag"},
                        {"value": "ueber20", "label": "Ja, mehr als 20 Zigaretten pro Tag"},
                    ],
                },
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie oder sehr selten"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche bis täglich)"},
                        {"value": "abhaengigkeit", "label": "Ich habe oder hatte ein Alkoholproblem (Abhängigkeit)"},
                    ],
                },
                {
                    "id": "ernaehrung_cd",
                    "type": "yes_no",
                    "label": "Essen Sie regelmäßig größere Mengen cadmiumreicher Lebensmittel, "
                             "z. B. Leber, Pilze, Muscheln oder andere Schalentiere, Kakaopulver, "
                             "getrockneten Seetang oder täglich mehr als 20 g Leinsamen?",
                    "hint": "Diese Angabe hilft, Ihre Laborwerte (Cadmium im Urin/Blut) richtig "
                            "einzuordnen.",
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
    # ── Anlass / nachgehende Vorsorge ─────────────────────────────────────
    {"wenn": {"vorsorge_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2 (Angebotsvorsorge), 7.2.2 und 8.1",
     "befund": "Vorstellung zur nachgehenden Vorsorge nach Ende der Cadmium-Tätigkeit.",
     "konsequenz": "Programm der nachgehenden Untersuchung durchführen (u. a. Urinstatus, "
                   "Spirometrie, Kreatinin im Serum, β2-Mikroglobulin im Urin, Cadmium im Urin – "
                   "Cadmium im Blut entfällt); nach langjähriger Exposition Nierensonographie, "
                   "bei Auffälligkeiten in Anamnese/Untersuchung ggf. bildgebende Diagnostik des "
                   "Thorax (rechtfertigende Indikation). Registrierung über das Meldeportal "
                   "»DGUV Vorsorge« (www.dguv-vorsorge.de) prüfen."},
    # ── Exposition ────────────────────────────────────────────────────────
    {"wenn": {"heissverfahren": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hohe Exposition",
     "quelle": "Abschnitte 6.1.1 und 7.2.2 (ergänzende Untersuchungen bei hohen Expositionen)",
     "befund": "Heißarbeiten mit möglicher Bildung von Cadmiumoxidrauch angegeben "
               "(Schweißen, thermisches Schneiden, Löten, Glühen, Bedampfen).",
     "konsequenz": "Abgleich mit der Gefährdungsbeurteilung (A-Staub-Anteil!). Bei hoher "
                   "Cadmium-Exposition ergänzend Geruchssinnprüfung (z. B. Sniffin' Sticks) sowie "
                   "Nasenspiegelung und Funktionstest der Nasenatmung (z. B. anteriore "
                   "Rhinomanometrie) durchführen. DGUV Empfehlung »Rauche und Gase beim "
                   "Schweißen« und TRGS 528 beachten."},
    {"wenn": {"expo_dauer": ["ueber10"]},
     "schwere": "pruefen",
     "bereich": "Langjährige Exposition",
     "quelle": "Abschnitte 6.2.2 und 7.2.2 (Nachuntersuchung)",
     "befund": "Mehr als 10 Jahre Cadmium-Exposition angegeben.",
     "konsequenz": "Bei Nachuntersuchung nach langjähriger Exposition Nierensonographie "
                   "veranlassen. Kumulative Körperlast beachten (biologische Halbwertszeit "
                   "10–20 Jahre): Biomonitoring Cadmium im Urin (Langzeitbelastung) und im Blut "
                   "(aktuelle Belastung) im Verlauf bewerten."},
    {"wenn": {"frueher_cadmium": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorbelastung",
     "quelle": "Abschnitte 7.1 (Arbeitsanamnese), 7.2.2 (Erstuntersuchung) und 6.4.2",
     "befund": "Frühere Tätigkeiten mit Cadmium- oder vergleichbarer Gefahrstoff-Exposition.",
     "konsequenz": "Bereits vorhandene Belastung bei der Erstuntersuchung per Biomonitoring "
                   "(Cadmium im Urin) feststellen und bei Verlaufskontrollen die Ergebnisse der "
                   "Erstvorsorge berücksichtigen. Frühere Expositionen dokumentieren; Anspruch "
                   "auf nachgehende Vorsorge (Kategorie-1A/1B-Stoffe, DGUV Vorsorge) klären."},
    {"wenn": {"zwischenfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfall/Unfall",
     "quelle": "Abschnitte 7.1 (Arbeitsanamnese) und 6.3.2",
     "befund": "Zwischenfall bzw. ungewöhnlicher Betriebszustand mit möglicher hoher "
               "Staub-/Rauchexposition angegeben.",
     "konsequenz": "Ereignis dokumentieren und ärztlich abklären; an die Latenzzeit akuter "
                   "Wirkungen von mehreren Stunden bis zu 3 Tagen denken (u. U. Lungenödem, "
                   "Nierenschäden). Ergeben sich Anhaltspunkte für unzureichende Schutzmaßnahmen, "
                   "Mitteilung an das Unternehmen und Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV)."},
    # ── Beschwerden ───────────────────────────────────────────────────────
    {"wenn": {"geruchssinn": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Geruchssinn",
     "quelle": "Abschnitte 6.3.3, 7.1 (Beschwerden) und 7.2.2",
     "befund": "Verschlechterung oder Verlust des Geruchssinns angegeben.",
     "konsequenz": "Mögliches Zeichen chronischer Cadmium-Einwirkung (Atrophie der "
                   "Nasenschleimhäute): Geruchssinnprüfung (z. B. Sniffin' Sticks) sowie "
                   "Nasenspiegelung und Prüfung der Nasenatmung mittels Funktionstest "
                   "durchführen; ggf. HNO-ärztliche Abklärung veranlassen."},
    {"wenn": {"atemwege_beschwerden": ["husten", "auswurf", "heiserkeit", "atemnot",
                                       "brustschmerzen", "nase_behindert"]},
     "schwere": "pruefen",
     "bereich": "Atemwegsbeschwerden",
     "quelle": "Abschnitte 6.3.2, 6.3.3, 7.1 und 7.2.2",
     "befund": "Atemwegsbeschwerden angegeben (Husten, Auswurf, Heiserkeit, Atemnot, "
               "Brustschmerzen oder behinderte Nasenatmung).",
     "konsequenz": "Spirometrie-Befund besonders bewerten (obstruktive Ventilationsstörung, "
                   "Emphysem-Hinweise) und Prüfung der Nasenatmung durchführen; ggf. "
                   "weiterführende pneumologische Abklärung. Zusammenhang mit der Tätigkeit "
                   "prüfen und Beurteilung nach Abschnitt 7.4 vornehmen."},
    {"wenn": {"metalldampffieber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Rauchexposition",
     "quelle": "Abschnitte 6.3.2 und 8.2",
     "befund": "Metalldampffieber-artige Beschwerden nach Arbeiten mit Metallrauch angegeben.",
     "konsequenz": "Hinweis auf relevante inhalative Rauchexposition: Ereignisse und Umstände "
                   "klären, Nieren- und Lungenparameter kontrollieren. Dem Unternehmen "
                   "Überprüfung der Schutzmaßnahmen (Absaugung, Atemschutz) vorschlagen "
                   "(§ 6 (4) ArbMedVV)."},
    {"wenn": {"allgemein_beschwerden": ["gewichtsabnahme", "muedigkeit"]},
     "schwere": "pruefen",
     "bereich": "Allgemeinsymptome",
     "quelle": "Abschnitte 6.3.3 und 7.1 (Beschwerden)",
     "befund": "Ungewollte Gewichtsabnahme und/oder auffallende Müdigkeit angegeben.",
     "konsequenz": "Mögliche Zeichen einer chronischen Cadmium-Wirkung: ärztliche Abklärung "
                   "(u. a. Nieren- und Leberparameter, BSG/CRP) und Verlaufskontrolle; "
                   "differenzialdiagnostische Abklärung veranlassen."},
    # ── Vorerkrankungen (Beurteilung nach 7.4) ────────────────────────────
    {"wenn": {"vorerkr_atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 7.4, 7.4.2, 7.4.3 und 7.4.4",
     "befund": "Erkrankung der oberen oder tieferen Atemwege in der Vorgeschichte.",
     "konsequenz": "Beurteilungsrelevante Erkrankung: prüfen, ob die Tätigkeit ohne "
                   "gesundheitliche Gefährdung möglich ist. Maßnahmen nach 7.4.2 erwägen "
                   "(Substitution, technische/organisatorische Schutzmaßnahmen, Begrenzung der "
                   "Expositionszeit, expositionsärmerer Arbeitsplatz, geeignete PSA); bei zu "
                   "erwartender Änderung des Schweregrads verkürzte Vorsorgefristen (7.4.3); "
                   "bleiben Maßnahmen erfolglos, Tätigkeitswechsel erwägen (7.4.4, Mitteilung "
                   "nur mit Einwilligung)."},
    {"wenn": {"vorerkr_niere": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nierenerkrankung",
     "quelle": "Abschnitte 6.3.1, 7.4 und 7.4.2/7.4.3",
     "befund": "Nierenerkrankung bzw. eingeschränkte Nierenfunktion in der Vorgeschichte.",
     "konsequenz": "Niere ist das kritische Zielorgan von Cadmium: Nierenfunktion gezielt "
                   "abklären (Kreatinin im Serum, β2-Mikroglobulin im Urin, Urinstatus), "
                   "Vorbefunde einholen. Prüfen, ob die Tätigkeit ohne Gefährdung möglich ist; "
                   "Maßnahmen nach 7.4.2 und verkürzte Fristen nach 7.4.3 erwägen, bei "
                   "Erfolglosigkeit Tätigkeitswechsel (7.4.4)."},
    {"wenn": {"vorerkr_diabetes": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Diabetes mellitus",
     "quelle": "Abschnitte 7.1 (allgemeine Anamnese) und 7.4 (diabetische Nephropathie)",
     "befund": "Diabetes mellitus angegeben.",
     "konsequenz": "Erhöhtes Risiko einer diabetischen Nephropathie: Nierenparameter "
                   "(Kreatinin, β2-Mikroglobulin, Urinstatus) engmaschig bewerten, "
                   "Stoffwechseleinstellung erfragen. Bei Nephropathie Beurteilung nach 7.4 "
                   "mit Maßnahmen (7.4.2) bzw. verkürzten Fristen (7.4.3)."},
    {"wenn": {"vorerkr_leber": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lebererkrankung",
     "quelle": "Abschnitte 7.4 und 7.4.2",
     "befund": "Lebererkrankung in der Vorgeschichte.",
     "konsequenz": "Beurteilungsrelevante Erkrankung: Leberenzyme (SGOT, SGPT, γ-GT) gezielt "
                   "bewerten, Vorbefunde einholen. Prüfen, ob die Tätigkeit ohne Gefährdung "
                   "möglich ist; Maßnahmen nach 7.4.2 bzw. verkürzte Fristen nach 7.4.3 erwägen."},
    # ── Rauchen / Alkohol / Ernährung ─────────────────────────────────────
    {"wenn": {"rauchen": ["bis10", "10bis20", "ueber20"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 6.2.3, 6.4.1, 7.1 und 8.1",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung zur potenzierenden Wirkung des Rauchens (zusätzliche Aufnahme von "
                   "1–3 µg Cadmium/Tag) und Empfehlung zum Rauchstopp. Raucherstatus bei der "
                   "Bewertung des Biomonitorings berücksichtigen (BAR-Werte gelten für "
                   "Nichtraucher). Hygieneberatung: gründliches Händewaschen besonders vor "
                   "Raucherpausen."},
    {"wenn": {"rauchen": ["ueber20"]},
     "schwere": "pruefen",
     "bereich": "Erheblicher Nikotinabusus",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Erheblicher Nikotinkonsum (mehr als 20 Zigaretten täglich).",
     "konsequenz": "Erheblicher Nikotinabusus ist beurteilungsrelevant nach 7.4: prüfen, ob die "
                   "Tätigkeit ohne gesundheitliche Gefährdung möglich ist; Maßnahmen nach 7.4.2 "
                   "und intensive Tabakentwöhnungsberatung; ggf. verkürzte Vorsorgefristen "
                   "(7.4.3)."},
    {"wenn": {"alkohol": ["abhaengigkeit"]},
     "schwere": "pruefen",
     "bereich": "Alkoholabhängigkeit",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Alkoholabhängigkeit angegeben.",
     "konsequenz": "Beurteilungsrelevant nach 7.4 (u. a. wegen Leberbelastung und Gefahr "
                   "mangelhafter Hygiene): Leberwerte gezielt bewerten, Behandlungs- und "
                   "Beratungsangebote vermitteln. Maßnahmen nach 7.4.2 prüfen; bleiben sie "
                   "erfolglos, Tätigkeitswechsel erwägen (7.4.4)."},
    {"wenn": {"ernaehrung_cd": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Ernährung",
     "quelle": "Abschnitte 6.2.3 und 6.4.2",
     "befund": "Regelmäßiger Verzehr cadmiumreicher Lebensmittel angegeben.",
     "konsequenz": "Ernährungsgewohnheiten bei der Bewertung des Biomonitorings "
                   "berücksichtigen. Beratung: cadmiumreiche Lebensmittel maßvoll verzehren, "
                   "täglich nicht mehr als 20 g Leinsamen."},
    # ── Schutzmaßnahmen / Hygiene ─────────────────────────────────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Atemschutz",
     "quelle": "Abschnitte 7.1, 8.1 und 8.2",
     "befund": "Atemschutz wird bei staub-/rauchintensiven Arbeiten selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA und zu den Gefahren der "
                   "inhalativen Cadmium-Aufnahme; Ursachen der Nichtbenutzung klären. Ergeben "
                   "sich Anhaltspunkte, dass die Schutzmaßnahmen nicht ausreichen, Mitteilung an "
                   "das Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"hygiene": ["essen_am_platz", "haende_selten", "kein_kleidungswechsel"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 (allgemeine Beratung) und 8.1",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht durchgehend eingehalten.",
     "konsequenz": "Gezielte Hygieneberatung: kein Essen, Trinken oder Rauchen am Arbeitsplatz, "
                   "gründliches Händewaschen vor Pausen (besonders vor Raucherpausen), "
                   "konsequenter Wechsel der Arbeitskleidung – Vermeidung der oralen "
                   "Cadmium-Aufnahme."},
    # ── Mutterschutz ──────────────────────────────────────────────────────
    {"wenn": {"schwanger": ["ja"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6 (Tabelle 1: reproduktionstoxisch), 7.1 und 8.1 (MuSchG)",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben.",
     "konsequenz": "Cadmium und mehrere Cadmiumverbindungen sind reproduktionstoxisch "
                   "(entwicklungsschädigend): Beschäftigungsbeschränkungen nach dem "
                   "Mutterschutzgesetz unverzüglich klären, bevor die Tätigkeit (weiter) "
                   "ausgeübt wird; Anpassung der Gefährdungsbeurteilung und der "
                   "Arbeitsbedingungen mit dem Unternehmen abstimmen."},
]
