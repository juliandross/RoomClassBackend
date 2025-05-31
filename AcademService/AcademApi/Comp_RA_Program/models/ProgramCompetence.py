from django.db import models

class ProgramCompetence(models.Model):
    proCompDescription = models.CharField(max_length=255)
    proCompLevel = models.CharField(max_length=50)