from AcademApi.Rubrics.models.Rubric import Rubric
from django.core.exceptions import ObjectDoesNotExist

class RubricRepository:
    # Metodo para obtener todas las rubricas
    @staticmethod
    def get_all_rubrics():
        return Rubric.objects.all()

    # Metodo para obtener una rubrica por su id
    @staticmethod
    def get_rubric_by_id(rubric_id):
        try:
            return Rubric.objects.get(id=rubric_id)
        except ObjectDoesNotExist:
            return None

    # Metodo para crear una rubrica
    @staticmethod
    def create_rubric(**kwargs):
        return Rubric.objects.create(**kwargs)

    # Metodo para actualizar una rubrica
    @staticmethod
    def update_rubric(rubric, **kwargs):
        for attr, value in kwargs.items():
            setattr(rubric, attr, value)
        rubric.save()
        return rubric

    # Metodo para eliminar una rubrica
    @staticmethod
    def delete_rubric(rubric):
        rubric.delete()

    # Metodo para obtener todas las rubricas de una asignatura
    @staticmethod
    def get_rubrics_by_subject(subjectRA):
        return Rubric.objects.filter(SubjectRA=subjectRA)