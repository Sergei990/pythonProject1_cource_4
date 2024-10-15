# from argparse import Namespace

from flask import request
from flask_restx import Namespace, Resource, abort

# from app.DAO.dicoration_for_auth.password import auth_requi
from app.contener import movie_sterilisations, movie_service, auth_user, movie_sterilisation
from dicoration_for_auth.dicorators import auth_required

# from main import auth_required

# from dicoration_for_auth.password import auth_required

# from main import auth_required

movies_ns = Namespace('movies')


# @auth_required
@movies_ns.route('/')
class MovieView(Resource):

    def get(self):
        # auth = request.headers
        # if  'Authorization' not in auth:
        #     abort(401)
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        title = request.args.get('title')
        status = request.args.get('status')
        data = {
            'director_id': director_id,
            'genre_id': genre_id,
            'year': year,
            'title': title,
            'status': status
        }
        return movie_sterilisations.dump(movie_service.movie_by_query(data))

    # @auth_required
    def post(self):
        auth = request.headers
        if 'Authorization' not in auth:
            abort(401)
        data = request.headers.get('Authorization')
        token = data.split('Bearer ')[-1]
        answer = auth_user.chek_token(token)
        if not answer:
            abort(401)
        elif answer.get('role') != 'admin':
            abort(403)
        new_movie = request.json
        return movie_service.add_movie(new_movie)


@movies_ns.route('/<int:uid>')
class MovieOne(Resource):

    def get(self, uid):
        return movie_sterilisation.dump(movie_service.one_movie(uid))

    def put(self, uid):
        auth = request.headers
        if 'Authorization' not in auth:
            abort(401)
        data = auth.get('Authorization')
        token = data.split('Bearer ')[-1]
        answer = auth_user.chek_token(token)
        if not  answer:
            abort(401)
        # elif 'admin' != answer.get('role'):
        #     abort(403)
        update_movie = request.json
        update_movie['id'] = uid
        return movie_service.update_movie(update_movie)

    def delete(self, uid):
        auth = request.headers
        if 'Authorization' not in auth:
            print('not aut')
            abort(401)
        data = auth.get('Authorization')
        token = data.split('Bearer ')[-1]
        print(token)
        result = auth_user.chek_token(token)
        print(f'hi{result}')
        if not result:
            print('not token',result)
            abort(401)
        # if result.get('role') == 'admin':
        result_delete = movie_service.delete_movie(uid)
        if not result_delete:
            return 'Not movie', 204
        return 'Movie delete', 201
            # abort(403)
