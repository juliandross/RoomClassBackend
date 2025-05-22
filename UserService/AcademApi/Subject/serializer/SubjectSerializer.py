from rest_framework import serializers
from AcademApi.Subject.models.Subject import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subjectName', 'subjectDescription', 'subjectCredits', 'subjectSemester', 'is_active']