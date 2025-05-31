from django.db import models

class Period(models.Model):
    perSemester = models.CharField(max_length=50)