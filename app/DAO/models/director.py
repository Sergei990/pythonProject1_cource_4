from sqlalchemy.orm import relationship
from marshmallow import Schema, fields
from configuration.database import db


class Director(db.Model):
    __tablename__ = 'director'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    movies = relationship('Movie', back_populates='directors')

class DirectorSchema(Schema):

    id = fields.Integer(dump_only=True)
    name = fields.String()