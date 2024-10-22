from app.DAO.userDAO import UserDAO

from app.service.auth_recvaer_service import AuthReceiverService


class UserService:
    def __init__(self, dao_user: UserDAO, auth_service: AuthReceiverService):
        self.dao_user = dao_user
        self.auth_service = auth_service

    def get_all_user(self):
        return self.dao_user.get_all_user()

    def get_one_user_by_id(self, uid):
        answer = self.dao_user.get_user_one(uid)
        # if not answer:
        #     return '', 204
        return answer

    def add_user(self, data_add):
        """
         добавляет нового пользователя в таблицу
        :param data_add: словарь {username:"Кто-то", password : какой-то, role : кем=то
        :return: возвращает  201 если все хорошо и 400 если все плохо
        """
        del data_add['password_2']
        password = data_add['password']

        modified_password = self.auth_service.generation_password(password)
        data_add['password'] = modified_password
        answer = self.dao_user.add_user(data_add)
        if not answer:
            return "Такой email уже есть", 400
        return "yes", 201

    def update_user(self, data_update):
        filter_user = self.dao_user.get_user_one(data_update.get('id'))
        if not filter_user:
            return "", 204
        filter_user.email = data_update.get('email')
        filter_user.password = self.auth_service.generation_password(data_update.get('password'))
        filter_user.name = data_update.get('name')
        filter_user.favorite_genre = data_update.get('favorite_genre')
        # filter_user.password = self.auth_service.generation_password(data_update.get('password'))
        # filter_user.role = data_update.get('role')
        self.dao_user.update_user(filter_user)
        return "", 201

        # def patch_user(self, data_patch):
        #     filter_user_for_patch = self.dao_user.get_user_one(data_patch.get('id'))
        #     if not filter_user_for_patch:
        #         return ",", 204
        #
        #     if data_patch.get('email'):
        #         filter_user_for_patch = data_patch.get('email')
        #     if data_patch.get('password'):
        #         filter_user_for_patch.password = self.auth_service.generation_password(data_patch.get('password'))
        #     if data_patch.get('name'):
        #         filter_user_for_patch.username = data_patch.get('name')
        #     if data_patch.get('favorite_genre'):
        #         filter_user_for_patch.favorite_genre = data_patch.get('favorite_genre')
        #     # self.dao_user.update_user(filter_user_for_patch)
        # return ".", 201

    def delete_user(self, did):

        result_for_delete_user = self.dao_user.get_user_one(did)
        if not result_for_delete_user:
            return "Not user", 204
        result = self.dao_user.delete_user_by_id(result_for_delete_user)
        if not result:
            return 'not delete', 400
        return "user delete", 201

    def password_comparison(self, data):
        users_by_name = self.dao_user.get_all_user_by_name(data.get('username'))
        if not users_by_name:
            return 'Not user', 204

        password = data.get('password')
        for user in users_by_name:
            result = self.auth_service.check_password(password, user.password)

            if not result:
                return {"not": "Not password"}, 401
        data_for_token = {"username": user.username, "role": user.role}
        access_token = self.auth_service.generation_access_token(data_for_token)
        refresh_token = self.auth_service.generation_refresh_token(data_for_token)
        print('HI')
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }, 200

    def check_token(self, data):

        # refresh_token = data.get("refresh_token")
        # print(f"cek 1-{refresh_token}")
        result_check_token = self.auth_service.chekc_token_authservice(data)
        print(f'result_check_token - {result_check_token}')
        # print(f"chec 2-{refresh_token}")
        if not result_check_token:
            return 'Time not'
        # new_token = self.auth_service.chekc_token_authservice(refresh_token)
        access_token = self.auth_service.generation_access_token(result_check_token)
        refresh_token = self.auth_service.generation_refresh_token(result_check_token)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }, 200

    def cech_user(self, data):
        """
        Проверяет пароль пользователя
        :param data: принимает словарь { email:какая-то почта password:Какой-то пароль}
        :return: пару access_token refresh_token
        """
        password = data.get('password')
        email = data.get('email')
        result_user_by_email = self.dao_user.get_user_by_email(email)
        if not result_user_by_email:
            return False
        date_for_generation_token = {'id': result_user_by_email.id,
                                     'email': result_user_by_email.email,
                                     'name': result_user_by_email.name,
                                     'favorite_genre': result_user_by_email.favorite_genre
                                     }
        # hahs_password_login_user = self.auth_service.generation_password(password)
        result_user_password = self.auth_service.check_password(password, result_user_by_email.password)
        if not result_user_password:
            return False
        get_access_token_for_user = self.auth_service.generation_access_token(date_for_generation_token)
        get_refresh_token_for_user = self.auth_service.generation_refresh_token(date_for_generation_token)
        result_user_auth = {"access_token": get_access_token_for_user,
                            "refresh_token": get_refresh_token_for_user}
        return result_user_auth

    def get_information_by_user(self, data_user):

        data_user_from_token = self.auth_service.chekc_token_authservice(data_user)
        print(f"user_service_token {data_user_from_token}")
        if not data_user_from_token:
            return False
        del data_user_from_token['exp']
        return data_user_from_token

    def paths_user_for_view(self, data_user, result_check_token):

        id_user = result_check_token.get('id')
        result_search_user_from_table = self.dao_user.get_user_one(id_user)
        # print(type(result_search_user_from_table))
        if data_user.get('name'):
            result_search_user_from_table.name = data_user.get('name')
        #     self.dao_user.update_user(result_search_user_from_table)
        if data_user.get('favorite_genre'):
            result_search_user_from_table.favorite_genre = data_user.get('favorite_genre')
        #     self.dao_user.update_user(result_search_user_from_table)
        # print(f"paths user - {data_user} - {result_check_token}")
        return self.dao_user.update_user(result_search_user_from_table)

    def method_put_for_update_password_user(self, new_password, information_user):

        password_one = new_password.get('password_1')
        password_two = new_password.get('password_2')
        get_user_by_id = self.dao_user.get_user_one(information_user.get('id'))
        print(f"method_put - {password_two}, {get_user_by_id}")
        result_check_password = self.auth_service.check_password(password_one,get_user_by_id.password)

        if not result_check_password:
            return False
        new_hash_password = self.auth_service.generation_password(password_two)
        get_user_by_id.email = get_user_by_id.email
        get_user_by_id.password = new_hash_password
        get_user_by_id.name = get_user_by_id.name
        get_user_by_id.favorite_genre = get_user_by_id.favorite_genre
        return self.dao_user.update_user(get_user_by_id)