import logging
import os
import secrets
from datetime import datetime, timedelta

from django.conf import settings
from django.db import IntegrityError, transaction
from django.utils import timezone
from django.utils.html import escape
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404

from .models import QuestionnaireSession, AnswerSet, QuestionnaireTemplate
from .serializers import (
    SubmitSerializer,
    QuestionnaireSessionSerializer,
)
from .schema import is_v2_schema, validate_answers
from .evaluation import evaluate_answers
from .translations import available_languages, load_translation

logger = logging.getLogger(__name__)


def parse_birth_date(value):
    """'YYYY-MM-DD' oder 'TT.MM.YYYY' → date | None (None auch bei leerem String)."""
    value = (value or '').strip()
    if not value:
        return None
    for fmt in ('%Y-%m-%d', '%d.%m.%Y'):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    raise ValueError(f'Ungültiges Datumsformat: {value}')


class AdminApiKeyPermission(BasePermission):
    """Einfacher API-Key-Schutz für Admin-Endpunkte."""
    def has_permission(self, request, view):
        admin_key = os.environ.get('ADMIN_API_KEY', '')
        if not admin_key:
            return False
        auth = request.META.get('HTTP_AUTHORIZATION', '')
        return secrets.compare_digest(auth, f'Bearer {admin_key}')


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
        # Schema laden (fuer die Validierung), ohne DB-Lock
        base_session = get_object_or_404(
            QuestionnaireSession.objects.select_related('template'), token=token
        )
        template_schema = base_session.template.schema_json

        if is_v2_schema(template_schema):
            # Schema-getriebene Validierung: nur bekannte Fragen werden gespeichert
            validated_data, schema_errors = validate_answers(template_schema, request.data)
            if schema_errors:
                return Response(schema_errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Legacy-Templates (v1): fixe ESS+Consent-Validierung
            serializer = SubmitSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
            validated_data = serializer.validated_data

        # Atomar: Doppel-Submit (Doppelklick, paralleler POST) sauber abfangen
        try:
            with transaction.atomic():
                session = get_object_or_404(
                    QuestionnaireSession.objects.select_for_update(), token=token
                )

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

                AnswerSet.objects.create(
                    session=session,
                    answers_json=validated_data,
                    ess_total=validated_data['ess_total'],
                    ess_band=validated_data['ess_band']
                )

                session.completed = True
                session.completed_at = timezone.now()
                session.save()
        except IntegrityError:
            return Response(
                {'error': 'Dieser Fragebogen wurde bereits ausgefüllt.'},
                status=status.HTTP_400_BAD_REQUEST
            )

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
        if session.is_expired():
            # Zugriffsfenster: Nach Ablauf des Links auch keine Ergebnisse mehr ausliefern
            return Response(
                {'error': 'Dieser Link ist abgelaufen.'},
                status=status.HTTP_410_GONE
            )
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
            'schema': session.template.schema_json,
            'evaluation': evaluate_answers(answer_set.answers_json),
            'ess_total': answer_set.ess_total,
            'ess_band': answer_set.ess_band,
            'completed_at': session.completed_at.strftime('%d.%m.%Y') if session.completed_at else None,
            'token': str(token),
            'patient_last_name': session.patient_last_name,
            'patient_first_name': session.patient_first_name,
            'patient_birth_date': session.patient_birth_date.strftime('%d.%m.%Y') if session.patient_birth_date else '',
        })


class TranslationView(APIView):
    """
    GET /api/i18n/            – verfügbare Sprachcodes
    GET /api/i18n/<lang>/     – Sprachdatei (UI-Texte + übersetzte Fragen)
    """
    def get(self, request, lang=None):
        if lang is None:
            return Response({'languages': available_languages()})
        data = load_translation(lang)
        if data is None:
            return Response(
                {'error': f'Sprache "{lang}" nicht verfügbar.'},
                status=status.HTTP_404_NOT_FOUND,
            )
        response = Response(data)
        # Sprachdateien ändern sich nur mit Deployments – aggressiv cachen
        response['Cache-Control'] = 'public, max-age=3600'
        return response


def _send_invitation_email(session):
    """Sendet die Einladungs-E-Mail an den Patienten."""
    url = f"{settings.APP_URL}/q/{session.token}"
    patient_name = f"{session.patient_first_name} {session.patient_last_name}".strip()
    valid_until = timezone.localtime(session.expires_at).strftime('%d.%m.%Y')
    subject = "Ihr verkehrsmedizinischer Fragebogen"
    text_body = (
        f"Sehr geehrte/r {patient_name},\n\n"
        "bitte füllen Sie vor Ihrem Termin den beigefügten Fragebogen aus:\n\n"
        f"{url}\n\n"
        f"Der Link ist bis zum {valid_until} gültig.\n\n"
        "Mit freundlichen Grüßen\n"
        "Dr. med. Björn Micka\n"
        "Betriebsmedizin · Notfallmedizin\n"
        "Christoph-Dassler-Str. 22, 91074 Herzogenaurach"
    )
    html_body = (
        f"<p>Sehr geehrte/r {escape(patient_name)},</p>"
        "<p>bitte füllen Sie vor Ihrem Termin den folgenden Fragebogen aus:</p>"
        f'<p><a href="{url}" style="font-size:16px;font-weight:bold;">Fragebogen öffnen</a></p>'
        f'<p style="color:#666;font-size:12px;">Direktlink: {url}</p>'
        f"<p>Der Link ist bis zum {valid_until} gültig.</p>"
        "<hr><p style='font-size:12px;color:#666;'>"
        "Dr. med. Björn Micka · Betriebsmedizin · Notfallmedizin<br>"
        "Christoph-Dassler-Str. 22, 91074 Herzogenaurach</p>"
    )
    send_mail(
        subject=subject,
        message=text_body,
        from_email=settings.EMAIL_FROM,
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
        sessions = (
            QuestionnaireSession.objects.all()
            .select_related('template')
            .prefetch_related('answers')
            .order_by('-created_at')
        )
        data = []
        for s in sessions:
            row = {
                'token': str(s.token),
                'patient_last_name': s.patient_last_name,
                'patient_first_name': s.patient_first_name,
                'patient_email': s.patient_email,
                'patient_birth_date': s.patient_birth_date.strftime('%d.%m.%Y') if s.patient_birth_date else '',
                'completed': s.completed,
                'completed_at': s.completed_at.strftime('%d.%m.%Y %H:%M') if s.completed_at else None,
                'created_at': s.created_at.strftime('%d.%m.%Y %H:%M'),
                'expires_at': s.expires_at.strftime('%d.%m.%Y'),
                'expired': s.is_expired(),
                'invitation_sent_at': s.invitation_sent_at.strftime('%d.%m.%Y %H:%M') if s.invitation_sent_at else None,
                'gdt_patient_id': s.gdt_patient_id,
                'gdt_result_delivered_at': (
                    s.gdt_result_delivered_at.strftime('%d.%m.%Y %H:%M')
                    if s.gdt_result_delivered_at else None
                ),
                'ess_total': None,
                'ess_band': None,
                'auswertung': None,
            }
            if s.completed:
                try:
                    answer_set = s.answers
                except AnswerSet.DoesNotExist:
                    answer_set = None
                if answer_set:
                    row['ess_total'] = answer_set.ess_total
                    row['ess_band'] = answer_set.ess_band
                    row['auswertung'] = evaluate_answers(
                        answer_set.answers_json
                    )['zusammenfassung']
            data.append(row)
        return Response(data)

    def post(self, request):
        d = request.data
        last_name = d.get('patient_last_name', '').strip()
        first_name = d.get('patient_first_name', '').strip()
        email = d.get('patient_email', '').strip()

        if not last_name or not first_name:
            return Response({'error': 'Name und Vorname sind erforderlich.'}, status=400)

        if email:
            from django.core.validators import validate_email
            from django.core.exceptions import ValidationError
            try:
                validate_email(email)
            except ValidationError:
                return Response({'error': 'Ungültige E-Mail-Adresse.'}, status=400)

        try:
            birth_date = parse_birth_date(d.get('patient_birth_date', ''))
        except ValueError:
            return Response({'error': 'Ungültiges Datumsformat.'}, status=400)

        template = QuestionnaireTemplate.objects.filter(is_active=True).order_by('-version').first()
        if not template:
            return Response({'error': 'Kein aktiver Fragebogen-Template gefunden.'}, status=500)

        session = QuestionnaireSession.objects.create(
            template=template,
            patient_last_name=last_name,
            patient_first_name=first_name,
            patient_email=email,
            patient_birth_date=birth_date,
            expires_at=timezone.now() + timedelta(days=settings.SESSION_VALIDITY_DAYS),
        )

        sent = False
        error_msg = None
        if email:
            try:
                _send_invitation_email(session)
                sent = True
            except Exception as e:
                sent = False
                error_msg = str(e)

        return Response({
            'token': str(session.token),
            'email_sent': sent,
            'email_error': error_msg,
        }, status=201)


class AdminSessionDetailView(APIView):
    """
    GET /api/admin/sessions/<token>/detail/ – vollständige Sicht für die Praxis:
    Patientendaten, Status, Antworten, Schema (für Anzeige-Labels) und die
    komplette automatische Auswertung inkl. Konsequenzen. Bewusst OHNE
    Ablauf-Sperre – der Arzt braucht auch nach Linkablauf vollen Zugriff.
    """
    permission_classes = [AdminApiKeyPermission]

    def get(self, request, token):
        session = get_object_or_404(
            QuestionnaireSession.objects.select_related('template'), token=token
        )
        data = {
            'token': str(session.token),
            'patient_last_name': session.patient_last_name,
            'patient_first_name': session.patient_first_name,
            'patient_email': session.patient_email,
            'patient_birth_date': (
                session.patient_birth_date.strftime('%d.%m.%Y')
                if session.patient_birth_date else ''
            ),
            'completed': session.completed,
            'completed_at': (
                session.completed_at.strftime('%d.%m.%Y %H:%M')
                if session.completed_at else None
            ),
            'created_at': session.created_at.strftime('%d.%m.%Y %H:%M'),
            'expires_at': session.expires_at.strftime('%d.%m.%Y %H:%M'),
            'expired': session.is_expired(),
            'invitation_sent_at': (
                session.invitation_sent_at.strftime('%d.%m.%Y %H:%M')
                if session.invitation_sent_at else None
            ),
            'gdt_patient_id': session.gdt_patient_id,
            'gdt_request_id': session.gdt_request_id,
            'gdt_result_delivered_at': (
                session.gdt_result_delivered_at.strftime('%d.%m.%Y %H:%M')
                if session.gdt_result_delivered_at else None
            ),
            'answers': None,
            'schema': session.template.schema_json,
            'evaluation': None,
            'ess_total': None,
            'ess_band': None,
        }
        if session.completed:
            try:
                answer_set = session.answers
            except AnswerSet.DoesNotExist:
                answer_set = None
            if answer_set:
                data['answers'] = answer_set.answers_json
                data['evaluation'] = evaluate_answers(answer_set.answers_json)
                data['ess_total'] = answer_set.ess_total
                data['ess_band'] = answer_set.ess_band
        return Response(data)


class AdminUpdateSessionView(APIView):
    """
    PATCH /api/admin/sessions/<token>/update/  – Patientendaten ändern
    """
    permission_classes = [AdminApiKeyPermission]

    def patch(self, request, token):
        session = get_object_or_404(QuestionnaireSession, token=token)
        d = request.data

        if 'patient_last_name' in d:
            session.patient_last_name = d['patient_last_name'].strip()
        if 'patient_first_name' in d:
            session.patient_first_name = d['patient_first_name'].strip()
        if 'patient_email' in d:
            email = d['patient_email'].strip()
            if email:
                from django.core.validators import validate_email
                from django.core.exceptions import ValidationError
                try:
                    validate_email(email)
                except ValidationError:
                    return Response({'error': 'Ungültige E-Mail-Adresse.'}, status=400)
            session.patient_email = email
        if 'patient_birth_date' in d:
            try:
                session.patient_birth_date = parse_birth_date(d['patient_birth_date'])
            except ValueError:
                return Response({'error': 'Ungültiges Datumsformat.'}, status=400)
        session.save()
        return Response({'success': True})


class AdminResendEmailView(APIView):
    """
    POST /api/admin/sessions/<token>/resend/  – Einladung erneut senden
    """
    permission_classes = [AdminApiKeyPermission]

    def post(self, request, token):
        session = get_object_or_404(QuestionnaireSession, token=token)
        if session.completed:
            return Response({'error': 'Dieser Fragebogen wurde bereits ausgefüllt.'}, status=400)
        if not session.patient_email:
            return Response({'error': 'Keine E-Mail-Adresse hinterlegt.'}, status=400)
        # Gültigkeit verlängern, damit die Angabe in der neuen Mail stimmt
        session.expires_at = timezone.now() + timedelta(days=settings.SESSION_VALIDITY_DAYS)
        session.save(update_fields=['expires_at'])
        try:
            _send_invitation_email(session)
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
        try:
            birth_date = parse_birth_date(d.get('patient_birth_date', ''))
        except ValueError as exc:
            return Response(
                {'error': f'{exc}. Erwartet YYYY-MM-DD.'},
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

        patient_email = d.get('patient_email', '').strip()

        session = QuestionnaireSession.objects.create(
            template           = template,
            patient_last_name  = last_name,
            patient_first_name = first_name,
            patient_birth_date = birth_date,
            patient_email      = patient_email,
            gdt_patient_id     = d.get('gdt_patient_id',  '').strip(),
            gdt_request_id     = d.get('gdt_request_id',  '').strip(),
            expires_at         = timezone.now() + timedelta(days=settings.SESSION_VALIDITY_DAYS),
        )

        questionnaire_url = f"{settings.APP_URL}/q/{session.token}"

        email_sent = False
        email_error = None
        if patient_email:
            try:
                _send_invitation_email(session)
                email_sent = True
            except Exception as exc:
                # E-Mail-Fehler blockiert die GDT-Session nicht, wird aber gemeldet
                email_error = str(exc)
                logger.error('Einladungs-Mail fehlgeschlagen (Session %s): %s', session.token, exc)

        return Response(
            {
                'token':       str(session.token),
                'url':         questionnaire_url,
                'email_sent':  email_sent,
                'email_error': email_error,
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
            if session.is_expired():
                # Abgelaufen und nie ausgefüllt: Bridge soll den Eintrag verwerfen
                return Response(
                    {'error': 'Session abgelaufen.'},
                    status=status.HTTP_410_GONE,
                )
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

        evaluation = evaluate_answers(answer_set.answers_json)

        # Merken, dass die Bridge das Ergebnis abgeholt hat (→ Ergebnis-GDT an SAMAS)
        if session.gdt_result_delivered_at is None:
            session.gdt_result_delivered_at = timezone.now()
            session.save(update_fields=['gdt_result_delivered_at'])

        return Response({
            'completed':          True,
            'auswertung_kritisch': evaluation['zusammenfassung']['kritisch'],
            'auswertung_pruefen':  evaluation['zusammenfassung']['pruefen'],
            'auswertung_hinweis':  evaluation['zusammenfassung']['hinweis'],
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
