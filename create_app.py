from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


db = SQLAlchemy(app)


def create_app(**config_overrides):

    app.config.from_pyfile("settings.py")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    # override the app used for testings purposes
    app.config.update(config_overrides)

    # import the blueprints
    from thread.views import thread_app
    from home.views import home_app
    from profile.views import profile_app

    # register the app blueprint
    app.register_blueprint(thread_app)
    app.register_blueprint(home_app)
    app.register_blueprint(profile_app)

    return app


