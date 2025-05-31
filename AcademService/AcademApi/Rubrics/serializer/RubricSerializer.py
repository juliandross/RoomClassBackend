from rest_framework import serializers
from AcademApi.Rubrics.models.Rubric import Rubric

class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubric
        fields = '__all__'