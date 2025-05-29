from rest_framework import serializers
from AcademApi.Comp_RA_Program.models.ProgramRA import ProgramRA

class ProgramRASerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramRA
        fields = '__all__'