class ErrorUsername(Exception):
    pass


class NotUsername(Exception):
    pass


class NotPassword(Exception):
    pass


class NotRole(Exception):
    pass


class NotFavorit_genre(Exception):
    pass


class NotEmail(Exception):
    pass


class NotTwoPassword(Exception):
    pass


def error_auth(data):

    if not data.get('name'):
        # data["username"] = 'Введите имя'
        raise NotUsername(data)
    if not data.get('password'):
        # data["password"] = "Введите пароль"
        raise NotPassword(data)
    if not data.get('email'):

        # data["role"] = "Введите права пользования"
        raise NotEmail(data)
    if not data.get('favorite_genre'):

        raise NotFavorit_genre
    if data.get('password') != data.get('password_2'):
        raise NotTwoPassword