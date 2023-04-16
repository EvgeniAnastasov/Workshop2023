from marshmallow import fields

from schemas.base import RepairsBaseSchema


class RepairsResponseSchema(RepairsBaseSchema):
    id = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
