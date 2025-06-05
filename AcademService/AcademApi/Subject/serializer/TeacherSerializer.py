from rest_framework import serializers
from AcademApi.Subject.models.Teacher import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'