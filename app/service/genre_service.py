from app.DAO.genreDAQ import GenreDAO


class GenreService:

    def __init__(self, dao_genre: GenreDAO):

        self.dao_genre = dao_genre

    def get_one_genre(self,gid):

        answer_by_get_one_genre = self.dao_genre.get_one_genre(gid)
        print(answer_by_get_one_genre)
        if not answer_by_get_one_genre:
            return 'not genre', 204
        return answer_by_get_one_genre

    def add_new_genre(self, data_genre):

        result_add_genre = self.dao_genre.add_genre_DAO(data_genre)
        if not result_add_genre:
            return 'Not add', 400
        return 'Is ok', 201

    def update_genre(self, data_update_genre):

        result_search = self.dao_genre.get_one_genre(data_update_genre.get('id'))
        if not result_search:
            return 'Not genre', 204
        result_search.name = data_update_genre.get('name')
        result_update = self.dao_genre.update_genre(result_search)
        if not result_update:
            return "Not update", 400
        return 'Is ok', 201

    def delete_genre(self, gid):

        result_search = self.dao_genre.get_one_genre(gid)
        if not result_search:
            return 'Not genre', 204
        result_delete = self.dao_genre.delete_genre(result_search)
        if not result_delete:
            return 'Not delete', 400
        return "Delete genre", 200
