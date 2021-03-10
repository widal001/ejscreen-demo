from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from mapper import api
from mapper.config import Config

db = SQLAlchemy()


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # register the api blueprint
    app.register_blueprint(api.bp)

    # initialize the database
    db.init_app(app)

    return app, db
