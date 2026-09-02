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
from .catalogs import CATALOG_REGISTRY
from .evaluation import evaluate_answers, evaluate_for_template
from .models import AnswerSet, QuestionnaireSession, QuestionnaireTemplate
from .schema import ESS_KEYS, is_visible, iter_questions, validate_answers


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

    def test_answers_nach_ablauf_410(self):
        session = self._completed_session(
            expires_at=timezone.now() - timedelta(days=1)
        )
        self.assertEqual(
            self.client.get(f'/api/answers/{session.token}/').status_code, 410
        )

    def test_answers_enthaelt_auswertung(self):
        session = self._completed_session()
        res = self.client.get(f'/api/answers/{session.token}/')
        self.assertEqual(res.status_code, 200)
        evaluation = res.json()['evaluation']
        self.assertIn('findings', evaluation)
        self.assertIn('zusammenfassung', evaluation)
        self.assertIn('disclaimer', evaluation)


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
            elif qtype in ("text", "textarea"):
                if q.get("required"):
                    answers[qid] = "Testangabe"
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

    def test_gateway_nein_ueberspringt_diagnoseblöcke(self):
        answers = build_valid_answers(CATALOG)
        self.assertEqual(answers.get('has_conditions'), 'no')
        # Diagnose-Einstiegsfragen sind unsichtbar und werden nicht verlangt
        for qid in ('diabetes_type', 'heart_disease', 'psychiatric', 'kidney_disease'):
            self.assertNotIn(qid, answers)
        res = self.submit(answers)
        self.assertEqual(res.status_code, 201, res.json())
        # Symptom-Screening bleibt Pflicht
        self.assertIn('microsleep', answers)
        self.assertIn('syncope', answers)

    def test_gateway_ja_verlangt_diagnoseblöcke(self):
        answers = build_valid_answers(CATALOG, overrides={'has_conditions': 'yes'})
        self.assertIn('diabetes_type', answers)
        del answers['heart_disease']
        res = self.submit(answers)
        self.assertEqual(res.status_code, 400)
        self.assertIn('heart_disease', res.json())

    def test_ess_wertebereich_wird_geprueft(self):
        answers = build_valid_answers(CATALOG)
        answers['ess_3'] = 7
        res = self.submit(answers)
        self.assertEqual(res.status_code, 400)
        self.assertIn('ess_3', res.json())


class AuswertungTests(TestCase):
    """Regelwerk der automatischen BASt-Auswertung (evaluation.py)."""

    def test_unauffaelliger_fragebogen_ohne_befunde(self):
        answers = build_valid_answers(CATALOG)
        result = evaluate_answers(answers)
        self.assertFalse(result['gruppe2'])
        self.assertEqual(result['zusammenfassung']['kritisch'], 0)
        self.assertEqual(result['zusammenfassung']['pruefen'], 0)

    def test_frischer_anfall_und_sekundenschlaf_sind_kritisch(self):
        answers = build_valid_answers(CATALOG, overrides={
            'seizure_ever': 'yes',
            'seizure_free': 'unter3m',
            'antiepileptics': 'aktuell',
            'microsleep': 'yes',
        })
        result = evaluate_answers(answers)
        kritisch = [f for f in result['findings'] if f['schwere'] == 'kritisch']
        self.assertGreaterEqual(len(kritisch), 2)
        kapitel = {f['kapitel'] for f in kritisch}
        self.assertIn('3.9.6', kapitel)
        self.assertIn('3.11.1', kapitel)
        # kritisch sortiert vor pruefen/hinweis
        self.assertEqual(result['findings'][0]['schwere'], 'kritisch')

    def test_gruppe2_verschaerft_epilepsie_und_icd(self):
        answers = build_valid_answers(CATALOG, overrides={
            'exam_occasion': 'lkw',
            'seizure_ever': 'yes',
            'seizure_free': 'ueber5j',
            'epilepsy': 'yes',
            'antiepileptics': 'nie',
            'pacemaker_icd': 'icd',
            'icd_shock': 'no',
        })
        result = evaluate_answers(answers)
        self.assertTrue(result['gruppe2'])
        bereiche = {
            f['bereich'] for f in result['findings'] if f['schwere'] == 'kritisch'
        }
        self.assertIn('Epilepsie', bereiche)
        self.assertIn('Defibrillator (ICD)', bereiche)

    def test_ess_grenzwert_elf_ausloest_abklaerung(self):
        ess_hoch = {f'ess_{i}': 2 for i in range(1, 9)}  # Summe 16
        answers = build_valid_answers(CATALOG, overrides=ess_hoch)
        answers['ess_total'] = 16
        result = evaluate_answers(answers)
        ess_findings = [f for f in result['findings'] if f['kapitel'] == '3.11.1']
        self.assertTrue(any(f['schwere'] == 'kritisch' for f in ess_findings))

    def test_taeglicher_cannabiskonsum_ist_kritisch_nach_3_13_2_2(self):
        # Neu (Stand 19.08.2026): Cannabis eigenständig in 3.13.2, nicht mehr BtM (3.14.1)
        answers = build_valid_answers(CATALOG, overrides={'cannabis': 'taeglich'})
        result = evaluate_answers(answers)
        cannabis = [f for f in result['findings'] if f['kapitel'] == '3.13.2.2']
        self.assertTrue(any(f['schwere'] == 'kritisch' for f in cannabis))
        self.assertFalse(any(f['kapitel'] == '3.14.1' for f in result['findings']))

    def test_gelegentlicher_cannabiskonsum_nur_hinweis(self):
        answers = build_valid_answers(CATALOG, overrides={'cannabis': 'gelegentlich'})
        result = evaluate_answers(answers)
        cannabis = [f for f in result['findings'] if f['kapitel'] == '3.13.2.2']
        self.assertEqual(len(cannabis), 1)
        self.assertEqual(cannabis[0]['schwere'], 'hinweis')

    def test_medizinalcannabis_faellt_unter_dauermedikation_3_14_2(self):
        answers = build_valid_answers(CATALOG, overrides={
            'cannabis': 'taeglich',
            'cannabis_medical': 'yes',
        })
        result = evaluate_answers(answers)
        kapitel = {f['kapitel'] for f in result['findings']}
        self.assertIn('3.14.2', kapitel)
        self.assertNotIn('3.13.2.2', kapitel)

    def test_reanimation_ist_kritisch_nach_3_4_10(self):
        answers = build_valid_answers(CATALOG, overrides={'resuscitated': 'yes'})
        result = evaluate_answers(answers)
        treffer = [f for f in result['findings'] if f['kapitel'] == '3.4.10']
        self.assertTrue(any(f['schwere'] == 'kritisch' for f in treffer))

    def test_schlaganfall_ohne_residuen_gruppe2_kein_regelausschluss_mehr(self):
        # Neu (3.9.4, gültig ab 19.08.2026): pauschaler Gruppe-2-Ausschluss entfallen
        answers = build_valid_answers(CATALOG, overrides={
            'exam_occasion': 'lkw',
            'stroke': 'yes',
            'stroke_prevention': 'yes',
        })
        result = evaluate_answers(answers)
        self.assertTrue(result['gruppe2'])
        schlaganfall = [f for f in result['findings'] if f['kapitel'] == '3.9.4']
        self.assertTrue(schlaganfall)
        self.assertTrue(all(f['schwere'] == 'pruefen' for f in schlaganfall))

    def test_hypoglykaemie_wiederholt_kritisch_einmalig_pruefen(self):
        # 3.5: erst die wiederholte schwere Hypoglykämie schließt die Eignung aus
        basis = {'has_conditions': 'yes', 'diabetes_type': 'type2'}
        wiederholt = build_valid_answers(
            CATALOG, overrides=dict(basis, hypoglycemia='repeated')
        )
        result = evaluate_answers(wiederholt)
        diabetes = [f for f in result['findings'] if f['kapitel'] == '3.5']
        self.assertTrue(any(f['schwere'] == 'kritisch' for f in diabetes))

        einmalig = build_valid_answers(
            CATALOG, overrides=dict(basis, hypoglycemia='once')
        )
        result = evaluate_answers(einmalig)
        diabetes = [f for f in result['findings'] if f['kapitel'] == '3.5']
        self.assertTrue(diabetes)
        self.assertTrue(all(f['schwere'] == 'pruefen' for f in diabetes))

    def test_gdt_result_liefert_auswertungs_zusammenfassung(self):
        call_command('load_catalog', verbosity=0)
        template = QuestionnaireTemplate.objects.get(slug='verkehrsmedizin-leitlinien')
        session = QuestionnaireSession.objects.create(
            template=template,
            patient_last_name='Mustermann', patient_first_name='Max',
            expires_at=timezone.now() + timedelta(days=14),
        )
        answers = build_valid_answers(CATALOG, overrides={'microsleep': 'yes'})
        res = self.client.post(
            f'/api/submit/{session.token}/', answers, content_type='application/json'
        )
        self.assertEqual(res.status_code, 201, res.json())
        with mock.patch.dict(os.environ, {'ADMIN_API_KEY': 'test-key-123'}):
            res = self.client.get(
                f'/api/gdt/result/{session.token}/',
                HTTP_AUTHORIZATION='Bearer test-key-123',
            )
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(res.json()['auswertung_kritisch'], 1)


class AdminCockpitTests(TestCase):
    """Admin-Liste mit Auswertung, Detail-Endpunkt, GDT-Übermittlungsstatus."""

    def setUp(self):
        call_command('load_catalog', verbosity=0)
        self.template = QuestionnaireTemplate.objects.get(slug='verkehrsmedizin-leitlinien')
        self.auth = {'HTTP_AUTHORIZATION': 'Bearer cockpit-key'}
        self.env = mock.patch.dict(os.environ, {'ADMIN_API_KEY': 'cockpit-key'})
        self.env.start()
        self.addCleanup(self.env.stop)

    def _completed(self, **overrides):
        session = QuestionnaireSession.objects.create(
            template=self.template,
            patient_last_name='Mustermann', patient_first_name='Max',
            gdt_patient_id=overrides.pop('gdt_patient_id', ''),
            expires_at=timezone.now() + timedelta(days=14),
        )
        answers = build_valid_answers(CATALOG, overrides=overrides)
        res = self.client.post(
            f'/api/submit/{session.token}/', answers, content_type='application/json'
        )
        assert res.status_code == 201, res.json()
        return session

    def test_liste_enthaelt_auswertung_und_ess(self):
        self._completed(microsleep='yes')
        res = self.client.get('/api/admin/sessions/', **self.auth)
        self.assertEqual(res.status_code, 200)
        row = res.json()[0]
        self.assertEqual(row['ess_total'], 8)
        self.assertGreaterEqual(row['auswertung']['kritisch'], 1)
        self.assertIn('expired', row)

    def test_detail_liefert_findings_mit_konsequenzen(self):
        session = self._completed(microsleep='yes')
        res = self.client.get(f'/api/admin/sessions/{session.token}/detail/', **self.auth)
        self.assertEqual(res.status_code, 200)
        d = res.json()
        self.assertIsNotNone(d['answers'])
        self.assertIn('sections', d['schema'])
        findings = d['evaluation']['findings']
        self.assertTrue(any(f['schwere'] == 'kritisch' for f in findings))
        self.assertTrue(all('konsequenz' in f and 'kapitel' in f for f in findings))

    def test_detail_funktioniert_auch_nach_ablauf(self):
        session = self._completed()
        session.expires_at = timezone.now() - timedelta(days=1)
        session.save()
        res = self.client.get(f'/api/admin/sessions/{session.token}/detail/', **self.auth)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()['expired'])

    def test_detail_ohne_key_403(self):
        session = self._completed()
        res = self.client.get(f'/api/admin/sessions/{session.token}/detail/')
        self.assertEqual(res.status_code, 403)

    def test_template_liste_fuer_einladung(self):
        res = self.client.get('/api/admin/templates/', **self.auth)
        self.assertEqual(res.status_code, 200)
        slugs = {t['slug'] for t in res.json()}
        self.assertIn('verkehrsmedizin-leitlinien', slugs)
        self.assertTrue(all('title' in t and 'basis' in t for t in res.json()))

    def test_anlage_ohne_slug_nimmt_verkehrsmedizin(self):
        res = self.client.post(
            '/api/admin/sessions/',
            {'patient_last_name': 'Test', 'patient_first_name': 'Default'},
            content_type='application/json', **self.auth,
        )
        self.assertEqual(res.status_code, 201, res.json())
        session = QuestionnaireSession.objects.get(token=res.json()['token'])
        self.assertEqual(session.template.slug, 'verkehrsmedizin-leitlinien')

    def test_anlage_mit_unbekanntem_slug_400(self):
        res = self.client.post(
            '/api/admin/sessions/',
            {'patient_last_name': 'Test', 'patient_first_name': 'Falsch',
             'template_slug': 'gibt-es-nicht'},
            content_type='application/json', **self.auth,
        )
        self.assertEqual(res.status_code, 400)

    def test_gdt_abruf_setzt_uebermittelt_zeitstempel(self):
        session = self._completed(gdt_patient_id='4711')
        self.assertIsNone(session.gdt_result_delivered_at)
        res = self.client.get(f'/api/gdt/result/{session.token}/', **self.auth)
        self.assertEqual(res.status_code, 200)
        session.refresh_from_db()
        self.assertIsNotNone(session.gdt_result_delivered_at)
        liste = self.client.get('/api/admin/sessions/', **self.auth).json()
        self.assertIsNotNone(liste[0]['gdt_result_delivered_at'])


class TranslationTests(TestCase):
    def test_sprachliste_enthaelt_deutsch(self):
        res = self.client.get('/api/i18n/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('de', res.json()['languages'])

    def test_deutsche_sprachdatei_hat_ui_und_fragen(self):
        res = self.client.get('/api/i18n/de/')
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn('ui', data)
        self.assertIn('questions', data)
        self.assertEqual(data['ui']['next'], 'Weiter')

    def test_unbekannte_sprache_404(self):
        self.assertEqual(self.client.get('/api/i18n/zz/').status_code, 404)
        self.assertEqual(self.client.get('/api/i18n/DE1/').status_code, 404)


class RegistryKatalogeTests(TestCase):
    """
    Qualitätstor für ALLE Kataloge der Registry (Verkehrsmedizin + DGUV
    2016/2024): Schema valide, Roundtrip build→validate→evaluate fehlerfrei,
    Einwilligungen vorhanden, Regeln referenzieren nur existierende Fragen
    mit existierenden Antwortwerten, und jeder Katalog ist einreichbar.
    """

    def _allowed_values(self, schema):
        """qid → Menge erlaubter Werte (nur für Fragen mit festem Wertevorrat)."""
        allowed = {}
        for _section, q in iter_questions(schema):
            if q.get('type') == 'yes_no':
                allowed[q['id']] = {'yes', 'no'}
            elif q.get('type') in ('choice', 'multi_choice'):
                allowed[q['id']] = {o['value'] for o in q.get('options', [])}
        return allowed

    def test_alle_kataloge_valide_und_auswertbar(self):
        for slug, entry in CATALOG_REGISTRY.items():
            with self.subTest(katalog=slug):
                schema = entry['catalog']
                self.assertEqual(schema.get('version'), 2)
                self.assertTrue(schema.get('title'))
                self.assertTrue(schema.get('sections'))
                answers = build_valid_answers(schema)
                cleaned, errors = validate_answers(schema, answers)
                self.assertEqual(errors, {}, f'{slug}: {errors}')
                result = evaluate_for_template(cleaned, slug)
                for key in ('findings', 'zusammenfassung', 'disclaimer'):
                    self.assertIn(key, result)

    def test_einwilligung_in_jedem_katalog(self):
        for slug, entry in CATALOG_REGISTRY.items():
            with self.subTest(katalog=slug):
                ids = {q['id'] for _s, q in iter_questions(entry['catalog'])}
                self.assertIn('consent_truth', ids)
                self.assertIn('consent_privacy', ids)

    def test_regeln_referenzieren_nur_existierende_fragen_und_werte(self):
        for slug, entry in CATALOG_REGISTRY.items():
            rules = entry['rules']
            if rules is None:  # Verkehrsmedizin: bespoke-Regelwerk
                continue
            with self.subTest(katalog=slug):
                self.assertGreaterEqual(len(rules), 1, f'{slug}: keine Regeln')
                schema = entry['catalog']
                ids = set()
                for _section, q in iter_questions(schema):
                    ids.add(q['id'])
                    if q.get('followup'):
                        ids.add(q['followup']['id'])
                allowed = self._allowed_values(schema)
                for rule in rules:
                    self.assertIn(rule.get('schwere'), ('kritisch', 'pruefen', 'hinweis'))
                    self.assertTrue(
                        rule.get('konsequenz'),
                        f'{slug}: Regel ohne Verfahrensanweisung: {rule.get("befund")}',
                    )
                    for cond in ('wenn', 'wenn_nicht'):
                        for qid, werte in rule.get(cond, {}).items():
                            self.assertIn(qid, ids, f'{slug}: unbekannte Frage "{qid}"')
                            if qid in allowed:
                                for wert in werte:
                                    self.assertNotIsInstance(
                                        wert, (list, dict),
                                        f'{slug}: Regelwerte müssen Skalare sein ({qid})',
                                    )
                                    self.assertIn(
                                        wert, allowed[qid],
                                        f'{slug}: Regelwert "{wert}" existiert nicht bei "{qid}"',
                                    )

    def test_jeder_katalog_kann_eingereicht_werden(self):
        call_command('load_catalog', verbosity=0)
        for template in QuestionnaireTemplate.objects.filter(is_active=True):
            with self.subTest(katalog=template.slug):
                session = QuestionnaireSession.objects.create(
                    template=template,
                    patient_last_name='Mustermann', patient_first_name='Max',
                    expires_at=timezone.now() + timedelta(days=14),
                )
                answers = build_valid_answers(template.schema_json)
                res = self.client.post(
                    f'/api/submit/{session.token}/', answers,
                    content_type='application/json',
                )
                self.assertEqual(res.status_code, 201, (template.slug, res.json()))


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
