import os
import uuid

from werkzeug.exceptions import BadRequest

from constants import TEMP_FILES_PATH
from db import db
from managers.auth_manager import auth
from models import RepairsModel, CarModel, RoleType
from services.firebase_service import FirebaseService
from utils.photo_decoder import decode_photo

firebase_service = FirebaseService()


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

        photo_name = f"{str(uuid.uuid4())}.{repair_data.pop('photo_extension')}"
        local_path_to_store_photo = os.path.join(TEMP_FILES_PATH, photo_name)
        photo_as_str = repair_data.pop('receipt_photo')
        decode_photo(local_path_to_store_photo, photo_as_str)

        # Upload photo to Firebase
        try:
            photo_firebase_url = firebase_service.upload_image(photo_name, local_path_to_store_photo)
        except Exception as ex:
            raise Exception("Upload to Firebase storage unsuccessful")
        finally:
            os.remove(local_path_to_store_photo)

        repair_data["receipt_photo"] = photo_firebase_url

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

    @staticmethod
    def update_repair(data, pk):
        RepairsModel.query.filter_by(id=pk).update(values=
                                                   {"VIN": data["VIN"],
                                                    "description": data["description"],
                                                    "amount": data["amount"],
                                                    "mileage": data["mileage"],
                                                    "receipt_photo": data["receipt_photo"]}
                                                   )
        db.session.commit()


role_mapper = {
    RoleType.mechanic: RepairManager.get_mechanic_repairs,
    RoleType.admin: RepairManager.get_all_repairs,
    RoleType.supervisor: RepairManager.get_all_repairs,
}
