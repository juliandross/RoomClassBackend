from rest_framework import serializers
from AcademApi.Rubrics.models.EvaluationCriteria import EvaluationCriteria

class EvaluationCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationCriteria
        fields = '__all__'