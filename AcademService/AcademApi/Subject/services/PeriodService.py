from AcademApi.Subject.repositories.PeriodRepository import PeriodRepository

class PeriodService:
    @staticmethod
    def list_all_periods():
        return PeriodRepository.get_all_periods()
    
    @staticmethod
    def get_period_by_id(per_id):
        return PeriodRepository.get_period_by_id(per_id)
    
    @staticmethod
    def create_period(data):
        return PeriodRepository.create_period(**data)
    
    @staticmethod
    def update_period(per_id, data):
        period = PeriodRepository.get_period_by_id(per_id)
        if period:
            return PeriodRepository.update_period(period, **data)
        return None
    
    @staticmethod
    def delete_period(per_id):
        period = PeriodRepository.get_period_by_id(per_id)
        if period:
            PeriodRepository.delete_period(period)
            return True
        return False