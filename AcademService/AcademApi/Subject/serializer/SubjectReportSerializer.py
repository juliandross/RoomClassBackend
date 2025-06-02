from rest_framework import serializers
from AcademApi.Subject.models.SubjectTeacherPeriod import SubjectTeacherPeriod
from AcademApi.Subject.models.Subject import Subject
from AcademApi.Subject.models.Teacher import Teacher
from AcademApi.Subject.models.Period import Period

# Serializador para Subject
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subjectName', 'subjectDescription', 'subjectCredits', 'subjectSemester', 'is_active']

# Serializador para Teacher (solo los campos propios de Teacher y User)
class TeacherSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    rol = serializers.CharField()

    class Meta:
        model = Teacher
        fields = [
            'id', 'email', 'first_name', 'last_name', 'rol',
            'teaType', 'teaTypeId', 'teaRecentTitle'
        ]

# Serializador para Period
class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['id', 'perSemester']

# Serializador principal para el reporte
class SubjectReportSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    period = PeriodSerializer(read_only=True)

    class Meta:
        model = SubjectTeacherPeriod
        fields = ['id', 'subject', 'teacher', 'period']