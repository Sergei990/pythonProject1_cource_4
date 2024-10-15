from enum import unique

from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from configuration.database import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    # username = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    # role = db.Column(db.String)
    favorite_genre = db.Column(db.String)
    # favorite_movie_id = db.Column(db.Integer, db.ForeignKey('favorite_movie.id'))
    # favorite_movies = relationship("FavoriteMovie", back_populates='favorite_movies')
    # movies = db.Column(db.Integer)
    # movies = relationship('FavoriteMovie', backref='users')


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    favorite_genre = fields.String()
    # role = fields.String()
