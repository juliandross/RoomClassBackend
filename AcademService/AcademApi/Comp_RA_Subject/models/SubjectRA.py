from django.db import models

class SubjectRA(models.Model):
    raDescription = models.CharField(max_length=255)
    subjectCompetence = models.ForeignKey('SubjectCompetence', on_delete=models.CASCADE)