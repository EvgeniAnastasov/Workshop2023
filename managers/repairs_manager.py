from werkzeug.exceptions import BadRequest

from db import db
from managers.auth_manager import auth
from models import RepairsModel, CarModel, RoleType


class RepairManager:
    @staticmethod
    def create_repair(repair_data):
        current_user = auth.current_user()
        repair_data["user_id"] = current_user.id

        # Check if car exist in database:
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

    @staticmethod
    def get_repairs():
        current_user = auth.current_user()
        role = current_user.role
        repairs = role_mapper[role]()
        return repairs

    @staticmethod
    def get_mechanic_repairs():
        current_user = auth.current_user()
        return RepairsModel.query.filter_by(user_id=current_user.id).all()

    @staticmethod
    def get_all_repairs():
        return RepairsModel.query.filter_by().all()

    @staticmethod
    def delete_repair(pk):
        repair = RepairsModel.query.filter_by(id=pk).first()
        if not repair:
            raise BadRequest("No such a repair.")
        db.session.delete(repair)
        db.session.commit()

    @staticmethod
    def get_single_repair(pk):
        repair = RepairsModel.query.filter_by(id=pk).first()
        if not repair:
            raise BadRequest("No such a repair.")
        return repair


role_mapper = {
    RoleType.mechanic: RepairManager.get_mechanic_repairs,
    RoleType.admin: RepairManager.get_all_repairs,
    RoleType.supervisor: RepairManager.get_all_repairs,
}
