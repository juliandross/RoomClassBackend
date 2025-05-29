from rest_framework import serializers
from AcademApi.Subject.models.SubjectTeacherPeriod import SubjectTeacherPeriod

class SubjectTeacherPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectTeacherPeriod
        fields = '__all__'