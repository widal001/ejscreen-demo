from mapper.models import Indicator

from mapper.common.ejscreen_columns import INDICATORS

indicators = {name: Indicator(**fields) for name, fields in INDICATORS.items()}


def populate(db):

    for indicator in indicators.values():
        db.session.add(indicator)

    db.session.commit()
