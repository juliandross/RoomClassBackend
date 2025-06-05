
from rest_framework import serializers
from AcademApi.Subject.models.SubjectTeacherPeriod import SubjectTeacherPeriod
from AcademApi.Subject.serializer.SubjectSerializer import SubjectSerializer
from AcademApi.Subject.serializer.TeacherSerializer import TeacherSerializer
from AcademApi.Subject.serializer.PeriodSerializer import PeriodSerializer

class SubjectTeacherPeriodSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    period = PeriodSerializer(read_only=True)
    class Meta:
        model = SubjectTeacherPeriod
        fields = '__all__'