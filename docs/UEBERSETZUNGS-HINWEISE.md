# Übersetzungs-Hinweise für die ärztliche Durchsicht

Alle Sprachdateien (`backend/questionnaires/i18n/`) sind maschinell übersetzt
(`machine_translated: true`) und strukturell gegen den deutschen Master geprüft.
Die Übersetzungs-Agenten haben folgende fachliche Entscheidungen und Prüfpunkte
notiert — bitte insbesondere die Einwilligungs-/Datenschutztexte und die
ESS-Formulierungen der wichtigsten Patientensprachen ärztlich freigeben.

## Batch 1: en, fr, it, es, pt, nl

Alle sechs Dateien liegen in C:\Users\Admiral\Documents\Django\fragebogen\backend\questionnaires\i18n\ und wurden vollständig gegen de.json geprüft (json.load OK, rekursiv identische Schlüsselmenge, _meta korrekt mit machine_translated=true, Platzhalter {current}/{total} intakt, Eigennamen/Adresse, DSGVO, FeV, Führerscheincodes sowie ESS/CPAP/ICD/AHI/MPU unverändert erhalten). Drei Präzisierungen wurden im Prüfdurchgang korrigiert: fr privacy_subtitle „(RGPD allemand)" → „(RGPD)" (die DSGVO ist die EU-Verordnung, kein deutsches Gesetz); it diabetes_type-Laienerklärung zu „malattia dello zucchero nel sangue" geglättet; es diabetes_type „(azúcar en la sangre)" → „(azúcar alta en la sangre)". Ärztlich prüfen lassen sollte man: (1) Titelbegriff „Verkehrsmedizin": en „Traffic Medicine" (Alternative wäre „Fitness to Drive"), fr „médecine du trafic" (eher schweizerische Prägung), es „medicina de tráfico", pt „medicina de tráfego" – in Spanien/Portugal ist der Begriff weniger etabliert als „reconocimiento/exame médico para conductores". (2) ESS-Items wurden sinngemäß an die offiziellen Landesversionen angelehnt, entsprechen aber nicht wortgleich den validierten Übersetzungen (z. B. offizielles engl. Item 8: „In a car, while stopped for a few minutes in the traffic") – falls die validierte Skala formal gefordert ist, Originalwortlaut je Sprache einsetzen. (3) band_severe „Ausgeprägt" ist uneinheitlich abgestuft: en „Severe", fr „Marqué", it „Marcato", es „Marcado", pt „Acentuado", nl „Sterk verhoogd". (4) en diabetes_type-Gloss „(high blood sugar disease)" für „Zuckerkrankheit" ist unüblich – ggf. einfach streichen. (5) nl ear_disease ergänzt „(BPPD)" als Abkürzung, die der deutsche Text nicht enthält. (6) „Dialyse (Blutwäsche)"-Laienglossen: en „blood washing", fr „épuration du sang", pt „limpeza do sangue", nl „bloedspoeling" – Verständlichkeit ok, aber unüblich als Fachjargon. (7) Genusformen: it/pt/es verwenden teils Paarformen (limitato/a), Spanisch stellenweise generisches Maskulinum („¿está ciego de un ojo?", „despierto") – bei Wunsch nach durchgängig geschlechtsneutraler Anrede nacharbeiten. (8) pt ist Europäisches Portugiesisch (carta de condução, autocarro, „A carregar…"); für brasilianische Patienten wären einzelne Begriffe (carteira de motorista, ônibus) geläufiger. (9) DSGVO-Artikelzitate wurden im deutschen Format belassen („Art. 6 Abs. 1 lit. a") mit lokaler Abkürzung als Klammerzusatz (GDPR/RGPD/AVG) – juristisch nachvollziehbar, aber für Laien sperrig.

## Batch 2: sk, hu, ro, bg

SELBSTKONTROLLE (System-Python, PYTHONUTF8=1): Alle 4 Dateien json.load erfolgreich, rekursiv identische Schlüsselmenge wie de.json (0 fehlend / 0 extra; einzige zulässige Abweichung: _meta.machine_translated). Keine leeren Werte. UTF-8 ohne BOM, Einrückung 1. {current}/{total} in ui.question_of in allen 4 Dateien unverändert vorhanden. Prüfskript: C:\Users\Admiral\AppData\Local\Temp\claude\C--Users-Admiral-Documents-Django-leiche-zugferd-invoice\d423dcf1-15d6-451c-8d40-49932ccb6b58\scratchpad\check_i18n.py

NICHT ÜBERSETZT (bewusst, wie vorgegeben):
- questions.license_classes.options: alle 14 Klassen-Codes (AM…T) wörtlich übernommen — automatisch verifiziert als einzige mit dem Deutschen identische Werte.
- ui.privacy_controller: "Dr. med. Björn Micka, Betriebsmedizin · Notfallmedizin, Christoph-Dassler-Str. 22, 91074 Herzogenaurach" komplett unverändert. ENTSCHEIDUNG ZUR PRÜFUNG: Auch die Fachgebietsbezeichnung "Betriebsmedizin · Notfallmedizin" blieb deutsch, da sie zum Briefkopf/Praxisnamen gehört und Regel 6 (nichts hinzufügen) einen erklärenden Klammerzusatz nicht eindeutig deckt. Falls für Patienten verständlicher gewünscht, bitte freigeben — dann ergänze ich in allen Sprachen einen Klammerzusatz.
- DSGVO-Verweise als "Art. 6 / Art. 9 / Art. 13 DSGVO" beibehalten; nur in privacy_subtitle je Sprache ein erklärender Klammerzusatz ("všeobecné nariadenie o ochrane údajov" / "általános adatvédelmi rendelet, 13. cikk" / "Regulamentul general privind protecția datelor" / "Общ регламент относно защитата на данните, чл. 13"). Absatz-/Buchstabenzusätze wurden landesüblich formatiert (sk "ods./písm.", hu "(1) a) pont", ro "alin./lit.", bg "ал./буква").
- ESS, CPAP, ICD, AHI, MPU, NYHA, AV(-Block), (Long-)QT, PDF bleiben als Abkürzung; MPU trägt in allen Sprachen die Erklärung, wo der deutsche Text eine hat (questions.license_withdrawn ausgeschrieben wie im Deutschen; questions.alcohol_traffic mit Kurzerklärung, da der deutsche Text dort nur "MPU" nennt — dies ist eine minimale Verständnishilfe, bitte gegenprüfen, ob das gewünscht ist).

RECHTSVERWEIS "Anlage 5 FeV" (questions.psych_test_done.hint): Code beibehalten, dazu je Sprache ein Klammerzusatz, dass es sich um die deutsche Fahrerlaubnis-Verordnung handelt (sk "prílohy 5 FeV (nemecké nariadenie o vodičských preukazoch)", hu "Anlage 5 FeV (a német vezetőiengedély-rendelet 5. melléklete)", ro "Anlage 5 FeV (anexa 5 la regulamentul german privind permisele de conducere)", bg "Anlage 5 FeV (приложение 5 към германската наредба за свидетелствата за управление)"). Bitte bestätigen, dass diese Auflösung fachlich korrekt ist.

ZEITFENSTER: Alle Zeitangaben 1:1 erhalten und stichprobenartig gegengelesen — "in den letzten 24 Monaten", "letzte 12 Monate", "letzte 3 Monate" (ICD-Schock), "weniger als 6 Monate" (Synkope), "weniger als 3 Monate" (Kopfverletzung/Antiepileptika-Ende) sowie sämtliche Optionsstufen von seizure_free (unter3m…ueber5j) und vertigo_last (unter3m…ueber2j). Keine Verschiebung von Grenzen; "3 bis 6 Monate" wurde inklusiv-neutral wiedergegeben (sk "3 až 6 mesiacov", hu "3–6 hónapja", ro "Între 3 și 6 luni", bg "От 3 до 6 месеца").

LAIENVERSTÄNDLICHE ENTSPRECHUNGEN (Fachbegriff + Laienbegriff wie im deutschen Original):
- "Unterzuckerung" → sk "pokles cukru v krvi", hu "vércukoresés", ro "scădere a glicemiei", bg "спадане на кръвната захар" (durchgängig, auch in diabetes_therapy-Optionen und Sektions-Untertitel).
- "Dialyse (Blutwäsche)" → sk "dialýza (čistenie krvi)", hu "dialízis (művesekezelés)", ro "dializă (spălarea sângelui)", bg "диализа (кръвоочистване)".
- "Grauer/Grüner Star" → sk "sivý zákal / zelený zákal (glaukóm)", hu "szürkehályog / zöldhályog (glaukóma)", ro "cataractă / glaucom", bg "катаракта/перде / глаукома". HINWEIS: Im Rumänischen gibt es keinen etablierten Laienbegriff analog zu "Grauer Star"; dort steht der Fachbegriff allein.
- "Schlaganfall/TIA": hu Sektionstitel als "Agyvérzés/agyi történés és az agy" gefasst, weil "stroke" im Ungarischen umgangssprachlich meist als "agyvérzés" erscheint, medizinisch aber weiter ist — bitte prüfen, ob "Stroke" oder "agyi érkatasztrófa" bevorzugt wird. In questions.stroke sind beide Begriffe genannt.
- "Sekundenschlaf" → sk "mikrospánok", hu "mikroalvás", bg umschrieben "кратък сън за секунди", ro umschrieben "momente de ațipire de câteva secunde" (kein etablierter Einwortbegriff).

GRAMMATISCHES GESCHLECHT: Bei Partizipien/Adjektiven, die sich auf die befragte Person beziehen, wurden neutrale Doppelformen gesetzt: sk "eingeschränkt" → "obmedzený(á)", ro "diagnosticat(ă)", bg "сляп(а)", "буден(на)". Ungarisch ist geschlechtsneutral, dort nicht nötig. Falls die UI solche Klammerformen nicht gewünscht sind, bitte melden — dann auf durchgehend maskuline oder rein neutrale Formulierungen umstellen.

ANREDE: Durchgängig höfliche Sie-Form. sk "Vy/vaše" (kleingeschrieben, slowakische Norm), ro "dumneavoastră", bg Höflichkeitsform mit großgeschriebenem "Вие/Вашият". Ungarisch: unpersönliche Höflichkeitskonstruktion ("Ön") bzw. Verbformen ohne Anredepronomen, wo natürlicher.

BESONDERE STELLE hu ui.question_of: Deutsch "Frage {current} von {total}" wurde als "{current}. kérdés a következőből: {total}" gesetzt, weil eine wörtliche Konstruktion im Ungarischen ungrammatisch wäre. Platzhalter unverändert. Falls im UI zu lang, wäre "{current} / {total}. kérdés" eine kürzere Alternative — bitte entscheiden.

WEITERE PRÜFPUNKTE FÜR DIE ÄRZTLICHE DURCHSICHT:
- exam_occasion.fahrgast "Mietwagen" wurde als "Mietwagen mit Fahrer" (Personenbeförderung) verstanden und entsprechend übersetzt (sk "prenajaté vozidlo s vodičom", hu "bérelt gépkocsi sofőrrel", ro "mașină închiriată cu șofer", bg "автомобил под наем с шофьор") — nicht als Selbstfahrer-Mietwagen. Bitte bestätigen.
- exertion_symptoms.hint "NYHA-Stadien": Abkürzung beibehalten, ohne Auflösung (wie im Deutschen).
- multiple_conditions.hint "Leitlinien Kap. 2.7": als "Leitlinien/Richtlinien, Kap. 2.7" ohne Nennung des konkreten Regelwerks übersetzt (wie im Deutschen).
- osas.followup "Schweregrad bzw. AHI-Wert": AHI unübersetzt, "(falls bekannt)" erhalten.
- alcohol_traffic.followup "Promillewert": sk "hodnota alkoholu v krvi", hu "véralkoholérték", ro "valoare a alcoolemiei", bg "стойност на алкохола" — die Promille-Einheit wurde nicht als Zahleneinheit fixiert, da in BG/RO üblicherweise in ‰ bzw. mg/l angegeben wird. Inhaltlich unverändert.
- band_normal im Rumänischen lautet "Normal (0–9)" und ist damit zeichengleich mit dem Deutschen — das ist korrektes Rumänisch, kein unübersetzter Rest.

## Batch 3: mk, tr, da, sv

SELBSTKONTROLLE (bestanden, Prüfskript: C:\Users\Admiral\AppData\Local\Temp\claude\C--Users-Admiral-Documents-Django-leiche-zugferd-invoice\d423dcf1-15d6-451c-8d40-49932ccb6b58\scratchpad\check_i18n.py)
- Alle 4 Dateien: json.load erfolgreich, UTF-8 ohne BOM, native Schrift, Einrückung 1.
- Rekursive Schlüsselmenge identisch mit de.json (446 Pfade) + genau 1 zulässiger Zusatz je Datei: /_meta/machine_translated. Keine fehlenden, keine überzähligen Schlüssel.
- {current}/{total} in ui.question_of in allen Dateien vorhanden. Optionsschlüssel (yes/type1/lkw/<1/>4/…) und Führerscheinklassen-Codes unverändert.
- _meta-Konvention deckt sich mit den 24 bereits vorhandenen Sprachdateien (language/name/machine_translated: true).
- Kein Registrierungsschritt nötig: backend/questionnaires/translations.py::available_languages() ermittelt die Sprachen per Glob über i18n/*.json; die neuen Codes sind damit sofort über /api/i18n/ verfügbar.

ÜBERSETZUNGSENTSCHEIDUNGEN, DIE ÄRZTLICHE DURCHSICHT BRAUCHEN

1. Anrede da/sv: In Dänisch und Schwedisch ist "du" die normale höfliche Patientenanrede; "De"/"Ni" wirkt heute archaisch bzw. distanzierend. Beide Dateien verwenden durchgehend "du". mk und tr verwenden die höfliche Mehrzahlform ("Вие"-Register bzw. "-siniz"). Falls bewusst formeller gewünscht, müsste da/sv komplett auf De/Ni umgestellt werden.

2. Nicht übersetzt (laut Vorgabe): "Dr. med. Björn Micka, Betriebsmedizin · Notfallmedizin, Christoph-Dassler-Str. 22, 91074 Herzogenaurach". Der Fachgebietszusatz "Betriebsmedizin · Notfallmedizin" steht damit in allen vier Sprachen deutsch im Datenschutztext – bitte prüfen, ob das so gewollt ist oder ob ein Klammerzusatz in der Zielsprache ergänzt werden soll.

3. Rechtsverweise stehen unverändert, mit Klammererklärung in der Zielsprache:
   - "Art. 13 DSGVO" / "Art. 6 Abs. 1 lit. a, Art. 9 Abs. 2 lit. a DSGVO" – Zusatz sinngemäß "EU-Datenschutz-Grundverordnung".
   - "Anlage 5 FeV" in psych_test_done.hint – Zusatz sinngemäß "deutsche Fahrerlaubnis-Verordnung". Hinweis: der Master nennt hier Anlage 5 FeV (nicht § 11 FeV); das wurde 1:1 übernommen.
   - MPU: Abkürzung erhalten. In license_withdrawn steht wie im Deutschen die Langform davor. In alcohol_traffic hat der deutsche Text nur "MPU" ohne Erklärung – dort wurde in allen vier Sprachen eine kurze Auflösung in Klammern ergänzt ("MPU – medizinisch-psychologische Untersuchung"), weil die Abkürzung außerhalb Deutschlands unbekannt ist. Das ist die einzige inhaltliche Ergänzung gegenüber dem Master; bitte freigeben oder streichen lassen.

4. Fachabkürzungen unverändert: ESS, CPAP, ICD, AHI, NYHA, TIA (mk in Kyrillisch: ТИА), AV-Block, Long-QT, COPD/KOAH/KOL. Bei COPD wurde jeweils die landesübliche Form gewählt: tr "KOAH", da "KOL", sv "KOL", mk "COPD" (in Nordmazedonien gebräuchlich). Falls für die Aktenführung die einheitliche Form "COPD" gewünscht ist, wären tr/da/sv anzupassen.

5. Laienbegriffe analog zum deutschen Muster ergänzt, wo die Zielsprache sonst rein fachsprachlich wäre – nur als erklärende Klammer, ohne Bedeutungsänderung: Kardiologe → "Herzarzt" (da "hjertelæge", sv "hjärtläkare", tr "kalp doktoru", mk "специјалист за срце"); Nephrologe → "Nierenarzt" (tr, mk); Epilepsie → tr "epilepsi (sara)". Der deutsche Master macht dasselbe bei "Grauer Star/Glaukom" und "Diabetes mellitus (Zuckerkrankheit)".

6. Zeitfenster wurden wörtlich erhalten und stichprobenartig gegengeprüft: "in den letzten 24 Monaten", "letzten 12 Monaten", "letzten 3 Monaten", "weniger als 3 Monate", "weniger als 6 Monate", alle Optionsstufen von seizure_free (unter3m … ueber5j) und vertigo_last (unter3m … ueber2j) sowie antiepileptics (ende_unter3m/ende_ueber3m). Keine Auslassungen, keine Zusammenfassungen.

7. Formulierungen, die eine fachliche Zweitmeinung verdienen:
   - "Bewegungsapparat": mk "Мускулно-скелетен систем", tr "Hareket sistemi", da "Bevægeapparat", sv "Rörelseapparaten".
   - "Stoffwechselentgleisung" (diabetes_derailment): mk "растројство на метаболизмот", tr "metabolizmanın kontrolden çıkması", da "et stofskifte ude af kontrol", sv "urspårning av ämnesomsättningen" – bewusst laiennah statt rein fachsprachlich.
   - "Sekundenschlaf" (microsleep): tr "mikro uyku (saniyelik uyku)", da "mikrosøvn", sv "sekundsömn", mk "микросон".
   - "Lagerungsschwindel": da "lejringssvimmelhed", sv "lägesyrsel", tr "pozisyonel baş dönmesi", mk "позициона вртоглавица".
   - "Fahreignung/Fahrerlaubnis": da "køreegnethed"/"kørekort", sv "körlämplighet"/"körkort", tr "araç kullanma yeterliliği"/"sürücü belgesi", mk "способност за возење"/"возачка дозвола".
   - exam_occasion "PKW / andere Klasse": da/sv "Personbil / anden kategori" bzw. "annan behörighet", tr "Otomobil / diğer sınıf", mk "Патничко возило / друга категорија".

8. Bewusst identisch mit dem deutschen Wortlaut (Kognate, kein Übersetzungsfehler): ui.band_normal "Normal (0–9)" in tr/da/sv; ui.yes "Ja" in da/sv; sections.schlaf.subtitle "Inkl. Epworth Sleepiness Scale (ESS)" in da/sv; diabetes_therapy.insulin "Insulin" in da/sv; pacemaker_icd.icd "Defibrillator (ICD)" in da/sv; exam_occasion.bus "Bus (D, D1, DE, D1E)" in da.

9. mk ist wie vorgegeben in kyrillischer Schrift (anders als das bestehende sr.json, das laut _meta bewusst Latein verwendet) – für Mazedonisch gibt es keine amtliche Lateinschreibung, daher Kyrillisch. Enthält die korrekten Apostroph-Formen 'рбет / 'ркате; im JSON unproblematisch, aber bei Font-/Renderingtests im Frontend kurz gegenprüfen.

## Batch 4: hr, sl, sr, bs

PRÜFUNG (eigenes Skript, System-python, unabhängig vom gemeinsam genutzten check_i18n.py, das parallel von anderen Jobs überschrieben wurde):
Alle 4 Dateien: json.load erfolgreich, 447 Schlüssel (= 446 Master-Schlüssel + _meta.machine_translated), 319 Blatt-Strings, keine fehlenden/überzähligen Schlüssel, keine leeren Werte, Options-Schlüssel byte-identisch zum Master, {current}/{total} intakt und in keinem anderen String geschweifte Klammern, Eigenname + Adresse in privacy_controller wörtlich erhalten, UTF-8 ohne BOM, sr.json enthält keinerlei kyrillische Zeichen (reine latinica).

ÜBERSETZUNGSENTSCHEIDUNGEN (bitte fachlich gegenlesen):

1. Sprachvarianten: hr = ijekavisch/kroatischer Wortschatz (liječnik, tjedan, tlak → "krvni tlak", zrak). sr = ekavisch, lateinische Schrift, serbischer Wortschatz (lekar, nedeljno, pritisak, vazduh, saobraćaj). bs = ijekavisch mit bosnischem Wortschatz (ljekar, sedmica, pritisak, zrak, saobraćaj, općenito). sl = slowenisch. sr/bs sind daher bewusst NICHT identisch mit hr.

2. "Betriebsmedizin · Notfallmedizin" in privacy_controller wurde deutsch belassen (Teil der Briefkopf-Bezeichnung), mit Klammerzusatz in der Zielsprache ("medicina rada · urgentna medicina" bzw. "medicina dela · urgentna medicina"). Falls unerwünscht, den Klammerzusatz streichen.

3. DSGVO bleibt als Abkürzung stehen; einmalig in privacy_subtitle mit erklärendem Klammerzusatz ("Opća/Opšta uredba EU o zaštiti podataka", "Splošna uredba EU o varstvu podatkov"). Artikel-/Absatz-Zitate wurden formal an die Zielsprache angepasst (čl./st./tač. bzw. čl./odst./tč.), Nummern unverändert.

4. "Anlage 5 FeV" → "Prilog 5 FeV" mit Erklärung "(njemački/nemački Pravilnik o vozačkim dozvolama)" bzw. "(nemški pravilnik o vozniških dovoljenjih)". MPU, ESS, CPAP, ICD, AHI, NYHA, TIA, Long-QT unübersetzt wie im Master; ICD/MPU-Erklärungen wurden dort mitgeführt, wo der deutsche Text eine hat.

5. COPD wurde lokalisiert: hr "KOPB", sr "HOBP/COPD", bs "HOPB/COPD", sl "KOPB". Bitte prüfen, ob die Doppelform in sr/bs gewünscht ist oder nur das lokale Kürzel stehen soll.

6. Laienbegriffe analog zum Master ergänzt, nichts inhaltlich hinzugefügt: Unterzuckerung → "hipoglikemija (nizak šećer u krvi)" / "hipoglikemija (nizek krvni sladkor)"; Fachärzte mit Laienerklärung ("oftalmolog (očni ljekar)", "otorinolaringolog (ljekar za uho, grlo i nos)", "okulist (očesni zdravnik)").

7. Alle Zeitfenster wörtlich erhalten (24 Monate, 12 Monate, 6 Monate, 3 Monate, "weniger als 3 Monate", "3 bis 6 Monate" usw.), ebenso die ESS-Bänder 0–9 / 10–15 / ≥16 und die NYHA-Selbsteinschätzung (4 Stufen: keine Beschwerden – stärkere Belastung – leichte Belastung – in Ruhe).

8. Geschlechtsformen: Partizipien in Ich-Aussagen doppelt geführt (hr/sr/bs "Pročitao/pročitala sam", sl "Prebral/-a sem", "zadremao/zadremala", "zadremal/-a"). Falls im UI zu lang, kann auf die maskuline Kurzform gekürzt werden.

9. Zwei Stellen mit interpretierender Wortwahl, bitte besonders prüfen:
   - "Stoffwechselentgleisung" → hr/sr/bs "metabolički poremećaj (… zbog izmaknutih/izmaklih vrijednosti)", sl "presnovna iztirjenost". Fachlich gemeint ist die Entgleisung (Ketoazidose/hyperosmolar), nicht eine beliebige Stoffwechselstörung.
   - "Neueinstellung der Therapie" → "novo podešavanje terapije" / "ponovna nastavitev zdravljenja" (Sinn: Neu- bzw. Umstellung der Einstellung, nicht Therapieabbruch).

10. "Fahreignung" wurde durchgängig als "sposobnost za vožnju" / "zmožnost za vožnjo" wiedergegeben (nicht als "Fahrtauglichkeit"), passend zum Leitlinien-Kontext in seizure_free.hint, head_injury_recent.hint und multiple_conditions.hint.

## Batch 5: no, fi, lt, lv

TECHNISCHE PRÜFUNG (alle vier Dateien bestanden)
json.load erfolgreich; 447 Schlüssel je Datei gegenüber 446 im Master — die einzige Abweichung ist das laut Vorgabe geforderte _meta.machine_translated. Keine fehlenden, keine unerwarteten Schlüssel; alle Options-Schlüssel (yes, type1, lkw, <1, >4, 2x, AM…T usw.) unverändert. {current}/{total} in ui.question_of in allen Dateien intakt. UTF-8 ohne BOM, Einrückung 1, keine leeren Werte. Konvention aus is.json/el.json übernommen. Hinweis zur Selbstkontrolle: das Prüfskript im Scratchpad wurde während des Laufs von außen verändert und meldete zuletzt fremde Sprachcodes (mk, tr, da, sv) statt der übergebenen — ich habe die Verifikation deshalb unabhängig direkt gegen de.json neu ausgeführt; das oben genannte Ergebnis stammt aus diesem unabhängigen Lauf.

ANREDE
- fi/lt/lv: durchgängig höfliche Form (fi Teitittely „Onko teillä…/Vastatkaa", lt/lv „Jūs" groß).
- no: Norwegisch (bokmål) kennt keine lebende Sie-Form; die höfliche Registerwirkung wird über „du" plus „vennligst" erzeugt. Das ist die korrekte Lokalisierung, kein Registerverlust — sollte aber bekannt sein, falls der Ton mit den anderen Sprachen verglichen wird.

BEWUSSTE ÜBERSETZUNGSENTSCHEIDUNGEN
- Fachbegriff + Laienbegriff wie im Deutschen beibehalten, z.B. Hypoglykämie: lt „hipoglikemija (per mažas cukraus kiekis kraujyje)", lv „hipoglikēmija (pazemināts cukura līmenis asinīs)"; no/fi bewusst rein laiensprachlich („føling / lavt blodsukker", „liian matala verensokeri"), weil der Fachterminus dort im Patientengespräch unüblich ist.
- MPU: überall Abkürzung erhalten + Kurzerklärung in der Zielsprache mit dem Zusatz „deutsch/Vokietijos/Vācijas", da es sich um ein deutsches Verfahren ohne Entsprechung in den Zielländern handelt.
- FeV Anlage 5: Abkürzung erhalten, Klammerzusatz „die deutsche Fahrerlaubnis-Verordnung" in der Zielsprache ergänzt (durch Regel 5 gedeckt).
- DSGVO: Abkürzung unverändert; die Artikelverweise wurden in die landesübliche Zitierweise gesetzt (no „Art. 6 nr. 1 bokstav a", fi „6 artiklan 1 kohdan a alakohta", lt „6 str. 1 d. a punktas", lv „6. panta 1. punkta a) apakšpunkts"). Inhalt unverändert, nur Zitierform. Zusätzlich „EU-Datenschutz-Grundverordnung" einmal ausgeschrieben in ui.privacy_subtitle, da „DSGVO" außerhalb Deutschlands nicht bekannt ist.
- ESS, CPAP, ICD, AHI, NYHA, TIA, Führerscheinklassen-Codes unverändert; „Epworth Sleepiness Scale (ESS)" als Eigenname englisch belassen (deshalb ist sections.schlaf.subtitle in no.json identisch mit dem Deutschen — beabsichtigt, ebenso „Ja", „Normal (0–9)", „Insulin").
- Name und Adresse unverändert. Die Fachgebietsbezeichnung „Betriebsmedizin · Notfallmedizin" wurde übersetzt (no „bedriftsmedisin · akuttmedisin", fi „työterveyslääketiede · ensihoitolääketiede", lt „darbo medicina · skubioji medicina", lv „arodmedicīna · neatliekamā medicīna"). Falls die Verantwortlichen-Zeile rechtlich unverändert erscheinen soll, bitte hier zurückändern — das ist die einzige Stelle mit übersetztem Kanzleikopf.

ZEITFENSTER / MEDIZINISCHE PRÄZISION
Alle Zeitangaben wurden 1:1 gespiegelt und einzeln geprüft: „letzte 12/24 Monate", „weniger als 3/6 Monate", „vor mehr/weniger als 3 Monaten beendet", die Anfallsfreiheits-Staffel (unter3m … ueber5j) und die Schwindel-Staffel (unter3m … ueber2j). Die Unterscheidung „Ersterteilung/Verlängerung" und die NYHA-Abstufung („keine Beschwerden bei alltäglicher Belastung" / „stärkere" / „leichte" / „in Ruhe") sind semantisch exakt erhalten.

PUNKTE FÜR DIE ÄRZTLICHE DURCHSICHT (Formulierungen, bei denen die Zielsprache keine 1:1-Entsprechung hat)
1. „Herzstolpern": no „uregelmessige hjerteslag/ekstraslag", fi „lisälyönnit", lt „širdies suklupimai/ekstrasistolės", lv „sirds paklupšana/ekstrasistoles" — jeweils Laienausdruck + Fachbegriff, da der reine Laienausdruck in lt/lv unscharf ist.
2. „Stoffwechselentgleisung": keine idiomatische Entsprechung. Umschrieben als no „alvorlig ubalanse i stoffskiftet", fi „aineenvaihdunnan vakava häiriintyminen", lt „medžiagų apykaitos sutrikimas", lv „vielmaiņas izsviešana no līdzsvara" — jeweils mit dem deutschen Klammerbeispiel (Krankenhausbehandlung wegen entgleister Werte), das die Bedeutung trägt. Bitte prüfen, ob die Schärfe ausreicht.
3. „Entgiftung / Entwöhnungsbehandlung": als zwei getrennte Behandlungsarten übersetzt (fi „katkaisuhoito / vieroitushoito", lt „detoksikacija / atpratinimo gydymas", lv „detoksikācija / atradināšanas ārstēšana", no „avrusning / avvenningsbehandling"). In allen vier Ländern ist die Trennung weniger etabliert als im deutschen Suchtsystem.
4. „Lagerungsschwindel": bewusst als „gutartiger Lagerungsschwindel" wiedergegeben (no „godartet stillingssvimmelhet/krystallsyke", fi „hyvänlaatuinen asentohuimaus", lt „gerybinis padėties galvos svaigimas", lv „labdabīgs pozicionālais reibonis"), weil das Adjektiv im Zielsprachgebrauch fester Bestandteil des Terminus ist. Minimale Zufügung gegenüber dem Deutschen.
5. „Fahreignung": no „kjøreegnethet", fi „ajokelpoisuus", lt „tinkamumas vairuoti", lv „piemērotība vadīt transportlīdzekli" — im Deutschen ein Rechtsbegriff, in den Zielsprachen beschreibend. Inhaltlich korrekt, juristisch aber nicht deckungsgleich.
6. „Lenkhilfe" (vehicle_modified) wurde als Servolenkung/Lenkkraftunterstützung übersetzt (no „styrehjelp", fi „ohjaustehostin", lt „vairo stiprintuvas", lv „stūres pastiprinātājs"). Falls im Deutschen ein orthopädischer Lenkknauf gemeint ist, sollte hier präzisiert werden — das ist die einzige inhaltlich mehrdeutige Stelle im Master.
7. „Fahrgastbeförderung": in fi als „Henkilöiden kuljetus", in lt/lv als „Keleivių vežimas"/„Pasažieru pārvadāšana" — die deutsche Beförderungserlaubnis (Taxi/Mietwagen/Krankentransport) hat in den Zielländern kein identisches Pendant; die drei Klammerbeispiele tragen daher die Bedeutung.
8. Alle vier Dateien sind maschinell erzeugt und als machine_translated:true markiert; eine muttersprachliche Durchsicht insbesondere der Datenschutz- und Einwilligungstexte (ui.privacy_*, questions.consent_*) wird vor dem Produktiveinsatz empfohlen, da diese rechtsverbindlich sind.

## Batch 6: et, uk, be, ru

SELBSTKONTROLLE (System-python, Skript unter …\scratchpad\check_et_uk_be_ru.py): alle 4 Dateien json.load OK, Schlüsselmenge rekursiv identisch mit de.json (446 Pfade + erlaubter Zusatz /_meta/machine_translated = 447), kein fehlender/überzähliger Schlüssel, kein Wert 1:1 aus dem Deutschen übernommen (außer license_classes-Codes), {current}/{total} in ui.question_of unverändert, UTF-8 ohne BOM, durchgehend Zielschrift (et Latein, uk/be/ru Kyrillisch; die verbleibenden 193 lateinischen Zeichen pro kyrillischer Datei sind ausschließlich Name/Adresse, Führerscheincodes und die geschützten Abkürzungen).

ÜBERSETZUNGSENTSCHEIDUNGEN, die ärztlich geprüft werden sollten:

1. ui.header_title: „Verkehrsmedizinischer Fragebogen“ – et wörtlich „Liiklusmeditsiiniline küsimustik“. Im uk/be/ru ist die wörtliche Bildung („транспортно-медицинская анкета“) unüblich, daher patientennah „Medizinischer Fragebogen für Fahrer“ (uk „Медичний опитувальник для водіїв“, be „Медыцынскі апытальнік для кіроўцаў“, ru „Медицинская анкета для водителей“). In consent_privacy wurde dagegen die Fachformulierung „transportmedizinische Zwecke“ beibehalten. Falls einheitlich gewünscht, bitte melden.

2. privacy_controller: „Dr. med. Björn Micka, Betriebsmedizin · Notfallmedizin, Christoph-Dassler-Str. 22, 91074 Herzogenaurach“ ist in allen 4 Dateien vollständig unverändert – auch die Fachgebietsbezeichnung „Betriebsmedizin · Notfallmedizin“, da sie zum Praxis-/Namenszusatz gehört. Falls diese übersetzt werden soll, ist das eine bewusste Nachbesserung.

3. Gesetzesverweise: „DSGVO“ als Kürzel überall erhalten; in privacy_subtitle wurde einmalig ein Klammerzusatz in der Zielsprache ergänzt (uk/be/ru „Загальний регламент ЄС про захист даних“ bzw. Entsprechung, et „isikuandmete kaitse üldmäärus“) – laut Regel 5 zulässig. „Art. 6 Abs. 1 lit. a / Art. 9 Abs. 2 lit. a“ wurde in zielsprachlicher Zitierweise wiedergegeben, die Buchstaben-Kennung „a“ blieb lateinisch. Bei „Anlage 5 FeV“ wurde das Kürzel FeV belassen und ein erklärender Klammerzusatz („deutsche Fahrerlaubnis-Verordnung / Bestimmung über die Zulassung zum Führen von Kfz“) ergänzt, weil das Kürzel außerhalb Deutschlands unbekannt ist.

4. MPU: Kürzel überall erhalten. In questions.license_withdrawn steht – wie im Deutschen – die ausgeschriebene Erklärung („medizinisch-psychologische Untersuchung (MPU)“). In questions.alcohol_traffic hat der deutsche Text keine Erklärung; ein zunächst ergänzter Zusatz wurde bewusst wieder entfernt, damit nichts hinzugefügt wird. Patienten sehen die Erklärung damit nur bei der früheren Frage (Abschnitt „Anlass“). Falls die Erklärung an beiden Stellen erwünscht ist, bitte freigeben.

5. ESS, CPAP, ICD, AHI, NYHA, QT, AV-Block, ICD-Schock: Kürzel unverändert lateinisch. „COPD“ wurde als „Landeskürzel/COPD“ geschrieben (uk „ХОЗЛ/COPD“, be „ХАЗЛ/COPD“, ru „ХОБЛ/COPD“, et „KOK/COPD“), damit Patienten das im Heimatland gebräuchliche Kürzel wiedererkennen und der deutsche Befundtext trotzdem zuordenbar bleibt. COPD war in Regel 5 nicht gelistet – bitte prüfen, ob das so gewünscht ist.

6. Laienbegriff + Fachbegriff wie im Deutschen: „Grauer Star“ → „Katarakt/Linsentrübung“, „Grüner Star/Glaukom“ → „Glaukom“ (im Slawischen ist „глаукома“ der übliche Laienausdruck, ein zweiter Ausdruck existiert nicht); „Unterzuckerung“ → „Absenkung des Blutzuckers“ (keine Fachbezeichnung „Hypoglykämie“ verwendet, um B1-Niveau zu halten); „Schlafapnoe“, „Tinnitus“, „Kardiomyopathie“, „Polyneuropathie“, „Myasthenie“ als international übliche Termini belassen.

7. Zeitfenster wurden wörtlich und vollständig erhalten (u.a. „weniger als 3 Monate“, „3 bis 6 Monate“, „letzte 12 Monate“, „letzte 24 Monate“, „letzte 3 Monate“, „mehr als 5 Jahre“). Im Russischen wurde „1 bis 2 Jahre“ grammatisch korrekt als „От 1 года до 2 лет“ ausgeschrieben – inhaltlich identisch.

8. ESS-Items 5 und 7: Der deutsche Text unterscheidet „am Nachmittag hingelegt“ (ess_5) und „nach dem Mittagessen“ (ess_7). Diese Unterscheidung wurde in allen Sprachen bewusst erhalten (z.B. ru „во второй половине дня прилегли“ vs. „после обеда“), da „после обеда“ sonst beide Items gleich klingen ließe.

9. Geschlechtsneutralität: Bei Verbformen der Vergangenheit im Slawischen wurde die Doppelform in Klammern gesetzt (z.B. ru „никогда бы не задремал(-а)“, „Я прочитал(-а)“). Das ist in Formularen üblich, wirkt aber etwas technisch – alternativ wäre eine rein maskuline oder eine unpersönliche Formulierung möglich.

10. Höflichkeitsform: durchgehend Sie-Äquivalent, im Slawischen mit großgeschriebenem „Вы/Ваш“; im Estnischen „te/teie“ (Kleinschreibung ist dort die Norm).

11. Alle Options-Schlüssel (yes, no, type1, lkw, unter3m, 2x, „&lt;1“, „&gt;4“ usw.) sowie sämtliche Führerscheinklassen-Codes (AM … T) sind bitidentisch zum Master – automatisiert geprüft.

12. Kennzeichnung: In jeder Datei ist "_meta": {"language": …, "name": …, "machine_translated": true} gesetzt. Die Texte sind maschinell erzeugt und vor dem Patienteneinsatz durch eine muttersprachliche bzw. ärztliche Durchsicht zu bestätigen – besonders die Abschnitte Diabetes (Unterzuckerungsrisiko der Tablettengruppen), Herz (NYHA-Selbsteinschätzung) und Substanzen (Abhängigkeits-/MPU-Fragen), weil dort Fehldeutungen unmittelbar eignungsrelevant wären.

## Batch 7: ar, hi, ur

PRÜFUNG (System-python, Skript im Scratchpad): alle drei Dateien json.load-fähig, rekursive Schlüsselmenge exakt identisch zu de.json (missing=0, extra=0 außer dem erlaubten _meta/machine_translated), keine leeren Werte, {current}/{total} in ui.question_of unverändert, Options-Schlüssel unverändert. Einrückung 1, UTF-8 ohne BOM. Zusatzprüfung: kein Wert außer den Führerscheinklassen-Codes und privacy_controller ist mit dem deutschen Original identisch geblieben.

ÜBERSETZUNGSENTSCHEIDUNGEN / ZU PRÜFEN:

1. Titel/Fachbegriff "verkehrsmedizinisch": ar "الطب المروري", hi "यातायात-चिकित्सा", ur "ٹریفک میڈیسن". In allen drei Sprachen kein etablierter Standardterminus – gegebenenfalls durch die in der Praxis übliche Formulierung ersetzen.

2. Abkürzungen wie im Master beibehalten, mit kurzer zielsprachiger Erläuterung nur dort, wo der deutsche Text sie hat: ESS, CPAP, ICD, AHI, NYHA, COPD, MPU. MPU wurde an beiden Stellen (license_withdrawn, alcohol_traffic) mit "medizinisch-psychologische Untersuchung der Fahreignung" erläutert, weil der deutsche Text die Erklärung im Fließtext trägt.

3. Rechtsverweise unübersetzt gelassen und in Klammern erläutert: "DSGVO Art. 13", "DSGVO Art. 6 Abs. 1 lit. a, Art. 9 Abs. 2 lit. a" (Zusatz: europäische Datenschutz-Grundverordnung), "Anlage 5 FeV" (Zusatz: Anhang 5 der Fahrerlaubnis-Verordnung). Achtung: In der arabischen und urdu Datei stehen die lateinschriftlichen Verweise innerhalb von RTL-Text – im Frontend bitte optisch prüfen (mögliche Bidi-Umbrüche); ggf. Unicode-Isolate (U+2068/U+2069) ergänzen.

4. Namen/Adresse in privacy_controller vollständig unverändert lateinisch belassen (Dr. med. Björn Micka, Betriebsmedizin · Notfallmedizin, Christoph-Dassler-Str. 22, 91074 Herzogenaurach). Gleiches gilt für die Führerscheinklassen-Codes und die Klassenlisten in exam_occasion (C, C1, CE, C1E / D, D1, DE, D1E).

5. Zahlen: durchgehend westarabische Ziffern (0–9) wie im Master, auch in ar/ur – falls die Praxis östliche arabisch-indische Ziffern (٠-٩) bevorzugt, müsste das global geändert werden. Zeitfenster wurden wörtlich übernommen ("weniger als 3 Monate", "in den letzten 12/24 Monaten", "6 bis 12 Monate" usw.).

6. Laienbegriffe ergänzt, wo der deutsche Text es vormacht bzw. der Fachbegriff in der Zielsprache unbekannt wäre: Diabetes = "شوگر کی بیماری"/"शुगर की बीमारी", Parkinson = "الشلل الرعاش"/"कंपवात"/"رعشہ", Glaukom = "الماء الأزرق"/"काला मोतिया"/"کالا موتیا", Herzinfarkt = "الجلطة القلبية". Bei "Bewegungsapparat" wurde in hi/ur/ar erklärend "(Knochen, Gelenke, Muskeln)" ergänzt, da es keinen gängigen Einwortbegriff gibt – bitte freigeben oder streichen.

7. Geschlechtsneutralität: Hindi und Urdu markieren Verben am Sprecher. In Ich-Aussagen (consent_truth, consent_privacy, antiepileptics "aktuell", glucose_monitoring "keine_med") wurde die Doppelform "करता/करती", "لیتا/لیتی" verwendet. Arabisch ist an diesen Stellen neutral formuliert.

8. Anrede: durchgehend höflich – ar "يرجى …" + 2. Person Singular (Standardform in Formularen), hi "आप" mit -एँ/-ें-Imperativ, ur "آپ" mit "براہِ کرم". 

9. Fachlich heikle Stellen, die eine ärztliche Gegenlesung verdienen:
   - exertion_symptoms (NYHA-Selbsteinschätzung): Abstufungen "stärkere Belastung / leichte Belastung / in Ruhe" wurden wörtlich abgebildet.
   - diabetes_therapy tabl_low/tabl_high: Wirkstoffgruppen als Transkription (Metformin, Sulfonylharnstoffe/Glinide) – Terminologie in hi/ur ist nicht standardisiert.
   - heart_other: "Long-QT" als Code belassen (ar: متلازمة QT الطويل), "Aortenaneurysma" als "Aussackung der Hauptschlagader" umschrieben.
   - stroke: "TIA" belassen, Klammererklärung wörtlich übernommen.
   - alcohol_traffic "Promillewert": ar "نسبة الكحول", hi/ur mit Zusatz "प्रोमिल मान"/"پرومِل ویلیو" – falls unverständlich, ggf. auf "Blutalkoholwert" umstellen.
   - psychosis: "Wahnvorstellungen/Halluzinationen" in ur umschreibend als "وہم یا سنائی/دکھائی دینے والے خیالی مناظر" (Laienformulierung).
   - memory_problems "Orientierungsprobleme": ur als "راستہ/وقت پہچاننے کے مسائل" umschrieben, hi "दिशा-बोध", ar "التوجّه".

10. Alle Dateien sind maschinell übersetzt (machine_translated: true) und wurden nicht von einem muttersprachlichen Medizin-Fachübersetzer geprüft – vor dem Produktiveinsatz insbesondere die Einwilligungs- und Datenschutztexte (rechtsverbindlich) sowie die Zeitangaben in seizure_free, vertigo_last, hypoglycemia und head_injury_recent gegenlesen lassen.

## Batch 8: ka, hy, az, kk

ZUSTAND DER DATEIEN
- az.json und kk.json wurden komplett neu erstellt.
- ka.json und hy.json existierten bereits aus einem früheren Lauf und waren inhaltlich vollständig und sauber. Waehrend dieser Aufgabe wurde de.json vom Orchestrator erweitert (neu: sections.gesundheit sowie questions.has_conditions mit label+hint). Diese beiden Bloecke wurden in ka.json/hy.json ergaenzt; der uebrige Bestand blieb unveraendert, damit die dort bereits etablierte Terminologie stabil bleibt.

SELBSTKONTROLLE (alle vier Dateien bestanden)
- json.load erfolgreich; rekursive Schluesselmenge exakt identisch mit de.json (452 Master-Schluessel + _meta.machine_translated).
- {current}/{total} in ui.question_of unveraendert.
- Zeichensatzpruefung Zeichen fuer Zeichen: keine Schriftvermischung. Die einzigen lateinischen Zeichenfolgen in ka/hy/kk sind Fuehrerscheinklassen-Codes, "Björn" und die Platzhalter.
- Erhaltene Tokens in allen Dateien geprueft: DSGVO Art. 6/9/13, FeV, MPU, ESS, CPAP, ICD, AHI, NYHA, TIA, COPD, Long-QT, Kap. 2.7, vollstaendige Adresse.
- UTF-8 ohne BOM, exakt indent=1 / ensure_ascii=false.

UEBERSETZUNGSENTSCHEIDUNGEN
1. "Verkehrsmedizin" hat in keiner der vier Sprachen einen etablierten Fachbegriff. Gewaehlt: ka "სატრანსპორტო მედიცინა" (Bestand), hy "տրանսպորտային բժշկություն" (Bestand), az "yol-nəqliyyat təbabəti", kk "жол-көлік медицинасы". Bitte auf Akzeptanz pruefen.
2. Gesetzesverweise bleiben deutsch (DSGVO Art. 6 Abs. 1 lit. a, Art. 9 Abs. 2 lit. a, Art. 13; FeV Anlage 5) mit kurzem erklaerendem Klammerzusatz in der Zielsprache. § 11 FeV kommt im Master nicht vor.
3. MPU bleibt als Abkuerzung mit Erklaerung, wie im deutschen Text. Ebenso ESS, CPAP, ICD, AHI, NYHA, TIA, COPD, Long-QT in lateinischer Schrift belassen — der Master erklaert diese teils selbst.
4. ui.question_of: "Frage {current} von {total}" wurde in allen vier Sprachen als "… {current} / {total}" wiedergegeben. Grund: die woertliche Genitiv-/Ablativkonstruktion erzeugt bei variabler Zahl unsaubere Kasusendungen (v.a. ka/kk). Platzhalter sind unveraendert.
5. Fragezeichen: hy.json verwendet durchgehend das lateinische "?" statt des armenischen "՞" (Bestand aus dem frueheren Lauf, konsistent beibehalten). Das ist im digitalen Alltagsgebrauch verbreitet, aber typografisch nicht normgerecht — falls gewuenscht, ist das ein separater, mechanischer Fix.

FACHLICH ZU PRUEFENDE STELLEN (maschinell uebersetzt, muttersprachliche/aerztliche Durchsicht noetig)
- "Sulfonylharnstoffe": az "sulfonilsidik cövhəri preparatları", kk "сульфонилмочевина препараттары" (russisches Lehnwort, in KZ-Fachsprache ueblich), ka "სულფონილშარდოვანები", hy "սուլֆոնիլմիզանյութեր". Uneinheitlicher Lehnwortgrad — bitte gegenpruefen.
- "Lagerungsschwindel" (BPPV): kk "қалыптық бас айналу", az "mövqe başgicəllənməsi". Kein fest etablierter Laienbegriff; ggf. Klammerzusatz gewuenscht.
- "Vorhofflimmern": kk "жүрекше фибрилляциясы", az "qulaqcıqların fibrilyasiyası". Fachlich korrekt, fuer Laien evtl. schwer.
- "Herzstolpern": in allen vier Sprachen umschrieben ("Gefuehl des Stolperns/Aussetzens"), da kein exaktes Aequivalent existiert.
- "Mietwagen" (Fahrgastbefoerderung): in az/kk als "Mietwagen mit Fahrer" praezisiert (az "sürücülü icarə avtomobili", kk "жүргізушісі бар жалдамалы автокөлік), passend zum PBefG-Sinn. Im Bestand ka/hy steht nur "Mietwagen" ohne diesen Zusatz — kleine Inkonsistenz zwischen den Dateien, inhaltlich unkritisch.
- kk "COPD" wurde wie im Master als lateinische Abkuerzung belassen; in Kasachstan ist eher "ХОБЛ" gelaeufig. Falls gewuenscht, kann "COPD (ХОБЛ)" ergaenzt werden.
- az ui.band_normal lautet "Normal (0–9)" und ist damit zeichengleich mit dem deutschen Wert — das ist korrektes Aserbaidschanisch, kein vergessener String.

ZEITFENSTER UND MENGENANGABEN
Alle Zeitangaben wurden woertlich uebertragen und stichprobenartig geprueft: "letzte 24 Monate", "letzte 12 Monate", "letzte 3 Monate", "weniger als 3 Monate", "weniger als 6 Monate", die Staffelungen bei seizure_free (3/6/12 Monate, 1-2/2-5/ueber 5 Jahre), vertigo_last (bis ueber 2 Jahre), license_years und driving_hours. Keine Auslassungen, keine Zusaetze gegenueber dem deutschen Master.
