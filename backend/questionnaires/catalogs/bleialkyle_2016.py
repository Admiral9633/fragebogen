# -*- coding: utf-8 -*-
"""G 3 Bleialkyle – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 6. Auflage 2016, G 3 »Bleialkyle«
(Fassung Oktober 2014), S. 133–143."""

SLUG = "g3-bleialkyle-2016"

CATALOG = {
    "version": 2,
    "title": "G 3 Bleialkyle (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 3 »Bleialkyle« (Fassung Oktober 2014), S. 133–143",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "anlass",
            "title": "Anlass der Untersuchung",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung nach dem Grundsatz G 3 (Bleialkyle) "
                             "handelt es sich?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt, "
                            "Nachuntersuchungen in der Regel nach 12 bis 24 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung"},
                        {"value": "vorzeitig", "label": "Vorzeitige Nachuntersuchung (z. B. nach Erkrankung "
                                                        "oder auf eigenen Wunsch)"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Kontakt mit Bleialkylen",
            "subtitle": "Ihre Arbeit mit Bleitetraethyl/Bleitetramethyl oder verbleitem Kraftstoff",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "expo_bereiche",
                    "type": "multi_choice",
                    "label": "Bei welchen Arbeiten haben Sie mit Bleialkylen oder verbleitem "
                             "Kraftstoff zu tun?",
                    "hint": "Mehrfachauswahl möglich. Verbleiter Kraftstoff ist heute vor allem "
                            "Flugbenzin (AvGas) für Flugzeuge mit Kolbenmotor.",
                    "required": True,
                    "options": [
                        {"value": "herstellung", "label": "Herstellung von Bleialkylen"},
                        {"value": "zumischen", "label": "Zumischen von Bleialkylen zu Kraftstoffen für den "
                                                        "Flugbetrieb (AvGas)"},
                        {"value": "tank_befuellen", "label": "Befüllen oder Entladen von Tankfahrzeugen/Kesselwagen "
                                                             "(z. B. Füllschläuche anschließen und abschlagen)"},
                        {"value": "tank_reinigen", "label": "Reinigen von Kesselwagen, Tanks oder Rohrleitungen, in "
                                                            "denen Bleialkyle oder verbleiter Kraftstoff waren"},
                        {"value": "tankstellensanierung", "label": "Sanierung alter Tankstellen"},
                        {"value": "zapfanlagen", "label": "Wartung/Reparatur von Zapfanlagen für verbleiten Kraftstoff "
                                                          "auf Flugplätzen"},
                        {"value": "betanken", "label": "Betanken von Flugzeugen mit Kolbenmotoren"},
                        {"value": "motor_reparatur", "label": "Reparaturen an kraftstoffführenden Teilen von "
                                                              "Flugzeug-Kolbenmotoren"},
                        {"value": "werkstatt", "label": "Werkstatt für Fahrzeuge mit bleihaltigem Kraftstoff "
                                                        "(z. B. Oldtimer)"},
                        {"value": "keine", "label": "Keine dieser Arbeiten"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit mit Bleialkylen oder verbleitem "
                             "Kraftstoff in Berührung (z. B. benetzte Hände, durchfeuchtete "
                             "Kleidung, Spritzer)?",
                    "hint": "Bleialkyle werden auch über die Haut in den Körper aufgenommen "
                            "(erhöhte Resorptionsgefahr).",
                    "required": True,
                },
                {
                    "id": "frueher_blei",
                    "type": "yes_no",
                    "label": "Haben Sie längere Zeit in Bleibetrieben gearbeitet, vermehrt Blei "
                             "aufgenommen oder hatten Sie schon einmal eine Bleivergiftung?",
                    "required": True,
                    "followup": {"id": "frueher_blei_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten bzw. was ist damals festgestellt "
                                          "worden?", "when": "yes"},
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es Zwischenfälle, bei denen Sie dem Stoff stärker ausgesetzt "
                             "waren (z. B. Verschütten, Leckage, Übergießen)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "laerm_bereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie bei diesen Tätigkeiten in Lärmbereichen (so laut, "
                             "dass Gehörschutz vorgeschrieben ist)?",
                    "hint": "Bleialkyle können das Innenohr zusätzlich belasten (ototoxische "
                            "Wirkung).",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen und Hygiene ────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Schutzausrüstung und Hygiene an Ihrem Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_nutzung",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit möglichem Kontakt die vorgesehene "
                             "persönliche Schutzausrüstung (z. B. beständige Schutzhandschuhe, "
                             "Schutzkleidung, ggf. Atemschutz)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "Für meine Arbeit ist keine Schutzausrüstung vorgesehen / "
                                                           "Tätigkeit beginnt erst"},
                    ],
                },
                {
                    "id": "hygiene_essen",
                    "type": "yes_no",
                    "label": "Essen, trinken oder rauchen Sie in Arbeitsbereichen, in denen mit "
                             "Bleialkylen oder verbleitem Kraftstoff umgegangen wird?",
                    "required": True,
                },
                {
                    "id": "kleidung_wechsel",
                    "type": "yes_no",
                    "label": "Wechseln Sie nach der Arbeit die Arbeitskleidung und waschen sich "
                             "gründlich, bevor Sie nach Hause gehen?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, auf die bei Bleialkylen besonders geachtet wird",
            "questions": [
                {
                    "id": "beschwerden_zns",
                    "type": "multi_choice",
                    "label": "Haben Sie in letzter Zeit eine oder mehrere dieser Beschwerden?",
                    "hint": "Mehrfachauswahl möglich. Bleialkyle wirken vor allem auf das "
                            "Nervensystem.",
                    "required": True,
                    "options": [
                        {"value": "angsttraeume", "label": "Ausgeprägte Angstträume (Albträume)"},
                        {"value": "schlafstoerungen", "label": "Schlafstörungen"},
                        {"value": "verstimmung", "label": "Stärkere Verstimmung oder gedrückte Stimmung"},
                        {"value": "gewichtsabnahme", "label": "Ungewollte Gewichtsabnahme"},
                        {"value": "haendezittern", "label": "Zittern der Hände"},
                        {"value": "uebelkeit", "label": "Übelkeit, Appetitlosigkeit oder Erbrechen"},
                        {"value": "kopf_schwindel", "label": "Kopfschmerzen oder Schwindel"},
                        {"value": "verwirrtheit", "label": "Verwirrtheit, Halluzinationen (Dinge sehen/hören, die "
                                                           "nicht da sind) oder Angstzustände"},
                        {"value": "kreislauf", "label": "Kreislaufbeschwerden: Schwächegefühl, sehr niedriger "
                                                        "Blutdruck oder ungewöhnlich langsamer Puls"},
                        {"value": "keine", "label": "Keine dieser Beschwerden"},
                    ],
                },
                {
                    "id": "beschwerden_verlauf",
                    "type": "textarea",
                    "label": "Falls Sie Beschwerden angekreuzt haben: seit wann bestehen sie, "
                             "und bessern sie sich an freien Tagen oder im Urlaub?",
                    "required": False,
                },
                {
                    "id": "gereiztheit",
                    "type": "yes_no",
                    "label": "Haben andere Menschen (Familie, Kolleginnen/Kollegen) Ihnen "
                             "zurückgemeldet, dass Sie in letzter Zeit gereizter sind oder "
                             "häufiger in Streit geraten?",
                    "required": True,
                },
                {
                    "id": "zusammenhang_taetigkeit",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen Beschwerden und Ihrer "
                             "Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "vorzeitig"]},
                    "followup": {"id": "zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und warum vermuten Sie den "
                                          "Zusammenhang?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, die bei Bleialkylen wichtig sind",
            "questions": [
                {
                    "id": "vorerkrankungen_liste",
                    "type": "multi_choice",
                    "label": "Wurde bei Ihnen eine dieser Erkrankungen festgestellt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "blut", "label": "Erkrankung des Blutes (z. B. Blutarmut/Anämie)"},
                        {"value": "herz_kreislauf", "label": "Erkrankung des Herzens oder des Kreislaufs"},
                        {"value": "lunge", "label": "Erkrankung der Lunge (z. B. Asthma, Tuberkulose)"},
                        {"value": "nase_rachen", "label": "Erkrankung im Nasen- oder Rachenraum"},
                        {"value": "leber", "label": "Lebererkrankung"},
                        {"value": "niere", "label": "Nierenerkrankung"},
                        {"value": "stoffwechsel", "label": "Stoffwechselerkrankung (z. B. Diabetes/Zuckerkrankheit, Gicht)"},
                        {"value": "nervensystem", "label": "Erkrankung des Nervensystems (z. B. Nervenschäden, "
                                                           "Krampfanfälle/Epilepsie)"},
                        {"value": "haut", "label": "Hauterkrankung, besonders Ekzeme (juckende, entzündete Haut)"},
                        {"value": "keine", "label": "Keine dieser Erkrankungen"},
                    ],
                },
                {
                    "id": "vorerkrankungen_desc",
                    "type": "textarea",
                    "label": "Falls Sie etwas angekreuzt haben: welche Erkrankung, seit wann, "
                             "wie schwer, und sind Sie in Behandlung?",
                    "required": False,
                },
                {
                    "id": "psychisch",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine schwere psychische Erkrankung festgestellt "
                             "(z. B. Psychose, schwere Depression)?",
                    "required": True,
                },
                {
                    "id": "sucht",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen eine Abhängigkeit von Alkohol, Medikamenten "
                             "oder Drogen?",
                    "hint": "Diese Angabe ist wichtig, weil einige Wirkungen der Bleialkyle "
                            "ähnliche Beschwerden verursachen können.",
                    "required": True,
                },
                {
                    "id": "syphilis",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Syphilis (Lues) festgestellt, die nicht oder "
                             "nicht vollständig behandelt wurde?",
                    "hint": "Diese Frage steht im Grundsatz G 3, weil eine unbehandelte "
                            "Syphilis ähnliche Nervensymptome verursachen kann wie Bleialkyle.",
                    "required": True,
                },
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder länger "
                             "dauernde Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "vorzeitig"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Sind Sie derzeit schwanger oder stillen Sie?",
                    "hint": "Bleialkyle können das ungeborene Kind schädigen und die "
                            "Fortpflanzungsfähigkeit beeinträchtigen; darüber wird bei der "
                            "Untersuchung beraten.",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein / trifft nicht auf mich zu"},
                        {"value": "schwanger", "label": "Ja, ich bin schwanger"},
                        {"value": "stillt", "label": "Ja, ich stille"},
                        {"value": "keine_angabe", "label": "Keine Angabe"},
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
    # ── Exposition → spezielle Untersuchung/Biomonitoring (1.2.2, 3.1.4) ──
    {"wenn": {"expo_bereiche": ["herstellung", "zumischen", "tank_befuellen", "tank_reinigen",
                                "tankstellensanierung", "zapfanlagen", "betanken",
                                "motor_reparatur", "werkstatt"]},
     "schwere": "pruefen",
     "bereich": "Exposition/Biomonitoring",
     "quelle": "Abschnitte 1.2.2 und 3.1.4",
     "befund": "Tätigkeit mit zu erwartender Bleialkyl-Exposition angegeben.",
     "konsequenz": "Spezielle Untersuchung durchführen (großes Blutbild, Kreatinin im Serum, "
                   "SGPT, SGOT, γ-GT) und Biomonitoring nach Exposition: bei Bleitetraethyl "
                   "Diethylblei im Urin (BGW 25 µg/l, als Pb berechnet) und Gesamtblei im "
                   "Urin (BGW 50 µg/l, gilt auch für Gemische mit Bleitetramethyl); bei "
                   "Bleitetramethyl Gesamtblei im Urin (BGW 50 µg/l). Probennahme am "
                   "Expositions- bzw. Schichtende."},
    {"wenn": {"frueher_blei": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Bleibelastung",
     "quelle": "Abschnitt 2.1.2 (Befristete gesundheitliche Bedenken)",
     "befund": "Längere Tätigkeit in Bleibetrieben, vermehrte Bleiaufnahme oder frühere "
               "Bleivergiftung angegeben.",
     "konsequenz": "Befristete gesundheitliche Bedenken erwägen (2.1.2): Vorbefunde und "
                   "frühere Biomonitoring-Werte einholen, aktuelles Biomonitoring "
                   "durchführen; Wiederaufnahme bzw. Fortsetzung der Tätigkeit erst nach "
                   "Klärung, ggf. verkürzte Nachuntersuchungsfristen."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitte 1.2.2 und 3.2.2",
     "befund": "Zwischenfall mit erhöhter Exposition angegeben.",
     "konsequenz": "Hergang dokumentieren; Biomonitoring (Urinblei) zur Objektivierung der "
                   "Aufnahme veranlassen; auf Intoxikationszeichen achten (Symptome treten "
                   "oft erst nach Stunden bis Tagen auf); ggf. vorzeitige Nachuntersuchung "
                   "nach ärztlichem Ermessen (1.1)."},
    # ── Beschwerden/Intoxikationszeichen (1.2.1, 2.1.1, 2.1.2, 3.2) ───────
    {"wenn": {"beschwerden_zns": ["angsttraeume", "schlafstoerungen", "verstimmung",
                                  "gewichtsabnahme", "haendezittern", "uebelkeit",
                                  "kopf_schwindel", "kreislauf"]},
     "schwere": "pruefen",
     "bereich": "Intoxikationsverdacht",
     "quelle": "Abschnitte 1.2.1 (Besonders achten auf), 2.1.2 und 3.2.2",
     "befund": "Stoffspezifische Beschwerden angegeben (z. B. Angstträume, Schlafstörungen, "
               "Verstimmung, Gewichtsabnahme, Händezittern, Übelkeit, Kopfschmerz/Schwindel, "
               "Kreislaufstörungen).",
     "konsequenz": "Verdacht auf Bleialkyl-Wirkung abklären: Biomonitoring (Urinblei bzw. "
                   "Diethylblei im Urin) und spezielle Untersuchung nach 1.2.2. Bei "
                   "eindeutigen Anzeichen einer Intoxikation oder dringendem Verdacht sowie "
                   "bei Gesamtbleiausscheidung im Harn > 50 µg/l befristete gesundheitliche "
                   "Bedenken bis zum Abklingen der Symptome (2.1.2)."},
    {"wenn": {"beschwerden_zns": ["verwirrtheit"]},
     "schwere": "kritisch",
     "bereich": "Intoxikationsverdacht",
     "quelle": "Abschnitte 2.1.1 (Nachuntersuchung) und 3.2.2",
     "befund": "Verwirrtheit, Halluzinationen oder Angstzustände angegeben – mögliche "
               "eindeutige Anzeichen einer Bleialkyl-Intoxikation.",
     "konsequenz": "Klärung vor (weiterem) Einsatz: Blut- und Urinblei bestimmen "
                   "(entscheidend für die Differentialdiagnose ist allein der Bleigehalt in "
                   "Blut bzw. Urin), neurologisch-psychiatrische Abklärung. Zunächst "
                   "befristete Bedenken (2.1.2); bei Fortbestehen eindeutiger "
                   "Intoxikationszeichen (Depression, schizoide Verwirrtheitszustände, "
                   "erhöhter Blut-/Urinbleispiegel) dauernde gesundheitliche Bedenken "
                   "(2.1.1)."},
    {"wenn": {"gereiztheit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Intoxikationsverdacht",
     "quelle": "Abschnitt 1.2.1 (Besonders achten auf: Gereiztheit, Streitsucht)",
     "befund": "Fremdanamnestisch bemerkte Gereiztheit bzw. vermehrte Konflikte angegeben.",
     "konsequenz": "Ohne Suggestivfragen ärztlich vertiefen (Hinweis auf mögliche "
                   "ZNS-Wirkung); Biomonitoring und spezielle Untersuchung nach 1.2.2 "
                   "veranlassen; Differentialdiagnosen abgrenzen."},
    # ── Vorerkrankungen → Bedenken-Systematik (2.1.1 bis 2.1.3) ───────────
    {"wenn": {"vorerkrankungen_liste": ["blut", "herz_kreislauf", "lunge", "nase_rachen",
                                        "leber", "niere", "stoffwechsel", "nervensystem",
                                        "haut"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankungen",
     "quelle": "Abschnitte 2.1.1 und 2.1.3",
     "befund": "Vorerkrankung eines im Grundsatz genannten Organsystems angegeben (Blut, "
               "Herz-Kreislauf, Lunge, Nasen-/Rachenraum, Leber, Niere, Stoffwechsel, "
               "Nervensystem oder Haut).",
     "konsequenz": "Schweregrad klären: bei schweren Gesundheitsstörungen dauernde "
                   "gesundheitliche Bedenken (2.1.1); bei weniger ausgeprägten Erkrankungen "
                   "oder grenzwertigen Laborwerten keine Bedenken unter bestimmten "
                   "Voraussetzungen (2.1.3): technische/organisatorische Schutzmaßnahmen, "
                   "Begrenzung der Expositionszeit, Einsatz an Arbeitsplätzen mit geringerer "
                   "Exposition, PSA, verkürzte Nachuntersuchungsfristen. Bei erwarteter "
                   "Wiederherstellung befristete Bedenken (2.1.2)."},
    {"wenn": {"psychisch": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Psychische Erkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Schwere psychische Erkrankung (Geisteskrankheit im Sinne des Grundsatzes) "
               "angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken prüfen (2.1.1): fachärztliche "
                   "(psychiatrische) Befunde einholen und vor Aufnahme bzw. Fortsetzung der "
                   "Tätigkeit klären; nur bei leichter Ausprägung Aufnahme unter den "
                   "Voraussetzungen von 2.1.3 mit verkürzten Nachuntersuchungsfristen "
                   "erwägen."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Abhängigkeitserkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Alkohol-, Medikamenten- oder Drogenabhängigkeit angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken prüfen (2.1.1); Klärung vor Aufnahme "
                   "bzw. Fortsetzung der Tätigkeit. Erschwerte Differentialdiagnose beachten "
                   "(Intoxikationssymptome sind mit Alkoholismus/Rauschmittelsucht "
                   "verwechselbar – entscheidend ist der Bleigehalt in Blut bzw. Urin)."},
    {"wenn": {"syphilis": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Syphilis",
     "quelle": "Abschnitte 2.1.1 und 1.2.3 (Ergänzungsuntersuchung)",
     "befund": "Unbehandelte oder nicht ausgeheilte Syphilis (Lues) angegeben.",
     "konsequenz": "Dauernde gesundheitliche Bedenken prüfen (2.1.1); in unklaren Fällen "
                   "Ergänzungsuntersuchung TPHA im Serum (1.2.3). Behandlung veranlassen; "
                   "Einsatz erst nach Klärung (Lues III ist Differentialdiagnose der "
                   "Bleialkyl-Intoxikation)."},
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenanamnese",
     "quelle": "Abschnitt 1.1 (Vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder länger dauernde Erkrankung seit der letzten Untersuchung "
               "angegeben.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist angezeigt (nach schwerer oder längerer "
                   "Erkrankung, die Anlass zu Bedenken gegen eine Fortsetzung der Tätigkeit "
                   "geben könnte); Befunde einholen und Bedenken-Systematik nach 2.1 "
                   "anwenden."},
    {"wenn": {"zusammenhang_taetigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenanamnese",
     "quelle": "Abschnitte 1.1 und 4 (Berufskrankheit)",
     "befund": "Vermuteter Zusammenhang zwischen Erkrankung/Beschwerden und der Tätigkeit "
               "am Arbeitsplatz.",
     "konsequenz": "Vorzeitige Nachuntersuchung durchführen (1.1); Beschwerden objektivieren "
                   "(Biomonitoring, spezielle Untersuchung). Bei begründetem Verdacht "
                   "BK-Anzeige prüfen (BK-Nr. 1101 »Erkrankungen durch Blei oder seine "
                   "Verbindungen«)."},
    # ── Hautkontakt, PSA, Hygiene (2.2, 3.1.3) ────────────────────────────
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautresorption",
     "quelle": "Abschnitte 3.1.3 und 2.2",
     "befund": "Hautkontakt mit Bleialkylen bzw. verbleitem Kraftstoff angegeben.",
     "konsequenz": "Erhöhte Resorptionsgefahr über die Haut (v. a. Bleitetraethyl): "
                   "Schutzmaßnahmen nach TRGS 401 prüfen (beständige Handschuhe, "
                   "Schutzkleidung), Biomonitoring durchführen; wenn die "
                   "Gefährdungsbeurteilung aktualisiert werden muss, Mitteilung an den "
                   "Arbeitgeber unter Wahrung der schutzwürdigen Belange (2.2)."},
    {"wenn": {"psa_nutzung": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 2.2 und 2.1.3",
     "befund": "Vorgesehene Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Beratung zu Hygienemaßnahmen und persönlicher Schutzausrüstung (2.2); "
                   "Ursachen klären. Ergibt sich Bedarf zur Verbesserung des "
                   "Arbeitsschutzes, Mitteilung an den Arbeitgeber (Aktualisierung der "
                   "Gefährdungsbeurteilung) unter Wahrung der schutzwürdigen Belange."},
    {"wenn": {"hygiene_essen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Essen, Trinken oder Rauchen in Arbeitsbereichen mit Bleialkyl-Umgang.",
     "konsequenz": "Beratung zu allgemeinen Hygienemaßnahmen: keine Nahrungsaufnahme und "
                   "kein Rauchen im Arbeitsbereich, Händewaschen vor Pausen; "
                   "stoffspezifische Hinweise zu Schutzmaßnahmen nach GESTIS beachten."},
    {"wenn": {"kleidung_wechsel": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Arbeitskleidung wird nach der Arbeit nicht gewechselt bzw. keine gründliche "
               "Reinigung.",
     "konsequenz": "Beratung: Arbeitskleidung wechseln, gründliche Hautreinigung nach "
                   "Arbeitsende; Verschleppung des hautresorptiven Stoffes vermeiden."},
    # ── Beratung Reproduktion (2.2) ───────────────────────────────────────
    {"wenn": {"schwangerschaft": ["schwanger", "stillt"]},
     "schwere": "pruefen",
     "bereich": "Mutterschutz/Reproduktion",
     "quelle": "Abschnitt 2.2 (Beratung: fruchtschädigende Wirkung)",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben.",
     "konsequenz": "Unverzüglich auf die mögliche fruchtschädigende sowie die "
                   "Fortpflanzungsfähigkeit beeinträchtigende Wirkung der Bleialkyle "
                   "hinweisen; Beschäftigungsbeschränkungen nach dem Mutterschutzgesetz "
                   "klären und den Arbeitgeber zur Anpassung der Gefährdungsbeurteilung "
                   "veranlassen (expositionsfreier Einsatz)."},
    # ── Kombinationswirkung Lärm (3.1.1) ──────────────────────────────────
    {"wenn": {"laerm_bereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 3.1.1",
     "befund": "Tätigkeit mit höherer Bleialkyl-Exposition in Lärmbereichen angegeben.",
     "konsequenz": "Wegen der ototoxischen Eigenschaft der Bleialkyle mögliche "
                   "Kombinationswirkungen mit Lärm bei der Gehöruntersuchung nach dem "
                   "DGUV Grundsatz G 20 berücksichtigen; Koordination beider "
                   "Untersuchungsanlässe."},
]
