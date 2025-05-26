from django.db import models

class Subject(models.Model):
    subjectName = models.CharField(max_length=30)
    subjectDescription = models.CharField(max_length=100)
    subjectCredits = models.PositiveSmallIntegerField()
    subjectSemester = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
