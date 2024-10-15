from app.DAO.favorite_movie_DAO import FavoriteMovieDAO
from app.service.auth_recvaer_service import AuthReceiverService


class FavoriteMovieService:

    def __init__(self, favorite_movie_dao: FavoriteMovieDAO, auth_service: AuthReceiverService):
        self.favorite_movie_dao = favorite_movie_dao
        self.auth_service = auth_service

    def add_favorite_movie(self, data):
        return self.favorite_movie_dao.add_movie_for_favorite_movie(data)

    def delete_favorite_movie(self, movie_id, user_id):

        get_user_id = self.favorite_movie_dao.get_useer_id(user_id)
        for user in get_user_id:

            if user.id_movie == movie_id:

                return self.favorite_movie_dao.delete_movie_for_favorite_movie(user)




    def check_token_for_favorite_movie(self, token):

        result_check_token = self.auth_service.chekc_token_authservice(token)
        return result_check_token

    def get_all_movie_lick(self, id_user):
        list_movie = []
        result_users_id = self.favorite_movie_dao.get_useer_id(id_user)
        for item in result_users_id:
            print(item)
            result_movie_id = self.favorite_movie_dao.get_movie_by_id(item)
            list_movie.append(result_movie_id)
        return list_movie



        # return self.favorite_movie_dao.get_all_lick_movie(movie)
        # return self.favorite_movie_dao.get_one_lick_movie(result)
