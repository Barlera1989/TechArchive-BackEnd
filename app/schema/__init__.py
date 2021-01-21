from flask_marshmallow import Marshmallow
from flask import Flask


def config_serializer(app:Flask):
    Marshmallow(app)