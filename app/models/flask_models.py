from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()


news_category = db.Table(
    'news_category',
    db.Column('news_id', db.Integer, db.ForeignKey('news.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    create_at = db.Column(db.String, unique=False, nullable=True)
    password = db.Column(db.String(1024), unique=False, nullable=False)
    user_type = db.Column(db.String(50), default="Viewer",
                          unique=False, nullable=True)

    def __repr__(self):
        return f'''<User id={self.id} name={self.name} 
        description{self.description} email={self.email} 
        create_at={self.create_at} password={self.password} 
        user_type={self.user_type} >'''


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    subtitle = db.Column(db.String(500), unique=False, nullable=True)
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


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Category id={self.id} name={self.name} >'


class UserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    description = ma.auto_field()
    email = ma.auto_field()
    create_at = ma.auto_field()
    password = ma.auto_field()
    user_type = ma.auto_field()


class NewsSchema(ma.SQLAlchemySchema):

    class Meta:
        model = News

    id = ma.auto_field()
    title = ma.auto_field()
    subtitle = ma.auto_field()
    content = ma.auto_field()
    upvotes = ma.auto_field()
    downvotes = ma.auto_field()
    create_at = ma.auto_field()
    approved = ma.auto_field()
    author = ma.auto_field()


class CategorySchema(ma.SQLAlchemySchema):

    class Meta:
        model = Category

    id = ma.auto_field()
    name = ma.auto_field()
