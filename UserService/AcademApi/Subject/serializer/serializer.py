from rest_framework import serializers
from SubjectApi.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subjectName', 'subjectDescription', 'subjectCredits', 'subjectSemester', 'is_active']

        def create(self, validated_data):
            return super().create(validated_data)