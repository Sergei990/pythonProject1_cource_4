import base64
import datetime
import hashlib
import calendar
import hmac
from time import timezone

import jwt

from configuration.constante import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET, JWT_ALGO


class AuthReceiverService:
    """Для генерации токена и пароля"""

    def generation_password(self, password):
        """
        Возвращает хешированный пароль
        :param password: пароль переданный пользователем
        :return: хешированный пароль
        """
        password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('UTF-8'),
                                            PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        return base64.b64encode(password_hash)

    def check_password(self, password_user, password_bd):
        """
        Проверка пароля пользователя  и бд
        :param password_user: пароль переданный пользователем
        :param password_bd: пароль находящийся в базе данных
        :return: bool
        """
        result = base64.b64decode(password_bd)
        password_hash = hashlib.pbkdf2_hmac('sha512', password_user.encode('UTF-8'),
                                            PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        return hmac.compare_digest(password_hash, result)

    def generation_access_token(self, data):
        """
        Генерирует, asses  token
        :param data: отдает данные Имя, роль
        :return: токен
        """
        min_1 = datetime.datetime.utcnow() + datetime.timedelta(minutes=55)
        data['exp'] = calendar.timegm(min_1.timetuple())
        print(min_1)
        return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

    def generation_refresh_token(self, data):
        """
        генерирует refresh token
        :param data: Принимает имя, роль
        :return: возвращает refresh token
        """
        day_300 = datetime.datetime.utcnow() + datetime.timedelta(days=59)
        data['exp'] = calendar.timegm(day_300.timetuple())
        return jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGO)

    def chekc_token_authservice(self, data):
        """
        проверяет токен на ликвидность
        :param data: принимает токен
        :return: если токен ликвидный возвращает словарь с данными если нет то FAlse
        """
        try:
            # print(f"check auth- {data}")
            result_decode_token = jwt.decode(data, JWT_SECRET, algorithms=[JWT_ALGO])
            # print(f" token_servise - {result_decode_token}")
            return result_decode_token
        except Exception as e:
            print(f" except - {e}")
            return False
