# -*- coding: utf-8 -*-
"""Blei und anorganische Bleiverbindungen – DGUV Empfehlung 2024.
Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen,
1. Auflage 2024, »Blei und anorganische Bleiverbindungen« (E APB, Fassung
Januar 2022, Grenzwerte aktualisiert 2024), S. 157–180."""

SLUG = "blei-2024"

CATALOG = {
    "version": 2,
    "title": "Blei und anorganische Bleiverbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Blei und anorganische Bleiverbindungen« (E APB, "
             "Fassung Januar 2022, Grenzwerte aktualisiert 2024), S. 157–180",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen Blei?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Blei-Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur Blei-Vorsorge"},
                        {"value": "nachgehend", "label": "Ich arbeite nicht mehr mit Blei "
                                                         "(nachgehende Vorsorge nach dem Ausscheiden)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn die "
                            "Bleikonzentration in der Luft über 75 µg/m³ liegt. "
                            "Angebotsvorsorge: bei Einhaltung dieses Wertes. "
                            "Wunschvorsorge: auf Ihren eigenen Wunsch.",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["erste", "weitere"]},
                    "options": [
                        {"value": "pflicht", "label": "Vom Betrieb verpflichtend veranlasst (Pflichtvorsorge)"},
                        {"value": "angebot", "label": "Vom Betrieb angeboten (Angebotsvorsorge)"},
                        {"value": "wunsch", "label": "Auf meinen eigenen Wunsch (Wunschvorsorge)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Bleibelastung ────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Bleibelastung",
            "subtitle": "Ihre Arbeit und der Kontakt mit Blei",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "blei_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Bei welchen Tätigkeiten haben Sie Kontakt mit Blei oder "
                             "bleihaltigen Materialien?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "huette", "label": "Bleihütte: Verhütten, Einschmelzen oder Raffinieren von Blei"},
                        {"value": "recycling", "label": "Recycling bleihaltiger Abfälle (z. B. alte Akkus, Altmetall)"},
                        {"value": "akku", "label": "Herstellung von Bleiakkumulatoren (Batterien)"},
                        {"value": "entschichten", "label": "Entfernen bleihaltiger Farben/Beschichtungen "
                                                           "(Abbrennen, Schleifen, Strahlen, Abbeizen)"},
                        {"value": "schweissen", "label": "Schweißen oder Brennschneiden an Teilen mit "
                                                         "bleihaltigen Anstrichen (z. B. Abbruch)"},
                        {"value": "loeten", "label": "Löten oder Weichlöten mit bleihaltigem Lot (z. B. Elektronik)"},
                        {"value": "elektronik", "label": "Zerlegen bleihaltiger Altgeräte (Elektro-/Elektronikschrott)"},
                        {"value": "farben", "label": "Bleipigmente, Bleiglasuren, bleihaltige Farben oder "
                                                     "keramischer Siebdruck"},
                        {"value": "dach_glas", "label": "Dacheindeckung mit Blei oder Bleiverglasung/Restaurierung"},
                        {"value": "munition", "label": "Bleihaltige Munition/Sprengmaterial oder Reinigen "
                                                       "von Schießständen"},
                        {"value": "reinigung", "label": "Reinigung, Wartung oder Instandsetzung in "
                                                        "bleibelasteten Bereichen; Wäsche kontaminierter Kleidung"},
                        {"value": "andere", "label": "Andere Tätigkeit mit Blei"},
                        {"value": "keine", "label": "Keine davon / weiß nicht"},
                    ],
                },
                {
                    "id": "blei_chromat_arsenat",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Bleichromat (z. B. Chromgelb, Königsgelb) "
                             "oder Bleiarsenat?",
                    "hint": "Diese beiden Bleiverbindungen sind krebserzeugend und werden "
                            "zusätzlich nach eigenen Empfehlungen betreut.",
                    "required": True,
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit Blei oder "
                             "bleihaltigen Materialien?",
                    "required": True,
                    "options": [
                        {"value": "beginnt", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis10", "label": "1 bis 10 Jahre"},
                        {"value": "ueber10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "fruehere_blei",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten (auch privat, z. B. Schießsport, "
                             "Restaurieren) Kontakt mit Blei?",
                    "required": True,
                    "followup": {"id": "fruehere_blei_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es an Ihrem Arbeitsplatz Unfälle, Zwischenfälle oder ungewöhnliche "
                             "Betriebszustände, bei denen viel Bleistaub oder Bleirauch frei wurde?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Läuft bei Ihnen zurzeit ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere", "nachgehend"]},
                },
                {
                    "id": "laermbereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie zusätzlich in einem Lärmbereich "
                             "(Bereich, in dem Gehörschutz getragen werden muss)?",
                    "hint": "Blei kann das Gehör zusätzlich belasten (»ototoxisch« = ohrschädigend).",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Ein großer Teil des Bleis wird über Hand-Mund-Kontakt aufgenommen – "
                        "Hygiene ist deshalb besonders wichtig.",
            "questions": [
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Tragen Sie die vorgesehene persönliche Schutzausrüstung "
                             "(z. B. Atemschutz, Schutzkleidung, Handschuhe)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_erforderlich", "label": "An meinem Arbeitsplatz nicht erforderlich"},
                    ],
                },
                {
                    "id": "hygiene_massnahmen",
                    "type": "multi_choice",
                    "label": "Welche Hygieneregeln setzen Sie bei der Arbeit regelmäßig um?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "haende", "label": "Hände und Gesicht waschen und Mund ausspülen, "
                                                     "bevor ich esse, trinke oder rauche"},
                        {"value": "duschen", "label": "Duschen bei Schichtende"},
                        {"value": "sw_trennung", "label": "Arbeits- und Privatkleidung getrennt aufbewahren "
                                                          "(Schwarz-Weiß-Trennung)"},
                        {"value": "kein_handy", "label": "Keine persönlichen Gegenstände (z. B. Handy) "
                                                         "im Arbeitsbereich benutzen"},
                        {"value": "keine", "label": "Keine oder kaum eine davon"},
                    ],
                },
                {
                    "id": "essen_arbeitsbereich",
                    "type": "yes_no",
                    "label": "Essen, trinken oder rauchen Sie im Arbeitsbereich?",
                    "required": True,
                },
                {
                    "id": "kleidung_nachhause",
                    "type": "yes_no",
                    "label": "Fahren Sie in Arbeitskleidung nach Hause, oder wird Ihre "
                             "Arbeitskleidung zu Hause gewaschen?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Frühe Anzeichen einer Bleibelastung",
            "questions": [
                {
                    "id": "beschwerden_allgemein",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine oder mehrere dieser Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "muedigkeit", "label": "Auffällige Müdigkeit oder Abgeschlagenheit"},
                        {"value": "appetit", "label": "Appetitmangel"},
                        {"value": "blaesse", "label": "Auffällige Blässe der Haut"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "magen_darm",
                    "type": "multi_choice",
                    "label": "Haben Sie Magen-Darm-Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "verstopfung", "label": "Anhaltende Verstopfung (Obstipation)"},
                        {"value": "koliken", "label": "Krampfartige oder kolikartige Bauchschmerzen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "nerven",
                    "type": "multi_choice",
                    "label": "Haben Sie Beschwerden, die das Nervensystem betreffen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "gedaechtnis", "label": "Probleme mit Kurzzeitgedächtnis, Konzentration "
                                                          "oder Aufmerksamkeit"},
                        {"value": "missempfindungen", "label": "Kribbeln, Taubheitsgefühl oder Schwäche "
                                                               "in Armen oder Beinen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "zahnfleisch_saum",
                    "type": "yes_no",
                    "label": "Ist Ihnen ein dunkler, gräulich-schwarzer Saum am Zahnfleisch "
                             "oder eine Verfärbung der Zunge aufgefallen (»Bleisaum«)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Gesundheit und Vorgeschichte ───────────────────────────────
        {
            "id": "gesundheit",
            "title": "Gesundheit & Vorgeschichte",
            "subtitle": "Erkrankungen, Medikamente und besondere Schutzbedürfnisse",
            "questions": [
                {
                    "id": "vorerkrankungen",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine dieser Erkrankungen festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "leber", "label": "Erkrankung der Leber"},
                        {"value": "niere", "label": "Erkrankung der Nieren"},
                        {"value": "blut", "label": "Erkrankung des Blutes (z. B. Blutarmut/Anämie)"},
                        {"value": "nerven_erkr", "label": "Erkrankung des Nervensystems "
                                                          "(Gehirn, Rückenmark oder Nerven)"},
                        {"value": "diabetes", "label": "Zuckerkrankheit (Diabetes mellitus)"},
                        {"value": "schilddruese", "label": "Ausgeprägte Schilddrüsenüberfunktion (Hyperthyreose)"},
                        {"value": "verdauung", "label": "Erkrankung des Magen-Darm-Trakts"},
                        {"value": "gefaesse", "label": "Erkrankung der Blutgefäße "
                                                       "(z. B. Durchblutungsstörungen, Arteriosklerose)"},
                        {"value": "bluthochdruck", "label": "Stark erhöhter Blutdruck (Hypertonie höheren Grades)"},
                        {"value": "tuberkulose", "label": "Tuberkulose"},
                        {"value": "koerperschwaeche", "label": "Allgemeine Körperschwäche"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "vorerkrankungen_details",
                    "type": "textarea",
                    "label": "Falls Sie eine Erkrankung angekreuzt haben: Welche genau, seit wann, "
                             "und wie wird sie behandelt?",
                    "required": False,
                },
                {
                    "id": "bk_anerkannt",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen schon einmal eine Berufskrankheit angezeigt "
                             "oder anerkannt?",
                    "required": True,
                    "followup": {"id": "bk_anerkannt_desc", "type": "text",
                                 "label": "Welche, und wann?", "when": "yes"},
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
                    "id": "schwanger_still",
                    "type": "choice",
                    "label": "Sind Sie zurzeit schwanger, oder stillen Sie?",
                    "hint": "Blei kann das ungeborene Kind schädigen und geht in die Muttermilch über. "
                            "Für Schwangere und Stillende gelten besondere Schutzvorschriften.",
                    "required": True,
                    "options": [
                        {"value": "ja_schwanger", "label": "Ja, ich bin schwanger"},
                        {"value": "ja_stillt", "label": "Ja, ich stille"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "nicht_zutreffend", "label": "Trifft auf mich nicht zu"},
                    ],
                },
                {
                    "id": "kinderwunsch",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen aktuell ein Kinderwunsch (Familienplanung)?",
                    "hint": "Blei kann die Fruchtbarkeit von Frauen und Männern beeinträchtigen.",
                    "required": True,
                },
                {
                    "id": "unter18",
                    "type": "yes_no",
                    "label": "Sind Sie unter 18 Jahre alt?",
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
    # ── Mutterschutz / besondere Personengruppen ──────────────────────────
    {"wenn": {"schwanger_still": ["ja_schwanger"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6 (Reproduktionstoxizität Kat. 1A, H360FD) und 7.1; MuSchG",
     "befund": "Schwangerschaft bei Tätigkeit mit Bleiexposition angegeben.",
     "konsequenz": "Vor Fortsetzung der Tätigkeit klären: Beschäftigungsbeschränkungen nach "
                   "Mutterschutzgesetz prüfen – Blei ist entwicklungsschädigend, ein sicherer "
                   "Schwellenwert lässt sich nicht ableiten (BGW für Frauen im gebärfähigen "
                   "Alter ausgesetzt). Unverzüglich ärztliche Beratung, Blutbleibestimmung und "
                   "Veranlassung der mutterschutzrechtlichen Maßnahmen im Betrieb."},
    {"wenn": {"schwanger_still": ["ja_stillt"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 6 (H362 – Wirkung auf/über Laktation) und 7.1; MuSchG",
     "befund": "Stillzeit bei Tätigkeit mit Bleiexposition angegeben.",
     "konsequenz": "Vor Fortsetzung der Tätigkeit klären: Blei kann über die Muttermilch auf das "
                   "Kind übergehen (H362). Beschäftigungsbeschränkungen für stillende Mütter "
                   "nach MuSchG prüfen; Blutbleibestimmung und Beratung veranlassen."},
    {"wenn": {"unter18": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Jugendarbeitsschutz",
     "quelle": "Abschnitt 7.1 (Beratung: Beschäftigungsbeschränkungen); JArbSchG",
     "befund": "Person ist unter 18 Jahre alt.",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Tätigkeit klären: Beschäftigungs-"
                   "beschränkungen für Jugendliche nach Jugendarbeitsschutzgesetz prüfen; "
                   "Einsatz mit Bleiexposition nur im dort zugelassenen Rahmen."},
    {"wenn": {"kinderwunsch": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Reproduktionstoxizität",
     "quelle": "Abschnitte 6, 7.1 und 8.1",
     "befund": "Aktueller Kinderwunsch angegeben.",
     "konsequenz": "Beratung zur fruchtbarkeitsgefährdenden und entwicklungsschädigenden "
                   "Wirkung von Blei (H360FD, betrifft Frauen und Männer). Biomonitoring "
                   "besprechen; bei Frauen im gebärfähigen Alter Blutbleiwert möglichst "
                   "niedrig halten (BGW ausgesetzt, EU-Zielwert 45 µg/l) und Schutzmaßnahmen "
                   "bzw. expositionsärmeren Einsatz prüfen."},
    # ── Biomonitoring-Anlässe ─────────────────────────────────────────────
    {"wenn": {"fruehere_blei": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitt 7.2.2 (Erstuntersuchung)",
     "befund": "Frühere (berufliche oder private) Bleiexposition angegeben.",
     "konsequenz": "Bei anamnestisch festgestellter Bleiexposition bereits bei der "
                   "Erstuntersuchung Biomonitoring Blei im Blut durchführen; frühere "
                   "Tätigkeiten und Expositionszeiträume dokumentieren."},
    {"wenn": {"vorsorge_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2 (Angebotsvorsorge) und 7.2.2",
     "befund": "Nachgehende Vorsorge nach dem Ausscheiden aus der Tätigkeit.",
     "konsequenz": "Untersuchungsprogramm nach 7.2.2 anbieten; Biomonitoring Blei im Blut "
                   "fortführen, solange erhöhte Blutbleiwerte nachweisbar sind. Anmeldung "
                   "über das Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de) prüfen."},
    {"wenn": {"blei_chromat_arsenat": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Krebserzeugende Bleiverbindungen",
     "quelle": "Abschnitt 2 (Anwendungsbereich) und Fußnote 1",
     "befund": "Tätigkeit mit Bleichromat oder Bleiarsenat angegeben.",
     "konsequenz": "Zusätzlich die DGUV Empfehlungen »Chrom(VI)-Verbindungen« bzw. »Arsen und "
                   "Arsenverbindungen« heranziehen (krebserzeugende Wirkung). Nachgehende "
                   "Vorsorge nach dem Ausscheiden sicherstellen – Anmeldung über das "
                   "Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de)."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese)",
     "befund": "Unfall, Zwischenfall oder ungewöhnlicher Betriebszustand mit erhöhter "
               "Bleifreisetzung angegeben.",
     "konsequenz": "Ereignis dokumentieren; außerplanmäßiges Biomonitoring Blei im Blut "
                   "erwägen. Abgleich mit der Gefährdungsbeurteilung; ergeben sich Anhalts-"
                   "punkte für unzureichende Schutzmaßnahmen, Mitteilung an das Unternehmen "
                   "und Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV)."},
    # ── Beschwerden: frühe Indikatoren einer Bleivergiftung ───────────────
    {"wenn": {"beschwerden_allgemein": ["muedigkeit", "appetit", "blaesse"]},
     "schwere": "pruefen",
     "bereich": "Frühindikatoren Bleivergiftung",
     "quelle": "Abschnitte 6.3.2/6.3.3 und 7.2.2",
     "befund": "Unspezifische Frühzeichen (Müdigkeit/Abgeschlagenheit, Appetitmangel, "
               "Blässe) angegeben.",
     "konsequenz": "Klinische Untersuchung veranlassen: großes Blutbild mit Differential-"
                   "blutbild, Kreatinin im Serum, Leberenzyme, β2-Mikroglobulin im Harn, "
                   "Urinstatus sowie Biomonitoring Blei im Blut. Bei deutlichem Überschreiten "
                   "des BGW Effektparameter bestimmen (ALA im Urin, ALA-D im Blut, Copro-"
                   "porphyrin im Urin, freies Erythrozytenporphyrin, Blutausstrich auf "
                   "Tüpfelzellen). Vorsorgetermin ggf. vorziehen."},
    {"wenn": {"magen_darm": ["verstopfung", "koliken"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm-Beschwerden",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Chronische Verstopfung oder kolikartige Bauchschmerzen angegeben "
               "(mögliche Bleiwirkung auf die glatte Muskulatur).",
     "konsequenz": "Ärztliche Abklärung mit Biomonitoring Blei im Blut und klinischer "
                   "Untersuchung nach 7.2.2; bei kolikartigen Beschwerden differential-"
                   "diagnostisch an Bleiintoxikation denken und Verdacht auf BK-Nr. 1101 "
                   "prüfen; Vorsorgetermin ggf. vorziehen."},
    {"wenn": {"nerven": ["gedaechtnis", "missempfindungen"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 6.3.3 und 7.2.2 (ergänzend bei klinischen Auffälligkeiten)",
     "befund": "Kognitive Beschwerden (Kurzzeitgedächtnis, Konzentration) oder "
               "Missempfindungen/Schwäche in Armen/Beinen angegeben.",
     "konsequenz": "Neurologische Untersuchung einschließlich Neurophysiologie/"
                   "Elektromyographie veranlassen; Biomonitoring Blei im Blut. Befund bei "
                   "der Beurteilung nach 7.4 berücksichtigen."},
    {"wenn": {"zahnfleisch_saum": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bleisaum",
     "quelle": "Abschnitte 6.3.3 und 7.2.1",
     "befund": "Dunkler Saum am Zahnfleisch bzw. Verfärbung der Zunge (möglicher Bleisaum).",
     "konsequenz": "Inspektion von Zunge und Zahnfleisch (7.2.1); als Zeichen relevanter "
                   "Bleiaufnahme werten: Biomonitoring Blei im Blut, Hygiene- und "
                   "Mundpflegeberatung."},
    # ── Vorerkrankungen (Beurteilungskriterien 7.4) ───────────────────────
    {"wenn": {"vorerkrankungen": ["leber", "niere", "blut", "nerven_erkr", "diabetes",
                                   "schilddruese", "verdauung", "gefaesse", "bluthochdruck",
                                   "tuberkulose", "koerperschwaeche"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankungen",
     "quelle": "Abschnitte 7.4, 7.4.2, 7.4.3 und 7.4.4",
     "befund": "Beurteilungsrelevante Vorerkrankung nach Abschnitt 7.4 angegeben.",
     "konsequenz": "Individuelles Ausmaß der Erkrankung ärztlich bewerten; prüfen, ob die "
                   "Tätigkeit ohne gesundheitliche Gefährdung möglich ist. Bei weniger "
                   "ausgeprägten Störungen Maßnahmen nach 7.4.2 empfehlen (Substitution, "
                   "technische/organisatorische Schutzmaßnahmen, Begrenzung der Expositions-"
                   "zeit, expositionsärmerer Einsatz, PSA). Bei zu erwartender Änderung des "
                   "Schweregrads verkürzte Vorsorgefristen (7.4.3). Ohne Erfolgsaussicht "
                   "Tätigkeitswechsel erwägen (7.4.4; Mitteilung an den Arbeitgeber nur mit "
                   "Einwilligung, § 6 (4) ArbMedVV)."},
    # ── Schutzmaßnahmen und Hygiene ───────────────────────────────────────
    {"wenn": {"psa_nutzung": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA unter Beachtung des "
                   "individuellen Gesundheitszustands; Ursachen klären. Ergeben sich Anhalts-"
                   "punkte, dass Arbeitsschutzmaßnahmen nicht ausreichen, Mitteilung an das "
                   "Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"hygiene_massnahmen": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Arbeitshygiene",
     "quelle": "Abschnitte 8.1 und 8.2 (TRGS 505)",
     "befund": "Hygieneregeln werden nicht oder kaum umgesetzt.",
     "konsequenz": "Spezielle Hygieneberatung nach 8.1: konsequente Schwarz-Weiß-Trennung, "
                   "Hände und Gesicht waschen, Mund ausspülen und Zähne putzen vor Essen/"
                   "Rauchen, Duschen bei Schichtende, keine persönlichen Gegenstände im "
                   "Schwarzbereich, Arbeitskleidung nicht mit nach Hause. Orale Aufnahme ist "
                   "ein wesentlicher Belastungspfad: Biomonitoring erwägen; bei Mängeln am "
                   "Hygieneregime Maßnahmen nach TRGS 505 gegenüber dem Unternehmen "
                   "vorschlagen (8.2)."},
    {"wenn": {"essen_arbeitsbereich": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitshygiene",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Essen, Trinken oder Rauchen im Arbeitsbereich angegeben.",
     "konsequenz": "Beratung: Nahrungs- und Genussmittelaufnahme in kontaminierten Bereichen "
                   "führt zu erheblicher oraler Bleiaufnahme. Biomonitoring Blei im Blut "
                   "erwägen; das Unternehmen auf Mängel im Hygieneregime hinweisen und "
                   "Maßnahmen nach TRGS 505 vorschlagen (8.2)."},
    {"wenn": {"kleidung_nachhause": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kontaminationsverschleppung",
     "quelle": "Abschnitt 8.1",
     "befund": "Arbeitskleidung wird mit nach Hause genommen bzw. zu Hause gewaschen.",
     "konsequenz": "Beratung: nicht in Arbeitskleidung nach Hause fahren, Arbeitssachen nicht "
                   "zu Hause waschen (Kontaminationsverschleppung, Schutz der Familie). "
                   "Unternehmen auf Schwarz-Weiß-Trennung und betriebliche Wäsche der "
                   "Arbeitskleidung hinweisen."},
    # ── Sonstiges ─────────────────────────────────────────────────────────
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 6.1.1",
     "befund": "Tätigkeit mit Bleiexposition in einem Lärmbereich angegeben.",
     "konsequenz": "Wegen der ototoxischen Eigenschaft von Blei mögliche Kombinations-"
                   "wirkungen mit Lärm bei der Gehöruntersuchung nach der DGUV Empfehlung "
                   "»Lärm« berücksichtigen."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheiten-Verfahren",
     "quelle": "Abschnitt 7.1 (weitere Vorsorgen)",
     "befund": "Laufendes Berufskrankheiten-Verfahren angegeben.",
     "konsequenz": "Verfahren dokumentieren (BK-Nr. 1101 »Erkrankungen durch Blei oder seine "
                   "Verbindungen«); vorliegende Befunde in Beurteilung und Beratung "
                   "einbeziehen."},
]
