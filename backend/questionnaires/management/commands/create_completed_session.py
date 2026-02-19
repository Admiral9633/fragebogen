"""
Erstellt eine vollständig ausgefüllte Test-Session
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from questionnaires.models import QuestionnaireTemplate, QuestionnaireSession, AnswerSet


class Command(BaseCommand):
    help = 'Erstellt eine ausgefüllte Test-Session'

    def handle(self, *args, **kwargs):
        # Hole oder erstelle Template
        template, _ = QuestionnaireTemplate.objects.get_or_create(
            slug='verkehrsmedizin-v1',
            defaults={
                'version': 1,
                'schema_json': {
                    'sections': ['ess'],
                    'title': 'Verkehrsmedizinischer Fragebogen'
                },
                'is_active': True
            }
        )

        # Erstelle Session
        session = QuestionnaireSession.objects.create(
            template=template,
            expires_at=timezone.now() + timedelta(days=7),
            patient_identifier='TEST-COMPLETED',
            completed=True,
            completed_at=timezone.now()
        )

        # Erstelle Antworten
        test_answers = {
            'ess_1': 2,
            'ess_2': 1,
            'ess_3': 0,
            'ess_4': 3,
            'ess_5': 2,
            'ess_6': 0,
            'ess_7': 1,
            'ess_8': 2,
            'ess_total': 11,
            'ess_band': 'erhöht',
            'consent_complete': True,
            'consent_privacy': True
        }

        AnswerSet.objects.create(
            session=session,
            answers_json=test_answers,
            ess_total=11,
            ess_band='erhöht'
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Ausgefüllte Test-Session erstellt!\n'
                f'  Token: {session.token}\n'
                f'  Fragebogen-URL: http://localhost:3000/q/{session.token}\n'
                f'  PDF-URL: http://localhost:8000/api/pdf/{session.token}/\n'
            )
        )
