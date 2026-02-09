# from framework.config.config_loader import ConfigLoader
# from framework.logger.logger import get_logger
# from framework.drivers.driver_factory import DriverFactory


# class BaseTest:
#     @classmethod
#     def setup_class(cls):
#         env_config = ConfigLoader.get_env_config()

#         cls.logger = get_logger(env_config["log_level"])
#         cls.base_url = env_config["base_url"]
        
#         cls.driver = DriverFactory.create_driver(
#             browser=env_config["browser"],
#             headless=env_config["headless"]
#         )

#         cls.driver.get(cls.base_url)
#         cls.logger.info(f"Browser launched at {cls.base_url}")
#         cls.logger.info(f"Starting tests on {cls.base_url}")

#     @classmethod
#     def teardown_class(cls):
#         cls.driver.quit()
#         cls.logger.info("Browser closed")
#         cls.logger.info("Test execution completed")

import pytest


@pytest.mark.usefixtures("test_context")
class BaseTest:
    pass
