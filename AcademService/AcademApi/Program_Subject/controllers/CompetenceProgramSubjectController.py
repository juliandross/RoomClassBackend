from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AcademApi.Program_Subject.services.CompetenceProgramSubjectService import CompetenceProgramSubjectService
from AcademApi.Program_Subject.serializer.CompetenceProgramSubjectSerializer import CompetenceProgramSubjectSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CompetenceProgramSubjectListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("Lista de competencias de programa asignatura")
        competence_program_subjects = CompetenceProgramSubjectService.list_all_competence_program_subjects()
        serializer = CompetenceProgramSubjectSerializer(competence_program_subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            competence_program_subject = CompetenceProgramSubjectService.create_competence_program_subject(request.data)
            serializer = CompetenceProgramSubjectSerializer(competence_program_subject)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class CompetenceProgramSubjectDetailView(APIView):
    def get(self, request, cps_id):
        competence_program_subject = CompetenceProgramSubjectService.get_competence_program_subject_by_id(cps_id)
        if competence_program_subject:
            serializer = CompetenceProgramSubjectSerializer(competence_program_subject)
            return Response(serializer.data)
        return Response({"detail": "Competencia de programa asignatura no encontrada."}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, cps_id):
        competence_program_subject = CompetenceProgramSubjectService.update_competence_program_subject(cps_id, request.data)
        if competence_program_subject:
            serializer = CompetenceProgramSubjectSerializer(competence_program_subject)
            return Response(serializer.data)
        return Response({"detail": "Competencia de programa asignatura no encontrada."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, cps_id):
        if CompetenceProgramSubjectService.delete_competence_program_subject(cps_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Competencia de programa asignatura no encontrada."}, status=status.HTTP_404_NOT_FOUND)