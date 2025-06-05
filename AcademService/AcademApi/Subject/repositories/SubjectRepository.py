from AcademApi.Subject.models.Subject import Subject
from django.core.exceptions import ObjectDoesNotExist

class SubjectRepository:
    @staticmethod
    def get_all_subjects():
        # Solo obtener sujetos activos
        return Subject.objects.filter(is_active=True).all()

    @staticmethod
    def get_subject_by_id(subject_id):
        try:
            # Solo obtener sujetos activos
            if not Subject.objects.filter(id=subject_id, is_active=True).exists():
                raise ObjectDoesNotExist
            return Subject.objects.get(id=subject_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create_subject(**kwargs):
        return Subject.objects.create(**kwargs)

    @staticmethod
    def update_subject(subject, **kwargs):
        for attr, value in kwargs.items():
            setattr(subject, attr, value)
        subject.save()
        return subject

    @staticmethod
    def delete_subject(subject):
        subject.delete()

    @staticmethod
    def list_available_subjects():
        """
        List all available subjects.
        This method can be extended to filter subjects based on specific criteria.
        """
        return Subject.objects.filter(is_active=True)  # Assuming is_active is a field in Subject model
    
    @staticmethod
    def unactivate_subject(subject_id):
        try:
            subject = Subject.objects.get(id=subject_id)
            if not subject.is_active:
                return None
            subject.is_active = False 
            subject.save()
            return subject
        except ObjectDoesNotExist:
            return None