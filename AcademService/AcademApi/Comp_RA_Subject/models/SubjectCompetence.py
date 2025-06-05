from django.db import models

class SubjectCompetence(models.Model):
    compDescription = models.CharField(max_length=255)
    compLevel = models.CharField(max_length=50)
    programCompetence = models.ForeignKey('ProgramCompetence', on_delete=models.CASCADE)
    subjectTeacherPeriod = models.ForeignKey('SubjectTeacherPeriod', on_delete=models.CASCADE)