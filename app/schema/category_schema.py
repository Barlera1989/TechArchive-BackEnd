from app.models import Category


from flask_marshmallow import Marshmallow
ma = Marshmallow()


class CategorySchema(ma.SQLAlchemySchema):

    class Meta:
        model = Category

    id = ma.auto_field()
    name = ma.auto_field()
