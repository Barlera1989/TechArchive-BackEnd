from environs import Env
from app import create_app

env = Env()

application = create_app(env.str('FLASK_ENV'))


if __name__ == '__main__':
    application.run('0.0.0.0', port=5000)
