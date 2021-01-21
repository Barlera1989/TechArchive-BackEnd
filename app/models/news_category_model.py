from app.configs.database import SingletonSQLAlchemy


db = SingletonSQLAlchemy()


news_category = db.Table(
    'news_category',
    db.Column('news_id', db.Integer, db.ForeignKey('news.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)
