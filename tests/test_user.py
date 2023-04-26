from tests.base import TestRESTAPIBase
from tests.helper import test_user_data


class TestUsersSchema(TestRESTAPIBase):
    def test_required_fields_empty_raises(self):
        data = {}
        res = self.client.post("/register", json=data)

        assert res.status_code == 400
        assert res.json == {'message': {'email': ['Missing data for required field.'],
                                        'first_name': ['Missing data for required field.'],
                                        'last_name': ['Missing data for required field.'],
                                        'password': ['Missing data for required field.']}}

    def test_first_name_and_last_name_start_with_lower_raises(self):
        data = test_user_data

        data['first_name'] = "ivan"
        res = self.client.post("/register", json=data)
        assert res.status_code == 400
        assert res.json == {'message': {'first_name': ['Name should starts with capital letter']}}

        data['first_name'] = "Ivan"
        data['last_name'] = "ivanov"
        res = self.client.post("/register", json=data)
        assert res.status_code == 400
        assert res.json == {'message': {'last_name': ['Name should starts with capital letter']}}
