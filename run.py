import time
from pathlib import Path

from sqlalchemy import inspect, exc

from setup import create_local_db
from mapper import create_app
from mapper.api.models import db, Indicator
from mapper.common.get_ejscreen_data import run_etl

test_data = Path.cwd() / "tests" / "data" / "sample.geojson"


def create_local_app():

    app = create_app()
    app.config["TESTING"] = True

    with app.app_context():
        for _ in range(25):
            try:
                inspector = inspect(db.engine)
                if "indicator" not in inspector.get_table_names():
                    print("Database is empty, populating database")
                    create_local_db(app)
                return app
            except exc.OperationalError as e:
                print("Waiting for database...")
                time.sleep(1)
                error = e
        raise error


if __name__ == "__main__":

    app = create_local_app()
    app.run(debug=True, host="0.0.0.0")
