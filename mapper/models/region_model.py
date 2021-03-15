import enum

from marshmallow import Schema, EXCLUDE, fields
from sqlalchemy.ext.hybrid import hybrid_property

# from geoalchemy2 import Geometry

from mapper.models import db


class CensusHierarchy(enum.IntEnum):
    census_block = 0
    block_group = 10
    census_tract = 20
    county = 30
    state = 40
    division = 50
    region = 60
    nation = 70


class Region(db.Model):
    """Stores the unique list of regions and relatively stable metadata about
    those regions like their FIPS code, geometry, and level of Census hierarchy
    """

    __tablename__ = "region"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    fips_code = db.Column(db.String, nullable=False)
    census_hierarchy = db.Column(db.Integer, default=10)
    state = db.Column(db.String)

    # relationships
    indicator_scores = db.relationship(
        "IndicatorScore",
        back_populates="region",
        cascade="all, delete, delete-orphan",
    )

    # hybrid properties
    @hybrid_property
    def census_level(self):
        return CensusHierarchy(self.census_hierarchy).name

    @census_level.setter
    def census_level(self, level):
        print(level)
        self.census_hierarchy = CensusHierarchy[level].value


class RegionSchema(Schema):
    id = fields.Integer(dump_only=True)
    fips_code = fields.String()
    census_level = fields.String()
    state = fields.String()

    class Meta:
        unknown = EXCLUDE
