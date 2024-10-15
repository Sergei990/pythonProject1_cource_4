# from app.service.auth_recvaer_service import AuthReceiverDAO
from app.DAO.directorDAO import DirectorDAO
from app.DAO.favorite_movie_DAO import FavoriteMovieDAO
from app.DAO.genreDAQ import GenreDAO
from app.DAO.models.director import DirectorSchema
from app.DAO.models.favorite_movie import FavoriteMovie, FavoriteMovieSchema
from app.DAO.models.genre import GenreSchema
# from app.DAO.models.genre import Genre
from app.DAO.models.movie import MovieSchema
from app.DAO.models.user import UserSchema
from app.DAO.movieDAO import MovieDAO
from app.DAO.userDAO import UserDAO
from app.service.auth_recvaer_service import AuthReceiverService
from app.service.director_service import DirectorService
from app.service.favorite_movie_service import FavoriteMovieService
from app.service.genre_service import GenreService
from app.service.movie_service import MovieService
from app.service.user_service import UserService
from configuration.config import Config
from configuration.database import db
from dicoration_for_auth.dicorators import Access

movie_dao = MovieDAO(db.session)
confi_password = Config
# get_password = Password(confi_password)
movie_service = MovieService(movie_dao)
user_dao = UserDAO(db.session)
auth_user = AuthReceiverService()
user_service = UserService(user_dao, auth_user)
user_schemas = UserSchema(many=True)
user_schema = UserSchema()
director_schemas = DirectorSchema(many=True)
director_schema = DirectorSchema()
movie_sterilisations = MovieSchema(many=True)
movie_sterilisation = MovieSchema()
director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
access = Access(auth_user)
genre_schemas = GenreSchema(many=True)
genre_schema = GenreSchema()
# favorite_movie=FavoriteMovie()
favorite_movie_for_user_DAO = FavoriteMovieDAO(db.session)
favorite_movie_for_user_service = FavoriteMovieService(favorite_movie_for_user_DAO, auth_user)
favorite_movie_for_user_schemas = FavoriteMovieSchema(many=True)