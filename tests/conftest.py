import os
import tempfile
from pathlib import Path

import pytest
from testing.postgresql import Postgresql

from mapper import create_app
from mapper.api.models import db
from tests.populate_db import populate


@pytest.fixture(scope="function")
def client():

    # create a temporary database
    with Postgresql() as postgresql:
        app = create_app()
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = postgresql.url()

        # create a test client and database for the app
        with app.test_client() as client:
            with app.app_context():
                # enables support for GeoAlchemy features
                with db.engine.connect() as conn:
                    conn.execute("CREATE EXTENSION postgis;")
                # adds test data
                db.create_all()
                populate(db)
                print("Populated DB")
                yield client
