import pytest
from datetime import datetime

from framework.config.config_loader import ConfigLoader
from framework.drivers.driver_factory import DriverFactory
from framework.logger.logger import get_logger

import pytest
from framework.utils.screenshot_utils import ScreenshotUtil


@pytest.fixture(scope="function")
def test_context(request):
    """
    Class-scoped fixture responsible for:
    - Loading environment configuration
    - Initializing logger
    - Creating & closing browser
    - Injecting shared test context into test classes
    """

    # ----------------------------
    # Load environment configuration
    # ----------------------------
    env_config = ConfigLoader.get_env_config()
    env_name = env_config.get("env_name", "unknown")

    # ----------------------------
    # Initialize logger
    # ----------------------------
    logger = get_logger(env_config["log_level"])

    logger.info("=" * 80)
    logger.info("TEST EXECUTION STARTED")
    logger.info(f"Environment      : {env_name}")
    logger.info(f"Base URL         : {env_config['base_url']}")
    logger.info(f"Browser          : {env_config['browser']}")
    logger.info(f"Headless Mode    : {env_config['headless']}")
    logger.info(f"Start Time       : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 80)

    # ----------------------------
    # Create browser
    # ----------------------------
    driver = DriverFactory.create_driver(
        browser=env_config["browser"],
        headless=env_config["headless"],
        incognito=env_config.get("incognito", False)
    )

    logger.info("Browser instance created successfully")

    # ----------------------------
    # Navigate to application
    # ----------------------------
    driver.get(env_config["base_url"])
    logger.info(f"Navigated to URL : {env_config['base_url']}")

    # ----------------------------
    # Inject context into test class
    # ----------------------------
    request.cls.driver = driver
    request.cls.logger = logger
    request.cls.base_url = env_config["base_url"]

    # Optional credentials (if present)
    request.cls.username = env_config.get("username")
    request.cls.password = env_config.get("password")

    # ----------------------------
    # Yield control to tests
    # ----------------------------
    yield

    # ----------------------------
    # Teardown (always executed)
    # ----------------------------
    logger.info("-" * 80)
    logger.info("TEST EXECUTION FINISHED")
    logger.info(f"End Time         : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    driver.quit()
    logger.info("Browser closed successfully")
    logger.info("=" * 80)

import allure
from framework.utils.screenshot_utils import ScreenshotUtil

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item.cls, "driver", None)
        logger = getattr(item.cls, "logger", None)

        if driver:
            screenshot_path = ScreenshotUtil.capture(
                driver,
                name=item.name
            )
            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="UI Screenshot on Failure",
                    attachment_type=allure.attachment_type.PNG
                )
            if logger:
                logger.error(f"Screenshot captured: {screenshot_path}")