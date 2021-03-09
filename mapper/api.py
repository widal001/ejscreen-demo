from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for

bp = Blueprint("api", __name__, url_prefix="/api/")
api = Api(bp)


class TodoItem(Resource):
    def get(self, id):
        return {"task": 'Say "Hello, World!"'}


api.add_resource(TodoItem, "/todos/<int:id>")
