from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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
    
    # Action to get all Subjects with their associated Competences (signature competences)
    # and their associated RAs (RAs Subject)
    @action(detail=False, methods=['get'], url_path='subjectCompetence/subjectRA')
    def subjects_with_competences_and_ra(self, request):
        subjects = Subject.objects.prefetch_related(
            'subjectteacherperiod_set__subjectcompetence_set__subjectra_set'
        )
    
        data = []
        for subject in subjects:
            competences_data = []
            
            # Accedemos por las relaciones prefetch
            for stp in subject.subjectteacherperiod_set.all():
                for subjectCompetence in stp.subjectcompetence_set.all():
                    ras = subjectCompetence.subjectra_set.all()
                    competences_data.append({
                        'Competence': SubjectCompetenceSerializer(subjectCompetence).data,
                        'SubjectRA': SubjectRASerializer(ras, many=True).data
                    })
            
            data.append({
                'Subject': SubjectSerializer(subject).data,
                'SubjectCompetences': competences_data
            })
        
        return Response(data)

    
    # Action to get a Subject with their associated Competences (signature competences)
    # and their associated RAs (RAs Subject)
    @action(detail=True, methods=['get'], url_path='subjectCompetence/subjectRA')
    def subject_with_competences_and_ra_by_id(self, request, pk=None):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({'error': 'Asignatura no encontrada.'}, status=404)
        
        # Buscar todas las competencias de asignatura asociadas directamente por relación
        subject_competences = SubjectCompetence.objects.filter(subjectTeacherPeriod__subject=subject)
        
        # Para cada competencia, buscar los RA asociados
        data = []
        for subjectCompetence in subject_competences:
            ras = SubjectRA.objects.filter(subjectCompetence=subjectCompetence)
            data.append({
                'Competence': SubjectCompetenceSerializer(subjectCompetence).data,
                'SubjectRA': SubjectRASerializer(ras, many=True).data
            })
        
        return Response({
            'subject': SubjectSerializer(subject).data,
            'SubjectCompetences': data
        })

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
    
    # Action to get all Program Competences with their associated RAs
    @action(detail=False, methods=['get'], url_path='RA_asociated')
    def program_competence_with_ra_asociated(self, request):
        competences = ProgramCompetence.objects.all()
        data = []
        for competence in competences:
            ra_count = ProgramRA.objects.filter(programCompetence = competence)
            data.append({
               'competenceProgram': ProgramCompetenceSerializer(competence).data,
               'RA_Program': ProgramRASerializer(ra_count, many=True).data
            })
        return Response(data)
    
    # Action to get a program competence with their associated RAs by ID
    @action(detail=True, methods=['get'], url_path='RA_asociated')
    def program_competence_with_ra_asociated_by_id(self, request, pk=None):
        try:
            competence = ProgramCompetence.objects.get(pk=pk)
            ra_count = ProgramRA.objects.filter(programCompetence=competence)
            data = {
                'competenceProgram': ProgramCompetenceSerializer(competence).data,
                'RA_Program': ProgramRASerializer(ra_count, many=True).data
            }
            return Response(data)
        except ProgramCompetence.DoesNotExist:
            return Response({'error': 'Competencia de programa no encontrada.'}, status=404)
        
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