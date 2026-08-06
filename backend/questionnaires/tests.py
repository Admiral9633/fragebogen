"""
API-Tests für den Fragebogen-Kern: Submit, Ablauf, Escaping, Admin-Schutz, Purge.

Ausführen mit: python manage.py test questionnaires
"""
import os
from datetime import timedelta
from unittest import mock

from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from .models import AnswerSet, QuestionnaireSession, QuestionnaireTemplate
from .views import GeneratePDFView


def make_session(**kwargs):
    template = QuestionnaireTemplate.objects.filter(slug='test-v1').first()
    if template is None:
        template = QuestionnaireTemplate.objects.create(
            slug='test-v1', version=1, schema_json={'sections': ['ess']}, is_active=True
        )
    defaults = {
        'template': template,
        'patient_last_name': 'Mustermann',
        'patient_first_name': 'Max',
        'expires_at': timezone.now() + timedelta(days=14),
    }
    defaults.update(kwargs)
    return QuestionnaireSession.objects.create(**defaults)


def valid_submit_payload(**extra):
    payload = {f'ess_{i}': 1 for i in range(1, 9)}
    payload.update({'consent_truth': True, 'consent_privacy': True})
    payload.update(extra)
    return payload


class SubmitTests(TestCase):
    def test_submit_berechnet_ess_und_schliesst_ab(self):
        session = make_session()
        res = self.client.post(
            f'/api/submit/{session.token}/',
            valid_submit_payload(),
            content_type='application/json',
        )
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json()['ess_total'], 8)
        self.assertEqual(res.json()['ess_band'], 'normal')
        session.refresh_from_db()
        self.assertTrue(session.completed)

    def test_doppelter_submit_gibt_400(self):
        session = make_session()
        first = self.client.post(
            f'/api/submit/{session.token}/',
            valid_submit_payload(),
            content_type='application/json',
        )
        self.assertEqual(first.status_code, 201)
        second = self.client.post(
            f'/api/submit/{session.token}/',
            valid_submit_payload(),
            content_type='application/json',
        )
        self.assertEqual(second.status_code, 400)
        self.assertEqual(AnswerSet.objects.filter(session=session).count(), 1)

    def test_abgelaufener_link_gibt_410(self):
        session = make_session(expires_at=timezone.now() - timedelta(days=1))
        res = self.client.get(f'/api/session/{session.token}/')
        self.assertEqual(res.status_code, 410)


class ErgebnisZugriffTests(TestCase):
    def _completed_session(self, **kwargs):
        session = make_session(**kwargs)
        AnswerSet.objects.create(
            session=session,
            answers_json=valid_submit_payload(),
            ess_total=8,
            ess_band='normal',
        )
        session.completed = True
        session.completed_at = timezone.now()
        session.save()
        return session

    def test_answers_liefert_daten(self):
        session = self._completed_session()
        res = self.client.get(f'/api/answers/{session.token}/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['ess_total'], 8)

    def test_answers_und_pdf_nach_ablauf_410(self):
        session = self._completed_session(
            expires_at=timezone.now() - timedelta(days=1)
        )
        self.assertEqual(
            self.client.get(f'/api/answers/{session.token}/').status_code, 410
        )
        self.assertEqual(
            self.client.get(f'/api/pdf/{session.token}/').status_code, 410
        )

    def test_pdf_html_escaped_patienten_eingaben(self):
        session = self._completed_session()
        answer_set = session.answers
        answer_set.answers_json = valid_submit_payload(
            accidents='yes',
            accidents_desc='<script>alert(1)</script>',
            license_classes='<b>B</b>',
            driving_hours='<img src=x onerror=alert(1)>',
        )
        answer_set.save()

        html = GeneratePDFView()._generate_html(session, answer_set)
        self.assertNotIn('<script>alert(1)</script>', html)
        self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;', html)
        self.assertNotIn('<img src=x', html)
        self.assertNotIn('<b>B</b>', html)


class AdminApiKeyTests(TestCase):
    def test_ohne_key_403(self):
        res = self.client.get('/api/admin/sessions/')
        self.assertEqual(res.status_code, 403)

    @mock.patch.dict(os.environ, {'ADMIN_API_KEY': 'test-key-123'})
    def test_mit_key_200_und_gdt_ablauf_410(self):
        auth = {'HTTP_AUTHORIZATION': 'Bearer test-key-123'}
        self.assertEqual(
            self.client.get('/api/admin/sessions/', **auth).status_code, 200
        )
        expired = make_session(expires_at=timezone.now() - timedelta(days=1))
        res = self.client.get(f'/api/gdt/result/{expired.token}/', **auth)
        self.assertEqual(res.status_code, 410)

    @mock.patch.dict(os.environ, {'ADMIN_API_KEY': 'test-key-123'})
    def test_falscher_key_403(self):
        res = self.client.get(
            '/api/admin/sessions/', HTTP_AUTHORIZATION='Bearer falscher-key'
        )
        self.assertEqual(res.status_code, 403)


class PurgeSessionsTests(TestCase):
    def test_purge_loescht_nur_lange_abgelaufene(self):
        alt = make_session(expires_at=timezone.now() - timedelta(days=45))
        frisch = make_session(expires_at=timezone.now() - timedelta(days=5))
        aktiv = make_session()

        call_command('purge_sessions', '--days', '30', verbosity=0)

        tokens = set(
            QuestionnaireSession.objects.values_list('token', flat=True)
        )
        self.assertNotIn(alt.token, tokens)
        self.assertIn(frisch.token, tokens)
        self.assertIn(aktiv.token, tokens)
