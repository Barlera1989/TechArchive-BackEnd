from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from environs import Env
from secrets import token_hex
from app.configs import config_db
from app.views import config_views
from app.schema import config_serializer
from app.models.category_model import db


def create_app(config='production'):
    env = Env()
    env.read_env()

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')

    app.config['JWT_SECRET_KEY'] = token_hex(16)
    config_db(app)
    config_serializer(app)
    Migrate(app, db)

    JWTManager(app)

    config_views(app)

    return app
