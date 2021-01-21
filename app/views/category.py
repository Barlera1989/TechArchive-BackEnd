from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.news_model import db, News
from app.models.category_model import Category
from app.schema.category_schema import CategorySchema
from app.services.http import build_api_response
from app.services.news_services import service_alter_news_information

bp_category = Blueprint('api_category', __name__, url_prefix='/category')
category_schema = CategorySchema()


@bp_category.route('/')
def all_category():
    categories = Category.query.all()
    categories_list = [category_schema.dump(
        category) for category in categories]

    return {
        'data': categories_list
    }, HTTPStatus.OK


@bp_category.route('/create', methods=['POST'])
def create_category():
    data = request.get_json()

    category = Category(
        name=data['name'],
    )

    db.session.add(category)
    db.session.commit()
    return build_api_response(HTTPStatus.OK)
