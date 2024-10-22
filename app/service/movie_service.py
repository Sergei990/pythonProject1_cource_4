# from app.DAO.models.movie import Movie
from app.DAO.movieDAO import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    # def all_movie(self):
    #     return self.dao.get_all_movie()
    def one_movie(self, mid):
        return self.dao.get_one_movie(mid)

    def movie_by_query(self, data):
        director_id = data.get('director_id')
        genre_id = data.get('genre_id')
        year = data.get('year')
        status = data.get('status')
        title = data.get('title')
        page = data.get('page')

        result = []
        if director_id is not None:
            result_by_director = self.dao.get_movie_by_director(director_id)
            # for movie in result_by_director:
            result.extend(result_by_director)
        if genre_id is not None:
            result_by_genre = self.dao.get_movie_by_genre(genre_id)
            # for genre in result_by_genre:
            #     result.append(genre)
            result.extend(result_by_genre)
            return result
            # result.extend(result_by_genre)
        # elif year is not None:
        #     result_by_year = self.dao.get_movie_by_year(year)
        #     for year in result_by_year:
        #         result.append(year)
        #     result.extend(result_by_year)
        elif title is not None:
            result_by_title = self.dao.get_movie_by_title(title)
            # result.extend(result_by_title)

        elif status is not None:
            result_by_new_movie = self.dao.get_new_movie()
            return result_by_new_movie
        elif  page is not None:
            result_page = self.dao.get_movie_by_paginate()
            return result_page

        else:
            return self.dao.get_all_movie()


    def add_movie(self, movie):

        return self.dao.add_movie(movie)
        # if not answer:
        #     return 'Фильм не добавлен', 400
        # return 'Фильм добавлен', 201

    def update_movie(self, data):
        filter = self.dao.get_one_movie(data.get('id'))
        filter.title = data.get('title')
        filter.description = data.get('description')
        filter.trailer = data.get('trailer')
        filter.year = data.get('year')
        filter.rating = data.get('rating')
        filter.genre_id = data.get('genre_id')
        filter.director_id = data.get('director_id')

        return self.dao.update_movie(filter)
        # if not answer:
        #     return 'Фильм не обновлен', 400
        # return 'Фильм обновлен', 201

    def delete_movie(self, did):
        movie_result_by_id = self.dao.get_one_movie(did)
        if not movie_result_by_id:
            return 'Not movie', 204

        return self.dao.delete(movie_result_by_id)
        # if not result:
        #     return ' not Delete'
        # return 'Фильм удален', 201
    def get_all_movie_for_lick(self, data):
        return self.dao.get_all_movie()