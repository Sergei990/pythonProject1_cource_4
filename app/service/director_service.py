from app.DAO.directorDAO import DirectorDAO


class DirectorService:
    def __init__(self, dao_director: DirectorDAO):
        self.dao_director = dao_director

    def get_all_directors(self):
        return self.dao_director.get_all_directors()

    def get_one_director_by_id(self,did):
        return self.dao_director.get_one_director(did)


    def create_director(self, new_director):
        result = self.dao_director.add(new_director)
        if not result:
            return " ", 400
        return " ", 201

    def update_director(self, data):

        result = self.dao_director.get_one_director(data.get('id'))
        if not result:
            return "Not", 204
        result.name = data.get('name')
        self.dao_director.update(result)

        return "Yes", 201

    def delete_director(self, did):

        result_director = self.dao_director.get_one_director(did)
        if not result_director:
            return "Not", 204

        result_delete = self.dao_director.delete(result_director)
        if not result_delete:
            return 'Not delete', 400
        return "Yes", 201
