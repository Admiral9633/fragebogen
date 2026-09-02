# -*- coding: utf-8 -*-
"""G 37 Bildschirmarbeitsplätze – DGUV Grundsatz 2016. Quelle: DGUV Grundsätze für
arbeitsmedizinische Untersuchungen, 7. Auflage 2016 (Gentner Verlag), G 37
»Bildschirmarbeitsplätze« (Fassung Oktober 2014), S. 519–528."""

SLUG = "g37-bildschirm-2016"

CATALOG = {
    "version": 2,
    "title": "G 37 Bildschirmarbeitsplätze (DGUV Grundsatz 2016)",
    "basis": "DGUV Grundsätze für arbeitsmedizinische Untersuchungen, 7. Auflage 2016, "
             "G 37 »Bildschirmarbeitsplätze« (Fassung Oktober 2014), S. 519–528",
    "sections": [
        # ── 1 ─ Untersuchungsanlass (Abschnitt 1.1: Untersuchungsarten, Fristen)
        {
            "id": "untersuchung",
            "title": "Untersuchungsanlass",
            "subtitle": "Angaben zu Ihrer G-37-Untersuchung",
            "questions": [
                {
                    "id": "untersuchungsart",
                    "type": "choice",
                    "label": "Um welche Untersuchung handelt es sich?",
                    "required": True,
                    "options": [
                        {"value": "erst", "label": "Erstuntersuchung (vor Aufnahme der "
                                                   "Bildschirmtätigkeit)"},
                        {"value": "nach", "label": "Nachuntersuchung (ich war schon einmal "
                                                   "zur G-37-Untersuchung)"},
                    ],
                },
                {
                    "id": "alter_ueber40",
                    "type": "yes_no",
                    "label": "Sind Sie älter als 40 Jahre?",
                    "hint": "Das Alter bestimmt den empfohlenen Abstand zwischen den "
                            "Untersuchungen: bis 40 Jahre alle 60 Monate, über 40 Jahre "
                            "alle 36 Monate.",
                    "required": True,
                },
                {
                    "id": "letzte_untersuchung",
                    "type": "choice",
                    "label": "Wie lange liegt Ihre letzte G-37-Untersuchung "
                             "(Bildschirm-Sehtest) zurück?",
                    "required": True,
                    "show_if": {"id": "untersuchungsart", "in": ["nach"]},
                    "options": [
                        {"value": "unter36", "label": "Weniger als 36 Monate (3 Jahre)"},
                        {"value": "36bis60", "label": "36 bis 60 Monate (3 bis 5 Jahre)"},
                        {"value": "ueber60", "label": "Mehr als 60 Monate (5 Jahre)"},
                        {"value": "unbekannt", "label": "Weiß ich nicht"},
                    ],
                },
                {
                    "id": "beschwerden_zusammenhang",
                    "type": "yes_no",
                    "label": "Vermuten Sie einen Zusammenhang zwischen gesundheitlichen "
                             "Beschwerden und Ihrer Tätigkeit am Bildschirm?",
                    "hint": "In diesem Fall kann die Nachuntersuchung vorzeitig "
                            "durchgeführt werden.",
                    "required": True,
                    "followup": {"id": "beschwerden_zusammenhang_desc", "type": "textarea",
                                 "label": "Welche Beschwerden, und seit wann?", "when": "yes"},
                },
            ],
        },
        # ── 2 ─ Arbeitsplatz und Bildschirmarbeit (Arbeitsanamnese, 1.2.1) ──
        {
            "id": "taetigkeit",
            "title": "Arbeitsplatz & Bildschirmarbeit",
            "subtitle": "Ihre Arbeit am Bildschirm",
            "questions": [
                {
                    "id": "taetigkeit_beschreibung",
                    "type": "text",
                    "label": "Welche Tätigkeit üben Sie aus (Beruf, Arbeitsaufgabe)?",
                    "required": True,
                },
                {
                    "id": "bildschirm_dauer",
                    "type": "choice",
                    "label": "Wie viele Stunden arbeiten Sie an einem normalen Arbeitstag "
                             "am Bildschirm?",
                    "hint": "Beschwerden am Bewegungsapparat hängen direkt mit der Dauer "
                            "der Bildschirmtätigkeit zusammen.",
                    "required": True,
                    "options": [
                        {"value": "unter2", "label": "Weniger als 2 Stunden"},
                        {"value": "2bis4", "label": "2 bis 4 Stunden"},
                        {"value": "4bis6", "label": "4 bis 6 Stunden"},
                        {"value": "ueber6", "label": "Mehr als 6 Stunden"},
                    ],
                },
                {
                    "id": "geraete",
                    "type": "multi_choice",
                    "label": "Mit welchen Geräten und Medien erfüllen Sie Ihre "
                             "Arbeitsaufgaben? (Mehrfachauswahl möglich)",
                    "hint": "Bitte alles ankreuzen, was Sie beruflich regelmäßig nutzen.",
                    "required": True,
                    "options": [
                        {"value": "monitor", "label": "Fester Arbeitsplatz mit Bildschirm"},
                        {"value": "mehrere", "label": "Mehrere Bildschirme gleichzeitig"},
                        {"value": "notebook", "label": "Notebook/Laptop"},
                        {"value": "mobil", "label": "Smartphone oder Tablet"},
                        {"value": "3d", "label": "Dreidimensionale Darstellungen (3D)"},
                        {"value": "sonstige", "label": "Andere Geräte"},
                    ],
                },
                {
                    "id": "telearbeit",
                    "type": "yes_no",
                    "label": "Arbeiten Sie regelmäßig mobil oder von zu Hause aus "
                             "(Telearbeit/Heimarbeitsplatz)?",
                    "required": True,
                },
                {
                    "id": "einweisung",
                    "type": "yes_no",
                    "label": "Wurden Sie in die richtige Einstellung Ihres Arbeitsplatzes "
                             "eingewiesen (Stuhl, Tisch, Bildschirm)?",
                    "required": True,
                },
                {
                    "id": "ergonomie_probleme",
                    "type": "yes_no",
                    "label": "Gibt es an Ihrem Arbeitsplatz ergonomische Probleme (z. B. "
                             "ungünstige Beleuchtung, Spiegelungen, schlecht einstellbarer "
                             "Stuhl oder Tisch, unpraktische Software, Lärm)?",
                    "required": True,
                    "followup": {"id": "ergonomie_probleme_desc", "type": "textarea",
                                 "label": "Welche Probleme?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Sehvermögen und Augen (1.2.1, 1.2.2, 3.2) ────────────────────
        {
            "id": "sehen",
            "title": "Sehen & Augen",
            "subtitle": "Ihr Sehvermögen und Beschwerden an den Augen",
            "questions": [
                {
                    "id": "sehhilfe",
                    "type": "choice",
                    "label": "Tragen Sie eine Brille oder Kontaktlinsen?",
                    "hint": "Der Sehtest wird – wenn vorhanden – mit Ihrer Sehhilfe "
                            "durchgeführt. Bitte bringen Sie sie mit.",
                    "required": True,
                    "options": [
                        {"value": "keine", "label": "Nein"},
                        {"value": "ferne", "label": "Ja, Brille oder Kontaktlinsen für "
                                                    "die Ferne"},
                        {"value": "lese", "label": "Ja, eine Lesebrille (Alterssichtigkeit)"},
                        {"value": "gleitsicht", "label": "Ja, eine Gleitsicht- oder "
                                                         "Bifokalbrille"},
                        {"value": "bildschirmbrille", "label": "Ja, eine spezielle "
                                                               "Bildschirmbrille"},
                    ],
                },
                {
                    "id": "sehen_unscharf",
                    "type": "yes_no",
                    "label": "Haben Sie Schwierigkeiten, Texte oder Zeichen am Bildschirm "
                             "scharf zu erkennen – auch mit Ihrer Brille oder Ihren "
                             "Kontaktlinsen?",
                    "required": True,
                },
                {
                    "id": "augen_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach Bildschirmarbeit Beschwerden an den "
                             "Augen oder Kopfschmerzen?",
                    "required": True,
                },
                {
                    "id": "augen_symptome",
                    "type": "multi_choice",
                    "label": "Welche Beschwerden haben Sie? (Mehrfachauswahl möglich)",
                    "required": True,
                    "show_if": {"id": "augen_beschwerden", "in": ["yes"]},
                    "options": [
                        {"value": "brennen", "label": "Brennende oder tränende Augen"},
                        {"value": "kopfschmerz", "label": "Kopfschmerzen"},
                        {"value": "flimmern", "label": "Flimmern vor den Augen oder "
                                                       "verschwommenes Sehen"},
                        {"value": "doppel", "label": "Doppelbilder"},
                        {"value": "andere", "label": "Andere Beschwerden"},
                    ],
                },
                {
                    "id": "augenerkrankung",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Augenerkrankung bekannt (z. B. Grauer "
                             "oder Grüner Star, Netzhauterkrankung, Schielen)?",
                    "required": True,
                    "followup": {"id": "augenerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "sehbehinderung",
                    "type": "yes_no",
                    "label": "Besteht bei Ihnen eine deutliche Sehbehinderung, Blindheit "
                             "oder Einäugigkeit (Sehen nur mit einem Auge)?",
                    "hint": "Einäugigkeit oder Blindheit schließt Bildschirmarbeit "
                            "grundsätzlich nicht aus.",
                    "required": True,
                },
                {
                    "id": "farbsehen",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Farbsehschwäche bekannt (z. B. "
                             "Rot-Grün-Schwäche)?",
                    "required": True,
                },
            ],
        },
        # ── 4 ─ Bewegungsapparat (1.2.1, 3.3) ────────────────────────────────
        {
            "id": "bewegungsapparat",
            "title": "Muskeln & Gelenke",
            "subtitle": "Beschwerden am Bewegungsapparat",
            "questions": [
                {
                    "id": "msk_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei oder nach der Arbeit Beschwerden an Muskeln, "
                             "Gelenken oder der Wirbelsäule?",
                    "required": True,
                },
                {
                    "id": "msk_regionen",
                    "type": "multi_choice",
                    "label": "Wo haben Sie Beschwerden? (Mehrfachauswahl möglich)",
                    "required": True,
                    "show_if": {"id": "msk_beschwerden", "in": ["yes"]},
                    "options": [
                        {"value": "nacken", "label": "Nacken/Halswirbelsäule"},
                        {"value": "schulter", "label": "Schultergürtel/Schultern"},
                        {"value": "unterarm", "label": "Unterarme"},
                        {"value": "haende", "label": "Hände oder Handgelenke"},
                        {"value": "ruecken", "label": "Unterer Rücken/Lendenwirbelsäule"},
                        {"value": "andere", "label": "Andere Körperregion"},
                    ],
                },
                {
                    "id": "msk_vorerkrankung",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Erkrankung des Bewegungsapparates bekannt "
                             "(z. B. Bandscheibenvorfall, Arthrose, rheumatische "
                             "Erkrankung)?",
                    "required": True,
                    "followup": {"id": "msk_vorerkrankung_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "bewegungsmangel",
                    "type": "yes_no",
                    "label": "Bewegen Sie sich außerhalb der Arbeit regelmäßig (z. B. "
                             "Sport, Radfahren, zügiges Gehen)?",
                    "hint": "Bewegungsmangel ist eine der Ursachen für Beschwerden am "
                            "Bewegungssystem bei Bildschirmarbeit.",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Allgemeine Gesundheit (Allgemeine Anamnese, 1.2.1; 3.3) ──────
        {
            "id": "gesundheit",
            "title": "Allgemeine Gesundheit",
            "subtitle": "Vorerkrankungen und Medikamente",
            "questions": [
                {
                    "id": "neuro",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine neurologische Erkrankung bekannt "
                             "(Erkrankung des Nervensystems, z. B. Migräne, Epilepsie, "
                             "Lähmungen, Missempfindungen)?",
                    "required": True,
                    "followup": {"id": "neuro_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "stoffwechsel",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen eine Stoffwechselerkrankung bekannt (z. B. "
                             "Diabetes/Zuckerkrankheit, Schilddrüsenerkrankung)?",
                    "required": True,
                    "followup": {"id": "stoffwechsel_desc", "type": "text",
                                 "label": "Welche Erkrankung?", "when": "yes"},
                },
                {
                    "id": "blutdruck",
                    "type": "yes_no",
                    "label": "Ist bei Ihnen Bluthochdruck bekannt?",
                    "required": True,
                },
                {
                    "id": "med_dauer",
                    "type": "yes_no",
                    "label": "Nehmen Sie dauerhaft Medikamente ein?",
                    "required": True,
                    "followup": {"id": "med_dauer_desc", "type": "text",
                                 "label": "Welche Medikamente?", "when": "yes"},
                },
                {
                    "id": "psych_belastung",
                    "type": "yes_no",
                    "label": "Fühlen Sie sich durch Ihre Bildschirmarbeit psychisch stark "
                             "belastet (z. B. Zeitdruck, viele Aufgaben gleichzeitig, "
                             "eintönige Arbeit, ständige Erreichbarkeit, Alleinarbeit)?",
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
    # ── Fristen (Abschnitt 1.1) ───────────────────────────────────────────
    {"wenn": {"alter_ueber40": ["yes"], "letzte_untersuchung": ["36bis60", "ueber60"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Person über 40 Jahre, letzte G-37-Untersuchung liegt mehr als 36 Monate "
               "zurück.",
     "konsequenz": "Nachuntersuchungsfrist überschritten (über 40 Jahre: 36 Monate): "
                   "Nachuntersuchung jetzt vollständig durchführen (allgemeine und "
                   "spezielle Untersuchung) und den nächsten Termin nach der "
                   "36-Monats-Frist planen; in begründeten Einzelfällen individuelle "
                   "Verkürzung."},
    {"wenn": {"alter_ueber40": ["no"], "letzte_untersuchung": ["ueber60"]},
     "schwere": "pruefen",
     "bereich": "Nachuntersuchungsfrist",
     "quelle": "Abschnitt 1.1 (Untersuchungsarten, Fristen)",
     "befund": "Person bis 40 Jahre, letzte G-37-Untersuchung liegt mehr als 60 Monate "
               "zurück.",
     "konsequenz": "Nachuntersuchungsfrist überschritten (bis 40 Jahre: 60 Monate): "
                   "Nachuntersuchung jetzt vollständig durchführen und den nächsten "
                   "Termin fristgerecht planen."},
    {"wenn": {"beschwerden_zusammenhang": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Vorzeitige Nachuntersuchung",
     "quelle": "Abschnitt 1.1 (vorzeitige Nachuntersuchung)",
     "befund": "Vermuteter Zusammenhang zwischen Beschwerden und der Tätigkeit am "
               "Bildschirmarbeitsplatz.",
     "konsequenz": "Vorzeitige Nachuntersuchung ist ausdrücklich vorgesehen bei "
                   "Beschäftigten, die einen ursächlichen Zusammenhang zwischen "
                   "Erkrankung und Tätigkeit vermuten: Beschwerden gezielt abklären "
                   "(allgemeine und spezielle Untersuchung), Arbeitsplatzverhältnisse "
                   "einbeziehen."},
    # ── Sehvermögen (Abschnitte 1.2.2, 1.2.3, 2.1.3, 3.2, 3.4) ────────────
    {"wenn": {"sehen_unscharf": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehvermögen",
     "quelle": "Abschnitte 1.2.2 und 1.2.3; Tabelle 1",
     "befund": "Schwierigkeiten, Zeichen am Bildschirm scharf zu erkennen (auch mit "
               "Sehhilfe).",
     "konsequenz": "Spezielle Untersuchung durchführen und gegen die Mindestanforderungen "
                   "prüfen: Sehschärfe Ferne 0,8/0,8, Sehschärfe Nähe "
                   "arbeitsplatzbezogen 0,8/0,8, beidäugig 0,8, zentrales Gesichtsfeld "
                   "und Farbsinn regelrecht (Verfahren nach DIN 58220 Teil 5). Bei "
                   "Auffälligkeiten Maßnahmen zur Verbesserung der Sehschärfe, ggf. "
                   "spezielle Sehhilfe (Bildschirmbrille); werden die "
                   "Mindestanforderungen weiterhin nicht erfüllt, augenärztliche "
                   "Untersuchung ermöglichen (1.2.3)."},
    {"wenn": {"augen_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Asthenopische Beschwerden",
     "quelle": "Abschnitte 1.1, 1.2.2 und 3.3",
     "befund": "Augenbeschwerden oder Kopfschmerzen bei bzw. nach Bildschirmarbeit.",
     "konsequenz": "Asthenopische Beschwerden abklären: spezielle Untersuchung "
                   "(Sehschärfe Ferne und Nähe arbeitsplatzbezogen, Phorie, zentrales "
                   "Gesichtsfeld, Farbsinn); ergonomische Gestaltung des Arbeitsplatzes "
                   "mitprüfen (Ausleuchtung, Kontrast, Abstände, Blickwinkel). "
                   "Arbeitsplatzbezogene Beschwerden sind zugleich Anlass für eine "
                   "vorzeitige Nachuntersuchung."},
    {"wenn": {"augen_symptome": ["doppel"]},
     "schwere": "pruefen",
     "bereich": "Binokulares Sehen",
     "quelle": "Abschnitte 1.2.2 und 3.2",
     "befund": "Doppelbilder bei Bildschirmarbeit angegeben.",
     "konsequenz": "Phorie (mögliche Fehlstellung der Augen) mit Testgeräten prüfen; das "
                   "binokulare Sehen ist für Bildschirmarbeit entscheidend. Bei "
                   "fortbestehenden Auffälligkeiten und Klärungsbedarf augenärztliche "
                   "Untersuchung ermöglichen (1.2.3)."},
    {"wenn": {"augenerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Augenerkrankung",
     "quelle": "Abschnitte 1.2.3 und 2.1.3",
     "befund": "Bekannte Augenerkrankung angegeben.",
     "konsequenz": "Vorbefunde einbeziehen, spezielle Untersuchung durchführen; bei "
                   "Klärungsbedarf oder möglichen Auswirkungen auf die weitere Tätigkeit "
                   "augenärztliche Untersuchung ermöglichen. In Einzelfällen verkürzte "
                   "Untersuchungsintervalle empfehlen (2.1.3)."},
    {"wenn": {"sehbehinderung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Sehbehinderung/Blindheit",
     "quelle": "Abschnitte 2.1, 2.1.3 und 3.2",
     "befund": "Deutliche Sehbehinderung, Blindheit oder Einäugigkeit angegeben.",
     "konsequenz": "Einäugigkeit oder Blindheit schließt Bildschirmarbeit grundsätzlich "
                   "nicht aus. Beurteilung in Zusammenarbeit mit einem "
                   "Rehabilitationszentrum für Blinde und Sehbehinderte oder einer "
                   "entsprechenden Einrichtung; Hilfsmittel prüfen (Lupenfunktion, "
                   "Vorlesefunktion, Brailledisplay) und dem Arbeitgeber Vorschläge zur "
                   "Arbeitsplatzgestaltung mitteilen."},
    {"wenn": {"farbsehen": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Farbsinn",
     "quelle": "Abschnitt 1.2.2; Tabellen 1 und 2",
     "befund": "Bekannte Farbsehschwäche angegeben.",
     "konsequenz": "Farbsinnprüfung (Farbentafeln z. B. nach Ishihara oder Testgeräte); "
                   "Mindestanforderung ist ein regelrechter Farbsinn. Abgleich mit der "
                   "Arbeitsaufgabe; bei Arbeitsaufgaben mit besonderen Anforderungen an "
                   "das Sehvermögen können zusätzliche Untersuchungen erforderlich "
                   "werden."},
    {"wenn": {"sehhilfe": ["lese", "gleitsicht"]},
     "schwere": "hinweis",
     "bereich": "Alterssichtigkeit/Bildschirmbrille",
     "quelle": "Abschnitte 3.2 und 3.4",
     "befund": "Alterssichtigkeit (Lese-/Gleitsichtkorrektur) angegeben.",
     "konsequenz": "Reduzierte Akkommodationsbreite und Schwächen im Kontrastsehen bei "
                   "der Beurteilung und Beratung berücksichtigen. Ist eine spezielle "
                   "arbeitsplatzbezogene Korrektur erforderlich, Bildschirmbrille "
                   "entsprechend den durch den Arbeitsplatz vorgegebenen Sehabständen "
                   "und Blickrichtungen verordnen (3.4)."},
    # ── Bewegungsapparat (Abschnitte 1.2.1, 2.1.3, 3.3) ───────────────────
    {"wenn": {"msk_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bewegungsapparat",
     "quelle": "Abschnitte 1.2.1, 2.1.3 und 3.3",
     "befund": "Beschwerden an Muskeln, Gelenken oder Wirbelsäule bei bzw. nach der "
               "Arbeit.",
     "konsequenz": "Ursachen prüfen: unzureichende Ergonomie, Vorerkrankungen, "
                   "Bewegungsmangel; auch unzureichendes Sehvermögen als Mitursache "
                   "(Ausgleichsbewegungen, Fehlhaltung) abklären – daher Sehtest "
                   "durchführen. Ausgleich durch technische oder organisatorische "
                   "Maßnahmen bzw. ärztliche Therapie schaffen; Vorschläge für die "
                   "Änderung der Arbeitsplatzverhältnisse dem Arbeitgeber mitteilen."},
    {"wenn": {"msk_vorerkrankung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Bewegungsapparat",
     "quelle": "Abschnitte 2.1.3 und 3.3",
     "befund": "Bekannte Erkrankung des Bewegungsapparates angegeben.",
     "konsequenz": "Bestehende Vorerkrankungen sind eine Ursache für Beschwerden bei "
                   "Bildschirmarbeit: ergonomische Arbeitsplatzgestaltung prüfen, "
                   "ärztliche Therapie sicherstellen; in Einzelfällen verkürzte "
                   "Untersuchungsintervalle empfehlen (2.1.3)."},
    # ── Psychische Belastung, Ergonomie, Organisation (2.2, 3.3) ──────────
    {"wenn": {"psych_belastung": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Psychische Belastung",
     "quelle": "Abschnitte 2.2 und 3.3",
     "befund": "Starke psychische Belastung durch die Bildschirmarbeit angegeben.",
     "konsequenz": "Mögliche psychische Fehl-Beanspruchung (Monotonie, psychische "
                   "Sättigung, Ermüdung) durch Arbeitsverdichtung, Multitasking, "
                   "permanente Erreichbarkeit oder fehlende soziale Einbindung "
                   "(Telearbeit) abklären; Beratung zur Arbeitsorganisation "
                   "(Zeitvorgaben, Unterbrechungen) und ggf. organisatorische "
                   "Maßnahmen im Rahmen der Arbeitsgestaltung anregen."},
    {"wenn": {"ergonomie_probleme": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Ergonomie",
     "quelle": "Abschnitte 2.1.3, 3.2 und 3.3; DGUV Information 215-410",
     "befund": "Ergonomische Probleme am Bildschirmarbeitsplatz angegeben.",
     "konsequenz": "Beratung zur Gestaltung des Bildschirmarbeitsplatzes (Körperhaltung, "
                   "Blickwinkel, Abstände, Ausleuchtung, Kontrast; DGUV Information "
                   "215-410); Vorschläge für die Änderung der Arbeitsplatzverhältnisse "
                   "dem Arbeitgeber mitteilen."},
    {"wenn": {"einweisung": ["no"]},
     "schwere": "hinweis",
     "bereich": "Arbeitseinweisung",
     "quelle": "Abschnitt 1.2.1 (Arbeitsanamnese)",
     "befund": "Keine Einweisung in die ergonomische Einstellung des Arbeitsplatzes "
               "erfolgt.",
     "konsequenz": "Einweisung in die richtige Einstellung von Stuhl, Tisch und "
                   "Bildschirm veranlassen; Arbeitgeber auf die fehlende "
                   "Arbeitseinweisung hinweisen."},
    {"wenn": {"geraete": ["mobil"]},
     "schwere": "hinweis",
     "bereich": "Mobile Endgeräte",
     "quelle": "Abschnitt 2.2 (Beratung)",
     "befund": "Regelmäßige berufliche Nutzung von Smartphone oder Tablet.",
     "konsequenz": "In der Arbeitsanamnese konkret erfragen, welche Geräte bzw. Medien "
                   "in welcher Form und in welchem Umfang genutzt werden; Belastungen "
                   "und Beanspruchungen mobiler IKT-gestützter Arbeit erfassen und "
                   "bewerten; Beratung zu Ergonomie, Arbeitsgestaltung und speziellen "
                   "Sehhilfen."},
    # ── Allgemeine Gesundheit (1.2.1, 2.1.3) ──────────────────────────────
    {"wenn": {"stoffwechsel": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Stoffwechselerkrankung",
     "quelle": "Abschnitte 1.2.1 und 2.1.3",
     "befund": "Stoffwechselerkrankung (z. B. Diabetes) angegeben.",
     "konsequenz": "Bei der Beurteilung berücksichtigen (mögliche Auswirkungen auf das "
                   "Sehvermögen); Behandlungsstand klären, ärztliche Therapie als "
                   "Ausgleich sicherstellen; in Einzelfällen verkürzte "
                   "Untersuchungsintervalle empfehlen."},
    {"wenn": {"neuro": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Neurologische Störung",
     "quelle": "Abschnitte 1.2.1 und 2.1.3",
     "befund": "Neurologische Erkrankung angegeben.",
     "konsequenz": "Anamnese vertiefen und Auswirkungen auf Wahrnehmung und "
                   "Bildschirmtätigkeit prüfen; Ausgleich durch technische oder "
                   "organisatorische Maßnahmen bzw. ärztliche Therapie schaffen "
                   "(2.1.3)."},
    {"wenn": {"med_dauer": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Medikamente",
     "quelle": "Abschnitt 1.2.1 (Allgemeine Anamnese)",
     "befund": "Dauerbehandlung mit Medikamenten angegeben.",
     "konsequenz": "Dauermedikation bei der Beurteilung berücksichtigen (mögliche "
                   "Wirkungen auf Sehvermögen und Konzentrationsfähigkeit); "
                   "Medikamentenanamnese ärztlich vertiefen."},
    {"wenn": {"blutdruck": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Bluthochdruck",
     "quelle": "Abschnitt 1.2.1 (Allgemeine Anamnese)",
     "befund": "Bluthochdruck angegeben.",
     "konsequenz": "Behandlungsstand klären (Bluthochdruck kann Augenveränderungen "
                   "verursachen); ärztliche Therapie sicherstellen und bei der "
                   "Beurteilung berücksichtigen."},
]
