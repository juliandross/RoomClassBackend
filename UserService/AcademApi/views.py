from rest_framework import viewsets

from AcademApi.Comp_RA_Subject.serializer.SubjectCompetenceSerializer import SubjectCompetenceSerializer
from AcademApi.Comp_RA_Subject.models.SubjectCompetence import SubjectCompetence

from AcademApi.Comp_RA_Subject.serializer.SubjectRASerializer import SubjectRASerializer
from AcademApi.Comp_RA_Subject.models.SubjectRA import SubjectRA


# Create your views here.

# Class to handle the SubjectCompetence API
class SubjectCompetenceViewSet(viewsets.ModelViewSet):
    queryset = SubjectCompetence.objects.all()
    serializer_class = SubjectCompetenceSerializer

class SubjectRAViewSet(viewsets.ModelViewSet):
    queryset = SubjectRA.objects.all()
    serializer_class = SubjectRASerializer