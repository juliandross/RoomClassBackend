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
        if 'password' not in data:
            return Response({'detail': 'El campo "password" es obligatorio.'}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get('first_name') or not data.get('email') or not data.get('last_name'):
            return Response({'detail': 'Los campos "name" y "email" son obligatorios.'}, status=status.HTTP_400_BAD_REQUEST)
        if TeacherRepository.get_teacher_by_id(data.get('id')):
            return Response({'detail': 'Ya existe un docente con este ID.'}, status=status.HTTP_400_BAD_REQUEST)
        if TeacherRepository.get_teacher_by_email(data.get('email')):
            return Response({'detail': 'Ya existe un docente con este email.'}, status=status.HTTP_400_BAD_REQUEST)
        if TeacherRepository.get_teacher_by_identification(data.get('identification')):
            return Response({'detail': 'Ya existe un docente con esta identificación.'}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get('rol'):
            data['rol'] = 'DOCENTE'
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
    
    @staticmethod
    def patch_teacher(tea_id, data):
        teacher = TeacherRepository.get_teacher_by_id(tea_id)
        if not teacher:
            return Response({"detail": "Docente no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        if teacher.is_active == False:
            return Response({"detail": "Docente no activo."}, status=status.HTTP_400_BAD_REQUEST)
        if 'identification' in data:
            existing_teacher = TeacherRepository.get_teacher_by_identification(data['identification'])
            if existing_teacher and existing_teacher.id != tea_id:
                return Response({"detail": "Ya existe un docente con esta identificación."}, status=status.HTTP_400_BAD_REQUEST)
        if 'email' in data:
            existing_teacher = TeacherRepository.get_teacher_by_email(data['email'])
            if existing_teacher and existing_teacher.id != tea_id:
                return Response({"detail": "Ya existe un docente con este email."}, status=status.HTTP_400_BAD_REQUEST)
        # Aquí sí llama al patch del repositorio
        return TeacherRepository.patch_teacher(tea_id, data)