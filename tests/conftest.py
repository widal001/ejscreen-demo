import pytest

from mapper.app import create_app


@pytest.fixture(scope="function")
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            yield client
