from django.urls import path, include
from rest_framework import routers
from AcademApi import views
from AcademApi.Subject.controllers.SubjectTeacherPeriodController import SubjectAssingController

routers = routers.DefaultRouter()
routers.register(r'subjectCompetence', views.SubjectCompetenceViewSet, basename='subjectCompetence')
routers.register(r'subjectRA', views.SubjectRAViewSet, basename='subjectRA')
routers.register(r'subject', views.SubjectViewSet, basename='subject')
routers.register(r'programCompetence', views.ProgramCompetenceViewSet, basename='programCompetence')
routers.register(r'programRA', views.ProgramRAViewSet, basename='programRA')
routers.register(r'period', views.PeriodViewSet, basename='period')
routers.register(r'teacher', views.TeacherViewSet, basename='teacher')
routers.register(r'subjectTeacherPeriod', views.SubjectTeacherPeriodViewSet, basename='subjectTeacherPeriod')
routers.register(r'competenceProgramSubject', views.CompetenceProgramSubjectViewSet, basename='competenceProgramSubject')
routers.register(r'level', views.LevelViewSet, basename='level')
routers.register(r'evaluationCriteria', views.EvaluationCriteriaViewSet, basename='evaluationCriteria')
routers.register(r'rubric', views.RubricViewSet, basename='rubric')
urlpatterns = [
    path('', include(routers.urls)),
    # Subject related URLs
    path('subjectReport/<int:subject_id>/', SubjectAssingController.as_view({'get': 'get_subject_report'}), name='subject-report'),
]