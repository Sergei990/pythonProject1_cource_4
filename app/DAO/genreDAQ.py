from app.DAO.models.genre import Genre


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_one_genre(self, gid):
        try:
            w=self.session.query(Genre).filter(Genre.id == gid).one()
            print(w)
            return w
        except Exception as error:
            print(error)
            return False

    def add_genre_DAO(self, new_genre):
        try:
            self.session.add(Genre(**new_genre))
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            print(e)
            return False

    def update_genre(self, data):
        try:
            self.session.add(data)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            return False

    def delete_genre(self, data_for_delete):
        try:
            self.session.delete(data_for_delete)
            self.session.commit()
            return True
        except Exception as r:
            self.session.rollback()
            print(r)
            return False
