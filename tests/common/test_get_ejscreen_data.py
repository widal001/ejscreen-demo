import json
from pathlib import Path

from geoalchemy2.functions import ST_AsGeoJSON

from mapper.common.ejscreen_indicators import INDICATORS
from mapper.api.models import db, Region, Indicator, IndicatorScore
from tests.data.indicator_scores import SCORES


def test_run_etl(client):

    # setup - json
    ejscreen_file = Path.cwd() / "tests" / "data" / "sample.geojson"
    expected_scores = SCORES["Block 1"]
    with open(ejscreen_file) as f:
        geo_json = json.load(f)
    expected_geom = geo_json["features"][0]["geometry"]

    # execute
    region = Region.query.get(1)
    scores = region.indicator_scores
    geom = json.loads(db.session.query(ST_AsGeoJSON(Region.geometry)).first()[0])

    # validate
    assert region is not None
    assert geom == expected_geom
    assert len(scores) == 18
    for score in scores:
        indicator = score.indicator.source_name
        assert expected_scores[indicator] == score.value
