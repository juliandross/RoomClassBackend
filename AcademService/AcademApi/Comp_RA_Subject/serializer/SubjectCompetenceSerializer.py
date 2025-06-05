from rest_framework import serializers
from AcademApi.Comp_RA_Subject.models.SubjectCompetence import SubjectCompetence

class SubjectCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectCompetence
        fields = '__all__'