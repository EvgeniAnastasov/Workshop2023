from marshmallow import Schema, fields, validate, ValidationError


class UserRequestBase(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


def validate_vin_is_capital_letters(vin):
    if not vin.isupper():
        raise ValidationError('VIN should consist only capital letters and numbers')


class CarsBaseSchema(Schema):
    VIN = fields.Str(
        required=True,
        validate=validate.And(validate.Length(min=17, max=17), validate_vin_is_capital_letters))

    car_brand = fields.Str(required=True)
    car_model = fields.Str(required=True)
    year = fields.Int(required=True)


class RepairsBaseSchema(Schema):
    VIN = fields.Str(
        required=True,
        validate=validate.And(validate.Length(min=17, max=17), validate_vin_is_capital_letters))
    description = fields.Str(required=True)
    amount = fields.Float(required=True)
    mileage = fields.Int(required=True)
    receipt_photo = fields.Str(required=True)
    photo_extension = fields.Str(required=True)
