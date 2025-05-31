from rest_framework import serializers
from AcademApi.Comp_RA_Program.models.ProgramCompetence import ProgramCompetence

class ProgramCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramCompetence
        fields = '__all__'