from django.db import models

class SubjectTeacherPeriod(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    period = models.ForeignKey('Period', on_delete=models.CASCADE)