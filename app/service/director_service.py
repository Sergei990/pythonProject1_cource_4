from app.DAO.directorDAO import DirectorDAO


class DirectorService:
    def __init__(self, dao_director: DirectorDAO):
        self.dao_director = dao_director

    def get_all_directors(self):
        """

        :return: Возвращает список словарей режиссеров
        """
        return self.dao_director.get_all_directors()

    def get_one_director_by_id(self,did):
        """

        :param did: Integer id режиссера
        :return: возвращает словарь
        """
        return self.dao_director.get_one_director_DAO(did)


    def create_director(self, new_director):
        result = self.dao_director.add_new_director_DAO(new_director)
        if not result:
            return " ", 400
        return " ", 201

    def update_director(self, data):

        result = self.dao_director.get_one_director_DAO(data.get('id'))
        if not result:
            return "Not", 204
        result.name = data.get('name')
        self.dao_director.update_director_DAO(result)

        return "Yes", 201

    def delete_director(self, did):

        result_director = self.dao_director.get_one_director_DAO(did)
        if not result_director:
            return "Not director", 204

        result_delete = self.dao_director.delete_director_DAO(result_director)
        if not result_delete:
            return 'Not delete', 400
        return "Yes", 201
