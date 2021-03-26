import os

from sqlalchemy import inspect
from testing.postgresql import Postgresql

from mapper import create_app
from mapper.api.models import db, Indicator
from setup import create_local_db


def test_create_local_db():
    """Tests create_local_db() for expected behavior:
    - All of the tables are created
    - The tables created are populated with test data
    """

    # setup - create app
    tables = ["indicator", "region", "indicator_score"]

    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("UNITTEST_DB")
    with app.app_context():
        # setup - confirm db is empty
        db.drop_all()
        inspector = inspect(db.engine)
        assert "indicator" not in inspector.get_table_names()

        # execution
        create_local_db(app)
        inspector = inspect(db.engine)
        indicator = Indicator.query.get(1)

        # validation
        for table in tables:
            assert table in inspector.get_table_names()
        assert indicator.source_name == "ACSTOTPOP"
