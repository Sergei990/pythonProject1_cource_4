from flask import Flask, request
from sqlalchemy.testing import fails

from configuration.config import Config
from configuration.database import db
from flask_restx import Api, abort

from views.auth_view import auth_ns
from views.director_view import directors_ns
from views.favorite_movie_views import favorites_ns
from views.genreview import genres_ns
from views.movies_views import movies_ns
from views.user_views import users_ns


def create(object):
    applications = Flask(__name__)
    applications.config.from_object(object)
    applications.app_context().push()
    return applications


def config_app(app):
    db.init_app(app)
    db.create_all()
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(users_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorites_ns)
# def conecst(app):

def create_table(app):
    with app.app_context():
        db.create_all()
        db.session.commit()
# print('is_ok')

def auth_required(func):
    def wrapper(*args, **kwargs):
        with app.app_context():
            if 'Authorization' not in request.headers:
                abort(401)
        return func(*args, **kwargs)
    return wrapper()
object = Config()
app = create(object)
config_app(app)
create_table(app)


if __name__ == '__main__':


    app.run()