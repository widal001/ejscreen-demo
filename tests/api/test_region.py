import pytest

from mapper.models import Region
from mapper.models import db


class TestRegionResource:
    def test_get_regions(self, client):

        # setup
        props = {"fips_code": "010010201001", "state": "AL"}

        # execute
        rv = client.get("/api/regions")
        region = rv.json["data"][0]

        # validate
        assert rv.status_code == 200
        assert region["id"] == 1
        assert region["properties"] == props
