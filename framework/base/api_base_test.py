import pytest
from framework.config.config_loader import ConfigLoader
from framework.logger.logger import get_logger


class APIBaseTest:
    @classmethod
    def setup_class(cls):
        env_config = ConfigLoader.get_env_config()
        cls.logger = get_logger(env_config["log_level"])
