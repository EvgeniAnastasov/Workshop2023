from marshmallow import fields, ValidationError, validate

from schemas.base import UserRequestBase


def validate_name_start_with_capital_letter(name):
    if name:
        if not name[0].isupper():
            raise ValidationError('Name should starts with capital letter')


class UserRegisterRequestSchema(UserRequestBase):
    first_name = fields.String(
        required=True,
        validate=validate.And(validate.Length(min=3), validate_name_start_with_capital_letter))
    last_name = fields.String(
        required=True,
        validate=validate.And(validate.Length(min=3), validate_name_start_with_capital_letter))


class UserLoginRequestSchema(UserRequestBase):
    pass
