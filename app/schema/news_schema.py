from app.models import News


from flask_marshmallow import Marshmallow
ma = Marshmallow()


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
