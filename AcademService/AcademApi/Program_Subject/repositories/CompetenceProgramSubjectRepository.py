from AcademApi.Program_Subject.models.CompetenceProgramSubject import CompetenceProgramSubject
from django.core.exceptions import ObjectDoesNotExist

class CompetenceProgramSubjectRepository:
    @staticmethod
    def get_all_competence_program_subjects():

        return CompetenceProgramSubject.objects.all()
    
    @staticmethod
    def get_competence_program_subject_by_id(cps_id):
        try:
            return CompetenceProgramSubject.objects.get(id=cps_id)
        except ObjectDoesNotExist:
            return None
    
    @staticmethod
    def create_competence_program_subject(**kwargs):
        return CompetenceProgramSubject.objects.create(**kwargs)

    @staticmethod
    def update_competence_program_subject(competenceProgramSubject, **kwargs):
        for attr, value in kwargs.items():
            setattr(competenceProgramSubject, attr, value)
        competenceProgramSubject.save()
        return competenceProgramSubject

    @staticmethod
    def delete_competence_program_subject(competenceProgramSubject):
        competenceProgramSubject.delete()