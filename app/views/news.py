from flask import Blueprint, request
from app.models.flask_models import News, db, NewsSchema
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.http import build_api_response
import hashlib
from datetime import datetime
from pytz import timezone

bp_news = Blueprint('api_news', __name__, url_prefix='/news')
fuso_horario = timezone('America/Sao_Paulo')
news_schema = NewsSchema


@bp_news.route('/', methods=['GET'])
def get_all_news():
    all_news = News.query.all()
    news_list = [news_schema.dump(news) for news in all_news]
    return {
        'data': news_list
    }, HTTPStatus.OK


@bp_news.route('/<user_id>/<news_id>', methods=['GET'])
def get_news(news_id):
    filtered_news = News.query.filter_by(id=news_id).first()
    news = news_schema.dump(filtered_news)
    return {
        'data': news
    }, HTTPStatus.OK


@bp_news.route('/<user_id>/create')
def create_news(user_id):
    data = request.get_json()
    news = News(
        id = data['id'],
        title = data['title'],
        subtitle = data['subtitle'],
        content = data['content'],
        upvotes = data['upvotes'],
        downvotes = data['downvotes'],
        create_at = data['create_at'],
        approved = data['approved'],
        author = data['author']
    )
    try:
        db.session.add(news)
        db.session.commit()
        return {
            'data': news
        }, HTTPStatus.OK
    except:
        return {
            'data': news
        }, HTTPStatus.BAD_REQUEST
    

@bp_news.route('/<user_id>/<news_id>', methods=['DELETE'])
def delete_news(news_id):
    news = News.query.get_or_404(news_id)
    db.session.delete(news)
    db.session.commit()
    return {'news excluded'},HTTPStatus.OK


@bp_news.route('/<user_id>/<news_id>', methods=['PATCH'])
def patch_news(news_id):
    if News.query.filter_by(id=news_id).first() is not None:
        data = request.get_json()
        news = News.query.get(news_id)

        news.title = data['title'] if data.get(
            'title') else news.title

        news.subtitle = data['subtitle'] if data.get(
            'subtitle') else news.subtitle

        news.content = data['content'] if data.get(
            'content') else news.content

        news.upvotes = data['upvotes'] if data.get(
            'upvotes') else news.upvotes

        news.downvotes = data['downvotes'] if data.get(
            'downvotes') else news.downvotes

        news.create_at = data['create_at'] if data.get(
            'create_at') else news.create_at

        news.approved = data['approved'] if data.get(
            'approved') else news.approved

        news.author = data['author'] if data.get(
            'author') else news.author

        db.session.commit()
        
    return {'news excluded'},HTTPStatus.OK
