from pathlib import Path

from mapper.common.get_ejscreen_data import run_etl

ejscreen_file = Path.cwd() / "tests" / "data" / "sample.geojson"


def populate(db):

    run_etl(ejscreen_file)
