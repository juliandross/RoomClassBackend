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
from AcademApi.permissions import IsCoordinator

# Class to handle the directory Comp_RA_Subject
class SubjectCompetenceViewSet(viewsets.ModelViewSet):
    queryset = SubjectCompetence.objects.all()
    serializer_class = SubjectCompetenceSerializer
    
    # Action to get a Subject Competence with their associated RAs
    @action(detail=True, methods=['get'], url_path='RA')
    def subject_competence_with_ra_asociated(self, request, pk=None):
        try:
            subject_competence = SubjectCompetence.objects.get(pk=pk)
        except SubjectCompetence.DoesNotExist:
            return Response({'error': 'Competencia de asignatura no encontrada.'}, status=404)
        
        ras = SubjectRA.objects.filter(subjectCompetence=subject_competence)
        
        data = {
            'SubjectCompetence': SubjectCompetenceSerializer(subject_competence).data,
            'SubjectRA': SubjectRASerializer(ras, many=True).data
        }
        
        return Response(data)

class SubjectRAViewSet(viewsets.ModelViewSet):
    queryset = SubjectRA.objects.all()
    serializer_class = SubjectRASerializer
    
    # Action to get a Subject RA with their associated Rubric
    @action(detail=True, methods=['get'], url_path='Rubric')
    def subject_ra_with_rubric_asociated(self, request, pk=None):
        try:
            subject_ra = SubjectRA.objects.get(pk=pk)
        except SubjectRA.DoesNotExist:
            return Response({'error': 'RA de asignatura no encontrado.'}, status=404)
        
        try:
            rubric = Rubric.objects.get(SubjectRA=subject_ra)
            rubric_data = RubricSerializer(rubric).data
        except Rubric.DoesNotExist:
            return Response({'error': 'No hay ninguna rúbrica asociada al resultado de aprendizaje de asignatura.'}, status=404)
        
        data = {
            'SubjectRA': SubjectRASerializer(subject_ra).data,
            'Rubric': rubric_data
        }
        return Response(data)
    

# Class to handle the direcory Subject 
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsCoordinator]
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
        
    # Action to get a Subject with their associated program competences
    @action(detail=True, methods=['get'], url_path='programCompetence')
    def subject_with_program_competences(self, request, pk=None):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({'error': 'Asignatura no encontrada.'}, status=404)
        
        # Obtener todos los enlaces intermedios
        competence_links = CompetenceProgramSubject.objects.filter(subject=subject).select_related('programCompetence')
        
        # Serializar solo las competencias (no los enlaces)
        program_competences_data = [
            ProgramCompetenceSerializer(link.programCompetence).data
            for link in competence_links
        ]
        
        return Response({
            'subject': SubjectSerializer(subject).data,
            'programCompetences': program_competences_data
        })

        

class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    # Action to get a Teacher with their associated Subjects
    @action(detail=True, methods=['get'], url_path='Subject_asociated')
    def teacher_byId_with_subject_asociated(self, request, pk=None):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response({'error': 'Docente no encontrado.'}, status=404)
        
        subjects = Subject.objects.filter(subject_teacher_periods__teacher=teacher).distinct()
        
        subjects_data = []
        for subject in subjects:
            subjects_data.append({
                'Subject': SubjectSerializer(subject).data,
            })
        
        result = {
            'Teacher': TeacherSerializer(teacher).data,
            'Subjects': subjects_data
        }
        return Response(result)
    # Action to get a Teacher with their associated SubjectTeacherPeriod
    @action(detail=True, methods=['get'], url_path='SubjectTeacherPeriod_asociated')
    def teacher_byId_with_subject_asociated(self, request, pk=None):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response({'error': 'Docente no encontrado.'}, status=404)
        
        # Obtener todos los SubjectTeacherPeriod asociados a este docente
        subject_teacher_periods = SubjectTeacherPeriod.objects.filter(teacher=teacher).distinct()
        
        stp_data = []
        for stp in subject_teacher_periods:
            stp_data.append({
                'SubjectTeacherPeriod': SubjectTeacherPeriodSerializer(stp).data,
            })
        
        result = {
            'Teacher': TeacherSerializer(teacher).data,
            'SubjectTeacherPeriods': stp_data
        }
        return Response(result)
            
class SubjectTeacherPeriodViewSet(viewsets.ModelViewSet):
    queryset = SubjectTeacherPeriod.objects.all()
    serializer_class = SubjectTeacherPeriodSerializer
    
    # Action to get a "SubjectTeacherPeriod" with their associated Subjects competences
    @action(detail=True, methods=['get'], url_path='SubjectCompetence_asociated')
    def subject_teacher_period_with_competence_asociated(self, request, pk=None):
        try:
            subject_teacher_period = SubjectTeacherPeriod.objects.get(pk=pk)
        except SubjectTeacherPeriod.DoesNotExist:
            return Response({'error': 'Instancia de "sujec_teacher_period" no encontrada.'}, status=404)
        
        competences = SubjectCompetence.objects.filter(subjectTeacherPeriod=subject_teacher_period)
        
        competences_data = []
        for competence in competences:
            competences_data.append({
                'SubjectCompetence': SubjectCompetenceSerializer(competence).data,
            })
        
        result = {
            'SubjectTeacherPeriod': SubjectTeacherPeriodSerializer(subject_teacher_period).data,
            'SubjectCompetences': competences_data
        }
        return Response(result)
    
    # Action to get all "SubjectTeacherPeriod" with their associated Subjects competences + RAs
    @action(detail=True, methods=['get'], url_path='SubjectCompetence/RA')
    def subject_teacher_period_with_competence_ra_asociated(self, request, pk=None):
        try:
            subject_teacher_period = SubjectTeacherPeriod.objects.get(pk=pk)
        except SubjectTeacherPeriod.DoesNotExist:
            return Response({'error': 'Instancia de "subject_teacher_period" no encontrada.'}, status=404)
        
        competences = SubjectCompetence.objects.filter(subjectTeacherPeriod=subject_teacher_period)
        
        competences_data = []
        for competence in competences:
            ras = SubjectRA.objects.filter(subjectCompetence=competence)
            competences_data.append({
                'SubjectCompetence': SubjectCompetenceSerializer(competence).data,
                'SubjectRA': SubjectRASerializer(ras, many=True).data
            })
        
        result = {
            'SubjectTeacherPeriod': SubjectTeacherPeriodSerializer(subject_teacher_period).data,
            'SubjectCompetences': competences_data
        }
        return Response(result)
    

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