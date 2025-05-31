from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AcademApi.Subject.services.TeacherService import TeacherService
from AcademApi.Subject.serializer.TeacherSerializer import TeacherSerializer
from AcademApi.Subject.models.Teacher import Teacher
from rest_framework.permissions import IsAuthenticated

class TeacherListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teachers = TeacherService.get_all_teachers()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            teacher = TeacherService.create_teacher(request.data)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, tea_id):
        teacher = TeacherService.get_teacher_by_id(tea_id)
        if teacher:
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
        return Response({"detail": "Docente no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, tea_id):
        teacher = TeacherService.update_teacher(tea_id, request.data)
        if teacher:
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
        return Response({"detail": "Docente no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, tea_id):
        if TeacherService.delete_teacher(tea_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Docente no encontrado."}, status=status.HTTP_404_NOT_FOUND)