from django.urls import path, include
from rest_framework import routers
from AcademApi import views

routers = routers.DefaultRouter()
routers.register(r'subjects', views.SubjectViewSet, basename='subject')

urlpatterns = [
    path('', include(routers.urls)),
]