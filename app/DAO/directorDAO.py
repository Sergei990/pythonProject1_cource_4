from app.DAO.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all()

    def get_one_director(self, did):
        """
        В
        :param did: integer получаем id
        :return: возвращаем одного режиссера по его id
         если нет в таблице возвращаем False
        """
        try:
            return self.session.query(Director).filter(Director.id == did).one()

        except Exception:
            return False

    def add(self, data):
        """
        Добавляет нового режиссера в таблицу
        :param data: данные нового режиссера
        :return: Возвращает True если успешно добавлен режиссер, и False если режиссер не добавлен
        """
        try:
            self.session.add(Director(**data))
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False

    def update(self, update_director):
        """
        Изменяет данные о режиссере
        :param update_director: Новые данные режиссера
        :return: Возвращает True если данные изменены и False если произошла ошибка
        """
        try:
            self.session.add(update_director)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False

    def delete(self, delete_director):
        """
        удаляет режиссера
        :param delete_director: integer,
        :return: возвращает True если режиссер удален и False если произошла ошибка
        """
        try:
            self.session.delete(delete_director)
            self.session.commit()
            return True
        except Exception:
            return False
