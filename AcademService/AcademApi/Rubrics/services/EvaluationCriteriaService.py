from AcademApi.Rubrics.repositories.EvaluationCriteriaRepository import EvaluationCriteriaRepository

class EvaluationCriteriaService:
    @staticmethod
    def list_all_criteria():
        return EvaluationCriteriaRepository.get_all_criteria()
    
    @staticmethod
    def get_criteria_by_id(criteria_id):
        return EvaluationCriteriaRepository.get_criteria_by_id(criteria_id)
    
    @staticmethod
    def create_criteria(data):
        return EvaluationCriteriaRepository.create_criteria(**data)
    
    @staticmethod
    def update_criteria(criteria_id, data):
        criteria = EvaluationCriteriaRepository.get_criteria_by_id(criteria_id)
        if criteria:
            return EvaluationCriteriaRepository.update_criteria(criteria, **data)
        return None
    
    @staticmethod
    def delete_criteria(criteria_id):
        criteria = EvaluationCriteriaRepository.get_criteria_by_id(criteria_id)
        if criteria:
            EvaluationCriteriaRepository.delete_criteria(criteria)
            return True
        return False
    
    @staticmethod
    def get_criteria_by_rubric(rubric):
        return EvaluationCriteriaRepository.get_criteria_by_rubric(rubric)