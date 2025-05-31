from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from AcademApi.Rubrics.serializer.RubricSerializer import RubricSerializer
from AcademApi.Rubrics.services.RubricService import RubricService
from rest_framework.permissions import IsAuthenticated, AllowAny

class RubricListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rubrics = RubricService.list_all_rubrics()
        serializer = RubricSerializer(rubrics, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            rubric = RubricService.create_rubric(request.data)
            serializer = RubricSerializer(rubric)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RubricDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, rubric_id):
        rubric = RubricService.get_rubric_by_id(rubric_id)
        if rubric:
            serializer = RubricSerializer(rubric)
            return Response(serializer.data)
        return Response({"detail": "Rubrica no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, rubric_id):
        rubric = RubricService.update_rubric(rubric_id, request.data)
        if rubric:
            serializer = RubricSerializer(rubric)
            return Response(serializer.data)
        return Response({"detail": "Rubrica no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, rubric_id):
        if RubricService.delete_rubric(rubric_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Rubrica no encontrada."}, status=status.HTTP_404_NOT_FOUND)

class RubricBySubjectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, subjectRA_id):
        rubrics = RubricService.get_rubrics_by_subject(subjectRA_id)
        if rubrics:
            serializer = RubricSerializer(rubrics, many=True)
            return Response(serializer.data)
        return Response({"detail": "No se encontraron rubricas para esta asignatura."}, status=status.HTTP_404_NOT_FOUND)