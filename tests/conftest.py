from pytest import fixture

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from environs import Env

from app.configs.database import SingletonSQLAlchemy


@fixture(scope='session')
def engine():
    env = Env()
    return create_engine(env.str('DATABASE_URL_TEST'))


@fixture(scope='session')
def tables(engine):
    app = __import__('app').create_app('teste')
    app_ctx = app.app_context()
    app_ctx.push()
    db = SingletonSQLAlchemy()
    db.create_all()
    yield
    db.drop_all()
    app_ctx.pop()


@fixture
def db_session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@fixture
def app_client(autouse=True):
    with __import__('app').create_app('test').test_client() as client:
        return client


@fixture
def app_adapter(app_client):
    return app_client.application.url_map.bind('')
