from django.urls import path
from .views import (
    QuestionnaireSessionView,
    SubmitQuestionnaireView,
    AnswersView,
    TranslationView,
    AdminSessionListView,
    AdminSessionDetailView,
    AdminTemplateListView,
    AdminResendEmailView,
    AdminDeleteSessionView,
    AdminUpdateSessionView,
    GdtSessionCreateView,
    GdtResultView,
)

urlpatterns = [
    path('session/<uuid:token>/', QuestionnaireSessionView.as_view(), name='session-detail'),
    path('submit/<uuid:token>/', SubmitQuestionnaireView.as_view(), name='submit-questionnaire'),
    path('answers/<uuid:token>/', AnswersView.as_view(), name='answers-data'),
    path('i18n/', TranslationView.as_view(), name='i18n-list'),
    path('i18n/<slug:lang>/', TranslationView.as_view(), name='i18n-detail'),
    # Admin
    path('admin/sessions/', AdminSessionListView.as_view(), name='admin-sessions'),
    path('admin/templates/', AdminTemplateListView.as_view(), name='admin-templates'),
    path('admin/sessions/<uuid:token>/detail/', AdminSessionDetailView.as_view(), name='admin-detail'),
    path('admin/sessions/<uuid:token>/resend/', AdminResendEmailView.as_view(), name='admin-resend'),
    path('admin/sessions/<uuid:token>/update/', AdminUpdateSessionView.as_view(), name='admin-update'),
    path('admin/sessions/<uuid:token>/delete/', AdminDeleteSessionView.as_view(), name='admin-delete'),
    # GDT-Schnittstelle
    path('gdt/session/', GdtSessionCreateView.as_view(), name='gdt-session-create'),
    path('gdt/result/<uuid:token>/', GdtResultView.as_view(), name='gdt-result'),
]
