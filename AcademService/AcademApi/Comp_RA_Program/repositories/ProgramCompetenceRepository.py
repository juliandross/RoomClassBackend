from AcademApi.Comp_RA_Program.models.ProgramCompetence import ProgramCompetence
from django.core.exceptions import ObjectDoesNotExist

class ProgramCompetenceRepository:
    # Metodo para obtener todas las competencias de programa
    @staticmethod
    def get_all_program_competences():
        return ProgramCompetence.objects.all()

    # Metodo para obtener una competencia de programa por su id
    @staticmethod
    def get_program_competence_by_id(pro_comp_id):
        try:
            return ProgramCompetence.objects.get(id=pro_comp_id)
        except ObjectDoesNotExist:
            return None
    
    # Metodo para crear una competencia de programa
    @staticmethod
    def create_program_competence(**kwargs):
        return ProgramCompetence.objects.create(**kwargs)

    # Metodo para actualizar una competencia de programa
    @staticmethod
    def update_program_competence(programCompetence, **kwargs):
        for attr, value in kwargs.items():
            setattr(programCompetence, attr, value)
        programCompetence.save()
        return programCompetence
    
    # Metodo para eliminar una competencia de programa
    @staticmethod
    def delete_program_competence(programCompetence):
        programCompetence.delete()