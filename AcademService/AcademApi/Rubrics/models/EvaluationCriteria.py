from django.db import models

class EvaluationCriteria(models.Model):
    critPonderacion = models.CharField(max_length=100)
    Rubric = models.ForeignKey('Rubric', on_delete=models.CASCADE)