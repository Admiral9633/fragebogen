# -*- coding: utf-8 -*-
"""Staubbelastung – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Staubbelastung« (E STB, Fassung Januar 2022), S. 612–633."""

SLUG = "staubbelastung-2024"

CATALOG = {
    "version": 2,
    "title": "Staubbelastung (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Staubbelastung« (E STB, Fassung Januar 2022), S. 612–633",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen Staubbelastung?",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Ja, erste Staub-Vorsorge"},
                        {"value": "weitere", "label": "Nein, ich war schon einmal zur Staub-Vorsorge"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn der Allgemeine "
                            "Staubgrenzwert (A-Staub bzw. E-Staub nach TRGS 900) nicht eingehalten "
                            "wird. Angebotsvorsorge: wenn eine Staubbelastung nicht ausgeschlossen "
                            "werden kann.",
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
        # ── 2 ─ Tätigkeit und Staubbelastung ───────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Staubbelastung",
            "subtitle": "Ihre Arbeit und der Staub, dem Sie ausgesetzt sind",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "staub_taetigkeiten",
                    "type": "multi_choice",
                    "label": "Welche staubintensiven Arbeiten kommen bei Ihnen vor?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "bohren_schleifen", "label": "Bohren, Schleifen, Trennen oder Fräsen "
                                                              "im Trockenverfahren (z. B. Stein, Beton, Putz)"},
                        {"value": "freistrahl", "label": "Freistrahlarbeiten (Sandstrahlen und Ähnliches)"},
                        {"value": "schuettgueter", "label": "Arbeiten mit Pulvern oder Schüttgütern "
                                                            "(z. B. Verwiegen, Absacken, Abfüllen, Mahlen, Mischen)"},
                        {"value": "abbruch", "label": "Abbruch- oder Stemmarbeiten, Abbruch von Dämmstoffen"},
                        {"value": "giesserei", "label": "Gießerei-, Stahlwerks- oder Ofenarbeiten "
                                                        "(z. B. Putzerei, Ausmauern von Tiegeln)"},
                        {"value": "holz_kunststoff", "label": "Holz- oder Kunststoffbearbeitung mit Staubentwicklung"},
                        {"value": "reinigung", "label": "Reinigungs- oder Instandhaltungsarbeiten in "
                                                        "staubigen Bereichen (z. B. Baureinigung)"},
                        {"value": "andere", "label": "Andere staubige Tätigkeit"},
                        {"value": "keine", "label": "Keine davon / kaum Staub"},
                    ],
                },
                {
                    "id": "spezialstaub",
                    "type": "multi_choice",
                    "label": "Kommen an Ihrem Arbeitsplatz besondere Staubarten vor?",
                    "hint": "Für diese Stäube gelten eigene DGUV Empfehlungen. Kreuzen Sie an, "
                            "was auf Sie zutrifft – Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "quarz", "label": "Quarzhaltiger Staub (silikogener Staub, z. B. "
                                                    "Sandstrahlen, Steinbearbeitung, Tunnelbau)"},
                        {"value": "asbest", "label": "Asbesthaltiger Staub (z. B. Sanierung alter Gebäude)"},
                        {"value": "fasern", "label": "Künstliche Mineralfasern / Hochtemperaturwollen "
                                                     "(z. B. Ofen- und Feuerungsbau, Dämmstoffe)"},
                        {"value": "schweissrauch", "label": "Schweißrauche (Schweißen und Trennen von Metallen)"},
                        {"value": "keine", "label": "Keine davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Seit wann arbeiten Sie insgesamt mit Staubbelastung?",
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
                    "id": "frueher_staub",
                    "type": "yes_no",
                    "label": "Waren Sie in früheren Berufen oder Tätigkeiten Staub oder anderen "
                             "atemwegsbelastenden Stoffen ausgesetzt?",
                    "required": True,
                    "followup": {"id": "frueher_staub_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, welche Stoffe, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "weitere_gefahrstoffe",
                    "type": "yes_no",
                    "label": "Gibt es an Ihrem Arbeitsplatz weitere Gefährdungen für die Atemwege, "
                             "z. B. reizende Gase, Dämpfe oder Chemikalien?",
                    "required": True,
                    "followup": {"id": "weitere_gefahrstoffe_desc", "type": "text",
                                 "label": "Welche?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen",
            "subtitle": "Technische Maßnahmen und persönliche Schutzausrüstung (PSA)",
            "questions": [
                {
                    "id": "technische_massnahmen",
                    "type": "choice",
                    "label": "Gibt es an Ihrem Arbeitsplatz technische Maßnahmen gegen Staub "
                             "(z. B. Absaugung, Wasserbedüsung, geschlossene Kabine, Lüftung)?",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja, durchgehend"},
                        {"value": "teilweise", "label": "Teilweise / nicht überall"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "nicht_relevant", "label": "Betrifft mich nicht / kaum Staub"},
                    ],
                },
                {
                    "id": "atemschutz_tragen",
                    "type": "choice",
                    "label": "Tragen Sie bei staubintensiven Arbeiten Atemschutz "
                             "(z. B. FFP-Maske, Atemschutzgerät)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "Nicht nötig / arbeite (noch) nicht im Staubbereich"},
                    ],
                },
                {
                    "id": "atemschutz_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie beim Tragen des Atemschutzes Probleme "
                             "(z. B. Atemnot, Druckstellen, Beschlagen der Brille, Hitzegefühl)?",
                    "required": True,
                    "show_if": {"id": "atemschutz_tragen", "in": ["immer", "meist", "selten"]},
                    "followup": {"id": "atemschutz_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
            ],
        },
        # ── 4 ─ Atembeschwerden ────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Atembeschwerden",
            "subtitle": "Husten, Auswurf und Atemnot",
            "questions": [
                {
                    "id": "husten",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Husten?",
                    "required": True,
                    "followup": {"id": "husten_desc", "type": "text",
                                 "label": "Seit wann, und wie oft?", "when": "yes"},
                },
                {
                    "id": "auswurf",
                    "type": "yes_no",
                    "label": "Haben Sie häufig Auswurf (Schleim beim Husten)?",
                    "required": True,
                },
                {
                    "id": "husten_auswurf_chronisch",
                    "type": "yes_no",
                    "label": "Bestehen Husten und Auswurf an den meisten Tagen über mindestens "
                             "3 Monate pro Jahr – und das in 2 aufeinander folgenden Jahren?",
                    "hint": "So ist eine chronische Bronchitis (dauerhafte Entzündung der "
                            "Bronchien) definiert.",
                    "required": True,
                    "show_if": {"id": "auswurf", "in": ["yes"]},
                },
                {
                    "id": "atemnot",
                    "type": "choice",
                    "label": "Haben Sie Atemnot (Luftnot, Kurzatmigkeit)?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "belastung", "label": "Ja, bei körperlicher Anstrengung "
                                                        "(z. B. Treppensteigen, schwere Arbeit)"},
                        {"value": "ruhe", "label": "Ja, auch in Ruhe"},
                    ],
                },
                {
                    "id": "beschwerden_arbeitsbezug",
                    "type": "yes_no",
                    "label": "Sind Ihre Atembeschwerden bei oder nach der Arbeit stärker und "
                             "bessern sie sich am Wochenende oder im Urlaub?",
                    "required": True,
                    "show_if": {"id": "atemnot", "not_in": ["nein"]},
                },
                {
                    "id": "verschlechterung",
                    "type": "yes_no",
                    "label": "Haben sich Ihre Atembeschwerden seit der letzten Staub-Vorsorge "
                             "verschlechtert, oder sind neue Beschwerden dazugekommen?",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "in": ["weitere"]},
                    "followup": {"id": "verschlechterung_desc", "type": "textarea",
                                 "label": "Was hat sich verändert?", "when": "yes"},
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen",
            "subtitle": "Erkrankungen von Lunge, Atemwegen und Herz",
            "questions": [
                {
                    "id": "asthma",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen jemals Asthma bronchiale festgestellt?",
                    "required": True,
                },
                {
                    "id": "copd",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine chronische (obstruktive) Bronchitis, COPD "
                             "oder ein Lungenemphysem (überblähte Lunge) festgestellt?",
                    "required": True,
                },
                {
                    "id": "hyperreagibilitaet",
                    "type": "yes_no",
                    "label": "Reagieren Ihre Atemwege seit mehr als 6 Monaten überempfindlich "
                             "(z. B. Hustenreiz oder Engegefühl schon bei Staub, kalter Luft, "
                             "Rauch oder Gerüchen)?",
                    "required": True,
                },
                {
                    "id": "lungenerkrankung_roentgen",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Staublunge (z. B. Silikose, Asbestose), eine "
                             "Lungenfibrose (Vernarbung der Lunge), eine Sarkoidose oder eine "
                             "Allergie-Lungenentzündung (exogen allergische Alveolitis, z. B. "
                             "»Farmerlunge«) festgestellt?",
                    "required": True,
                    "followup": {"id": "lungenerkrankung_roentgen_desc", "type": "text",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "systemerkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine Systemerkrankung, die die Lunge mitbetreffen kann "
                             "(z. B. Rheuma, Sklerodermie, andere Bindegewebs- oder "
                             "Autoimmunerkrankungen)?",
                    "required": True,
                    "followup": {"id": "systemerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "herzinsuffizienz",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Herzschwäche (Herzinsuffizienz) oder eine "
                             "andere Herz-Kreislauf-Erkrankung mit Auswirkung auf die Atmung "
                             "festgestellt?",
                    "required": True,
                    "followup": {"id": "herzinsuffizienz_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein (z. B. Asthma-Sprays, "
                             "Kortison, Herzmedikamente)?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "textarea",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Rauchen ────────────────────────────────────────────────────
        {
            "id": "rauchen",
            "title": "Rauchen",
            "subtitle": "Tabakkonsum – wichtig für die Beurteilung der Atemwege",
            "questions": [
                {
                    "id": "raucher_status",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "ehemals", "label": "Früher ja, jetzt nicht mehr (Ex-Raucher/in)"},
                        {"value": "regelmaessig", "label": "Ja, ich rauche regelmäßig"},
                    ],
                },
                {
                    "id": "rauch_details",
                    "type": "textarea",
                    "label": "Was rauchen bzw. rauchten Sie (Zigaretten, Zigarren, Pfeife), "
                             "wie viel pro Tag, und von wann bis wann?",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ehemals", "regelmaessig"]},
                },
                {
                    "id": "packungsjahre",
                    "type": "choice",
                    "label": "Wie viele »Packungsjahre« kommen bei Ihnen ungefähr zusammen?",
                    "hint": "Packungsjahre = Schachteln pro Tag × Raucherjahre. Beispiel: "
                            "1 Schachtel täglich über 10 Jahre = 10 Packungsjahre.",
                    "required": True,
                    "show_if": {"id": "raucher_status", "in": ["ehemals", "regelmaessig"]},
                    "options": [
                        {"value": "unter10", "label": "Weniger als 10"},
                        {"value": "10bis20", "label": "10 bis 20"},
                        {"value": "ueber20", "label": "Mehr als 20"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
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
    # ── Anwendungsbereich: besondere Staubarten (Abschnitt 2) ─────────────
    {"wenn": {"spezialstaub": ["quarz"]},
     "schwere": "pruefen",
     "bereich": "Anwendungsbereich",
     "quelle": "Abschnitt 2 (Anwendungsbereich)",
     "befund": "Exposition gegenüber quarzhaltigem (silikogenem) Staub angegeben.",
     "konsequenz": "DGUV Empfehlung »Silikogener Staub« anwenden; Vorsorgeumfang danach "
                   "ausrichten (u. a. radiologische Diagnostik nach deren Anhang). Abgleich "
                   "mit der Gefährdungsbeurteilung des Betriebs."},
    {"wenn": {"spezialstaub": ["asbest"]},
     "schwere": "pruefen",
     "bereich": "Anwendungsbereich",
     "quelle": "Abschnitt 2 (Anwendungsbereich)",
     "befund": "Exposition gegenüber asbestfaserhaltigem Staub angegeben.",
     "konsequenz": "DGUV Empfehlung »Asbest« anwenden (krebserzeugender Gefahrstoff; dort "
                   "auch Regelungen zur nachgehenden Vorsorge). Exposition mit der "
                   "Gefährdungsbeurteilung abgleichen und dem Unternehmen ggf. Maßnahmen "
                   "nach § 6 (4) ArbMedVV vorschlagen."},
    {"wenn": {"spezialstaub": ["fasern"]},
     "schwere": "pruefen",
     "bereich": "Anwendungsbereich",
     "quelle": "Abschnitt 2 (Anwendungsbereich)",
     "befund": "Exposition gegenüber Staub aus künstlich hergestellten anorganischen "
               "Fasern angegeben.",
     "konsequenz": "DGUV Empfehlung »Tätigkeiten mit Hochtemperaturwollen (Faserstäube "
                   "Kategorie 1A oder 1B)« anwenden; Faserart über die "
                   "Gefährdungsbeurteilung klären."},
    {"wenn": {"spezialstaub": ["schweissrauch"]},
     "schwere": "pruefen",
     "bereich": "Anwendungsbereich",
     "quelle": "Abschnitt 2 (Anwendungsbereich)",
     "befund": "Exposition gegenüber Schweißrauchen angegeben.",
     "konsequenz": "Zusätzlich die DGUV Empfehlung »Schweißen und Trennen von Metallen« "
                   "anwenden und den Vorsorgeumfang entsprechend erweitern."},
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"asthma": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Asthma bronchiale in der Vorgeschichte angegeben.",
     "konsequenz": "Manifeste obstruktive Atemwegserkrankung nach 7.4 abklären: Spirometrie "
                   "sorgfältig bewerten, ggf. erweiterte Lungenfunktionsdiagnostik "
                   "(Bronchodilatationstest, Ganzkörperplethysmographie). Prüfen, ob die "
                   "Tätigkeit ohne gesundheitliche Gefährdung möglich ist; sonst Maßnahmen "
                   "nach 7.4.2 (technische/organisatorische/persönliche Schutzmaßnahmen), "
                   "verkürzte Fristen nach 7.4.3 oder Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"copd": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Chronische (obstruktive) Bronchitis, COPD oder Lungenemphysem angegeben.",
     "konsequenz": "Funktionelle Auswirkung objektivieren (Spirometrie, ggf. erweiterte "
                   "Lungenfunktionsdiagnostik nach 7.2.2). Bei wesentlicher funktioneller "
                   "Auswirkung Maßnahmen nach 7.4.2, verkürzte Fristen nach 7.4.3 bzw. "
                   "Tätigkeitswechsel nach 7.4.4 erwägen; Beratung, dass eine gezielte "
                   "Behandlung möglich ist."},
    {"wenn": {"hyperreagibilitaet": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwegserkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Anhaltend überempfindliche Atemwege (länger als 6 Monate) angegeben.",
     "konsequenz": "Symptomatische, irreversible bronchiale Hyperreagibilität abklären: "
                   "Bestimmung der bronchialen Hyperreaktivität (7.2.2). Bei Bestätigung "
                   "Beurteilung nach 7.4 mit Maßnahmen nach 7.4.2–7.4.4."},
    {"wenn": {"lungenerkrankung_roentgen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lungenerkrankung",
     "quelle": "Abschnitte 7.2.2 und 7.4",
     "befund": "Staublungen-, fibrosierende oder granulomatöse Lungenerkrankung bzw. "
               "exogen allergische Alveolitis in der Vorgeschichte angegeben.",
     "konsequenz": "Vorbefunde und eventuell vorhandene Voraufnahmen heranziehen; bei "
                   "klinischem Verdacht auf eine Lungenerkrankung im Sinne von 7.4 besteht "
                   "die Indikation für eine Röntgenuntersuchung des Thorax (7.2.2). "
                   "Beurteilung nach 7.4 (Streuungskriterien bzw. ICOERD); Maßnahmen nach "
                   "7.4.2–7.4.4 prüfen."},
    {"wenn": {"systemerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Lungenerkrankung",
     "quelle": "Abschnitte 7.1 und 7.4",
     "befund": "Systemerkrankung mit möglicher Lungenbeteiligung angegeben.",
     "konsequenz": "Lungenbeteiligung ärztlich abklären (Anamnese vertiefen, Spirometrie, "
                   "ggf. erweiterte Lungenfunktionsdiagnostik, Facharztbefunde einholen); "
                   "Ergebnis in die Beurteilung nach 7.4 einbeziehen."},
    {"wenn": {"herzinsuffizienz": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Herz-Kreislauf",
     "quelle": "Abschnitte 7.2.1 und 7.4",
     "befund": "Herzinsuffizienz bzw. kardiopulmonale Erkrankung angegeben.",
     "konsequenz": "Kardiopulmonale Situation abklären (körperliche Untersuchung der "
                   "Atmungs- und Kreislauforgane, Vorbefunde). Bei bestehender "
                   "Herzinsuffizienz oder Erkrankungen, bei denen stärkere Staubbelastung "
                   "ein zusätzliches Risiko bedeutet (z. B. Stauungsbronchitis), Maßnahmen "
                   "nach 7.4.2–7.4.4 erwägen."},
    # ── Beschwerden (Abschnitte 6.3, 7.1, 7.2.2) ──────────────────────────
    {"wenn": {"husten_auswurf_chronisch": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 6.3 und 7.2.2",
     "befund": "Husten und Auswurf an den meisten Tagen über mindestens je 3 Monate in "
               "2 aufeinander folgenden Jahren (WHO-Definition der chronischen Bronchitis).",
     "konsequenz": "Verdacht auf chronische Bronchitis: Spirometrie bewerten, in "
                   "Abhängigkeit von Anamnese und Befunden erweiterte "
                   "Lungenfunktionsdiagnostik (7.2.2); Beurteilung nach 7.4 und Beratung "
                   "zum Zusammenhang zwischen exogenen Faktoren und chronischen "
                   "Atemwegserkrankungen (8.1)."},
    {"wenn": {"atemnot": ["belastung", "ruhe"]},
     "schwere": "pruefen",
     "bereich": "Beschwerden",
     "quelle": "Abschnitte 6.3 und 7.2.2",
     "befund": "Atemnot bei Belastung bzw. in Ruhe angegeben.",
     "konsequenz": "Obstruktive Ventilationsstörung abklären: Spirometrie, ggf. erweiterte "
                   "Lungenfunktionsdiagnostik (Bronchodilatationstest, "
                   "Ganzkörperplethysmographie, bronchiale Hyperreaktivität). Bei klinischem "
                   "Verdacht auf eine Lungenerkrankung im Sinne von 7.4 Röntgen-Thorax "
                   "indiziert (7.2.2)."},
    {"wenn": {"beschwerden_arbeitsbezug": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Arbeitsbezug",
     "quelle": "Abschnitte 6.5, 7.1 und 8.2",
     "befund": "Atembeschwerden mit Bezug zur Tätigkeit (Besserung am Wochenende/im "
               "Urlaub) angegeben.",
     "konsequenz": "Tätigkeitsspezifische Symptomatik ärztlich vertiefen; Anhaltspunkte für "
                   "unzureichende Schutzmaßnahmen dem Unternehmen mitteilen und Maßnahmen "
                   "vorschlagen (§ 6 (4) ArbMedVV, 8.2). Bei begründetem Verdacht auf eine "
                   "Berufskrankheit (BK-Nr. 4111 bzw. 4302) Meldung prüfen (6.5)."},
    {"wenn": {"verschlechterung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Verlauf",
     "quelle": "Abschnitte 7.1, 7.2.2 und 7.4.3",
     "befund": "Verschlechterung bzw. neue Atembeschwerden seit der letzten Vorsorge.",
     "konsequenz": "Aktualisierte Anamnese mit tätigkeitsspezifischen Symptomen vertiefen; "
                   "Spirometrie im Vergleich zur Voruntersuchung bewerten, ggf. erweiterte "
                   "Lungenfunktionsdiagnostik. Bei zu erwartender Änderung des "
                   "Schweregrads verkürzte Vorsorgefristen nach 7.4.3 empfehlen."},
    # ── Schutzmaßnahmen (Abschnitte 7.1, 8.1, 8.2) ────────────────────────
    {"wenn": {"atemschutz_tragen": ["selten", "nie"]},
     "wenn_nicht": {"staub_taetigkeiten": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 7.1, 8.1 und 8.2",
     "befund": "Atemschutz wird bei staubintensiven Arbeiten selten oder nie getragen.",
     "konsequenz": "Beratung zum Tragen geeigneter PSA und zu staubarmem Arbeiten (8.1); "
                   "Ursachen klären. Ergeben sich Anhaltspunkte, dass die Maßnahmen des "
                   "Arbeitsschutzes nicht ausreichen, Mitteilung an das Unternehmen und "
                   "Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV, 8.2)."},
    {"wenn": {"technische_massnahmen": ["nein"]},
     "wenn_nicht": {"staub_taetigkeiten": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 6.1.1 und 8.2",
     "befund": "Keine technischen Staubschutzmaßnahmen (Absaugung, Bedüsung, Kabine) "
               "bei staubintensiver Tätigkeit angegeben.",
     "konsequenz": "Abgleich mit der Gefährdungsbeurteilung: Tätigkeiten ohne wirksame "
                   "Absaugung/Bedüsung zählen zu den Arbeitsverfahren mit höherer "
                   "Exposition (6.1.1). Dem Unternehmen technische bzw. organisatorische "
                   "Schutzmaßnahmen vorschlagen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"atemschutz_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Schutzmaßnahmen",
     "quelle": "Abschnitte 7.4.2 und 8.1",
     "befund": "Probleme beim Tragen des Atemschutzes angegeben.",
     "konsequenz": "Beratung zur Auswahl geeigneter PSA unter Beachtung des individuellen "
                   "Gesundheitszustandes (7.4.2); Trageprobleme dokumentieren und ggf. dem "
                   "Unternehmen alternative Schutzmaßnahmen vorschlagen."},
    # ── Rauchen (Abschnitte 6.3 und 8.1) ──────────────────────────────────
    {"wenn": {"raucher_status": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 6.3 und 8.1",
     "befund": "Regelmäßiger Tabakkonsum angegeben.",
     "konsequenz": "Beratung zum Zusammenhang zwischen exogenen Faktoren (Rauchen plus "
                   "Staubbelastung) und der Entwicklung chronischer Atemwegserkrankungen "
                   "(8.1); Tabakentwöhnung empfehlen; Packungsjahre dokumentieren (7.1)."},
]
