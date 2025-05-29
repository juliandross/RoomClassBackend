from django.urls import path, include
from rest_framework import routers
from AcademApi import views

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

urlpatterns = [
    path('', include(routers.urls))
]