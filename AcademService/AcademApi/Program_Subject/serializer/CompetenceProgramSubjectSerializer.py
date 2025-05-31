from rest_framework import serializers
from AcademApi.Program_Subject.models.CompetenceProgramSubject import CompetenceProgramSubject

class CompetenceProgramSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetenceProgramSubject
        fields = '__all__'