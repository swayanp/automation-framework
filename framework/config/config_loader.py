import os
import yaml
import re


class ConfigLoader:
    _config = None

    @classmethod
    def load_config(cls):
        if cls._config is None:
            with open("framework_config.yaml", "r") as file:
                cls._config = yaml.safe_load(file)
        return cls._config

    @classmethod
    def get_env_config(cls):
        config = cls.load_config()
        env = os.getenv("TEST_ENV", config["default_env"])
        return config["environments"][env]
    
    @staticmethod
    def load_db_config():
        with open("framework/config/db_config.yaml", "r") as file:
            content = file.read()

        # replace ${VAR} with env variables
        for var in re.findall(r"\$\{(.*?)\}", content):
            content = content.replace(
                f"${{{var}}}", os.getenv(var, "")
            )

        config = yaml.safe_load(content)
        env = config["default_env"]
        return config["environments"][env]
