from marshmallow import Schema, fields


class CarsRequestSchema(Schema):
    VIN = fields.Str(required=True)
    car_brand = fields.Str(required=True)
    car_model = fields.Str(required=True)
    year = fields.Int(required=True)
