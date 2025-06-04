from django.urls import path, include
from rest_framework import routers
from AcademApi import views
from AcademApi.Subject.controllers.SubjectTeacherPeriodController import SubjectAssingController
from AcademApi.Subject.controllers.TeacherController import TeacherController
from AcademApi.Subject.controllers.SubjectController import SubjectController

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
    # Subject assign related URLs
    path('subjectReport/<int:subject_id>/', SubjectAssingController.as_view({'get': 'get_subject_report_by_id'}), name='subject-report'),
    path('subjectReport/', SubjectAssingController.as_view({'get': 'list_subject_report'}), name='subject-reports'),
    # Subject related URLs
    path('listAvailableSubjects/', SubjectController.as_view({'get': 'list_available_subjects'}), name='available-subjects'),
    path('unactivateSubject/<int:subject_id>/', SubjectController.as_view({'patch': 'unactivate_subject'}), name='unactivate-subject'),
    # Teacher related URLs
    path('teacherCreateByCoordinator/', TeacherController.as_view({'post':'create_teacher_by_coordinator'}), name='teacher-create-by-coordinator'),
    path('avaliableTeachers/', TeacherController.as_view({'get': 'list_avaliable_teachers'}), name='avaliable-teachers'),
    path('unactivateTeacher/<int:tea_id>/', TeacherController.as_view({'patch': 'unactivate_teacher'}), name='unactivate-teacher'),

    
]