from django.contrib import admin
from .models import QuestionnaireTemplate, QuestionnaireSession, AnswerSet


@admin.register(QuestionnaireTemplate)
class QuestionnaireTemplateAdmin(admin.ModelAdmin):
    list_display = ['slug', 'version', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['slug']


@admin.register(QuestionnaireSession)
class QuestionnaireSessionAdmin(admin.ModelAdmin):
    list_display = ['token', 'template', 'created_at', 'expires_at', 'completed']
    list_filter = ['completed', 'created_at', 'template']
    search_fields = ['token', 'patient_identifier']
    readonly_fields = ['token', 'created_at']


@admin.register(AnswerSet)
class AnswerSetAdmin(admin.ModelAdmin):
    list_display = ['session', 'ess_total', 'ess_band', 'created_at']
    list_filter = ['ess_band', 'created_at']
    search_fields = ['session__token']
    readonly_fields = ['created_at', 'updated_at']
