import json
from pathlib import Path

from mapper.models import db, Region, Indicator, IndicatorScore


def transform_and_load(feature):
    props = feature["properties"]

    region = Region(fips_code=props["ID"], state=props["ST_ABBREV"])

    q = db.session.query(Indicator).with_entities(Indicator.id, Indicator.source_name)
    indicators = q.all()

    for id_, name in indicators:
        score = IndicatorScore(
            indicator_id=id_,
            value=props[name],
            year=2020,
        )
        region.indicator_scores.append(score)

    db.session.add(region)
    db.session.commit()
