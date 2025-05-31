from django.db import models

class Rubric(models.Model):
    rubDescription = models.CharField(max_length=100)
    SubjectRA = models.ForeignKey('SubjectRA', on_delete=models.CASCADE)