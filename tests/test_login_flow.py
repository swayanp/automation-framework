from framework.base.base_test import BaseTest
from framework.pages.login_page import LoginPage
from framework.pages.products_page import ProductsPage


import pytest
import allure

@pytest.mark.sanity
class TestLoginFlow(BaseTest):
    
    @allure.title("Login with valid credentials should succeed")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self):
        login_page = LoginPage(self.driver, self.logger)
        login_page.login(self.username, self.password)

        products_page = ProductsPage(self.driver, self.logger)
        assert products_page.get_title() == "Product"
