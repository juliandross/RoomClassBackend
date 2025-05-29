from AcademApi.Subject.repositories.TeacherRepository import TeacherRepository

class TeacherService:
    @staticmethod
    def list_all_teachers():
        return TeacherRepository.get_all_teachers()
    
    @staticmethod
    def get_teacher_by_id(tea_id):
        return TeacherRepository.get_teacher_by_id(tea_id)
    
    @staticmethod
    def create_teacher(data):
        return TeacherRepository.create_teacher(**data)
    
    @staticmethod
    def update_teacher(tea_id, data):
        teacher = TeacherRepository.get_teacher_by_id(tea_id)
        if teacher:
            return TeacherRepository.update_teacher(teacher, **data)
        return None
    
    @staticmethod
    def delete_teacher(tea_id):
        teacher = TeacherRepository.get_teacher_by_id(tea_id)
        if teacher:
            TeacherRepository.delete_teacher(teacher)
            return True
        return False