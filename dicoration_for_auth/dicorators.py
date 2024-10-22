import jwt
# from flask import request, current_app
#
# from flask_restx import abort
#
# from configuration.constante import JWT_SECRET, JWT_ALGO
# from flask import current_app
#
# from main import app
#
from flask import request
from flask_restx import abort

# from app.contener import auth_user
# from configuration.constante import JWT_SECRET, JWT_ALGO


# from main import app


# from main import app


# from main import app


# from main import context, app


# from main import app


# from main import app


def admin_receiver(func):
    def wrapper(*args, **kwargs):

        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        role = None
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
            role = user.get('role', 'admin')
        except Exception:
            abort(401)
        if role != 'admin':
            abort(403)
        return func(*args, **kwargs)
    return wrapper()
#
def auth_required(func):
    def wrapper(*args, **kwargs):
        # with app.app_context():
        token = request.headers
        if not token:
            abort(401)
        return func(*args,**kwargs)
    return wrapper()

class Authentication:

    # def __init__(self, headers):
    #
    #     self.headers = headers

    def auth_user(self,data):
        if 'Authentication' not in data:
            abort(401)

# with app.test_request_context()

class Access:
    def __init__(self, auth_user):
        self.auth_user = auth_user
    def auth_required(self):
        if 'Authorization' not in request.headers:
            abort(401)
        role = None
        data = request.headers.get('Authorization')
        get_token = data.split('Bearer ')[-1]
        valid_token = self.auth_user.chek_token(get_token)
        if not valid_token:
            abort(401)
        elif valid_token.get('role') != 'admin':
            abort(403)
        return True

def check_input_data_user(func):
    def wrapper( *args, **kwargs):
        data = request.json
        result = {}
        if  not data.get('email'):
            result['email'] = 'Not email'
        elif not data.get('password'):
            result['password'] = 'Not password'

        elif not data.get('name'):
            result['name'] = 'Npt name'

        return func(*args, **kwargs)
    return wrapper()
