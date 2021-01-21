import hashlib

from app.configs.database import SingletonSQLAlchemy


db = SingletonSQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    create_at = db.Column(db.String, unique=False, nullable=True)
    password = db.Column(db.String(1024), unique=False, nullable=False)
    user_type = db.Column(db.String(50), default="Viewer",
                          unique=False, nullable=True)

    def checkPassword(user, password):
        crypto_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if crypto_pass == user.password:
            return True
        return False

    def __repr__(self):
        return f'''<User id={self.id} name={self.name} 
        description{self.description} email={self.email} 
        create_at={self.create_at} password={self.password} 
        user_type={self.user_type} >'''
