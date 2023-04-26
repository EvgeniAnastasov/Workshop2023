from models import CarModel, RoleType
from tests.base import TestRESTAPIBase, generate_token
from tests.factory import UserFactory
from tests.helper import test_car_data


class TestCars(TestRESTAPIBase):

    def test_required_fields_empty_raises(self):
        user = UserFactory(role=RoleType.mechanic)
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        data = {}
        res = self.client.post("/cars", headers=headers, json=data)

        assert res.status_code == 400
        assert res.json == {'message': {'VIN': ['Missing data for required field.'],
                                        'car_brand': ['Missing data for required field.'],
                                        'car_model': ['Missing data for required field.'],
                                        'year': ['Missing data for required field.']}}

    def test_add_car(self):
        cars = CarModel.query.all()
        assert len(cars) == 0

        user = UserFactory(role=RoleType.mechanic)
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        data = test_car_data
        res = self.client.post("/cars", headers=headers, json=data)

        cars = CarModel.query.all()
        assert len(cars) == 1
        assert res.status_code == 201
        assert res.json['VIN'] == 'TTTTTTTTTT0000000'
        assert res.json['car_brand'] == 'Test1'
        assert res.json['car_model'] == 'Test2'
        assert res.json['year'] == 1111
