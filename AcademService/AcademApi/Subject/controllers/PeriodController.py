from rest_framework.viewsets import APIView
from rest_framework.response import Response
from rest_framework import status
from AcademApi.Subject.services.PeriodService import PeriodService
from AcademApi.Subject.serializer.PeriodSerializer import PeriodSerializer
from AcademApi.Subject.models.Period import Period
from rest_framework.permissions import IsAuthenticated

class PeriodListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        periods = PeriodService.get_all_periods()
        serializer = PeriodSerializer(periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            period = PeriodService.create_period(request.data)
            serializer = PeriodSerializer(period)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class PeriodDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, per_id):
        period = PeriodService.get_period_by_id(per_id)
        if period:
            serializer = PeriodSerializer(period)
            return Response(serializer.data)
        return Response({"detail": "Periodo no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, per_id):
        period = PeriodService.update_period(per_id, request.data)
        if period:
            serializer = PeriodSerializer(period)
            return Response(serializer.data)
        return Response({"detail": "Periodo no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, per_id):
        if PeriodService.delete_period(per_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Periodo no encontrado."}, status=status.HTTP_404_NOT_FOUND)