# -*- coding: utf-8 -*-
"""G 35 Arbeitsaufenthalt im Ausland – DGUV Grundsatz 2016.

Quelle: DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage
2016, G 35 "Arbeitsaufenthalt im Ausland unter besonderen klimatischen oder
gesundheitlichen Belastungen" (Fassung Oktober 2014), S. 495–508.
"""

SLUG = "g35-ausland-2016"

CATALOG = {
    "version": 2,
    "title": "G 35 Arbeitsaufenthalt im Ausland (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 6. Auflage 2016, "
             "G 35 „Arbeitsaufenthalt im Ausland unter besonderen klimatischen oder "
             "gesundheitlichen Belastungen“ (Fassung Oktober 2014), S. 495–508",
    "sections": [
        # ── 1 ──────────────────────────────────────────────────────────────
        {
            "id": "einsatz",
            "title": "Tätigkeit & Auslandseinsatz",
            "subtitle": "Angaben zu Ihrem Arbeitsaufenthalt im Ausland",
            "questions": [
                {
                    "id": "untersuchungsart",
                    "type": "choice",
                    "label": "Welche Untersuchung findet heute statt?",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung vor der Ausreise"},
                        {"value": "nach", "label": "Nachuntersuchung während der laufenden Auslandstätigkeit"},
                        {"value": "rueckkehr", "label": "Untersuchung nach Rückkehr bzw. nach Beendigung der Tätigkeit"},
                    ],
                },
                {
                    "id": "aufenthaltsdauer",
                    "type": "choice",
                    "label": "Wie lange halten Sie sich beruflich pro Jahr im Ausland auf "
                             "(insgesamt, auch mehrere Reisen zusammengerechnet)?",
                    "hint": "Bei mehr als 3 Monaten pro Jahr ist vor der ersten Ausreise "
                            "eine Erstuntersuchung vorgesehen.",
                    "required": True,
                    "options": [
                        {"value": "unter3m", "label": "Bis 3 Monate pro Jahr"},
                        {"value": "ueber3m", "label": "Mehr als 3 Monate pro Jahr"},
                    ],
                },
                {
                    "id": "besondere_bedingungen",
                    "type": "yes_no",
                    "label": "Gelten für Ihren Einsatz besondere Bedingungen (besonders schlechte "
                             "medizinische Versorgung, ständig wechselnde Einsatzorte, besonders "
                             "hohe Infektionsgefahr oder besondere berufliche Belastung)?",
                    "required": True,
                },
                {
                    "id": "zielgebiet",
                    "type": "multi_choice",
                    "label": "In welche Gebiete führt bzw. führte Ihre Tätigkeit?",
                    "hint": "Mehrfachauswahl möglich. „Warme Länder“ liegen zwischen 30° "
                            "nördlicher und 30° südlicher Breite (Tropen und Subtropen).",
                    "required": True,
                    "options": [
                        {"value": "tropen", "label": "Tropen (Gürtel beiderseits des Äquators)"},
                        {"value": "subtropen", "label": "Subtropen / warme Länder"},
                        {"value": "polar", "label": "Polarregionen"},
                        {"value": "sonstige", "label": "Sonstige Länder mit ungünstigen hygienischen Bedingungen "
                                                       "oder schlechter medizinischer Versorgung"},
                    ],
                },
                {
                    "id": "hoehe",
                    "type": "yes_no",
                    "label": "Arbeiten Sie im Ausland in größeren Höhen (Gebirge)?",
                    "required": True,
                },
                {
                    "id": "fruehere_aufenthalte",
                    "type": "yes_no",
                    "label": "Hatten Sie bereits früher längere Arbeitsaufenthalte im Ausland?",
                    "required": True,
                    "followup": {
                        "id": "fruehere_aufenthalte_desc",
                        "type": "text",
                        "label": "Wann, wo, und gab es dabei gesundheitliche Probleme?",
                        "when": "yes",
                    },
                },
                {
                    "id": "letzte_rueckkehruntersuchung",
                    "type": "choice",
                    "label": "Wurde bei Ihnen nach einem früheren Auslandseinsatz schon einmal "
                             "eine Rückkehruntersuchung durchgeführt?",
                    "hint": "Liegt die Rückkehruntersuchung nicht länger als 1 Jahr zurück, "
                            "ist vor einem erneuten Einsatz keine neue Erstuntersuchung "
                            "erforderlich – eine ärztliche Beratung aber weiterhin.",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["erst"]},
                    "options": [
                        {"value": "keine", "label": "Nein, dies ist mein erster Auslandseinsatz"},
                        {"value": "unter1j", "label": "Ja, vor weniger als 1 Jahr"},
                        {"value": "ueber1j", "label": "Ja, vor mehr als 1 Jahr"},
                    ],
                },
                {
                    "id": "letzte_untersuchung",
                    "type": "choice",
                    "label": "Wann war Ihre letzte arbeitsmedizinische Untersuchung nach G 35?",
                    "hint": "Nachuntersuchungen sind nach 24 bis 36 Monaten sowie nach "
                            "Beendigung der Tätigkeit vorgesehen.",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                    "options": [
                        {"value": "unter24m", "label": "Vor weniger als 2 Jahren"},
                        {"value": "m24bis36", "label": "Vor 2 bis 3 Jahren"},
                        {"value": "ueber36m", "label": "Vor mehr als 3 Jahren"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "landwechsel",
                    "type": "yes_no",
                    "label": "Steht ein Wechsel in ein Land mit deutlich anderen klimatischen "
                             "oder gesundheitlichen Belastungen an?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach"]},
                },
                {
                    "id": "mitreisende",
                    "type": "yes_no",
                    "label": "Begleiten Ehepartnerin/Ehepartner oder Kinder Sie in das Einsatzland?",
                    "required": True,
                },
            ],
        },
        # ── 2 ──────────────────────────────────────────────────────────────
        {
            "id": "verlauf",
            "title": "Verlauf des Auslandsaufenthalts",
            "subtitle": "Erkrankungen und Belastungen während der Tätigkeit",
            "questions": [
                {
                    "id": "laengere_erkrankung",
                    "type": "yes_no",
                    "label": "Waren Sie während der Auslandstätigkeit über mehrere Wochen krank "
                             "oder körperlich beeinträchtigt?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                    "followup": {
                        "id": "laengere_erkrankung_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung/Beeinträchtigung, wann, und wie wurde sie behandelt?",
                        "when": "yes",
                    },
                },
                {
                    "id": "zusammenhang_taetigkeit",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen einer Erkrankung und "
                             "Ihrer Tätigkeit bzw. Ihrem Arbeitsplatz im Ausland?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                    "followup": {
                        "id": "zusammenhang_taetigkeit_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankung, und warum vermuten Sie den Zusammenhang?",
                        "when": "yes",
                    },
                },
                {
                    "id": "exposition_risiko",
                    "type": "yes_no",
                    "label": "Gab es besondere Ansteckungsrisiken (z.B. unsauberes Trinkwasser, "
                             "Baden in Süßwasser, viele Insektenstiche ohne Schutz, enger "
                             "Tierkontakt oder Tierbisse)?",
                    "hint": "Über Süßwasser kann z.B. die Wurmerkrankung Bilharziose "
                            "(Schistosomiasis) übertragen werden.",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                    "followup": {
                        "id": "exposition_risiko_desc",
                        "type": "textarea",
                        "label": "Welche Risiken waren das, und wie oft kamen sie vor?",
                        "when": "yes",
                    },
                },
                {
                    "id": "malaria_prophylaxe",
                    "type": "choice",
                    "label": "Haben Sie die für Ihr Einsatzgebiet empfohlene Malaria-Vorbeugung "
                             "durchgeführt (Tabletten und Mückenschutz)?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                    "options": [
                        {"value": "regelmaessig", "label": "Ja, regelmäßig wie empfohlen"},
                        {"value": "unregelmaessig", "label": "Ja, aber unregelmäßig oder vorzeitig beendet"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "nicht_erforderlich", "label": "Für mein Einsatzgebiet nicht empfohlen"},
                    ],
                },
            ],
        },
        # ── 3 ──────────────────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Beschwerden, die auf eine Tropenkrankheit oder andere Erkrankung "
                        "hinweisen können",
            "questions": [
                {
                    "id": "fieber",
                    "type": "yes_no",
                    "label": "Hatten Sie während oder nach dem Auslandsaufenthalt unklares Fieber?",
                    "hint": "Fieber nach Tropenaufenthalt muss immer rasch abgeklärt werden "
                            "(u.a. Ausschluss einer Malaria).",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                    "followup": {
                        "id": "fieber_desc",
                        "type": "text",
                        "label": "Wann traten die Fieberepisoden auf, und wurden sie untersucht?",
                        "when": "yes",
                    },
                },
                {
                    "id": "durchfall",
                    "type": "yes_no",
                    "label": "Haben Sie anhaltende oder immer wiederkehrende Durchfälle?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                },
                {
                    "id": "husten",
                    "type": "yes_no",
                    "label": "Haben Sie Husten, der seit 4 Wochen oder länger anhält?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                },
                {
                    "id": "allgemeinsymptome",
                    "type": "yes_no",
                    "label": "Haben Sie ungewollt stark an Gewicht verloren oder geschwollene "
                             "Lymphknoten an mehreren Körperstellen bemerkt?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                },
                {
                    "id": "hautveraenderungen",
                    "type": "yes_no",
                    "label": "Haben Sie auffällige Hautveränderungen (z.B. juckende Quaddeln, "
                             "stark juckende Stellen oder schlecht heilende Geschwüre)?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach", "rueckkehr"]},
                },
                {
                    "id": "psychisch_auffaellig",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich seelisch stark belastet (z.B. anhaltender Stress, "
                             "Schlafstörungen, gedrückte Stimmung, Heimweh, Anpassungsprobleme "
                             "an das fremde Umfeld)?",
                    "hint": "Der Wechsel in einen fremden Kulturkreis kann psychisch belasten "
                            "(sogenannter Akulturationsstress).",
                    "required": True,
                },
            ],
        },
        # ── 4 ──────────────────────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Medikamente",
            "subtitle": "Erkrankungen und Behandlungen, die für den Auslandseinsatz wichtig sind",
            "questions": [
                {
                    "id": "chronische_erkrankung",
                    "type": "yes_no",
                    "label": "Haben Sie eine chronische Erkrankung (z.B. Herz-Kreislauf-Erkrankung, "
                             "Zuckerkrankheit/Diabetes, Rheuma, Asthma, psychische Erkrankung)?",
                    "required": True,
                    "followup": {
                        "id": "chronische_erkrankung_desc",
                        "type": "textarea",
                        "label": "Welche Erkrankungen sind das, und wie werden sie behandelt?",
                        "when": "yes",
                    },
                },
                {
                    "id": "versorgung_einsatzort",
                    "type": "choice",
                    "label": "Kann Ihre Erkrankung am Einsatzort ärztlich betreut werden, und "
                             "erhalten Sie dort zuverlässig Ihre Medikamente?",
                    "required": True,
                    "show_if": {"id": "chronische_erkrankung", "in": ["yes"]},
                    "options": [
                        {"value": "ja", "label": "Ja, Betreuung und Medikamente sind gesichert"},
                        {"value": "nein", "label": "Nein"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "staendige_betreuung",
                    "type": "yes_no",
                    "label": "Benötigen Sie wegen einer Erkrankung ständige ärztliche Betreuung "
                             "oder engmaschige Kontrolluntersuchungen?",
                    "required": True,
                },
                {
                    "id": "akute_erkrankung",
                    "type": "yes_no",
                    "label": "Sind Sie derzeit akut erkrankt oder wegen einer vorübergehenden "
                             "Gesundheitsstörung in Behandlung?",
                    "required": True,
                    "followup": {
                        "id": "akute_erkrankung_desc",
                        "type": "text",
                        "label": "Um welche Erkrankung handelt es sich, und wie lange dauert "
                                 "die Behandlung voraussichtlich noch?",
                        "when": "yes",
                    },
                },
                {
                    "id": "medikamente",
                    "type": "yes_no",
                    "label": "Nehmen Sie regelmäßig Medikamente ein?",
                    "required": True,
                    "followup": {
                        "id": "medikamente_desc",
                        "type": "textarea",
                        "label": "Welche Medikamente nehmen Sie ein?",
                        "when": "yes",
                    },
                },
                {
                    "id": "impfschutz",
                    "type": "choice",
                    "label": "Ist Ihr Impfschutz nach Ihrem Kenntnisstand vollständig "
                             "(Standardimpfungen und Reiseimpfungen für Ihr Zielland)?",
                    "hint": "Bitte bringen Sie Ihren Impfausweis zur Untersuchung mit.",
                    "required": True,
                    "options": [
                        {"value": "vollstaendig", "label": "Ja, vollständig"},
                        {"value": "unvollstaendig", "label": "Nein, es fehlen Impfungen"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "alkohol",
                    "type": "choice",
                    "label": "Wie oft trinken Sie Alkohol?",
                    "hint": "Erfahrungsgemäß steigt der Alkoholkonsum bei Auslandseinsätzen "
                            "häufig an (Stress, Langeweile, andere Trinkgewohnheiten vor Ort).",
                    "required": True,
                    "options": [
                        {"value": "nie", "label": "Nie"},
                        {"value": "gelegentlich", "label": "Gelegentlich"},
                        {"value": "regelmaessig", "label": "Regelmäßig (mehrmals pro Woche)"},
                        {"value": "zugenommen", "label": "Mein Konsum hat im Ausland deutlich zugenommen"},
                    ],
                },
                {
                    "id": "schwangerschaft",
                    "type": "choice",
                    "label": "Besteht bei Ihnen derzeit eine Schwangerschaft?",
                    "required": True,
                    "options": [
                        {"value": "nein", "label": "Nein"},
                        {"value": "ja", "label": "Ja"},
                        {"value": "unsicher", "label": "Bin mir nicht sicher"},
                        {"value": "entfaellt", "label": "Entfällt"},
                    ],
                },
                {
                    "id": "zahnbehandlung",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen derzeit eine Zahnbehandlung nicht abgeschlossen oder "
                             "bekannt, dass Zähne behandelt werden müssten?",
                    "hint": "Eine erforderliche zahnärztliche Behandlung sollte vor der "
                            "Ausreise abgeschlossen werden.",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["erst"]},
                },
            ],
        },
        # ── 5 ──────────────────────────────────────────────────────────────
        {
            "id": "einwilligung",
            "title": "Einwilligung",
            "subtitle": "Bestätigung Ihrer Angaben",
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
    # ── Untersuchungsanlass & Fristen ───────────────────────────────────────
    {"wenn": {"besondere_bedingungen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Untersuchungsanlass",
     "quelle": "G 35 Abschnitt 1.1",
     "befund": "Besondere Einsatzbedingungen (schlechte medizinische Versorgung, ständig "
               "wechselnde Einsatzorte, besonders hohe Infektionsgefahr oder besondere "
               "berufliche Belastung)",
     "konsequenz": "Erstuntersuchung ungeachtet der Aufenthaltsdauer durchführen; Beratungs- "
                   "und Untersuchungsumfang an die besonderen Bedingungen anpassen."},
    {"wenn": {"letzte_rueckkehruntersuchung": ["unter1j"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "G 35 Abschnitt 1.1",
     "befund": "Rückkehruntersuchung liegt weniger als 1 Jahr zurück",
     "konsequenz": "Vor dem erneuten Arbeitsaufenthalt ist keine neue Erstuntersuchung "
                   "erforderlich; die ärztliche Beratung bleibt erforderlich."},
    {"wenn": {"letzte_untersuchung": ["ueber36m"]},
     "schwere": "hinweis",
     "bereich": "Fristen",
     "quelle": "G 35 Abschnitt 1.1",
     "befund": "Letzte G 35-Untersuchung liegt mehr als 3 Jahre zurück",
     "konsequenz": "Nachuntersuchungsfrist (24–36 Monate) ist überschritten – "
                   "Nachuntersuchung jetzt vollständig durchführen und künftige Frist "
                   "vormerken."},
    {"wenn": {"landwechsel": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Fristen",
     "quelle": "G 35 Abschnitt 1.1",
     "befund": "Wechsel in ein Land mit erheblich verschiedener klimatischer oder "
               "gesundheitlicher Belastung",
     "konsequenz": "Vorzeitige Nachuntersuchung veranlassen; Beratung auf das neue "
                   "Einsatzland ausrichten (Klima, Infektionsrisiken, medizinische "
                   "Versorgung)."},
    {"wenn": {"laengere_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Fristen",
     "quelle": "G 35 Abschnitt 1.1 und 1.2.3",
     "befund": "Mehrwöchige Erkrankung oder körperliche Beeinträchtigung während der "
               "Auslandstätigkeit",
     "konsequenz": "Vorzeitige Nachuntersuchung; klären, ob gesundheitliche Bedenken gegen "
                   "die Fortsetzung des Arbeitsaufenthaltes bestehen; ggf. "
                   "Ergänzungsuntersuchung veranlassen."},
    {"wenn": {"zusammenhang_taetigkeit": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Berufskrankheit",
     "quelle": "G 35 Abschnitt 1.1 und 4",
     "befund": "Vermuteter Zusammenhang zwischen Erkrankung und Tätigkeit",
     "konsequenz": "Nachuntersuchung veranlassen; Verdacht auf Berufskrankheit prüfen "
                   "(BK-Nrn. 3101, 3102, 3104) und ggf. BK-Anzeige erstatten."},
    # ── Exposition & Symptome ───────────────────────────────────────────────
    {"wenn": {"exposition_risiko": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "G 35 Abschnitt 1.2.2 (Nachuntersuchung)",
     "befund": "Relevantes Expositionsrisiko (Trinkwasser, Süßwasser, Insekten, Tiere)",
     "konsequenz": "Gezielte Serologie sowie Stuhl- und Urinuntersuchungen bei relevantem "
                   "Expositionsrisiko durchführen."},
    {"wenn": {"fieber": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Infektionszeichen",
     "quelle": "G 35 Abschnitt 1.2.3, 2.1.2 und 5.1",
     "befund": "Unklares Fieber während oder nach dem Auslandsaufenthalt",
     "konsequenz": "Unverzügliche Abklärung (v.a. Malaria-Ausschluss); falls keine Klärung "
                   "möglich, ergänzende Befunde bei einer Institution oder einem Arzt mit "
                   "tropenmedizinischer Erfahrung einholen; bis zur Klärung befristete "
                   "gesundheitliche Bedenken."},
    {"wenn": {"durchfall": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Magen-Darm",
     "quelle": "G 35 Abschnitt 1.2.3",
     "befund": "Anhaltende Durchfälle",
     "konsequenz": "Ergänzungsuntersuchung: gezielte Stuhluntersuchungen (u.a. auf Lamblien "
                   "und Amöben); bei fehlender Klärung tropenmedizinische Vorstellung."},
    {"wenn": {"husten": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "G 35 Abschnitt 1.2.3",
     "befund": "Anhaltender Husten (4 Wochen und länger)",
     "konsequenz": "Ergänzungsuntersuchung veranlassen, u.a. Gamma-Interferontest "
                   "(Tuberkulose-Ausschluss); ggf. fachärztliche Abklärung."},
    {"wenn": {"allgemeinsymptome": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allgemeinsymptome",
     "quelle": "G 35 Abschnitt 1.2.3 und 5.1",
     "befund": "Starker Gewichtsverlust oder generalisierte Lymphknotenschwellungen",
     "konsequenz": "Ergänzungsuntersuchung (u.a. HIV-Test, Differenzialdiagnostik); bei "
                   "fehlender Klärung Vorstellung bei einer Institution mit "
                   "tropenmedizinischer Erfahrung."},
    {"wenn": {"hautveraenderungen": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "G 35 Abschnitt 1.2.3",
     "befund": "Urtikarielle, pruriginöse oder ulzerative Hautveränderungen",
     "konsequenz": "Abklärung der Hautveränderungen; ggf. dermatologische bzw. "
                   "tropenmedizinische Vorstellung (z.B. Verdacht auf Wurmerkrankung oder "
                   "Leishmaniose)."},
    {"wenn": {"psychisch_auffaellig": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Psyche",
     "quelle": "G 35 Abschnitt 1.2.3 und 3.4",
     "befund": "Psychische Auffälligkeiten bzw. starke seelische Belastung",
     "konsequenz": "Abklärung psychischer Auffälligkeiten; Beratung zu Akulturationsstress "
                   "und Belastungen im Ausland; ggf. fachärztliche Vorstellung vor "
                   "(weiterem) Einsatz."},
    # ── Beurteilung (Abschnitt 2.1) ─────────────────────────────────────────
    {"wenn": {"staendige_betreuung": ["yes"]},
     "schwere": "kritisch",
     "bereich": "Beurteilung",
     "quelle": "G 35 Abschnitt 2.1.1",
     "befund": "Ständige ärztliche Betreuung erforderlich",
     "konsequenz": "Dauernde gesundheitliche Bedenken erwägen, wenn unter den Belastungen "
                   "des Auslandsaufenthaltes mit Verschlimmerung zu rechnen ist oder "
                   "typische Komplikationen am Tätigkeitsort nicht behandelt werden können; "
                   "Schwere der Erkrankung, Funktionsbeeinträchtigungen und "
                   "Behandlungsmöglichkeiten vor Ort prüfen – Klärung VOR der Ausreise."},
    {"wenn": {"chronische_erkrankung": ["yes"], "versorgung_einsatzort": ["nein", "unbekannt"]},
     "schwere": "kritisch",
     "bereich": "Beurteilung",
     "quelle": "G 35 Abschnitt 2.1.1 und 2.1.3",
     "befund": "Chronische Erkrankung ohne gesicherte ärztliche Betreuung bzw. "
               "Medikamentenversorgung am Einsatzort",
     "konsequenz": "Versorgungslage am Einsatzort VOR der Ausreise verbindlich klären; "
                   "keine Bedenken bestehen nur, wenn Betreuung und medikamentöse Versorgung "
                   "vor Ort gesichert sind und eine Verschlimmerung nicht wahrscheinlich "
                   "ist – andernfalls gesundheitliche Bedenken aussprechen."},
    {"wenn": {"akute_erkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Beurteilung",
     "quelle": "G 35 Abschnitt 2.1.2",
     "befund": "Akute bzw. vorübergehende Gesundheitsstörung",
     "konsequenz": "Befristete gesundheitliche Bedenken bis zur Wiederherstellung bzw. bis "
                   "zum Abschluss einer noch offenen Ergänzungsuntersuchung; danach erneut "
                   "beurteilen."},
    # ── Prophylaxe & Beratung ───────────────────────────────────────────────
    {"wenn": {"impfschutz": ["unvollstaendig", "unbekannt"]},
     "schwere": "pruefen",
     "bereich": "Impfschutz",
     "quelle": "G 35 Abschnitt 2.2",
     "befund": "Unvollständiger oder unbekannter Impfschutz",
     "konsequenz": "Impfstatus anhand des Impfausweises klären; Impfungen vor der Ausreise "
                   "vervollständigen; Beratung zu Impfungen und medikamentöser Prophylaxe."},
    {"wenn": {"malaria_prophylaxe": ["unregelmaessig", "nein"]},
     "schwere": "pruefen",
     "bereich": "Malariaprophylaxe",
     "quelle": "G 35 Abschnitt 2.2",
     "befund": "Empfohlene Malariaprophylaxe nicht oder nur unregelmäßig durchgeführt",
     "konsequenz": "Beratung zur medikamentösen Malariaprophylaxe und zum Mückenschutz "
                   "wiederholen; bei jedem unklaren Fieber unverzüglich Malariadiagnostik "
                   "veranlassen."},
    {"wenn": {"schwangerschaft": ["ja"]},
     "schwere": "pruefen",
     "bereich": "Schwangerschaft",
     "quelle": "G 35 Abschnitt 1.1",
     "befund": "Neu eingetretene bzw. bestehende Schwangerschaft",
     "konsequenz": "Vorzeitige Nachuntersuchung nach ärztlichem Ermessen; Beratung zu "
                   "besonderen Risiken (Malaria, Impfungen, medizinische Versorgung am "
                   "Einsatzort) und ggf. Anpassung der Einsatzplanung."},
    {"wenn": {"mitreisende": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Familie",
     "quelle": "G 35 Abschnitt 3.3",
     "befund": "Ehepartner/Kinder reisen mit ins Einsatzland",
     "konsequenz": "Aus medizinischer Sicht Beratung bzw. Untersuchung nach den Kriterien "
                   "des G 35 auch für mitreisende Ehepartner und Kinder empfehlen; "
                   "Kostenübernahme arbeitsvertraglich klären."},
]
