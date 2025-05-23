from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from AcademApi.Comp_RA_Subject.serializer.SubjectRASerializer import SubjectRASerializer
from AcademApi.Comp_RA_Subject.services.SubjectRAService import SubjectRAService
from rest_framework.permissions import IsAuthenticated, AllowAny

class SubjectRAListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        subject_ras = SubjectRAService.list_all_subject_ra()
        serializer = SubjectRASerializer(subject_ras, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            subject_ra = SubjectRAService.create_subject_ra(request.data)
            serializer = SubjectRASerializer(subject_ra)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class SubjectRADetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, subjectRA_id):
        subject_ra = SubjectRAService.get_subject_ra_by_id(subjectRA_id)
        if subject_ra:
            serializer = SubjectRASerializer(subject_ra)
            return Response(serializer.data)
        return Response({"detail": "Resultado de aprendizaje no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, subjectRA_id):
        subject_ra = SubjectRAService.update_subject_ra(subjectRA_id, request.data)
        if subject_ra:
            serializer = SubjectRASerializer(subject_ra)
            return Response(serializer.data)
        return Response({"detail": "Resultado de aprendizaje no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, subjectRA_id):
        if SubjectRAService.delete_subject_ra(subjectRA_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Resultado de aprendizaje no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    