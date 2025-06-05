from django.db import models

class ProgramRA(models.Model):
    proRADescription = models.CharField(max_length=255)
    programCompetence = models.ForeignKey('ProgramCompetence', on_delete=models.CASCADE)