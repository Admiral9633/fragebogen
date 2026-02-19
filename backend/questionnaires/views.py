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
        """Generiere HTML – exakter Wortlaut aus Online-Fragebogen, 2 Seiten"""
        a = answer_set.answers_json

        def x(val, target="yes"):
            """Angekreuzte oder leere Box"""
            if str(val) == str(target):
                return '<span class="cb-x">&#10003;</span>'
            return '<span class="cb-o">&nbsp;</span>'

        def yn(val):
            if val == "yes": return "Ja"
            if val == "no":  return "Nein"
            return "—"

        def v(key, fallback="—"):
            r = str(a.get(key, "") or "").strip()
            return r if r else fallback

        def row(label, key, subtext=None, bg="#ffffff", cls=""):
            val = a.get(key, "")
            sub = f'<div class="sub">{subtext}</div>' if subtext else ""
            row_cls = cls if cls else ""
            return (f'<tr style="background:{bg}" class="{row_cls}">'
                    f'<td class="q">{label}{sub}</td>'
                    f'<td class="c">{x(val,"yes")}</td>'
                    f'<td class="c">{x(val,"no")}</td></tr>')

        def row_ft(label, key, ft_key, ft_label="Beschreibung", bg="#ffffff"):
            """Ja/Nein Zeile mit Freitext direkt darunter wenn ausgefüllt"""
            val = a.get(key, "")
            ft  = str(a.get(ft_key, "") or "").strip()
            sub = f'<div class="ft">{ft_label}: {ft}</div>' if ft else ""
            return (f'<tr style="background:{bg}">'
                    f'<td class="q">{label}{sub}</td>'
                    f'<td class="c">{x(val,"yes")}</td>'
                    f'<td class="c">{x(val,"no")}</td></tr>')

        # ── Führerscheinklassen ────────────────────────────────────────────
        lic_arr = a.get("license_classes_arr", [])
        if isinstance(lic_arr, str):
            lic_arr = [s.strip() for s in lic_arr.split(",") if s.strip()]
        lic_str = v("license_classes")

        # ── Alkohol-Antwort ────────────────────────────────────────────────
        alc_map = {"none":"Keinen","occasional":"Gelegentlich","regular":"Regelmäßig","risky":"Riskant"}
        alc_val = alc_map.get(a.get("alcohol",""), "—")

        # ── Diabetes ──────────────────────────────────────────────────────
        dt_map = {"none":"Kein Diabetes","type1":"Typ 1","type2":"Typ 2"}
        dt_val = dt_map.get(a.get("diabetes_type",""), "—")
        has_dm = a.get("diabetes_type","") not in ("none","",None)
        th_map = {"insulin":"Insulin","tablets":"Tabletten","diet":"Diät","other":"Sonstige"}
        th_val = th_map.get(a.get("diabetes_therapy",""), "")

        # ── ESS ───────────────────────────────────────────────────────────
        ess_q = [
            "Beim Sitzen und Lesen",
            "Beim Fernsehen",
            "Wenn Sie passiv in der Öffentlichkeit sitzen (z.B. im Theater oder bei einer Besprechung)",
            "Als Beifahrer im Auto während einer einstündigen Fahrt ohne Pause",
            "Wenn Sie sich am Nachmittag hingelegt haben, um auszuruhen",
            "Wenn Sie sitzen und sich mit jemandem unterhalten",
            "Wenn Sie nach dem Mittagessen (ohne Alkohol) ruhig dasitzen",
            "Wenn Sie als Fahrer eines Autos verkehrsbedingt einige Minuten halten müssen",
        ]
        ess_rows = ""
        for i, label in enumerate(ess_q):
            val = str(a.get(f"ess_{i+1}", ""))
            bg  = "#f5f5f5" if i % 2 == 0 else "#fff"
            ess_rows += (f'<tr style="background:{bg}">'
                         f'<td class="q">{i+1}. {label}</td>'
                         f'<td class="c">{x(val,"0")}</td>'
                         f'<td class="c">{x(val,"1")}</td>'
                         f'<td class="c">{x(val,"2")}</td>'
                         f'<td class="c">{x(val,"3")}</td></tr>')

        ess_total = answer_set.ess_total or 0
        if ess_total <= 9:   ess_band = f"{ess_total}/24 – Normal (0–9)"
        elif ess_total <= 15: ess_band = f"{ess_total}/24 – Erhöht (10–15)"
        else:                 ess_band = f"{ess_total}/24 – Ausgeprägt (≥16) – ärztliche Abklärung erforderlich"

        completed = session.completed_at.strftime('%d.%m.%Y') if session.completed_at else "—"

        # ── Einwilligung ──────────────────────────────────────────────────
        consent_truth   = a.get("consent_truth", False)
        consent_privacy = a.get("consent_privacy", False)

        html = f"""<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8"/>
<title>Verkehrsmedizinischer Fragebogen</title>
<style>
  @page {{ size: A4; margin: 14mm 13mm 12mm 13mm; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: Helvetica, Arial, sans-serif; font-size: 8pt; color: #1a1a1a; margin:0; line-height:1.35; }}
  h1 {{ font-size:13pt; font-weight:bold; color:#1f3864; margin:0 0 6px 0; letter-spacing:0.3pt; }}
  h2 {{ font-size:7.5pt; font-weight:bold; color:#ffffff; background:#1f3864;
        margin:7px 0 0 0; padding:2px 6px; border:none; }}
  table {{ width:100%; border-collapse:collapse; margin-bottom:3px; }}
  .c {{ border:1px solid #aab; width:26px; text-align:center; padding:1px; vertical-align:middle; }}
  .q {{ border:1px solid #ccd; padding:2px 6px; vertical-align:middle; }}
  .cb-x {{ display:inline-block; width:12px; height:12px;
           background:#1f3864; color:#ffffff;
           text-align:center; font-size:9pt; font-weight:bold; line-height:12px;
           border:1px solid #1f3864; }}
  .cb-o {{ display:inline-block; width:12px; height:12px;
           background:#ffffff; border:1.5px solid #8899aa; }}
  .th  {{ background:#1f3864; color:#ffffff; border:1px solid #1f3864;
          padding:2px 4px; font-size:7.5pt; text-align:center; font-weight:bold; }}
  .thl {{ background:#1f3864; color:#ffffff; border:1px solid #1f3864;
          padding:2px 6px; font-size:7.5pt; font-weight:bold; }}
  .hdr {{ background:#eef1f7; border:1px solid #c8d0e0; padding:5px 8px; margin-bottom:5px; }}
  .italic-box {{ background:#f0f4fb; border:1px solid #c8d0e0; padding:4px 8px;
                 font-style:italic; font-size:7.5pt; margin-bottom:2px; }}
  .warn {{ border:2px solid #1f3864; background:#f7f0f0; padding:5px 8px;
           font-style:italic; font-size:8pt; font-weight:bold; margin:5px 0; color:#1a1a1a; }}
  .sig  {{ border-bottom:1px solid #555; height:22px; margin-top:3px; }}
  .xs   {{ font-size:7pt; color:#555; margin-top:1px; }}
  .sub  {{ font-size:7pt; color:#666; font-style:italic; margin-top:1px; }}
  .ft   {{ font-size:7.5pt; color:#333; font-style:italic; margin-top:1px; padding-left:8px;
           border-left:2px solid #1f3864; }}
  .val  {{ font-weight:bold; }}
  .page-break {{ page-break-before:always; }}
  .r1 {{ background:#f3f5fa; }}
  .r2 {{ background:#ffffff; }}
</style></head><body>

<!-- �?�?�?�?�?�? SEITE 1 �?�?�?�?�?�? -->
<h1>Verkehrsmedizinischer Fragebogen</h1>

<div class="hdr">
<table><tr>
  <td style="width:55%;vertical-align:top">
    <table style="width:100%">
      <tr><td style="width:90px;padding:1px 4px">Name:</td><td style="border-bottom:1px solid #888">&nbsp;</td></tr>
      <tr><td style="padding:1px 4px">Vorname:</td><td style="border-bottom:1px solid #888">&nbsp;</td></tr>
      <tr><td style="padding:1px 4px">Geburtsdatum:</td><td style="border-bottom:1px solid #888">&nbsp;</td></tr>
    </table>
  </td>
  <td style="width:45%;padding-left:12px;vertical-align:top;font-size:8pt;line-height:1.6">
    <strong>Dr. med. Björn Micka</strong><br/>
    Betriebsmedizin, Notfallmedizin<br/>
    Christoph-Dassler-Str. 22, 91074 Herzogenaurach
  </td>
</tr></table>
<div style="margin-top:3px;font-size:8pt">
  Ausgefüllt am: <span class="val">{completed}</span>
</div>
</div>

<!-- 1. Fahrprofil -->
<h2>1. Fahrprofil</h2>
<table>
  <tr class="r1"><td class="q">Führerscheinklassen</td>
    <td colspan="2" class="q"><span class="val">{lic_str}</span></td></tr>
  <tr class="r2"><td class="q">Fahrzeit pro Tag (Stunden)</td>
    <td colspan="2" class="q"><span class="val">{v('driving_hours')}</span></td></tr>
  {row("Regelmäßige Nachtfahrten","night_driving",bg="#f5f5f5")}
  {row_ft("Unfälle oder Beinahe-Unfälle in den letzten 24 Monaten","accidents","accidents_desc","Beschreibung",bg="#fff")}
</table>

<!-- 2. Warnsymptome -->
<h2>2. Warnsymptome – Plötzliches Ausfallrisiko</h2>
<table>
  <tr class="thl"><td class="thl">Frage</td><td class="th">ja</td><td class="th">nein</td></tr>
  {row("Ohnmacht oder Bewusstlosigkeit in den letzten 5 Jahren","syncope",bg="#f5f5f5")}
  {row("Krampfanfälle oder epileptische Anfälle","seizures",bg="#fff")}
  {row("Schwindelattacken","dizziness",bg="#f5f5f5")}
  {row("Neurologische Ausfälle (z.B. Lähmung, Sprachstörung)","neuro_deficit",bg="#fff")}
</table>

<!-- 3. Sehen & Hören -->
<h2>3. Sehen &amp; Hören</h2>
<table>
  <tr class="thl"><td class="thl">Frage</td><td class="th">ja</td><td class="th">nein</td></tr>
  {row("Brille oder Kontaktlinsen","glasses",bg="#f5f5f5")}
  {row_ft("Sehprobleme (Doppeltsehen, Gesichtsfeldausfälle, Nachtsehen)","vision_problems","vision_desc","Art der Sehprobleme",bg="#fff")}
  {row("Hörgerät oder relevante Hörstörung","hearing_aid",bg="#f5f5f5")}
</table>

<!-- 4. Herz-Kreislauf -->
<h2>4. Herz-Kreislauf</h2>
<table>
  <tr class="thl"><td class="thl">Frage</td><td class="th">ja</td><td class="th">nein</td></tr>
  {row("Herzinfarkt oder koronare Erkrankung","heart_attack",bg="#f5f5f5")}
  {row("Rhythmusstörungen, Schrittmacher oder ICD","arrhythmia",bg="#fff")}
  {row("Herzinsuffizienz","heart_failure",bg="#f5f5f5")}
  {row("Synkopenabklärung bereits erfolgt","syncope_workup",bg="#fff")}
</table>

<!-- 5. Neurologie -->
<h2>5. Neurologie</h2>
<table>
  <tr class="thl"><td class="thl">Frage</td><td class="th">ja</td><td class="th">nein</td></tr>
  {row("Epilepsie","epilepsy",bg="#f5f5f5")}
  {row("Parkinson","parkinson",bg="#fff")}
  {row("Multiple Sklerose (MS)","ms",bg="#f5f5f5")}
  {row("Migräne mit Aura","migraine_aura",bg="#fff")}
  {row("Gleichgewichtsstörungen","balance_disorder",bg="#f5f5f5")}
</table>

<!-- �?�?�?�?�?�? SEITE 2 �?�?�?�?�?�? -->
<div class="page-break"></div>
<h1>Verkehrsmedizinischer Fragebogen – Seite 2</h1>

<!-- 6. Diabetes / Stoffwechsel -->
<h2>6. Diabetes / Stoffwechsel</h2>
<table>
  <tr class="r1"><td class="q">Diabetesform</td>
    <td colspan="2" class="q"><span class="val">{dt_val}</span></td></tr>
  {row("Hypoglykämie mit Fremdhilfe in den letzten 12 Monaten","hypoglycemia",bg="#fff")}"""

        if has_dm:
            html += f"""
  <tr class="r1"><td class="q">Hypowahrnehmungsstörung</td>
    <td class="c">{x(a.get('hypo_awareness',''),'yes')}</td>
    <td class="c">{x(a.get('hypo_awareness',''),'no')}</td></tr>
  <tr class="r2"><td class="q">Aktuelle Therapie</td>
    <td colspan="2" class="q"><span class="val">{th_val}</span></td></tr>"""

        html += f"""
</table>

<!-- 7. Schlaf & Tagesschläfrigkeit -->
<h2>7. Schlaf &amp; Tagesschläfrigkeit</h2>
<table>
  <tr class="thl"><td class="thl">Frage</td><td class="th">ja</td><td class="th">nein</td></tr>
  {row("Ausgeprägte Tagesmüdigkeit","daytime_sleepiness",bg="#f5f5f5")}
  {row("Sekundenschlaf beim Fahren","microsleep",bg="#fff")}
  {row("Schnarchen oder Atemaussetzer","snoring",bg="#f5f5f5")}
</table>
<div class="italic-box">
  <strong>Epworth Sleepiness Scale (ESS)</strong> – Wie wahrscheinlich ist es, dass Sie in den folgenden
  Situationen einnicken würden?&nbsp; 0 = Nie &nbsp;·&nbsp; 1 = Gering &nbsp;·&nbsp; 2 = Mittel &nbsp;·&nbsp; 3 = Hoch
</div>
<table>
  <tr>
    <td class="thl" style="width:62%">Situation</td>
    <td class="th">0</td><td class="th">1</td><td class="th">2</td><td class="th">3</td>
  </tr>
  {ess_rows}
  <tr style="background:#1f3864">
    <td class="q" style="font-weight:bold;color:#ffffff;border:1px solid #1f3864">Gesamtpunktzahl</td>
    <td colspan="4" class="q" style="font-weight:bold;color:#ffffff;border:1px solid #1f3864">{ess_band}</td>
  </tr>
</table>

<!-- 8. Psychische Gesundheit -->
<h2>8. Psychische Gesundheit</h2>
<table>
  <tr class="thl"><td class="thl">Frage</td><td class="th">ja</td><td class="th">nein</td></tr>
  {row_ft("Depression, Angststörung oder andere psychiatrische Erkrankung","psychiatric","psychiatric_desc","Art der Erkrankung",bg="#f5f5f5")}
  {row("Stationäre psychiatrische Behandlung in den letzten 5 Jahren","psychiatric_inpatient",bg="#fff")}
  {row("Konzentrations- oder Gedächtnisprobleme","concentration",bg="#f5f5f5")}
</table>

<!-- 9. Substanzen & Medikamente -->
<h2>9. Substanzen &amp; Medikamente</h2>
<table>
  <tr class="r1"><td class="q">Alkohol (Regelmäßiger oder riskanter Konsum)</td>
    <td colspan="2" class="q"><span class="val">{alc_val}</span></td></tr>
  {row_ft("Drogenkonsum aktuell oder früher","drugs","drugs_desc","Art und Zeitraum",bg="#fff")}
  {row_ft("Medikamente mit sedierender Wirkung","sedating_meds","sedating_meds_desc","Welche Medikamente",bg="#f5f5f5")}
  {row("Nebenwirkungen wie Schläfrigkeit oder Schwindel","side_effects",bg="#fff")}
</table>

<!-- 10. Einwilligung -->
<h2>10. Einwilligung &amp; Datenschutz</h2>
<div class="italic-box">
  Entsprechend DSGVO unterliegen alle Angaben der medizinischen Schweigepflicht.
  Sie werden nicht dauerhaft auf Datenträgern gespeichert.
</div>
<table>
  <tr class="r1">
    <td class="q">Ich bestätige, dass meine Angaben <strong>vollständig und wahrheitsgemäß</strong> sind.</td>
    <td class="c">{x(consent_truth, True)}</td>
    <td class="c">{x(not consent_truth, True)}</td>
  </tr>
  <tr class="r2">
    <td class="q">Ich habe die <strong>Datenschutzhinweise</strong> gelesen und willige in die Verarbeitung meiner Daten zu verkehrsmedizinischen Zwecken ein.</td>
    <td class="c">{x(consent_privacy, True)}</td>
    <td class="c">{x(not consent_privacy, True)}</td>
  </tr>
</table>

<div class="warn">
  Zur wahrheitsgemäßen Beantwortung <u>a l l e r</u> Fragen sind Sie verpflichtet.
  Das Verschweigen von Vorerkrankungen stellt einen Verstoß gegen § 11 FeV dar
  und kann rechtliche Konsequenzen haben!
</div>

<table style="margin-top:10px">
  <tr>
    <td style="width:44%;padding-right:8px">
      <div class="sig">&nbsp;</div><div class="xs">Ort / Datum</div>
    </td>
    <td style="width:12%">&nbsp;</td>
    <td style="width:44%">
      <div class="sig">&nbsp;</div><div class="xs">Unterschrift Patient</div>
    </td>
  </tr>
</table>

</body></html>"""
        return html

