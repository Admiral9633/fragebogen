"""
Lädt den Leitlinien-Fragenkatalog (catalog.py) als aktives Fragebogen-Template.

Idempotent: Bei erneutem Aufruf wird das bestehende Template aktualisiert.
Alle anderen Templates werden deaktiviert, damit neue Sessions immer den
aktuellen Katalog verwenden. Bereits angelegte Sessions behalten ihr Template.
"""
from django.core.management.base import BaseCommand

from questionnaires.catalog import CATALOG
from questionnaires.models import QuestionnaireTemplate

SLUG = "verkehrsmedizin-leitlinien"


class Command(BaseCommand):
    help = "Lädt/aktualisiert den Fragenkatalog nach Begutachtungsleitlinien als aktives Template"

    def handle(self, *args, **options):
        template, created = QuestionnaireTemplate.objects.update_or_create(
            slug=SLUG,
            defaults={
                "version": CATALOG["version"],
                "schema_json": CATALOG,
                "is_active": True,
            },
        )
        deactivated = (
            QuestionnaireTemplate.objects.exclude(pk=template.pk)
            .filter(is_active=True)
            .update(is_active=False)
        )

        n_sections = len(CATALOG["sections"])
        n_questions = sum(len(s["questions"]) for s in CATALOG["sections"])
        self.stdout.write(self.style.SUCCESS(
            f"Template '{SLUG}' {'angelegt' if created else 'aktualisiert'} "
            f"({n_sections} Abschnitte, {n_questions} Fragen); "
            f"{deactivated} andere(s) Template(s) deaktiviert."
        ))
