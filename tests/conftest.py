import os
import tempfile
from pathlib import Path

import pytest

from mapper.app import create_app
from tests.populate_db import populate


@pytest.fixture(scope="function")
def client():

    # create a temporary database
    dir = Path.cwd() / "temp_dir"
    dir.mkdir(exist_ok=True)
    db_file, db_path = tempfile.mkstemp(dir=dir)
    uri = "sqlite:///" + db_path

    try:
        # create the app and
        app, db = create_app()
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = uri

        # create a test client and database for the app
        with app.test_client() as client:
            with app.app_context():
                db.create_all()
                populate(db)
                yield client

    except Exception as error:
        raise error

    finally:
        # close and delete the temp database
        os.close(db_file)
        os.unlink(db_path)
