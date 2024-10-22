from flask import request
from flask_restx import Namespace, Resource, abort
# from pycparser.ply.yacc import token

from app.DAO.error_auth_DAO import NotUsername, NotPassword, NotRole, error_auth, NotFavorit_genre
from app.contener import user_schemas, user_service, user_schema, auth_user

users_ns = Namespace('users')


@users_ns.route('/')
class UserView(Resource):
    # @auth_required
    def get(self):
        """

        :return: Возвращает информацию о пользователе
        """
        auth = request.headers
        if 'Authorization' not in auth:
            abort(401)
        user_data = auth.get('Authorization')
        token = user_data.split('Bearer ')[-1]

        result_check_token = user_service.get_information_by_user(token)

        if not result_check_token:
            abort(401)

        return result_check_token

    def patch(self):
        """

        :return: Возвращает код если пользователь не обновлен, 201 если пользователь обновлен
        """
        if "Authorization" not in request.headers:
            abort(403)
        data_token = request.headers.get('Authorization')
        token = data_token.split('Bearer ')[-1]
        result_check = user_service.get_information_by_user(token)
        if not result_check:
            abort(401)
        new_data_user = request.json
        result_update_user = user_service.paths_user_for_view(new_data_user, result_check)
        if not result_update_user:
            return 'Not update', 400
        return 'Yes update', 201

    def put(self):
        """
        Изменят пароль пользователя

        :return: Возвращает 400 если пароль не изменен,201 если пароль изменен
        """
        header = request.headers
        if 'Authorization' not in header:
            abort(401)
        data_from_header = header.get('Authorization')
        token = data_from_header.split('Bearer ')[-1]
        result_information_user = user_service.get_information_by_user(token)
        if not result_information_user:
            abort(401)
        passwords_user = request.json
        result_update_password_for_user = user_service.method_put_for_update_password_user(passwords_user,
                                                                                           result_information_user)
        if not result_update_password_for_user:
            return 'Not update password', 400
        return 'Yes update password', 201

        # new_password = request.json


@users_ns.route('/<int:uid>')
class UsersViews(Resource):
    def get(self, uid):
        """
        Возвращает один фильм по id
        :param uid: Integer
        :return: Возвращает 204 если фильма нет в бд, возвращает фильм
        """
        one_movie = user_schema.dump(user_service.get_one_user_by_id(uid))
        if not one_movie:
            return 'Not movie', 204
        return one_movie, 200

    def put(self, uid):
        """
        Изменяет данные пользователя
        :param uid: Integer id user
        :return:
        """
        result_put = request.json
        result_put['id'] = uid
        return user_service.update_user(result_put)

    def delete(self, uid):
        """

        :param uid:
        :return:
        """
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers.get('Authorization')
        token = data.split('Bearer ')[-1]
        r = data.split('Bearer ')
        print(f' hi={r} {token}')
        answer = auth_user.chek_token(token)
        if not answer:
            abort(401)
        elif answer.get('role') != 'admin':
            abort(403)
        return user_service.delete_user(uid)
