from selenium.webdriver.common.by import By
from framework.pages.base_page import BasePage


class ProductsPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_item_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)
