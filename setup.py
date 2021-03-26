from pathlib import Path

from mapper import create_app
from mapper.api.models import db
from mapper.common.get_ejscreen_data import run_etl

test_data = Path.cwd() / "tests" / "data" / "sample.geojson"


def create_local_db(app, path=test_data):
    with app.app_context():
        with db.engine.connect() as conn:
            conn.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
        db.drop_all()
        db.create_all()  # Create sql tables for our data models
        run_etl(test_data)  # populate with test data


if __name__ == "__main__":
    app = create_app()
    app.config["TESTING"] = True
    create_local_db(app)
