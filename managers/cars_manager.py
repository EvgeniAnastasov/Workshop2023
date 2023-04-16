from werkzeug.exceptions import BadRequest

from db import db
from models import CarModel


class CarsManager:
    @staticmethod
    def create_car(car_data):
        car = CarModel(**car_data)
        # Check if car exist
        car_in_db = CarModel.query.filter_by(VIN=car_data['VIN']).first()
        if car_in_db:
            raise BadRequest("Car already exist")
        db.session.add(car)
        db.session.commit()

        return car


