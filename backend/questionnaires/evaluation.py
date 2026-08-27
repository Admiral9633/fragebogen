# -*- coding: utf-8 -*-
"""
Automatische Auswertung der Fragebogen-Antworten nach den
Begutachtungsleitlinien zur Kraftfahreignung (BASt, Stand 2022).

WICHTIG: Dies ist Entscheidungsunterstützung für die ärztliche Beurteilung.
Die Hinweise referenzieren das jeweilige Leitlinien-Kapitel und ersetzen
keine Begutachtung; die abschließende Bewertung trifft die Ärztin/der Arzt.

Schweregrade:
  kritisch – Konstellation, die nach Leitlinie die Fahreignung derzeit
             ausschließt oder regelhaft ausschließen kann
  pruefen  – eignungsrelevanter Befund, der Abklärung/Unterlagen erfordert
  hinweis  – beurteilungsrelevante Zusatzinformation
"""

SCHWERE_ORDER = {"kritisch": 0, "pruefen": 1, "hinweis": 2}


def evaluate_rules(answers, rules, gruppe2=False):
    """
    Datengetriebene Auswertung für DGUV-Kataloge.

    Eine Regel feuert, wenn ALLE Bedingungen in "wenn" zutreffen
    ({frage_id: [erlaubte werte]}); optional schließt "wenn_nicht"
    ({frage_id: [werte]}) die Regel aus, sobald EINE dieser Bedingungen zutrifft.
    Bei Multi-Choice-Antworten (Listen) trifft eine Bedingung zu, sobald
    EINER der angekreuzten Werte in der Werteliste der Regel steht.
    """
    def _match(answer, werte):
        if isinstance(answer, list):
            return any(a in werte for a in answer)
        return answer in werte

    out = []
    for rule in rules or []:
        wenn = rule.get("wenn", {})
        if not wenn:
            continue
        if not all(_match(answers.get(q), werte) for q, werte in wenn.items()):
            continue
        wenn_nicht = rule.get("wenn_nicht", {})
        if any(_match(answers.get(q), werte) for q, werte in wenn_nicht.items()):
            continue
        out.append({
            "schwere": rule.get("schwere", "hinweis"),
            "bereich": rule.get("bereich", ""),
            "kapitel": rule.get("quelle", rule.get("kapitel", "")),
            "befund": rule.get("befund", ""),
            "konsequenz": rule.get("konsequenz", ""),
        })

    out.sort(key=lambda f: SCHWERE_ORDER.get(f["schwere"], 9))
    counts = {"kritisch": 0, "pruefen": 0, "hinweis": 0}
    for f in out:
        counts[f["schwere"]] += 1
    return {
        "gruppe2": gruppe2,
        "findings": out,
        "zusammenfassung": counts,
        "disclaimer": (
            "Automatisch erzeugte Hinweise nach den DGUV Empfehlungen/Grundsätzen "
            "für arbeitsmedizinische Untersuchungen. Entscheidungsunterstützung – "
            "die abschließende Beurteilung obliegt der Ärztin/dem Arzt."
        ),
    }


def evaluate_for_template(answers, template_slug):
    """Auswertung passend zum Template: bespoke Verkehrsmedizin oder Regel-Engine."""
    from questionnaires.catalogs import CATALOG_REGISTRY

    entry = CATALOG_REGISTRY.get(template_slug)
    if entry is None or entry.get("rules") is None:
        # Verkehrsmedizin (und unbekannte/Legacy-Templates): BASt-Regelwerk —
        # feuert nur auf bekannte Frage-IDs und ist damit auch für Legacy sicher
        return evaluate_answers(answers)
    return evaluate_rules(answers, entry["rules"])

GRUPPE2_ANLAESSE = {"lkw", "bus", "fahrgast"}
GRUPPE2_KLASSEN = {"C", "C1", "CE", "C1E", "D", "D1", "DE"}


def is_gruppe2(answers):
    """Gruppe 2 (LKW/Bus/Fahrgastbeförderung) aus Anlass oder Klassen ableiten."""
    if answers.get("exam_occasion") in GRUPPE2_ANLAESSE:
        return True
    classes = answers.get("license_classes") or []
    return any(c in GRUPPE2_KLASSEN for c in classes)


def _f(schwere, bereich, kapitel, befund, konsequenz):
    return {
        "schwere": schwere,
        "bereich": bereich,
        "kapitel": kapitel,
        "befund": befund,
        "konsequenz": konsequenz,
    }


def evaluate_answers(answers):  # noqa: C901 - bewusst ein flaches Regelwerk
    """Antworten → Liste eignungsrelevanter Befunde mit Leitlinien-Bezug."""
    a = answers
    g2 = is_gruppe2(a)
    out = []

    def yes(key):
        return a.get(key) == "yes"

    # ── Anfälle & Epilepsie (Kap. 3.9.6) ─────────────────────────────────────
    if yes("seizure_ever"):
        frei = a.get("seizure_free")
        if frei == "unter3m":
            out.append(_f("kritisch", "Epileptische Anfälle", "3.9.6",
                "Anfall vor weniger als 3 Monaten",
                "Mindest-Anfallsfreiheit nicht erreicht (Gruppe 1: je nach Konstellation "
                "3–12 Monate; Gruppe 2: mindestens 6 Monate bis 5 Jahre). Derzeit keine "
                "Fahreignung anzunehmen."))
        elif frei == "3bis6m":
            out.append(_f("kritisch" if g2 else "pruefen", "Epileptische Anfälle", "3.9.6",
                "Anfallsfreiheit 3–6 Monate",
                "Gruppe 1 nur nach provoziertem Anfall mit vermeidbarem Auslöser (3 Monate) "
                "möglich; nach unprovoziertem Anfall 6 Monate erforderlich. Gruppe 2: Frist "
                "nicht erreicht."))
        elif frei == "6bis12m":
            out.append(_f("kritisch" if g2 else "pruefen", "Epileptische Anfälle", "3.9.6",
                "Anfallsfreiheit 6–12 Monate",
                "Gruppe 1: nach erstmaligem unprovoziertem Anfall erfüllt; bei Epilepsie "
                "erst ab 1 Jahr. Gruppe 2: nach erstmaligem unprovoziertem Anfall sind "
                "2 Jahre gefordert."))
        if a.get("epilepsy") == "yes":
            if g2:
                out.append(_f("kritisch", "Epilepsie", "3.9.6",
                    "Diagnostizierte Epilepsie (Gruppe-2-Untersuchung)",
                    "Gruppe 2: grundsätzlich keine Eignung; einzige Ausnahme 5 Jahre "
                    "Anfallsfreiheit ohne antiepileptische Behandlung."))
            else:
                out.append(_f("pruefen", "Epilepsie", "3.9.6",
                    "Diagnostizierte Epilepsie",
                    "Gruppe 1: mindestens 1 Jahr Anfallsfreiheit erforderlich (auch unter "
                    "Medikation möglich); jährliche fachneurologische Kontrollen."))
        ae = a.get("antiepileptics")
        if ae in ("reduktion", "ende_unter3m"):
            out.append(_f("kritisch", "Antiepileptika", "3.9.6",
                "Antiepileptika werden reduziert bzw. wurden vor <3 Monaten beendet",
                "Während der Reduzierung des letzten Medikaments und in den ersten "
                "3 Monaten ohne Medikation besteht keine Fahreignung."))
        elif ae == "aktuell" and g2:
            out.append(_f("kritisch", "Antiepileptika", "3.9.6",
                "Antiepileptika-Einnahme (Gruppe-2-Untersuchung)",
                "Gruppe 2 ist nur ohne Einnahme von Antiepileptika möglich."))

    # ── Synkopen (Kap. 3.4.11) ───────────────────────────────────────────────
    if a.get("syncope") == "mehrmals":
        if yes("syncope_recent"):
            out.append(_f("kritisch", "Synkopen", "3.4.11",
                "Wiederholte Ohnmachten, letzte vor <6 Monaten",
                "Bei wiederholter unklarer Synkope Gruppe 1 mindestens 6 Monate keine "
                "Fahreignung; Gruppe 2 in der Regel keine Eignung. Erneute Diagnostik "
                "erforderlich."))
        else:
            out.append(_f("pruefen", "Synkopen", "3.4.11",
                "Wiederholte Ohnmachten in der Vorgeschichte",
                "Ursache und Rezidivrisiko klären; Gruppe 2 bei unklarer Ursache in der "
                "Regel keine Eignung (Ausnahme: Synkopen mit geringem Risiko am Steuer)."))
        if yes("syncope_prodromi") is False and a.get("syncope_prodromi") == "no":
            out.append(_f("pruefen", "Synkopen", "3.4.11",
                "Ohnmachten ohne Vorboten (Prodromi)",
                "Fehlende Prodromi verschärfen die Beurteilung – rechtzeitiges Anhalten "
                "ist nicht möglich."))
    elif a.get("syncope") == "einmal":
        out.append(_f("hinweis", "Synkopen", "3.4.11",
            "Einmalige Ohnmacht in der Vorgeschichte",
            "Nach erster Synkope bleibt die Eignung in der Regel erhalten, sofern kein "
            "sehr hohes Wiederholungsrisiko vorliegt (Ursache dokumentieren)."))

    # ── Tagesschläfrigkeit / ESS / OSAS (Kap. 3.11) ──────────────────────────
    ess = a.get("ess_total")
    if isinstance(ess, int):
        if ess >= 16:
            out.append(_f("kritisch", "Tagesschläfrigkeit", "3.11.1",
                f"ESS {ess}/24 – ausgeprägte Tagesschläfrigkeit",
                "Unbehandelte/therapierefraktäre schwere Tagesschläfrigkeit schließt die "
                "Fahreignung aus; schlafmedizinische Abklärung (Stufe 2) zwingend."))
        elif ess >= 11:
            out.append(_f("pruefen", "Tagesschläfrigkeit", "3.11.1",
                f"ESS {ess}/24 – auffällige Tagesschläfrigkeit (Grenzwert 11)",
                "Weitere schlafmedizinische Abklärung (Stufe 2, ggf. Fahrprobe) "
                "erforderlich, bevor die Fahreignung bejaht wird."))
    if yes("microsleep"):
        out.append(_f("kritisch", "Tagesschläfrigkeit", "3.11.1",
            "Ungewolltes Einschlafen / Sekundenschlaf",
            "Kernsymptom auffälliger Tagesschläfrigkeit mit hohem Unfallrisiko – vor "
            "Bejahung der Fahreignung abklären und behandeln; Details (am Steuer?) "
            "erfragen."))
    elif yes("daytime_sleepiness"):
        out.append(_f("pruefen", "Tagesschläfrigkeit", "3.11.1",
            "Monotonie-Intoleranz (Wachbleiben in eintönigen Situationen schwer)",
            "Stufe-1-Kriterium der Leitlinie – ESS-Ergebnis und Fremdanamnese "
            "berücksichtigen, ggf. schlafmedizinische Abklärung."))
    if yes("osas"):
        cpap = a.get("cpap")
        if cpap in ("keine", "abgebrochen", "unregelmaessig"):
            out.append(_f("kritisch", "Schlafapnoe", "3.11.2",
                "Diagnostiziertes OSAS ohne konsequent genutzte Therapie",
                "Mittel-/schweres OSAS mit Tagesschläfrigkeit schließt die Fahreignung "
                "aus; Eignung nur bei eingehaltener Therapie mit gebesserter Wachheit. "
                "Therapieadhärenz und AHI klären."))
        else:
            out.append(_f("hinweis", "Schlafapnoe", "3.11.2",
                "OSAS unter regelmäßiger Therapie (z.B. CPAP)",
                "Regelmäßige ärztliche Kontrollen erforderlich: Gruppe 2 mindestens "
                "jährlich, Gruppe 1 höchstens alle 3 Jahre."))
    elif yes("snoring"):
        out.append(_f("pruefen", "Schlafapnoe", "3.11.2",
            "Fremdanamnestisch lautes Schnarchen / Atempausen",
            "OSAS-Verdacht – bei Verdacht ist vor Erteilung/Erneuerung der Fahrerlaubnis "
            "eine schlafmedizinische Untersuchung erforderlich."))

    # ── Diabetes (Kap. 3.5) ──────────────────────────────────────────────────
    if a.get("diabetes_type") not in (None, "", "none"):
        if yes("hypoglycemia"):
            out.append(_f("kritisch", "Diabetes", "3.5",
                "Schwere Unterzuckerung mit Fremdhilfe in den letzten 12 Monaten",
                "Bei wiederholter schwerer Hypoglykämie im Wachzustand in der Regel "
                "3 Monate keine Eignung ab letzter Episode; Gruppe 2: keine wiederholte "
                "schwere Hypoglykämie in den letzten 12 Monaten. Anzahl und Umstände "
                "(wach/Schlaf) klären."))
        if yes("hypo_awareness"):
            out.append(_f("kritisch", "Diabetes", "3.5",
                "Hypoglykämie-Wahrnehmungsstörung",
                "Schließt die Fahreignung beider Gruppen aus, bis die Wahrnehmung "
                "(Training, Therapieumstellung) wiederhergestellt ist."))
        therapie = a.get("diabetes_therapy")
        if therapie in ("insulin", "tabl_high"):
            if g2:
                out.append(_f("pruefen", "Diabetes", "3.5",
                    "Therapie mit Hypoglykämierisiko (Gruppe-2-Untersuchung)",
                    "Gruppe 2: fachärztlich-diabetologische Begutachtung alle 3 Jahre, "
                    "stabile Stoffwechselführung über 3 Monate, Glukoseselbstkontrollen "
                    "mindestens zweimal täglich sowie zu fahrrelevanten Zeiten."))
            if a.get("glucose_monitoring") in ("seltener", "nein"):
                out.append(_f("pruefen", "Diabetes", "3.5",
                    "Unzureichende Glukose-Selbstkontrollen unter risikobehafteter Therapie",
                    "Geforderte Selbstkontrollen (insbesondere zu fahrrelevanten Zeiten) "
                    "werden nicht eingehalten – Schulung/Auflagen erwägen."))
        if yes("diabetes_derailment"):
            out.append(_f("pruefen", "Diabetes", "3.5",
                "Kürzliche Neueinstellung oder Stoffwechselentgleisung",
                "Fahrpause bis zum Abschluss der Einstellphase (sichere "
                "Hypoglykämiewahrnehmung, normalisiertes Sehvermögen); Gruppe 2: "
                "stabile Stoffwechselführung über 3 Monate nachweisen."))

    # ── Herz-Kreislauf (Kap. 3.4) ────────────────────────────────────────────
    if a.get("pacemaker_icd") == "icd":
        if g2:
            out.append(_f("kritisch", "Defibrillator (ICD)", "3.4.1.4",
                "ICD-Träger (Gruppe-2-Untersuchung)",
                "Fahrer der Gruppe 2 mit ICD sind in der Regel nicht geeignet."))
        else:
            out.append(_f("pruefen", "Defibrillator (ICD)", "3.4.1.4",
                "ICD-Träger",
                "Wartefristen beachten (primärpräventiv 1–2 Wochen, sekundärpräventiv "
                "3 Monate); regelmäßige ICD-Kontrollen erforderlich."))
        if yes("icd_shock"):
            out.append(_f("kritisch", "Defibrillator (ICD)", "3.4.1.4",
                "ICD-Schockabgabe in den letzten 3 Monaten",
                "Nach adäquater Schockabgabe 3 Monate keine Fahreignung; inadäquate "
                "Schocks müssen sicher verhindert sein (kardiologische Stellungnahme)."))
    if yes("heart_attack"):
        out.append(_f("pruefen", "Koronare Herzkrankheit", "3.4.4",
            "Herzinfarkt / Stent / Bypass in der Vorgeschichte",
            "Wartefristen und Pumpfunktion prüfen (Gruppe 1: ab Entlassung bzw. "
            "4 Wochen bei EF ≤35 %; Gruppe 2: 6 Wochen und nur bei EF >35 %, nach "
            "Bypass 3 Monate). Aktuellen kardiologischen Befund anfordern."))
    belastung = a.get("exertion_symptoms")
    if belastung == "ruhe":
        out.append(_f("kritisch", "Herzinsuffizienz", "3.4.5",
            "Beschwerden bereits in Ruhe (entspricht NYHA IV)",
            "Keine Fahreignung für beide Gruppen."))
    elif belastung == "leicht":
        out.append(_f("kritisch" if g2 else "pruefen", "Herzinsuffizienz", "3.4.5",
            "Beschwerden bei leichter Belastung (entspricht NYHA III)",
            "Gruppe 2: keine Fahreignung. Gruppe 1: nur bei stabilem NYHA III nach "
            "fachärztlicher Untersuchung."))
    if yes("bp_dizziness"):
        out.append(_f("pruefen", "Blutdrucktherapie", "3.4.2",
            "Schwindel/Schwarzwerden unter Blutdruckmedikation",
            "Therapiebedingter Blutdruckabfall kann zum Kontrollverlust am Steuer "
            "führen – Medikation überprüfen."))
    if yes("arrhythmia"):
        out.append(_f("pruefen", "Herzrhythmusstörungen", "3.4.1",
            "Bekannte Herzrhythmusstörungen",
            "Kardiologische Untersuchung inkl. Langzeit-EKG; rhythmogene Synkopen "
            "schließen die Eignung aus. Gruppe 2: AV-Block III/Mobitz II und "
            "alternierender Schenkelblock schließen die Eignung aus."))
    if yes("heart_other"):
        out.append(_f("pruefen", "Herz-/Gefäßerkrankung", "3.4.7–3.4.12",
            "Klappenfehler / angeborener Herzfehler / Kardiomyopathie / "
            "Ionenkanalerkrankung / Aneurysma / Karotisstenose angegeben",
            "Je nach Diagnose gelten eigene Fristen und Gruppe-2-Ausschlüsse – "
            "kardiologische Unterlagen anfordern und nach dem jeweiligen Kapitel "
            "beurteilen."))
    if yes("family_sudden_death"):
        out.append(_f("hinweis", "Familienanamnese", "3.4.9/3.4.10",
            "Plötzlicher Herztod bei Verwandten 1. Grades",
            "Risikokriterium (u.a. bei hypertropher Kardiomyopathie für Gruppe 2) – "
            "bei kardialen Diagnosen in die Beurteilung einbeziehen."))

    # ── Gehirn (Kap. 3.9.4 / 3.9.5) ──────────────────────────────────────────
    if yes("stroke"):
        if yes("stroke_residuals"):
            out.append(_f("kritisch", "Schlaganfall/TIA", "3.9.4",
                "Zustand nach Schlaganfall/Hirnblutung/TIA mit fortbestehenden Ausfällen",
                "Relevante neurologische/neuropsychologische Ausfälle schließen die "
                "Eignung beider Gruppen aus, bis sie erfolgreich behandelt bzw. "
                "kompensiert sind."))
        else:
            out.append(_f("kritisch" if g2 else "pruefen", "Schlaganfall/TIA", "3.9.4",
                "Zustand nach Schlaganfall/Hirnblutung/TIA",
                "Gruppe 2: die Belastungen sind Betroffenen generell nicht zuzumuten. "
                "Gruppe 1: Wiedererlangung nach erfolgreicher Therapie möglich; "
                "Nachuntersuchungen nach 1, 2 und 4 Jahren."))
    if yes("head_injury"):
        if yes("head_injury_recent"):
            out.append(_f("kritisch", "Hirnverletzung/-operation", "3.9.5",
                "Hirnverletzung oder -operation vor weniger als 3 Monaten",
                "Im Allgemeinen 3 Monate keine Eignung für beide Gruppen; Ausnahme nur "
                "bei neurologisch nachgewiesener Störungsfreiheit."))
        if yes("brain_residuals"):
            out.append(_f("pruefen", "Hirnverletzung/-operation", "3.9.5",
                "Folgebeschwerden nach Hirnverletzung/-operation",
                "Hirnorganische Leistungsstörungen bzw. Anfallskomplikationen abklären "
                "(neurologisch, ggf. neuropsychologisch; vgl. 3.9.6/3.12.2)."))

    # ── Nervensystem (Kap. 3.9.1–3.9.3) ──────────────────────────────────────
    if yes("parkinson"):
        out.append(_f("kritisch" if g2 else "pruefen", "Parkinson/Extrapyramidal", "3.9.3",
            "Parkinson-Krankheit bzw. Bewegungs-/Koordinationsstörung",
            "Gruppe 2: bei erkennbarer Symptomatik in der Regel keine Eignung. "
            "Gruppe 1: nur bei erfolgreicher Therapie/leichten Fällen; "
            "Nachuntersuchungen nach 1, 2 und 4 Jahren."))
    if yes("ms_spinal"):
        out.append(_f("pruefen", "Rückenmark/MS", "3.9.1",
            "Rückenmarkserkrankung/-verletzung bzw. Multiple Sklerose",
            "Ausmaß der motorischen Behinderung und Kompensierbarkeit (Fahrzeugumbau) "
            "prüfen; Gruppe 2 bei relevanter Behinderung in der Regel ausgeschlossen; "
            "bei progredienten Verläufen Nachuntersuchungen."))
    if yes("muscle_nerve"):
        out.append(_f("pruefen", "Neuromuskulär", "3.9.2",
            "Muskel-/Nervenerkrankung (Myasthenie, Muskelschwund, Polyneuropathie)",
            "Bei relevanter motorischer Beeinträchtigung Gruppe 2 ausgeschlossen; "
            "Gruppe 1 im Einzelfall neurologisch nachweisen; ggf. Nachuntersuchungen "
            "nach 1, 2 und 4 Jahren."))
    if yes("paralysis_attacks"):
        out.append(_f("kritisch", "Anfallsartige Lähmungen", "3.9.2",
            "Anfallsartige Lähmungen / plötzliche Muskelschwäche",
            "Mit Anfallsleiden vergleichbar – Eignung setzt Anfallsfreiheit oder "
            "nachweislich langsam einsetzende, kontrollierbare Lähmungen voraus."))
    if yes("motor_limits"):
        out.append(_f("pruefen", "Motorik", "3.3/3.9",
            "Lähmungen/Gefühlsstörungen mit möglicher Fahrrelevanz",
            "Kompensation nach den Sicherheitsmaßnahmen für körperbehinderte "
            "Kraftfahrer (Anhang B) prüfen; ggf. Fahrprobe und Fahrzeugauflagen."))

    # ── Gleichgewicht/Schwindel (Kap. 3.10) ──────────────────────────────────
    if yes("vertigo"):
        letzte = a.get("vertigo_last")
        prodromi = a.get("vertigo_prodromi")
        if letzte == "unter3m" and prodromi == "nie":
            out.append(_f("kritisch", "Schwindel", "3.10",
                "Schwindelattacken ohne Vorboten, letzte vor <3 Monaten",
                "Attackenfreier Beobachtungszeitraum von mindestens 3 Monaten (je nach "
                "Krankheitsbild länger) nicht erfüllt – derzeit keine Fahreignung "
                "anzunehmen."))
        elif letzte in ("unter3m", "3bis6m"):
            out.append(_f("pruefen", "Schwindel", "3.10",
                "Kürzliche Schwindelattacken",
                "Krankheitsbild und attackenfreie Fristen klären (z.B. Menière: "
                "Gruppe 1 6–12 Monate, Gruppe 2 2–4 Jahre; HNO-fachärztliche "
                "Untersuchung)."))
        if yes("vertigo_positional"):
            out.append(_f("pruefen", "Schwindel", "3.10.1",
                "Lageabhängiger Schwindel (V.a. gutartiger Lagerungsschwindel)",
                "Fahreignung erst nach erfolgreicher Therapie/Spontanremission "
                "(Nachweis per Lagerungsprüfung)."))
        if yes("vertigo_ear"):
            out.append(_f("pruefen", "Schwindel", "3.10.1",
                "Drehschwindel mit Ohrsymptomen (V.a. Morbus Menière)",
                "Fristen abhängig von Prodromi und Gruppe (6 Monate bis 4 Jahre "
                "Attackenfreiheit); fachärztliche Abklärung."))

    # ── Psyche (Kap. 3.12) ───────────────────────────────────────────────────
    if yes("psychosis"):
        out.append(_f("kritisch" if g2 else "pruefen", "Psychose", "3.12.5",
            "Schizophrenie/Psychose in der Vorgeschichte",
            "Gruppe 2: nach schizophrener Erkrankung in der Regel dauerhaft keine "
            "Eignung. Gruppe 1: möglich, wenn keine das Realitätsurteil "
            "beeinträchtigenden Störungen mehr nachweisbar sind; fachpsychiatrische "
            "Beurteilung."))
    if yes("psychiatric_severe"):
        out.append(_f("pruefen", "Affektive Störung", "3.12.4",
            "Stationäre Behandlung / Manie / Suizidalität in der Vorgeschichte",
            "Sehr schwere Phasen schließen die Eignung während der Phase aus; bei "
            "mehreren Phasen nur mit belegter Prophylaxe und regelmäßigen "
            "psychiatrischen Kontrollen. Gruppe 2: Symptomfreiheit gefordert, nach "
            "mehreren Phasen in der Regel keine Eignung."))
    if yes("memory_problems"):
        out.append(_f("pruefen", "Kognition/Demenz", "3.12.2/3.12.3",
            "Zunehmende Gedächtnis-/Orientierungsprobleme (auch fremdanamnestisch)",
            "Demenz-Abklärung (ggf. neuropsychologisch, Fahrprobe); ausgeprägte "
            "Demenz schließt beide Gruppen aus, Gruppe 2 bereits bei geringeren "
            "Einschränkungen."))

    # ── Alkohol, Drogen, Medikamente (Kap. 3.13/3.14) ────────────────────────
    if yes("alcohol_dependence"):
        out.append(_f("kritisch", "Alkohol", "3.13.2",
            "Alkoholabhängigkeit bzw. Entgiftung/Entwöhnung in der Vorgeschichte",
            "Bei Abhängigkeit keine Eignung; Wiedererlangung erst nach erfolgreicher "
            "Entwöhnung und in der Regel einjähriger, ärztlich (inkl. Labor) belegter "
            "Abstinenz."))
    if yes("alcohol_traffic"):
        out.append(_f("pruefen", "Alkohol", "3.13.1",
            "Verkehrsauffälligkeit unter Alkohol (Trunkenheitsfahrt/MPU)",
            "Missbrauchsverdacht – sichere Trennung von Konsum und Fahren klären; "
            "Wiederherstellung erst nach stabil geändertem Trinkverhalten (in der "
            "Regel 1 Jahr, mindestens 6 Monate)."))
    if yes("alcohol_control"):
        out.append(_f("pruefen", "Alkohol", "3.13.1",
            "Kontrollverlust über den Alkoholkonsum angegeben",
            "Leitlinien-Kriterium für Missbrauch – Konsummuster und "
            "Abhängigkeitskriterien (ICD-10) explorieren."))
    elif a.get("alcohol") == "taeglich":
        out.append(_f("pruefen", "Alkohol", "3.13.1",
            "(Fast) täglicher Alkoholkonsum",
            "Konsummuster hinsichtlich Gewöhnung/Missbrauch explorieren (Labor: "
            "z.B. CDT/GGT erwägen)."))
    if yes("drugs"):
        if a.get("cannabis") == "regelmaessig":
            out.append(_f("kritisch", "Betäubungsmittel", "3.14.1",
                "Regelmäßiger (täglicher/gewohnheitsmäßiger) Cannabiskonsum",
                "Schließt die Eignung in der Regel aus. Bei gelegentlichem Konsum: "
                "Trennung von Konsum und Fahren, kein Beigebrauch."))
        else:
            out.append(_f("pruefen", "Betäubungsmittel", "3.14.1",
                "Drogenkonsum aktuell oder in der Vorgeschichte",
                "Aktuelle BtM-Einnahme schließt die Eignung aus (außer ärztlich "
                "verordnet); nach Abhängigkeit einjährige Abstinenz mit unangekündigten "
                "Laborkontrollen nachweisen."))
        if yes("substitution"):
            out.append(_f("kritisch", "Substitution", "3.14.1",
                "Laufende Substitutionsbehandlung (z.B. Methadon)",
                "In der Regel keine Eignung; seltene Ausnahmen erfordern u.a. über "
                "einjährige Substitution, stabile Integration und ein Jahr "
                "nachgewiesene Beigebrauchsfreiheit."))
    if yes("med_side_effects"):
        out.append(_f("kritisch", "Dauermedikation", "3.14.2",
            "Spürbare Nebenwirkungen (Müdigkeit, Verlangsamung, Schwindel) unter "
            "Dauermedikation",
            "Erhebliche unerwünschte Wirkungen wie Verlangsamung und "
            "Konzentrationsstörungen schließen die Eignung aus – Medikation "
            "anpassen und neu beurteilen."))
    elif yes("sedating_meds"):
        out.append(_f("pruefen", "Dauermedikation", "3.14.2",
            "Dauerbehandlung mit potenziell sedierenden Medikamenten",
            "Psychoaktive Dauermedikation kann die Eignung unabhängig vom "
            "Grundleiden beeinträchtigen; regelmäßige ärztliche Überwachung mit "
            "Nachweis erforderlich."))
    if yes("benzo_regular"):
        out.append(_f("pruefen", "Dauermedikation", "3.14.2",
            "Regelmäßige Einnahme von Schlaf-/Beruhigungsmitteln über Monate",
            "Risiko einer Low-dose-Abhängigkeit (auch bei kleinen abendlichen "
            "Mengen) – Entzugssymptome explorieren, Ausschleichen erwägen."))
    if yes("med_recent_change"):
        out.append(_f("hinweis", "Dauermedikation", "3.14.2",
            "Kürzlich neu angesetztes/umgestelltes Medikament",
            "In der Initialphase einer Behandlung ist besondere Vorsicht geboten."))

    # ── Sehen & Hören (Kap. 3.1/3.2) ─────────────────────────────────────────
    if yes("eye_disease") or yes("one_eyed") or yes("night_vision"):
        details = [t for t, k in (
            ("Augenerkrankung", "eye_disease"),
            ("einseitig stark gemindertes Sehen", "one_eyed"),
            ("Probleme bei Dämmerung/Blendung", "night_vision"),
        ) if yes(k)]
        out.append(_f("pruefen", "Sehvermögen", "3.1",
            "Angegeben: " + ", ".join(details),
            "Sehanforderungen nach § 12 / Anlage 6 FeV prüfen (Gruppe 2 deutlich "
            "strenger, ggf. augenärztliche Untersuchung); Kompensation z.B. Verzicht "
            "auf Nachtfahrten möglich."))
    if yes("hearing_impaired") and g2:
        out.append(_f("pruefen", "Hörvermögen", "3.2",
            "Hochgradige Schwerhörigkeit/Gehörlosigkeit (Gruppe-2-Untersuchung)",
            "HNO-fachärztliche Eignungsuntersuchung, regelmäßige Kontrollen und "
            "Nachweis von 3 Jahren Fahrpraxis mit Klasse B erforderlich; "
            "Begleitstörungen (Gleichgewicht/Sehen) ausschließen."))

    # ── Innere Organe (Kap. 3.6–3.8) ─────────────────────────────────────────
    if yes("dialysis"):
        out.append(_f("kritisch" if g2 else "pruefen", "Niere", "3.6",
            "Dialysepflichtige Niereninsuffizienz",
            "Gruppe 2: in der Regel keine Eignung (Ausnahme nur nach nephrologischer "
            "Einzelbegutachtung). Gruppe 1: nur unter ständiger ärztlicher Betreuung "
            "und Kontrolle."))
    elif yes("kidney_disease"):
        out.append(_f("pruefen", "Niere", "3.6",
            "Chronische Nierenerkrankung",
            "Maßgeblich ist die tatsächliche Beeinträchtigung von Allgemeinbefinden "
            "und Leistungsfähigkeit; nephrologische Betreuung dokumentieren."))
    if yes("transplant"):
        out.append(_f("pruefen", "Transplantation", "3.6/3.7",
            "Zustand nach Organtransplantation",
            "Organfunktion, Immunsuppressions-Nebenwirkungen und Nachsorge prüfen; "
            "nach Nierentransplantation jährliche Nachbegutachtung, Herz: Gruppe 2 "
            "in der Regel keine Eignung (<5 Jahre)."))
    if yes("cough_syncope"):
        out.append(_f("kritisch", "Lunge", "3.8",
            "Hustensynkopen (Schwindel/Bewusstlosigkeit bei Hustenanfall)",
            "Können die Fähigkeit zum sicheren Führen von Kraftfahrzeugen aufheben – "
            "internistische Abklärung vor Bejahung der Eignung."))
    if yes("dyspnea"):
        out.append(_f("pruefen", "Lunge", "3.8",
            "Atemnot bei leichter Belastung/in Ruhe bzw. Sauerstofftherapie",
            "Hinweis auf fortgeschrittene Erkrankung mit möglicher respiratorischer "
            "Insuffizienz – Lungenfunktion/Blutgase und kardiale Rückwirkungen "
            "(Cor pulmonale, vgl. 3.4.5) klären."))

    # ── Allgemeines ──────────────────────────────────────────────────────────
    if a.get("has_conditions") == "no":
        out.append(_f("hinweis", "Anamnese", "2.5",
            "Patient verneint Vorerkrankungen, dauerhafte Einschränkungen und "
            "laufende ärztliche Behandlung",
            "Verkürzter Fragensatz: Diagnose-Blöcke wurden übersprungen; Symptom- "
            "und Ereignis-Screening (Anfälle, Synkopen, Tagesschläfrigkeit, "
            "Substanzen) wurde vollständig erhoben."))
    if yes("license_withdrawn"):
        out.append(_f("pruefen", "Verkehrsvorgeschichte", "3.13/3.17",
            "Früherer Fahrerlaubnisentzug bzw. MPU",
            "Anlass und Ausgang klären; körperliche/psychische Ursachen der damaligen "
            "Auffälligkeit dürfen nicht fortbestehen."))
    if a.get("psych_test_done") == "no":
        out.append(_f("pruefen", "Fahrgastbeförderung/Bus", "3.19",
            "Psychologischer Leistungstest noch nicht absolviert",
            "Für Klassen D/D1 und Fahrgastbeförderung ist der Nachweis der "
            "psychischen Leistungsfähigkeit nach Anlage 5 Nr. 2 FeV erforderlich."))
    if yes("multiple_conditions"):
        out.append(_f("hinweis", "Kumulation", "2.7",
            "Mehrere Erkrankungen gleichzeitig angegeben",
            "Kumulierte Auffälligkeiten können in ihrer Summe Eignungszweifel "
            "begründen, auch wenn jede einzelne unbedenklich wäre."))
    if yes("accidents"):
        out.append(_f("hinweis", "Fahranamnese", "2.5",
            "Unfälle/Beinahe-Unfälle in den letzten 24 Monaten",
            "Unfallhergang auf mögliche medizinische Ursachen (Sekundenschlaf, "
            "Synkope, Seh-/Reaktionsdefizit) prüfen."))

    out.sort(key=lambda f: SCHWERE_ORDER.get(f["schwere"], 9))
    counts = {"kritisch": 0, "pruefen": 0, "hinweis": 0}
    for f in out:
        counts[f["schwere"]] += 1

    return {
        "gruppe2": g2,
        "findings": out,
        "zusammenfassung": counts,
        "disclaimer": (
            "Automatisch erzeugte Hinweise nach den Begutachtungsleitlinien zur "
            "Kraftfahreignung (BASt, Stand 2022). Entscheidungsunterstützung – die "
            "abschließende Beurteilung obliegt der Ärztin/dem Arzt."
        ),
    }
