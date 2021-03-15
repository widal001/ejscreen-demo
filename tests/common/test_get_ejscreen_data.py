import json
from pathlib import Path

from mapper.common.get_ejscreen_data import EJScreen


class TestInit:
    def test_success(self):
        # setup
        dir = Path.cwd() / "tests" / "data"
        src_file = dir / "source_geo.json"
        exp_file = dir / "filtered_geo.json"
        with open(exp_file) as f:
            expected = json.load(f)

        # execution
        etl = EJScreen(src_file)

        # validation
        assert etl.json == expected

    def test_missing_file(self):
        assert 1
