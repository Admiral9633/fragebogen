"""
Management Command zum Erstellen von Sample-Daten für Tests
"""
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from questionnaires.models import QuestionnaireTemplate, QuestionnaireSession


class Command(BaseCommand):
    help = 'Erstellt Test-Daten für die Entwicklung'

    def handle(self, *args, **kwargs):
        self.stdout.write('Erstelle Test-Daten...')

        # Aktuellen Leitlinien-Katalog laden (idempotent)
        call_command('load_catalog')
        template = (
            QuestionnaireTemplate.objects.filter(is_active=True)
            .order_by('-version')
            .first()
        )

        # Erstelle Test-Sessions
        for i in range(3):
            session = QuestionnaireSession.objects.create(
                template=template,
                expires_at=timezone.now() + timedelta(days=7),
                patient_identifier=f'TEST-{i+1:03d}'
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'✓ Session erstellt: {session.token}\n'
                    f'  URL: http://localhost:3000/q/{session.token}'
                )
            )

        self.stdout.write(self.style.SUCCESS('\n✓ Test-Daten erfolgreich erstellt!'))
