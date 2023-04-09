from marshmallow import Schema, fields

from schemas.base import UserRequestBase


class UserRegisterRequestSchema(UserRequestBase):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)


class UserLoginRequestSchema(UserRequestBase):
    pass
