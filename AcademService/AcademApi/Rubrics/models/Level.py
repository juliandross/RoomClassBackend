from django.db import models

class Level(models.Model):
    nivCategoria = models.CharField(max_length=30)
    nivDescripcion = models.CharField(max_length=100)
    EvaluationCriteria = models.ForeignKey('EvaluationCriteria', on_delete=models.CASCADE)