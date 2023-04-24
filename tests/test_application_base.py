from models import RoleType
from tests.base import TestRESTAPIBase, generate_token
from tests.factory import UserFactory


class TestLoginRequired(TestRESTAPIBase):
    def test_auth_required(self):
        auth_required_urls = [
            ("GET", "/repairs"),
            ("POST", "/repairs"),
            ("GET", "/repair/1"),
            ("PUT", "/repair/1"),
            ("DELETE", "/repair/1"),
            ("GET", "/cars"),
            ("POST", "/cars"),
            ("GET", "/car/1"),
            ("PUT", "/car/1"),
        ]

        for method, url in auth_required_urls:
            if method == "GET":
                res = self.client.get(url)
            elif method == "POST":
                res = self.client.post(url)
            elif method == "PUT":
                res = self.client.put(url)
            else:
                res = self.client.delete(url)

            assert res.status_code == 401
            assert res.json == {'message': 'Invalid or missing token'}

    def test_edit_car_permission_required(self):
        user = UserFactory(role=RoleType.mechanic)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.put("/car/1", headers=headers)

        assert res.status_code == 403
        assert res.json == {'message': 'You do not have permission to access this resource'}

    def test_get_put_repair_permission_required(self):
        user = UserFactory(role=RoleType.mechanic)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}
        urls = [
            ("GET", "/repair/1"),
            ("PUT", "/repair/1"),
        ]

        for method, url in urls:
            if method == "GET":
                res = self.client.get(url, headers=headers)
            else:
                res = self.client.put(url, headers=headers)

            assert res.status_code == 403
            assert res.json == {'message': 'You do not have permission to access this resource'}

    def test_delete_repair_permission_required(self):
        user = UserFactory(role=RoleType.mechanic)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.delete("/repair/1", headers=headers)

        assert res.status_code == 403
        assert res.json == {'message': 'You do not have permission to access this resource'}

        user = UserFactory(role=RoleType.supervisor)
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}"}

        res = self.client.delete("/repair/1", headers=headers)

        assert res.status_code == 403
        assert res.json == {'message': 'You do not have permission to access this resource'}
