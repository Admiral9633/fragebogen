# -*- coding: utf-8 -*-
"""
Lädt ALLE Fragenkataloge der Registry (questionnaires/catalogs) als aktive
Fragebogen-Templates: Verkehrsmedizin (BASt-Leitlinien) plus die
DGUV-Untersuchungen in alter (Grundsätze 2016) und neuer Fassung
(Empfehlungen 2024).

Idempotent: Bestehende Templates werden aktualisiert, Templates ohne
Registry-Eintrag deaktiviert (bereits angelegte Sessions behalten ihres).
"""
from django.core.management.base import BaseCommand

from questionnaires.catalogs import CATALOG_REGISTRY
from questionnaires.models import QuestionnaireTemplate


class Command(BaseCommand):
    help = "Lädt/aktualisiert alle Fragenkataloge der Registry als aktive Templates"

    def handle(self, *args, **options):
        active_pks = []
        for slug, entry in sorted(CATALOG_REGISTRY.items()):
            catalog = entry["catalog"]
            template, created = QuestionnaireTemplate.objects.update_or_create(
                slug=slug,
                defaults={
                    "version": catalog.get("version", 2),
                    "schema_json": catalog,
                    "is_active": True,
                },
            )
            active_pks.append(template.pk)
            n_questions = sum(len(s["questions"]) for s in catalog["sections"])
            self.stdout.write(
                f"  {'+' if created else '='} {slug}: "
                f"{catalog.get('title', slug)} "
                f"({len(catalog['sections'])} Abschnitte, {n_questions} Fragen)"
            )

        deactivated = (
            QuestionnaireTemplate.objects.exclude(pk__in=active_pks)
            .filter(is_active=True)
            .update(is_active=False)
        )
        self.stdout.write(self.style.SUCCESS(
            f"{len(active_pks)} Kataloge aktiv; {deactivated} Template(s) deaktiviert."
        ))
