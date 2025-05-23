from django.urls import path, include
from rest_framework import routers
from AcademApi import views

routers = routers.DefaultRouter()
routers.register(r'subjectCompetence', views.SubjectCompetenceViewSet, basename='subjectCompetence')
routers.register(r'subjectRA', views.SubjectRAViewSet, basename='subjectRA')

urlpatterns = [
    path('', include(routers.urls))
]