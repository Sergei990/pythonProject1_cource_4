from unittest.mock import MagicMock

import pytest

from app.DAO.models.movie import Movie
from app.service.movie_service import MovieService
from views.movies_views import MovieView, MovieOne


@pytest.fixture()
def create_movie_view_service():
    movie_view = MovieService
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
    movie_view.one_movie = MagicMock(return_value=movie_one)
    movie_view.movie_by_query = MagicMock(return_value=movie_one)
    movie_view.update_movie = MagicMock(return_value=True)
    movie_view.movie_by_query = MagicMock(return_value=[movie_one, movie_two])
    return movie_view


class TestMovieViewOne:
    @pytest.fixture(autouse=True)
    def create_view(self, create_movie_view_service):
        self.movie_view = MovieOne(create_movie_view_service)

    def test_one_movie(self):
        data = {'id': 1}
        result = self.movie_view.get(data)
        assert result.get('title') == 'title test one'
        assert result is not None

    #

class TestMovieViews:
    @pytest.fixture(autouse=True)
    def movie_one(self,create_movie_view_service):
        self.movie_view_one = MovieView(create_movie_view_service)

    def test_movie_by_query(self):
        data = {'director_id':1}

        result = self.movie_view_one.get()
        assert result is not None