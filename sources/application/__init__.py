from flask import Flask
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Set app context for database
    database.init_app(app)

    with app.app_context():
        from . import routes

        # Create tables in database if they do not exist
        database.create_all()

        return app
