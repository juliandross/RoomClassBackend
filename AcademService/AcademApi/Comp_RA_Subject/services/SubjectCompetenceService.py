from AcademApi.Comp_RA_Subject.repositories.SubjectCompetenceRepository import SubjectCompetenceRepository

class SubjectCompetenceService:
    @staticmethod
    def list_all_subject_competences():
        return SubjectCompetenceRepository.get_all_subject_competences()
    
    @staticmethod
    def get_subject_competence_by_id(comp_id):
        return SubjectCompetenceRepository.get_subject_competence_by_id(comp_id)
    
    @staticmethod
    def create_subject_competence(data):
        return SubjectCompetenceRepository.create_subject_competence(**data)
    
    @staticmethod
    def update_subject_competence(comp_id, data):
        subject_competence = SubjectCompetenceRepository.get_subject_competence_by_id(comp_id)
        if subject_competence:
            return SubjectCompetenceRepository.update_subject_competence(subject_competence, **data)
        return None
    
    @staticmethod
    def delete_subject_competence(comp_id):
        subject_competence = SubjectCompetenceRepository.get_subject_competence_by_id(comp_id)
        if subject_competence:
            SubjectCompetenceRepository.delete_subject_competence(subject_competence)
            return True
        return False
    
    @staticmethod
    def get_subject_competences_by_asginature(asignature_id=None):
        # Traer el objeto SubjectTeacherPeriod que tiene la competencia
        return SubjectCompetenceRepository.get_subject_competences_by_asginature(asignature_id)