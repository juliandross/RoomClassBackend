from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from AcademApi.Rubrics.serializer.LevelSerializer import LevelSerializer
from AcademApi.Rubrics.services.LevelService import LevelService
from rest_framework.permissions import IsAuthenticated, AllowAny

class LevelListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        levels = LevelService.list_all_levels()
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            level = LevelService.create_level(request.data)
            serializer = LevelSerializer(level)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LevelDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, level_id):
        level = LevelService.get_level_by_id(level_id)
        if level:
            serializer = LevelSerializer(level)
            return Response(serializer.data)
        return Response({"detail": "Nivel no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, level_id):
        level = LevelService.update_level(level_id, request.data)
        if level:
            serializer = LevelSerializer(level)
            return Response(serializer.data)
        return Response({"detail": "Nivel no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, level_id):
        if LevelService.delete_level(level_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Nivel no encontrado."}, status=status.HTTP_404_NOT_FOUND)

class LevelsByCriteriaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, criteria_id):
        levels = LevelService.get_levels_by_criteria(criteria_id)
        if levels:
            serializer = LevelSerializer(levels, many=True)
            return Response(serializer.data)
        return Response({"detail": "No se encontraron niveles para este criterio de evaluación."}, status=status.HTTP_404_NOT_FOUND)