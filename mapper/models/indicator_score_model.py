from marshmallow import Schema, EXCLUDE, fields

from mapper.models import db


class IndicatorScore(db.Model):
    """Database table that stores the unique list of indicators and metadata
    about those indicators like their source, description, and category
    """

    __tablename__ = "indicator_score"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id"), nullable=False)
    indicator_id = db.Column(db.Integer, db.ForeignKey("indicator.id"), nullable=False)
    year = db.Column(db.Integer)
    value = db.Column(db.Float)

    # relationships
    region = db.relationship("Region", foreign_keys=region_id)
    indicator = db.relationship("Indicator", foreign_keys=indicator_id)

    # constraints
    __table_args__ = (
        db.UniqueConstraint("region_id", "indicator_id", "year", name="entry"),
    )


class IndicatorScoreSchema(Schema):
    id = fields.Integer(dump_only=True)
    region_id = fields.Integer()
    indicator_id = fields.Integer()
    year = fields.Integer()
    value = fields.Float()

    class Meta:
        unknown = EXCLUDE
