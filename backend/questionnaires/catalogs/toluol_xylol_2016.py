# -*- coding: utf-8 -*-
"""G 29 Toluol und Xylol – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 29 »Toluol und Xylol«
(Fassung Oktober 2014), S. 429–438."""

SLUG = "g29-toluol_xylol-2016"

CATALOG = {
    "version": 2,
    "title": "G 29 Toluol und Xylol (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 29 »Toluol und Xylol« (Fassung Oktober 2014), S. 429–438",
    "sections": [
        # ── 1 ─ Anlass der Untersuchung ────────────────────────────────────
        {
            "id": "untersuchung",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Ist dies Ihre Erstuntersuchung nach G 29 (Toluol und Xylol)?",
                    "hint": "Erstuntersuchung: vor Aufnahme der Tätigkeit. "
                            "Nachuntersuchung: in der Regel nach 12–24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Ja, Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nein, Nachuntersuchung"},
                    ],
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Waren Sie seit der letzten Untersuchung schwer oder längere "
                             "Zeit krank?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wie lange waren Sie krank?",
                                 "when": "yes"},
                },
                {
                    "id": "verdacht_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie, dass gesundheitliche Beschwerden bei Ihnen mit "
                             "Ihrer Arbeit mit Toluol/Xylol zusammenhängen?",
                    "required": True,
                    "followup": {"id": "verdacht_zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
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
                        {"value": "beschichtung_gummi", "label": "Oberflächenbeschichtung in der Kunststoff- oder Gummiindustrie (Toluol)"},
                        {"value": "tankreinigung", "label": "Reinigen von Lagertanks für Xylol"},
                        {"value": "spritzbeschichtung", "label": "Spritzbeschichtung, Beschichten in Behältern oder Korrosionsschutzarbeiten"},
                        {"value": "histologie", "label": "Arbeiten mit Xylol im Labor (z. B. histologisches Labor) ohne wirksame Lüftung"},
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
                    "id": "schutzkleidung",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit möglichem Hautkontakt geeignete "
                             "Schutzhandschuhe bzw. Schutzkleidung?",
                    "hint": "Wegen der Aufnahme über die Haut ist Schutzkleidung bei "
                            "Toluol und Xylol besonders wichtig.",
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
            "subtitle": "Beschwerden, auf die bei Toluol und Xylol besonders geachtet wird",
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
                        {"value": "ermuedbarkeit", "label": "Schnelle Ermüdbarkeit (rasch erschöpft)"},
                        {"value": "uebelkeit", "label": "Übelkeit"},
                        {"value": "appetitlosigkeit", "label": "Appetitlosigkeit"},
                        {"value": "gewichtsabnahme", "label": "Ungewollte Gewichtsabnahme"},
                        {"value": "alkoholintoleranz", "label": "Alkohol wird schlechter vertragen als früher (Alkoholintoleranz)"},
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
                    "id": "parasthesien",
                    "type": "yes_no",
                    "label": "Haben Sie häufiger Kribbeln, »Ameisenlaufen« oder "
                             "Taubheitsgefühle in Händen oder Füßen (Parästhesien)?",
                    "required": True,
                },
                {
                    "id": "neurasthenie",
                    "type": "yes_no",
                    "label": "Leiden Sie unter anhaltender Nervosität, Reizbarkeit, "
                             "Schlafstörungen oder auffälligen Stimmungsveränderungen?",
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
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
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
    # ── Dauernde gesundheitliche Bedenken (Abschnitt 2.1.1) ───────────────
    {"wenn": {"neuro_erkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 2.1.1/2.1.2 (gesundheitliche Bedenken) und 1.2.3",
     "befund": "Neurologische Erkrankung in der Vorgeschichte angegeben.",
     "konsequenz": "Bei erheblichen neurologischen Störungen bestehen dauernde "
                   "gesundheitliche Bedenken (2.1.1); ist eine Wiederherstellung zu "
                   "erwarten, befristete Bedenken (2.1.2). Ausmaß ärztlich klären, "
                   "orientierende neurologische Untersuchung, in unklaren Fällen "
                   "fachärztliche Ergänzungsuntersuchung. Bei weniger ausgeprägten "
                   "Störungen Schutzmaßnahmen und verkürzte Nachuntersuchungsfristen "
                   "prüfen (2.1.3)."},
    {"wenn": {"alkohol_abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 2.1.1/2.1.2 und 2.2",
     "befund": "Alkoholabhängigkeit angegeben.",
     "konsequenz": "Bei Alkoholabhängigkeit bestehen dauernde gesundheitliche Bedenken "
                   "(2.1.1); bei zu erwartender Wiederherstellung befristete Bedenken "
                   "(2.1.2). Ausmaß klären (u. a. γ-GT, ALAT, ASAT), Behandlung "
                   "empfehlen, Beratung zum potenzierenden Einfluss von Alkohol auf die "
                   "Stoffwirkung."},
    {"wenn": {"atemwegserkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 2.1.1/2.1.2",
     "befund": "Obstruktive Atemwegserkrankung (z. B. Asthma, COPD) angegeben.",
     "konsequenz": "Bei obstruktiven Atemwegserkrankungen bestehen dauernde "
                   "gesundheitliche Bedenken (2.1.1); bei zu erwartender "
                   "Wiederherstellung befristete Bedenken (2.1.2). Schweregrad klären; "
                   "bei weniger ausgeprägter Erkrankung prüfen, ob Aufnahme/Fortsetzung "
                   "der Tätigkeit mit Schutzmaßnahmen (2.1.3) möglich ist."},
    # ── Keine Bedenken unter Voraussetzungen (Abschnitt 2.1.3) ────────────
    {"wenn": {"hauterkrankung_chron": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitt 2.1.3",
     "befund": "Chronisch-entzündliche Hauterkrankung angegeben.",
     "konsequenz": "Keine gesundheitlichen Bedenken nur unter bestimmten Voraussetzungen: "
                   "technische/organisatorische Schutzmaßnahmen, Einsatz an Arbeitsplätzen "
                   "mit geringerer Exposition, persönliche Schutzausrüstung unter "
                   "Beachtung des Hautzustandes sowie verkürzte Nachuntersuchungsfristen "
                   "prüfen; Hautbefund dokumentieren."},
    {"wenn": {"augen_chron": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen",
     "quelle": "Abschnitt 2.1.3",
     "befund": "Chronische konjunktivale Reizerscheinungen angegeben.",
     "konsequenz": "Bei ausgeprägten chronischen Bindehautreizungen keine Bedenken nur "
                   "unter bestimmten Voraussetzungen: Expositionsminderung, "
                   "Schutzmaßnahmen und verkürzte Nachuntersuchungsfristen prüfen; ggf. "
                   "augenärztliche Abklärung."},
    # ── Zwischenanamnese: Warnsymptome (Abschnitte 1.2.1, 1.2.2, 1.2.3) ───
    {"wenn": {"symptome": ["kopfschmerzen", "schwindel", "ermuedbarkeit", "uebelkeit",
                           "appetitlosigkeit", "gewichtsabnahme", "alkoholintoleranz"]},
     "schwere": "pruefen",
     "bereich": "Tätigkeitsspezifische Symptome",
     "quelle": "Abschnitte 1.2.1 (Zwischenanamnese) und 1.2.2/1.2.3",
     "befund": "Symptome, auf die nach G 29 besonders zu achten ist (Kopfschmerzen, "
               "Schwindel, Ermüdbarkeit, Übelkeit, Appetitlosigkeit, Gewichtsabnahme "
               "oder Alkoholintoleranz), angegeben.",
     "konsequenz": "Spezielle Untersuchung vollständig durchführen: großes Blutbild, "
                   "Biomonitoring (Toluol bzw. Xylol im Vollblut, o-Kresol bzw. "
                   "Methylhippursäure im Urin, BGW nach TRGS 903; entfällt nur bei "
                   "Erstuntersuchung), "
                   "γ-GT/ALAT/ASAT und orientierende neurologische Untersuchung. In "
                   "unklaren Fällen fachärztliche Ergänzungsuntersuchung; vorgezogene "
                   "Nachuntersuchung nach ärztlichem Ermessen."},
    {"wenn": {"akut_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Akute Überexposition",
     "quelle": "Abschnitte 3.2.2 und 2.2",
     "befund": "Pränarkotische Beschwerden (Benommenheit, Rauschgefühl, Gangunsicherheit) "
               "während oder nach der Arbeit angegeben.",
     "konsequenz": "Hinweis auf zu hohe aktuelle Exposition (Gefahr von Exzitation und "
                   "Narkose bei akuter Intoxikation): Biomonitoring zum Schichtende "
                   "veranlassen, Expositionssituation klären. Dem Arbeitgeber die "
                   "notwendige Aktualisierung der Gefährdungsbeurteilung mitteilen "
                   "(unter Wahrung der schutzwürdigen Belange der untersuchten Person)."},
    {"wenn": {"parasthesien": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 3.2.3, 1.2.2/1.2.3 und 4",
     "befund": "Parästhesien (Kribbeln, Taubheitsgefühle) angegeben.",
     "konsequenz": "Mögliches Zeichen einer chronischen Lösungsmittelschädigung: "
                   "orientierende neurologische Untersuchung, in unklaren Fällen "
                   "neurologische Ergänzungsuntersuchung. An BK-Nr. 1317 "
                   "(Polyneuropathie/Enzephalopathie) denken, ggf. BK-Anzeige prüfen; "
                   "verkürzte Nachuntersuchungsfrist erwägen."},
    {"wenn": {"neurasthenie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 3.2.3 und 1.2.3",
     "befund": "Neurasthenische Beschwerden (Nervosität, Reizbarkeit, Schlafstörungen, "
               "Stimmungsveränderungen) angegeben.",
     "konsequenz": "Auf chronische Gesundheitsschädigung (neurasthenische Beschwerden, "
                   "u. U. psychische Verhaltensstörungen) achten: Zusammenhang mit der "
                   "Exposition klären, orientierende neurologische Untersuchung, in "
                   "unklaren Fällen fachärztliche Ergänzungsuntersuchung."},
    {"wenn": {"haut_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 3.2.1 und 2.1.3/2.2",
     "befund": "Hautprobleme (trockene, rissige, gerötete Haut, Ekzem) angegeben.",
     "konsequenz": "Dermatitiden durch die entfettende Wirkung möglich: Haut ärztlich "
                   "beurteilen, Hautschutz und geeignete Schutzkleidung beraten "
                   "(GESTIS-Hinweise »Umgang und Verwendung«); bei ausgeprägtem Befund "
                   "Voraussetzungen nach 2.1.3 und verkürzte Nachuntersuchungsfrist "
                   "prüfen."},
    {"wenn": {"augen_reiz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augen/Schleimhäute",
     "quelle": "Abschnitte 3.2.1 und 2.1.3",
     "befund": "Wiederkehrende Reizung von Augen oder Schleimhäuten bei der Arbeit.",
     "konsequenz": "Abklären, ob chronische konjunktivale Reizerscheinungen vorliegen "
                   "(dann Beurteilung nach 2.1.3); Expositionssituation und Lüftung "
                   "prüfen, ggf. Mitteilung an den Arbeitgeber zur Aktualisierung der "
                   "Gefährdungsbeurteilung."},
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Schwere oder längere Erkrankung seit der letzten Untersuchung angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt: prüfen, ob die Erkrankung "
                   "Anlass zu Bedenken gegen die Fortsetzung der Tätigkeit gibt; "
                   "Befunde/Arztberichte einholen und Beurteilung nach Abschnitt 2.1 "
                   "vornehmen."},
    {"wenn": {"verdacht_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitte 1.1 und 4",
     "befund": "Die untersuchte Person vermutet einen Zusammenhang zwischen Beschwerden "
               "und der Tätigkeit.",
     "konsequenz": "Nachuntersuchung (auch außerhalb der Frist von 12–24 Monaten) "
                   "durchführen; Beschwerden gezielt abklären (inkl. Biomonitoring). Bei "
                   "begründetem Verdacht auf eine Berufskrankheit (BK-Nr. 1303 bzw. 1317) "
                   "ärztliche BK-Anzeige erstatten."},
    # ── Benzolgehalt (Vorbemerkungen) ─────────────────────────────────────
    {"wenn": {"benzol_anteil": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Benzol-Mischexposition",
     "quelle": "Vorbemerkungen",
     "befund": "Verwendete Produkte enthalten mehr als 0,1 Gew.-% Benzol.",
     "konsequenz": "Grundsatz G 8 »Benzol« in die Untersuchung einbeziehen (Benzol ist "
                   "krebserzeugend; dortiges Untersuchungs- und Biomonitoringprogramm "
                   "anwenden). Sicherheitsdatenblätter anfordern und die "
                   "Gefährdungsbeurteilung abgleichen."},
    # ── Hautkontakt und PSA (Abschnitte 3.1.3 und 2.2) ────────────────────
    {"wenn": {"hautkontakt": ["yes"], "schutzkleidung": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Hautschutz/PSA",
     "quelle": "Abschnitte 3.1.3 und 2.2",
     "befund": "Direkter Hautkontakt mit Toluol/Xylol ohne konsequente Schutzkleidung.",
     "konsequenz": "Wegen der hautresorptiven Eigenschaften intensiv zu Schutzkleidung "
                   "und Hygienemaßnahmen beraten (stoffspezifische Hinweise in GESTIS, "
                   "Rubrik »Umgang und Verwendung«). Biomonitoring zur Erfassung der "
                   "tatsächlichen Belastung nutzen; bei unzureichendem Schutz dem "
                   "Arbeitgeber die Aktualisierung der Gefährdungsbeurteilung mitteilen."},
    # ── Kombinations- und Mischexposition (Abschnitte 3.1.1 und 3.1.4) ────
    {"wenn": {"laermbereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Ototoxische Kombinationswirkung",
     "quelle": "Abschnitt 3.1.1",
     "befund": "Lösungsmitteltätigkeit im Lärmbereich angegeben.",
     "konsequenz": "Mögliche Kombinationswirkung der ototoxischen Stoffe Toluol/Xylol mit "
                   "Lärm bei der Gehörvorsorge nach Grundsatz G 20 »Lärm« "
                   "berücksichtigen."},
    {"wenn": {"mischexposition": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitt 3.1.4 (Störfaktoren)",
     "befund": "Gleichzeitige Exposition gegenüber weiteren Lösungsmitteln angegeben.",
     "konsequenz": "Beim Biomonitoring mögliche Confounder beachten: Mischexposition "
                   "(z. B. m-Xylol mit Ethylbenzol oder 2-Butanon) kann Blutwerte und "
                   "Metabolitenausscheidung verändern; Ergebnisse entsprechend vorsichtig "
                   "interpretieren."},
    # ── Beratung Alkohol (Abschnitt 2.2) ──────────────────────────────────
    {"wenn": {"alkohol_konsum": ["regelmaessig"]},
     "wenn_nicht": {"alkohol_abhaengigkeit": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Beratung zum potenzierenden Einfluss von konsumiertem Alkohol auf die "
                   "Wirkung von Toluol/Xylol; γ-GT, ALAT und ASAT in die Untersuchung "
                   "einbeziehen (erwünschter Untersuchungsteil)."},
]
