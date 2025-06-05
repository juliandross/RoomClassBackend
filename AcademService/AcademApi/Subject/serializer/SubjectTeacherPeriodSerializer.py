from rest_framework import serializers
from AcademApi.Subject.models.SubjectTeacherPeriod import SubjectTeacherPeriod
from AcademApi.Subject.models.Subject import Subject
from AcademApi.Subject.models.Teacher import Teacher
from AcademApi.Subject.models.Period import Period
from AcademApi.Subject.serializer.SubjectSerializer import SubjectSerializer
from AcademApi.Subject.serializer.TeacherSerializer import TeacherSerializer
from AcademApi.Subject.serializer.PeriodSerializer import PeriodSerializer

class SubjectTeacherPeriodSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), write_only=True)
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), write_only=True)
    period = serializers.PrimaryKeyRelatedField(queryset=Period.objects.all(), write_only=True)

    subject_detail = SubjectSerializer(source='subject', read_only=True)
    teacher_detail = TeacherSerializer(source='teacher', read_only=True)
    period_detail = PeriodSerializer(source='period', read_only=True)

    class Meta:
        model = SubjectTeacherPeriod
        fields = ['id', 'subject', 'teacher', 'period', 'subject_detail', 'teacher_detail', 'period_detail']