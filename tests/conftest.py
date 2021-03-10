import os
import tempfile

import pytest

from mapper.app import create_app


@pytest.fixture(scope="function")
def client():

    # create the app and
    app, db = create_app()
    app.config["TESTING"] = True

    # create a temporary database
    db_file, app.config["DATABASE"] = tempfile.mkstemp()

    # create a test client and database for the app
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

    # close and delete the temp database
    os.close(db_file)
    os.unlink(app.config["DATABASE"])
