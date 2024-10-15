from unittest.mock import MagicMock

import pytest
from sqlalchemy import True_

from app.DAO.models.movie import Movie
from app.DAO.movieDAO import MovieDAO
from app.contener import movie_dao
from app.service.movie_service import MovieService
from configuration.database import db
from main import app


# @pytest.fixture()
# def movie_dao_config():
#     movie = MovieDAO(None)
#     movie_one = Movie(id=1,
#                       title='title test one',
#                       description='description test one',
#                       trailer='trailer test one',
#                       year=2001,
#                       rating=1.1,
#                       genre_id=1,
#                       director_id=1
#                       )
#     movie_two = Movie(id=2,
#                       title='title test two',
#                       description='description test two',
#                       trailer='trailer test two',
#                       year=2002,
#                       rating=2.2,
#                       genre_id=2,
#                       director_id=2)
#     movie.add_movie = MagicMock(return_value=True)
#     return movie


# @pytest.fixture()
class TestMovieDAO:
    @pytest.fixture(autouse=True)
    def config_for_test(self):
        self.movie = MovieDAO(db.session)

    def test_one_movie(self):
        # with app.app_context():
        result = self.movie.get_one_movie(7)
        print(result)
        assert result.id == 7
        assert self.movie.get_one_movie(None) == False

    def test_all_movie(self):
        result = self.movie.get_all_movie()
        assert len(result) > 0

    def test_get_movie_by_director_id(self):
        result_by_id_director = self.movie.get_movie_by_director(3)
        for item in result_by_id_director:
            assert item.director_id == 3
            assert item.director_id != 5

    def test_get_movie_by_genre_id(self):
        result_by_id_genre = self.movie.get_movie_by_genre(7)
        for item in result_by_id_genre:
            assert item.genre_id == 7
            assert item.genre_id != 10

    def test_get_movie_by_year(self):
        result_get_movie_by_year = self.movie.get_movie_by_year(2000)
        for movie in result_get_movie_by_year:
            assert movie.year == 2000

    def test_get_movie_by_new(self):

        result_new_movie = self.movie.get_new_movie()
        assert len(result_new_movie) > 0
        assert type(result_new_movie) == list

    def test_movie_add(self):
        data = {
            'title': 'title test one',
            'description': 'description test one',
            'trailer': 'trailer test one',
            'year': 2001,
            'rating': 1.1,
            'director_id': 1,
            'genre_id': 1
            }

        #
        assert self.movie.create_movie_for_test(data) == True
        # print(result_add)
        # assert result_add == True

    def test_movie_update(self):

        data = Movie(id=1,
                     title='title test one',
                     description='description test one',
                     trailer='trailer test one',
                     year=2001,
                     rating=1.1,
                     genre_id=1,
                     director_id=1
                     )
        assert self.movie.update_movie_for_test(data) == True

