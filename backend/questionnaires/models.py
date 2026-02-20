from django.db import models
import uuid
from datetime import timedelta
from django.utils import timezone


class QuestionnaireTemplate(models.Model):
    """
    Template für Fragebögen mit versioniertem JSON-Schema
    """
    slug = models.SlugField(unique=True, max_length=100)
    version = models.IntegerField(default=1)
    schema_json = models.JSONField(
        help_text="JSON Schema mit Fragen und Struktur"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-version']
        unique_together = ['slug', 'version']
    
    def __str__(self):
        return f"{self.slug} (v{self.version})"


class QuestionnaireSession(models.Model):
    """
    Individuelle Fragebogen-Sitzung mit Token-basiertem Zugang
    """
    token = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        editable=False,
        db_index=True
    )
    template = models.ForeignKey(
        QuestionnaireTemplate, 
        on_delete=models.CASCADE,
        related_name='sessions'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Patientendaten
    patient_last_name = models.CharField(max_length=100, blank=True)
    patient_first_name = models.CharField(max_length=100, blank=True)
    patient_email = models.EmailField(blank=True)
    patient_birth_date = models.DateField(null=True, blank=True)
    invitation_sent_at = models.DateTimeField(null=True, blank=True)

    # Legacy
    patient_identifier = models.CharField(
        max_length=100,
        blank=True,
        help_text="Anonymisierte Patienten-ID"
    )

    # GDT-Schnittstelle
    gdt_patient_id = models.CharField(
        max_length=100,
        blank=True,
        help_text="GDT Feld 3000 – interne SAMAS Patienten-ID"
    )
    gdt_request_id = models.CharField(
        max_length=100,
        blank=True,
        help_text="GDT Feld 8315 – Anforderungskennung für Rückantwort"
    )
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Session {self.token} - {self.template.slug}"
    
    def save(self, *args, **kwargs):
        if not self.expires_at:
            # Standard: 7 Tage Gültigkeit
            self.expires_at = timezone.now() + timedelta(days=7)
        super().save(*args, **kwargs)
    
    def is_expired(self):
        return timezone.now() > self.expires_at
    
    def is_valid(self):
        return not self.is_expired() and not self.completed


class AnswerSet(models.Model):
    """
    Gespeicherte Antworten zu einer Fragebogen-Sitzung
    """
    session = models.OneToOneField(
        QuestionnaireSession, 
        on_delete=models.CASCADE,
        related_name='answers'
    )
    answers_json = models.JSONField(
        help_text="Alle Antworten als JSON"
    )
    
    # ESS spezifische Felder
    ess_total = models.IntegerField(
        null=True, 
        blank=True,
        help_text="Epworth Sleepiness Scale Gesamtscore (0-24)"
    )
    ess_band = models.CharField(
        max_length=20, 
        null=True, 
        blank=True,
        choices=[
            ('normal', 'Normal (0-9)'),
            ('erhöht', 'Erhöht (10-15)'),
            ('ausgeprägt', 'Ausgeprägt (≥16)'),
        ]
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Answer Set'
        verbose_name_plural = 'Answer Sets'
    
    def __str__(self):
        return f"Answers for {self.session.token}"
