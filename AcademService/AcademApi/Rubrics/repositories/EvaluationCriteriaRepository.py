from AcademApi.Rubrics.models.EvaluationCriteria import EvaluationCriteria
from django.core.exceptions import ObjectDoesNotExist

class EvaluationCriteriaRepository:
    # Method to get all evaluation criteria
    @staticmethod
    def get_all_criteria():
        return EvaluationCriteria.objects.all()

    # Method to get evaluation criteria by ID
    @staticmethod
    def get_criteria_by_id(criteria_id):
        try:
            return EvaluationCriteria.objects.get(id=criteria_id)
        except ObjectDoesNotExist:
            return None

    # Method to create evaluation criteria
    @staticmethod
    def create_criteria(**kwargs):
        return EvaluationCriteria.objects.create(**kwargs)

    # Method to update evaluation criteria
    @staticmethod
    def update_criteria(criteria, **kwargs):
        for attr, value in kwargs.items():
            setattr(criteria, attr, value)
        criteria.save()
        return criteria

    # Method to delete evaluation criteria
    @staticmethod
    def delete_criteria(criteria):
        criteria.delete()

    # Method to get all evaluation criteria for a rubric
    @staticmethod
    def get_criteria_by_rubric(rubric):
        return EvaluationCriteria.objects.filter(Rubric=rubric)