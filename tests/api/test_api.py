from tests.data.indicators_data import INDICATORS


def test_get_indicators(client):
    """Start with a blank database."""
    # setup
    expected = list(INDICATORS.values())
    # execution
    rv = client.get("/api/indicators")
    # validation
    assert rv.status_code == 200
    assert rv.json["data"] == expected
