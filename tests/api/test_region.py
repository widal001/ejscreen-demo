from mapper.models import Region
from mapper.models import db


class TestRegionModel:
    def test_add_region(self, client):
        # setup
        data = {
            "id": 999,
            "fips_code": "0000001",
            "state": "MD",
        }

        # execution
        region = Region(**data)
        db.session.add(region)
        db.session.commit()
        region = Region.query.get(999)

        print(region.census_level)

        # validation
        assert region is not None
        assert region.census_level == "block_group"
        for k, v in data.items():
            assert getattr(region, k) == v

        # validation - census_level setter
        region.census_level = "block_group"
        assert region.census_hierarchy == 10
