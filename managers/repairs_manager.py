from werkzeug.exceptions import BadRequest

from db import db
from managers.auth_manager import auth
from models import RepairsModel, CarModel


class RepairManager:
    @staticmethod
    def create_repair(repair_data):
        current_user = auth.current_user()
        repair_data["user_id"] = current_user.id

        vin = repair_data["VIN"]
        vin_in_car_db = CarModel.query.filter_by(VIN=vin).first()
        if not vin_in_car_db:
            raise BadRequest("Car with given VIN not in database. Please enter car data first.")
        car_id = vin_in_car_db.id
        repair_data["car_id"] = car_id

        repair = RepairsModel(**repair_data)
        db.session.add(repair)
        db.session.commit()

        return repair

