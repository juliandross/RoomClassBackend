from django.db import models

class Teacher(models.Model):
    teaMail = models.EmailField(max_length=254, unique=True)
    teaName = models.CharField(max_length=100)
    teaLastName = models.CharField(max_length=100)
    teaType = models.CharField(max_length=50)
    teaTypeId = models.CharField(max_length=50)
    teaRecentTitle = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)