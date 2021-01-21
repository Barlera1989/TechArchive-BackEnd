from app.models import User


from flask_marshmallow import Marshmallow
ma = Marshmallow()


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
