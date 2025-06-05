from rest_framework import serializers
from AcademApi.Subject.models.Period import Period

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'