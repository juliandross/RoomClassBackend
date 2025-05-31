from AcademApi.Comp_RA_Program.repositories.ProgramRARepository import ProgramRARepository

class ProgramRAService:
    @staticmethod
    def list_all_program_ras():
        return ProgramRARepository.get_all_program_ras()
    
    @staticmethod
    def get_program_ra_by_id(pro_ra_id):
        return ProgramRARepository.get_program_ra_by_id(pro_ra_id)
    
    @staticmethod
    def create_program_ra(data):
        return ProgramRARepository.create_program_ra(**data)
    
    @staticmethod
    def update_program_ra(pro_ra_id, data):
        program_ra = ProgramRARepository.get_program_ra_by_id(pro_ra_id)
        if program_ra:
            return ProgramRARepository.update_program_ra(program_ra, **data)
        return None
    
    @staticmethod
    def delete_program_ra(pro_ra_id):
        program_ra = ProgramRARepository.get_program_ra_by_id(pro_ra_id)
        if program_ra:
            ProgramRARepository.delete_program_ra(program_ra)
            return True
        return False