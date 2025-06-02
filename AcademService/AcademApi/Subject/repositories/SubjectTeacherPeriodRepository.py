from AcademApi.Subject.models.SubjectTeacherPeriod import SubjectTeacherPeriod
from django.core.exceptions import ObjectDoesNotExist

class SubjectTeacherPeriodRepository:
    # Metodo para obtener todos los SubjectTeacherPeriod
    @staticmethod
    def get_all_subject_teacher_periods():
        return SubjectTeacherPeriod.objects.all()

    # Metodo para obtener un SubjectTeacherPeriod por su id
    @staticmethod
    def get_subject_teacher_period_by_id(stp_id):
        try:
            return SubjectTeacherPeriod.objects.get(id=stp_id)
        except ObjectDoesNotExist:
            return None

    # Metodo para crear un SubjectTeacherPeriod
    @staticmethod
    def create_subject_teacher_period(**kwargs):
        return SubjectTeacherPeriod.objects.create(**kwargs)

    # Metodo para actualizar un SubjectTeacherPeriod
    @staticmethod
    def update_subject_teacher_period(subject_teacher_period, **kwargs):
        for attr, value in kwargs.items():
            setattr(subject_teacher_period, attr, value)
        subject_teacher_period.save()
        return subject_teacher_period

    # Metodo para eliminar un SubjectTeacherPeriod
    @staticmethod
    def delete_subject_teacher_period(subject_teacher_period):
        subject_teacher_period.delete()
        
    @staticmethod
    def get_subject_report(subject_id):
        try:
            subjectReport = SubjectTeacherPeriod.objects.select_related('subject', 'teacher', 'period').get(id=subject_id)
            return subjectReport
        except SubjectTeacherPeriod.DoesNotExist:
            return None
        
    @staticmethod
    def list_subject_reports():
        return SubjectTeacherPeriod.objects.select_related('subject', 'teacher', 'period').all()