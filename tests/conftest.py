import os
import tempfile
from pathlib import Path

import pytest
from testing.postgresql import Postgresql

from setup import create_local_db
from mapper import create_app
from mapper.api.models import db
from tests.populate_db import populate


@pytest.fixture(scope="function")
def client():

    # create a temporary database
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("UNITTEST_DB")

    # create a test client and database for the app
    with app.test_client() as client:
        with app.app_context():
            create_local_db(app)
            print("Populated DB")
            yield client
