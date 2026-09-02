# -*- coding: utf-8 -*-
"""Arbeiten mit Absturzgefahr – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen
für arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
Kapitel »Arbeiten mit Absturzgefahr« (E ABS, Eignungsbeurteilung,
Fassung Januar 2022), S. 1050–1064."""

SLUG = "absturz-2024"

CATALOG = {
    "version": 2,
    "title": "Arbeiten mit Absturzgefahr (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Arbeiten mit Absturzgefahr« (E ABS, Eignungsbeurteilung, "
             "Fassung Januar 2022), S. 1050–1064",
    "sections": [
        # ── 1 ─ Anlass der Eignungsbeurteilung ─────────────────────────────
        {
            "id": "anlass",
            "title": "Anlass der Beurteilung",
            "subtitle": "Angaben zu Ihrem Termin",
            "questions": [
                {
                    "id": "beurteilung_art",
                    "type": "choice",
                    "label": "Ist dies Ihre erste Eignungsbeurteilung für Arbeiten mit Absturzgefahr?",
                    "hint": "Eine Eignungsbeurteilung prüft, ob Sie die Tätigkeit in der Höhe aus "
                            "gesundheitlicher Sicht sicher ausüben können. Das Ergebnis kann "
                            "Folgen für die Aufnahme oder Fortsetzung der Tätigkeit haben.",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Eignungsbeurteilung"},
                        {"value": "erneute", "label": "Nein, ich wurde schon einmal beurteilt"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit & Absturzgefährdung (Abschnitte 2, 6.1, 7.1) ─────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Absturzgefährdung",
            "subtitle": "Ihre Arbeit in der Höhe",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "einsatzbereiche",
                    "type": "multi_choice",
                    "label": "Wo bzw. wie arbeiten Sie mit Absturzgefahr?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "freileitungen", "label": "Frei- oder Fahrleitungen (z. B. Strommasten, Bahn)"},
                        {"value": "bruecken_tuerme", "label": "Brücken, Masten, Türme, Schornsteine oder Windenergieanlagen"},
                        {"value": "montage", "label": "Auf-/Abbau freitragender Konstruktionen (Stahlbau, Fertigteilbau)"},
                        {"value": "seiltechnik", "label": "Seilunterstützte Zugangs- und Positionierungstechnik "
                                                          "(z. B. Fassadenreinigung, Rigging, Baumarbeiten, Felssicherung)"},
                        {"value": "hoehenrettung", "label": "Höhenrettung (Rettung aus Höhen und Tiefen)"},
                        {"value": "bohrturm_geruest_schacht", "label": "Bohrtürme, Gerüste oder Schächte"},
                        {"value": "sonstiges", "label": "Andere Arbeiten in großer Höhe"},
                    ],
                },
                {
                    "id": "psa_absturz",
                    "type": "yes_no",
                    "label": "Benutzen Sie persönliche Schutzausrüstung (PSA) gegen Absturz, "
                             "z. B. Auffanggurt und Sicherungsseil?",
                    "required": True,
                },
                {
                    "id": "einsatzbedingungen",
                    "type": "yes_no",
                    "label": "Arbeiten Sie dabei unter besonderen Bedingungen, z. B. bei Wind und "
                             "Wetter im Freien, bei Kälte, Hitze oder Nässe?",
                    "required": True,
                    "followup": {"id": "einsatzbedingungen_desc", "type": "text",
                                 "label": "Welche Bedingungen sind das?", "when": "yes"},
                },
                {
                    "id": "koerperlich_schwer",
                    "type": "yes_no",
                    "label": "Ist Ihre Tätigkeit körperlich schwer (z. B. Tragen von Lasten, "
                             "Klettern über längere Zeit)?",
                    "required": True,
                },
            ],
        },
        # ── 3 ─ Seit der letzten Beurteilung (nur erneute; Abschnitt 7.1) ──
        {
            "id": "zwischenanamnese",
            "title": "Seit der letzten Beurteilung",
            "subtitle": "Veränderungen seit Ihrem letzten Termin",
            "questions": [
                {
                    "id": "zwischen_erkrankung",
                    "type": "yes_no",
                    "label": "Sind seit der letzten Beurteilung neue Erkrankungen aufgetreten "
                             "oder bestehende schlimmer geworden?",
                    "show_if": {"id": "beurteilung_art", "in": ["erneute"]},
                    "required": True,
                    "followup": {"id": "zwischen_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankungen?", "when": "yes"},
                },
                {
                    "id": "zwischen_unfall",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Beurteilung einen Unfall "
                             "(beruflich oder privat)?",
                    "show_if": {"id": "beurteilung_art", "in": ["erneute"]},
                    "required": True,
                    "followup": {"id": "zwischen_unfall_desc", "type": "text",
                                 "label": "Was ist passiert?", "when": "yes"},
                },
                {
                    "id": "zwischen_synkope",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Beurteilung Schwindel- oder "
                             "Ohnmachtsanfälle (Synkopen)?",
                    "show_if": {"id": "beurteilung_art", "in": ["erneute"]},
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Aktuelle Beschwerden (Abschnitte 7.1, 7.4) ─────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Wie es Ihnen zurzeit geht",
            "questions": [
                {
                    "id": "hoehenangst",
                    "type": "yes_no",
                    "label": "Haben Sie Angst vor der Höhe (Höhenangst) oder fühlen Sie sich "
                             "in der Höhe unsicher?",
                    "required": True,
                },
                {
                    "id": "panikattacken",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal Panikattacken (plötzliche starke Angst "
                             "mit Herzrasen, Atemnot oder Zittern)?",
                    "required": True,
                },
                {
                    "id": "schwindel",
                    "type": "yes_no",
                    "label": "Leiden Sie unter Schwindel (z. B. Drehgefühl, Schwanken, "
                             "Unsicherheit beim Gehen oder Stehen)?",
                    "required": True,
                    "followup": {"id": "schwindel_desc", "type": "text",
                                 "label": "Wie äußert sich der Schwindel, und wie oft tritt er auf?",
                                 "when": "yes"},
                },
                {
                    "id": "ohnmacht",
                    "type": "yes_no",
                    "label": "Hatten Sie schon einmal eine Ohnmacht oder plötzliche "
                             "Bewusstlosigkeit?",
                    "required": True,
                },
                {
                    "id": "sehstoerungen",
                    "type": "yes_no",
                    "label": "Haben Sie Sehstörungen, z. B. unscharfes Sehen, Doppelbilder oder "
                             "Ausfälle im Blickfeld (Gesichtsfeld)?",
                    "hint": "Gemeint sind Probleme, die auch mit Brille oder Kontaktlinsen bestehen.",
                    "required": True,
                    "followup": {"id": "sehstoerungen_desc", "type": "text",
                                 "label": "Welche Sehstörungen?", "when": "yes"},
                },
                {
                    "id": "hoerminderung",
                    "type": "yes_no",
                    "label": "Hören Sie schlecht oder haben Sie Ohrgeräusche (Tinnitus)?",
                    "required": True,
                },
                {
                    "id": "belastungs_atemnot",
                    "type": "yes_no",
                    "label": "Bekommen Sie bei körperlicher Anstrengung schnell Atemnot oder "
                             "Brustschmerzen?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen (Abschnitte 7.1, 7.4) ──────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Frühere & bestehende Erkrankungen",
            "subtitle": "Bitte auch länger zurückliegende Erkrankungen angeben",
            "questions": [
                {
                    "id": "psychische_erkrankung",
                    "type": "yes_no",
                    "label": "Sind bei Ihnen psychische Erkrankungen bekannt (z. B. Angststörung, "
                             "Depression, starke Stimmungsschwankungen)?",
                    "required": True,
                    "followup": {"id": "psychische_erkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung, und sind Sie in Behandlung?",
                                 "when": "yes"},
                },
                {
                    "id": "anfallsleiden",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen ein Anfallsleiden bekannt (z. B. Epilepsie, "
                             "Krampfanfälle)?",
                    "required": True,
                    "followup": {"id": "anfallsleiden_desc", "type": "text",
                                 "label": "Wann war der letzte Anfall, und werden Sie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "neuro_ereignis",
                    "type": "yes_no",
                    "label": "Hatten Sie eine schwere Kopfverletzung (Schädel-Hirn-Trauma), "
                             "einen Schlaganfall, eine Durchblutungsstörung des Gehirns oder "
                             "eine Lähmung?",
                    "required": True,
                },
                {
                    "id": "herz_kreislauf",
                    "type": "multi_choice",
                    "label": "Sind bei Ihnen Erkrankungen des Herzens oder des Kreislaufs bekannt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "rhythmus", "label": "Herzrhythmusstörungen (Herzstolpern, Herzrasen)"},
                        {"value": "insuffizienz", "label": "Herzschwäche (Herzinsuffizienz)"},
                        {"value": "infarkt", "label": "Herzinfarkt in der Vorgeschichte"},
                        {"value": "hypertonie", "label": "Bluthochdruck (arterielle Hypertonie)"},
                        {"value": "herzfehler_durchblutung", "label": "Herzfehler oder Durchblutungsstörungen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "atemwege",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der Atemwege oder der Lunge "
                             "(z. B. chronische Bronchitis, Asthma, Lungenemphysem)?",
                    "required": True,
                },
                {
                    "id": "diabetes",
                    "type": "choice",
                    "label": "Haben Sie Diabetes mellitus (Zuckerkrankheit)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "diaet", "label": "Ja, nur mit Ernährung/Bewegung behandelt"},
                        {"value": "tabletten", "label": "Ja, mit Tabletten behandelt"},
                        {"value": "insulin", "label": "Ja, mit Insulin behandelt"},
                    ],
                },
                {
                    "id": "hypoglykaemie",
                    "type": "yes_no",
                    "label": "Hatten Sie schon Unterzuckerungen (Hypoglykämien), z. B. mit Zittern, "
                             "Schwitzen, Verwirrtheit oder Bewusstlosigkeit?",
                    "show_if": {"id": "diabetes", "in": ["diaet", "tabletten", "insulin"]},
                    "required": True,
                },
                {
                    "id": "endokrin_nieren",
                    "type": "yes_no",
                    "label": "Haben Sie eine Erkrankung der Schilddrüse, der Nebennieren "
                             "oder der Nieren?",
                    "required": True,
                    "followup": {"id": "endokrin_nieren_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "ohrenerkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Ohrenerkrankung, die Schwindel auslösen kann "
                             "(z. B. Morbus Menière, Gleichgewichtsstörung des Innenohrs)?",
                    "required": True,
                },
                {
                    "id": "bewegungsapparat",
                    "type": "yes_no",
                    "label": "Haben Sie Erkrankungen oder Einschränkungen an Armen, Beinen, "
                             "Gelenken oder der Wirbelsäule, die Sie bei der Arbeit behindern?",
                    "required": True,
                    "followup": {"id": "bewegungsapparat_desc", "type": "text",
                                 "label": "Welche Einschränkungen?", "when": "yes"},
                },
                {
                    "id": "uebergewicht",
                    "type": "choice",
                    "label": "Haben Sie starkes Übergewicht (Body-Mass-Index 30 oder höher)?",
                    "hint": "Der BMI errechnet sich aus Gewicht und Größe. Beispiel: "
                            "bei 1,80 m entspricht BMI 30 etwa 97 kg.",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ja", "label": "Ja"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Besteht bei Ihnen aktuell eine Schwangerschaft?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ja", "label": "Ja"},
                        {"value": "entfaellt", "label": "Trifft auf mich nicht zu"},
                    ],
                },
            ],
        },
        # ── 6 ─ Medikamente & Suchtmittel (Abschnitt 7.1) ──────────────────
        {
            "id": "medikamente",
            "title": "Medikamente & Suchtmittel",
            "subtitle": "Was Sie regelmäßig einnehmen oder konsumieren",
            "questions": [
                {
                    "id": "medikamente_regelmaessig",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "textarea",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
                {
                    "id": "medikamente_sedierend",
                    "type": "multi_choice",
                    "label": "Sind darunter Medikamente aus einer dieser Gruppen?",
                    "hint": "Mehrfachauswahl möglich. Im Zweifel bitte den Beipackzettel prüfen "
                            "oder das Medikament beim Termin mitbringen.",
                    "show_if": {"id": "medikamente_regelmaessig", "in": ["yes"]},
                    "required": True,
                    "options": [
                        {"value": "sedativ", "label": "Beruhigende oder müde machende Mittel "
                                                      "(z. B. Schlafmittel, starke Schmerzmittel, Allergiemittel)"},
                        {"value": "psychopharmaka", "label": "Psychopharmaka (Mittel gegen Depressionen, Angst, Psychosen)"},
                        {"value": "herz_kreislauf_mittel", "label": "Herz-Kreislauf-Mittel (z. B. Blutdrucksenker)"},
                        {"value": "antivertiginosa", "label": "Mittel gegen Schwindel (Antivertiginosa)"},
                        {"value": "keine", "label": "Keines davon"},
                    ],
                },
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "gelegentlich", "label": "Gelegentlich (z. B. am Wochenende)"},
                        {"value": "regelmaessig", "label": "Mehrmals pro Woche"},
                        {"value": "taeglich", "label": "(Fast) täglich"},
                    ],
                },
                {
                    "id": "drogen",
                    "type": "yes_no",
                    "label": "Nehmen Sie Drogen (z. B. Cannabis, Amphetamine) oder haben Sie "
                             "früher regelmäßig Drogen genommen?",
                    "required": True,
                },
                {
                    "id": "abhaengigkeit",
                    "type": "yes_no",
                    "label": "Besteht oder bestand bei Ihnen eine Abhängigkeit von Alkohol, "
                             "Drogen oder Medikamenten?",
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

# Hinweis zur Regelauswahl: Audiometrie, Optometrie, Spirometrie, EKG, Ergometrie
# und Labor (Glucose, Kreatinin, Urinstatus u. a.) gehören nach Abschnitt 7.2.2
# ohnehin zum Standardprogramm jeder Eignungsuntersuchung. Regeln lösen daher nur
# dort aus, wo die Quelle DARÜBER HINAUS eine Konsequenz vorsieht (Eignungszweifel,
# fachärztliche Abklärung, verkürzte Fristen, besondere Beratung).
RULES = [
    # ── Psyche & Höhenangst (Abschnitt 7.4) ────────────────────────────────
    {"wenn": {"hoehenangst": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Höhenangst",
     "quelle": "Abschnitt 7.4 (Beurteilungskriterien)",
     "befund": "Höhenangst bzw. Unsicherheit in der Höhe angegeben.",
     "konsequenz": "Freiheit von Höhenangst ist Voraussetzung für die Tätigkeit; bei Höhenangst "
                   "(Akrophobie) ist eine Eignung i. d. R. nicht gegeben (7.4.4). Vor einer "
                   "Eignungsfeststellung fachärztliche/psychotherapeutische Abklärung veranlassen "
                   "und prüfen, ob Maßnahmen nach 7.4.2 (technische/organisatorische "
                   "Schutzmaßnahmen) oder eine Behandlung Aussicht auf Erfolg haben."},
    {"wenn": {"panikattacken": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Psychische Erkrankung",
     "quelle": "Abschnitte 7.1 und 7.4 (Angststörungen, Panikattacken)",
     "befund": "Panikattacken in der Vorgeschichte angegeben.",
     "konsequenz": "Panikattacken sind ein Beurteilungskriterium gegen die Tätigkeit mit "
                   "Absturzgefahr. Psychiatrische/psychotherapeutische Abklärung vor Einsatz; "
                   "Eignung nur, wenn Stabilität belegt ist, ggf. verkürzte Beurteilungsfrist "
                   "nach 7.4.3."},
    {"wenn": {"psychische_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Psychische Erkrankung",
     "quelle": "Abschnitt 7.4 (psychische Erkrankungen)",
     "befund": "Psychische Erkrankung (z. B. Angststörung, ausgeprägte Stimmungsschwankungen) angegeben.",
     "konsequenz": "Psychische Stabilität ist Voraussetzung. Behandlungsstand erfragen, ggf. "
                   "fachärztliche Stellungnahme einholen; bei zu erwartender Änderung des "
                   "Schweregrads verkürzte Beurteilungsfrist nach 7.4.3 vorsehen."},
    # ── Bewusstlosigkeitsrisiko & Nervensystem (Abschnitt 7.4) ─────────────
    {"wenn": {"ohnmacht": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Synkopen/Bewusstlosigkeit",
     "quelle": "Abschnitt 7.4 (Risiko plötzlicher Bewusstlosigkeit)",
     "befund": "Ohnmacht bzw. plötzliche Bewusstlosigkeit in der Vorgeschichte.",
     "konsequenz": "Es sollten keine Erkrankungen vorliegen, die das Risiko plötzlicher "
                   "Bewusstlosigkeit erhöhen. Ursache vor Einsatz klären: EKG, ggf. Ergometrie "
                   "und kardiologische/neurologische Ergänzungsuntersuchung veranlassen; bis "
                   "zur Klärung Eignung nicht bestätigen."},
    {"wenn": {"zwischen_synkope": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Synkopen/Bewusstlosigkeit",
     "quelle": "Abschnitt 7.1 (anlassbezogene erneute Eignungsuntersuchung)",
     "befund": "Schwindel- oder Ohnmachtsanfälle (Synkopen) seit der letzten Beurteilung.",
     "konsequenz": "Anlassbezogene Abklärung vor weiterem Einsatz: aktualisierte Anamnese, "
                   "Gleichgewichtsprüfung (Romberg/Unterberger), EKG; bei Auffälligkeiten "
                   "weitere fachärztliche Abklärung. Bis zur Klärung Eignung nicht bestätigen."},
    {"wenn": {"anfallsleiden": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Nervensystem",
     "quelle": "Abschnitt 7.4 (Anfallsleiden; DGUV Information 250-001)",
     "befund": "Anfallsleiden (z. B. Epilepsie) angegeben.",
     "konsequenz": "Differenzierte Beurteilung nach DGUV Information 250-001 »Berufliche "
                   "Beurteilung bei Epilepsie und nach erstem epileptischen Anfall«: "
                   "neurologische Stellungnahme (Anfallsart, -häufigkeit, Behandlungsstand) "
                   "vor Einsatz einholen; bis dahin keine Eignungsfeststellung."},
    {"wenn": {"neuro_ereignis": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nervensystem",
     "quelle": "Abschnitte 7.1 und 7.4 (neurologische Erkrankungen)",
     "befund": "Schädel-Hirn-Trauma, Schlaganfall, zerebrale Durchblutungsstörung oder "
               "Lähmung in der Vorgeschichte.",
     "konsequenz": "Neurologische Ergänzungsuntersuchung veranlassen (Restsymptome, "
                   "Anfallsrisiko, Lähmungen mit funktioneller Auswirkung); bei Zustand nach "
                   "Schlaganfall Eignung besonders kritisch prüfen (7.4). Eignung erst nach "
                   "unauffälligem Befund."},
    # ── Schwindel, Gleichgewicht, Sinnesorgane (Abschnitte 7.2.2, 7.4) ─────
    {"wenn": {"schwindel": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Gleichgewicht/Schwindel",
     "quelle": "Abschnitte 7.2.2 und 7.4 (Schwindelanfälle)",
     "befund": "Schwindel angegeben.",
     "konsequenz": "Schwindelfreiheit ist Voraussetzung. Prüfung der Kopf-Körper-"
                   "Gleichgewichtsfunktion (Stehversuch nach Romberg, Tretversuch nach "
                   "Unterberger) durchführen; bei Auffälligkeiten fachärztliche (HNO-/"
                   "neurootologische) Abklärung vor Einsatz."},
    {"wenn": {"ohrenerkrankung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "HNO",
     "quelle": "Abschnitt 7.4 (Hals-Nasen-Ohren-Erkrankungen)",
     "befund": "Ohrenerkrankung mit möglicher Schwindelfolge (z. B. Morbus Menière) angegeben.",
     "konsequenz": "Erkrankungen, die zu Schwindel führen, sprechen gegen die Tätigkeit. "
                   "HNO-fachärztliche Abklärung vor Einsatz; Eignung nur bei stabil "
                   "anfallsfreiem Verlauf, ggf. verkürzte Frist nach 7.4.3."},
    {"wenn": {"sehstoerungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 7.2.2 und 7.4 (Erkrankungen der Augen)",
     "befund": "Sehstörungen (Unschärfe, Doppelbilder oder Gesichtsfeldausfälle) angegeben.",
     "konsequenz": "Optometrie (Nähe, Ferne, Farbsehen, Perimetrie) durchführen. Bei beidäugig "
                   "korrigierter Sehleistung unter 0,7 (Fern und Nah) oder stark eingeschränktem "
                   "Gesichtsfeld augenärztliche Abklärung der Grunderkrankung (Einäugigkeit ist "
                   "keine absolute Kontraindikation – tätigkeitsbezogen bewerten); "
                   "Augenbewegungsstörungen mit Schwindel oder verschwommenen Bildern sprechen "
                   "gegen die Tätigkeit."},
    # ── Herz-Kreislauf, Belastbarkeit, Stoffwechsel (Abschnitt 7.4) ────────
    {"wenn": {"herz_kreislauf": ["rhythmus", "insuffizienz", "infarkt", "hypertonie",
                                 "herzfehler_durchblutung"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitt 7.4 (Herz-Kreislauf-Erkrankungen)",
     "befund": "Herz-Kreislauf-Erkrankung angegeben (Rhythmusstörung, Herzschwäche, Infarkt, "
               "Bluthochdruck, Herzfehler oder Durchblutungsstörung).",
     "konsequenz": "Leistungs- und Regulationsfähigkeit sowie Ohnmachts-/Schwindelrisiko prüfen: "
                   "Blutdruck, EKG und Ergometrie durchführen, ggf. kardiologische "
                   "Ergänzungsuntersuchung. Bei Zustand nach Herzinfarkt Eignung besonders "
                   "kritisch prüfen; ggf. verkürzte Frist nach 7.4.3."},
    {"wenn": {"belastungs_atemnot": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Kardiopulmonale Belastbarkeit",
     "quelle": "Abschnitt 7.4 (physische Belastbarkeit; Atemwege/Lungen)",
     "befund": "Atemnot oder Brustschmerz bei körperlicher Anstrengung angegeben.",
     "konsequenz": "Gute physische Belastbarkeit ist Voraussetzung. Spirometrie und Ergometrie "
                   "(Anhang 2 »Leitfaden Ergometrie«) durchführen; bei auffälligen Befunden "
                   "fachärztliche (kardiologische/pneumologische) Abklärung vor Einsatz."},
    {"wenn": {"diabetes": ["tabletten", "insulin"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechsel",
     "quelle": "Abschnitt 7.4 (Stoffwechselkrankheiten)",
     "befund": "Medikamentös behandelter Diabetes mellitus angegeben.",
     "konsequenz": "Bei schlecht eingestelltem, neu aufgetretenem oder zur Hypoglykämie "
                   "neigendem Diabetes (insbesondere insulinpflichtig) Stellungnahme des "
                   "behandelnden Diabetologen bzw. der Diabetologin einholen; "
                   "Glukose kontrollieren, verkürzte Frist nach 7.4.3 erwägen."},
    {"wenn": {"hypoglykaemie": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Stoffwechsel",
     "quelle": "Abschnitt 7.4 (Stoffwechselkrankheiten mit Bewusstlosigkeitsrisiko)",
     "befund": "Unterzuckerungen (Hypoglykämien) in der Vorgeschichte.",
     "konsequenz": "Stoffwechselkrankheiten, die zu plötzlicher Bewusstlosigkeit führen können, "
                   "sprechen gegen die Tätigkeit. Vor Einsatz diabetologische Stellungnahme und "
                   "stabile Stoffwechseleinstellung fordern; bis dahin Eignung nicht bestätigen."},
    {"wenn": {"uebergewicht": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Belastbarkeit/Übergewicht",
     "quelle": "Abschnitte 7.2.2 und 7.4 (Übergewicht BMI ≥ 30)",
     "befund": "Starkes Übergewicht (BMI ≥ 30) angegeben.",
     "konsequenz": "Bei BMI ≥ 30 ist der ergometrische Nachweis einer angepassten "
                   "kardiopulmonalen Leistungsfähigkeit erforderlich (Ergometrie nach Anhang 2 "
                   "»Leitfaden Ergometrie«, auch bei jeder Nachuntersuchung); Beratung zu "
                   "Ernährung und sportlichem Training anbieten (8.1)."},
    # ── Bewegungsapparat (Abschnitt 7.4) ───────────────────────────────────
    {"wenn": {"bewegungsapparat": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bewegungsapparat",
     "quelle": "Abschnitt 7.4 (Erkrankungen des Bewegungsapparats)",
     "befund": "Einschränkung an Armen, Beinen, Gelenken oder Wirbelsäule angegeben.",
     "konsequenz": "Funktion gezielt bewerten (Ganzkörperstatus): Eine Eignung ist i. d. R. "
                   "nicht gegeben, wenn die sichere Handhabung der Ausrüstung (PSA, Seiltechnik) "
                   "nicht gewährleistet ist; ggf. orthopädische Ergänzungsuntersuchung."},
    # ── Suchtmittel & Medikamente (Abschnitte 7.1, 7.4, 8.1) ───────────────
    {"wenn": {"abhaengigkeit": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Suchtmittel",
     "quelle": "Abschnitt 7.4 (Drogen-, Medikamenten-, Alkoholabhängigkeit)",
     "befund": "Abhängigkeit von Alkohol, Drogen oder Medikamenten angegeben (aktuell oder früher).",
     "konsequenz": "Abhängigkeit spricht gegen die Eignung. Suchtmedizinische Abklärung; Eignung "
                   "allenfalls nach belegter stabiler Abstinenz und mit verkürzter "
                   "Beurteilungsfrist nach 7.4.3."},
    {"wenn": {"medikamente_sedierend": ["sedativ", "psychopharmaka", "herz_kreislauf_mittel",
                                        "antivertiginosa"]},
     "schwere": "pruefen",
     "bereich": "Medikamente",
     "quelle": "Abschnitte 7.1 und 8.1 (Medikamente mit tätigkeitsrelevanter Wirkung)",
     "befund": "Einnahme von Medikamenten mit sedativer Nebenwirkung, Psychopharmaka, "
               "Herz-Kreislauf-Mitteln oder Antivertiginosa angegeben.",
     "konsequenz": "Wirkung der Medikamente im Hinblick auf die Absturzgefährdung prüfen und "
                   "die versicherte Person dazu beraten (8.1); ggf. Rücksprache mit den "
                   "Behandelnden zur Therapieumstellung, bis dahin Einsatz kritisch bewerten."},
    # ── Mutterschutz & abschließende Beratung (Abschnitte 6.4, 8.1) ────────
    {"wenn": {"schwangerschaft": ["ja"]},
     "schwere": "kritisch",
     "bereich": "Mutterschutz",
     "quelle": "Abschnitt 6.4 (besondere gesundheitliche Aspekte; § 11 Abs. 5 MuSchG)",
     "befund": "Bestehende Schwangerschaft angegeben.",
     "konsequenz": "Im Rahmen der Gefährdungsbeurteilung prüfen, ob unverantwortbare "
                   "Gefährdungen nach § 11 Abs. 5 Mutterschutzgesetz vorliegen; Arbeitgeber "
                   "über erforderliche Schutzmaßnahmen bzw. ein Tätigkeitsverbot in der Höhe "
                   "informieren, bevor die Tätigkeit (fort-)geführt wird."},
    {"wenn": {"psa_absturz": ["yes"]},
     "schwere": "hinweis",
     "bereich": "PSA/Hängetrauma",
     "quelle": "Abschnitt 8.1 (abschließende Beratung; DGUV Information 204-011)",
     "befund": "Benutzung persönlicher Schutzausrüstung gegen Absturz angegeben.",
     "konsequenz": "Beratung zum Hängetrauma durchführen: Zeitfenster zur Rettung und "
                   "Erstbehandlung nach DGUV Information 204-011 erläutern; auf Einhaltung der "
                   "Sicherheitsvorschriften und funktionierende Rettungskette hinweisen. "
                   "Zudem darauf hinweisen, bei Beschwerden oder zwischenzeitlichen "
                   "Erkrankungen Vorgesetzte zu informieren und ärztlichen Rat einzuholen."},
]
