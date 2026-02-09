# import pytest
# from framework.data.data_loader import DataLoader
# from framework.base.base_test import BaseTest
# from framework.api.api_client import APIClient
# from framework.api.api_endpoints import APIEndpoints


# @pytest.mark.api
# class TestLoginAPI(BaseTest):

#     def test_login_success(self):
#         data = DataLoader.load_yaml("api_users.yaml")["valid_user"]
#         client = APIClient("https://reqres.in", self.logger)

#         response = client.post(APIEndpoints.LOGIN, json=data)

#         assert response.status_code == 200
#         assert "token" in response.json()

#     def test_login_failure(self):
#         data = DataLoader.load_yaml("api_users.yaml")["invalid_user"]
#         client = APIClient("https://reqres.in", self.logger)

#         response = client.post(APIEndpoints.LOGIN, json=data)

#         assert response.status_code == 400
#         assert "error" in response.json()
