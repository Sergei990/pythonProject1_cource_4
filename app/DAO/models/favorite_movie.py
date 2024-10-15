

from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from app.DAO.models.movie import MovieSchema
from app.DAO.models.user import UserSchema
from configuration.database import db


class FavoriteMovie(db.Model):
    __tablename__ = 'favorite_movie'

    id = db.Column(db.Integer, primary_key=True)
    id_movie = db.Column(db.Integer, db.ForeignKey('movie.id'))
    # movies_ = relationship('Movie',back_populates='movie')
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    # users = relationship('User',back_populates='favorite_movies')

class FavoriteMovieSchema(Schema):

    id = fields.Integer(dump_only=True)
    id_movie = fields.Nested(MovieSchema)
    id_user = fields.Nested(UserSchema)