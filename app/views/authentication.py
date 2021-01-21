from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from datetime import timedelta
from http import HTTPStatus
from app.services.user_services import create_user
from app.services.http import build_api_response
from app.models import User

bp_auth = Blueprint('auth', __name__)


@bp_auth.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if User.query.filter_by(email=email).first() is not None:
        filtered_user = User.query.filter_by(email=email).first()
        if User.checkPassword(filtered_user, password):
            access_token = create_access_token(
                identity=filtered_user.id, expires_delta=timedelta(days=14))
            return {'token': access_token}
        return build_api_response(HTTPStatus.UNAUTHORIZED)

    return build_api_response(HTTPStatus.FORBIDDEN)
