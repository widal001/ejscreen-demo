from mapper.common.ejscreen_indicators import INDICATORS
from mapper.models import db, Region, Indicator, IndicatorScore
from tests.data.indicator_scores import SCORES


def test_run_etl(client):

    # setup - json
    expected_scores = SCORES["Block 1"]

    # execute
    region = Region.query.get(1)
    scores = region.indicator_scores

    # validate
    assert region is not None
    assert len(scores) == 18
    for score in scores:
        indicator = score.indicator.source_name
        assert expected_scores[indicator] == score.value
