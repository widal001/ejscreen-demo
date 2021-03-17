import pytest
from sqlalchemy.exc import IntegrityError

from mapper.models import db, IndicatorScore, Region


class TestIndicatorScoreModel:
    def test_add_duplicate(self, client):
        # setup
        score_data = {
            "indicator_id": 1,
            "region_id": 1,
            "year": 2020,
            "value": 10,
        }

        # validation
        with pytest.raises(IntegrityError):
            score = IndicatorScore(**score_data)
            db.session.add(score)
            db.session.commit()
