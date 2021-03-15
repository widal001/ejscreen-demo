import json
from pathlib import Path

from mapper.common.get_ejscreen_data import transform_and_load
from mapper.models import Region, Indicator, IndicatorScore


def test_transform_and_load(client):

    # setup
    file = Path.cwd() / "tests" / "data" / "source_geo.json"
    with open(file) as f:
        geo = json.load(f)
    feature = geo["features"][0]

    # execute
    transform_and_load(feature)
    region = Region.query.get(1)
    scores = region.indicator_scores

    # validate
    assert region is not None
    assert len(scores) == 18
    assert 0
