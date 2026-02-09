from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def clear_login_form(self):
        self.driver.refresh()

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_login_successful(self):
        return "inventory" in self.driver.current_url

    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def get_error_message(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MSG)
            ).text
        except TimeoutException:
            self.logger.error("Login error message did not appear on UI")
            return None
