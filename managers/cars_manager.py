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

    @staticmethod
    def get_all_cars():
        return CarModel.query.filter_by().all()

    @staticmethod
    def get_single_car(pk):
        car = CarModel.query.filter_by(id=pk).first()
        if not car:
            raise BadRequest("No such a car")
        return car

    @staticmethod
    def update_car(data, pk):
        CarModel.query.filter_by(id=pk).update(values=
                                               {"VIN": data["VIN"],
                                                "car_brand": data["car_brand"],
                                                "car_model": data["car_model"],
                                                "year": data["year"],
                                                })
        db.session.commit()
