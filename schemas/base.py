from marshmallow import Schema, fields, validate, ValidationError
from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    uppercase=1,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=1,  # need min. 1 special characters
)


def validate_password(value):
    errors = policy.test(value)
    if errors:
        raise ValidationError(f"Not a valid password. "
                              f"Password should contain at least 1 capital letter, 1 digit and 1 special symbol")


class UserRequestBase(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True,
                             validate=validate.And(validate.Length(min=5, max=20), validate_password))


def validate_vin_is_capital_letters(vin):
    if not vin.isupper():
        raise ValidationError('VIN should consist only capital letters and numbers')


class CarsBaseSchema(Schema):
    VIN = fields.Str(
        required=True,
        validate=validate.And(validate.Length(min=17, max=17), validate_vin_is_capital_letters))

    car_brand = fields.Str(required=True, validate=validate.Length(min=1))
    car_model = fields.Str(required=True, validate=validate.Length(min=1))
    year = fields.Int(required=True)


class RepairsBaseSchema(Schema):
    VIN = fields.Str(
        required=True,
        validate=validate.And(validate.Length(min=17, max=17), validate_vin_is_capital_letters))

    description = fields.Str(required=True, validate=validate.Length(min=3))
    amount = fields.Float(required=True)
    mileage = fields.Int(required=True)
    receipt_photo = fields.Str(required=True)
    photo_extension = fields.Str(required=True)
