from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AcademApi.Comp_RA_Program.services.ProgramCompetenceService import ProgramCompetenceService
from AcademApi.Comp_RA_Program.serializer.ProgramCompetenceSerializer import ProgramCompetenceSerializer
from AcademApi.Comp_RA_Program.models.ProgramCompetence import ProgramCompetence
from rest_framework.permissions import IsAuthenticated, AllowAny

class ProgramCompetenceListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("List of program competences")
        program_competences = ProgramCompetenceService.list_all_program_competences()
        serializer = ProgramCompetenceSerializer(program_competences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            program_competence = ProgramCompetenceService.create_program_competence(request.data)
            serializer = ProgramCompetenceSerializer(program_competence)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProgramCompetenceDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pro_comp_id):
        program_competence = ProgramCompetenceService.get_program_competence_by_id(pro_comp_id)
        if program_competence:
            serializer = ProgramCompetenceSerializer(program_competence)
            return Response(serializer.data)
        return Response({"detail": "Competencia de programa no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pro_comp_id):
        program_competence = ProgramCompetenceService.update_program_competence(pro_comp_id, request.data)
        if program_competence:
            serializer = ProgramCompetenceSerializer(program_competence)
            return Response(serializer.data)
        return Response({"detail": "Competencia de programa no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pro_comp_id):
        if ProgramCompetenceService.delete_program_competence(pro_comp_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Competencia de programa no encontrada."}, status=status.HTTP_404_NOT_FOUND)