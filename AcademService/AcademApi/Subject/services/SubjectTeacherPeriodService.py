from AcademApi.Subject.repositories.SubjectTeacherPeriodRepository import SubjectTeacherPeriodRepository
from rest_framework.response import Response
from rest_framework import status
class SubjectTeacherPeriodService:
    def __init__(self):
        self.subject_teacher_period_repository = SubjectTeacherPeriodRepository()
        
    @staticmethod
    def list_all_subject_teacher_periods():
        return SubjectTeacherPeriodRepository.get_all_subject_teacher_periods()
    
    @staticmethod
    def get_subject_teacher_period_by_id(stp_id):
        return SubjectTeacherPeriodRepository.get_subject_teacher_period_by_id(stp_id)
    
    @staticmethod
    def create_subject_teacher_period(data):
        return SubjectTeacherPeriodRepository.create_subject_teacher_period(**data)
    
    @staticmethod
    def update_subject_teacher_period(stp_id, data):
        subject_teacher_period = SubjectTeacherPeriodRepository.get_subject_teacher_period_by_id(stp_id)
        if subject_teacher_period:
            return SubjectTeacherPeriodRepository.update_subject_teacher_period(subject_teacher_period, **data)
        return None
    
    @staticmethod
    def delete_subject_teacher_period(stp_id):
        subject_teacher_period = SubjectTeacherPeriodRepository.get_subject_teacher_period_by_id(stp_id)
        if subject_teacher_period:
            SubjectTeacherPeriodRepository.delete_subject_teacher_period(subject_teacher_period)
            return True
        return False
    
        
    @staticmethod
    def get_subject_report(subject_id):
        subject_teacher_period = SubjectTeacherPeriodRepository.get_subject_report(subject_id)
        if not subject_teacher_period:
            return None
        return subject_teacher_period