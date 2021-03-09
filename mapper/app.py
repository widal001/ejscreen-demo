from flask import Flask

from mapper import api


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    SECRET_KEY = "dev"
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(api.bp)

    return app
