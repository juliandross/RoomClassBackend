from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AcademApi.Subject.services.SubjectService import SubjectService
from AcademApi.Subject.serializer.SubjectSerializer import SubjectSerializer
from AcademApi.Subject.models.Subject import Subject
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

class SubjectListCreateView(APIView):
    permission_classes = [IsAuthenticated]    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subjectService = SubjectService()

    def get(self, request):
        subjects = self.subjectService.list_subjects()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            print("Creando una asignatura...")
            subject = self.subjectService.create_subject(request.data)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SubjectDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, subject_id):
        subject = self.subjectService.retrieve_subject(subject_id)
        if not subject:
            return Response({"detail": "Asignatura no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, subject_id):
        subject = self.subjectService.update_subject(subject_id, request.data)
        if not subject:
            return Response({"detail": "Asignatura no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def delete(self, request, subject_id):
        success = self.subjectService.delete_subject(subject_id)
        if not success:
            return Response({"detail": "Asignatura no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SubjectController(viewsets.ViewSet):
    def __init__(self):
        self.subjectService = SubjectService()
        self.permission_classes = [IsAuthenticated]
        
    def list_available_subjects(self, request):
        subjects = self.subjectService.list_available_subjects()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    
    def unactivate_subject(self, request, subject_id):
        result = SubjectService.unactivate_subject(subject_id)
        if isinstance(result, Response):
            return result  # Ya es una respuesta de error (404)
        return Response({"detail": "Asignatura desactivada correctamente."}, status=status.HTTP_200_OK)