from rest_framework import viewsets

from AcademApi.Subject.models.Subject import Subject
from AcademApi.Subject.serializer.SubjectSerializer import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer