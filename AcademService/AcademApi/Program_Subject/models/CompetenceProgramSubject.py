from django.db import models

class CompetenceProgramSubject(models.Model):
    programCompetence = models.ForeignKey('ProgramCompetence', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)