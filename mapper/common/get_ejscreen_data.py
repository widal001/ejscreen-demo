import json
from pathlib import Path

from mapper.common.ejscreen_columns import INDICATORS


class EJScreen:
    def __init__(self, file):

        self.json = self._extract_json(file)

    def _extract_json(self, file):

        with open(file) as f:
            geo_json = json.load(f)

        return geo_json
