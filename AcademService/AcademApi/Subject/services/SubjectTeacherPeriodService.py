from AcademApi.Subject.repositories.SubjectTeacherPeriodRepository import SubjectTeacherPeriodRepository

class SubjectTeacherPeriodService:
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