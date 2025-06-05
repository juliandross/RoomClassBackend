from django.db import models

class SubjectTeacherPeriod(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='subject_teacher_periods')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='subject_teacher_periods')
    period = models.ForeignKey('Period', on_delete=models.CASCADE, related_name='subject_teacher_periods')