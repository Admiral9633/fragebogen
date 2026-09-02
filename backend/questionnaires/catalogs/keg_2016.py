# -*- coding: utf-8 -*-
"""G 40 Krebserzeugende und erbgutverändernde Gefahrstoffe – allgemein – DGUV Grundsatz 2016.
Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, Ausgabe 2016,
G 40 (Fassung Oktober 2014), S. 561–624 (Kernteil S. 561–571, Tabellen 1–6 im Anhang)."""

SLUG = "g40-keg-2016"

CATALOG = {
    "version": 2,
    "title": "G 40 Krebserzeugende und erbgutverändernde Gefahrstoffe – allgemein "
             "(DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, Ausgabe 2016, "
             "G 40 »Krebserzeugende und erbgutverändernde Gefahrstoffe – allgemein« "
             "(Fassung Oktober 2014), S. 561–624",
    "sections": [
        # ── 1 ─ Untersuchungsanlass ────────────────────────────────────────
        {
            "id": "anlass",
            "title": "Untersuchungsanlass",
            "subtitle": "Angaben zu Ihrem Untersuchungstermin",
            "questions": [
                {
                    "id": "untersuchung_art",
                    "type": "choice",
                    "label": "Um welche Untersuchung nach dem Grundsatz G 40 handelt es sich heute?",
                    "hint": "Die Erstuntersuchung findet vor Aufnahme der Tätigkeit statt; "
                            "Nachuntersuchungen folgen je nach Belastung nach 24 bis 60 Monaten.",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der Tätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich wurde schon einmal nach G 40 untersucht)"},
                        {"value": "nachgehend", "label": "Nachgehende Untersuchung (die Tätigkeit mit diesen "
                                                         "Stoffen ist bereits beendet)"},
                    ],
                },
            ],
        },
        # ── 2 ─ Tätigkeit und Exposition ───────────────────────────────────
        {
            "id": "taetigkeit",
            "title": "Tätigkeit & Umgang mit Gefahrstoffen",
            "subtitle": "Ihre Arbeit und die Stoffe, mit denen Sie zu tun haben",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus bzw. sollen Sie aufnehmen "
                             "(Beruf, Arbeitsbereich)?",
                    "required": True,
                },
                {
                    "id": "stoffe",
                    "type": "multi_choice",
                    "label": "Mit welchen krebserzeugenden oder erbgutverändernden Gefahrstoffen "
                             "haben Sie bei der Arbeit Kontakt oder Umgang?",
                    "hint": "Mehrfachauswahl möglich. Die Angaben stehen meist in Ihrer "
                            "Unterweisung oder im Sicherheitsdatenblatt.",
                    "required": True,
                    "options": [
                        {"value": "acrylnitril", "label": "Acrylnitril"},
                        {"value": "pak", "label": "Polycyclische aromatische Kohlenwasserstoffe "
                                                  "(PAK, z. B. Teer, Pech, Ruß)"},
                        {"value": "beryllium", "label": "Beryllium oder seine Verbindungen"},
                        {"value": "butadien", "label": "1,3-Butadien"},
                        {"value": "epichlorhydrin", "label": "Epichlorhydrin (1-Chlor-2,3-Epoxypropan)"},
                        {"value": "cobalt", "label": "Cobalt (Kobalt) oder seine Verbindungen"},
                        {"value": "dimethylsulfat", "label": "Dimethylsulfat"},
                        {"value": "hydrazin", "label": "Hydrazin"},
                        {"value": "zytostatika", "label": "Krebserzeugende Zytostatika "
                                                          "(z. B. in Apotheke, Klinik, Pflege)"},
                        {"value": "nitrosamine", "label": "Nitrosamine"},
                        {"value": "andere", "label": "Andere krebserzeugende Stoffe"},
                        {"value": "unbekannt", "label": "Weiß ich nicht genau"},
                    ],
                },
                {
                    "id": "stoffe_desc",
                    "type": "text",
                    "label": "Falls Sie »Andere krebserzeugende Stoffe« angekreuzt haben: "
                             "Welche Stoffe sind das?",
                    "required": False,
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Unfälle oder kurzzeitig hohe Belastungen mit "
                             "diesen Stoffen (z. B. Verschütten, Leckage, Einatmen von Dämpfen, "
                             "Hautkontakt)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
                {
                    "id": "psa",
                    "type": "choice",
                    "label": "Tragen Sie die vorgesehene persönliche Schutzausrüstung "
                             "(z. B. Schutzhandschuhe, Atemschutz, Schutzkleidung)?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "keine_vorgesehen", "label": "Für meine Arbeit ist keine vorgesehen"},
                    ],
                },
                {
                    "id": "fruehere_expo",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt mit krebserzeugenden "
                             "Gefahrstoffen (z. B. Asbest, Benzol, Teer, Holzstaub)?",
                    "required": True,
                    "followup": {"id": "fruehere_expo_desc", "type": "textarea",
                                 "label": "Welche Stoffe, welche Tätigkeiten, und wie lange?",
                                 "when": "yes"},
                },
                {
                    "id": "ausserberuflich",
                    "type": "yes_no",
                    "label": "Sind oder waren Sie außerhalb der Arbeit krebserzeugenden Stoffen "
                             "ausgesetzt (z. B. Hobby-Werkstatt, Umgang mit Altöl oder Teer)?",
                    "required": True,
                    "followup": {"id": "ausserberuflich_desc", "type": "text",
                                 "label": "Wodurch?", "when": "yes"},
                },
                {
                    "id": "strahlen",
                    "type": "yes_no",
                    "label": "Waren Sie früher einer erheblichen Belastung durch ionisierende "
                             "Strahlen ausgesetzt (z. B. Strahlentherapie, häufige Röntgen-"
                             "untersuchungen, beruflicher Strahlenkontakt)?",
                    "required": True,
                    "followup": {"id": "strahlen_desc", "type": "text",
                                 "label": "Wodurch, und wann?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Nur bei Nach-/nachgehenden Untersuchungen ──────────────────
        {
            "id": "zwischenanamnese",
            "title": "Seit der letzten Untersuchung",
            "subtitle": "Nur bei Nach- und nachgehenden Untersuchungen",
            "questions": [
                {
                    "id": "schwere_erkrankung",
                    "type": "yes_no",
                    "label": "Hatten Sie seit der letzten Untersuchung eine schwere oder länger "
                             "dauernde Erkrankung?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                    "followup": {"id": "schwere_erkrankung_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, und wann?", "when": "yes"},
                },
                {
                    "id": "zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung von Ihnen "
                             "und Ihrer Tätigkeit am Arbeitsplatz?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                },
                {
                    "id": "aehnliche_erkrankungen",
                    "type": "yes_no",
                    "label": "Sind bei Kolleginnen oder Kollegen an vergleichbaren Arbeitsplätzen "
                             "gehäuft ähnliche Erkrankungen aufgetreten?",
                    "required": True,
                    "show_if": {"id": "untersuchung_art", "in": ["nach", "nachgehend"]},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Beschwerden & Warnzeichen",
            "subtitle": "Beschwerden, auf die der Grundsatz G 40 besonders achtet",
            "questions": [
                {
                    "id": "warnzeichen_allgemein",
                    "type": "multi_choice",
                    "label": "Haben Sie eines der folgenden allgemeinen Warnzeichen bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "infekte", "label": "Wiederholt schwere Infektionskrankheiten"},
                        {"value": "wunden", "label": "Schlecht heilende Wunden"},
                        {"value": "gewicht", "label": "Ungewollte starke Gewichtsabnahme"},
                        {"value": "lymphknoten", "label": "Geschwollene Lymphknoten (z. B. am Hals, "
                                                          "in der Achsel oder Leiste)"},
                        {"value": "keine", "label": "Nein, keines davon"},
                    ],
                },
                {
                    "id": "beschwerden_koerper",
                    "type": "multi_choice",
                    "label": "Haben Sie eine der folgenden Beschwerden?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "reizhusten", "label": "Chronischer Reizhusten (dauerhafter trockener Husten)"},
                        {"value": "heiserkeit", "label": "Länger andauernde Heiserkeit"},
                        {"value": "auswurf_blut", "label": "Auswurf (Schleim beim Husten) mit Blutbeimengungen"},
                        {"value": "blut_urin", "label": "Blut im Urin"},
                        {"value": "stuhl_auffaellig", "label": "Stuhlgang von wechselnder Beschaffenheit "
                                                               "mit Blut- oder Schleimbeimengungen"},
                        {"value": "keine", "label": "Nein, keine davon"},
                    ],
                },
                {
                    "id": "haut_schleimhaut",
                    "type": "multi_choice",
                    "label": "Haben Sie Veränderungen an Haut oder Schleimhäuten bemerkt?",
                    "hint": "Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "hautveraenderungen", "label": "Hautveränderungen (z. B. Ekzeme, starke "
                                                                 "Verhornungen, Geschwüre, Pigmentflecken, "
                                                                 "auffällige oder veränderte Muttermale)"},
                        {"value": "schleimhaut", "label": "Veränderungen der Schleimhaut in Mund, Rachen "
                                                          "oder Nase (z. B. weiße Flecken, wunde Stellen)"},
                        {"value": "keine", "label": "Nein, keine davon"},
                    ],
                },
            ],
        },
        # ── 5 ─ Vorgeschichte ──────────────────────────────────────────────
        {
            "id": "vorgeschichte",
            "title": "Vorerkrankungen & Vorgeschichte",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "krebs",
                    "type": "yes_no",
                    "label": "Hatten oder haben Sie eine Krebserkrankung?",
                    "required": True,
                    "followup": {"id": "krebs_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, wann, und wie wurde sie behandelt?",
                                 "when": "yes"},
                },
                {
                    "id": "praekanzerose",
                    "type": "yes_no",
                    "label": "Wurde bei Ihnen eine Krebsvorstufe festgestellt (Präkanzerose, z. B. "
                             "auffällige Gewebeveränderung, die ärztlich als Vorstufe von Krebs "
                             "bezeichnet wurde)?",
                    "required": True,
                    "followup": {"id": "praekanzerose_desc", "type": "text",
                                 "label": "Welche, und wo?", "when": "yes"},
                },
                {
                    "id": "patho_labor",
                    "type": "yes_no",
                    "label": "Wurden bei Ihnen dauerhaft deutlich auffällige Laborwerte festgestellt "
                             "(z. B. Blutbild- oder Leberwerte), die bis heute bestehen?",
                    "required": True,
                    "followup": {"id": "patho_labor_desc", "type": "text",
                                 "label": "Welche Werte, falls bekannt?", "when": "yes"},
                },
                {
                    "id": "immundefekt",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen ein schwerer Immundefekt (stark geschwächte "
                             "körpereigene Abwehr)?",
                    "required": True,
                },
                {
                    "id": "immunsuppression",
                    "type": "yes_no",
                    "label": "Erhalten oder erhielten Sie eine Behandlung, die das Immunsystem "
                             "dauerhaft schwächt (z. B. Immunsuppressiva nach Transplantation, "
                             "Chemotherapie, Kortison in hoher Dauerdosis)?",
                    "required": True,
                    "followup": {"id": "immunsuppression_desc", "type": "text",
                                 "label": "Welche Behandlung, und wann?", "when": "yes"},
                },
                {
                    "id": "familie",
                    "type": "yes_no",
                    "label": "Kommen in Ihrer Familie gehäuft bösartige Tumorerkrankungen (Krebs) "
                             "oder Erkrankungen des Immunsystems vor?",
                    "required": True,
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {"id": "medikamente_desc", "type": "textarea",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Rauchen & Alkohol ──────────────────────────────────────────
        {
            "id": "noxen",
            "title": "Rauchen & Alkohol",
            "subtitle": "Angaben laut Grundsatz G 40 (Raucher- und Alkoholanamnese)",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nein, ich habe nie geraucht"},
                        {"value": "frueher", "label": "Früher, ich habe aufgehört"},
                        {"value": "ja", "label": "Ja, ich rauche"},
                    ],
                },
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Trinken Sie Alkohol?",
                    "required": True,
                    "options": [
                        {"value": "nie_selten", "label": "Nie oder sehr selten"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche)"},
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
    # ── Dauernde gesundheitliche Bedenken (Abschnitt 2.1.1) ───────────────
    {"wenn": {"krebs": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Krebserkrankung",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Durchgemachte oder bestehende Krebserkrankung angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken gegen Aufnahme bzw. "
                   "Fortsetzung der Tätigkeit. Nach 2.1.3 prüfen, ob unter bestimmten "
                   "Voraussetzungen (technische Schutzmaßnahmen, PSA unter Beachtung des "
                   "individuellen Gesundheitszustands, verkürzte Nachuntersuchungsfristen) "
                   "die Tätigkeit dennoch möglich ist; Vorbefunde einholen."},
    {"wenn": {"praekanzerose": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Präkanzerose",
     "quelle": "Abschnitte 2.1.1 und Tabelle 2 (Präkanzerosen)",
     "befund": "Krebsvorstufe (Präkanzerose) in der Vorgeschichte angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken (2.1.1). Fachärztliche "
                   "Abklärung bzw. Verlaufskontrolle veranlassen (vgl. Tabelle 2); nach 2.1.3 "
                   "prüfen, ob die Tätigkeit unter Voraussetzungen (Schutzmaßnahmen, PSA, "
                   "verkürzte Nachuntersuchungsfristen) möglich ist."},
    {"wenn": {"patho_labor": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Laborbefunde",
     "quelle": "Abschnitte 2.1.1 und 1.2.3 (Ergänzungsuntersuchung)",
     "befund": "Fortbestehende, deutlich auffällige Laborwerte angegeben.",
     "konsequenz": "Vorbefunde anfordern und Laborkontrolle veranlassen; bei fortbestehend "
                   "eindeutig pathologischen Werten für klinisch relevante Parameter dauernde "
                   "gesundheitliche Bedenken (2.1.1). In unklaren Fällen weiterführende "
                   "fachärztliche Ergänzungsuntersuchung (1.2.3: z. B. hämatologisch, "
                   "biochemisch, sonographisch, endoskopisch)."},
    {"wenn": {"immundefekt": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Immunsystem",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Schwerer Immundefekt angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken (2.1.1); Vorbefunde "
                   "einholen. Nach 2.1.3 prüfen, ob unter bestimmten Voraussetzungen "
                   "(Schutzmaßnahmen, PSA, verkürzte Nachuntersuchungsfristen) die Tätigkeit "
                   "möglich ist."},
    {"wenn": {"immunsuppression": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Immunsystem",
     "quelle": "Abschnitt 2.1.1 (Dauernde gesundheitliche Bedenken)",
     "befund": "Therapie, die das Immunsystem nachhaltig schwächt, angegeben.",
     "konsequenz": "Tatbestand für dauernde gesundheitliche Bedenken (2.1.1); Therapie- und "
                   "Medikamentenanamnese vertiefen. Nach 2.1.3 prüfen, ob die Tätigkeit unter "
                   "Voraussetzungen (Schutzmaßnahmen, PSA, verkürzte Nachuntersuchungsfristen) "
                   "fortgesetzt werden kann."},
    # ── Vorzeitige Nachuntersuchung (Abschnitt 1.1) ───────────────────────
    {"wenn": {"schwere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenanamnese",
     "quelle": "Abschnitt 1.1 (Vorzeitige Nachuntersuchung)",
     "befund": "Schwere oder länger dauernde Erkrankung seit der letzten Untersuchung "
               "angegeben.",
     "konsequenz": "Prüfen, ob die Erkrankung Anlass zu Bedenken gegen eine Fortsetzung der "
                   "Tätigkeit geben könnte; vorzeitige Nachuntersuchung nach 1.1 durchführen "
                   "bzw. das Untersuchungsprogramm entsprechend erweitern; Befunde der "
                   "behandelnden Ärzte einholen."},
    {"wenn": {"zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Zwischenanamnese",
     "quelle": "Abschnitt 1.1 (Vorzeitige Nachuntersuchung)",
     "befund": "Die untersuchte Person vermutet einen ursächlichen Zusammenhang zwischen "
               "einer Erkrankung und ihrer Tätigkeit.",
     "konsequenz": "Vorzeitige Nachuntersuchung nach 1.1 ist angezeigt; Verdacht ärztlich "
                   "abklären, Expositionsdaten (Luft-/Biomonitoring) heranziehen und ggf. "
                   "BK-Anzeige prüfen (Abschnitt 4)."},
    {"wenn": {"aehnliche_erkrankungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Erkrankungshäufung",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung) und 2.2 (Beratung)",
     "befund": "Gehäuftes Auftreten ähnlicher Erkrankungen an vergleichbaren Arbeitsplätzen "
               "angegeben.",
     "konsequenz": "Häufung dokumentieren und abklären; dem Arbeitgeber die notwendige "
                   "Aktualisierung der Gefährdungsbeurteilung zur Verbesserung des "
                   "Arbeitsschutzes mitteilen (2.2) – unter Wahrung der schutzwürdigen "
                   "Belange der untersuchten Person."},
    # ── Beschwerden / Warnzeichen (Abschnitte 1.2.1–1.2.3) ────────────────
    {"wenn": {"warnzeichen_allgemein": ["infekte", "wunden", "gewicht", "lymphknoten"]},
     "schwere": "pruefen",
     "bereich": "Allgemeine Warnzeichen",
     "quelle": "Abschnitte 1.2.1 und 1.2.2",
     "befund": "Allgemeine Warnzeichen angegeben (schwere Infekte, schlecht heilende Wunden, "
               "ungewollte Gewichtsabnahme oder Lymphknotenschwellung).",
     "konsequenz": "Gezielte ärztliche Abklärung: BSG oder CRP und großes Blutbild (1.2.2) "
                   "bewerten; in unklaren Fällen weiterführende fachärztliche "
                   "Ergänzungsuntersuchung (1.2.3); auf Paraneoplasien achten (Tabellen 3–6)."},
    {"wenn": {"beschwerden_koerper": ["reizhusten", "heiserkeit", "auswurf_blut"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 1.2.1 und 1.2.2",
     "befund": "Chronischer Reizhusten, länger andauernde Heiserkeit oder blutiger Auswurf "
               "angegeben.",
     "konsequenz": "Gezielte Abklärung der Atemwege; ggf. radiologische Diagnostik des Thorax "
                   "(nach 1.2.2 nur, wenn die Wirkungsweise des Gefahrstoffs dies erfordert, "
                   "z. B. Benzo(a)pyren, Dichlordimethylether, Dieselmotor-Emissionen, oder im "
                   "Einzelfall bei Auffälligkeiten); fachärztliche Ergänzungsuntersuchung "
                   "(1.2.3) erwägen."},
    {"wenn": {"beschwerden_koerper": ["blut_urin"]},
     "schwere": "pruefen",
     "bereich": "Harnwege",
     "quelle": "Abschnitte 1.2.1 (Urinstatus) und 1.2.3",
     "befund": "Blut im Urin angegeben.",
     "konsequenz": "Urinstatus (Mehrfachteststreifen einschließlich Erythrozyten und "
                   "Leukozyten) durchführen und bewerten; bei bestätigtem Befund urologische "
                   "Ergänzungsuntersuchung (1.2.3) veranlassen."},
    {"wenn": {"beschwerden_koerper": ["stuhl_auffaellig"]},
     "schwere": "pruefen",
     "bereich": "Verdauungstrakt",
     "quelle": "Abschnitte 1.2.2 und 1.2.3",
     "befund": "Stuhlgang von wechselnder Konsistenz mit Blut- oder Schleimbeimengungen "
               "angegeben.",
     "konsequenz": "Suchtest auf okkultes Blut im Stuhl (1.2.2) durchführen; bei auffälligem "
                   "Ergebnis endoskopische Ergänzungsuntersuchung (1.2.3) veranlassen."},
    {"wenn": {"haut_schleimhaut": ["hautveraenderungen", "schleimhaut"]},
     "schwere": "pruefen",
     "bereich": "Haut/Schleimhaut",
     "quelle": "Abschnitte 1.2.1, Tabellen 2 und 3",
     "befund": "Haut- oder Schleimhautveränderungen angegeben (z. B. Ekzeme, Hyperkeratosen, "
               "Ulzerationen, Pigmentstörungen, Naevi, Schleimhautveränderungen in Mund, "
               "Rachen oder Nase).",
     "konsequenz": "Gezielte Inspektion auf Präkanzerosen und kutane Paraneoplasien (Tabellen 2 "
                   "und 3); dermatologische bzw. HNO-ärztliche Ergänzungsuntersuchung (1.2.3) "
                   "veranlassen."},
    # ── Exposition und Arbeitsschutz ──────────────────────────────────────
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Expositionsereignis",
     "quelle": "Abschnitte 1.2.1 (Nachuntersuchung) und 3.1 (Biomonitoring)",
     "befund": "Unfall bzw. kurzzeitig hohe Exposition gegenüber krebserzeugenden Stoffen "
               "angegeben.",
     "konsequenz": "Ereignis dokumentieren; Daten aus arbeitsplatz- oder personenbezogenem "
                   "Luft- bzw. Biomonitoring heranziehen (1.2.1); Biomonitoring mit "
                   "zuverlässigen, qualitätsgesicherten Methoden nach Abschnitt 3.1 erwägen."},
    {"wenn": {"psa": ["selten", "nie"]},
     "schwere": "hinweis",
     "bereich": "Schutzausrüstung",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Vorgesehene persönliche Schutzausrüstung wird selten oder nie getragen.",
     "konsequenz": "Beratung zu allgemeinen Hygienemaßnahmen und persönlicher Schutzausrüstung "
                   "sowie zur krebserzeugenden Wirkung des Arbeitsstoffs (2.2); bei Hinweisen "
                   "auf unzureichenden Arbeitsschutz Mitteilung an den Arbeitgeber zur "
                   "Aktualisierung der Gefährdungsbeurteilung."},
    {"wenn": {"fruehere_expo": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Frühere Exposition",
     "quelle": "Abschnitte 1.1 (nachgehende Untersuchungen) und 1.2.1",
     "befund": "Frühere berufliche Belastung durch krebserzeugende Gefahrstoffe angegeben.",
     "konsequenz": "Frühere Expositionen dokumentieren und bei der Beurteilung berücksichtigen; "
                   "nachgehende Untersuchungen über den Organisationsdienst für nachgehende "
                   "Untersuchungen (ODIN, www.odin-info.de) bzw. – je nach Stoff – über die "
                   "GVS sicherstellen."},
    {"wenn": {"ausserberuflich": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Außerberufliche Exposition",
     "quelle": "Abschnitt 1.2.1 (Anamnese)",
     "befund": "Exposition gegenüber krebserzeugenden Gefahrstoffen außerhalb der beruflichen "
               "Tätigkeit angegeben.",
     "konsequenz": "Außerberufliche Exposition dokumentieren und bei Beurteilung und Beratung "
                   "berücksichtigen; Beratung zur Verringerung der Belastung."},
    {"wenn": {"strahlen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Strahlenexposition",
     "quelle": "Abschnitt 1.2.1 (Anamnese)",
     "befund": "Frühere therapeutische oder sonstige erhebliche Exposition gegen ionisierende "
               "Strahlen angegeben.",
     "konsequenz": "Strahlenanamnese dokumentieren und als zusätzlichen Risikofaktor bei der "
                   "Beurteilung berücksichtigen; Zurückhaltung bei zusätzlicher radiologischer "
                   "Diagnostik (Leitlinien der Bundesärztekammer, 1.3)."},
    # ── Beratung zu Noxen (Raucher-/Alkoholanamnese, 1.2.1) ───────────────
    {"wenn": {"rauchen": ["ja"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 1.2.1 (Raucheranamnese) und 2.2, Tabelle 2",
     "befund": "Aktives Rauchen angegeben.",
     "konsequenz": "Raucheranamnese vertiefen; Beratung zum kombinierten Krebsrisiko von "
                   "Tabakrauch und Arbeitsstoffen (Tabakrauch ist Risikofaktor zahlreicher "
                   "Präkanzerosen, Tabelle 2); Tabakentwöhnung empfehlen."},
    {"wenn": {"alkohol": ["regelmaessig"]},
     "schwere": "hinweis",
     "bereich": "Alkohol",
     "quelle": "Abschnitte 1.2.1 (Alkoholanamnese) und 2.2, Tabelle 2",
     "befund": "Regelmäßiger Alkoholkonsum angegeben.",
     "konsequenz": "Alkoholanamnese vertiefen; Beratung zum Krebsrisiko durch Alkohol "
                   "(Risikofaktor u. a. für Kehlkopf-, Mundhöhlen- und Leberkarzinome, "
                   "Tabelle 2) und zur Reduktion des Konsums."},
]
