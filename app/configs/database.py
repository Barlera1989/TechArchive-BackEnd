from flask_sqlalchemy import SQLAlchemy, BaseQuery, Model
from flask import Flask


class Singleton(type):
    _instance_list = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance_list:
            new_instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instance_list[cls] = new_instance
        return cls._instance_list[cls]


class SingletonSQLAlchemy(SQLAlchemy, metaclass=Singleton):
    def __init__(self, app=None, use_native_unicode=True, session_options=None, metadata=None, query_class=BaseQuery, model_class=Model, engine_options=None):
        super().__init__(app=app, use_native_unicode=use_native_unicode, session_options=session_options,
                         metadata=metadata, query_class=query_class, model_class=model_class, engine_options=engine_options)


def get_sqlalchemy_instances():
    return SingletonSQLAlchemy()


def config_db(app: Flask, db: SQLAlchemy = get_sqlalchemy_instances()):
    db.init_app(app)
    app.db = db

    from app.models import News
    from app.models import Category
    from app.models import news_category
    from app.models import User
