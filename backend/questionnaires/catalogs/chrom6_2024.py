# -*- coding: utf-8 -*-
"""Chrom(VI)-Verbindungen – DGUV Empfehlung 2024. Quelle: DGUV Empfehlungen für
arbeitsmedizinische Beratungen und Untersuchungen, 1. Auflage 2024,
»Chrom(VI)-Verbindungen« (E CR6, Fassung Januar 2022), S. 207–227."""

SLUG = "chrom6-2024"

CATALOG = {
    "version": 2,
    "title": "Chrom(VI)-Verbindungen (DGUV Empfehlung 2024)",
    "basis": "DGUV Empfehlungen für arbeitsmedizinische Beratungen und Untersuchungen, "
             "1. Auflage 2024, »Chrom(VI)-Verbindungen« (E CR6, Fassung Januar 2022), "
             "S. 207–227",
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
                    "label": "Um welche Vorsorge handelt es sich heute?",
                    "hint": "Chrom(VI)-Verbindungen sind krebserzeugend. Deshalb gibt es auch "
                            "nach dem Ende der Tätigkeit weiter Vorsorge (nachgehende Vorsorge).",
                    "required": True,
                    "options": [
                        {"value": "erste", "label": "Erste Vorsorge wegen Chrom(VI)-Verbindungen"},
                        {"value": "weitere", "label": "Weitere Vorsorge (ich war schon einmal hier)"},
                        {"value": "nachgehend", "label": "Nachgehende Vorsorge (Tätigkeit ist beendet)"},
                    ],
                },
                {
                    "id": "vorsorge_anlass",
                    "type": "choice",
                    "label": "Wie kam dieser Termin zustande?",
                    "hint": "Pflichtvorsorge: Ihr Betrieb muss sie veranlassen, wenn eine "
                            "wiederholte Belastung mit Chrom(VI)-Verbindungen oder eine Gefährdung "
                            "durch Hautkontakt nicht ausgeschlossen werden kann.",
                    "required": True,
                    "show_if": {"id": "vorsorge_art", "not_in": ["nachgehend"]},
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
            "title": "Tätigkeit & Chrom-Belastung",
            "subtitle": "Ihre Arbeit mit Chrom(VI)-Verbindungen",
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
                    "label": "Welche dieser Arbeiten führen Sie durch?",
                    "hint": "Bei diesen Arbeiten ist mit einer Belastung durch Chrom(VI)-"
                            "Verbindungen zu rechnen. Mehrfachauswahl möglich.",
                    "required": True,
                    "options": [
                        {"value": "galvanik", "label": "Galvanik / Hartverchromen (z. B. an offenen Bädern)"},
                        {"value": "schweissen_schneiden", "label": "Schweißen oder thermisches Schneiden von "
                                                                   "Chrom-Nickel-Stahl (Edelstahl)"},
                        {"value": "enge_raeume", "label": "Schweißen in engen Räumen (z. B. Tanks, Kessel, "
                                                          "Behälter, Schächte, Rohrleitungen)"},
                        {"value": "thermisch_spritzen", "label": "Thermisches Spritzen (Flamm-, Lichtbogen-, "
                                                                 "Plasmaspritzen) mit chromhaltigen Werkstoffen"},
                        {"value": "anstriche", "label": "Spritzlackieren mit chromathaltigen Farben oder "
                                                        "Entfernen/Abschleifen chromathaltiger Anstriche"},
                        {"value": "herstellen", "label": "Herstellen oder Verarbeiten von Chrom(VI)-Verbindungen "
                                                         "(auch Wartung, Reinigung, Instandhaltung)"},
                        {"value": "abbruch", "label": "Abbrucharbeiten an Anlagen, in denen Chrom(VI)-"
                                                      "Verbindungen hergestellt wurden"},
                        {"value": "holzschutz", "label": "Imprägnieren von Holz mit chromhaltigen "
                                                         "Holzschutzmitteln (Kesseldruckanlagen)"},
                        {"value": "sonstige", "label": "Andere Arbeiten mit Chrom(VI)-Verbindungen"},
                        {"value": "keine", "label": "Keine davon / weiß ich nicht"},
                    ],
                },
                {
                    "id": "bleichromat",
                    "type": "yes_no",
                    "label": "Arbeiten Sie mit Bleichromat oder Bleidichromat (bleihaltige "
                             "gelbe/rote Chrompigmente, z. B. in alten Farben)?",
                    "required": True,
                },
                {
                    "id": "expo_dauer",
                    "type": "choice",
                    "label": "Wie lange arbeiten Sie insgesamt schon mit möglichem Kontakt zu "
                             "Chrom(VI)-Verbindungen?",
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
                    "id": "vorexposition",
                    "type": "yes_no",
                    "label": "Hatten Sie in früheren Tätigkeiten Kontakt zu Chrom(VI)-Verbindungen "
                             "oder anderen krebserzeugenden Gefahrstoffen?",
                    "required": True,
                    "followup": {"id": "vorexposition_desc", "type": "textarea",
                                 "label": "Welche Tätigkeiten und Stoffe, und wie lange?", "when": "yes"},
                },
                {
                    "id": "zwischenfaelle",
                    "type": "yes_no",
                    "label": "Gab es bei Ihrer Arbeit Unfälle, Zwischenfälle oder ungewöhnliche "
                             "Betriebszustände mit besonders hoher Chrom-Belastung (z. B. "
                             "Verschütten, Absaugung ausgefallen)?",
                    "required": True,
                    "followup": {"id": "zwischenfaelle_desc", "type": "textarea",
                                 "label": "Was ist passiert, und wann?", "when": "yes"},
                },
            ],
        },
        # ── 3 ─ Schutzmaßnahmen ────────────────────────────────────────────
        {
            "id": "schutz",
            "title": "Schutzmaßnahmen & Hygiene",
            "subtitle": "Atemschutz, Handschuhe und Hygiene am Arbeitsplatz",
            "questions": [
                {
                    "id": "atemschutz",
                    "type": "choice",
                    "label": "Tragen Sie bei Arbeiten mit Chrom-Belastung Atemschutz?",
                    "required": True,
                    "options": [
                        {"value": "immer", "label": "Ja, immer"},
                        {"value": "meist", "label": "Meistens"},
                        {"value": "selten", "label": "Nur selten"},
                        {"value": "nie", "label": "Nein, nie"},
                        {"value": "nicht_noetig", "label": "Für meine Tätigkeit nicht vorgesehen"},
                    ],
                },
                {
                    "id": "handschuhe",
                    "type": "choice",
                    "label": "Tragen Sie bei möglichem Hautkontakt geeignete Schutzhandschuhe?",
                    "hint": "Lösliche Chrom(VI)-Verbindungen können über die Haut aufgenommen "
                            "werden und Allergien auslösen.",
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
                    "id": "hautkontakt",
                    "type": "yes_no",
                    "label": "Kommt Ihre Haut bei der Arbeit trotzdem direkt mit chromhaltigen "
                             "Flüssigkeiten, Stäuben oder Nebeln in Kontakt?",
                    "required": True,
                },
                {
                    "id": "hygiene",
                    "type": "yes_no",
                    "label": "Können Sie die Hygieneregeln am Arbeitsplatz einhalten (nicht essen/"
                             "trinken/rauchen im Arbeitsbereich, Hände reinigen, Arbeitskleidung "
                             "getrennt aufbewahren und wechseln)?",
                    "required": True,
                    "followup": {"id": "hygiene_desc", "type": "text",
                                 "label": "Was funktioniert nicht?", "when": "no"},
                },
            ],
        },
        # ── 4 ─ Beschwerden ────────────────────────────────────────────────
        {
            "id": "beschwerden",
            "title": "Aktuelle Beschwerden",
            "subtitle": "Nase, Atemwege, Haut und Augen",
            "questions": [
                {
                    "id": "nase_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Beschwerden an der Nase: häufiges Nasenbluten, Borken/"
                             "Krusten, ständig laufende Nase oder wunde Stellen in der Nase?",
                    "hint": "Chrom(VI)-Verbindungen können die Nasenscheidewand schädigen – oft "
                            "ohne Schmerzen.",
                    "required": True,
                    "followup": {"id": "nase_beschwerden_desc", "type": "text",
                                 "label": "Welche Beschwerden, seit wann?", "when": "yes"},
                },
                {
                    "id": "atemwege_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Husten, Auswurf, Heiserkeit, pfeifende Atmung oder Atemnot?",
                    "required": True,
                    "followup": {"id": "atemwege_beschwerden_desc", "type": "text",
                                 "label": "Welche Beschwerden, seit wann?", "when": "yes"},
                },
                {
                    "id": "haut_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie Hautbeschwerden: Rötung, Juckreiz, Ausschlag oder Ekzem "
                             "(entzündete, nässende oder schuppende Haut), besonders an den Händen?",
                    "required": True,
                    "followup": {"id": "haut_beschwerden_desc", "type": "text",
                                 "label": "Wo, und seit wann?", "when": "yes"},
                },
                {
                    "id": "haut_wunden",
                    "type": "yes_no",
                    "label": "Haben Sie schlecht heilende Wunden, kleine Geschwüre oder tiefe, "
                             "schmerzhafte Hautrisse (Rhagaden), z. B. an Händen oder Unterarmen?",
                    "required": True,
                },
                {
                    "id": "augen_beschwerden",
                    "type": "yes_no",
                    "label": "Haben Sie bei der Arbeit gereizte Augen (Brennen, Tränen, Rötung)?",
                    "required": True,
                },
            ],
        },
        # ── 5 ─ Vorerkrankungen ────────────────────────────────────────────
        {
            "id": "vorerkrankungen",
            "title": "Vorerkrankungen & Allergien",
            "subtitle": "Frühere und bestehende Erkrankungen",
            "questions": [
                {
                    "id": "vorerkr_atemwege",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie Erkrankungen der Atemwege oder der Lunge "
                             "(z. B. chronische Bronchitis, Asthma, COPD, Lungenentzündungen, "
                             "Erkrankungen des Rippenfells)?",
                    "required": True,
                    "followup": {"id": "vorerkr_atemwege_desc", "type": "textarea",
                                 "label": "Welche Erkrankung, seit wann, in Behandlung?", "when": "yes"},
                },
                {
                    "id": "vorerkr_nnh",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie chronische Entzündungen, Polypen oder andere "
                             "Erkrankungen der Nasennebenhöhlen oder des Rachens?",
                    "required": True,
                    "followup": {"id": "vorerkr_nnh_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "vorerkr_haut",
                    "type": "yes_no",
                    "label": "Haben oder hatten Sie eine chronische Hauterkrankung (z. B. "
                             "chronisches Ekzem, Neurodermitis, sehr trockene rissige Haut)?",
                    "required": True,
                    "followup": {"id": "vorerkr_haut_desc", "type": "text",
                                 "label": "Welche Erkrankung, seit wann?", "when": "yes"},
                },
                {
                    "id": "allergie",
                    "type": "yes_no",
                    "label": "Haben Sie Allergien, insbesondere eine Kontaktallergie gegen Chromat "
                             "(z. B. »Zementekzem«) oder wiederkehrende allergische Beschwerden?",
                    "required": True,
                    "followup": {"id": "allergie_desc", "type": "text",
                                 "label": "Welche Allergien?", "when": "yes"},
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
                    "id": "allgemein_erkrankungen",
                    "type": "yes_no",
                    "label": "Haben Sie sonstige Erkrankungen oder gesundheitliche Einschränkungen, "
                             "die hier noch nicht genannt wurden?",
                    "required": True,
                    "followup": {"id": "allgemein_erkrankungen_desc", "type": "textarea",
                                 "label": "Welche?", "when": "yes"},
                },
            ],
        },
        # ── 6 ─ Rauchen und besondere Situationen ──────────────────────────
        {
            "id": "weitere_angaben",
            "title": "Rauchen & besondere Situationen",
            "subtitle": "Weitere Angaben, die für die Beratung wichtig sind",
            "questions": [
                {
                    "id": "rauchen",
                    "type": "choice",
                    "label": "Rauchen Sie?",
                    "hint": "Rauchen und Chrom(VI)-Belastung können sich in ihrer "
                            "krebserzeugenden Wirkung gegenseitig verstärken.",
                    "required": True,
                    "options": [
                        {"value": "ja", "label": "Ja"},
                        {"value": "frueher", "label": "Früher, jetzt nicht mehr"},
                        {"value": "nie", "label": "Nein, nie"},
                    ],
                },
                {
                    "id": "personengruppe",
                    "type": "choice",
                    "label": "Trifft eine der folgenden Angaben auf Sie zu?",
                    "hint": "Für Schwangere, Stillende und Jugendliche gelten besondere "
                            "Beschäftigungsbeschränkungen (Mutterschutzgesetz, "
                            "Jugendarbeitsschutzgesetz).",
                    "required": True,
                    "options": [
                        {"value": "schwanger", "label": "Ich bin schwanger"},
                        {"value": "stillend", "label": "Ich stille"},
                        {"value": "unter18", "label": "Ich bin unter 18 Jahre alt"},
                        {"value": "nein", "label": "Nichts davon"},
                        {"value": "keine_angabe", "label": "Keine Angabe"},
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
    # ── Beurteilungsrelevante Erkrankungen (Abschnitt 7.4) ────────────────
    {"wenn": {"vorerkr_nnh": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nasennebenhöhlen/Rachen",
     "quelle": "Abschnitte 7.4, 7.4.2, 7.4.3 und 7.2.2",
     "befund": "Chronische Erkrankung der Nasennebenhöhlen oder des Rachens angegeben.",
     "konsequenz": "Beurteilungsrelevante Erkrankung nach 7.4: Ausmaß ärztlich klären, in "
                   "unklaren Fällen HNO-ärztliche Untersuchung veranlassen. Maßnahmen nach "
                   "7.4.2 prüfen (Substitution, technische/organisatorische Schutzmaßnahmen, "
                   "expositionsärmerer Einsatz, PSA); bei zu erwartender Änderung des "
                   "Schweregrads verkürzte Vorsorgefrist nach 7.4.3."},
    {"wenn": {"vorerkr_atemwege": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege/Lunge",
     "quelle": "Abschnitte 7.4, 7.4.2–7.4.4 und 7.2.2",
     "befund": "Erkrankung der Atemwege, der Lunge oder des Rippenfells in der Vorgeschichte.",
     "konsequenz": "Spirometrie-Befund besonders gewichten; in unklaren Fällen pulmologische "
                   "Abklärung veranlassen. Maßnahmen nach 7.4.2 und ggf. verkürzte Frist nach "
                   "7.4.3 prüfen; bleiben Maßnahmen ohne Erfolg, Tätigkeitswechsel nach 7.4.4 "
                   "erwägen (Mitteilung an den Arbeitgeber nur mit Einwilligung, § 6 (4) ArbMedVV)."},
    {"wenn": {"vorerkr_haut": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 7.4, 7.4.2, 7.4.3 und 7.2.2",
     "befund": "Chronische Hauterkrankung (z. B. chronisches Ekzem, starke Rhagadenbildung) "
               "angegeben.",
     "konsequenz": "Hautuntersuchung (Ekzeme, Rhagaden, allergische Manifestationen, schlecht "
                   "heilende Wunden); Maßnahmen nach 7.4.2 prüfen (insb. Vermeiden von "
                   "Hautkontakt, geeignete Schutzhandschuhe, Hautschutz), verkürzte Frist nach "
                   "7.4.3 erwägen. Bei bloßer Spuren-Exposition stattdessen DGUV Empfehlung "
                   "»Gefährdung der Haut« anwenden."},
    {"wenn": {"allergie": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Allergie",
     "quelle": "Abschnitte 6.3, 7.4 und 7.4.2–7.4.4",
     "befund": "Allergie bzw. rezidivierende allergische Manifestationen angegeben "
               "(ggf. Chromat-Kontaktallergie).",
     "konsequenz": "Rezidivierende allergische Manifestationen sind beurteilungsrelevant (7.4): "
                   "allergologisch-dermatologische Abklärung erwägen, besondere Rezidivneigung "
                   "des Chromatekzems beachten. Maßnahmen nach 7.4.2 prüfen; bei Erfolglosigkeit "
                   "Tätigkeitswechsel nach 7.4.4 erwägen."},
    {"wenn": {"haut_wunden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3.2, 6.3.3, 6.5 und 7.4",
     "befund": "Schlecht heilende Wunden, Geschwüre oder tiefe Rhagaden angegeben.",
     "konsequenz": "Auf chromattypische, schlecht heilende »Chromatgeschwüre« untersuchen; "
                   "schlecht heilende Wunden und starke Rhagadenbildung sind "
                   "beurteilungsrelevant (7.4). Behandlung einleiten, Hautkontakt unterbinden; "
                   "BK-Anzeige prüfen (BK-Nr. 1103, bei Hauterkrankung BK-Nr. 5101)."},
    # ── Zielorgan-Beschwerden (Abschnitte 6.3 und 7.1/7.2.2) ──────────────
    {"wenn": {"nase_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Nase",
     "quelle": "Abschnitte 6.3.3, 7.1 und 7.2.2",
     "befund": "Nasenbluten, Borkenbildung, Sekretabsonderung oder wunde Stellen der Nase "
               "angegeben.",
     "konsequenz": "Spekulumuntersuchung der Nase durchführen (Indikation z. B. "
                   "Aerosolbelastung); auf Septumveränderungen der Stadien A–C (Rötung, "
                   "Ulzeration, Perforation) achten. In unklaren Fällen HNO-ärztliche "
                   "Untersuchung. Hinweis auf mögliche unzureichende Schutzmaßnahmen: "
                   "Gefährdungsbeurteilung überprüfen lassen, Mitteilung nach § 6 (4) ArbMedVV."},
    {"wenn": {"atemwege_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Atemwege",
     "quelle": "Abschnitte 6.3.3, 7.1 und 7.2.2",
     "befund": "Husten, Heiserkeit, Auswurf oder Atemnot angegeben.",
     "konsequenz": "Spirometrie-Ergebnis besonders gewichten (Leitfaden "
                   "»Lungenfunktionsprüfung«); an chronische Bronchitis, spastische Komponente "
                   "und Bronchialasthma denken. In unklaren Fällen pulmologische Abklärung "
                   "veranlassen; Abgleich mit der Gefährdungsbeurteilung."},
    {"wenn": {"haut_beschwerden": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Haut",
     "quelle": "Abschnitte 6.3.2, 6.3.3 und 7.2.2",
     "befund": "Hautrötung, Juckreiz, Ausschlag oder Ekzem angegeben.",
     "konsequenz": "Untersuchung der Haut (Ekzeme, Rhagaden, allergische Manifestationen); an "
                   "allergisches Kontaktekzem durch Chromat denken (besondere Rezidivneigung). "
                   "Beratung zu Hautschutz und Schutzhandschuhen; bei Verdacht auf "
                   "Berufsdermatose BK-Anzeige (BK-Nr. 5101) prüfen."},
    {"wenn": {"augen_beschwerden": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Augen",
     "quelle": "Abschnitt 6.3.2",
     "befund": "Augenreizung (Brennen, Tränen, Rötung) bei der Arbeit angegeben.",
     "konsequenz": "Hinweis auf akute Reizwirkung von Chromat-Stäuben/-Dämpfen "
                   "(Konjunktivitis, Hornhautschäden möglich): Exposition und Augenschutz "
                   "prüfen, Überprüfung der Gefährdungsbeurteilung anregen; bei anhaltenden "
                   "Beschwerden augenärztliche Vorstellung empfehlen."},
    # ── Biomonitoring und Exposition (Abschnitte 6.4 und 7.2.2) ───────────
    {"wenn": {"vorexposition": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Biomonitoring",
     "quelle": "Abschnitte 6.4 und 7.2.2 (Erstuntersuchung)",
     "befund": "Frühere Exposition gegenüber Chrom(VI)-Verbindungen oder vergleichbaren "
               "Gefahrstoffen angegeben.",
     "konsequenz": "Bei der Erstuntersuchung Biomonitoring als Basiswert durchführen: "
                   "Chrombestimmung in Urin und in der Erythrozytenfraktion des Vollbluts. "
                   "Bewertung über EKA-Korrelation (Alkalichromate) bzw. BAR Gesamt-Chrom "
                   "0,6 µg/l Urin; über Art, Umfang und Ablauf des Biomonitorings aufklären."},
    {"wenn": {"zwischenfaelle": ["yes"]},
     "schwere": "pruefen",
     "bereich": "Exposition",
     "quelle": "Abschnitte 7.1 und 6.4",
     "befund": "Unfall, Zwischenfall oder ungewöhnlicher Betriebszustand mit erhöhter "
               "Exposition angegeben.",
     "konsequenz": "Ereignis dokumentieren (7.1); Biomonitoring veranlassen (Chrom in Urin "
                   "und Erythrozyten, Bewertung über EKA-Korrelation). Ergeben sich Hinweise "
                   "auf unzureichende Schutzmaßnahmen, Mitteilung an das Unternehmen und "
                   "Vorschlag von Maßnahmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"expo_taetigkeiten": ["schweissen_schneiden", "enge_raeume", "thermisch_spritzen"]},
     "schwere": "hinweis",
     "bereich": "Schweißrauche",
     "quelle": "Abschnitte 6.1.1 und 6.4 (Fußnoten 5/7)",
     "befund": "Tätigkeit mit Schweißrauch-Exposition angegeben (Schweißen/Schneiden/"
               "thermisches Spritzen von chromhaltigen Werkstoffen).",
     "konsequenz": "Zusätzlich die DGUV Empfehlung »Schweißen und Trennen von Metallen« "
                   "anwenden. Beim Biomonitoring beachten: Chrom in der Erythrozytenfraktion "
                   "gilt nicht für Schweißrauch-Exposition – Chrom im Urin (Probenahme bei "
                   "Expositions- bzw. Schichtende) verwenden."},
    {"wenn": {"bleichromat": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Mischexposition",
     "quelle": "Abschnitt 2 (Anwendungsbereich)",
     "befund": "Tätigkeit mit Bleichromat/Bleidichromat angegeben.",
     "konsequenz": "Wegen der Toxizität des Bleis zusätzlich die DGUV Empfehlung »Blei und "
                   "anorganische Bleiverbindungen« heranziehen (inkl. Blei-Biomonitoring)."},
    # ── Schutzmaßnahmen und Hygiene (Abschnitte 7.1, 8.1, 8.2) ────────────
    {"wenn": {"atemschutz": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Atemschutz",
     "quelle": "Abschnitte 7.1, 8.1 und 8.2",
     "befund": "Atemschutz wird bei chrombelasteten Arbeiten selten oder nie getragen.",
     "konsequenz": "Intensive Beratung zum Vermeiden der Inhalation und zum geeigneten "
                   "Atemschutz; Abgleich mit der Gefährdungsbeurteilung. Ergeben sich "
                   "Anhaltspunkte, dass die Schutzmaßnahmen nicht ausreichen, Mitteilung an "
                   "das Unternehmen und Vorschlag von Schutzmaßnahmen (§ 6 (4) ArbMedVV, "
                   "TRGS 561)."},
    {"wenn": {"handschuhe": ["selten", "nie"]},
     "schwere": "pruefen",
     "bereich": "Hautschutz",
     "quelle": "Abschnitte 6.2, 7.1 und 8.1",
     "befund": "Bei möglichem Hautkontakt werden selten oder nie Schutzhandschuhe getragen.",
     "konsequenz": "Beratung: lösliche Chrom(VI)-Verbindungen sind hautresorptiv und "
                   "sensibilisierend – richtigen Einsatz geeigneter Schutzhandschuhe und "
                   "Hautschutzmaßnahmen erläutern (TRGS 401). Bei fortbestehendem ungeschütztem "
                   "Hautkontakt Mitteilung an das Unternehmen (§ 6 (4) ArbMedVV)."},
    {"wenn": {"hautkontakt": ["yes"]},
     "schwere": "hinweis",
     "bereich": "Hautschutz",
     "quelle": "Abschnitte 6.2, 6.3.2 und 8.2",
     "befund": "Direkter Hautkontakt zu chromhaltigen Flüssigkeiten/Stäuben trotz "
               "Schutzmaßnahmen angegeben.",
     "konsequenz": "Beratung zu Hautresorption, Sensibilisierung und Chromatgeschwüren; "
                   "Haut auf Rhagaden und Wunden kontrollieren. Überprüfung der "
                   "Gefährdungsbeurteilung und der Schutzmaßnahmen anregen (TRGS 401/561)."},
    {"wenn": {"hygiene": ["no"]},
     "schwere": "hinweis",
     "bereich": "Hygiene",
     "quelle": "Abschnitte 7.1 und 8.1",
     "befund": "Hygieneregeln am Arbeitsplatz können nicht eingehalten werden.",
     "konsequenz": "Beratung zu Hygienemaßnahmen (nicht essen/trinken/rauchen im "
                   "Arbeitsbereich, Hautreinigung, Wechsel und getrennte Aufbewahrung der "
                   "Arbeitskleidung); organisatorische Defizite dem Unternehmen mitteilen "
                   "(§ 6 (4) ArbMedVV)."},
    # ── Beratung und besondere Personengruppen ────────────────────────────
    {"wenn": {"rauchen": ["ja"]},
     "schwere": "hinweis",
     "bereich": "Rauchen",
     "quelle": "Abschnitte 6.3.1 und 8.1",
     "befund": "Aktueller Tabakkonsum angegeben.",
     "konsequenz": "Beratung: bei Rauchern ist Synkarzinogenität mit Chrom(VI)-Verbindungen "
                   "möglich – eindringlich auf das erhöhte Bronchialkarzinom-Risiko hinweisen "
                   "und Tabakentwöhnung empfehlen; Rauchverbot im Arbeitsbereich beachten."},
    {"wenn": {"personengruppe": ["schwanger", "stillend", "unter18"]},
     "schwere": "pruefen",
     "bereich": "Beschäftigungsbeschränkungen",
     "quelle": "Abschnitt 7.1 (allgemeine Beratung)",
     "befund": "Schwangerschaft, Stillzeit oder Alter unter 18 Jahren angegeben.",
     "konsequenz": "Beschäftigungsbeschränkungen für Jugendliche sowie werdende und stillende "
                   "Mütter unverzüglich klären (Mutterschutzgesetz, Jugendarbeitsschutzgesetz "
                   "i. V. m. angrenzenden Regelwerken); Chrom(VI)-Verbindungen sind "
                   "krebserzeugend und keimzellmutagen – Tätigkeitsanpassung mit dem "
                   "Unternehmen abstimmen."},
    {"wenn": {"vorsorge_art": ["nachgehend"]},
     "schwere": "hinweis",
     "bereich": "Nachgehende Vorsorge",
     "quelle": "Abschnitte 2 (Angebotsvorsorge) und 7.2.2 (Nachgehende Untersuchung)",
     "befund": "Termin im Rahmen der nachgehenden Vorsorge nach Ende der Tätigkeit.",
     "konsequenz": "Programm der nachgehenden Vorsorge anwenden: Anamnese; bildgebende "
                   "Untersuchung des Thorax nur bei Auffälligkeiten in Anamnese und/oder "
                   "Untersuchung (rechtfertigende Indikation), in unklaren Fällen HNO-ärztliche "
                   "Untersuchung. Registrierung über das Meldeportal »DGUV Vorsorge« "
                   "(www.dguv-vorsorge.de) sicherstellen."},
]
