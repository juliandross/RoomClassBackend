from AcademApi.Rubrics.Levels.models.Level import Level
from django.core.exceptions import ObjectDoesNotExist

class LevelRepository:
    # Method to get all levels
    @staticmethod
    def get_all_levels():
        return Level.objects.all()

    # Method to get a level by its ID
    @staticmethod
    def get_level_by_id(level_id):
        try:
            return Level.objects.get(id=level_id)
        except ObjectDoesNotExist:
            return None

    # Method to create a level
    @staticmethod
    def create_level(**kwargs):
        return Level.objects.create(**kwargs)

    # Method to update a level
    @staticmethod
    def update_level(level, **kwargs):
        for attr, value in kwargs.items():
            setattr(level, attr, value)
        level.save()
        return level

    # Method to delete a level
    @staticmethod
    def delete_level(level):
        level.delete()

    # Method to get all levels for a evaluation criteria
    @staticmethod
    def get_levels_by_criteria(criteria):
        return Level.objects.filter(EvaluationCriteria=criteria)

