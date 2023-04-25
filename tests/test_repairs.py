import os
from unittest.mock import patch

from constants import TEMP_FILES_PATH
from models import RoleType, RepairsModel
from services.firebase_service import FirebaseService
from tests.base import TestRESTAPIBase, generate_token, mock_uuid
from tests.factory import UserFactory
from tests.helper import test_input_data, test_car_data


class TestRepairsSchema(TestRESTAPIBase):
    def test_required_fields_empty_raises(self):
        user = UserFactory(role=RoleType.mechanic)
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        data = {}
        res = self.client.post("/repairs", headers=headers, json=data)

        assert res.status_code == 400
        assert res.json == {'message': {'VIN': ['Missing data for required field.'],
                                        'amount': ['Missing data for required field.'],
                                        'description': ['Missing data for required field.'],
                                        'mileage': ['Missing data for required field.'],
                                        'photo_extension': ['Missing data for required field.'],
                                        'receipt_photo': ['Missing data for required field.']}}

    def test_vin_is_lower_case_or_not_len17_or_both_raises(self):
        user = UserFactory(role=RoleType.mechanic)
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        data = test_input_data

        # Test VIN has lower case
        data["VIN"] = "AAAAAAAAAAAAAAAAa"
        res = self.client.post("/repairs", headers=headers, json=data)
        assert res.status_code == 400
        assert res.json == {'message': {'VIN': ['VIN should consist only capital letters and numbers']}}

        # Test with len(VIN)=16
        data["VIN"] = "AAAAAAAAAAAAAAAA"
        res = self.client.post("/repairs", headers=headers, json=data)
        assert res.status_code == 400
        assert res.json == {'message': {'VIN': ['Length must be between 17 and 17.']}}

        # Test with empty VIN
        data["VIN"] = ""
        res = self.client.post("/repairs", headers=headers, json=data)
        assert res.status_code == 400
        assert res.json == {'message': {'VIN': ['Length must be between 17 and 17.',
                                                'VIN should consist only capital letters and numbers']}}


class TestRepairs(TestRESTAPIBase):
    @patch("uuid.uuid4", mock_uuid)
    @patch.object(FirebaseService, "upload_image", return_value="some_url.com")
    def test_create_repair(self, mock_firebase_upload):
        repairs = RepairsModel.query.all()
        assert len(repairs) == 0

        user = UserFactory(role=RoleType.mechanic)
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        # Create car in database first!
        car_data = test_car_data
        self.client.post("/cars", headers=headers, json=car_data)

        data = test_input_data
        res = self.client.post("/repairs", headers=headers, json=data)

        repairs = RepairsModel.query.all()
        assert len(repairs) == 1
        assert res.status_code == 201
        assert res.json['VIN'] == 'TTTTTTTTTT0000000'
        assert res.json['amount'] == 9999.0
        assert res.json['description'] == 'test_desc'
        assert res.json['mileage'] == 8888
        assert res.json['receipt_photo'] == "some_url.com"

        expected_photo_name = f"{mock_uuid()}.{data['photo_extension']}"
        expected_file_path = os.path.join(TEMP_FILES_PATH, expected_photo_name)
        mock_firebase_upload.assert_called_once_with(expected_photo_name, expected_file_path)
