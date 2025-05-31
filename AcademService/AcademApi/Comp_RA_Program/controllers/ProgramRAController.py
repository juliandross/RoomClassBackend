from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AcademApi.Comp_RA_Program.services.ProgramRAService import ProgramRAService
from AcademApi.Comp_RA_Program.serializer.ProgramRASerializer import ProgramRASerializer
from AcademApi.Comp_RA_Program.models.ProgramRA import ProgramRA
from rest_framework.permissions import IsAuthenticated, AllowAny

class ProgramRAListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print("Lista de resultados de aprendizaje de programa")
        program_ras = ProgramRAService.list_all_program_ras()
        serializer = ProgramRASerializer(program_ras, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            program_ra = ProgramRAService.create_program_ra(request.data)
            serializer = ProgramRASerializer(program_ra)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class ProgramRADetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pro_ra_id):
        program_ra = ProgramRAService.get_program_ra_by_id(pro_ra_id)
        if program_ra:
            serializer = ProgramRASerializer(program_ra)
            return Response(serializer.data)
        return Response({"detail": "Resultado de aprendizaje de programa no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pro_ra_id):
        program_ra = ProgramRAService.update_program_ra(pro_ra_id, request.data)
        if program_ra:
            serializer = ProgramRASerializer(program_ra)
            return Response(serializer.data)
        return Response({"detail": "Resultado de aprendizaje de programa no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pro_ra_id):
        if ProgramRAService.delete_program_ra(pro_ra_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Resultado de aprendizaje de programa no encontrado."}, status=status.HTTP_404_NOT_FOUND)