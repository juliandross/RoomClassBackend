from AcademApi.Comp_RA_Program.repositories.ProgramCompetenceRepository import ProgramCompetenceRepository

class ProgramCompetenceService:
    @staticmethod
    def list_all_program_competences():
        return ProgramCompetenceRepository.get_all_program_competences()
    
    @staticmethod
    def get_program_competence_by_id(pro_comp_id):
        return ProgramCompetenceRepository.get_program_competence_by_id(pro_comp_id)
    
    @staticmethod
    def create_program_competence(data):
        return ProgramCompetenceRepository.create_program_competence(**data)
    
    @staticmethod
    def update_program_competence(pro_comp_id, data):
        program_competence = ProgramCompetenceRepository.get_program_competence_by_id(pro_comp_id)
        if program_competence:
            return ProgramCompetenceRepository.update_program_competence(program_competence, **data)
        return None
    
    @staticmethod
    def delete_program_competence(pro_comp_id):
        program_competence = ProgramCompetenceRepository.get_program_competence_by_id(pro_comp_id)
        if program_competence:
            ProgramCompetenceRepository.delete_program_competence(program_competence)
            return True
        return False