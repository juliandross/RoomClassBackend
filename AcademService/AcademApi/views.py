from django.shortcuts import render
from rest_framework import viewsets

from AcademApi.Comp_RA_Subject.serializer.SubjectCompetenceSerializer import SubjectCompetenceSerializer
from AcademApi.Comp_RA_Subject.models.SubjectCompetence import SubjectCompetence

from AcademApi.Comp_RA_Subject.serializer.SubjectRASerializer import SubjectRASerializer
from AcademApi.Comp_RA_Subject.models.SubjectRA import SubjectRA


from AcademApi.Subject.models.Subject import Subject
from AcademApi.Subject.serializer.SubjectSerializer import SubjectSerializer

from AcademApi.Comp_RA_Program.models.ProgramCompetence import ProgramCompetence
from AcademApi.Comp_RA_Program.models.ProgramRA import ProgramRA
from AcademApi.Comp_RA_Program.serializer.ProgramCompetenceSerializer import ProgramCompetenceSerializer
from AcademApi.Comp_RA_Program.serializer.ProgramRASerializer import ProgramRASerializer

from AcademApi.Subject.models.Period import Period
from AcademApi.Subject.models.Teacher import Teacher
from AcademApi.Subject.models.SubjectTeacherPeriod import SubjectTeacherPeriod
from AcademApi.Subject.serializer.PeriodSerializer import PeriodSerializer
from AcademApi.Subject.serializer.TeacherSerializer import TeacherSerializer
from AcademApi.Subject.serializer.SubjectTeacherPeriodSerializer import SubjectTeacherPeriodSerializer

from AcademApi.Program_Subject.models.CompetenceProgramSubject import CompetenceProgramSubject
from AcademApi.Program_Subject.serializer.CompetenceProgramSubjectSerializer import CompetenceProgramSubjectSerializer

from AcademApi.Rubrics.models.Level import Level
from AcademApi.Rubrics.serializer.LevelSerializer import LevelSerializer
from AcademApi.Rubrics.models.EvaluationCriteria import EvaluationCriteria
from AcademApi.Rubrics.serializer.EvaluationCriteriaSerializer import EvaluationCriteriaSerializer
from AcademApi.Rubrics.models.Rubric import Rubric
from AcademApi.Rubrics.serializer.RubricSerializer import RubricSerializer

# Class to handle the directory Comp_RA_Subject
class SubjectCompetenceViewSet(viewsets.ModelViewSet):
    queryset = SubjectCompetence.objects.all()
    serializer_class = SubjectCompetenceSerializer

class SubjectRAViewSet(viewsets.ModelViewSet):
    queryset = SubjectRA.objects.all()
    serializer_class = SubjectRASerializer

# Class to handle the direcory Subject 
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectTeacherPeriodViewSet(viewsets.ModelViewSet):
    queryset = SubjectTeacherPeriod.objects.all()
    serializer_class = SubjectTeacherPeriodSerializer

# Class to handle the directory Comp_RA_Program
class ProgramCompetenceViewSet(viewsets.ModelViewSet):
    queryset = ProgramCompetence.objects.all()  
    serializer_class = ProgramCompetenceSerializer
    
class ProgramRAViewSet(viewsets.ModelViewSet):
    queryset = ProgramRA.objects.all()
    serializer_class = ProgramRASerializer

# Class to handle the directory Program_Subject
class CompetenceProgramSubjectViewSet(viewsets.ModelViewSet):
    queryset = CompetenceProgramSubject.objects.all()
    serializer_class = CompetenceProgramSubjectSerializer

# Class to handle the directory Rubrics
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class EvaluationCriteriaViewSet(viewsets.ModelViewSet):
    queryset = EvaluationCriteria.objects.all()
    serializer_class = EvaluationCriteriaSerializer

# Class to handle the directory Rubric
class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer