from AcademApi.Comp_RA_Subject.models.SubjectCompetence import SubjectCompetence
from django.core.exceptions import ObjectDoesNotExist

class SubjectCompetenceRepository:
    # Metodo para obtener todas las competencias de asignatura
    @staticmethod
    def get_all_subject_competences():
        return SubjectCompetence.objects.all()

    # Metodo para obtener una competencia de asignatura por su id
    @staticmethod
    def get_subject_competence_by_id(comp_id):
        try:
            return SubjectCompetence.objects.get(id=comp_id)
        except ObjectDoesNotExist:
            return None
    
    # Metodo para crear una competencia de asignatura
    @staticmethod
    def create_subject_competence(**kwargs):
        return SubjectCompetence.objects.create(**kwargs)

    # Metodo para actualizar una competencia de asignatura
    @staticmethod
    def update_subject_competence(subjectCompetence, **kwargs):
        for attr, value in kwargs.items():
            setattr(subjectCompetence, attr, value)
        subjectCompetence.save()
        return subjectCompetence
    
    # Metodo para eliminar una competencia de asignatura
    @staticmethod
    def delete_subject_competence(subjectCompetence):
        subjectCompetence.delete()
        
    @staticmethod
    def get_subject_competences_by_asginature(asignature_id=None):
        
        return SubjectCompetence.objects.filter(programCompetence=asignature_id).all()