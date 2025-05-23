from AcademApi.Comp_RA_Subject.models import SubjectRA
from django.core.exceptions import ObjectDoesNotExist

class SubjectRARepository:
    # Metodo para obtener todas las RA de asignatura
    @staticmethod
    def get_all_subject_ra():
        return SubjectRA.objects.all()
    
    # Metodo para obtener una RA de asignatura por su id
    @staticmethod
    def get_subject_ra_by_id(subjectRA_id):
        try:
            return SubjectRA.objects.get(id=subjectRA_id)
        except ObjectDoesNotExist:
            return None
    
    # Metodo para crear una RA de asignatura
    @staticmethod
    def create_subject_ra(**kwargs):
        return SubjectRA.objects.create(**kwargs)
    
    # Metodo para actualizar una RA de asignatura
    @staticmethod
    def update_subject_ra(subjectRA, **kwargs):
        for attr, value in kwargs.items():
            setattr(subjectRA, attr, value)
        subjectRA.save()
        return subjectRA
    
    # Metodo para eliminar una RA de asignatura
    @staticmethod
    def delete_subject_ra(subjectRA):
        subjectRA.delete()