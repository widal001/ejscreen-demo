import dash
from flask import Flask
from flask.helpers import get_root_path
from flask_bootstrap import Bootstrap

from config import Config


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    if test_config:
        app.config.from_mapping(**test_config)
    else:
        app.config.from_object(Config)

    register_dashapps(app)
    register_blueprints(app)
    register_database(app)

    Bootstrap(app)

    return app


def register_dashapps(server):
    from mapper.dashboard.callbacks import layout
    from mapper.dashboard.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }

    assets = get_root_path(__name__) + "/dashboard/assets/"
    dashapp = dash.Dash(
        __name__,
        server=server,
        url_base_pathname="/mapper/",
        assets_folder=assets,
        meta_tags=[meta_viewport],
    )

    with server.app_context():
        dashapp.title = "Mapper"
        dashapp.layout = layout
        register_callbacks(dashapp)


def register_blueprints(server):
    from mapper import api
    from mapper import webapp

    server.register_blueprint(api.api_bp)
    server.register_blueprint(webapp.webapp_bp)


def register_database(server):
    from mapper.api.models import db

    db.init_app(server)
