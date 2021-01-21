from flask import Flask


def config_views(app: Flask):
    from .news import bp_news
    app.register_blueprint(bp_news)

    from .user import bp_users
    app.register_blueprint(bp_users)

    from .authentication import bp_auth
    app.register_blueprint(bp_auth)

    from .category import bp_category
    app.register_blueprint(bp_category)
