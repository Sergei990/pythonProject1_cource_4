from unittest.mock import MagicMock

import pytest

from app.DAO.models.movie import Movie
from app.DAO.movieDAO import MovieDAO
from app.contener import movie_service
from app.service.movie_service import MovieService


@pytest.fixture()
def create_movie_for_test():
    movie = MovieDAO(None)

    movie_one = Movie(id=1,
                      title='title test one',
                      description='description test one',
                      trailer='trailer test one',
                      year=2001,
                      rating=1.1,
                      genre_id=1,
                      director_id=1
                      )
    movie_two = Movie(id=2,
                      title='title test two',
                      description='description test two',
                      trailer='trailer test two',
                      year=2002,
                      rating=2.2,
                      genre_id=2,
                      director_id=2)
    all_movie = [movie_one, movie_two]
    movie.add_movie = MagicMock(return_value=Movie(id=100))
    movie.get_one_movie = MagicMock(return_value=movie_one)
    movie.get_movie_by_director = MagicMock(return_value=all_movie)
    movie.get_movie_by_genre = MagicMock(return_value=all_movie)
    movie.get_all_movie = MagicMock(return_value=all_movie)
    movie.get_new_movie = MagicMock(return_value=[movie_two, movie_one])
    movie.update_movie = MagicMock(return_value=True)
    # if not movie_service.delete_movie(1):
    # movie.delete = MagicMock(return_value=False)
    # else:
    movie.delete = MagicMock(return_value=True)

    # movie.update_movie = MagicMock(return_value=False)
    # movie.get_movie_by_director = MagicMock(return_value=movie_one)
    # movie.add_movie = MagicMock(return_value=Movie(id=10))
    # movie.get_one_movie = MagicMock(returtn_value=False)
    return movie


class TestMovieService:
    @pytest.fixture(autouse=True)
    def config_movie_service(self, create_movie_for_test):
        self.movie_test = MovieService(dao=create_movie_for_test)

    def test_get_one_movie(self):
        result_by_one_movie = self.movie_test.one_movie(1)
        assert result_by_one_movie.id == 1
        assert result_by_one_movie is not None

    # @pytest.mark.xfail()
    # def test_get_one_movie_er(self):
    #     assert self.movie_test.one_movie(None).id ==1
    #     assert self.movie_test.one_movie(1) != False
    def test_create_movie(self):
        data = {'id': 100,
                'title': 'title test one',
                'description': 'description test one',
                'trailer': 'trailer test one',
                'year': 2001,
                'rating': 1.1,
                'genre_id': 1,
                'director_id': 1}
        result = self.movie_test.add_movie(data)
        assert result.id == 100

    # @pytest.mark.parametrize()
    def test_all_movie(self):
        data = {'director_id': 1,
                'genre_id': 2,
                'year_id': 2001,
                'status': 'new'}
        result = self.movie_test.movie_by_query(data)
        # for movie in result:
        assert result[0].director_id == 1
        assert result[1].genre_id == 2
        assert result[0].year == 2001
        # assert movie.year == 2001
        all = {}
        assert len(self.movie_test.movie_by_query(all)) > 0

    # @pytest.mark.parametrize()
    def test_new_movie(self):
        data = {'status': 'new'}
        movie_all = self.movie_test.movie_by_query(data)
        # for movie in movie_all:
        #     assert movie.year[0], movie.year == 2002,2001
        assert movie_all[0].year == 2002
        assert movie_all[1].year == 2001

    def test_update_movie(self):
        data = {'id': 1,
                'title': 'title test one',
                'description': 'description test one',
                'trailer': 'trailer test one',
                'year': 2001,
                'rating': 1.1,
                'genre_id': 1,
                'director_id': 1}
        result_update = self.movie_test.update_movie(data)
        # assert result_update.id == 1
        assert result_update == True

    def test_delete_movie(self):

        assert self.movie_test.delete_movie(1) == True

        # assert self.movie_test.delete_movie(None) == False

