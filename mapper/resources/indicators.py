from flask_restful import Resource


class Indicators(Resource):
    def get(self):
        return {"task": 'Say "Hello, World!"'}
