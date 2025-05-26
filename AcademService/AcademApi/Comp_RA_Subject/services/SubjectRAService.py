from AcademApi.Comp_RA_Subject.repositories.SubjectRARepository import SubjectRARepository

class SubjectRAService:
    @staticmethod
    def list_all_subject_ra():
        return SubjectRARepository.get_all_subject_ra()
    
    @staticmethod
    def get_subject_ra_by_id(subjectRA_id):
        return SubjectRARepository.get_subject_ra_by_id(subjectRA_id)
    
    @staticmethod
    def create_subject_ra(data):
        return SubjectRARepository.create_subject_ra(**data)
    
    @staticmethod
    def update_subject_ra(subjectRA_id, data):
        subject_ra = SubjectRARepository.get_subject_ra_by_id(subjectRA_id)
        if subject_ra:
            return SubjectRARepository.update_subject_ra(subject_ra, **data)
        return None
    
    @staticmethod
    def delete_subject_ra(subjectRA_id):
        subject_ra = SubjectRARepository.get_subject_ra_by_id(subjectRA_id)
        if subject_ra:
            SubjectRARepository.delete_subject_ra(subject_ra)
            return True
        return False