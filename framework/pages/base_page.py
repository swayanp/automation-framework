from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os


class BasePage:
    def __init__(self, driver, logger, timeout=10):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        self.logger.debug(f"Clicking on {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.logger.debug(f"Typing '{text}' into {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    # def capture_debug_artifacts(self, name):
    #     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #     os.makedirs("debug_artifacts", exist_ok=True)

    #     screenshot_path = f"debug_artifacts/{name}_{timestamp}.png"
    #     source_path = f"debug_artifacts/{name}_{timestamp}.html"

    #     self.driver.save_screenshot(screenshot_path)
    #     with open(source_path, "w", encoding="utf-8") as f:
    #         f.write(self.driver.page_source)

    #     self.logger.error(f"Screenshot saved: {screenshot_path}")
    #     self.logger.error(f"Page source saved: {source_path}")
