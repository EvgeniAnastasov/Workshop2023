from datetime import datetime

from db import db


class CarModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    VIN = db.Column(db.String(100), nullable=False, unique=True)
    car_brand = db.Column(db.String(20), nullable=False)
    car_model = db.Column(db.String(20), nullable=False)
    year = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
