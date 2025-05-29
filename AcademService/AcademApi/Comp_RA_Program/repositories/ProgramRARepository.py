from AcademApi.Comp_RA_Program.models.ProgramRA import ProgramRA
from django.core.exceptions import ObjectDoesNotExist

class ProgramRARepository:
    # Metodo para obtener todos los resultados de aprendizaje de programa
    @staticmethod
    def get_all_program_ras():
        return ProgramRA.objects.all()

    # Metodo para obtener un resultado de aprendizaje de programa por su id
    @staticmethod
    def get_program_ra_by_id(pro_ra_id):
        try:
            return ProgramRA.objects.get(id=pro_ra_id)
        except ObjectDoesNotExist:
            return None
    
    # Metodo para crear un resultado de aprendizaje de programa
    @staticmethod
    def create_program_ra(**kwargs):
        return ProgramRA.objects.create(**kwargs)

    # Metodo para actualizar un resultado de aprendizaje de programa
    @staticmethod
    def update_program_ra(programRA, **kwargs):
        for attr, value in kwargs.items():
            setattr(programRA, attr, value)
        programRA.save()
        return programRA
    
    # Metodo para eliminar un resultado de aprendizaje de programa
    @staticmethod
    def delete_program_ra(programRA):
        programRA.delete()