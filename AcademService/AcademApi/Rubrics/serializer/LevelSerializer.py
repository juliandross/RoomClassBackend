from AcademApi.Rubrics.models.Level import Level
from rest_framework import serializers

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'