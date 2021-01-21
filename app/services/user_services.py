from app.models.user_model import User, db
from app.services.http import build_api_response
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus


def serialize_user(user):
    return {
        'id': user.id,
        'name': user.name,
        'description': user.description,
        'email': user.email,
        'user_type': user.user_type,
        'create_at': user.create_at
    }


def serialize_user_list(user_list):
    return [serialize_user(user) for user in user_list]


def create_user(**kwargs):
    user = User(
        name=kwargs['name'],
        description=kwargs['description'],
        email=kwargs['email'],
        create_at=kwargs['create_at'],
        password=kwargs['password'],
        user_type=kwargs['user_type']
    )

    try:
        db.session.add(user)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)
    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)
