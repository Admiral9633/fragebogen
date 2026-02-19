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
        """Generiere HTML für PDF Export"""
        answers = answer_set.answers_json
        
        html = f"""
        <!DOCTYPE html>
        <html lang="de">
        <head>
            <meta charset="UTF-8">
            <title>Verkehrsmedizinischer Fragebogen</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    line-height: 1.6;
                }}
                h1 {{
                    color: #2c3e50;
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 10px;
                }}
                h2 {{
                    color: #34495e;
                    margin-top: 30px;
                }}
                .info-box {{
                    background: #f8f9fa;
                    padding: 15px;
                    border-left: 4px solid #3498db;
                    margin: 20px 0;
                }}
                .ess-result {{
                    background: #e8f4f8;
                    padding: 20px;
                    border-radius: 5px;
                    margin: 20px 0;
                }}
                .ess-score {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #2980b9;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }}
                th {{
                    background: #3498db;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background: #f2f2f2;
                }}
                .footer {{
                    margin-top: 50px;
                    font-size: 12px;
                    color: #7f8c8d;
                    border-top: 1px solid #ddd;
                    padding-top: 20px;
                }}
            </style>
        </head>
        <body>
            <h1>Verkehrsmedizinischer Fragebogen</h1>
            
            <div class="info-box">
                <strong>Session-ID:</strong> {session.token}<br>
                <strong>Ausgefüllt am:</strong> {session.completed_at.strftime('%d.%m.%Y %H:%M') if session.completed_at else 'N/A'}<br>
                <strong>Template:</strong> {session.template.slug} (Version {session.template.version})
            </div>
            
            <div class="ess-result">
                <h2>Epworth Sleepiness Scale (ESS) - Ergebnis</h2>
                <p class="ess-score">Gesamtscore: {answer_set.ess_total} / 24</p>
                <p><strong>Bewertung:</strong> {answer_set.ess_band.upper()}</p>
                
                <table>
                    <thead>
                        <tr>
                            <th>Situation</th>
                            <th>Wert</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>ESS 1 - Sitzend beim Lesen</td><td>{answers.get('ess_1', 0)}</td></tr>
                        <tr><td>ESS 2 - Beim Fernsehen</td><td>{answers.get('ess_2', 0)}</td></tr>
                        <tr><td>ESS 3 - Passiv in öffentlichen Räumen</td><td>{answers.get('ess_3', 0)}</td></tr>
                        <tr><td>ESS 4 - Als Beifahrer im Auto (1 Std.)</td><td>{answers.get('ess_4', 0)}</td></tr>
                        <tr><td>ESS 5 - Nachmittags beim Hinlegen</td><td>{answers.get('ess_5', 0)}</td></tr>
                        <tr><td>ESS 6 - Sitzend im Gespräch</td><td>{answers.get('ess_6', 0)}</td></tr>
                        <tr><td>ESS 7 - Nach dem Mittagessen</td><td>{answers.get('ess_7', 0)}</td></tr>
                        <tr><td>ESS 8 - Im Auto bei Verkehrsstau</td><td>{answers.get('ess_8', 0)}</td></tr>
                    </tbody>
                </table>
                
                <p><em>Bewertung: 0 = würde nie einnicken, 1 = geringe Wahrscheinlichkeit, 
                2 = mittlere Wahrscheinlichkeit, 3 = hohe Wahrscheinlichkeit</em></p>
            </div>
            
            <h2>Interpretation</h2>
            <ul>
                <li><strong>Normal (0-9):</strong> Keine erhöhte Tagesschläfrigkeit</li>
                <li><strong>Erhöht (10-15):</strong> Erhöhte Tagesschläfrigkeit, weitere Abklärung empfohlen</li>
                <li><strong>Ausgeprägt (≥16):</strong> Stark erhöhte Tagesschläfrigkeit, ärztliche Abklärung erforderlich</li>
            </ul>
            
            <div class="footer">
                <p>Dokument erstellt am: {timezone.now().strftime('%d.%m.%Y %H:%M')}</p>
                <p>Rechtsgrundlage: FeV Anlage 4, BASt Begutachtungsleitlinien</p>
            </div>
        </body>
        </html>
        """
        return html
