from marshmallow import fields

from schemas.base import RepairsBaseSchema


class RepairResponseSchema(RepairsBaseSchema):
    id = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
    user_id = fields.Integer(required=True)
    car_id = fields.Integer(required=True)
