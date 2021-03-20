import json
from pathlib import Path

from shapely.geometry import shape

from mapper.api.models import db, Region, Indicator, IndicatorScore
from mapper.common.ejscreen_indicators import INDICATORS


def run_etl(file):
    try:
        load_indicators()
        features = extract_features(file)
        for f in features:
            load_feature(f)
    except FileNotFoundError as error:
        raise error


def extract_features(file):
    with open(file) as f:
        geo_json = json.load(f)
    return geo_json["features"]


def load_indicators(indicators=INDICATORS):
    for fields in INDICATORS.values():
        indicator = Indicator(**fields)
        db.session.add(indicator)
    db.session.commit()


def load_feature(feature):

    # get properties and indicators
    props = feature["properties"]
    geo = shape(feature["geometry"]).wkt
    fields = (Indicator.id, Indicator.source_name)
    indicators = db.session.query(Indicator).with_entities(*fields).all()

    # create region and scores

    region = Region(fips_code=props["ID"], geometry=geo, state=props["ST_ABBREV"])
    for id_, name in indicators:
        score = IndicatorScore(indicator_id=id_, value=props[name], year=2020)
        region.indicator_scores.append(score)

    # add records and commit session
    db.session.add(region)
    db.session.commit()
