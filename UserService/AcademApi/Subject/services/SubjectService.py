from SubjectApi.Subject.repositories.SubjectRepository import SubjectRepository

class SubjectService:
    @staticmethod
    def list_subjects():
        return SubjectRepository.get_all_subjects()

    @staticmethod
    def retrieve_subject(subject_id):
        return SubjectRepository.get_subject_by_id(subject_id)

    @staticmethod
    def create_subject(data):
        if SubjectRepository.get_subject_by_name(data.get('subjectName')):
            raise ValueError("Subject ya registrado")
        return SubjectRepository.create_subject(**data)

    @staticmethod
    def update_subject(subject_id, data):
        subject = SubjectRepository.get_subject_by_id(subject_id)
        if not subject:
            return None
        return SubjectRepository.update_subject(subject, **data)

    @staticmethod
    def delete_subject(subject_id):
        subject = SubjectRepository.get_subject_by_id(subject_id)
        if not subject:
            return None
        SubjectRepository.delete_subject(subject)
        return True