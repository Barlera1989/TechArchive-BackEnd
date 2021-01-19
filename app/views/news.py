from flask import Blueprint, request
from app.models.flask_models import News,Category, db, NewsSchema
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.http import build_api_response
from app.services.news_services import service_alter_news_information

bp_news = Blueprint('api_news', __name__, url_prefix='/news')
news_schema = NewsSchema()


@bp_news.route('/', methods=['GET'])
def get_all_news():
    all_news = News.query.all()
    news_list = [news_schema.dump(news) for news in all_news]
    return {
        'data': news_list
    }, HTTPStatus.OK


@bp_news.route('/<user_id>/<news_id>', methods=['GET'])
def get_news(user_id,news_id):
    filtered_news = News.query.filter_by(id=news_id).first() 
    news = news_schema.dump(filtered_news)
    return {
        'data': news
    }, HTTPStatus.OK


@bp_news.route('/<user_id>/create',methods=['POST'])
def create_news(user_id):
    data = request.get_json()
    news = News(
        title = data['title'],
        subtitle = data['subtitle'],
        content = data['content'],
        upvotes = data['upvotes'],
        downvotes = data['downvotes'],
        create_at = data['create_at'],
        approved = data['approved'],
        author = user_id
    )
    if "categories" in data:
        for category_id in list(data["categories"]):
            filtered_category = Category.query.filter_by(id=category_id).first()
            news.news_category.append(filtered_category) 
    db.session.add(news)
    db.session.commit()
    return {
        'data': f'{news}'
    }, HTTPStatus.OK

    

@bp_news.route('/<user_id>/<news_id>', methods=['DELETE'])
def delete_news(news_id):
    news = News.query.get_or_404(news_id)
    db.session.delete(news)
    db.session.commit()
    return {'news excluded'},HTTPStatus.OK


@bp_news.route('/<user_id>/<news_id>', methods=['PATCH'])
def patch_news(news_id):
    data = request.get_json()
    service_alter_news_information(news_id,data)
    return {'news altered'},HTTPStatus.OK
