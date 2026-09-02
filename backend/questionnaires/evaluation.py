# -*- coding: utf-8 -*-
"""
Automatische Auswertung der Fragebogen-Antworten nach den
Begutachtungsleitlinien zur Kraftfahreignung (BASt, Stand 19.08.2026).

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
GRUPPE2_KLASSEN = {"C", "C1", "CE", "C1E", "D", "D1", "DE", "D1E"}


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
        elif frei == "1bis2j" and g2 and a.get("epilepsy") != "yes":
            out.append(_f("pruefen", "Epileptische Anfälle", "3.9.6",
                "Anfallsfreiheit 1–2 Jahre (Gruppe-2-Untersuchung)",
                "Gruppe 2: nach erstmaligem unprovoziertem Anfall sind 2 Jahre "
                "Anfallsfreiheit gefordert (nach provoziertem Anfall mit vermeidbarem "
                "Auslöser 6 Monate – Konstellation klären)."))
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
        if a.get("syncope_prodromi") == "no":
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
                "erforderlich, bevor die Fahreignung bejaht wird. Bedingte Fahreignung "
                "mit Auflagen (z.B. Begrenzung von Fahrstrecke/Fahrzeit, keine monotonen "
                "Autobahnfahrten) nur bei bewusster Wahrnehmung der Schläfrigkeit und "
                "verantwortungsvollem Umgang."))
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
    if a.get("sleepiness_coping") == "nein" and (yes("daytime_sleepiness") or yes("microsleep")):
        out.append(_f("pruefen", "Tagesschläfrigkeit", "3.11.1",
            "Schläfrigkeitszeichen werden nicht zuverlässig erkannt / keine Gegenmaßnahmen",
            "Keine bedingte Fahreignung möglich, wenn die Schläfrigkeit nicht "
            "realistisch eingeschätzt wird und kein verantwortungsvoller Umgang "
            "(Pausen, geplanter Kurzschlaf) besteht."))
    if yes("osas"):
        cpap = a.get("cpap")
        if cpap in ("keine", "abgebrochen", "unregelmaessig"):
            out.append(_f("kritisch", "Schlafapnoe", "3.11.2",
                "Diagnostiziertes OSAS ohne konsequent genutzte Therapie",
                "Mittelschweres (AHI 15–29/h) oder schweres (AHI ≥30/h) OSAS in "
                "Verbindung mit Tagesschläfrigkeit schließt die Fahreignung aus; "
                "Eignung nur bei eingehaltener Therapie mit gebesserter Wachheit. "
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
        if a.get("hypoglycemia") in ("repeated", "yes"):  # "yes" = Altdaten (früher yes/no)
            out.append(_f("kritisch", "Diabetes", "3.5",
                "Wiederholte schwere Unterzuckerung mit Fremdhilfe (mindestens zweimal "
                "in 12 Monaten)",
                "Wiederholte schwere Hypoglykämie schließt die Eignung zunächst aus. "
                "Gruppe 1: bei Episoden im Wachzustand in der Regel 3 Monate ab letzter "
                "Episode nicht geeignet (im Einzelfall kürzer oder länger); "
                "fachärztliches Gutachten und regelmäßige ärztliche Kontrollen. "
                "Gruppe 2: in den letzten 12 Monaten keine wiederholte schwere "
                "Hypoglykämie; im günstigen Einzelfall kürzere Frist, mindestens aber "
                "3 Monate bis zur Wiedererlangung. Umstände (wach/Schlaf) klären."))
        elif a.get("hypoglycemia") == "once":
            out.append(_f("pruefen", "Diabetes", "3.5",
                "Einmalige schwere Unterzuckerung mit Fremdhilfe in den letzten "
                "12 Monaten",
                "Eine schwere Hypoglykämie im Wachzustand soll – auch ohne "
                "Fahrzeugführung – Anlass zu einer erneuten Prüfung der Eignung sein; "
                "Stoffwechsellage und Hypoglykämiewahrnehmung sicherstellen."))
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
        if a.get("icd_indication") == "nach_ereignis" and not g2:
            out.append(_f("pruefen", "Defibrillator (ICD)", "3.4.1.4",
                "Sekundärpräventive ICD-Indikation (nach überlebtem Ereignis)",
                "Gruppe 1: Fahreignung frühestens 3 Monate nach Implantation; adäquate "
                "ICD-Funktion und Wundheilung kardiologisch bestätigen lassen."))
        if yes("icd_shock"):
            out.append(_f("kritisch", "Defibrillator (ICD)", "3.4.1.4",
                "ICD-Schockabgabe in den letzten 3 Monaten",
                "Nach adäquater Schockabgabe 3 Monate keine Fahreignung; inadäquate "
                "Schocks müssen sicher verhindert sein (kardiologische Stellungnahme)."))
    if a.get("pacemaker_icd") == "schrittmacher":
        out.append(_f("pruefen", "Herzschrittmacher", "3.4.1.3",
            "Herzschrittmacher-Träger",
            "Gruppe 1: Fahreignung nach Implantation/Aggregatwechsel gegeben, wenn "
            "adäquate Funktion und Wundheilung kardiologisch bestätigt sind. Gruppe 2: "
            "1 Woche Wartefrist (ohne Schrittmacherabhängigkeit und ohne Synkopen, auch "
            "nach Aggregatwechsel), 4 Wochen bei Synkopen, Schrittmacherabhängigkeit "
            "oder Elektrodenwechsel. Regelmäßige kardiologische Kontrollen erforderlich."))
    if a.get("pacemaker_icd") == "vad":
        if g2:
            out.append(_f("kritisch", "Herzunterstützungssystem (VAD)", "3.4.5.2",
                "Träger eines Herzunterstützungssystems (Gruppe-2-Untersuchung)",
                "Gruppe 2: Die Fahreignung ist generell nicht mehr gegeben."))
        else:
            out.append(_f("pruefen", "Herzunterstützungssystem (VAD)", "3.4.5.2",
                "Träger eines Herzunterstützungssystems",
                "Gruppe 1: Fahreignung nur nach individueller kardiologischer/"
                "herzchirurgischer Beurteilung."))
    if yes("heart_attack"):
        out.append(_f("pruefen", "Koronare Herzkrankheit", "3.4.4.1–3.4.4.4",
            "Herzinfarkt / Stent / Bypass in der Vorgeschichte",
            "Wartefristen und Pumpfunktion prüfen (Gruppe 1: nach ACS ab Entlassung "
            "bzw. 4 Wochen bei EF ≤ 35 % oder dekompensierter Herzinsuffizienz, nach "
            "Bypass 2–4 Wochen; Gruppe 2: nach ACS 6 Wochen und nur bei EF > 35 %, "
            "nach PCI 4 Wochen mit jährlichen Kontrollen, nach Bypass 3 Monate). "
            "Aktuellen kardiologischen Befund anfordern."))
    ereignis = a.get("heart_event_when")
    if yes("heart_attack") and ereignis == "unter6w":
        out.append(_f("kritisch" if g2 else "pruefen", "Koronare Herzkrankheit",
            "3.4.4.1–3.4.4.4",
            "Herzinfarkt/Stent/Bypass vor weniger als 6 Wochen",
            "Gruppe 2: nach ACS in den ersten 6 Wochen keine Fahreignung (danach nur "
            "bei EF > 35 %); nach PCI 4 Wochen, nach Bypass 3 Monate. Gruppe 1: nach "
            "ACS ab Klinikentlassung (EF > 35 %) bzw. nach 4 Wochen (EF ≤ 35 % oder "
            "dekompensierte Herzinsuffizienz), nach Bypass 2–4 Wochen. Kardiologische "
            "Untersuchung erforderlich."))
    elif yes("heart_attack") and ereignis == "6w_bis_3m" and g2:
        out.append(_f("pruefen", "Koronare Herzkrankheit", "3.4.4.4",
            "Herzereignis/Eingriff vor 6 Wochen bis 3 Monaten (Gruppe-2-Untersuchung)",
            "Nach Bypassoperation gilt für Gruppe 2 eine Frist von 3 Monaten "
            "(vollständige Rekonvaleszenz einschließlich Sternumstabilität); nach ACS "
            "EF > 35 % nachweisen."))
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
    elif belastung == "stark" and g2:
        out.append(_f("pruefen", "Herzinsuffizienz", "3.4.5",
            "Beschwerden bei stärkerer Belastung (entspricht NYHA II, "
            "Gruppe-2-Untersuchung)",
            "Gruppe 2: Fahreignung bei NYHA I–II nur mit EF > 35 %; jährliche "
            "kardiologische Kontrolluntersuchungen erforderlich."))
    if a.get("low_ef") == "ja":
        out.append(_f("kritisch" if g2 else "pruefen", "Pumpfunktion (EF)",
            "3.4.4.1/3.4.5/3.4.7",
            "Hochgradig eingeschränkte Pumpfunktion angegeben (EF ≤ 35 %)",
            "Gruppe 2: EF ≤ 35 % schließt die Fahreignung nach ACS, bei "
            "Herzinsuffizienz (auch NYHA I–II) und bei Klappenerkrankungen aus. "
            "Gruppe 1: nach ACS 4 Wochen Wartefrist. Aktuellen "
            "Echokardiographie-Befund anfordern."))
    if yes("bp_dizziness"):
        out.append(_f("pruefen", "Blutdrucktherapie", "3.4.2",
            "Schwindel/Schwarzwerden unter Blutdruckmedikation",
            "Therapiebedingter Blutdruckabfall kann zum Kontrollverlust am Steuer "
            "führen – Medikation überprüfen."))
    if yes("bp_organ_symptoms"):
        out.append(_f("kritisch", "Arterielle Hypertonie", "3.4.2",
            "Zerebrale Symptomatik/Sehstörungen im Rahmen der Hypertonie",
            "Bei zerebralen Symptomen oder Sehstörungen im Rahmen einer arteriellen "
            "Hypertonie besteht für beide Gruppen – unabhängig von den gemessenen "
            "Werten – keine Fahreignung, bis die Symptomatik erfolgreich behandelt ist."))
    if a.get("bp_values") == "ueber180":
        out.append(_f("pruefen", "Arterielle Hypertonie", "3.4.2",
            "Blutdruckwerte ≥ 180 mmHg systolisch bzw. ≥ 110 mmHg diastolisch (Grad 3)",
            "Gruppe 2: Werte ≥ 180 und/oder ≥ 110 mmHg können die Fahreignung in Frage "
            "stellen. Beide Gruppen: maligner Hypertonus (Grad-3-Werte mit drohender/"
            "progressiver Organschädigung) schließt die Fahreignung aus. Fachärztliche "
            "Untersuchung und regelmäßige Kontrollen erforderlich."))
    if yes("arrhythmia"):
        out.append(_f("pruefen", "Herzrhythmusstörungen", "3.4.1.1/3.4.1.2",
            "Bekannte Herzrhythmusstörungen",
            "Kardiologische Untersuchung inkl. Langzeit-EKG; rhythmogene Synkopen "
            "schließen die Eignung aus. Anhaltende Kammertachykardien bei "
            "struktureller Herzerkrankung schließen beide Gruppen aus. Gruppe 2: "
            "AV-Block III, Mobitz II und alternierender Schenkelblock schließen die "
            "Eignung aus; polymorphe nicht-anhaltende Kammertachykardien: individuelle "
            "kardiologische Entscheidung."))
    if yes("resuscitated"):
        out.append(_f("kritisch", "Überlebter plötzlicher Herztod", "3.4.10",
            "Zustand nach Reanimation / überlebtem plötzlichem Herztod",
            "Bei Ionenkanalerkrankungen (Brugada-, Short-QT-Syndrom, katecholaminerge "
            "polymorphe VT) ist die Fahreignung nach überlebtem plötzlichem Herztod "
            "nicht gegeben (Gruppe 2 auch mit ICD nicht). Sekundärpräventive "
            "ICD-Versorgung: Gruppe 1 frühestens nach 3 Monaten, Gruppe 2 in der Regel "
            "keine Eignung. Vollständige kardiologische Abklärung erforderlich."))
    if yes("pavk_rest_pain"):
        out.append(_f("kritisch", "pAVK", "3.4.6",
            "pAVK mit Ruheschmerzen",
            "Bei Ruheschmerzen keine Fahreignung (beide Gruppen). Wieder gegeben nach "
            "erfolgreicher Intervention (Gruppe 1: 24 Stunden, Gruppe 2: 1 Woche) bzw. "
            "Operation (Gruppe 1: 1 Woche, Gruppe 2: 4 Wochen) mit unkompliziertem "
            "Verlauf – internistisch-chirurgische Einschätzung erforderlich."))
    elif yes("pavk"):
        out.append(_f("hinweis", "pAVK", "3.4.6",
            "Periphere arterielle Verschlusskrankheit ohne Ruheschmerz",
            "Gruppe 2: klinische Diagnostik empfohlen, um die häufig assoziierte "
            "koronare Herzerkrankung einzubeziehen; bei TIA/Insult gelten die Auflagen "
            "der neurologischen Kapitel."))
    if yes("heart_other"):
        out.append(_f("pruefen", "Herz-/Gefäßerkrankung", "3.4.6.1/3.4.7–3.4.10/3.4.12",
            "Klappenfehler / angeborener Herzfehler / Kardiomyopathie / "
            "Ionenkanalerkrankung / Aneurysma / Karotisstenose angegeben",
            "Je nach Diagnose gelten eigene Fristen und Gruppe-2-Ausschlüsse – u.a. "
            "Aortenaneurysma > 5,5 cm bzw. operationsbedürftig (Gruppe 2: keine "
            "Fahreignung, 3 Monate nach OP wieder möglich; mindestens jährliche "
            "Durchmesserkontrollen); schwere Mitral-/Aortenklappenstenose und schwere "
            "pulmonale Hypertension (Gruppe 2: keine Fahreignung; nach Klappen-OP "
            "Gruppe 1: 2–4 Wochen, Gruppe 2: 3 Monate); HCM mit Synkopen oder "
            "≥ 2 Risikokriterien (Gruppe 2: keine Fahreignung); Long-QT mit Synkopen, "
            "Torsades-de-Pointes oder QTc > 500 ms (beide Gruppen: keine Fahreignung); "
            "Karotisstenose (Gruppe 1: keine Einschränkung, Gruppe 2: nach "
            "neurologischer Untersuchung und effektiver Therapie). Kardiologische "
            "Unterlagen anfordern und nach dem jeweiligen Kapitel beurteilen."))
    if yes("family_sudden_death"):
        out.append(_f("hinweis", "Familienanamnese", "3.4.9.1/3.4.10",
            "Plötzlicher Herztod bei Verwandten 1. Grades",
            "Risikokriterium – bei hypertropher Kardiomyopathie eines von vier "
            "Gruppe-2-Kriterien (zwei davon schließen die Eignung aus); bei "
            "Ionenkanalerkrankungen in die Beurteilung einbeziehen."))

    # ── Gehirn (Kap. 3.9.4 / 3.9.5) ──────────────────────────────────────────
    if yes("stroke"):
        if yes("stroke_residuals"):
            out.append(_f("kritisch", "Schlaganfall/TIA", "3.9.4",
                "Zustand nach Schlaganfall/Hirnblutung/TIA mit fortbestehenden Ausfällen",
                "Relevante neurologische und/oder neuropsychologische Ausfälle (z.B. "
                "Lähmungen, Aphasie, Gesichtsfeldausfälle) schließen die Eignung beider "
                "Gruppen aus. Beurteilung frühestens nach Abschluss einer adäquaten "
                "Rehabilitationsmaßnahme; umschriebene Restausfälle ggf. nach den "
                "Sicherheitsmaßnahmen für körperbehinderte Kraftfahrer (Kap. 3.3) "
                "kompensieren, Schäden am optischen System nach Kap. 3.1 beurteilen."))
            if a.get("stroke_rehab") in ("laufend", "keine"):
                out.append(_f("kritisch", "Schlaganfall/TIA", "3.9.4",
                    "Fortbestehende Ausfälle ohne abgeschlossene Rehabilitation",
                    "Die Eignungsbeurteilung soll frühestens nach Abschluss einer "
                    "adäquaten Rehabilitationsmaßnahme erfolgen – derzeit keine "
                    "Fahreignung anzunehmen."))
        else:
            out.append(_f("pruefen", "Schlaganfall/TIA", "3.9.4",
                "Zustand nach Schlaganfall/Hirnblutung/TIA",
                "Nach erfolgreicher Therapie kann – abhängig vom Einzelfall – bedingt "
                "wieder Fahreignung angenommen werden. Nach TIA mit Bewusstseinsstörung "
                "oder relevanten Ausfällen nur, wenn nach Diagnostik und Therapie keine "
                "signifikant erhöhte Rezidivgefahr besteht. Gruppe 2: gruppenspezifische "
                "Anforderungen (besondere Verantwortung) und Belastungen (z.B. "
                "unregelmäßige Arbeitszeiten) angemessen berücksichtigen. "
                "Nachuntersuchungen je nach Lage des Falles, bei fortschreitenden "
                "Krankheitsbildern in individuellen Abständen."))
        if a.get("stroke_prevention") == "no":
            out.append(_f("pruefen", "Schlaganfall/TIA", "3.9.4",
                "Keine Ursachenabklärung/Sekundärprophylaxe nach Schlaganfall/TIA "
                "angegeben",
                "Ohne entsprechende Diagnostik und Therapie ist eine signifikant "
                "erhöhte Rezidivgefahr nicht auszuschließen – risikolose Teilnahme am "
                "Straßenverkehr ist dann nicht gegeben; fachneurologische Abklärung "
                "anfordern."))
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
                "Krankheitsbild und attackenfreie Fristen klären (z.B. Menière "
                "Gruppe 1: mit Prodromi 6 Monate Beobachtung ab Diagnose, ohne "
                "Prodromi 1 Jahr attackenfrei; Gruppe 2: 2 Jahre mit / 4 Jahre ohne "
                "Prodromi; vestibuläre Migräne deutlich kürzer); HNO-fachärztliche "
                "Untersuchung."))
        if yes("vertigo_positional"):
            out.append(_f("pruefen", "Schwindel", "3.10.1",
                "Lageabhängiger Schwindel (V.a. gutartiger Lagerungsschwindel)",
                "Fahreignung erst nach erfolgreicher Therapie/Spontanremission "
                "(Nachweis per Lagerungsprüfung)."))
        if yes("vertigo_ear"):
            out.append(_f("pruefen", "Schwindel", "3.10.1",
                "Drehschwindel mit Ohrsymptomen (V.a. Morbus Menière)",
                "Fristen abhängig von Prodromi und Gruppe: Gruppe 1 mit Prodromi "
                "6 Monate Beobachtung, ohne Prodromi 1 Jahr attackenfrei; Gruppe 2 "
                "mindestens 2 bzw. 4 Jahre Attackenfreiheit; keine Fahreignung für "
                "einspurige Fahrzeuge; fachärztliche Abklärung."))
        if yes("vertigo_migraine"):
            schwere = "kritisch" if (g2 and prodromi == "nie"
                                     and letzte in ("unter3m", "3bis6m", "6bis12m")) else "pruefen"
            out.append(_f(schwere, "Schwindel", "3.10.2",
                "Schwindelanfälle im Zusammenhang mit Migräne (V.a. vestibuläre Migräne)",
                "Gruppe 1: mit Prodromi im Intervall uneingeschränkt geeignet, ohne "
                "Prodromi 6 Monate attackenfreie Beobachtungszeit. Gruppe 2: mit "
                "Prodromi 6 Monate Beobachtungszeit, ohne Prodromi 12–24 Monate "
                "attackenfrei (je nach Schweregrad); fachärztliche Untersuchung bzw. "
                "Begutachtung (Gruppe 2)."))
        if yes("vertigo_situational"):
            out.append(_f("pruefen", "Schwindel", "3.10.4",
                "Situationsabhängiger Schwindel (V.a. funktionelle Schwindelform / "
                "phobischer Schwankschwindel)",
                "Keine Einschränkung der Fahreignung, außer Fahrsituationen sind "
                "Auslöser des Schwindels – dann fachärztliche Untersuchung (ggf. "
                "psychiatrisch/psychosomatisch, siehe Kap. 3.12); "
                "Einzelfallbeurteilung."))
    if yes("ear_disease"):
        out.append(_f("pruefen", "Schwindel", "3.10.1",
            "Diagnostizierte Erkrankung des Gleichgewichtsorgans/Innenohrs",
            "Fahreignung je nach Krankheitsbild erst nach erfolgreicher Therapie bzw. "
            "Kompensation und fachärztlicher HNO-Untersuchung: BPLS nur nach "
            "erfolgreicher Therapie/Spontanremission (Lagerungsprüfung); akute/"
            "bilaterale Vestibulopathie nur bei nachgewiesener Kompensation; "
            "Vestibularisparoxysmie nach 3 Monaten attackenfreier Beobachtung; "
            "Bogengangsfistel/Radikalhöhle nach operativer Sanierung (ggf. Auflagen "
            "wie Ohrstöpsel)."))
    if yes("vertigo") or yes("ear_disease"):
        klassen = a.get("license_classes") or []
        if any(k in ("AM", "A1", "A2", "A") for k in klassen):
            out.append(_f("pruefen", "Schwindel", "3.10.1",
                "Schwindel/Gleichgewichtsstörung bei beantragter oder vorhandener "
                "Motorradklasse (einspurige Fahrzeuge)",
                "Für einspurige Kraftfahrzeuge gelten strengere Maßstäbe: bei Morbus "
                "Menière, bilateraler Vestibulopathie oder persistierendem "
                "vollständigem Vestibularisausfall (auch nach Vestibularisschwannom) "
                "ist die Fahreignung für einspurige Fahrzeuge nicht gegeben."))

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

    # ── Alkohol, Cannabis, Drogen, Medikamente (Kap. 3.13/3.14) ──────────────
    if yes("alcohol_dependence"):
        out.append(_f("kritisch", "Alkohol", "3.13.1.1",
            "Alkoholabhängigkeit bzw. Entgiftung/Entwöhnung in der Vorgeschichte",
            "Bei Abhängigkeit keine Eignung. Wiedererlangung erst nach "
            "Entzugsbehandlung und suchtspezifischer Rehabilitation mit belegter "
            "Abstinenz von mindestens 12 Monaten; bei ambulanter Reha oder ohne "
            "therapeutische Unterstützung 15 Monate (davon 3 Monate nach "
            "Maßnahmenende). Liegt die belegte Abstinenz länger zurück, genügt der "
            "Nachweis der letzten 3 Monate vor Begutachtung."))
    if yes("alcohol_traffic"):
        out.append(_f("pruefen", "Alkohol", "3.13.1.2",
            "Verkehrsauffälligkeit unter Alkohol (Trunkenheitsfahrt/MPU)",
            "Missbrauchsverdacht – Trennvermögen und Trennbereitschaft klären. "
            "Wiederherstellung erst nach beendetem, gefestigtem riskanten "
            "Konsumverhalten oder Konsumverzicht (in der Regel 1 Jahr, frühestens "
            "6 Monate); ggf. Kurs für alkoholauffällige Fahrer nach § 70 FeV "
            "(§ 11 Abs. 10 FeV)."))
    if yes("alcohol_control"):
        out.append(_f("pruefen", "Alkohol", "3.13.1.2",
            "Kontrollverlust über den Alkoholkonsum angegeben",
            "Leitlinien-Indiz für Missbrauch – Konsummuster sowie ICD-10-Kriterien "
            "für schädlichen Gebrauch (F1x.1) und Abhängigkeit (F1x.2) explorieren."))
    elif a.get("alcohol") == "taeglich":
        out.append(_f("pruefen", "Alkohol", "3.13.1.2",
            "(Fast) täglicher Alkoholkonsum",
            "Konsummuster hinsichtlich Gewöhnung/Missbrauch explorieren (Labor: "
            "z.B. CDT/GGT erwägen)."))
    if yes("alcohol_binge"):
        out.append(_f("pruefen", "Alkohol", "3.13.1.2",
            "Rauschtrinken (größere Mengen Alkohol in kurzer Zeit)",
            "Riskantes Konsummuster (Binge drinking) ist Leitlinien-Indiz für "
            "Alkoholmissbrauch – Konsumform (Sturztrunk, hochprozentige Spirituosen), "
            "Mischkonsum und Trennverhalten explorieren."))
    if a.get("cannabis") in ("gelegentlich", "regelmaessig", "taeglich"):
        if yes("cannabis_medical"):
            out.append(_f("pruefen", "Dauermedikation", "3.14.2",
                "Einnahme von ärztlich verordnetem Medizinalcannabis",
                "Bestimmungsgemäße Einnahme eines verschriebenen Arzneimittels fällt "
                "nicht unter Kap. 3.13.2, sondern unter die Dauerbehandlung mit "
                "Arzneimitteln: Intoxikationen und leistungsmindernde Nebenwirkungen "
                "ausschließen, ärztliche Überwachung mit Nachweis; zusätzlichen nicht "
                "verordneten Konsum abklären."))
        elif a.get("cannabis") == "taeglich":
            out.append(_f("kritisch", "Cannabis", "3.13.2.2",
                "Täglicher oder fast täglicher Cannabiskonsum",
                "Chronisches Konsummuster mit zu erwartender ausgeprägter "
                "Toleranzbildung ist Leitlinien-Indiz für Cannabismissbrauch; bei "
                "Missbrauch keine Eignung. Wiederherstellung nach gefestigter Änderung "
                "des Konsumverhaltens oder Konsumverzicht (in der Regel 1 Jahr, "
                "frühestens 6 Monate); Abhängigkeitskriterien nach ICD-10 prüfen "
                "(dann Kap. 3.13.2.1)."))
        elif a.get("cannabis") == "regelmaessig":
            out.append(_f("pruefen", "Cannabis", "3.13.2.2",
                "Regelmäßiger (mehrmals wöchentlicher) Cannabiskonsum",
                "Missbrauchsverdacht – riskantes Konsummuster, Mischkonsum sowie "
                "Trennvermögen und Trennbereitschaft (Wartezeit zwischen Konsum und "
                "Fahrtantritt, rechtliche Grenzwerte) klären; ICD-10-Kriterien für "
                "schädlichen Gebrauch/Abhängigkeit explorieren."))
        else:
            out.append(_f("hinweis", "Cannabis", "3.13.2.2",
                "Gelegentlicher Cannabiskonsum",
                "Gelegentlicher Konsum schließt die Eignung nicht per se aus; "
                "entscheidend ist ein hinreichend sicheres Trennverhalten "
                "(ausreichende Wartezeit zwischen Konsum und Fahrtantritt, "
                "Einhaltung der rechtlichen Grenzwerte)."))
    if yes("cannabis_traffic"):
        out.append(_f("pruefen", "Cannabis", "3.13.2.2",
            "Verkehrsauffälligkeit unter Cannabiseinfluss",
            "Hinweis auf fehlendes Trennverhalten (Missbrauchsverdacht) – "
            "Wiederherstellung erst nach gefestigter Konsumänderung oder "
            "Konsumverzicht (in der Regel 1 Jahr, frühestens 6 Monate); ggf. Kurs für "
            "cannabisauffällige Fahrer nach § 70 FeV (§ 11 Abs. 10 FeV)."))
    if yes("mixed_consumption"):
        out.append(_f("pruefen", "Alkohol/Cannabis", "3.13.1.2/3.13.2.2",
            "Häufiger Mischkonsum von Cannabis mit Alkohol oder anderen Substanzen",
            "Mischkonsum ist Leitlinien-Indiz für Missbrauch – Konsumverhalten und "
            "Trennverhalten für beide Substanzen explorieren."))
    if yes("drug_dependence"):
        out.append(_f("kritisch", "Abhängigkeit", "3.13.2.1/3.14.1",
            "Cannabis- bzw. Drogenabhängigkeit oder Entzugs-/Entwöhnungsbehandlung "
            "in der Vorgeschichte",
            "Bei Abhängigkeit keine Eignung. Wiedererlangung erst nach Entzug und "
            "suchtspezifischer Rehabilitation mit belegter Abstinenz von mindestens "
            "12 Monaten (ambulante Reha/Selbstheiler: 15 Monate); bei "
            "Betäubungsmitteln Nachweis über mindestens 4 unvorhersehbar anberaumte "
            "Laborkontrollen innerhalb der Jahresfrist."))
    if yes("drugs"):
        out.append(_f("pruefen", "Betäubungsmittel", "3.14.1",
            "Konsum anderer Drogen (außer Cannabis) aktuell oder in der Vorgeschichte",
            "Einnahme von Betäubungsmitteln schließt die Eignung aus (außer "
            "bestimmungsgemäße Einnahme eines verschriebenen Arzneimittels); nach "
            "Abhängigkeit einjährige Abstinenz mit mindestens 4 unvorhersehbar "
            "anberaumten Laborkontrollen nachweisen (bei ambulanter Reha oder ohne "
            "therapeutische Unterstützung 15 Monate, vgl. Kap. 3.13.1.1/3.13.2.1)."))
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
            "Fachärztliche (HNO-)Eignungsuntersuchung bei Führerscheinerwerb, "
            "regelmäßige ärztliche Kontrollen und Nachweis von 3 Jahren Fahrpraxis "
            "mit Klasse B erforderlich; maßgebend ist das Tonaudiogramm ohne "
            "Hörhilfe (besseres Ohr, Hörverlust > 60 %, Vierfrequenztabelle nach "
            "Roeser); assoziierte Erkrankungen mitbeurteilen."))
        if a.get("license_years") in ("erstantrag", "unter3"):
            out.append(_f("pruefen", "Hörvermögen", "3.2",
                "Für Gruppe 2 geforderte 3-jährige Fahrpraxis (Klasse B) laut "
                "Angabe noch nicht erfüllt",
                "Vorherige Bewährung von 3 Jahren Fahrpraxis auf Kfz der Klasse B "
                "ist Voraussetzung der bedingten Eignung."))
    if yes("hearing_impaired") and (yes("vertigo") or yes("eye_disease")
                                    or yes("one_eyed") or yes("night_vision")):
        out.append(_f("pruefen", "Hörvermögen", "3.2",
            "Hochgradige Schwerhörigkeit/Gehörlosigkeit zusammen mit Seh- bzw. "
            "Gleichgewichtsstörung",
            "Eignung setzt voraus, dass keine weiteren schwerwiegenden Mängel "
            "(z.B. Sehstörungen, Gleichgewichtsstörungen) vorliegen; assoziierte "
            "Erkrankungen fachärztlich abklären (HNO, ggf. weitere "
            "Fachdisziplinen)."))

    # ── Bewegungsapparat (Kap. 3.3) ──────────────────────────────────────────
    if yes("mobility_limits") or yes("prosthesis"):
        out.append(_f("pruefen", "Bewegungsapparat", "3.3",
            "Dauerhafte Bewegungseinschränkung bzw. Prothese/orthopädisches "
            "Hilfsmittel",
            "Kompensierbarkeit nach Anhang B (Sicherheitsmaßnahmen bei "
            "körperbehinderten Kraftfahrern) prüfen: Prothesenverträglichkeit, "
            "Belastbarkeit bei Langzeitbelastung, Restfunktionen; ggf. Fahrprobe "
            "und Beschränkungen/Auflagen (Fahrzeugumbau); Kap. 3.9.1-3.9.3 "
            "mitbeachten."))
    if yes("vehicle_modified"):
        out.append(_f("hinweis", "Bewegungsapparat", "3.3",
            "Fahrzeug wegen körperlicher Einschränkung umgebaut",
            "Passung der Umbauten nach Anhang B und Eintragung der "
            "Beschränkungen/Auflagen im Führerschein kontrollieren."))

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
        out.append(_f("pruefen", "Transplantation", "3.6/3.7/3.4.5.1",
            "Zustand nach Organtransplantation",
            "Organfunktion, Immunsuppressions-Nebenwirkungen und Nachsorge prüfen; "
            "nach Nierentransplantation jährliche Nachbegutachtung, Herz: Gruppe 2 "
            "in der Regel keine Eignung, Ausnahme frühestens 5 Jahre nach "
            "Transplantation bei stabilen Verhältnissen (3.4.5.1)."))
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
        out.append(_f("pruefen", "Verkehrsvorgeschichte", "3.13/3.16/3.17",
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
            "Kraftfahreignung (BASt, Stand 19.08.2026). Entscheidungsunterstützung – "
            "die abschließende Beurteilung obliegt der Ärztin/dem Arzt."
        ),
    }
