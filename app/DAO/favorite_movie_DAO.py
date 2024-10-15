from app.DAO.models.favorite_movie import FavoriteMovie
from app.DAO.models.movie import Movie


class FavoriteMovieDAO:

    def __init__(self, session):
        self.session = session

    def add_movie_for_favorite_movie(self, data):

        # try:
            self.session.add(FavoriteMovie(**data))
            self.session.commit()
            return True
        # except Exception as e:
        #     print(f'error Favorite movie DAO def add_movie {e}')
            # self.session.rollback()
            # return False

    def delete_movie_for_favorite_movie(self, data):

       try:
           self.session.delete(data)
           self.session.commit()
           return True
       except Exception as error:
           print(f'Error update_movie_for_favorite_movie {error}')
           self.session.rollback()
           return False

    # def get_all_lick_movie(self, user):
    #     result = self.session.query(FavoriteMovie).filter(FavoriteMovie.id_user == user).all()
    #     movie_list = []
    #     for item in result:
    #         movie = self.session.query(Movie).filter(Movie.id == item.id_movie).all()
    #     return movie
            # movie_list.append(movie)
        # return movie_list
    def get_useer_id(self, id_user):
        result_user_id = self.session.query(FavoriteMovie).filter(FavoriteMovie.id_user == id_user).all()
        return result_user_id
    def get_movie_by_id(self, movie):
        result_movie_id = self.session.query(Movie).filter(Movie.id == movie.id_movie).one()
        return result_movie_id