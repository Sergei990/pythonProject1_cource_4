
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from app.DAO.models.director import DirectorSchema
from app.DAO.models.genre import GenreSchema
from app.DAO.models.user import UserSchema
from configuration.database import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genres = relationship('Genre', back_populates='movies')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    directors = relationship('Director', back_populates='movies')
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # users = relationship('User', back_populates='movies')
    # favorite_movie_id = db.Column(db.Integer, db.ForeignKey('favorite_movie.id'))
    # users = relationship('FavoriteMovie', backref='movies')
    # movies_ = relationship('FavoriteMovie', back_populates=

class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    genre_id = fields.Nested(GenreSchema)
    director_id = fields.Nested(DirectorSchema)
    user_id = fields.Nested(UserSchema)
