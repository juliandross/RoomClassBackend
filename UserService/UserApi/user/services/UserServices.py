from UserApi.user.repositories.UserRepository import UserRepository

class UserService:
    @staticmethod
    def list_users():
        return UserRepository.get_all_users()

    @staticmethod
    def retrieve_user(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def create_user(data):
        
        if UserRepository.get_user_by_email(data.get('email')):
            raise ValueError("Email ya registrado")
        return UserRepository.create_user(**data)

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return None
        return UserRepository.update_user(user, **data)

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return None
        UserRepository.delete_user(user)
        return True
