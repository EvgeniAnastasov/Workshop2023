from marshmallow import fields

from schemas.base import CarsBaseSchema


class CarsResponseSchema(CarsBaseSchema):
    id = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
