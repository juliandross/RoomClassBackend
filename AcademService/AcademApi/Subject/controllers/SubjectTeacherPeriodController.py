from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AcademApi.Subject.services.SubjectTeacherPeriodService import SubjectTeacherPeriodService
from AcademApi.Subject.serializer.SubjectTeacherPeriodSerializer import SubjectTeacherPeriodSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from AcademApi.Subject.serializer.SubjectReportSerializer import SubjectReportSerializer
class SubjectTeacherPeriodListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        subject_teacher_periods = SubjectTeacherPeriodService.get_all_subject_teacher_periods()
        serializer = SubjectTeacherPeriodSerializer(subject_teacher_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            subject_teacher_period = SubjectTeacherPeriodService.create_subject_teacher_period(request.data)
            serializer = SubjectTeacherPeriodSerializer(subject_teacher_period)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SubjectTeacherPeriodDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, stp_id):
        subject_teacher_period = SubjectTeacherPeriodService.get_subject_teacher_period_by_id(stp_id)
        if subject_teacher_period:
            serializer = SubjectTeacherPeriodSerializer(subject_teacher_period)
            return Response(serializer.data)
        return Response({"detail": "Asignatura docente periodo no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, stp_id):
        subject_teacher_period = SubjectTeacherPeriodService.update_subject_teacher_period(stp_id, request.data)
        if subject_teacher_period:
            serializer = SubjectTeacherPeriodSerializer(subject_teacher_period)
            return Response(serializer.data)
        return Response({"detail": "Asignatura docente periodo no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, stp_id):
        if SubjectTeacherPeriodService.delete_subject_teacher_period(stp_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Asignatura docente periodo no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
class SubjectAssingController(viewsets.ViewSet):
    def __init__(self):
        self.subject_service = SubjectTeacherPeriodService()
        permission_classes = [IsAuthenticated]
        
    # This method is used to get the report of a subject (Teacher, Subject and Period)
    def get_subject_report(self, request, subject_id=None):
        subjectReport = self.subject_service.get_subject_report(subject_id)
        if not subjectReport:
            return Response({"detail": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response(
            SubjectReportSerializer(subjectReport).data,
            status=status.HTTP_200_OK
        )