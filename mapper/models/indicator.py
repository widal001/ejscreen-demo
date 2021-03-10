from marshmallow import Schema, EXCLUDE, fields

from mapper.app import db


class Indicator(db.Model):
    """Database table that stores the unique list of indicators and metadata
    about those indicators like their source, description, and category
    """

    __tablename__ = "indicators"

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    source = db.Column(db.String)
    source_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)


class IndicatorsSchema(Schema):
    id = fields.Integer(dump_only=True)
    category = fields.String()
    source = fields.String()
    source_name = fields.String()
    description = fields.String()

    class Meta:
        unknown = EXCLUDE
