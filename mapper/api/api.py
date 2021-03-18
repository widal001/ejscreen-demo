from flask import Blueprint
from flask_restful import Api

from mapper.api.resources import Indicators, Regions

api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)

api.add_resource(Indicators, "/indicators")
api.add_resource(Regions, "/regions")
