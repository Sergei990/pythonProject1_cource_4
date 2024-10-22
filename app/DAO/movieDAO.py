from datetime import datetime

from flask import current_app
from sqlalchemy import desc

from app.DAO.models.movie import Movie
from configuration.database import db


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def paginate_(self):
        self.page = current_app.config['PAGE']

    def get_all_movie(self):
        page = current_app.config['PAGE']
        print(page)
        pages = 1
        return self.session.query(Movie).all()

    def get_movie_by_paginate(self):
        result_ = db.paginate(db.select(Movie)).items
        print(result_)
        return result_

    def get_one_movie(self, mid):
        try:
            return self.session.query(Movie).filter(Movie.id == mid).one()
        except Exception as t:
            print(t)
            return False

    def get_movie_by_director(self, did):

        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_movie_by_genre(self, gid):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_movie_by_title(self, title):
        return self.session.query(Movie).filter(Movie.title.like(f'{title}%')).all()

    def get_movie_favorite_for_users(self, data):
        return self.session.query(Movie).filter(Movie.id == data).all()

    def get_new_movie(self, ):
        # r=self.session.query(Movie).order_by(desc(Movie.year)).all()
        return db.paginate(db.session.query(Movie).order_by(desc(Movie.year))).items

    def add_movie(self, data):
        try:
            with self.session.begin():
                self.session.add(Movie(**data))
                self.session.commit()
                return True
        except Exception:
            self.session.rollback()
            return False

    def update_movie(self, update_movie):
        try:
            self.session.add(update_movie)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False

    def delete(self, did):
        try:
            self.session.delete(did)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False

    def create_movie_for_test(self, data):
        """
        Метод для тестирования БД. Добавляет новый фильм, но не сохраняет его
        :param data: Словарь
        :return: Если фильм добавлен возвращает True
        """
        try:

            self.session.add(Movie(**data))
            return True
        except Exception as er:
            print(er)
            return False

    def update_movie_for_test(self, data):
        try:
            self.session.add(data)

            return True
        except Exception as er:
            print(er)
            return False
