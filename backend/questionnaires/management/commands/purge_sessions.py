"""
Löscht abgelaufene Fragebogen-Sessions samt Antworten (DSGVO-Retention).

Gelöscht werden Sessions, deren Zugangslink seit mehr als --days Tagen
abgelaufen ist (Default: 30). Die Antworten (AnswerSet) hängen per
on_delete=CASCADE an der Session und werden mitgelöscht.

Empfohlener Einsatz: täglicher Cron/Scheduled Task, z.B.
  docker-compose exec backend python manage.py purge_sessions
"""
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from questionnaires.models import QuestionnaireSession


class Command(BaseCommand):
    help = 'Löscht Sessions, deren Link seit mehr als --days Tagen abgelaufen ist'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=30,
            help='Karenzzeit in Tagen nach Ablauf des Links (Default: 30)',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Nur anzeigen, was gelöscht würde',
        )

    def handle(self, *args, **options):
        cutoff = timezone.now() - timedelta(days=options['days'])
        qs = QuestionnaireSession.objects.filter(expires_at__lt=cutoff)
        count = qs.count()

        if options['dry_run']:
            self.stdout.write(f'{count} Session(s) würden gelöscht (expires_at < {cutoff:%d.%m.%Y}).')
            return

        qs.delete()
        self.stdout.write(self.style.SUCCESS(
            f'{count} abgelaufene Session(s) gelöscht (expires_at < {cutoff:%d.%m.%Y}).'
        ))
