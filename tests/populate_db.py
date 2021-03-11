from mapper.models.indicator_model import Indicator

from tests.data.indicators_data import INDICATORS

indicators = {name: Indicator(**fields) for name, fields in INDICATORS.items()}


def populate(db):

    for indicator in indicators.values():
        db.session.add(indicator)

    db.session.commit()
