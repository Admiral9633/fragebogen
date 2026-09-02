# -*- coding: utf-8 -*-
"""Toluol und Xylol – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Toluol und Xylol« (E TLX, Fassung Januar 2022), S. 698–714."""

SLUG = "toluol_xylol-2024"

CATALOG = {
    "version": 2,
    "title": "Toluol und Xylol (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Toluol und Xylol« (E TLX, Fassung Januar 2022), S. 698–714",
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
                             "Toluol oder Xylol?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge zu diesem Anlass"},
                        {"value": "weitere", "label": "Nein, ich war deswegen schon einmal zur Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der "
                            "Arbeitsplatzgrenzwert nicht eingehalten wird oder Hautkontakt "
                            "mit Toluol/Xylol nicht ausgeschlossen werden kann. "
                            "Angebotsvorsorge: wenn eine Belastung möglich ist.",
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
            "subtitle": "Ihre Arbeit mit Toluol, Xylol oder lösungsmittelhaltigen Produkten",
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
                    "label": "Bei welchen Arbeiten haben Sie Kontakt mit Toluol, Xylol oder "
                             "Lösungsmittelgemischen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "entfettung", "label": "Metallentfettung oder Oberflächenreinigung mit Lösungsmitteln"},
                        {"value": "abbruch", "label": "Abbruch-, Sanierungs- oder Instandsetzungsarbeiten in Produktions-/Abfüllanlagen"},
                        {"value": "kontaminiert", "label": "Arbeiten in verunreinigten (kontaminierten) Bereichen"},
                        {"value": "beengt", "label": "Arbeiten mit Lösungsmitteln in engen Räumen oder bei schlechter Lüftung"},
                        {"value": "behaelter", "label": "Reinigen von Anlagen, Tanks oder Behältern"},
                        {"value": "beschichtung", "label": "Lackieren/Beschichten (Spritzen, Tauchen, Streichen) oder Korrosionsschutz"},
                        {"value": "herstellung", "label": "Herstellung von Lacken, Druckfarben, Klebstoffen, Reinigungsmitteln oder Gummi"},
                        {"value": "histologie", "label": "Arbeiten mit Xylol im Labor (z. B. histologisches Labor)"},
                        {"value": "andere", "label": "Andere Tätigkeit mit Toluol/Xylol"},
                        {"value": "keine", "label": "Keine davon / Tätigkeit beginnt erst"},
                    ],
                },
                {
                    "id": "benzol_anteil",
                    "type": "choice",
                    "label": "Enthalten die Produkte, mit denen Sie arbeiten, mehr als 0,1 % Benzol?",
                    "hint": "Diese Angabe finden Sie im Sicherheitsdatenblatt des Produkts. "
                            "Fragen Sie im Zweifel Ihre Sicherheitsfachkraft.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt mit Toluol, Xylol oder "
                             "solchen Lösungsmitteln?",
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
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit direkt mit Toluol, Xylol oder "
                             "lösungsmittelhaltigen Produkten in Berührung (z. B. Spritzer, "
                             "benetzte Lappen, Reinigen mit bloßen Händen)?",
                    "hint": "Toluol und Xylol können auch über die Haut in den Körper gelangen.",
                    "required": True,
                },
                {
                    "id": "mischexposition",
                    "type": "yes_no",
                    "label": "Arbeiten Sie gleichzeitig noch mit anderen Lösungsmitteln oder "
                             "Chemikalien (z. B. Verdünner, Aceton, Ethylbenzol, Butanon)?",
                    "required": True,
                    "followup": {"id": "mischexposition_desc", "type": "text",
                                 "label": "Mit welchen Stoffen?", "when": "yes"},
                },
                {
                    "id": "laermbereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit diesen Lösungsmitteln in lauten Bereichen "
                             "(Lärmbereich mit Gehörschutzpflicht)?",
                    "hint": "Toluol und Xylol können das Gehör zusätzlich belasten "
                            "(»ototoxische« = ohrschädigende Stoffe).",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Persönliche Schutzausrüstung und Hygiene am Arbeitsplatz",
            "questions": [
                {
                    "id": "handschuhe",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit möglichem Hautkontakt geeignete "
                             "Schutzhandschuhe?",
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
                    "id": "atemschutz",
                    "type": "yes_no",
                    "label": "Tragen Sie Atemschutz, wenn es bei der Arbeit stark nach "
                             "Lösungsmitteln riecht oder die Absaugung nicht ausreicht?",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                },
                {
                    "id": "hygiene",
                    "type": "yes_no",
                    "label": "Wechseln Sie mit Lösungsmitteln benetzte Arbeitskleidung zügig "
                             "und waschen Sie sich vor Pausen die Hände?",
                    "required": True,
                    "show_if": {"id": "expo_dauer", "not_in": ["keine"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden",
            "subtitle": "Beschwerden, die mit Toluol und Xylol zusammenhängen können",
            "questions": [
                {
                    "id": "symptome",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine oder mehrere der folgenden "
                             "Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "kopfschmerzen", "label": "Kopfschmerzen"},
                        {"value": "schwindel", "label": "Schwindelgefühl"},
                        {"value": "appetitlosigkeit", "label": "Appetitlosigkeit"},
                        {"value": "uebelkeit", "label": "Übelkeit"},
                        {"value": "gewichtsverlust", "label": "Ungewollter Gewichtsverlust"},
                        {"value": "ermuedbarkeit", "label": "Schnelle Ermüdbarkeit (rasch erschöpft)"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "akut_symptome",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich während oder direkt nach der Arbeit mit "
                             "Lösungsmitteln manchmal benommen, »wie berauscht«, unsicher "
                             "beim Gehen oder ungewöhnlich müde?",
                    "hint": "Solche Beschwerden können ein Zeichen für eine zu hohe "
                            "Lösungsmittelbelastung sein.",
                    "required": True,
                },
                {
                    "id": "konzentration",
                    "type": "yes_no",
                    "label": "Haben Konzentration oder Gedächtnis bei Ihnen spürbar "
                             "nachgelassen?",
                    "required": True,
                },
                {
                    "id": "haut_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Hautprobleme an Händen oder Unterarmen (z. B. sehr "
                             "trockene, rissige, gerötete oder juckende Haut, Ekzem)?",
                    "hint": "Toluol und Xylol entfetten die Haut und können Ekzeme auslösen.",
                    "required": True,
                    "followup": {"id": "haut_beschwerden_desc", "type": "text",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "augen_reiz",
                    "type": "yes_no",
                    "label": "Sind Ihre Augen oder Schleimhäute (Nase, Rachen) bei der Arbeit "
                             "häufig gereizt (Brennen, Rötung, Tränen)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen und besondere Umstände ─────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & besondere Umstände",
            "subtitle": "Erkrankungen, die bei der Beurteilung wichtig sind",
            "questions": [
                {
                    "id": "neuro_erkrankung",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine Erkrankung des Nervensystems "
                             "(z. B. Nervenschädigung/Polyneuropathie, Krampfanfälle/Epilepsie, "
                             "Lähmungen, dauerhaftes Kribbeln oder Taubheitsgefühl)?",
                    "required": True,
                    "followup": {"id": "neuro_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, in Behandlung?",
                                 "when": "yes"},
                },
                {
                    "id": "alkohol_abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Alkoholabhängigkeit "
                             "(Alkoholkrankheit)?",
                    "required": True,
                },
                {
                    "id": "alkohol_konsum",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Alkohol kann die Wirkung von Toluol und Xylol verstärken.",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche)"},
                    ],
                },
                {
                    "id": "atemwegserkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine chronische Atemwegserkrankung mit verengten "
                             "Bronchien, z. B. Asthma oder COPD (obstruktive "
                             "Atemwegserkrankung)?",
                    "required": True,
                },
                {
                    "id": "hauterkrankung_chron",
                    "type": "yes_no",
                    "label": "Haben Sie eine chronisch-entzündliche Hauterkrankung "
                             "(z. B. Neurodermitis, chronisches Handekzem, Schuppenflechte)?",
                    "required": True,
                },
                {
                    "id": "augen_chron",
                    "type": "yes_no",
                    "label": "Haben Sie eine dauerhafte (chronische) Reizung oder Entzündung "
                             "der Augenbindehaut?",
                    "required": True,
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Sind Sie derzeit schwanger, oder stillen Sie?",
                    "hint": "Toluol kann vermutlich das Kind im Mutterleib schädigen. Diese "
                            "Angabe ist freiwillig, aber für Ihren Schutz wichtig "
                            "(Mutterschutzgesetz).",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "keine_angabe", "label": "Trifft nicht zu / keine Angabe"},
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
    # ── Mutterschutz (Abschnitte 6.3.1, 7.1 und 8.1) ──────────────────────
    {"wenn": {"schwangerschaft": ["ja"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6.3.1 (Hinweis fruchtschädigende Wirkung), 7.1 und 8.1",
     "befund": "Schwangerschaft bzw. Stillzeit bei Tätigkeit mit Toluol/Xylol angegeben.",
     "konsequenz": "Vor (weiterer) Tätigkeit klären: Toluol kann vermutlich das Kind im "
                   "Mutterleib schädigen. Unverzüglich über die fruchtschädigende Wirkung "
                   "aufklären, mutterschutzrechtliche Gefährdungsbeurteilung nach MuSchG "
                   "anstoßen (Umsetzung/expositionsfreier Arbeitsplatz), mit Einwilligung "
                   "der Beschäftigten Rücksprache mit dem Unternehmen."},
    # ── Benzolgehalt (Abschnitt 2 Anwendungsbereich) ──────────────────────
    {"wenn": {"benzol_anteil": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Benzol-Mischexposition",
     "quelle": "Abschnitt 2 (Anwendungsbereich)",
     "befund": "Verwendete Produkte enthalten mehr als 0,1 Gew.-% Benzol.",
     "konsequenz": "DGUV Empfehlung »Benzol« in die Vorsorge einbeziehen (Benzol ist "
                   "krebserzeugend; dort vorgesehenes Programm inkl. Biomonitoring "
                   "anwenden). Sicherheitsdatenblätter anfordern und die "
                   "Gefährdungsbeurteilung mit dem Unternehmen abgleichen."},
    {"wenn": {"benzol_anteil": ["unbekannt"]},
     "schwere": "hinweis",
     "bereich": "Benzol-Mischexposition",
     "quelle": "Abschnitt 2 (Anwendungsbereich)",
     "befund": "Benzolgehalt der verwendeten Produkte unbekannt.",
     "konsequenz": "Benzolgehalt über Sicherheitsdatenblatt/Unternehmen klären lassen; "
                   "bei mehr als 0,1 Gew.-% Benzol die DGUV Empfehlung »Benzol« einbeziehen."},
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"neuro_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Neurologische Erkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Erhebliche neurologische Störungen sind beurteilungsrelevant: "
                   "orientierende neurologische Untersuchung durchführen, in unklaren "
                   "Fällen fachärztliche (neurologische) Abklärung. Prüfen, ob die "
                   "Tätigkeit ohne Gesundheitsgefährdung möglich ist; ggf. Maßnahmen nach "
                   "7.4.2 (Substitution, Expositionsminderung), verkürzte Vorsorgefristen "
                   "nach 7.4.3, bei Erfolglosigkeit Tätigkeitswechsel erwägen (7.4.4)."},
    {"wenn": {"alkohol_abhaengigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 7.4 und 8.1",
     "befund": "Alkoholabhängigkeit angegeben.",
     "konsequenz": "Alkoholabhängigkeit ist beurteilungsrelevant (verstärkende Wirkung "
                   "von Ethanol auf Toluol/Xylol): individuelles Ausmaß ärztlich prüfen, "
                   "Leberwerte (γ-GT, ALAT, ASAT) bestimmen, Beratung zur "
                   "Wirkungsverstärkung. Maßnahmen nach 7.4.2/7.4.3 prüfen; bei "
                   "Erfolglosigkeit Tätigkeitswechsel erwägen (7.4.4); Behandlung "
                   "empfehlen."},
    {"wenn": {"atemwegserkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitt 7.4",
     "befund": "Obstruktive Atemwegserkrankung (z. B. Asthma, COPD) angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung: Schweregrad und aktuelle Therapie "
                   "klären, Reizwirkung der Lösungsmitteldämpfe berücksichtigen. Prüfen, "
                   "ob die Tätigkeit ohne Gefährdung möglich ist; ggf. Maßnahmen nach "
                   "7.4.2 (z. B. Expositionsminderung, geeigneter Atemschutz) und "
                   "verkürzte Vorsorgefristen nach 7.4.3."},
    {"wenn": {"hauterkrankung_chron": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 7.4 und 7.2.2",
     "befund": "Chronisch-entzündliche Hauterkrankung angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung (entfettende, hautresorptive Stoffe): "
                   "Inspektion der Haut, Hautschutzberatung, geeignete Schutzhandschuhe "
                   "(Auswahl nach Sicherheitsdatenblatt bzw. GESTIS/GISCHEM/WINGIS). "
                   "Maßnahmen nach 7.4.2 und verkürzte Vorsorgefristen nach 7.4.3 prüfen; "
                   "an BK-Nr. 5101 (schwere/wiederholt rückfällige Hauterkrankung) denken."},
    {"wenn": {"augen_chron": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen",
     "quelle": "Abschnitt 7.4",
     "befund": "Chronische konjunktivale Reizerscheinungen angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung: Ausmaß klären, ggf. augenärztliche "
                   "Abklärung. Expositionsminderung/Schutzmaßnahmen nach 7.4.2 und "
                   "verkürzte Vorsorgefristen nach 7.4.3 prüfen."},
    # ── Tätigkeitsspezifische Symptome (Abschnitte 7.1 und 7.2.2) ─────────
    {"wenn": {"symptome": ["kopfschmerzen", "schwindel", "appetitlosigkeit",
                           "uebelkeit", "gewichtsverlust", "ermuedbarkeit"]},
     "schwere": "pruefen",
     "bereich": "Tätigkeitsspezifische Symptome",
     "quelle": "Abschnitte 7.1 (Anamnese) und 7.2.2",
     "befund": "Tätigkeitsspezifische Symptome (Kopfschmerzen, Schwindel, Appetitlosigkeit, "
               "Übelkeit, Gewichtsverlust oder leichte Ermüdbarkeit) angegeben.",
     "konsequenz": "Untersuchung anbieten: Urinstatus, großes Blutbild, Leberwerte (γ-GT, "
                   "ALAT, ASAT), orientierende neurologische Untersuchung sowie "
                   "Biomonitoring (Toluol im Blut/Urin, o-Kresol bzw. Methylhippursäure im "
                   "Urin, BGW nach TRGS 903). Zeitlichen Zusammenhang mit der Exposition "
                   "klären; in unklaren Fällen weiterführende fachärztliche Untersuchung."},
    {"wenn": {"akut_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Überexposition",
     "quelle": "Abschnitte 6.3.2, 7.2.2 und 8.2",
     "befund": "Pränarkotische Beschwerden (Benommenheit, Rauschgefühl, Gangunsicherheit) "
               "während oder nach der Arbeit angegeben.",
     "konsequenz": "Hinweis auf zu hohe aktuelle Exposition: Biomonitoring zum "
                   "Schichtende veranlassen (BGW-Vergleich nach TRGS 903), Exposition und "
                   "Schutzmaßnahmen erfragen. Anhaltspunkte für unzureichenden "
                   "Arbeitsschutz dem Unternehmen mitteilen und Schutzmaßnahmen "
                   "vorschlagen (§ 6 (4) ArbMedVV); Überprüfung der "
                   "Gefährdungsbeurteilung anstoßen."},
    {"wenn": {"konzentration": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Nachlassen von Konzentration oder Gedächtnis angegeben.",
     "konsequenz": "Mögliches Frühzeichen einer toxischen Enzephalopathie (BK-Nr. 1317): "
                   "orientierende neurologische Untersuchung, in unklaren Fällen "
                   "weiterführende fachärztliche (neurologisch-psychiatrische) "
                   "Untersuchung veranlassen; Expositionshöhe und Biomonitoring "
                   "einbeziehen."},
    {"wenn": {"haut_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3, 7.2.2 und 8.1",
     "befund": "Hautprobleme (trockene, rissige, gerötete Haut, Ekzem) angegeben.",
     "konsequenz": "Inspektion der Haut durchführen; Hautschutzberatung (Handschuhe, "
                   "Hautschutzplan, Hygiene). Bei ausgeprägtem oder wiederkehrendem Ekzem "
                   "hautärztliche Abklärung und BK-Nr. 5101 bedenken; ggf. Maßnahmen nach "
                   "7.4.2."},
    {"wenn": {"augen_reiz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen/Schleimhäute",
     "quelle": "Abschnitte 6.3.1 und 7.4",
     "befund": "Wiederkehrende Reizung von Augen oder Schleimhäuten bei der Arbeit.",
     "konsequenz": "Abklären, ob chronische konjunktivale Reizerscheinungen vorliegen "
                   "(dann Beurteilung nach 7.4); Expositionssituation prüfen und dem "
                   "Unternehmen ggf. Lüftungs-/Schutzmaßnahmen vorschlagen."},
    # ── Hautkontakt und PSA (Abschnitte 6.2, 8.1 und 8.2) ─────────────────
    {"wenn": {"hautkontakt": ["yes"], "handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Hautschutz/PSA",
     "quelle": "Abschnitte 6.2, 8.1 und 8.2",
     "befund": "Direkter Hautkontakt mit Toluol/Xylol ohne konsequente Schutzhandschuhe.",
     "konsequenz": "Wegen der hautresorptiven Eigenschaften intensiv zu PSA beraten "
                   "(geeignete Handschuhmaterialien nach Sicherheitsdatenblatt bzw. "
                   "GESTIS/GISCHEM/WINGIS, Hygiene, Kleidungswechsel). Biomonitoring "
                   "erwägen (erfasst auch die Hautaufnahme). Reichen die Schutzmaßnahmen "
                   "nicht aus, Mitteilung an das Unternehmen mit Maßnahmenvorschlag "
                   "(§ 6 (4) ArbMedVV)."},
    {"wenn": {"hygiene": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 8.1",
     "befund": "Benetzte Arbeitskleidung wird nicht zügig gewechselt bzw. Händehygiene fehlt.",
     "konsequenz": "Beratung zu Hygienemaßnahmen: benetzte Kleidung sofort wechseln, "
                   "Hände vor Pausen reinigen, Hautkontakt und Einatmen von Dämpfen "
                   "vermeiden."},
    # ── Kombinations- und Mischexposition (Abschnitte 6.1 und 6.4) ────────
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Ototoxische Kombinationswirkung",
     "quelle": "Abschnitt 6.1",
     "befund": "Lösungsmitteltätigkeit im Lärmbereich angegeben.",
     "konsequenz": "Mögliche Kombinationswirkung der ototoxischen Stoffe Toluol/Xylol mit "
                   "Lärm bei der Gehörvorsorge nach der DGUV Empfehlung »Lärm« "
                   "berücksichtigen; Abgleich mit der Gefährdungsbeurteilung."},
    {"wenn": {"mischexposition": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 6.4 (Störfaktoren)",
     "befund": "Gleichzeitige Exposition gegenüber weiteren Lösungsmitteln angegeben.",
     "konsequenz": "Beim Biomonitoring mögliche Confounder beachten: Mischexposition "
                   "(z. B. m-Xylol mit Ethylbenzol oder 2-Butanon) kann die Ausscheidung "
                   "der Metabolite verändern; Ergebnisse entsprechend vorsichtig "
                   "interpretieren, ggf. Parameter ergänzen."},
    # ── Beratung Alkohol (Abschnitte 6.3.2 und 8.1) ───────────────────────
    {"wenn": {"alkohol_konsum": ["regelmaessig"]},
     "wenn_nicht": {"alkohol_abhaengigkeit": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 6.3.2 und 8.1",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung zum wirkungsverstärkenden Einfluss von konsumiertem Alkohol "
                   "auf Toluol/Xylol; ggf. Leberwerte (γ-GT, ALAT, ASAT) in die "
                   "Untersuchung einbeziehen."},
]
