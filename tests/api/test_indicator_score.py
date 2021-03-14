from mapper.models import db, IndicatorScore, Region


class TestIndicatorScoreModel:
    def test_add_indicator_score(self, client):
        # setup
        region_data = {"id": 1, "fips_code": "0000001", "state": "MD"}
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
        score = IndicatorScore.query.get(1)
        assert score.region.fips_code == "0000001"
        for k, v in score_data.items():
            actual = getattr(score, k)
            print(f"attr: {k}")
            print(f"expected: {v}")
            print(f"actual: {actual}")
            assert actual == v
