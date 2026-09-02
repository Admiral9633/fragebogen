# -*- coding: utf-8 -*-
"""Fluor und anorganische Fluorverbindungen – DGUV Empfehlung 2024.
Quelle: DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen,
1. Auflage 2024, Kapitel »Fluor und anorganische Fluorverbindungen« (E FLU,
Fassung Januar 2022, Grenzwerte aktualisiert 2024), S. 243–266."""

SLUG = "fluor-2024"

CATALOG = {
    "version": 2,
    "title": "Fluor und anorganische Fluorverbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Fluor und anorganische Fluorverbindungen« (E FLU, "
             "Fassung Januar 2022, Grenzwerte aktualisiert 2024), S. 243–266",
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
                    "label": "Ist dies Ihre erste arbeitsmedizinische Vorsorge wegen Fluor "
                             "bzw. Fluorverbindungen?",
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
                            "Arbeitsplatzgrenzwert nicht eingehalten wird oder eine "
                            "Gesundheitsgefährdung durch Hautkontakt (z. B. mit Flusssäure) "
                            "nicht ausgeschlossen werden kann. Angebotsvorsorge: wenn eine "
                            "Belastung nicht ausgeschlossen werden kann.",
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
        # ── 2 ─ Tätigkeit und Belastung ────────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Belastung",
            "subtitle": "Ihre Arbeit mit Fluor und Fluorverbindungen",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "stoffe",
                    "type": "multi_choice",
                    "label": "Mit welchen dieser Stoffe haben Sie bei der Arbeit zu tun?",
                    "hint": "Mehrfachauswahl möglich. Die Angaben stehen meist im "
                            "Sicherheitsdatenblatt oder in der Betriebsanweisung.",
                    "required": True,
                    "options": [
                        {"value": "fluor_gas", "label": "Fluor (blassgelbes, stechend riechendes Gas)"},
                        {"value": "hf_flusssaeure", "label": "Fluorwasserstoff oder Flusssäure (HF)"},
                        {"value": "feste_fluoride", "label": "Feste Fluoride / Fluoridsalze (z. B. Natriumfluorid, Kryolith, Hydrogenfluoride)"},
                        {"value": "bortrifluorid", "label": "Bortrifluorid oder andere fluorhaltige Gase"},
                        {"value": "sulfuryldifluorid", "label": "Sulfuryldifluorid (Begasungsmittel gegen Schädlinge)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "arbeitsverfahren",
                    "type": "multi_choice",
                    "label": "Welche dieser Arbeiten führen Sie durch?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "herstellen_abfuellen", "label": "Herstellen, Um- oder Abfüllen von Fluor, Fluorwasserstoff, Flusssäure oder Fluoriden"},
                        {"value": "glas_keramik", "label": "Ätzen, Polieren oder Mattieren von Glas oder Keramik (z. B. mit Flusssäure)"},
                        {"value": "aluminium_elektrolyse", "label": "Schmelzflusselektrolyse / Aluminiumherstellung"},
                        {"value": "metall_oberflaeche", "label": "Oberflächenbehandlung von Metallen (Beizen, Polieren, Galvanisieren, Edelstahl reinigen)"},
                        {"value": "schweissen", "label": "Schweißen mit basischen Elektroden oder Fülldrähten (über 6 % Fluoride)"},
                        {"value": "reiniger", "label": "Arbeiten mit flusssäurehaltigen Reinigern (z. B. Felgen-, Fassaden-, Keramikreiniger)"},
                        {"value": "holzschutz", "label": "Herstellen oder Anwenden fluoridhaltiger Holzschutzmittel"},
                        {"value": "begasung", "label": "Begasung mit Sulfuryldifluorid (Schädlingsbekämpfung)"},
                        {"value": "kunststoff_hitze", "label": "Erhitzen fluorhaltiger Kunststoffe über ca. 400 °C (z. B. PTFE/Teflon)"},
                        {"value": "labor", "label": "Laborarbeiten mit Flusssäure oder Fluoriden"},
                        {"value": "sonstige", "label": "Andere Arbeiten mit Fluorverbindungen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit Fluor oder Fluorverbindungen?",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Bisher gar nicht / Tätigkeit beginnt erst"},
                        {"value": "unter1", "label": "Weniger als 1 Jahr"},
                        {"value": "1bis10", "label": "1 bis 10 Jahre"},
                        {"value": "ueber10", "label": "Mehr als 10 Jahre"},
                    ],
                },
                {
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kann es bei Ihrer Arbeit zu direktem Hautkontakt mit Flusssäure "
                             "oder flusssäurehaltigen Lösungen kommen (z. B. Spritzer)?",
                    "hint": "Flusssäure dringt durch die Haut und kann auch in verdünnter "
                            "Form tiefe Gewebeschäden und lebensbedrohliche Vergiftungen "
                            "verursachen.",
                    "required": True,
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Unfälle oder Zwischenfälle mit "
                             "Fluorverbindungen (z. B. Hautspritzer, Verätzung, Einatmen von "
                             "Dämpfen, ungewöhnliche Betriebszustände)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "frueher_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Berufen oder Tätigkeiten Kontakt mit "
                             "Fluor, Flusssäure oder Fluoriden?",
                    "required": True,
                    "followup": {"id": "frueher_expo_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten, und wie lange?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Persönliche Schutzausrüstung und Verhalten am Arbeitsplatz",
            "questions": [
                {
                    "id": "psa_tragen",
                    "type": "multi_choice",
                    "label": "Welche persönliche Schutzausrüstung (PSA) benutzen Sie beim "
                             "Umgang mit diesen Stoffen?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "atemschutz", "label": "Atemschutz (Maske, Filtergerät)"},
                        {"value": "handschuhe", "label": "Chemikalien-Schutzhandschuhe"},
                        {"value": "brille", "label": "Schutzbrille oder Gesichtsschutz"},
                        {"value": "kleidung", "label": "Schutzkleidung / Schürze"},
                        {"value": "keine", "label": "Keine Schutzausrüstung"},
                        {"value": "kein_umgang", "label": "Ich habe (noch) keinen direkten Umgang mit den Stoffen"},
                    ],
                },
                {
                    "id": "psa_probleme",
                    "type": "yes_no",
                    "label": "Haben Sie Probleme beim Tragen der Schutzausrüstung "
                             "(z. B. Atemnot unter der Maske, Hautreizung durch Handschuhe)?",
                    "required": True,
                    "followup": {"id": "psa_probleme_desc", "type": "text",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
                {
                    "id": "hygiene",
                    "type": "choice",
                    "label": "Können Sie die Hygieneregeln am Arbeitsplatz einhalten "
                             "(Hände waschen, Arbeitskleidung wechseln, nicht am Arbeitsplatz "
                             "essen/trinken/rauchen)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "teilweise", "label": "Nur teilweise"},
                        {"value": "nein", "label": "Nein / kaum möglich"},
                    ],
                },
                {
                    "id": "notfall_bekannt",
                    "type": "yes_no",
                    "label": "Wissen Sie, was bei Hautkontakt mit Flusssäure sofort zu tun ist "
                             "(z. B. Spülen und Calciumgluconat-Gel auftragen)?",
                    "required": True,
                    "show_if": {"id": "hautkontakt", "in": ["yes"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, die mit Fluorverbindungen zusammenhängen können",
            "questions": [
                {
                    "id": "atemwege",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere dieser Atemwegs-Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "husten", "label": "Häufiger Husten"},
                        {"value": "auswurf", "label": "Vermehrter Auswurf (Schleim beim Husten)"},
                        {"value": "atemnot", "label": "Kurzatmigkeit bei Belastung"},
                        {"value": "atemgeraeusche", "label": "Pfeifende oder rasselnde Atemgeräusche"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "reizung",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit Reizungen der Augen, der Nase oder des "
                             "Rachens (z. B. Tränenfluss, Nasenlaufen, Brennen, Hustenreiz)?",
                    "required": True,
                },
                {
                    "id": "magen_darm",
                    "type": "yes_no",
                    "label": "Haben Sie Magen-Darm-Beschwerden (z. B. Übelkeit, "
                             "Magenschmerzen, Verdauungsprobleme)?",
                    "required": True,
                },
                {
                    "id": "haut_symptome",
                    "type": "yes_no",
                    "label": "Haben Sie Hautveränderungen, die mit der Arbeit zusammenhängen "
                             "könnten (Rötung, Brennen, schlecht heilende oder schmerzende "
                             "Stellen – auch wenn Schmerzen erst Stunden später auftraten)?",
                    "required": True,
                    "followup": {"id": "haut_symptome_desc", "type": "text",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "skelett_beschwerden",
                    "type": "multi_choice",
                    "label": "Haben Sie eine oder mehrere dieser Beschwerden am "
                             "Bewegungsapparat?",
                    "hint": "Mehrfachauswahl möglich. Solche Beschwerden können auf eine "
                            "Fluorid-Einlagerung in den Knochen (Skelettfluorose) hinweisen.",
                    "required": True,
                    "options": [
                        {"value": "gelenkschmerzen", "label": "Rheuma-ähnliche Gelenk- oder Gliederschmerzen"},
                        {"value": "bleierne_schwere", "label": "»Bleierne Schwere« in Armen oder Beinen"},
                        {"value": "nacken", "label": "Schmerzen und Steifheit im Nacken"},
                        {"value": "ruecken", "label": "Rückenschmerzen, besonders bei Erschütterungen"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Medikamente",
            "subtitle": "Erkrankungen, die für die Beurteilung wichtig sind",
            "questions": [
                {
                    "id": "lunge",
                    "type": "multi_choice",
                    "label": "Sind bei Ihnen Erkrankungen der Atemwege oder der Lunge bekannt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "asthma", "label": "Asthma bronchiale"},
                        {"value": "copd", "label": "COPD oder chronische Bronchitis"},
                        {"value": "andere_lunge", "label": "Andere Lungenerkrankung (z. B. Lungenfibrose)"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "skelett_erkrankung",
                    "type": "multi_choice",
                    "label": "Sind bei Ihnen Erkrankungen der Knochen oder der Wirbelsäule "
                             "bekannt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "osteoporose", "label": "Osteoporose (Knochenschwund)"},
                        {"value": "knochen_tb", "label": "Knochentuberkulose (auch früher)"},
                        {"value": "bechterew", "label": "Morbus Bechterew (entzündliche Wirbelsäulenerkrankung)"},
                        {"value": "andere_skelett", "label": "Andere Knochen- oder Wirbelsäulenerkrankung"},
                        {"value": "keine", "label": "Keine davon"},
                    ],
                },
                {
                    "id": "bk_verfahren",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Berufskrankheit anerkannt, oder läuft "
                             "derzeit ein Berufskrankheiten-Verfahren?",
                    "required": True,
                    "followup": {"id": "bk_verfahren_desc", "type": "text",
                                 "label": "Welche Berufskrankheit bzw. welches Verfahren?",
                                 "when": "yes"},
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
                    "id": "gesundheit_sonst",
                    "type": "yes_no",
                    "label": "Haben Sie sonstige gesundheitliche Einschränkungen oder "
                             "Erkrankungen, die hier noch nicht genannt wurden?",
                    "required": True,
                    "followup": {"id": "gesundheit_sonst_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
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
    # ── Beurteilungsrelevante Vorerkrankungen (Abschnitt 7.4) ─────────────
    {"wenn": {"lunge": ["asthma", "copd", "andere_lunge"]},
     "schwere": "pruefen",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 7.4 und 7.4.2–7.4.4",
     "befund": "Atemwegs-/Lungenerkrankung (Asthma bzw. obstruktive/restriktive "
               "Funktionseinschränkung möglich) angegeben.",
     "konsequenz": "Spirometrie sorgfältig durchführen und bewerten; Ausmaß der "
                   "Funktionseinschränkung klären (ggf. fachärztliche Vorbefunde einholen). "
                   "Beurteilung nach 7.4: bei geringer Ausprägung Maßnahmen nach 7.4.2 prüfen "
                   "(Substitution, technische/organisatorische Schutzmaßnahmen, Begrenzung der "
                   "Expositionszeit, geeignete PSA); bei zu erwartender Änderung des "
                   "Schweregrads verkürzte Vorsorgefristen nach 7.4.3; bleiben Maßnahmen ohne "
                   "Erfolg, Tätigkeitswechsel nach 7.4.4 erwägen (Mitteilung an den Arbeitgeber "
                   "nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"skelett_erkrankung": ["osteoporose", "knochen_tb", "bechterew"]},
     "schwere": "pruefen",
     "bereich": "Skelettsystem",
     "quelle": "Abschnitte 7.4 und 7.4.2–7.4.4",
     "befund": "Beurteilungsrelevante Skeletterkrankung (Osteoporose, Knochentuberkulose "
               "oder Morbus Bechterew) angegeben.",
     "konsequenz": "Untersuchung des Muskel-Skelett-Systems (Beweglichkeit der Gelenke und "
                   "Wirbelsäule) nach 7.2.1; Vorbefunde einbeziehen. Prüfen, ob die Tätigkeit "
                   "ohne gesundheitliche Gefährdung möglich ist; ggf. Maßnahmen nach 7.4.2, "
                   "verkürzte Fristen nach 7.4.3 oder Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"skelett_erkrankung": ["andere_skelett"]},
     "schwere": "pruefen",
     "bereich": "Skelettsystem",
     "quelle": "Abschnitte 7.2.1 und 7.4",
     "befund": "Sonstige Knochen- oder Wirbelsäulenerkrankung angegeben.",
     "konsequenz": "Art und Ausmaß der Erkrankung ärztlich klären (Untersuchung des "
                   "Muskel-Skelett-Systems, ggf. Vorbefunde); Relevanz für die Beurteilung "
                   "nach 7.4 prüfen."},
    # ── Beschwerden → Ergänzungsdiagnostik in unklaren Fällen (7.2.2) ─────
    {"wenn": {"atemwege": ["husten", "auswurf", "atemnot", "atemgeraeusche"]},
     "schwere": "pruefen",
     "bereich": "Atemwegssymptome",
     "quelle": "Abschnitte 7.1 und 7.2.2",
     "befund": "Atemwegsbeschwerden (Husten, Auswurf, Belastungs-Kurzatmigkeit oder "
               "verschärfte Atemgeräusche) angegeben.",
     "konsequenz": "Spirometrie durchführen und bewerten; bei klinisch begründetem Verdacht "
                   "auf eine Atemwegs- oder Lungenerkrankung radiologische Untersuchung des "
                   "Thorax (rechtfertigende Indikation) veranlassen (7.2.2)."},
    {"wenn": {"skelett_beschwerden": ["gelenkschmerzen", "bleierne_schwere", "nacken", "ruecken"]},
     "schwere": "pruefen",
     "bereich": "Verdacht Skelettfluorose",
     "quelle": "Abschnitte 6.3.3, 7.1 und 7.2.2",
     "befund": "Beschwerden am Bewegungsapparat (rheumatische Beschwerden, bleierne Schwere, "
               "Nackensteifheit oder Rückenschmerzen bei Erschütterung) angegeben.",
     "konsequenz": "An eine Fluor-Osteosklerose (Skelettfluorose) denken: Beweglichkeit von "
                   "Gelenken und Wirbelsäule untersuchen, Fluoridausscheidung im Urin "
                   "(Biomonitoring, BGW/BAT 4 mg/l bei Expositions-/Schichtende) bewerten. "
                   "Bei klinisch begründetem Verdacht Röntgendiagnostik des Skelettsystems "
                   "(Übersicht Becken und LWS, dorsolumbaler Übergang seitlich, beide "
                   "Unterarme; rechtfertigende Indikation) nach 7.2.2 veranlassen."},
    {"wenn": {"reizung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Reizwirkung am Arbeitsplatz",
     "quelle": "Abschnitte 6.3.1, 7.1 und 8.2",
     "befund": "Reizungen von Augen, Nase oder Rachen bei der Arbeit angegeben.",
     "konsequenz": "Hinweis auf relevante inhalative Exposition: Angaben mit der "
                   "Gefährdungsbeurteilung abgleichen; ergeben sich Anhaltspunkte, dass "
                   "Schutzmaßnahmen nicht ausreichen, Mitteilung an das Unternehmen und "
                   "Vorschlag zusätzlicher Schutzmaßnahmen (§ 6 (4) ArbMedVV); Spirometrie "
                   "bewerten."},
    {"wenn": {"haut_symptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3.1, 6.3.2 und 8.1",
     "befund": "Arbeitsbezogene Hautveränderungen angegeben (Rötung, Brennen, verzögert "
               "schmerzende Stellen).",
     "konsequenz": "An Flusssäure-Verätzungen denken – Schmerzen können erst Stunden nach "
                   "Kontakt auftreten, ohne sichtbare Hautveränderung. Haut ärztlich "
                   "untersuchen, Expositionssituation klären; Beratung zu Hautschutz und "
                   "Verhalten bei Kontamination (Calciumgluconat, Flusssäurepass, "
                   "DGUV Information 213-071)."},
    {"wenn": {"magen_darm": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm",
     "quelle": "Abschnitte 6.3.2 und 7.1",
     "befund": "Gastrointestinale Beschwerden angegeben.",
     "konsequenz": "Gastrointestinale Beschwerden gehören zu den zu erfragenden Symptomen: "
                   "mögliche orale Fluoridaufnahme (Hygieneregime!) klären, Urinstatus und "
                   "Fluorid-Biomonitoring bewerten; bei unklarem Befund weitergehende "
                   "ärztliche Abklärung."},
    # ── Exposition, Zwischenfälle, Vorgeschichte ──────────────────────────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenfälle/Unfälle",
     "quelle": "Abschnitte 7.1 und 6.5",
     "befund": "Unfall oder Zwischenfall mit Fluorverbindungen bzw. ungewöhnliche "
               "Betriebszustände angegeben.",
     "konsequenz": "Hergang erfragen und dokumentieren (7.1); Folgen abklären (nach "
                   "inhalativer Belastung Spirometrie, ggf. Thorax-Röntgen bei klinischem "
                   "Verdacht; nach Hautkontakt Wundkontrolle). Fluorid-Biomonitoring im Urin "
                   "bewerten. Bei Verdacht auf eine Erkrankung durch Fluor oder seine "
                   "Verbindungen BK-Anzeige prüfen (BK-Nr. 1308)."},
    {"wenn": {"frueher_expo": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitt 7.1 (Arbeitsanamnese)",
     "befund": "Frühere Tätigkeiten mit Fluorid-Exposition angegeben.",
     "konsequenz": "Frühere Expositionen und Schutzmaßnahmen in der Arbeitsanamnese "
                   "dokumentieren und bei der Interpretation des Fluorid-Basiswerts im Urin "
                   "sowie bei der Beurteilung berücksichtigen."},
    {"wenn": {"expo_dauer": ["ueber10"]},
     "schwere": "hinweis",
     "bereich": "Langzeitexposition",
     "quelle": "Abschnitte 6.3.3 und 7.2.2",
     "befund": "Mehr als 10 Jahre Tätigkeit mit Fluor bzw. Fluorverbindungen angegeben.",
     "konsequenz": "Bei langjähriger Exposition gezielt auf Zeichen einer Skelettfluorose "
                   "achten (rheumatische Beschwerden, Bewegungseinschränkung, erhöhte "
                   "Fluoridausscheidung); Befunde aus Biomonitoring und Untersuchung des "
                   "Muskel-Skelett-Systems im Verlauf vergleichen."},
    # ── Schutzmaßnahmen und Beratung (Abschnitt 8) ────────────────────────
    {"wenn": {"psa_tragen": ["keine"]},
     "schwere": "pruefen",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 8.1 und 8.2",
     "befund": "Beim Umgang mit Fluorverbindungen wird keine Schutzausrüstung benutzt.",
     "konsequenz": "Intensive Beratung zum Tragen geeigneter PSA, insbesondere Atemschutz und "
                   "Hand-/Hautschutz (8.1); Abgleich mit der Gefährdungsbeurteilung. Ergeben "
                   "sich Anhaltspunkte, dass Schutzmaßnahmen nicht ausreichen, Mitteilung an "
                   "das Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV, "
                   "DGUV Information 213-071)."},
    {"wenn": {"psa_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Persönliche Schutzausrüstung",
     "quelle": "Abschnitte 7.4.2 und 8.1",
     "befund": "Probleme beim Tragen der Schutzausrüstung angegeben.",
     "konsequenz": "Individuelle PSA-Beratung unter Beachtung des Gesundheitszustands "
                   "(7.4.2): geeignete Auswahl von Atemschutz und Handschuhen, besondere "
                   "individuelle Aspekte aufzeigen; ggf. dem Unternehmen alternative "
                   "Schutzmaßnahmen vorschlagen."},
    {"wenn": {"hygiene": ["teilweise", "nein"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Hygieneregeln am Arbeitsplatz werden nicht oder nur teilweise eingehalten.",
     "konsequenz": "Beratung zu Hygienemaßnahmen: Vermeiden von Inhalation und Hautkontakt, "
                   "Hygiene am Arbeitsplatz, Wechsel der Arbeitskleidung (8.1); Ursachen "
                   "klären und ggf. organisatorische Verbesserungen beim Unternehmen anregen."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Flusssäure-Gefährdung",
     "quelle": "Abschnitte 6.2, 6.3 und 8.1",
     "befund": "Möglicher direkter Hautkontakt mit Flusssäure bzw. flusssäurehaltigen "
               "Lösungen angegeben.",
     "konsequenz": "Eingehende Beratung zur Toxizität der Flusssäure, insbesondere zur "
                   "lebensbedrohlichen Gefährdung bei Hautkontakt, und zum Verhalten bei "
                   "einer Kontamination (8.1); Hinweis auf Erste-Hilfe-Ausstattung "
                   "(Calciumgluconat) und Flusssäurepass gemäß DGUV Information 213-071."},
    {"wenn": {"notfall_bekannt": ["no"]},
     "schwere": "pruefen",
     "bereich": "Notfallwissen",
     "quelle": "Abschnitte 8.1 und 8.2 (DGUV Information 213-071)",
     "befund": "Verhalten bei Hautkontakt mit Flusssäure ist nicht bekannt.",
     "konsequenz": "Sofortmaßnahmen schulen (Spülen, Calciumgluconat-Gel, umgehende "
                   "ärztliche Behandlung, Flusssäurepass); dem Unternehmen die Planung von "
                   "Notfallmaßnahmen und Erste Hilfe nach DGUV Information 213-071 "
                   "empfehlen."},
    # ── Sonstige Angaben ──────────────────────────────────────────────────
    {"wenn": {"bk_verfahren": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Berufskrankheit",
     "quelle": "Abschnitte 7.1 und 6.5",
     "befund": "Anerkannte Berufskrankheit oder laufendes BK-Verfahren angegeben.",
     "konsequenz": "Berufskrankheit bzw. laufendes BK-Verfahren dokumentieren (7.1), "
                   "Vorbefunde einholen und bei der Beurteilung sowie der Festlegung von "
                   "Maßnahmen berücksichtigen."},
    {"wenn": {"medikamente": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Medikamente",
     "quelle": "Abschnitt 7.1 (Medikamentenanamnese)",
     "befund": "Regelmäßige Medikamenteneinnahme angegeben.",
     "konsequenz": "Medikamentenanamnese ärztlich vertiefen (7.1) und mögliche Wechsel- "
                   "wirkungen mit der Tätigkeit (z. B. Einfluss auf Knochenstoffwechsel, "
                   "Atemwege) berücksichtigen."},
]
