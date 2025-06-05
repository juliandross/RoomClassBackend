from AcademApi.Rubrics.repositories.RubricRepository import RubricRepository

class RubricService:
    @staticmethod
    def list_all_rubrics():
        return RubricRepository.get_all_rubrics()
    
    @staticmethod
    def get_rubric_by_id(rubric_id):
        return RubricRepository.get_rubric_by_id(rubric_id)
    
    @staticmethod
    def create_rubric(data):
        return RubricRepository.create_rubric(**data)
    
    @staticmethod
    def update_rubric(rubric_id, data):
        rubric = RubricRepository.get_rubric_by_id(rubric_id)
        if rubric:
            return RubricRepository.update_rubric(rubric, **data)
        return None
    
    @staticmethod
    def delete_rubric(rubric_id):
        rubric = RubricRepository.get_rubric_by_id(rubric_id)
        if rubric:
            RubricRepository.delete_rubric(rubric)
            return True
        return False
    
    @staticmethod
    def get_rubrics_by_subject(subjectRA):
        return RubricRepository.get_rubrics_by_subject(subjectRA)