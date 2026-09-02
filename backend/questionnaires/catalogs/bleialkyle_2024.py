# -*- coding: utf-8 -*-
"""Bleitetraethyl und Bleitetramethyl – DGUV Empfehlung 2024. Quelle: DGUV
Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen,
1. Auflage 2024, »Bleitetraethyl und Bleitetramethyl« (E OBP, Fassung
Januar 2022, Grenzwerte aktualisiert 2024), S. 139–156."""

SLUG = "bleialkyle-2024"

CATALOG = {
    "version": 2,
    "title": "Bleitetraethyl und Bleitetramethyl (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Bleitetraethyl und Bleitetramethyl« (E OBP, Fassung "
             "Januar 2022, Grenzwerte aktualisiert 2024), S. 139–156",
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
                             "Bleitetraethyl/Bleitetramethyl (Bleialkyle, z. B. in verbleitem "
                             "Flugbenzin)?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Vorsorge zu diesem Stoff"},
                        {"value": "weitere", "label": "Nein, ich war deswegen schon einmal zur Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: wenn der Arbeitsplatzgrenzwert nicht eingehalten "
                            "wird oder eine Gesundheitsgefährdung durch Hautkontakt nicht "
                            "ausgeschlossen werden kann. Angebotsvorsorge: wenn eine Exposition "
                            "nicht ausgeschlossen werden kann.",
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
            "title": "Tätigkeit & Kontakt mit Bleialkylen",
            "subtitle": "Ihre Arbeit mit Bleitetraethyl/Bleitetramethyl oder verbleitem Kraftstoff",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
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
                        {"value": "zumischen", "label": "Zumischen von Bleialkylen zu Kraftstoffen (z. B. AvGas-Herstellung)"},
                        {"value": "tank_befuellen", "label": "Befüllen oder Entladen von Tankfahrzeugen/Kesselwagen "
                                                             "(z. B. Füllschläuche anschließen und abschlagen)"},
                        {"value": "tank_reinigen", "label": "Reinigen oder Sanieren von Kesselwagen, Tanks oder Rohrleitungen, "
                                                            "in denen Bleialkyle oder verbleiter Kraftstoff waren"},
                        {"value": "tankstellensanierung", "label": "Sanierung alter Tankstellen"},
                        {"value": "zapfanlagen", "label": "Wartung/Reparatur von Zapfanlagen für verbleiten Kraftstoff "
                                                          "(z. B. auf Flugplätzen)"},
                        {"value": "betanken", "label": "Betanken von Flugzeugen mit älteren Kolbenmotoren"},
                        {"value": "motor_reparatur", "label": "Reparaturen an kraftstoffführenden Teilen von Flugzeug-Kolbenmotoren"},
                        {"value": "werkstatt", "label": "Spezialwerkstatt für Fahrzeuge, die bleihaltigen Kraftstoff benötigen "
                                                        "(z. B. Oldtimer)"},
                        {"value": "geschlossen_labor", "label": "Nur Umgang mit dicht geschlossenen Gebinden oder "
                                                                "Laborarbeit mit kleinen Mengen"},
                        {"value": "keine", "label": "Keine dieser Arbeiten"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit mit Bleialkylen oder verbleitem "
                             "Kraftstoff in Berührung (z. B. benetzte Hände, durchfeuchtete "
                             "Kleidung, Spritzer)?",
                    "hint": "Bleitetraethyl und Bleitetramethyl werden auch über die Haut in "
                            "den Körper aufgenommen.",
                    "required": True,
                },
                {
                    "id": "daempfe",
                    "type": "yes_no",
                    "label": "Atmen Sie bei der Arbeit Dämpfe oder Gerüche von Kraftstoff oder "
                             "Bleialkylen ein (süßlicher, etherähnlicher Geruch)?",
                    "required": True,
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es Zwischenfälle oder ungewöhnliche Betriebszustände, bei denen "
                             "Sie dem Stoff stärker ausgesetzt waren (z. B. Verschütten, "
                             "Leckage, Übergießen, defekte Absaugung)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_blei",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit Bleialkylen, "
                             "verbleitem Kraftstoff oder anderen Bleiverbindungen?",
                    "required": True,
                    "followup": {"id": "frueher_blei_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, wie lange, und gab es damals "
                                          "Untersuchungen oder auffällige Blei-Werte?", "when": "yes"},
                },
                {
                    "id": "laerm_bereich",
                    "type": "yes_no",
                    "label": "Arbeiten Sie bei diesen Tätigkeiten in Lärmbereichen (so laut, dass "
                             "Gehörschutz vorgeschrieben ist)?",
                    "hint": "Blei kann das Innenohr zusätzlich belasten (ototoxische Wirkung).",
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
                             "Schutzausrüstung (z. B. beständige Schutzhandschuhe, "
                             "Schutzkleidung, ggf. Atemschutz)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "Für meine Arbeit ist keine Schutzausrüstung vorgesehen"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme mit der Schutzausrüstung (z. B. Hautreizung "
                             "unter den Handschuhen, schlechte Passform, Atemschutz stört)?",
                    "required": True,
                    "show_if": {"id": "psa_nutzung", "not_in": ["nicht_noetig"]},
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
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
            "subtitle": "Beschwerden, auf die bei diesem Stoff besonders geachtet wird",
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
                        {"value": "verstimmung", "label": "Stärkere Verstimmung, gedrückte Stimmung oder Reizbarkeit"},
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
                    "id": "wesensveraenderung",
                    "type": "yes_no",
                    "label": "Haben Angehörige, Freunde oder Kolleginnen/Kollegen Ihnen "
                             "zurückgemeldet, dass sich Ihr Wesen oder Verhalten in letzter Zeit "
                             "verändert hat (z. B. reizbarer, aggressiver, verändert)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen, die bei diesem Stoff wichtig sind",
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
                        {"value": "atemwege", "label": "Erkrankung der Lunge oder Atemwege (z. B. Asthma, Tuberkulose)"},
                        {"value": "nase_rachen", "label": "Erkrankung im Nasen- oder Rachenraum"},
                        {"value": "leber", "label": "Lebererkrankung"},
                        {"value": "niere", "label": "Nierenerkrankung"},
                        {"value": "stoffwechsel", "label": "Stoffwechselerkrankung (z. B. Diabetes/Zuckerkrankheit, Gicht)"},
                        {"value": "nervensystem", "label": "Erkrankung des Nervensystems (z. B. Nervenschäden, "
                                                           "Krampfanfälle/Epilepsie)"},
                        {"value": "haut", "label": "Hauterkrankung, besonders Ekzeme (juckende, entzündete Haut)"},
                        {"value": "psychisch", "label": "Psychische Erkrankung (z. B. Depression, Psychose)"},
                        {"value": "keine", "label": "Keine dieser Erkrankungen"},
                    ],
                },
                {
                    "id": "vorerkrankungen_desc",
                    "type": "textarea",
                    "label": "Falls Sie etwas angekreuzt haben: welche Erkrankung, seit wann, "
                             "und sind Sie in Behandlung?",
                    "required": False,
                },
                {
                    "id": "sucht",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Medikamenten oder Drogen?",
                    "hint": "Diese Angabe ist wichtig, weil einige Wirkungen der Bleialkyle "
                            "ähnliche Beschwerden verursachen und das Nervensystem zusätzlich "
                            "belastet sein kann.",
                    "required": True,
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Berufskrankheit anerkannt, oder läuft derzeit "
                             "ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Berufskrankheit bzw. welches Verfahren?", "when": "yes"},
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Sind Sie derzeit schwanger oder stillen Sie?",
                    "hint": "Bleitetraethyl und Bleitetramethyl können das ungeborene Kind "
                            "schädigen (fortpflanzungsgefährdend, Kategorie 1A). Für werdende "
                            "und stillende Mütter gelten deshalb besondere Schutzregeln.",
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
    # ── Exposition → Biomonitoring (Abschnitte 6.4 und 7.2.2) ─────────────
    {"wenn": {"expo_bereiche": ["zumischen", "tank_befuellen", "tank_reinigen",
                                "tankstellensanierung", "zapfanlagen", "betanken",
                                "motor_reparatur", "werkstatt"]},
     "schwere": "pruefen",
     "bereich": "Exposition/Biomonitoring",
     "quelle": "Abschnitte 6.1.1, 6.4 und 7.2.2",
     "befund": "Tätigkeit mit höherer Bleialkyl-Exposition angegeben (anamnestisch "
               "festgestellte Exposition).",
     "konsequenz": "Biomonitoring als Bestandteil der Vorsorge durchführen: Blei im Vollblut, "
                   "Beurteilung anhand BLW 150 µg/l (Probennahme ohne Beschränkung); dazu "
                   "klinische Untersuchung nach 7.2.2 (Urinstatus, großes Blutbild, Kreatinin, "
                   "Leberenzyme). Abgleich der Angaben mit der Gefährdungsbeurteilung."},
    {"wenn": {"frueher_blei": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 7.1 (Arbeitsanamnese) und 7.2.2",
     "befund": "Frühere Tätigkeiten mit Bleialkylen bzw. Bleiverbindungen angegeben.",
     "konsequenz": "Frühere Expositionen und Vorbefunde (Biomonitoring-Werte, "
                   "Vorsorgebescheinigungen) einholen; Biomonitoring bereits bei der ersten "
                   "Vorsorge veranlassen (anamnestisch festgestellte Bleialkylexposition). "
                   "Kumulationsgefahr durch langsame Ausscheidung berücksichtigen."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese)",
     "befund": "Zwischenfall bzw. ungewöhnlicher Betriebszustand mit erhöhter Exposition "
               "angegeben.",
     "konsequenz": "Hergang dokumentieren; Biomonitoring (Blei im Vollblut) zur Objektivierung "
                   "der Aufnahme veranlassen; auf Intoxikationszeichen achten (Symptome treten "
                   "oft erst nach Stunden bis Tagen auf). Mitteilung an das Unternehmen nach "
                   "§ 6 (4) ArbMedVV prüfen, wenn Schutzmaßnahmen nicht ausreichen."},
    # ── Hautkontakt und PSA (Abschnitte 2, 6.2 und 8) ─────────────────────
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hautresorption",
     "quelle": "Abschnitte 2, 6.2 und 8.2",
     "befund": "Hautkontakt mit Bleialkylen bzw. verbleitem Kraftstoff angegeben.",
     "konsequenz": "Erhöhte Resorptionsgefahr über die Haut (v. a. Bleitetraethyl): "
                   "Hautkontakt begründet Pflichtvorsorge, wenn eine Gesundheitsgefährdung "
                   "nicht ausgeschlossen werden kann. Schutzmaßnahmen nach TRGS 401 prüfen "
                   "(beständige Handschuhe, Schutzkleidung), Biomonitoring veranlassen; bei "
                   "unzureichenden Maßnahmen Mitteilung an das Unternehmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"psa_nutzung": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 7.4.2, 8.1 und 8.2",
     "befund": "Vorgesehene Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA (unter Beachtung des "
                   "individuellen Gesundheitszustands); Ursachen der Nichtbenutzung klären. "
                   "Ergeben sich Anhaltspunkte, dass die Maßnahmen des Arbeitsschutzes nicht "
                   "ausreichen, Mitteilung an das Unternehmen und Vorschlag von "
                   "Schutzmaßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"psa_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitt 8.1",
     "befund": "Probleme mit der Schutzausrüstung angegeben.",
     "konsequenz": "Individuelle Beratung zur PSA-Auswahl (besondere individuelle Aspekte "
                   "aufzeigen); bei Hautproblemen unter Handschuhen Hautschutzplan und "
                   "Handschuhwechsel prüfen; ggf. Rückmeldung an das Unternehmen."},
    {"wenn": {"hygiene_essen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.4.2 (Hygieneregime) und 8.1",
     "befund": "Essen, Trinken oder Rauchen in Arbeitsbereichen mit Bleialkyl-Umgang.",
     "konsequenz": "Überprüfung des Hygieneregimes; Beratung zu Hygienemaßnahmen am "
                   "Arbeitsplatz (keine Nahrungsaufnahme/kein Rauchen im Arbeitsbereich, "
                   "Händewaschen); dem Unternehmen organisatorische Maßnahmen vorschlagen."},
    {"wenn": {"kleidung_wechsel": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Arbeitskleidung wird nach der Arbeit nicht gewechselt bzw. keine gründliche "
               "Reinigung.",
     "konsequenz": "Beratung zum Hygieneregime: Wechsel der Arbeitskleidung, gründliche "
                   "Hautreinigung nach Arbeitsende, getrennte Aufbewahrung von Arbeits- und "
                   "Straßenkleidung; Verschleppung des hautresorptiven Stoffes vermeiden."},
    # ── Beschwerden/Intoxikationszeichen (Abschnitte 6.3, 7.1 und 7.4) ────
    {"wenn": {"beschwerden_zns": ["angsttraeume", "schlafstoerungen", "verstimmung",
                                  "gewichtsabnahme", "haendezittern", "uebelkeit",
                                  "kopf_schwindel", "kreislauf"]},
     "schwere": "pruefen",
     "bereich": "Intoxikationsverdacht",
     "quelle": "Abschnitte 6.3.2/6.3.3, 7.1 (Beschwerden) und 7.4.2",
     "befund": "Stoffspezifische Beschwerden angegeben (z. B. Angstträume, Schlafstörungen, "
               "Verstimmung, Gewichtsabnahme, Händezittern, Übelkeit, Kopfschmerz/Schwindel, "
               "Kreislaufstörungen).",
     "konsequenz": "Verdacht auf Bleialkyl-Wirkung abklären: Biomonitoring (Blei im Vollblut, "
                   "BLW 150 µg/l; ggf. Bleiausscheidung im Urin), klinische Untersuchung nach "
                   "7.2.2. Bei eindeutigen Anzeichen einer Intoxikation oder dringlichem "
                   "Verdacht bzw. Gesamtbleiausscheidung im Harn > 50 µg/l Maßnahmen nach "
                   "7.4.2 bis zum Abklingen der Symptome (Expositionsbegrenzung, "
                   "Einsatz an Arbeitsplätzen mit geringerer Exposition)."},
    {"wenn": {"beschwerden_zns": ["verwirrtheit"]},
     "schwere": "kritisch",
     "bereich": "Intoxikationsverdacht",
     "quelle": "Abschnitte 6.3.2, 7.4.2 und 7.4.4",
     "befund": "Verwirrtheit, Halluzinationen oder Angstzustände angegeben – mögliche "
               "eindeutige Anzeichen einer Bleialkyl-Intoxikation.",
     "konsequenz": "Unverzügliche ärztliche Abklärung vor Fortsetzung der Tätigkeit: "
                   "Biomonitoring (Blut-/Urinblei) zur Differentialdiagnose (entscheidend ist "
                   "allein der Bleigehalt in Blut bzw. Urin), neurologisch-psychiatrische "
                   "Vorstellung. Bis zum Abklingen Maßnahmen nach 7.4.2; bei Fortbestehen "
                   "eindeutiger Intoxikationszeichen Tätigkeitswechsel erwägen (7.4.4, "
                   "Mitteilung nur mit Einwilligung der versicherten Person)."},
    {"wenn": {"wesensveraenderung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Intoxikationsverdacht",
     "quelle": "Abschnitte 7.1 (Beschwerden) und 6.3.3",
     "befund": "Fremdanamnestisch bemerkte Persönlichkeits- bzw. Verhaltensänderung "
               "angegeben.",
     "konsequenz": "Entwicklung einer Persönlichkeits-/Verhaltensstörung als mögliches "
                   "Intoxikationszeichen ärztlich vertiefen; Biomonitoring und klinische "
                   "Untersuchung veranlassen; Differentialdiagnosen (u. a. Alkohol-/ "
                   "Drogenabusus, psychiatrische Erkrankung) über Blut-/Urinblei abgrenzen."},
    # ── Vorerkrankungen (Abschnitt 7.4) ───────────────────────────────────
    {"wenn": {"vorerkrankungen_liste": ["blut", "herz_kreislauf", "atemwege", "nase_rachen",
                                        "leber", "niere", "stoffwechsel", "haut"]},
     "schwere": "pruefen",
     "bereich": "Vorerkrankungen",
     "quelle": "Abschnitte 7.4 bis 7.4.3",
     "befund": "Beurteilungsrelevante Vorerkrankung angegeben (Blut, Herz-Kreislauf, Lunge, "
               "Nasen-/Rachenraum, Leber, Niere, Stoffwechsel oder Haut).",
     "konsequenz": "Individuelles Ausmaß der Erkrankung klären; prüfen, ob die Tätigkeit ohne "
                   "gesundheitliche Gefährdung möglich ist. Bei weniger ausgeprägten "
                   "Erkrankungen Maßnahmen nach 7.4.2 empfehlen (Substitution, technische/ "
                   "organisatorische Schutzmaßnahmen, Expositionsbegrenzung, PSA); bei zu "
                   "erwartender Änderung des Schweregrads verkürzte Vorsorgefristen nach "
                   "7.4.3."},
    {"wenn": {"vorerkrankungen_liste": ["nervensystem", "psychisch"]},
     "schwere": "pruefen",
     "bereich": "Zielorgan Nervensystem",
     "quelle": "Abschnitte 6.3, 7.4 und 7.4.4",
     "befund": "Erkrankung des Nervensystems oder psychische Erkrankung angegeben – "
               "Bleialkyle wirken vor allem auf das Zentralnervensystem.",
     "konsequenz": "Sorgfältige Beurteilung, ob die Tätigkeit ohne gesundheitliche Gefährdung "
                   "möglich ist; ggf. fachärztliche (neurologisch-psychiatrische) Befunde "
                   "einholen. Verkürzte Vorsorgefristen nach 7.4.3 erwägen; haben Maßnahmen "
                   "nach 7.4.2/7.4.3 keine Aussicht auf Erfolg, Tätigkeitswechsel erwägen "
                   "(7.4.4)."},
    {"wenn": {"sucht": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Abhängigkeitserkrankung",
     "quelle": "Abschnitte 6.3.3 und 7.4",
     "befund": "Alkohol-, Medikamenten- oder Drogenabhängigkeit angegeben.",
     "konsequenz": "Bei der Beurteilung nach 7.4 berücksichtigen; klären, ob die Tätigkeit "
                   "ohne gesundheitliche Gefährdung möglich ist. Erschwerte "
                   "Differentialdiagnose beachten (Intoxikationssymptome sind mit "
                   "Alkoholismus/Rauschmittelsucht verwechselbar – Blut-/Urinblei "
                   "entscheidend); ggf. Maßnahmen nach 7.4.2 oder verkürzte Fristen nach "
                   "7.4.3."},
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 6.5 und 7.1",
     "befund": "Anerkannte Berufskrankheit bzw. laufendes BK-Verfahren angegeben.",
     "konsequenz": "Unterlagen zum BK-Verfahren einbeziehen (BK-Nr. 1101 »Erkrankungen durch "
                   "Blei oder seine Verbindungen«); Erkenntnisse bei Beurteilung und Beratung "
                   "berücksichtigen."},
    # ── Mutterschutz (Abschnitte 6 und 7.1) ───────────────────────────────
    {"wenn": {"schwangerschaft": ["schwanger", "stillt"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitte 6 (reproduktionstoxisch Kat. 1A) und 7.1 (Beratung)",
     "befund": "Schwangerschaft bzw. Stillzeit angegeben bei Tätigkeit mit reproduktions-"
               "toxischen Stoffen (Kat. 1A).",
     "konsequenz": "Beschäftigungsbeschränkungen nach dem Mutterschutzgesetz vor weiterer "
                   "Tätigkeit mit Bleitetraethyl/Bleitetramethyl klären; unverzügliche "
                   "Information und Beratung, Anpassung der Gefährdungsbeurteilung durch das "
                   "Unternehmen anstoßen (Umsetzung auf expositionsfreien Arbeitsplatz)."},
    # ── Kombinationswirkung Lärm (Abschnitt 6.1.1) ────────────────────────
    {"wenn": {"laerm_bereich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Kombinationswirkung Lärm",
     "quelle": "Abschnitt 6.1.1",
     "befund": "Tätigkeit mit höherer Bleialkyl-Exposition in Lärmbereichen angegeben.",
     "konsequenz": "Wegen der ototoxischen Eigenschaft von Blei mögliche Kombinationswirkung "
                   "mit Lärm bei der Gehöruntersuchung nach der DGUV Empfehlung »Lärm« "
                   "berücksichtigen; Koordination beider Vorsorgeanlässe."},
]
