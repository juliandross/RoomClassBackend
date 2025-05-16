from UserApi.models import User
from django.core.exceptions import ObjectDoesNotExist

class UserRepository:
    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create_user(**kwargs):
        return User.objects.create(**kwargs)

    @staticmethod
    def update_user(user, **kwargs):
        for attr, value in kwargs.items():
            setattr(user, attr, value)
        user.save()
        return user

    @staticmethod
    def delete_user(user):
        user.delete()
