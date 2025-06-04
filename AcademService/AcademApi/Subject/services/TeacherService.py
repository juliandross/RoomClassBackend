from AcademApi.Subject.repositories.TeacherRepository import TeacherRepository
from rest_framework.response import Response
from rest_framework import status
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
    
    @staticmethod
    def create_teacher_by_coordinator(data, rol):
        if rol != 'COORDINADOR':
            return Response({'detail': 'No autorizado. Solo coordinadores pueden crear docentes.'}, status=403)
        return TeacherRepository.create_teacher_by_coordinator(**data)
    
    @staticmethod
    def list_avaliable_teachers():
        """
        List all available teachers.
        This method can be extended to filter teachers based on specific criteria.
        """
        return TeacherRepository.list_avaliable_teachers()
    
    @staticmethod
    def unactivate_teacher(tea_id):
        teacher = TeacherService.get_teacher_by_id(tea_id)
        if not teacher:
            return Response({"detail": "Docente no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        teacher = TeacherRepository.unactivate_teacher(tea_id)
        if not teacher:
            return Response({"detail": "No se pudo desactivar el docente."}, status=status.HTTP_400_BAD_REQUEST)
        return teacher