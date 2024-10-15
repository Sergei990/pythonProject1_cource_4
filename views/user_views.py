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
        auth = request.headers
        if 'Authorization' not in auth:
            abort(401)
        user_data = auth.get('Authorization')
        token = user_data.split('Bearer ')[-1]
        print(f'hi - {token}')
        result_check_token = user_service.get_information_by_user(token)
        print(f"check - {result_check_token}")
        if not result_check_token:
            abort(401)

        return result_check_token

    # def post(self):
    #     try:
    #         new_user = request.json
    #         error_auth(new_user)
    #         return user_service.add_user(new_user)
    #     except NotUsername :
    #         return "Нет имени"
    #     except NotPassword:
    #         return "Нет пароля"
    #     except NotRole:
    #         return "Нет пользователя"
    #     except NotFavorit_genre:
    #         "Нет понравившегося жанра"

    def patch(self):
        if "Authorization" not in request.headers:
            abort(403)
        data_token = request.headers.get('Authorization')
        token = data_token.split('Bearer ')[-1]
        result_check = user_service.get_information_by_user(token)
        if not result_check:
            abort(401)
        # data_token_user = request.json
        new_data_user = request.json
        result_update_user = user_service.paths_user_for_view(new_data_user,result_check)
        if not result_update_user:
            return 'Not update', 400
        return 'Yes update', 201

    def put(self):

        header = request.headers
        if 'Authorization' not in header:
            abort(401)
        data_from_header = header.get('Authorization')
        token = data_from_header.split('Bearer ')[-1]
        result_information_user = user_service.get_information_by_user(token)
        if not result_information_user:
            abort(401)
        passwords_user = request.json
        result_update_password_for_user = user_service.method_put_for_update_password_user(passwords_user,result_information_user)
        if not result_update_password_for_user:
            return 'Not update password', 400
        return 'Yes update password', 201




        # new_password = request.json



@users_ns.route('/<int:uid>')
class UsersViews(Resource):
    def get(self, uid):

        one_movie = user_schema.dump(user_service.get_one_user_by_id(uid))
        if not one_movie:
            return 'Not movie', 204
        return one_movie, 200

    def put(self, uid):
        result_put = request.json
        result_put['id'] = uid
        return user_service.update_user(result_put)

    # def patch(self, uid):
    #     result_patch = request.json
    #     result_patch['id'] = uid
    #     return user_service.patch_user(result_patch)

    def delete(self, uid):
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
