from AcademApi.Subject.models.Period import Period
from django.core.exceptions import ObjectDoesNotExist

class PeriodRepository:
    # Metodo para obtener todos los periodos
    @staticmethod
    def get_all_periods():
        return Period.objects.all()

    # Metodo para obtener un periodo por su id
    @staticmethod
    def get_period_by_id(per_id):
        try:
            return Period.objects.get(id=per_id)
        except ObjectDoesNotExist:
            return None

    # Metodo para crear un periodo
    @staticmethod
    def create_period(**kwargs):
        return Period.objects.create(**kwargs)

    # Metodo para actualizar un periodo
    @staticmethod
    def update_period(period, **kwargs):
        for attr, value in kwargs.items():
            setattr(period, attr, value)
        period.save()
        return period

    # Metodo para eliminar un periodo
    @staticmethod
    def delete_period(period):
        period.delete()