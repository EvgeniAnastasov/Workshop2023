from db import db
from models import CarModel


class CarsManager:
    @staticmethod
    def create_car(car_data):
        car = CarModel(**car_data)
        db.session.add(car)
        db.session.commit()


