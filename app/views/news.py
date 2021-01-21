from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.news_model import db, News
from app.models.category_model import Category
from app.models.news_category_model import news_category
from app.schema.news_schema import NewsSchema
from app.services.http import build_api_response
from app.services.news_services import service_alter_news_information
from datetime import datetime
from pytz import timezone

fuso_horario = timezone('America/Sao_Paulo')
bp_news = Blueprint('api_news', __name__, url_prefix='/news')
news_schema = NewsSchema()


@bp_news.route('/', methods=['GET'])
def get_all_news():
    all_news = News.query.all()
    news_list = [news_schema.dump(news) for news in all_news]
    return {
        'data': news_list
    }, HTTPStatus.OK


@bp_news.route('/<news_id>', methods=['GET'])
def get_news(news_id):
    filtered_news = News.query.filter_by(id=news_id).first()
    news = news_schema.dump(filtered_news)
    return {
        'data': news
    }, HTTPStatus.OK


@bp_news.route('/create', methods=['POST'])
@jwt_required
def create_news():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        news = News(
            title=data['title'],
            subtitle=data['subtitle'],
            content=data['content'],
            upvotes=data['upvotes'],
            downvotes=data['downvotes'],
            approved=data['approved'],
            create_at=datetime.now(
            ).astimezone(fuso_horario).strftime('%d/%m/%Y %H:%M:%S'),
            author=user_id
        )
        if "categories" in data:
            for category_id in list(data["categories"]):
                filtered_category = Category.query.filter_by(
                    id=category_id).first()
                news.news_category.append(filtered_category)
        db.session.add(news)
        db.session.commit()
        return {
            'data': news_schema.dump(news)
        }, HTTPStatus.OK

    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_news.route('/<news_id>', methods=['DELETE'])
@jwt_required
def delete_news(news_id):
    user_id = get_jwt_identity()

    if News.query.filter_by(id=news_id).first() is not None:
        news = News.query.get_or_404(news_id)
        db.session.delete(news)
        db.session.commit()

    else:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return build_api_response(HTTPStatus.OK)


@bp_news.route('/<news_id>', methods=['PATCH'])
@jwt_required
def patch_news(news_id):
    user_id = get_jwt_identity()
    data = request.get_json()

    if News.query.filter_by(id=news_id).first() is not None:
        service_alter_news_information(news_id, data)

    else:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return build_api_response(HTTPStatus.OK)
