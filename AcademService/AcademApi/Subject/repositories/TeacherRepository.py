from AcademApi.Subject.models.Teacher import Teacher
from django.core.exceptions import ObjectDoesNotExist

class TeacherRepository:
    # Metodo para obtener todos los profesores
    @staticmethod
    def get_all_teachers():
        return Teacher.objects.all()
    
    # Metodo para obtener un profesor por su id
    @staticmethod
    def get_teacher_by_id(tea_id):
        try:
            return Teacher.objects.get(id=tea_id)
        except ObjectDoesNotExist:
            return None
    
    # Metodo para crear un profesor
    @staticmethod
    def create_teacher(**kwargs):
        return Teacher.objects.create(**kwargs)

    # Metodo para actualizar un profesor
    @staticmethod
    def update_teacher(teacher, **kwargs):
        for attr, value in kwargs.items():
            setattr(teacher, attr, value)
        teacher.save()
        return teacher
    
    # Metodo para eliminar un profesor
    @staticmethod
    def delete_teacher(teacher):
        teacher.delete()
        
    @staticmethod
    def create_teacher_by_coordinator(**kwargs):
        password = kwargs.pop('password', None)
        teacher = Teacher.objects.create(**kwargs)
        if password:
            teacher.set_password(password)
        teacher.save()
        return teacher
    