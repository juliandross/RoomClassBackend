from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from SubjectApi.Subject.services.SubjectService import SubjectService
from SubjectApi.Subject.serializer.SubjectSerializer import SubjectSerializer
from SubjectApi.Subject.models.Subject import Subject

class SubjectListCreateView(APIView):
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