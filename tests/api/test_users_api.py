import pytest
from framework.base.api_base_test import APIBaseTest
from framework.api.api_client import APIClient
from framework.api.api_endpoints import APIEndpoints


@pytest.mark.api
class TestUsersAPI(APIBaseTest):

    def test_get_users(self):
        client = APIClient("https://dummyjson.com", self.logger)
        response = client.get(APIEndpoints.USERS, params={"page": 2})

        assert response.status_code == 200
        assert "users" in response.json()

from framework.data.data_loader import DataLoader


@pytest.mark.api
class TestLoginAPI(APIBaseTest):

    def test_login_success(self):
        data = DataLoader.load_yaml("api_users.yaml")["valid_user"]
        client = APIClient("https://dummyjson.com", self.logger)

        response = client.post(APIEndpoints.LOGIN, json=data)

        assert response.status_code == 200
        assert "token" in response.json()

    def test_login_failure(self):
        data = DataLoader.load_yaml("api_users.yaml")["invalid_user"]
        client = APIClient("https://dummyjson.com", self.logger)

        response = client.post(APIEndpoints.LOGIN, json=data)

        assert response.status_code == 400
        assert "message" in response.json()
        assert response.json()["message"] == "Invalid credentials"
