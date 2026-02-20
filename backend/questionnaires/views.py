import os
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import QuestionnaireSession, AnswerSet, QuestionnaireTemplate
from .serializers import (
    SubmitSerializer,
    QuestionnaireSessionSerializer,
    AnswerSetSerializer
)


class AdminApiKeyPermission(BasePermission):
    """Einfacher API-Key-Schutz für Admin-Endpunkte."""
    def has_permission(self, request, view):
        admin_key = os.environ.get('ADMIN_API_KEY', '')
        if not admin_key:
            return False
        auth = request.META.get('HTTP_AUTHORIZATION', '')
        return auth == f'Bearer {admin_key}'


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


class AnswersView(APIView):
    """
    GET: Gibt Antworten als JSON zurück (für Puppeteer-Print-Page)
    """
    def get(self, request, token):
        session = get_object_or_404(QuestionnaireSession, token=token)
        if not session.completed:
            return Response(
                {'error': 'Session noch nicht abgeschlossen.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            answer_set = session.answers
        except AnswerSet.DoesNotExist:
            return Response({'error': 'Keine Antworten gefunden.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            'answers': answer_set.answers_json,
            'ess_total': answer_set.ess_total,
            'ess_band': answer_set.ess_band,
            'completed_at': session.completed_at.strftime('%d.%m.%Y') if session.completed_at else None,
            'token': str(token),
            'patient_last_name': session.patient_last_name,
            'patient_first_name': session.patient_first_name,
            'patient_birth_date': session.patient_birth_date.strftime('%d.%m.%Y') if session.patient_birth_date else '',
        })


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


def _send_invitation_email(session, app_url):
    """Sendet die Einladungs-E-Mail an den Patienten."""
    url = f"{app_url}/q/{session.token}"
    patient_name = f"{session.patient_first_name} {session.patient_last_name}".strip()
    subject = "Ihr verkehrsmedizinischer Fragebogen"
    text_body = (
        f"Sehr geehrte/r {patient_name},\n\n"
        "bitte füllen Sie vor Ihrem Termin den beigefügten Fragebogen aus:\n\n"
        f"{url}\n\n"
        "Der Link ist 14 Tage gültig.\n\n"
        "Mit freundlichen Grüßen\n"
        "Dr. med. Björn Micka\n"
        "Betriebsmedizin · Notfallmedizin\n"
        "Christoph-Dassler-Str. 22, 91074 Herzogenaurach"
    )
    html_body = (
        f"<p>Sehr geehrte/r {patient_name},</p>"
        "<p>bitte füllen Sie vor Ihrem Termin den folgenden Fragebogen aus:</p>"
        f'<p><a href="{url}" style="font-size:16px;font-weight:bold;">Fragebogen öffnen</a></p>'
        f'<p style="color:#666;font-size:12px;">Direktlink: {url}</p>'
        "<p>Der Link ist 14 Tage gültig.</p>"
        "<hr><p style='font-size:12px;color:#666;'>"
        "Dr. med. Björn Micka · Betriebsmedizin · Notfallmedizin<br>"
        "Christoph-Dassler-Str. 22, 91074 Herzogenaurach</p>"
    )
    from_email = os.environ.get('EMAIL_FROM', 'noreply@example.com')
    send_mail(
        subject=subject,
        message=text_body,
        from_email=from_email,
        recipient_list=[session.patient_email],
        html_message=html_body,
        fail_silently=False,
    )
    session.invitation_sent_at = timezone.now()
    session.save(update_fields=['invitation_sent_at'])


class AdminSessionListView(APIView):
    """
    GET  /api/admin/sessions/  – alle Sessions auflisten
    POST /api/admin/sessions/  – neue Session anlegen + E-Mail senden
    """
    permission_classes = [AdminApiKeyPermission]

    def get(self, request):
        sessions = QuestionnaireSession.objects.all().order_by('-created_at')
        data = []
        for s in sessions:
            data.append({
                'token': str(s.token),
                'patient_last_name': s.patient_last_name,
                'patient_first_name': s.patient_first_name,
                'patient_email': s.patient_email,
                'patient_birth_date': s.patient_birth_date.strftime('%d.%m.%Y') if s.patient_birth_date else '',
                'completed': s.completed,
                'completed_at': s.completed_at.strftime('%d.%m.%Y %H:%M') if s.completed_at else None,
                'created_at': s.created_at.strftime('%d.%m.%Y %H:%M'),
                'expires_at': s.expires_at.strftime('%d.%m.%Y'),
                'invitation_sent_at': s.invitation_sent_at.strftime('%d.%m.%Y %H:%M') if s.invitation_sent_at else None,
                'gdt_patient_id': s.gdt_patient_id,
            })
        return Response(data)

    def post(self, request):
        d = request.data
        last_name = d.get('patient_last_name', '').strip()
        first_name = d.get('patient_first_name', '').strip()
        email = d.get('patient_email', '').strip()
        birth_date_str = d.get('patient_birth_date', '').strip()

        if not last_name or not first_name or not email:
            return Response({'error': 'Name, Vorname und E-Mail sind erforderlich.'}, status=400)

        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
        except ValidationError:
            return Response({'error': 'Ungültige E-Mail-Adresse.'}, status=400)

        birth_date = None
        if birth_date_str:
            from datetime import datetime as dt
            for fmt in ('%Y-%m-%d', '%d.%m.%Y'):
                try:
                    birth_date = dt.strptime(birth_date_str, fmt).date()
                    break
                except ValueError:
                    continue

        template = QuestionnaireTemplate.objects.filter(is_active=True).order_by('-version').first()
        if not template:
            return Response({'error': 'Kein aktiver Fragebogen-Template gefunden.'}, status=500)

        from datetime import timedelta
        session = QuestionnaireSession.objects.create(
            template=template,
            patient_last_name=last_name,
            patient_first_name=first_name,
            patient_email=email,
            patient_birth_date=birth_date,
            expires_at=timezone.now() + timedelta(days=14),
        )

        app_url = os.environ.get('APP_URL', 'http://localhost:3000')
        try:
            _send_invitation_email(session, app_url)
            sent = True
            error_msg = None
        except Exception as e:
            sent = False
            error_msg = str(e)

        return Response({
            'token': str(session.token),
            'email_sent': sent,
            'email_error': error_msg,
        }, status=201)


class AdminResendEmailView(APIView):
    """
    POST /api/admin/sessions/<token>/resend/  – Einladung erneut senden
    """
    permission_classes = [AdminApiKeyPermission]

    def post(self, request, token):
        session = get_object_or_404(QuestionnaireSession, token=token)
        if not session.patient_email:
            return Response({'error': 'Keine E-Mail-Adresse hinterlegt.'}, status=400)
        app_url = os.environ.get('APP_URL', 'http://localhost:3000')
        try:
            _send_invitation_email(session, app_url)
            return Response({'success': True})
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class AdminDeleteSessionView(APIView):
    """
    DELETE /api/admin/sessions/<token>/  – Session löschen
    """
    permission_classes = [AdminApiKeyPermission]

    def delete(self, request, token):
        session = get_object_or_404(QuestionnaireSession, token=token)
        session.delete()
        return Response({'success': True})


class GdtSessionCreateView(APIView):
    """
    POST /api/gdt/session/
    Wird vom GDT-Bridge Windows Service aufgerufen.
    Erstellt eine neue Fragebogen-Session aus GDT-Patientendaten
    und gibt Token + URL zurück. Keine E-Mail-Pflicht.

    Body (JSON):
    {
        "patient_last_name":  "Mustermann",
        "patient_first_name": "Max",
        "patient_birth_date": "1975-03-21",   // YYYY-MM-DD
        "gdt_patient_id":     "12345",         // GDT Feld 3000
        "gdt_request_id":     "REQ-001",       // GDT Feld 8315 (optional)
        "template_slug":      "ess-fragebogen" // optional, Default: erster aktiver Template
    }

    Response (201):
    {
        "token": "<uuid>",
        "url":   "https://app.example.com/q/<uuid>"
    }
    """
    permission_classes = [AdminApiKeyPermission]

    def post(self, request):
        d = request.data
        last_name  = d.get('patient_last_name',  '').strip()
        first_name = d.get('patient_first_name', '').strip()

        if not last_name or not first_name:
            return Response(
                {'error': 'patient_last_name und patient_first_name sind erforderlich.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Geburtsdatum parsen (YYYY-MM-DD oder TT.MM.YYYY)
        birth_date = None
        birth_date_str = d.get('patient_birth_date', '').strip()
        if birth_date_str:
            from datetime import datetime as _dt
            for fmt in ('%Y-%m-%d', '%d.%m.%Y'):
                try:
                    birth_date = _dt.strptime(birth_date_str, fmt).date()
                    break
                except ValueError:
                    continue
            if birth_date is None:
                return Response(
                    {'error': f'Ungültiges Datumsformat: {birth_date_str}. Erwartet YYYY-MM-DD.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # Template holen
        template_slug = d.get('template_slug', '').strip()
        if template_slug:
            template = QuestionnaireTemplate.objects.filter(
                slug=template_slug, is_active=True
            ).order_by('-version').first()
            if not template:
                return Response(
                    {'error': f'Template "{template_slug}" nicht gefunden.'},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            template = QuestionnaireTemplate.objects.filter(
                is_active=True
            ).order_by('-version').first()
            if not template:
                return Response(
                    {'error': 'Kein aktiver Fragebogen-Template vorhanden.'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        from datetime import timedelta
        session = QuestionnaireSession.objects.create(
            template           = template,
            patient_last_name  = last_name,
            patient_first_name = first_name,
            patient_birth_date = birth_date,
            gdt_patient_id     = d.get('gdt_patient_id',  '').strip(),
            gdt_request_id     = d.get('gdt_request_id',  '').strip(),
            expires_at         = timezone.now() + timedelta(days=14),
        )

        app_url = os.environ.get('APP_URL', 'http://localhost:3000')
        questionnaire_url = f"{app_url}/q/{session.token}"

        return Response(
            {
                'token': str(session.token),
                'url':   questionnaire_url,
            },
            status=status.HTTP_201_CREATED,
        )


class GdtResultView(APIView):
    """
    GET /api/gdt/result/<token>/
    Wird vom GDT-Bridge Windows Service nach Abschluss des Fragebogens abgefragt.
    Gibt Ergebnisdaten im GDT-freundlichen Format zurück.

    Response (200, wenn abgeschlossen):
    {
        "completed":         true,
        "completed_at":      "21.03.2026",
        "gdt_patient_id":    "12345",
        "gdt_request_id":    "REQ-001",
        "patient_last_name": "Mustermann",
        "patient_first_name":"Max",
        "patient_birth_date":"21.03.1975",
        "ess_total":         8,
        "ess_band":          "normal",
        "ess_band_text":     "Normal (0–9)"
    }

    Response (202, noch nicht abgeschlossen):
    { "completed": false }
    """
    permission_classes = [AdminApiKeyPermission]

    def get(self, request, token):
        session = get_object_or_404(QuestionnaireSession, token=token)

        if not session.completed:
            return Response({'completed': False}, status=status.HTTP_202_ACCEPTED)

        try:
            answer_set = session.answers
        except Exception:
            return Response(
                {'error': 'Antworten nicht gefunden.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        band_map = {
            'normal':      'Normal (0–9)',
            'erhöht':      'Erhöht (10–15)',
            'ausgeprägt':  'Ausgeprägt (≥16) – ärztliche Abklärung erforderlich',
        }

        return Response({
            'completed':          True,
            'completed_at':       session.completed_at.strftime('%d.%m.%Y') if session.completed_at else '',
            'gdt_patient_id':     session.gdt_patient_id,
            'gdt_request_id':     session.gdt_request_id,
            'patient_last_name':  session.patient_last_name,
            'patient_first_name': session.patient_first_name,
            'patient_birth_date': session.patient_birth_date.strftime('%d.%m.%Y') if session.patient_birth_date else '',
            'ess_total':          answer_set.ess_total,
            'ess_band':           answer_set.ess_band,
            'ess_band_text':      band_map.get(answer_set.ess_band or '', answer_set.ess_band or ''),
        })
