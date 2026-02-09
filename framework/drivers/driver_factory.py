# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager


# class DriverFactory:

#     @staticmethod
#     def create_driver(browser: str, headless: bool):
#         if browser.lower() == "chrome":
#             options = Options()
#             if headless:
#                 options.add_argument("--headless=new")
#             options.add_argument("--start-maximized")
#             options.add_argument("--disable-gpu")
#             options.add_argument("--no-sandbox")

#             service = Service(ChromeDriverManager().install())
#             return webdriver.Chrome(service=service, options=options)

#         raise ValueError(f"Unsupported browser: {browser}")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:

    @staticmethod
    def create_driver(browser: str, headless: bool, incognito: bool = False):
        browser = browser.lower()

        if browser == "chrome":
            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            if incognito:
                options.add_argument("--incognito")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--headless=new")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")


            return webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif browser == "firefox":
            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            if incognito:
                options.add_argument("-private")

            return webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        elif browser == "edge":
            options = EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

            if incognito:
                options.add_argument("--inprivate")

            return webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )
