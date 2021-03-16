import pytest
from sqlalchemy.exc import IntegrityError

from mapper.models import db, IndicatorScore, Region


class TestIndicatorScoreModel:
    def test_add_indicator_score(self, client):
        # setup
        region_data = {"id": 999, "fips_code": "0000001", "state": "MD"}
        score_data = {
            "id": 999,
            "indicator_id": 1,
            "year": 2020,
            "value": 10,
        }

        # execution
        region = Region(**region_data)
        score = IndicatorScore(**score_data)
        score.region = region

        db.session.add(region)
        db.session.add(score)
        db.session.commit()

        # validation
        score = IndicatorScore.query.get(999)
        assert score.region.fips_code == "0000001"
        for k, v in score_data.items():
            actual = getattr(score, k)
            print(f"attr: {k}")
            print(f"expected: {v}")
            print(f"actual: {actual}")
            assert actual == v

    def test_add_duplicate(self, client):
        # setup
        region_data = {"id": 999, "fips_code": "0000001", "state": "MD"}
        score_data = {
            "indicator_id": 1,
            "year": 2020,
            "value": 10,
        }

        # execution
        region = Region(**region_data)
        score = IndicatorScore(**score_data)
        score.region = region

        db.session.add(region)
        db.session.add(score)
        db.session.commit()

        # validation
        with pytest.raises(IntegrityError):
            score_data["value"] = 11
            score2 = IndicatorScore(**score_data)
            score2.region = region

            db.session.add(region)
            db.session.add(score2)
            db.session.commit()
