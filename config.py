from environs import Env
from secrets import token_hex

env = Env()


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = token_hex(32)
    SECRET_KEY = token_hex(32)


class DevelopmentConfig(Config):
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://dev_q3:123456@172.29.150.47/techarchive'
    DEBUG = True


class TestingConfig(Config):
    ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_URI_TEST')
    TESTING = True


class ProductionConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_URI')
    JWT_SECRET_KEY = env.str('JWT_SECRET_KEY')
    SECRET_KEY = env.str('SECRET_KEY')

    config_selector = {

    }
