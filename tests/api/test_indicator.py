from mapper.common.ejscreen_columns import INDICATORS


class TestIndicatorsResource:
    def test_get_indicators(self, client):
        """Tests that 'api/indicators' returns the correct response body"""
        # setup
        expected = list(INDICATORS.values())
        # execution
        rv = client.get("/api/indicators")
        # validation
        assert rv.status_code == 200
        assert rv.json["data"] == expected
