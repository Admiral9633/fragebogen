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

from .catalog import CATALOG
from .models import AnswerSet, QuestionnaireSession, QuestionnaireTemplate
from .schema import ESS_KEYS, is_visible, iter_questions
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


def build_valid_answers(schema, overrides=None):
    """Minimal gültiger Antwortsatz für ein v2-Schema (sichtbarkeitsbewusst)."""
    answers = dict(overrides or {})
    # Mehrere Durchläufe, weil Sichtbarkeit von bereits gesetzten Antworten abhängt
    for _ in range(4):
        for _section, q in iter_questions(schema):
            qid = q["id"]
            if qid in answers or not is_visible(q, answers):
                continue
            qtype = q.get("type")
            if qtype == "yes_no":
                answers[qid] = "no"
            elif qtype == "choice":
                answers[qid] = q["options"][0]["value"]
            elif qtype == "multi_choice":
                answers[qid] = [q["options"][0]["value"]]
            elif qtype == "consent":
                answers[qid] = True
            elif qtype == "ess_matrix":
                for key in ESS_KEYS:
                    answers.setdefault(key, 1)
    return answers


class KatalogV2Tests(TestCase):
    def setUp(self):
        call_command('load_catalog', verbosity=0)
        self.template = QuestionnaireTemplate.objects.get(slug='verkehrsmedizin-leitlinien')
        self.session = QuestionnaireSession.objects.create(
            template=self.template,
            patient_last_name='Mustermann',
            patient_first_name='Max',
            expires_at=timezone.now() + timedelta(days=14),
        )

    def submit(self, answers):
        return self.client.post(
            f'/api/submit/{self.session.token}/', answers,
            content_type='application/json',
        )

    def test_load_catalog_deaktiviert_alte_templates(self):
        alt = QuestionnaireTemplate.objects.create(
            slug='alt', version=1, schema_json={'sections': ['ess']}, is_active=True
        )
        call_command('load_catalog', verbosity=0)
        alt.refresh_from_db()
        self.template.refresh_from_db()
        self.assertFalse(alt.is_active)
        self.assertTrue(self.template.is_active)

    def test_gueltiger_submit_berechnet_ess(self):
        res = self.submit(build_valid_answers(CATALOG))
        self.assertEqual(res.status_code, 201, res.json())
        self.assertEqual(res.json()['ess_total'], 8)
        self.assertEqual(res.json()['ess_band'], 'normal')

    def test_fehlende_einwilligung_gibt_400(self):
        answers = build_valid_answers(CATALOG)
        answers['consent_privacy'] = False
        res = self.submit(answers)
        self.assertEqual(res.status_code, 400)
        self.assertIn('consent_privacy', res.json())

    def test_fehlende_pflichtfrage_gibt_400(self):
        answers = build_valid_answers(CATALOG)
        del answers['night_driving']
        res = self.submit(answers)
        self.assertEqual(res.status_code, 400)
        self.assertIn('night_driving', res.json())

    def test_unbekannte_keys_werden_verworfen(self):
        answers = build_valid_answers(CATALOG)
        answers['hack'] = '<script>alert(1)</script>'
        res = self.submit(answers)
        self.assertEqual(res.status_code, 201, res.json())
        stored = self.session.answers.answers_json
        self.assertNotIn('hack', stored)

    def test_versteckte_folgefrage_wird_nicht_verlangt(self):
        # exam_occasion=pkw → psych_test_done ist unsichtbar und darf nicht fehlen
        answers = build_valid_answers(CATALOG)
        self.assertEqual(answers['exam_occasion'], 'pkw')
        self.assertNotIn('psych_test_done', answers)
        res = self.submit(answers)
        self.assertEqual(res.status_code, 201, res.json())

    def test_sichtbare_bedingte_frage_wird_verlangt(self):
        answers = build_valid_answers(CATALOG, overrides={'exam_occasion': 'bus'})
        answers.pop('psych_test_done', None)
        res = self.submit(answers)
        self.assertEqual(res.status_code, 400)
        self.assertIn('psych_test_done', res.json())

    def test_pdf_v2_rendert_und_escaped(self):
        answers = build_valid_answers(CATALOG, overrides={
            'accidents': 'yes',
            'accidents_desc': '<script>alert(1)</script>',
        })
        res = self.submit(answers)
        self.assertEqual(res.status_code, 201, res.json())
        answer_set = self.session.answers
        html = GeneratePDFView()._generate_html(self.session, answer_set)
        self.assertIn('Epworth Sleepiness Scale', html)
        self.assertIn('Anlass &amp; Fahrprofil', html)
        self.assertNotIn('<script>alert(1)</script>', html)
        self.assertIn('&lt;script&gt;alert(1)&lt;/script&gt;', html)

    def test_ess_wertebereich_wird_geprueft(self):
        answers = build_valid_answers(CATALOG)
        answers['ess_3'] = 7
        res = self.submit(answers)
        self.assertEqual(res.status_code, 400)
        self.assertIn('ess_3', res.json())


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
