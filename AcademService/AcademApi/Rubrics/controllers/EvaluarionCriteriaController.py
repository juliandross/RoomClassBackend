from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from AcademApi.EvaluationCriteria.serializer.EvaluationCriteriaSerializer import EvaluationCriteriaSerializer
from AcademApi.EvaluationCriteria.services.EvaluationCriteriaService import EvaluationCriteriaService
from rest_framework.permissions import IsAuthenticated, AllowAny

class EvaluationCriteriaListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        criteria = EvaluationCriteriaService.list_all_criteria()
        serializer = EvaluationCriteriaSerializer(criteria, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            criteria = EvaluationCriteriaService.create_criteria(request.data)
            serializer = EvaluationCriteriaSerializer(criteria)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class EvaluationCriteriaDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, criteria_id):
        criteria = EvaluationCriteriaService.get_criteria_by_id(criteria_id)
        if criteria:
            serializer = EvaluationCriteriaSerializer(criteria)
            return Response(serializer.data)
        return Response({"detail": "Criterio de evaluación no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, criteria_id):
        criteria = EvaluationCriteriaService.update_criteria(criteria_id, request.data)
        if criteria:
            serializer = EvaluationCriteriaSerializer(criteria)
            return Response(serializer.data)
        return Response({"detail": "Criterio de evaluación no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, criteria_id):
        if EvaluationCriteriaService.delete_criteria(criteria_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Criterio de evaluación no encontrado."}, status=status.HTTP_404_NOT_FOUND)

class EvaluationCriteriaByRubricView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, rubric_id):
        criteria = EvaluationCriteriaService.get_criteria_by_rubric(rubric_id)
        if criteria:
            serializer = EvaluationCriteriaSerializer(criteria, many=True)
            return Response(serializer.data)
        return Response({"detail": "No se encontraron criterios de evaluación para esta rúbrica."}, status=status.HTTP_404_NOT_FOUND)