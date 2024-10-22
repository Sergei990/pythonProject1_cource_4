from os import abort

from flask import request
from flask_restx import Namespace, Resource, abort

from app.contener import genre_service, auth_user, access, genre_schema, genre_schemas

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenreView(Resource):
    # @admin_receiver
    def post(self):
        """

        :return:
        """
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers.get('Authorization')
        get_token = data.split('Bearer ')[-1]
        valid_token = auth_user.chek_token(get_token)
        if not valid_token:
            abort(401)
        elif valid_token.get('role') != 'admin':
            abort(403)

        query = request.json
        return genre_service.add_new_genre(query)


@genres_ns.route('/<int:gid>')
class GenreViewUD(Resource):

    def get(self, gid):
        """

        :param gid:
        :return:
        """
        return genre_schema.dump(genre_service.get_one_genre(gid)), 200

    def put(self, gid):
        """

        :param gid:
        :return:
        """
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers.get('Authorization')
        get_toke = data.split('Bearer ')[-1]
        valid_token = auth_user.chek_token(get_toke)
        if not valid_token:
            abort(401)
        elif valid_token.get('role') != 'admin':
            abort(403)
        query = request.json
        query['id'] = gid
        return genre_service.update_genre(query)

    def delete(self, gid):
        """

        :param gid:
        :return:
        """
        result = access.auth_required()
        if not result:
            return result
        return genre_service.delete_genre(gid)
