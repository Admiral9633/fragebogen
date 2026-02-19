from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import QuestionnaireSession, AnswerSet, QuestionnaireTemplate
from .serializers import (
    SubmitSerializer, 
    QuestionnaireSessionSerializer,
    AnswerSetSerializer
)


class QuestionnaireSessionView(APIView):
    """
    GET: Hole Fragebogen-Session Details anhand des Tokens
    """
    def get(self, request, token):
        session = get_object_or_404(QuestionnaireSession, token=token)
        
        # Prüfe ob Session abgelaufen
        if session.is_expired():
            return Response(
                {'error': 'Dieser Link ist abgelaufen.'},
                status=status.HTTP_410_GONE
            )
        
        # Prüfe ob bereits ausgefüllt
        if session.completed:
            return Response(
                {'error': 'Dieser Fragebogen wurde bereits ausgefüllt.'},
                status=status.HTTP_410_GONE
            )
        
        serializer = QuestionnaireSessionSerializer(session)
        return Response({
            'session': serializer.data,
            'template': session.template.schema_json
        })


class SubmitQuestionnaireView(APIView):
    """
    POST: Fragebogen einreichen
    """
    def post(self, request, token):
        # Hole Session
        session = get_object_or_404(QuestionnaireSession, token=token)
        
        # Validiere Session
        if session.is_expired():
            return Response(
                {'error': 'Dieser Link ist abgelaufen.'},
                status=status.HTTP_410_GONE
            )
        
        if session.completed:
            return Response(
                {'error': 'Dieser Fragebogen wurde bereits ausgefüllt.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validiere Eingabedaten
        serializer = SubmitSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Speichere Antworten
        validated_data = serializer.validated_data
        
        AnswerSet.objects.create(
            session=session,
            answers_json=validated_data,
            ess_total=validated_data['ess_total'],
            ess_band=validated_data['ess_band']
        )
        
        # Markiere Session als abgeschlossen
        session.completed = True
        session.completed_at = timezone.now()
        session.save()
        
        return Response({
            'success': True,
            'ess_total': validated_data['ess_total'],
            'ess_band': validated_data['ess_band'],
            'message': 'Fragebogen erfolgreich eingereicht.'
        }, status=status.HTTP_201_CREATED)


class GeneratePDFView(APIView):
    """
    GET: Generiere PDF für eine abgeschlossene Session
    """
    def get(self, request, token):
        session = get_object_or_404(QuestionnaireSession, token=token)
        
        # Prüfe ob Session abgeschlossen
        if not session.completed:
            return Response(
                {'error': 'Dieser Fragebogen ist noch nicht abgeschlossen.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            answer_set = session.answers
        except AnswerSet.DoesNotExist:
            return Response(
                {'error': 'Keine Antworten gefunden.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Generiere HTML für PDF
        html_content = self._generate_html(session, answer_set)
        
        # Verwende xhtml2pdf für PDF-Generierung
        try:
            from io import BytesIO
            from xhtml2pdf import pisa
            
            pdf_buffer = BytesIO()
            pisa_status = pisa.CreatePDF(html_content, dest=pdf_buffer)
            
            if pisa_status.err:
                raise Exception(f'PDF-Generierung fehlgeschlagen: {pisa_status.err}')
            
            pdf_bytes = pdf_buffer.getvalue()
            response = HttpResponse(pdf_bytes, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="fragebogen_{token}.pdf"'
            return response
        except Exception as pdf_error:
            import logging
            logging.getLogger(__name__).error(f'PDF generation failed: {pdf_error}')
            # Fallback: druckbares HTML
            return HttpResponse(html_content, content_type='text/html')
    
    def _generate_html(self, session, answer_set):
        """Generiere HTML für PDF Export – Patientenfragebogen zweiseitig"""
        a = answer_set.answers_json

        def box(val, target="yes"):
            """CSS-Checkbox: gefüllt oder leer"""
            if str(val) == str(target):
                return '<span class="cb-checked">X</span>'
            return '<span class="cb-empty">&nbsp;</span>'

        def ess_box(val, n):
            if str(val) == str(n):
                return '<span class="cb-checked">X</span>'
            return '<span class="cb-empty">&nbsp;</span>'

        def yn_label(val):
            if val == "yes": return "Ja"
            if val == "no":  return "Nein"
            return "—"

        def txt(val, fallback="—"):
            v = a.get(val, "")
            return str(v).strip() if str(v).strip() else fallback

        ess_labels = [
            "Wenn Sie sitzen und lesen",
            "Beim Fernsehen",
            "Als Zuhoerer bei einem Vortrag, im Kino oder Theater",
            "Als Beifahrer im Auto (Fahrtzeit eine Stunde, keine Pause)",
            "Beim Hinlegen Nachmittags zum Ausruhen",
            "Wenn Sie sich sitzend mit jemandem unterhalten",
            "Im Sitzen nach dem Mittagessen (kein Alkohol getrunken)",
            "Sie muessen als Autofahrer vor einer roten Ampel halten",
        ]
        ess_keys = [f"ess_{i}" for i in range(1, 9)]
        ess_total = answer_set.ess_total or 0
        if ess_total <= 9:
            ess_band = "Normal (0-9) – keine erhöhte Tagesschläfrigkeit"
        elif ess_total <= 15:
            ess_band = "Erhöht (10-15) – weitere Abklärung empfohlen"
        else:
            ess_band = "Ausgeprägt (≥16) – ärztliche Abklärung erforderlich"

        license_arr = a.get("license_classes_arr", [])
        if isinstance(license_arr, str):
            license_arr = [x.strip() for x in license_arr.split(",") if x.strip()]

        def lic_box(cls):
            return box("yes" if cls in license_arr else "no", "yes")

        completed_str = session.completed_at.strftime('%d.%m.%Y') if session.completed_at else ""

        # ── ESS-Tabellenzeilen ──────────────────────────────────────────────
        ess_rows = ""
        for i, (key, label) in enumerate(zip(ess_keys, ess_labels)):
            val = str(a.get(key, ""))
            bg = "#f2f2f2" if i % 2 == 0 else "#ffffff"
            ess_rows += f"""<tr style="background:{bg}">
                <td class="td-label">{label}</td>
                <td class="td-cb">{ess_box(val,"0")}</td>
                <td class="td-cb">{ess_box(val,"1")}</td>
                <td class="td-cb">{ess_box(val,"2")}</td>
                <td class="td-cb">{ess_box(val,"3")}</td>
            </tr>"""

        # ── Ja/Nein Zeile ───────────────────────────────────────────────────
        def yn_row(label, key, bg):
            val = a.get(key, "")
            return f"""<tr style="background:{bg}">
                <td class="td-label">{label}</td>
                <td class="td-cb">{box(val,"yes")}</td>
                <td class="td-cb">{box(val,"no")}</td>
            </tr>"""

        # ── Seite-1-Tabelle: 6 Pflichtfragen Ausfallrisiko ──────────────────
        ausfallrisiko = [
            ("Bewusstseins- oder Gleichgewichtsstoerungen, Schwindel, Anfallsleiden jeglicher Ursache", "syncope"),
            ("Unbehandelte schlafbezogene Atemstörungen (Schlaf-Apnoe)", "snoring"),
            ("Zuckerkrankheit (Diabetes) mit Neigung zur Hypoglykämie", "hypoglycemia"),
            ("Chronischer Alkoholmissbrauch oder Drogenabhängigkeit", "drugs"),
            ("Dauerbehandlung mit Medikamenten, die die Fahrtüchtigkeit einschränken", "sedating_meds"),
            ("Erkrankungen des Herzens / Kreislaufs mit erheblicher Leistungseinschränkung", "heart_failure"),
        ]
        ausfallrisiko_rows = ""
        for i, (label, key) in enumerate(ausfallrisiko):
            bg = "#f2f2f2" if i % 2 == 0 else "#ffffff"
            ausfallrisiko_rows += yn_row(label, key, bg)

        # ── Seite-2-Tabelle: Eigenanamnese ──────────────────────────────────
        anamnese_items = [
            ("Augenkrankheiten / Sehstörungen",                  "vision_problems"),
            ("Ohrenkrankheiten / Hörstörungen",                  "hearing_aid"),
            ("Herzinfarkt / Koronare Herzerkrankung",             "heart_attack"),
            ("Herzrhythmusstörungen / Schrittmacher / ICD",      "arrhythmia"),
            ("Herzinsuffizienz",                                  "heart_failure"),
            ("Epilepsie / Krampfanfälle",                        "epilepsy"),
            ("Parkinson",                                         "parkinson"),
            ("Multiple Sklerose (MS)",                            "ms"),
            ("Migräne mit Aura",                                  "migraine_aura"),
            ("Gleichgewichtsstörungen / Schwindel",               "dizziness"),
            ("Ohnmacht / Bewusstlosigkeit",                       "syncope"),
            ("Neurologische Ausfälle (Lähmung, Sprachstörung)",  "neuro_deficit"),
            ("Diabetes mellitus",                                  "diabetes_type"),
            ("Unterzuckerung mit Fremdhilfe",                     "hypoglycemia"),
            ("Tagesschläfrigkeit / Sekundenschlaf",               "daytime_sleepiness"),
            ("Schlafapnoe / Schnarchen mit Atemaussetzern",       "snoring"),
            ("Psychiatrische Erkrankung",                         "psychiatric"),
            ("Konzentrations- / Gedächtnisstörungen",             "concentration"),
            ("Alkohol (regelmäßiger Konsum)",                     "alcohol"),
            ("Drogen- / Substanzkonsum",                          "drugs"),
            ("Sedierende Medikamente",                            "sedating_meds"),
        ]
        anamnese_rows = ""
        for i, (label, key) in enumerate(anamnese_items):
            bg = "#f2f2f2" if i % 2 == 0 else "#ffffff"
            if key == "diabetes_type":
                raw = a.get(key, "")
                effective = "no" if raw in ("none", "", None) else "yes"
                anamnese_rows += f"""<tr style="background:{bg}">
                    <td class="td-label">{label}</td>
                    <td class="td-cb">{box(effective,"yes")}</td>
                    <td class="td-cb">{box(effective,"no")}</td>
                </tr>"""
            else:
                anamnese_rows += yn_row(label, key, bg)

        # ── Freitexte ──────────────────────────────────────────────────────
        def freitext_row(label, val, bg):
            v = str(val).strip() if str(val).strip() else "—"
            return f"""<tr style="background:{bg}">
                <td class="td-label" style="width:180px;font-weight:bold">{label}</td>
                <td class="td-label" style="border-bottom:1px solid #ccc">{v}</td>
            </tr>"""

        freitexte = [
            ("Unfälle / Beinahe-Unfälle",   a.get("accidents_desc","")),
            ("Sehprobleme (Beschreibung)",   a.get("vision_desc","")),
            ("Diabetes-Typ",                 a.get("diabetes_type","")),
            ("Letzte Hypoglykämie",          a.get("last_hypo","")),
            ("Atemtherapie (CPAP etc.)",     a.get("cpap_therapy","")),
            ("Psychiatrisches Leiden",       a.get("psychiatric_desc","")),
            ("Medikamente mit Beschreibung", a.get("meds_desc","")),
            ("Schlafmittel / Sedativa",      a.get("sleeping_pills_desc","")),
            ("Anmerkungen / Sonstiges",      a.get("remarks","")),
        ]
        freitext_rows = ""
        for i, (label, val) in enumerate(freitexte):
            v = str(val).strip()
            if v and v not in ("none", "no", "yes"):
                bg = "#f2f2f2" if i % 2 == 0 else "#ffffff"
                freitext_rows += freitext_row(label, v, bg)

        if not freitext_rows:
            freitext_rows = '<tr><td colspan="2" class="td-label">Keine Freitext-Angaben</td></tr>'

        html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8"/>
<title>Patientenfragebogen</title>
<style>
  @page {{ size: A4; margin: 18mm 15mm 15mm 15mm; }}
  body {{ font-family: Arial, Helvetica, sans-serif; font-size: 9pt; color: #111; margin: 0; }}
  h1 {{ font-size: 17pt; font-weight: bold; margin: 0 0 10px 0; }}
  h2 {{ font-size: 10pt; font-weight: bold; margin: 10px 0 3px 0; border-bottom: 1px solid #999; padding-bottom: 2px; }}
  table {{ width: 100%; border-collapse: collapse; margin-bottom: 4px; }}
  .td-label {{ border: 1px solid #bbb; padding: 3px 6px; font-size: 8.5pt; }}
  .td-cb {{ border: 1px solid #bbb; padding: 3px; text-align: center; width: 34px; }}
  .cb-checked {{
    display: inline-block; width: 12px; height: 12px;
    border: 1.5px solid #000; text-align: center;
    font-size: 8pt; font-weight: bold; line-height: 12px;
    background: #ffffff;
  }}
  .cb-empty {{
    display: inline-block; width: 12px; height: 12px;
    border: 1.5px solid #000; background: #ffffff;
  }}
  .header-box {{ background: #e5e5e5; padding: 7px 10px; margin-bottom: 8px; }}
  .italic-box {{ background: #e5e5e5; padding: 7px 10px; font-style: italic; font-size: 8.5pt; margin-bottom: 5px; }}
  .warning-box {{ border: 2px solid #333; padding: 7px 10px; font-style: italic; font-size: 9pt; font-weight: bold; margin-top: 8px; margin-bottom:8px; }}
  .sig-line {{ border-bottom: 1px solid #555; height: 28px; }}
  .label-xs {{ font-size: 7.5pt; color: #444; margin-top: 2px; }}
  .page-break {{ page-break-before: always; }}
  .th-gray {{ background: #d0d0d0; border: 1px solid #bbb; padding: 3px 6px; font-size: 8.5pt; text-align: center; }}
  .info-right {{ font-size: 8.5pt; line-height: 1.6; }}
</style>
</head>
<body>

<!-- ══════════════════ SEITE 1 ══════════════════ -->
<h1>Patientenfragebogen</h1>

<div class="header-box">
<table>
  <tr>
    <td style="width:52%;vertical-align:top">
      <table style="width:100%">
        <tr><td style="padding:2px 4px;font-size:9pt;width:100px">Name:</td>
            <td style="border-bottom:1px solid #888;padding:1px 4px">&nbsp;</td></tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Vorname:</td>
            <td style="border-bottom:1px solid #888;padding:1px 4px">&nbsp;</td></tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Geburtsdatum:</td>
            <td style="border-bottom:1px solid #888;padding:1px 4px">&nbsp;</td></tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Führerschein:</td>
            <td style="padding:2px 4px;font-size:9pt">
              {lic_box('B')} PKW &nbsp;&nbsp;
              {lic_box('C')} LKW &nbsp;&nbsp;
              {lic_box('D')} Bus
            </td></tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Ausgefüllt am:</td>
            <td style="padding:2px 4px;font-size:9pt">{completed_str}</td></tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Fahrzeit/Tag:</td>
            <td style="padding:2px 4px;font-size:9pt">{txt('driving_hours')} h
              &nbsp;|&nbsp; Nachtfahrten: {yn_label(a.get('night_driving'))}</td></tr>
      </table>
    </td>
    <td style="width:48%;vertical-align:top;padding-left:14px" class="info-right">
      <strong>Dr. med. Björn Micka</strong><br/>
      Betriebsmedizin, Notfallmedizin<br/>
      Christoph-Dassler-Str. 22<br/>
      91074 Herzogenaurach
    </td>
  </tr>
</table>
</div>

<!-- Ausfallrisiko-Tabelle -->
<h2>Bestehen bei Ihnen folgende Erkrankungen? (bitte ankreuzen)</h2>
<table>
  <tr>
    <th class="th-gray" style="text-align:left">Beschwerde / Erkrankung</th>
    <th class="th-gray" style="width:34px">ja</th>
    <th class="th-gray" style="width:34px">nein</th>
  </tr>
  {ausfallrisiko_rows}
</table>

<!-- ESS -->
<h2>Fragebogen zur Tagesschläfrigkeit (Epworth Sleepiness Scale)</h2>
<div class="italic-box">
Wie leicht fällt es Ihnen, in folgenden Situationen einzuschlafen?
Kreuzen Sie die am besten zutreffende Zahl an:
0 = würde nie einschlafen &nbsp;|&nbsp; 1 = geringe &nbsp;|&nbsp; 2 = mittlere &nbsp;|&nbsp; 3 = hohe Wahrscheinlichkeit
</div>
<table>
  <tr>
    <th class="th-gray" style="text-align:left">Situation</th>
    <th class="th-gray">0<br/>Niemals</th>
    <th class="th-gray">1<br/>Gering</th>
    <th class="th-gray">2<br/>Mittel</th>
    <th class="th-gray">3<br/>Hoch</th>
  </tr>
  {ess_rows}
  <tr style="background:#d0d0d0">
    <td class="td-label" style="font-weight:bold">Gesamtpunktzahl</td>
    <td colspan="4" class="td-label" style="font-weight:bold;font-size:10pt">
      {ess_total} / 24 &nbsp;–&nbsp; {ess_band}
    </td>
  </tr>
</table>

<!-- Datenschutz -->
<h2>Datenschutzerklärung</h2>
<div class="italic-box">
Entsprechend DGSVO unterliegen alle erhobenen Fragen der medizinischen Schweigepflicht.
Sie werden nicht auf Datenträgern gespeichert. Weitergabe nur mit schriftlicher Erlaubnis.
Durch Ihre Unterschrift erklären Sie sich einverstanden.
</div>

<div class="warning-box">
Zur wahrheitsgemäßen Beantwortung <u>a l l e r</u> Fragen sind Sie verpflichtet.
Das Verschweigen von Vorerkrankungen stellt einen Verstoß gegen § 11 FeV dar
und kann rechtliche Konsequenzen haben!
</div>

<table style="margin-top:16px">
  <tr>
    <td style="width:46%;padding-right:8px">
      <div class="sig-line">&nbsp;</div>
      <div class="label-xs">Ort / Datum</div>
    </td>
    <td style="width:8%">&nbsp;</td>
    <td style="width:46%">
      <div class="sig-line">&nbsp;</div>
      <div class="label-xs">Unterschrift Patient</div>
    </td>
  </tr>
</table>


<!-- ══════════════════ SEITE 2 ══════════════════ -->
<div class="page-break"></div>
<h1>Patientenfragebogen – Eigenanamnese</h1>

<div class="header-box">
<table style="width:100%">
  <tr>
    <td style="font-size:9pt;padding:2px 6px;width:33%">Größe: {txt('height')} cm</td>
    <td style="font-size:9pt;padding:2px 6px;width:33%">Gewicht: {txt('weight')} kg</td>
    <td style="font-size:9pt;padding:2px 6px">GdB: {txt('disability_grade', 'k.A.')}</td>
  </tr>
</table>
</div>

<h2>Gesundheitliche Störungen</h2>
<table>
  <tr>
    <th class="th-gray" style="text-align:left">Erkrankung</th>
    <th class="th-gray" style="width:34px">ja</th>
    <th class="th-gray" style="width:34px">nein</th>
  </tr>
  {anamnese_rows}
</table>

<h2>Freitextangaben aus dem Fragebogen</h2>
<table>
  {freitext_rows}
</table>

<h2>Detaillierte Angaben</h2>
<table>
  {yn_row("Brille oder Kontaktlinsen", "glasses", "#f2f2f2")}
  {yn_row("Regelmäßige Nachtfahrten", "night_driving", "#ffffff")}
  {yn_row("Unfälle / Beinahe-Unfälle (letzte 24 Monate)", "accidents", "#f2f2f2")}
  {yn_row("Synkopenabklärung bereits erfolgt", "syncope_workup", "#ffffff")}
  {yn_row("Insulintherapie", "insulin_therapy", "#f2f2f2")}
  {yn_row("Regelmäßige Blutzuckerselbstkontrolle", "glucose_monitoring", "#ffffff")}
  {yn_row("CPAP / Schlaftherapie", "cpap_therapy", "#f2f2f2")}
  {yn_row("Psychotherapie oder psychiatrische Behandlung", "psychiatric_treatment", "#ffffff")}
  {yn_row("Alkohol täglich", "alcohol_daily", "#f2f2f2")}
  {yn_row("Schlaf- oder Beruhigungsmittel", "sleeping_pills", "#ffffff")}
  {yn_row("Einwilligung Wahrheitspflicht bestätigt", "consent_truth", "#f2f2f2")}
  {yn_row("Datenschutzerklärung akzeptiert", "consent_privacy", "#ffffff")}
</table>

<p style="font-size:7.5pt;font-style:italic;margin-top:10px;color:#555">
  Alle Führerscheinklassen: {txt('license_classes')} &nbsp;|&nbsp; Ausgefüllt am: {completed_str}
</p>

</body>
</html>"""
        return html

        def ess_cb(val, n):
            """Checkbox für ESS-Wert"""
            return "&#9745;" if str(val) == str(n) else "&#9744;"

        def yn(val):
            return ("ja" if val == "yes" else "nein") if val else "—"

        ess_labels = [
            "Wenn Sie sitzen und lesen",
            "Beim Fernsehen",
            "Als Zuh&#246;rer bei einem Vortrag, im Kino oder Theater",
            "Als Beifahrer im Auto (Fahrtzeit eine Stunde, keine Pause)",
            "Beim Hinlegen Nachmittags zum Ausruhen",
            "Wenn Sie sich sitzend mit jemandem unterhalten",
            "Im Sitzen nach dem Mittagessen (kein Alkohol getrunken)",
            "Sie m&#252;ssen als Autofahrer vor einer roten Ampel halten",
        ]
        ess_keys = [f"ess_{i}" for i in range(1, 9)]
        ess_total = answer_set.ess_total or 0

        license_arr = a.get("license_classes_arr", [])
        if isinstance(license_arr, str):
            license_arr = [x.strip() for x in license_arr.split(",") if x.strip()]

        def lic_cb(cls):
            return "&#9745;" if cls in license_arr else "&#9744;"

        completed_str = session.completed_at.strftime('%d.%m.%Y') if session.completed_at else ""

        # ── ESS-Tabellenzeilen ──────────────────────────────────────────────
        ess_rows = ""
        for i, (key, label) in enumerate(zip(ess_keys, ess_labels)):
            val = a.get(key, "")
            bg = "#f5f5f5" if i % 2 == 0 else "#ffffff"
            ess_rows += f"""
            <tr style="background:{bg}">
                <td style="border:1px solid #ccc;padding:3px 6px;font-size:9pt">{label}</td>
                <td style="border:1px solid #ccc;padding:3px 6px;text-align:center;font-size:11pt">{ess_cb(val,0)}</td>
                <td style="border:1px solid #ccc;padding:3px 6px;text-align:center;font-size:11pt">{ess_cb(val,1)}</td>
                <td style="border:1px solid #ccc;padding:3px 6px;text-align:center;font-size:11pt">{ess_cb(val,2)}</td>
                <td style="border:1px solid #ccc;padding:3px 6px;text-align:center;font-size:11pt">{ess_cb(val,3)}</td>
            </tr>"""

        # ── Ja/Nein-Tabelle Eigenanamnese ──────────────────────────────────
        def yn_row(label, key, bg):
            val = a.get(key, "")
            return f"""<tr style="background:{bg}">
                <td style="border:1px solid #bbb;padding:3px 6px;font-size:9pt">{label}</td>
                <td style="border:1px solid #bbb;padding:3px;text-align:center;font-size:11pt;width:30px">{cb(val,"yes")}</td>
                <td style="border:1px solid #bbb;padding:3px;text-align:center;font-size:11pt;width:30px">{cb(val,"no")}</td>
            </tr>"""

        anamnese_items = [
            ("Augenkrankheiten / Sehst&#246;rungen",                  "vision_problems"),
            ("Ohrenkrankheiten / H&#246;rst&#246;rungen",             "hearing_aid"),
            ("Herzinfarkt / Koronare Herzerkrankung",                  "heart_attack"),
            ("Herzrhythmusst&#246;rungen / Schrittmacher / ICD",       "arrhythmia"),
            ("Herzinsuffizienz",                                        "heart_failure"),
            ("Epilepsie / Krampfanf&#228;lle",                        "epilepsy"),
            ("Parkinson",                                               "parkinson"),
            ("Multiple Sklerose (MS)",                                  "ms"),
            ("Migr&#228;ne mit Aura",                                  "migraine_aura"),
            ("Gleichgewichtsst&#246;rungen / Schwindel",               "dizziness"),
            ("Ohnmacht / Bewusstlosigkeit",                             "syncope"),
            ("Neurologische Ausf&#228;lle (L&#228;hmung, Sprachst.)", "neuro_deficit"),
            ("Diabetes mellitus",                                       "diabetes_type"),
            ("Unterzuckerung mit Fremdhilfe",                           "hypoglycemia"),
            ("Tagessschl&#228;frigkeit / Sekundenschlaf",              "daytime_sleepiness"),
            ("Schlafapnoe / Schnarchen mit Atemaussetzern",            "snoring"),
            ("Psychiatrische Erkrankung",                               "psychiatric"),
            ("Konzentrations- / Ged&#228;chtnisst&#246;rungen",       "concentration"),
            ("Alkohol (regelm&#228;&#223;iger Konsum)",                "alcohol"),
            ("Drogen- / Substanzkonsum",                                "drugs"),
            ("Sedierende Medikamente",                                  "sedating_meds"),
        ]
        anamnese_rows = ""
        for i, (label, key) in enumerate(anamnese_items):
            bg = "#f5f5f5" if i % 2 == 0 else "#ffffff"
            # Diabetes: 'none' = nein, sonst ja
            if key == "diabetes_type":
                val = a.get(key, "")
                effective = "no" if val in ("none", "", None) else "yes"
                bg_local = "#f5f5f5" if i % 2 == 0 else "#ffffff"
                anamnese_rows += f"""<tr style="background:{bg_local}">
                    <td style="border:1px solid #bbb;padding:3px 6px;font-size:9pt">{label}</td>
                    <td style="border:1px solid #bbb;padding:3px;text-align:center;font-size:11pt;width:30px">{cb(effective,"yes")}</td>
                    <td style="border:1px solid #bbb;padding:3px;text-align:center;font-size:11pt;width:30px">{cb(effective,"no")}</td>
                </tr>"""
            else:
                anamnese_rows += yn_row(label, key, bg)

        driving_hours = a.get("driving_hours", "")
        accidents_desc = a.get("accidents_desc", "")
        vision_desc    = a.get("vision_desc", "")
        meds_desc      = a.get("meds_desc", "")

        html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8"/>
<title>Patientenfragebogen</title>
<style>
  @page {{ size: A4; margin: 18mm 15mm 15mm 15mm; }}
  body {{ font-family: Arial, Helvetica, sans-serif; font-size: 9pt; color: #111; margin: 0; }}
  h1 {{ font-size: 18pt; font-weight: bold; margin: 0 0 12px 0; }}
  h2 {{ font-size: 10pt; font-weight: bold; margin: 10px 0 4px 0; }}
  .section-box {{ background: #e8e8e8; padding: 8px 10px 6px 10px; margin-bottom: 6px; }}
  table {{ width: 100%; border-collapse: collapse; }}
  .page-break {{ page-break-before: always; }}
  .sig-line {{ border-bottom: 1px solid #555; height: 25px; margin-top: 4px; }}
  .label-small {{ font-size: 7.5pt; color: #444; margin-top: 2px; }}
  .italic-box {{ background: #e8e8e8; padding: 8px 10px; font-style: italic; font-size: 8.5pt; margin-bottom: 6px; }}
  .warning-box {{ border: 2px solid #333; padding: 8px 12px; font-style: italic; font-size: 9.5pt; font-weight: bold; margin-top: 8px; }}
  .info-right {{ font-size: 8.5pt; line-height: 1.5; }}
  td.field-cell {{ border-bottom: 1px solid #888; padding: 1px 4px; font-size: 9pt; }}
</style>
</head>
<body>

<!-- ═══════════════════════════ SEITE 1 ═══════════════════════════ -->
<h1>Patientenfragebogen</h1>

<!-- Patientendaten-Box (Seite 1 oben) -->
<div class="section-box">
<table>
  <tr>
    <td style="width:55%;vertical-align:top">
      <table style="width:100%">
        <tr><td style="padding:2px 4px;font-size:9pt">Name:</td><td class="field-cell">&nbsp;</td></tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Vorname:</td><td class="field-cell">&nbsp;</td></tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Geburtsdatum:</td><td class="field-cell">&nbsp;</td></tr>
        <tr>
          <td colspan="2" style="padding:3px 4px;font-size:9pt">
            F&#252;hrerschein:&nbsp;
            {lic_cb('B')} PKW &nbsp;&nbsp;&nbsp;
            {lic_cb('C')} LKW &nbsp;&nbsp;
            {lic_cb('D')} Bus &nbsp;&nbsp;
            Sonstige: {a.get('license_classes','')}
          </td>
        </tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Ausgef&#252;llt am:</td><td class="field-cell">{completed_str}</td></tr>
      </table>
    </td>
    <td style="width:45%;vertical-align:top;padding-left:16px" class="info-right">
      <strong>Dr. med. Bj&#246;rn Micka</strong><br/>
      Betriebsmedizin, Notfallmedizin<br/>
      Christoph-Dassler-Str. 22<br/>
      91074 Herzogenaurach
    </td>
  </tr>
</table>
</div>

<!-- Plötzliches Ausfallrisiko / Warnsymptome -->
<div class="section-box" style="margin-top:8px">
<table>
  <tr>
    <th style="text-align:left;font-size:9pt;padding:2px 4px;width:75%"><strong>Bestehen bei Ihnen folgende Erkrankungen (bitte ankreuzen):</strong></th>
    <th style="width:40px;text-align:center;font-size:9pt">ja</th>
    <th style="width:40px;text-align:center;font-size:9pt">nein</th>
  </tr>
</table>
</div>
<table>
  <tr>
    <th style="text-align:left;padding:3px 6px;font-size:8.5pt;background:#e8e8e8;border:1px solid #bbb">Beschwerde / Erkrankung</th>
    <th style="width:40px;text-align:center;background:#e8e8e8;border:1px solid #bbb;font-size:8.5pt">ja</th>
    <th style="width:40px;text-align:center;background:#e8e8e8;border:1px solid #bbb;font-size:8.5pt">nein</th>
  </tr>
  {yn_row("Bewusstseins- oder Gleichgewichtsst&#246;rungen, Schwindel, sowie Anfallsleiden jeglicher Ursache",
           "syncope", "#f5f5f5")}
  {yn_row("Unbehandelte schlafbezogene Atemst&#246;rungen (Schlaf-Apnoe)",
           "snoring", "#ffffff")}
  {yn_row("Zuckerkrankheit (Diabetes mellitus) mit erheblichen Schwankungen der Blutzucker-Werte insbesondere mit Neigung zum Unterzucker (Hypoglyk&#228;mie)",
           "hypoglycemia", "#f5f5f5")}
  {yn_row("Chronischer Alkoholmissbrauch oder Drogenabh&#228;ngigkeit oder andere Suchtformen",
           "drugs", "#ffffff")}
  {yn_row("Dauerbehandlung mit Medikamenten, die die Fahrt&#252;chtigkeit einschr&#228;nken",
           "sedating_meds", "#f5f5f5")}
  {yn_row("Erkrankungen oder Ver&#228;nderungen des Herzens oder des Kreislaufs mit erheblichen Einschr&#228;nkungen der Leistungs- oder Regulationsf&#228;higkeit, Blutdruckver&#228;nderungen st&#228;rkeren Grades",
           "heart_failure", "#ffffff")}
</table>

<!-- ESS-Abschnitt -->
<h2 style="margin-top:10px">Fragebogen zur Tagesschl&#228;frigkeit (Epworth Sleepiness Scale)</h2>
<div class="italic-box">
Wie leicht f&#228;llt es Ihnen, in folgenden Situationen einzuschlafen?<br/><br/>
Damit ist nicht nur das Gef&#252;hl m&#252;de zu sein gemeint, sondern das tats&#228;chliche Einschlafen. Die Fragen beziehen sich
auf das &#252;bliche t&#228;gliche Leben der vergangenen Wochen. Auch wenn Sie einige der beschriebenen T&#228;tigkeiten in letzter
Zeit nicht ausgef&#252;hrt haben, so versuchen Sie sich vorzustellen, welche Wirkung diese auf Sie gehabt h&#228;tten.<br/><br/>
Kreuzen Sie in der folgenden Tabelle die am besten zutreffende Zahl an:
</div>

<table>
  <tr style="background:#d0d0d0">
    <td style="border:1px solid #ccc;padding:3px 6px;font-size:9pt;width:55%">&nbsp;</td>
    <td style="border:1px solid #ccc;padding:3px;text-align:center;font-size:8pt;width:80px">Niemals<br/>0</td>
    <td style="border:1px solid #ccc;padding:3px;text-align:center;font-size:8pt;width:80px">Gering<br/>1</td>
    <td style="border:1px solid #ccc;padding:3px;text-align:center;font-size:8pt;width:80px">Mittel<br/>2</td>
    <td style="border:1px solid #ccc;padding:3px;text-align:center;font-size:8pt;width:80px">Hoch<br/>3</td>
  </tr>
  {ess_rows}
  <tr style="background:#d0d0d0">
    <td style="border:1px solid #ccc;padding:3px 6px;font-size:9pt;font-weight:bold">Gesamtpunktzahl</td>
    <td colspan="4" style="border:1px solid #ccc;padding:3px 6px;font-weight:bold;font-size:10pt">{ess_total} / 24
      &nbsp;&#8594;&nbsp;
      {"Normal (0&#8211;9)" if ess_total <= 9 else ("Erh&#246;ht (10&#8211;15)" if ess_total <= 15 else "Ausgepr&#228;gt (&#8805;16)")}
    </td>
  </tr>
</table>

<!-- Datenschutzerklärung -->
<h2 style="margin-top:10px">Datenschutzerkl&#228;rung</h2>
<div class="italic-box">
Entsprechend DGSVO (Datenschutz-Grundverordnung) unterliegen alle erhobenen Fragen der medizinischen Schweigepflicht<br/>
- sie werden nicht auf Datentr&#228;ger gespeichert. Weitergabe nur mit ihrer schriftlichen Erlaubnis! Die Personalien werden nur intern f&#252;r den Ausdruck der Bescheinigungen / Gutachten benutzt!<br/>
- Durch Ihre Unterschrift erkl&#228;ren Sie sich hiermit einverstanden.<br/>
- Durch das vorherige Ausf&#252;llen erleichtern Sie dem Arzt die Beurteilung und tragen mit zu einem z&#252;gigen Untersuchungsablauf bei!
</div>

<div class="warning-box">
Zur wahrheitsgem&#228;&#223;en Beantwortung&nbsp;&nbsp;<u>a l l e r</u>&nbsp;&nbsp;Fragen sind Sie verpflichtet.<br/>
Das Verschweigen von Vorerkrankungen stellt einen Versto&#223; gegen &#167;&nbsp;11 FeV<br/>
dar und kann rechtliche Konsequenzen haben!
</div>

<!-- Unterschrift -->
<table style="margin-top:20px">
  <tr>
    <td style="width:48%;padding-right:10px">
      <div class="sig-line">&nbsp;</div>
      <div class="label-small">Ort / Datum</div>
    </td>
    <td style="width:4%">&nbsp;</td>
    <td style="width:48%">
      <div class="sig-line">&nbsp;</div>
      <div class="label-small">Unterschrift Patient</div>
    </td>
  </tr>
</table>


<!-- ═══════════════════════════ SEITE 2 ═══════════════════════════ -->
<div class="page-break"></div>
<h1>Patientenfragebogen</h1>

<!-- Stammdaten -->
<div class="section-box">
<table style="width:100%">
  <tr>
    <td style="width:55%;vertical-align:top">
      <table style="width:100%">
        <tr><td style="padding:2px 4px;font-size:9pt;width:90px">Name:</td><td class="field-cell">&nbsp;</td></tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Vorname:</td><td class="field-cell">&nbsp;</td></tr>
        <tr><td style="padding:2px 4px;font-size:9pt">Geburtsdatum:</td><td class="field-cell">&nbsp;</td></tr>
        <tr>
          <td colspan="2" style="padding:3px 4px;font-size:9pt">
            F&#252;hrerschein:&nbsp;
            {lic_cb('B')} PKW &nbsp;&nbsp;&nbsp;
            {lic_cb('C')} LKW &nbsp;&nbsp;
            Fremdfirma: ________________
          </td>
        </tr>
        <tr><td style="padding:2px 4px;font-size:9pt">derzeitige T&#228;tigkeit:</td><td class="field-cell">{a.get('job_title','')}</td></tr>
      </table>
    </td>
    <td style="width:45%;vertical-align:top;padding-left:16px" class="info-right">
      <strong>Dr. med. Bj&#246;rn Micka</strong><br/>
      Betriebsmedizin, Notfallmedizin<br/>
      Christoph-Dassler-Str. 22<br/>
      91074 Herzogenaurach
    </td>
  </tr>
</table>
</div>

<!-- Eigenanamnese -->
<h2>Eigenanamnese</h2>
<div class="section-box">
<table style="width:100%">
  <tr>
    <td style="font-size:9pt;padding:2px 4px;width:30%">Gr&#246;&#223;e: {a.get('height','')} cm</td>
    <td style="font-size:9pt;padding:2px 4px;width:30%">Gewicht: {a.get('weight','')} kg</td>
    <td style="font-size:9pt;padding:2px 4px">GdB (Grad der Behinderung): {a.get('disability_grade','')}</td>
  </tr>
</table>
</div>

<table>
  <tr>
    <th style="text-align:left;padding:3px 6px;font-size:8.5pt;background:#d0d0d0;border:1px solid #bbb">Gesundheitliche St&#246;rungen</th>
    <th style="width:40px;text-align:center;background:#d0d0d0;border:1px solid #bbb;font-size:8.5pt">ja</th>
    <th style="width:40px;text-align:center;background:#d0d0d0;border:1px solid #bbb;font-size:8.5pt">nein</th>
  </tr>
  {anamnese_rows}
</table>

<!-- Freitext-Felder -->
<table style="margin-top:6px">
  <tr>
    <td style="padding:2px 0;font-size:9pt;width:90px">Medikamente:</td>
    <td class="field-cell">{meds_desc}</td>
  </tr>
  <tr>
    <td style="padding:2px 0;font-size:9pt">Operationen:</td>
    <td class="field-cell">&nbsp;</td>
  </tr>
  <tr>
    <td style="padding:2px 0;font-size:9pt">Schwere Unf&#228;lle:</td>
    <td class="field-cell">{accidents_desc}</td>
  </tr>
</table>

<div style="margin-top:12px">
  <p style="font-size:8pt;font-style:italic">Fahrprofil: {a.get('driving_hours','')} h/Tag &nbsp;|&nbsp;
  Nachtfahrten: {yn(a.get('night_driving'))} &nbsp;|&nbsp;
  Ausgef&#252;llt: {completed_str}</p>
</div>

<div style="position:fixed;bottom:10mm;right:15mm;font-size:7.5pt;font-style:italic">
  bitte beachten Sie die R&#252;ckseite &#x21b5;
</div>

</body>
</html>"""
        return html
