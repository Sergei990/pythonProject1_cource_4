

from flask import request
from flask_restx import Namespace, Resource, abort

from app.DAO.error_auth_DAO import NotUsername, NotPassword, NotEmail, error_auth, NotTwoPassword
from app.contener import user_service, auth_user
# from dicoration_for_auth.dicorators import check_input_data_user

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class RegisterUser(Resource):
    # @check_input_data_user
    def post(self):
        try:
            query = request.json
            error_auth(query)
            new_user = user_service.add_user(query)
            return new_user
        except NotUsername:
            return 'Not name users'
        except NotPassword:
            return 'Not password'
        except NotEmail:
            return 'Not email'
        except NotTwoPassword:
            return "Не правильный вторй пароль"
@auth_ns.route('/login')
class UserLogin(Resource):
    # @admin_receiver
    def post(self):
        login_user = request.json

        # return user_service.cech_token(token)
        result_check_user = user_service.cech_user(login_user)
        if not result_check_user:
            return ' Not validation email or password'

        return result_check_user, 200

    def put(self):
        cricen_token = request.headers
        if 'Authorization' not in request.headers:
            abort(401)
        data = cricen_token.get('Authorization')
        token = data.split('Bearer ')[-1]

        result_check_token = user_service.check_token(token)
        if not result_check_token:
            abort(401)
        return result_check_token
