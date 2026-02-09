import os
from datetime import datetime


class ScreenshotUtil:

    @staticmethod
    def capture(driver, name="failure"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs("test_artifacts/screenshots", exist_ok=True)

        file_path = f"test_artifacts/screenshots/{name}_{timestamp}.png"
        driver.save_screenshot(file_path)

        return file_path
