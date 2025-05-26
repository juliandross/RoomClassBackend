from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AcademApi.Comp_RA_Subject.services.SubjectCompetenceService import SubjectCompetenceService
from AcademApi.Comp_RA_Subject.serializer.SubjectCompetenceSerializer import SubjectCompetenceSerializer
from AcademApi.Comp_RA_Subject.models.SubjectCompetence import SubjectCompetence
from rest_framework.permissions import IsAuthenticated, AllowAny

class SubjectCompetenceListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print("Lita de competencias de asignatura")
        SubjectCompetence = SubjectCompetenceService.list_all_subject_competences()
        serializer = SubjectCompetenceSerializer(SubjectCompetence, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            SubjectCompetence = SubjectCompetenceService.create_subject_competence(request.data)
            serializer = SubjectCompetenceSerializer(SubjectCompetence)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class SubjectCompetenceDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, comp_id):
        SubjectCompetence = SubjectCompetenceService.get_subject_competence_by_id(comp_id)
        if SubjectCompetence:
            serializer = SubjectCompetenceSerializer(SubjectCompetence)
            return Response(serializer.data)
        return Response({"detail": "Competencia de asignatura no encontrada."}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, comp_id):
        SubjectCompetence = SubjectCompetenceService.update_subject_competence(comp_id, request.data)
        if SubjectCompetence:
            serializer = SubjectCompetenceSerializer(SubjectCompetence)
            return Response(serializer.data)
        return Response({"detail": "Competencia de asignatura no encontrada."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, comp_id):
        if SubjectCompetenceService.delete_subject_competence(comp_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Competencia de asignatura no encontrada."}, status=status.HTTP_404_NOT_FOUND)