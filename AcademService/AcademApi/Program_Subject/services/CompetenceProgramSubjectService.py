from AcademApi.Program_Subject.repositories.CompetenceProgramSubjectRepository import CompetenceProgramSubjectRepository

class CompetenceProgramSubjectService:
    @staticmethod
    def list_all_competence_program_subjects():
        return CompetenceProgramSubjectRepository.get_all_competence_program_subjects()
    
    @staticmethod
    def get_competence_program_subject_by_id(cps_id):
        return CompetenceProgramSubjectRepository.get_competence_program_subject_by_id(cps_id)
    
    @staticmethod
    def create_competence_program_subject(data):
        return CompetenceProgramSubjectRepository.create_competence_program_subject(**data)
    
    @staticmethod
    def update_competence_program_subject(cps_id, data):
        competence_program_subject = CompetenceProgramSubjectRepository.get_competence_program_subject_by_id(cps_id)
        if competence_program_subject:
            return CompetenceProgramSubjectRepository.update_competence_program_subject(competence_program_subject, **data)
        return None
    
    @staticmethod
    def delete_competence_program_subject(cps_id):
        competence_program_subject = CompetenceProgramSubjectRepository.get_competence_program_subject_by_id(cps_id)
        if competence_program_subject:
            CompetenceProgramSubjectRepository.delete_competence_program_subject(competence_program_subject)
            return True
        return False