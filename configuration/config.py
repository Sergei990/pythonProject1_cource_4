
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    PWD_HASH_SALT = b'secret here'
    PWD_HASH_ITERATIONS = 100_000