
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    PWD_HASH_SALT = b'secret here'
    PWD_HASH_ITERATIONS = 100_000
    PWD_SECRET = '1234'
    JWT_ALGO = 'HS256'
    JWT_SECRET = '0987'
    PAGE = 12