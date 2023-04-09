from datetime import datetime, timedelta

import jwt
from decouple import config
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.users import UserModel


class AuthManager:
    @staticmethod
    def create_user(user_data):
        user_data['password'] = generate_password_hash(user_data['password'])
        user = UserModel(**user_data)
        # Check if email exist
        email_in_db = UserModel.query.filter_by(email=user_data['email']).first()
        if email_in_db:
            raise BadRequest("Email already exist")
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login_user(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Invalid email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Invalid email or password")

        return user

    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=2)}
        return jwt.encode(payload, config("JWT_KEY"))
