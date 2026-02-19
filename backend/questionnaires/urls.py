from django.urls import path
from .views import (
    QuestionnaireSessionView,
    SubmitQuestionnaireView,
    GeneratePDFView,
    AnswersView,
)

urlpatterns = [
    path('session/<uuid:token>/', QuestionnaireSessionView.as_view(), name='session-detail'),
    path('submit/<uuid:token>/', SubmitQuestionnaireView.as_view(), name='submit-questionnaire'),
    path('pdf/<uuid:token>/', GeneratePDFView.as_view(), name='generate-pdf'),
    path('answers/<uuid:token>/', AnswersView.as_view(), name='answers-data'),
]
