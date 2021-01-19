from flask import Blueprint, request
from app.services.user_services import create_user
from flask_jwt_extended import create_access_token
from app.models.flask_models import User
from datetime import timedelta
from app.services.http import build_api_response
from http import HTTPStatus

bp_auth = Blueprint('auth', __name__, url_prefix='/')


@bp_auth.route('/login', methods=['POST'])
def login():

    email = request.json.get('email')
    password = request.json.get('password')

    getdata = User.query.all()

    for i in range(len(getdata)):
        if email == getdata[i].email:

            if password == getdata[i].password:
                access_token = create_access_token(
                    identity=getdata[i].id, expires_delta=timedelta(days=7))
                return {'token': access_token}

            return build_api_response(HTTPStatus.UNAUTHORIZED)

    return build_api_response(HTTPStatus.FORBIDDEN)
