from flask_restful import Resource

from mapper.models.indicator_model import Indicator, IndicatorSchema


class Indicators(Resource):
    def get(self):
        """Returns a list of indicators and their metadata

        Endpoint: GET api/indicators

        Response:
            200: {
                "status": "success",
                "data": [{
                    "id": 1,
                    "category": "demographic",
                    "source": "EJScreen",
                    "source_name": "ACSTOTPOP",
                    "description": "Total population",
                }]
            }
        """
        schema = IndicatorSchema(many=True)
        programs = Indicator.query.all()
        result = schema.dump(programs)
        return {"status": "success", "data": result}, 200
