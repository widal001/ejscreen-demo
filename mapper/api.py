from flask import Flask, Blueprint
from flask_restful import Api

from mapper.resources.indicators import Indicators
from mapper.resources.regions import Regions

bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(bp)

api.add_resource(Indicators, "/indicators")
api.add_resource(Regions, "/regions")
