from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from UserApi.user.services.UserServices import UserService
from common_models.user.User import User
from UserApi.user.serializer.UserSerializer import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserListCreateView(APIView):
    permission_classes = [AllowAny]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.userService = UserService()
    
    def get(self, request):
        users = self.userService.list_users()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        return UserService.create_user(request.data)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, user_id):
        user = UserService.retrieve_user(user_id)
        if not user:
            return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = UserService.update_user(user_id, request.data)
        if not user:
            return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, user_id):
        success = UserService.delete_user(user_id)
        if not success:
            return Response({"detail": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserController(viewsets.ViewSet):
    
    def __init__(self):
        self.user_service = UserService()
    permission_classes = [IsAuthenticated]
    
    def getUserByEmail(self, request, email=None):
        user = self.user_service.get_user_by_email(email)
        if not user:
            return None
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)