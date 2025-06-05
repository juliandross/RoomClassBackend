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
    
    @staticmethod
    def get_teacher_by_email(email):
        """
        Get a teacher by their email.
        Returns None if no teacher is found with the given email.
        """
        try:
            return Teacher.objects.get(email=email)
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
    def get_teacher_by_identification(identification):
        """
        Get a teacher by their identification.
        Returns None if no teacher is found with the given identification.
        """
        try:
            return Teacher.objects.get(identification=identification)
        except ObjectDoesNotExist:
            return None
    @staticmethod
    def create_teacher_by_coordinator(**kwargs):
        password = kwargs.pop('password', None)
        teacher = Teacher(**kwargs)  # No uses .create aquí
        if password:
            teacher.set_password(password)
        teacher.save()
        return teacher
    
    @staticmethod
    def list_avaliable_teachers():
        """
        List all available teachers.
        This method can be extended to filter teachers based on specific criteria.
        """
        return Teacher.objects.filter(is_active=True)  # Assuming is_active is a field in Teacher model
    
    @staticmethod
    def unactivate_teacher(tea_id):
        try:
            teacher = Teacher.objects.get(id=tea_id)
            if(not teacher.is_active):
                return None
            teacher.is_active = False 
            teacher.save()
            return teacher
        except ObjectDoesNotExist:
            return None
        
    @staticmethod
    def patch_teacher(tea_id, data):
        """
        Patch a teacher's information.
        This method updates only the fields provided in the data dictionary.
        """
        try:
            teacher = Teacher.objects.get(id=tea_id)
            for attr, value in data.items():
                setattr(teacher, attr, value)
            teacher.save()
            return teacher
        except ObjectDoesNotExist:
            return None