from app.configs.database import SingletonSQLAlchemy


db = SingletonSQLAlchemy()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Category id={self.id} name={self.name} >'
