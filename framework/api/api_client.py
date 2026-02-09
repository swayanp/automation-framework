import requests
import allure
import json
import json as json_lib


class APIClient:

    def __init__(self, base_url, logger):
        self.base_url = base_url
        self.logger = logger

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET {url}")
        response = requests.get(url, params=params, headers=headers)
        allure.attach(
            json.dumps(response.json(), indent=2),
            name=f"GET {endpoint} Response",
            attachment_type=allure.attachment_type.JSON
        )        
        return response

    def post(self, endpoint, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST {url}")

        response = requests.post(url, json=json, headers=headers)

        allure.attach(
            json_lib.dumps(response.json(), indent=2),
            name=f"POST {endpoint} Response",
            attachment_type=allure.attachment_type.JSON
        )

        return response
