from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from configuration.database import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    movies = relationship('Movie', back_populates='genres')


class GenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
