from flask import request
from flask_restx import Namespace, Resource, abort
# from pycparser.ply.yacc import token

from app.contener import director_service, auth_user, director_schemas, director_schema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorView(Resource):

    def get(self):
        return director_schemas.dump(director_service.get_all_directors()), 200

    def post(self):
        query = request.json
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers.get('Authorization')
        get_token = data.split('Bearer ')[-1]
        valid_token = auth_user.chek_token(get_token)
        if not valid_token:
            abort(401)
        elif valid_token.get('rola') != 'admin':
            abort(403)
        return director_service.create_director(query)


@directors_ns.route('/<int:did>')
class DirectorSearcher(Resource):
    def get(self, did):
        result_by_director_id = director_schema.dump(director_service.get_one_director_by_id(did))
        if not result_by_director_id:
            return "", 204
        return director_schema.dump(result_by_director_id), 200

    def put(self, did):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers.get('Authorization')
        get_token = data.split('Bearer ')[-1]
        valid_token = auth_user.chek_token(get_token)
        if not valid_token:
            abort(401)
        elif valid_token.get('role') != 'admin':
            abort(403)
        update = request.json
        update['id'] = did
        return director_service.update_director(update)

    def delete(self, did):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers.get('Authorization')
        get_token = data.split('Bearer ')[-1]
        valid_token = auth_user.chek_token(get_token)
        if not valid_token:
            abort(401)
        elif valid_token.get('role') != 'admin':
            abort(403)
        return director_service.delete_director(did)
