from rest_framework import serializers
from AcademApi.Comp_RA_Subject.models.SubjectRA import SubjectRA

class SubjectRASerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectRA
        fields = '__all__'