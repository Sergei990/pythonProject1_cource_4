

from flask import request
from flask_restx import Namespace, Resource, abort

from app.contener import favorite_movie_for_user_service, movie_service, movie_sterilisations, \
    favorite_movie_for_user_schemas, user_schema, user_schemas, auth_user
from dicoration_for_auth.dicorators import admin_receiver

favorites_ns = Namespace('favorites/movies')


@favorites_ns.route('/<int:movie_id>')
class FavoriteMovieView(Resource):

    def post(self,movie_id):
        get_token = request.headers
        if 'Authorization' not in get_token:
            abort(401)
        data_token = get_token.get('Authorization')
        token = data_token.split('Bearer ')[-1]
        # data_movie = request.json
        result_check_token = favorite_movie_for_user_service.check_token_for_favorite_movie(token)
        if not result_check_token:
            abort(401)
        print(movie_id)
        result_searhs_movie = movie_service.one_movie(movie_id)
        if not result_searhs_movie:
            return ' Not movie', 204
        data_movie = {
            "id_movie":movie_id,
            "id_user":result_check_token.get('id')
        }
        print(data_movie)
        result_add_like_movie = favorite_movie_for_user_service.add_favorite_movie(data_movie)
        if not result_add_like_movie:
            return ' Not add movie', 400
        return "Yes add movie ", 201

    def delete(self, movie_id):

        header = request.headers
        if 'Authorization' not in header:
            abort(401)
        data_token = header.get('Authorization')
        token = data_token.split('Bearer ')[-1]
        result_check_token = auth_user.chekc_token_authservice(token)
        if not result_check_token:
            abort(403)
        id_user = result_check_token.get('id')
        result = favorite_movie_for_user_service.delete_favorite_movie(movie_id,id_user)
        if not result:
            return 'Not delete', 204
        return ',', 201



@favorites_ns.route("/")
class ReadeFavoriteMovie(Resource):
    def get(self):
        result_header_for_get_movie = request.headers

        if 'Authorization' not in result_header_for_get_movie:
            abort(401)
        data = result_header_for_get_movie.get('Authorization')
        result_user = data.split('Bearer ')[-1]
        if not result_user:
            abort(401)

        result_check_token = favorite_movie_for_user_service.check_token_for_favorite_movie(result_user)
        if not result_check_token:
            abort(401)
        # print(result_check_token)
        result_search_user = result_check_token.get('id')
        # print(result_search_user)
        result_movies = favorite_movie_for_user_service.get_all_movie_lick(result_search_user)
        print(result_movies)
        # print(result_movies, result_search_user)
        # result_movies_from_table = movie_service.
        return movie_sterilisations.dump(result_movies)

