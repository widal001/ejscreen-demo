from marshmallow import Schema, EXCLUDE, fields

# from sqlalchemy.ext.hybrid import hybrid_property

from mapper.api.models import db


class Indicator(db.Model):
    """Stores the unique list of indicators and metadata about those
    indicators like their source, description, and category
    """

    __tablename__ = "indicator"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    source = db.Column(db.String)
    source_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    # relationships
    scores = db.relationship(
        "IndicatorScore",
        back_populates="indicator",
        cascade="all, delete, delete-orphan",
    )


class IndicatorSchema(Schema):
    id = fields.Integer(dump_only=True)
    category = fields.String()
    source = fields.String()
    source_name = fields.String()
    description = fields.String()

    class Meta:
        unknown = EXCLUDE
