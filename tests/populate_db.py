from mapper.models.indicator import Indicator

from tests.data.indicators_data import INDICATORS

indicators = {name: Indicator(**fields) for name, fields in INDICATORS.items()}


def populate(db):

    for indicator in indicators.values():
        print(indicator.source_name)
        db.session.add(indicator)

    db.session.commit()
