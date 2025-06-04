from common_models.user.User import User
from UserApi.user.repositories.UserRepository import UserRepository
from UserApi.user.serializer.UserSerializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
class UserService:
    @staticmethod
    def list_users():
        if not UserRepository.get_all_users():
            return Response({"detail": "No hay usuarios registrados"}, status=status.HTTP_404_NOT_FOUND)
        users = UserRepository.get_all_users()
        serializer = UserSerializer(users, many=True)
        return serializer.data

    @staticmethod
    def retrieve_user(user_id):
        if not UserRepository.get_user_by_id(user_id):
            return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        user = UserRepository.get_user_by_id(user_id)
        serializer = UserSerializer(user)
        return serializer.data
    
    @staticmethod
    def create_user(data):
        if UserRepository.get_user_by_email(data.get('email')):
            return Response({"detail": "El correo electrónico ya está en uso"}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get('password'):
            return Response({"detail": "La contraseña es requerida"}, status=status.HTTP_400_BAD_REQUEST)
        user = UserRepository.create_user(**data)
        if not user:
            return Response({"detail": "Error al crear el usuario"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return None
        return UserRepository.update_user(user, **data)

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return None
        UserRepository.delete_user(user)
        return True
    
    @staticmethod
    def get_user_by_email(email):
        user = UserRepository.get_user_by_email(email)
        if not user:
            return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return user

    @staticmethod
    def createCoordinate(data):
        if not data.get('email'):
            return Response({"detail": "El correo electrónico es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get('password'):
            return Response({"detail": "La contraseña es requerida"}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get('identification'):
            return Response({"detail": "La identificación es requerida"}, status=status.HTTP_400_BAD_REQUEST)
        if UserRepository.get_user_by_email(data.get('email')):
            return Response({"detail": "El correo electrónico ya está en uso"}, status=status.HTTP_400_BAD_REQUEST)
        if UserRepository.get_user_by_identification(data.get('identification')):
            return Response({"detail": "Ya existe un usuario con esta identificación"}, status=status.HTTP_400_BAD_REQUEST)
        user = UserRepository.createCoordinate(**data)
        if not user:
            return Response({"detail": "Error al crear el usuario"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @staticmethod
    def patch_user(user_id, data):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        # Valida que no sea el email del mismo usuario
        if 'email' in data and data['email'] != user.email:
            if UserRepository.get_user_by_email(data['email']):
                return Response({"detail": "El correo electrónico ya está en uso"}, status=status.HTTP_400_BAD_REQUEST)
        if 'identification' in data and data['identification'] != user.identification:
            if UserRepository.get_user_by_identification(data['identification']):
                return Response({"detail": "Ya existe un usuario con esta identificación"}, status=status.HTTP_400_BAD_REQUEST)
        updated_user = UserRepository.patch_user(user, **data)
        if not updated_user:
            return Response({"detail": "Error al actualizar el usuario"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(updated_user)
        return Response(serializer.data, status=status.HTTP_200_OK)