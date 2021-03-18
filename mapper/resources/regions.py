import json

from flask_restful import Resource
from geoalchemy2.functions import ST_AsGeoJSON

from mapper.models import db, Region


def format_row(col):
    entry = {
        "type": "Feature",
        "id": col[0],
        "properties": {"fips_code": col[1], "state": col[2]},
        "geometry": json.loads(col[3]),
    }
    return entry


class Regions(Resource):
    def get(self):
        """Returns a list of regions and their metadata

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
        geom = ST_AsGeoJSON(Region.geometry)
        fields = (Region.id, Region.fips_code, Region.state, geom)
        q = db.session.query(Region).with_entities(*fields)
        result = [format_row(x) for x in q.all()]
        return {"status": "success", "data": result}, 200
