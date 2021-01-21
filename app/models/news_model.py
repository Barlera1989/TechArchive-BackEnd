from app.configs.database import SingletonSQLAlchemy
from app.models.news_category_model import news_category


db = SingletonSQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1024), unique=True, nullable=False)
    subtitle = db.Column(db.Text, unique=False, nullable=True)
    content = db.Column(db.Text, unique=True, nullable=False)
    upvotes = db.Column(db.Integer, default=0, unique=False, nullable=True)
    downvotes = db.Column(db.Integer, default=0, unique=False, nullable=True)
    create_at = db.Column(db.String, unique=False, nullable=True)
    approved = db.Column(db.Boolean, default=False, nullable=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    news_category = db.relationship('Category', secondary=news_category, lazy='subquery',
                                    backref=db.backref('news', lazy=True))

    def __repr__(self):
        return f'''<News id={self.id} title={self.title} subtitle={self.subtitle} 
                    author={self.author} content={self.content[:10]} 
                    upvotes={self.upvotes} downvotes={self.downvotes} 
                    create_at={self.create_at} approved={self.approved} >'''
