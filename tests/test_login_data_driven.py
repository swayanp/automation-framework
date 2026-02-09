import pytest
from framework.base.base_test import BaseTest
from framework.pages.login_page import LoginPage
from framework.pages.products_page import ProductsPage
from framework.data.data_loader import DataLoader


@pytest.mark.regression
class TestLoginDataDriven(BaseTest):

    @pytest.mark.parametrize(
        "user",
        DataLoader.load_yaml("login_users.yaml")["valid_users"]
    )
    def test_valid_login(self, user):
        login_page = LoginPage(self.driver, self.logger)
        login_page.login(user["username"], user["password"])

        products_page = ProductsPage(self.driver, self.logger)
        assert products_page.get_title() == "Products"

    @pytest.mark.parametrize(
        "user",
        DataLoader.load_yaml("login_users.yaml")["invalid_users"]
    )
    def test_invalid_login(self, user):
        login_page = LoginPage(self.driver, self.logger)
        login_page.login(user["username"], user["password"])

        actual_error = login_page.get_error_message()
        expected_error = user["expected_error"]

        self.logger.info("=" * 60)
        self.logger.info(f"INVALID LOGIN TEST")
        self.logger.info(f"Username        : '{user['username']}'")
        self.logger.info(f"Expected error  : '{expected_error}'")
        self.logger.info(f"Actual error    : '{actual_error}'")
        self.logger.info("=" * 60)

        assert actual_error is not None, "Error message was not displayed on UI"
        assert expected_error in actual_error, (
            f"Expected error '{expected_error}' "
            f"but got '{actual_error}'"
        )
