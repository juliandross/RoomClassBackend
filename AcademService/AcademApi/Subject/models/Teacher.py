from django.db import models
from common_models.user.User import User

class Teacher(User):
    teaType = models.CharField(max_length=50)
    teaTypeId = models.CharField(max_length=50)
    teaRecentTitle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'