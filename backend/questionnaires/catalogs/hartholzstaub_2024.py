# -*- coding: utf-8 -*-
"""Hartholzstaub – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
Kapitel »Hartholzstaub« (E HHS, Fassung Januar 2022), S. 303–320."""

SLUG = "hartholzstaub-2024"

CATALOG = {
    "version": 2,
    "title": "Hartholzstaub (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Hartholzstaub« (E HHS, Fassung Januar 2022), S. 303–320",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen Hartholzstaub?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge wegen Hartholzstaub"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur Hartholzstaub-Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: wenn der Arbeitsplatzgrenzwert für Hartholzstaub "
                            "(2 mg/m³) nicht eingehalten wird. Angebotsvorsorge: wenn eine Belastung "
                            "nicht ausgeschlossen ist. Nachgehende Vorsorge: nach dem Ende der "
                            "Tätigkeit mit Hartholzstaub.",
                    "required": True,
                    "options": [
                        {"value": "pflicht", "label": "Vom Betrieb verpflichtend veranlasst (Pflichtvorsorge)"},
                        {"value": "angebot", "label": "Vom Betrieb angeboten (Angebotsvorsorge)"},
                        {"value": "wunsch", "label": "Auf meinen eigenen Wunsch (Wunschvorsorge)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (Tätigkeit ist beendet)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Staubbelastung ───────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Staubbelastung",
            "subtitle": "Ihre Arbeit mit Holz und Holzstaub",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "holzarten",
                    "type": "multi_choice",
                    "label": "Welche Hölzer be- oder verarbeiten Sie?",
                    "hint": "Harthölzer sind z. B. Buche, Eiche, Birke, Esche, Ahorn, Kirsche, "
                            "Teak oder Mahagoni. Auch Holzwerkstoffe wie MDF-Platten enthalten "
                            "Hartholz-Anteile. Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "buche_eiche", "label": "Buche oder Eiche"},
                        {"value": "andere_harthoelzer", "label": "Andere Harthölzer (z. B. Birke, Esche, Ahorn, Teak, Mahagoni)"},
                        {"value": "holzwerkstoffe", "label": "Holzwerkstoffe (z. B. MDF-, Spanplatten)"},
                        {"value": "weichholz", "label": "Überwiegend Weichholz (z. B. Fichte, Tanne)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "taetigkeiten_expo",
                    "type": "multi_choice",
                    "label": "Führen Sie eine oder mehrere dieser Arbeiten aus?",
                    "hint": "Bei diesen Arbeiten ist die Staubbelastung erfahrungsgemäß besonders "
                            "hoch. Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "handschleifen", "label": "Handschleifarbeiten"},
                        {"value": "maschinen", "label": "Arbeiten an stark staubenden Maschinen (z. B. Bandsäge, Fräse, Schleifbock, Drechselbank, Parkettschleifmaschine)"},
                        {"value": "filterwechsel", "label": "Wechsel von Filterelementen oder Staub-Sammelbehältern"},
                        {"value": "kehren_abblasen", "label": "Kehren von Holzstaub oder Abblasen mit Druckluft"},
                        {"value": "silo", "label": "Einfahren in Silos"},
                        {"value": "restauration", "label": "Möbel- oder Holzrestauration vor Ort"},
                        {"value": "musikinstrumente", "label": "Herstellen oder Restaurieren von Musikinstrumenten aus Holz"},
                        {"value": "keine", "label": "Keine dieser Arbeiten"},
                    ],
                },
                {
                    "id": "staubgemindert",
                    "type": "choice",
                    "label": "Gibt es an Ihrem Arbeitsplatz wirksame Absaugungen oder andere "
                             "Maßnahmen gegen Holzstaub?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, Maschinen sind abgesaugt / Arbeitsbereich ist staubgemindert"},
                        {"value": "teilweise", "label": "Teilweise"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "weiss_nicht", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei staubenden Arbeiten Atemschutz (z. B. Staubmaske)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_erforderlich", "label": "Ist bei meiner Arbeit nicht vorgesehen"},
                    ],
                },
                {
                    "id": "hygiene",
                    "type": "choice",
                    "label": "Halten Sie die Hygieneregeln am Arbeitsplatz ein (kein Essen und "
                             "Trinken am staubigen Arbeitsplatz, Wechsel der Arbeitskleidung, "
                             "kein Abblasen der Kleidung mit Druckluft)?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, durchgehend"},
                        {"value": "teilweise", "label": "Teilweise"},
                        {"value": "nein", "label": "Nein / solche Regeln gibt es bei uns nicht"},
                    ],
                },
                {
                    "id": "holzschutzmittel",
                    "type": "yes_no",
                    "label": "Verarbeiten Sie Holzschutzmittel oder bearbeiten Sie chemisch "
                             "behandeltes Holz?",
                    "required": True,
                    "followup": {"id": "holzschutzmittel_desc", "type": "text",
                                 "label": "Welche Mittel bzw. welche Arbeiten?", "when": "yes"},
                },
                {
                    "id": "beschichtungen",
                    "type": "yes_no",
                    "label": "Verarbeiten Sie Oberflächenbeschichtungen wie Lacke oder Öle, oder "
                             "arbeiten Sie in kontaminierten (schadstoffbelasteten) Bereichen?",
                    "required": True,
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es Zwischenfälle, Unfälle oder ungewöhnliche Betriebszustände "
                             "mit besonders hoher Staubbelastung (z. B. Ausfall der Absaugung)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_holzstaub",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Berufen oder Tätigkeiten Holzstaub ausgesetzt?",
                    "required": True,
                    "followup": {"id": "frueher_holzstaub_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
                {
                    "id": "andere_krebserzeugend",
                    "type": "yes_no",
                    "label": "Arbeiten oder arbeiteten Sie mit anderen krebserzeugenden Stoffen "
                             "(z. B. Asbest, Quarzstaub, Chrom(VI)-Verbindungen)?",
                    "required": True,
                    "followup": {"id": "andere_krebserzeugend_desc", "type": "text",
                                 "label": "Welche Stoffe, und wie lange?", "when": "yes"},
                },
                {
                    "id": "hobby_holz",
                    "type": "yes_no",
                    "label": "Bearbeiten Sie auch in der Freizeit regelmäßig Holz (z. B. "
                             "Heimwerken, Drechseln, Schnitzen)?",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden an Nase, Augen und Atemwegen",
            "questions": [
                {
                    "id": "nasenatmung",
                    "type": "yes_no",
                    "label": "Ist Ihre Nasenatmung behindert (Sie bekommen durch die Nase "
                             "schlecht Luft)?",
                    "required": True,
                    "followup": {"id": "nasenatmung_desc", "type": "text",
                                 "label": "Seit wann, und eher auf einer Seite oder beidseits?",
                                 "when": "yes"},
                },
                {
                    "id": "sekret",
                    "type": "yes_no",
                    "label": "Haben Sie vermehrten Ausfluss aus der Nase (ständig laufende oder "
                             "verschleimte Nase)?",
                    "required": True,
                },
                {
                    "id": "nasenbluten",
                    "type": "choice",
                    "label": "Haben Sie Nasenbluten?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein / praktisch nie"},
                        {"value": "selten", "label": "Gelegentlich"},
                        {"value": "haeufig", "label": "Häufig oder blutig gefärbter Schnupfen"},
                    ],
                },
                {
                    "id": "geruch",
                    "type": "yes_no",
                    "label": "Hat sich Ihr Geruchssinn verschlechtert (Geruchsstörung)?",
                    "required": True,
                },
                {
                    "id": "augen",
                    "type": "yes_no",
                    "label": "Haben Sie Augenbeschwerden wie Doppelbilder, ein hervortretendes "
                             "Auge oder ständiges Augentränen?",
                    "required": True,
                },
                {
                    "id": "atemwege_symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie Beschwerden der tieferen Atemwege?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Husten"},
                        {"value": "auswurf", "label": "Auswurf (Schleim beim Husten)"},
                        {"value": "atemnot", "label": "Atemnot / Luftnot"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
            ],
        },
        # ── 4 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Frühere Erkrankungen und Allergien",
            "questions": [
                {
                    "id": "tumor_nase",
                    "type": "yes_no",
                    "label": "Hatten oder haben Sie eine bösartige Tumorerkrankung (Krebs) der "
                             "inneren Nase oder der Nasennebenhöhlen?",
                    "required": True,
                },
                {
                    "id": "nase_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie andere Erkrankungen der Nase oder der Nasennebenhöhlen "
                             "(z. B. chronische Nebenhöhlen-Entzündung, Polypen)?",
                    "required": True,
                    "followup": {"id": "nase_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "nase_op",
                    "type": "yes_no",
                    "label": "Wurden Sie im Bereich der Nase oder der Nasennebenhöhlen operiert?",
                    "required": True,
                    "followup": {"id": "nase_op_desc", "type": "text",
                                 "label": "Welche Operation, und wann?", "when": "yes"},
                },
                {
                    "id": "atemwegserkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Atemwegs- oder Lungenerkrankung (z. B. Asthma, "
                             "COPD, chronische Bronchitis)?",
                    "required": True,
                    "followup": {"id": "atemwegserkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "allergien",
                    "type": "multi_choice",
                    "label": "Haben Sie Allergien?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "holzstaub", "label": "Allergie gegen Holzstaub"},
                        {"value": "atemwege", "label": "Allergische Atemwegserkrankung (z. B. Heuschnupfen, allergisches Asthma)"},
                        {"value": "andere", "label": "Andere Allergien"},
                        {"value": "keine", "label": "Keine Allergien bekannt"},
                    ],
                },
                {
                    "id": "infektneigung",
                    "type": "yes_no",
                    "label": "Sind Sie besonders anfällig für Infekte (häufige Erkältungen, "
                             "Nebenhöhlen- oder Atemwegsinfekte)?",
                    "required": True,
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Berufskrankheit anerkannt, oder läuft derzeit "
                             "ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Erkrankung bzw. welches Verfahren?", "when": "yes"},
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
                    "id": "allg_einschraenkungen",
                    "type": "yes_no",
                    "label": "Gibt es sonstige gesundheitliche Einschränkungen oder Erkrankungen, "
                             "die wir kennen sollten?",
                    "required": True,
                    "followup": {"id": "allg_einschraenkungen_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Rauchen & Schnupftabak ─────────────────────────────────────
        {
            "id": "rauchen_sektion",
            "title": "Rauchen & Schnupftabak",
            "subtitle": "Tabak kann zusammen mit Hartholzstaub das gleiche Organsystem belasten",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, nie geraucht"},
                        {"value": "frueher", "label": "Früher geraucht, jetzt nicht mehr"},
                        {"value": "aktuell", "label": "Ja, ich rauche"},
                    ],
                },
                {
                    "id": "schnupftabak",
                    "type": "yes_no",
                    "label": "Verwenden Sie Schnupftabak?",
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
    {"wenn": {"tumor_nase": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Tumorerkrankung Nase/NNH",
     "quelle": "Abschnitte 7.4 und 7.4.4",
     "befund": "Vorangegangene oder bestehende maligne Tumorerkrankung der inneren "
               "Nase bzw. der Nasennebenhöhlen angegeben.",
     "konsequenz": "Vor Aufnahme bzw. Fortsetzung der Tätigkeit klären, ob eine Ausübung "
                   "ohne gesundheitliche Gefährdung möglich ist: HNO-Vorbefunde einholen, "
                   "HNO-ärztliche Abklärung. Maßnahmen nach 7.4.2 prüfen (Substitution, "
                   "technische/organisatorische Schutzmaßnahmen, expositionsarmer Einsatz); "
                   "haben diese keine Aussicht auf Erfolg, Tätigkeitswechsel nach 7.4.4 "
                   "erwägen (Mitteilung an den Arbeitgeber nur mit Einwilligung, § 6 (4) "
                   "ArbMedVV)."},
    {"wenn": {"nase_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung Nase/NNH",
     "quelle": "Abschnitte 7.1 und 7.4",
     "befund": "Vorangegangene Erkrankung der Nase oder der Nasennebenhöhlen angegeben.",
     "konsequenz": "Beurteilungsrelevante Vorerkrankung (7.4): Inspektion der inneren Nase "
                   "mit Nasenspekulum, HNO-ärztliche Abklärung in unklaren Fällen. Maßnahmen "
                   "nach 7.4.2 prüfen; bei zu erwartender Änderung des Schweregrads verkürzte "
                   "Vorsorgefristen nach 7.4.3 vorsehen."},
    {"wenn": {"nase_op": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankung Nase/NNH",
     "quelle": "Abschnitt 7.1 (Allgemeine Anamnese)",
     "befund": "Operation im Bereich der Nasennebenhöhlen angegeben.",
     "konsequenz": "OP-Berichte bzw. HNO-Vorbefunde einholen und beim Nasenbefund "
                   "berücksichtigen; bei unklarem Befund HNO-ärztliche Abklärung."},
    # ── Zielorgan-Symptome (Abschnitte 6.3, 7.1, 7.4) ─────────────────────
    {"wenn": {"nasenatmung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nasensymptome",
     "quelle": "Abschnitte 6.3.2, 7.2.2 und 7.4",
     "befund": "Behinderte Nasenatmung angegeben.",
     "konsequenz": "Beurteilungsrelevantes Symptom: Inspektion der inneren Nase mit "
                   "Nasenspekulum, HNO-ärztliche Abklärung in unklaren Fällen; ab dem "
                   "45. Lebensjahr ggf. zusätzlich Endoskopie der Nase mit flexiblem "
                   "Endoskop, Fotodokumentation bei auffälligem oder unklarem Befund."},
    {"wenn": {"sekret": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nasensymptome",
     "quelle": "Abschnitte 7.1, 7.2.2 und 7.4",
     "befund": "Vermehrte Sekretabsonderung aus der Nase angegeben.",
     "konsequenz": "Beurteilungsrelevantes Symptom: Inspektion der inneren Nase, in "
                   "unklaren Fällen HNO-ärztliche Abklärung (ggf. Endoskopie mit "
                   "Fotodokumentation)."},
    {"wenn": {"nasenbluten": ["haeufig"]},
     "schwere": "pruefen",
     "bereich": "Nasensymptome",
     "quelle": "Abschnitte 6.3.2, 7.2.2 und 7.4",
     "befund": "Häufiges Nasenbluten bzw. blutig gefärbter Schnupfen angegeben.",
     "konsequenz": "Mögliches Frühzeichen eines Adenokarzinoms der inneren Nase: "
                   "Inspektion der inneren Nase, HNO-ärztliche Abklärung; ggf. Endoskopie "
                   "mit Fotodokumentation. Ergebnis in die Beurteilung nach 7.4 einbeziehen."},
    {"wenn": {"geruch": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nasensymptome",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 7.2.2",
     "befund": "Geruchsstörung angegeben.",
     "konsequenz": "Inspektion der inneren Nase; in unklaren Fällen HNO-ärztliche "
                   "Abklärung, ggf. Endoskopie mit Fotodokumentation."},
    {"wenn": {"augen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augensymptome",
     "quelle": "Abschnitte 6.3 und 7.1 (Beschwerden)",
     "befund": "Augensymptome (Doppelbilder, hervortretendes Auge, Augentränen) angegeben.",
     "konsequenz": "Mögliches Zeichen eines in die Augenhöhle einwachsenden Prozesses: "
                   "zeitnahe HNO-ärztliche Abklärung veranlassen, ggf. augenärztliche "
                   "Mituntersuchung; Befund dokumentieren."},
    {"wenn": {"atemwege_symptome": ["husten", "auswurf", "atemnot"]},
     "schwere": "pruefen",
     "bereich": "Tiefere Atemwege",
     "quelle": "Abschnitt 7.2.2 (Klinische Untersuchungen)",
     "befund": "Beschwerden der tieferen Atemwege (Husten, Auswurf oder Atemnot) angegeben.",
     "konsequenz": "Ergänzend Spirometrie (Lungenfunktionsprüfung) durchführen und ggf. "
                   "pulmologische Abklärung veranlassen."},
    {"wenn": {"atemwegserkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 2, 7.1 und 7.2.2",
     "befund": "Obstruktive Atemwegs- bzw. Lungenerkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Spirometrie und ggf. pulmologische Abklärung; DGUV Empfehlung "
                   "»Obstruktive Atemwegserkrankungen« zusätzlich einbeziehen. Eignung der "
                   "persönlichen Schutzausrüstung unter Beachtung des Gesundheitszustands "
                   "prüfen (7.4.2)."},
    {"wenn": {"allergien": ["holzstaub"]},
     "schwere": "pruefen",
     "bereich": "Sensibilisierung",
     "quelle": "Abschnitte 2, 6.3.3 und Vorsorgeanlässe (Angebotsvorsorge)",
     "befund": "Allergie gegen Holzstaub angegeben.",
     "konsequenz": "Bei atemwegs- oder hautsensibilisierenden Holzstäuben (TRGS 907) die "
                   "DGUV Empfehlungen »Obstruktive Atemwegserkrankungen« bzw. »Gefährdung "
                   "der Haut« zusätzlich einbeziehen; Angebotsvorsorge hierfür sicherstellen. "
                   "Auslösende Holzarten identifizieren und Expositionsvermeidung beraten."},
    # ── Exposition und Schutzmaßnahmen (Abschnitte 6.1, 8.2) ──────────────
    {"wenn": {"taetigkeiten_expo": ["handschleifen", "maschinen", "filterwechsel",
                                    "kehren_abblasen", "silo", "restauration",
                                    "musikinstrumente"]},
     "schwere": "pruefen",
     "bereich": "Hohe Staubexposition",
     "quelle": "Abschnitte 6.1.1 und 8.2",
     "befund": "Tätigkeit mit höherer Exposition angegeben, bei der der Arbeitsplatz-"
               "grenzwert von 2 mg/m³ vermutlich nicht eingehalten werden kann.",
     "konsequenz": "Abgleich mit der Gefährdungsbeurteilung: bei Überschreitung des AGW ist "
                   "Pflichtvorsorge erforderlich (TRGS 553). Ergeben sich Anhaltspunkte, dass "
                   "die Schutzmaßnahmen nicht ausreichen, Mitteilung an das Unternehmen und "
                   "Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV); Beratung zu PSA und "
                   "Hygiene intensivieren."},
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "hinweis",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitt 8.1",
     "befund": "Atemschutz wird bei staubenden Arbeiten selten oder nie getragen.",
     "konsequenz": "Beratung zum Tragen geeigneter persönlicher Schutzausrüstung (ggf. "
                   "besondere individuelle Aspekte aufzeigen); prüfen, ob Atemschutz laut "
                   "Gefährdungsbeurteilung vorgesehen ist, ggf. Rückmeldung an das "
                   "Unternehmen."},
    {"wenn": {"hygiene": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 (Beratung) und 8.1",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht durchgehend umgesetzt.",
     "konsequenz": "Beratung zu Hygienemaßnahmen: kein Essen und Trinken am Arbeitsplatz, "
                   "Wechsel der Arbeitskleidung, kein Abblasen von Arbeitsplatz oder "
                   "Kleidung; Vermeidung der Inhalation von Holzstaub."},
    # ── Kombinationswirkungen (Abschnitt 7.1, Beratung) ───────────────────
    {"wenn": {"rauchen": ["aktuell"]},
     "schwere": "hinweis",
     "bereich": "Tabakkonsum",
     "quelle": "Abschnitt 7.1 (Allgemeine Beratung)",
     "befund": "Aktueller Tabakkonsum (Rauchen) angegeben.",
     "konsequenz": "Beratung zur möglichen Wechselwirkung von Rauchen mit Hartholzstaub "
                   "(Co-Exposition, die das gleiche Organsystem betrifft); Tabakentwöhnung "
                   "empfehlen."},
    {"wenn": {"schnupftabak": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Tabakkonsum",
     "quelle": "Abschnitt 7.1 (Allgemeine Anamnese und Beratung)",
     "befund": "Gebrauch von Schnupftabak angegeben.",
     "konsequenz": "Beratung zur möglichen Wechselwirkung von Schnupftabak mit "
                   "Hartholzstaub am Zielorgan Nase; Verzicht empfehlen."},
    {"wenn": {"andere_krebserzeugend": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Weitere Kanzerogene",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese und Beratung)",
     "befund": "Frühere oder aktuelle Exposition gegenüber weiteren krebserzeugenden "
               "Arbeitsstoffen angegeben.",
     "konsequenz": "Exposition dokumentieren, mögliche Co-Exposition (z. B. Lungen-"
                   "kanzerogene) beraten; prüfen, ob weitere Vorsorgeanlässe bestehen und "
                   "ob eine Anmeldung zur nachgehenden Vorsorge (DGUV Vorsorge, "
                   "www.dguv-vorsorge.de) erforderlich ist."},
    # ── Nachgehende Vorsorge (Vorsorgeanlässe, Abschnitt 2) ───────────────
    {"wenn": {"vorsorge_anlass": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Vorsorgeanlässe (Angebotsvorsorge) und Abschnitt 7.2.2",
     "befund": "Vorstellung zur nachgehenden Vorsorge nach Ende der Tätigkeit mit "
               "Hartholzstaub.",
     "konsequenz": "Untersuchungsprogramm wie Nachuntersuchung durchführen (Inspektion der "
                   "inneren Nase, ggf. Endoskopie ab dem 45. Lebensjahr); Anmeldung über das "
                   "Meldeportal »DGUV Vorsorge« (www.dguv-vorsorge.de) sicherstellen, damit "
                   "weitere Einladungen erfolgen."},
]
