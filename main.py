import docker
from flask import Flask, request
from sqlalchemy.testing import fails

from configuration.config import Config
from configuration.database import db
from flask_restx import Api, abort, cors
from flask_cors import CORS
from views.auth_view import auth_ns
from views.director_view import directors_ns
from views.favorite_movie_views import favorites_ns
from views.genreview import genres_ns
from views.movies_views import movies_ns
from views.user_views import users_ns


def create(object):
    """

    :param object:
    :return:
    """
    applications = Flask(__name__)
    applications.config.from_object(object)
    applications.app_context().push()
    return applications


def config_app(app):
    """

    :param app:
    """
    db.init_app(app)

    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(users_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorites_ns)
object = Config()
app = create(object)
config_app(app)

if __name__ == '__main__':

    app.run()
