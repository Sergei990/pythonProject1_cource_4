from app.DAO.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all_user(self):
        """

        :return: Возвращает список словарей
        """
        return self.session.query(User).all()

    def get_user_one(self, uid):
        """

        :param uid: Получает id пользователя
        :return: Возвращает словарь с одним пользователем
        """
        try:
            return self.session.query(User).filter(User.id == uid).one()
        except Exception:
            return False

    def add_user(self, data):
        """ Добавляет пользователя в БД

        :param data: Получат словарь
        :return: возвращает True если пользователь добавлен, или false если пользователь не добавлен
        """
        try:
            with self.session.begin():
                self.session.add(User(**data))
                self.session.commit()
                return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def update_user(self, new_user):

        try:
            self.session.add(new_user)
            self.session.commit()
            return True
        except Exception as error:
            self.session.rollback()
            print(f" update user - {error}")
            return False

    def delete_user_by_id(self, delete_user):
        try:
            self.session.delete(delete_user)
            self.session.commit()
            return True
        except Exception as r:
            self.session.rollback()
            print(r)
            return False

    def get_all_user_by_name(self, name):

        return self.session.query(User).filter(User.username == name).all()

    def get_user_by_email(self, email):
        try:
            result_user_by_email = self.session.query(User).filter(User.email == email).one()
            return result_user_by_email
        except Exception as e:
            return False
