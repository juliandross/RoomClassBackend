from AcademApi.Rubrics.repositories.LevelRepository import LevelRepository

class LevelService:
    @staticmethod
    def list_all_levels():
        return LevelRepository.get_all_levels()
    
    @staticmethod
    def get_level_by_id(level_id):
        return LevelRepository.get_level_by_id(level_id)
    
    @staticmethod
    def create_level(data):
        return LevelRepository.create_level(**data)
    
    @staticmethod
    def update_level(level_id, data):
        level = LevelRepository.get_level_by_id(level_id)
        if level:
            return LevelRepository.update_level(level, **data)
        return None
    
    @staticmethod
    def delete_level(level_id):
        level = LevelRepository.get_level_by_id(level_id)
        if level:
            LevelRepository.delete_level(level)
            return True
        return False
    
    @staticmethod
    def get_levels_by_criteria(criteria):
        return LevelRepository.get_levels_by_criteria(criteria)