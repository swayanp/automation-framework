# import os
# import yaml
# import re


# class ConfigLoader:
#     _config = None

#     @classmethod
#     def load_config(cls):
#         if cls._config is None:
#             with open("framework_config.yaml", "r") as file:
#                 cls._config = yaml.safe_load(file)
#         return cls._config

#     @classmethod
#     def get_env_config(cls):
#         config = cls.load_config()
#         env = os.getenv("TEST_ENV", config["default_env"])
#         return config["environments"][env]
    
#     # @staticmethod
#     # def load_db_config():
#     #     with open("framework/config/db_config.yaml", "r") as file:
#     #         content = file.read()

#     #     # replace ${VAR} with env variables
#     #     for var in re.findall(r"\$\{(.*?)\}", content):
#     #         content = content.replace(
#     #             f"${{{var}}}", os.getenv(var, "")
#     #         )

#     #     config = yaml.safe_load(content)
#     #     env = config["default_env"]
#     #     return config["environments"][env]
#     @staticmethod
#     def load_db_config():
#         # If running inside Docker / CI
#         if os.getenv("DB_HOST"):
#             return {
#                 "host": os.getenv("DB_HOST"),
#                 "port": int(os.getenv("DB_PORT", 5432)),
#                 "database": os.getenv("DB_NAME"),
#                 "username": os.getenv("DB_USER"),
#                 "password": os.getenv("DB_PASSWORD"),
#             }

#         # Fallback to YAML for local runs
#         with open("framework/config/db_config.yaml", "r") as file:
#             config = yaml.safe_load(file)

#         env = config["default_env"]
#         return config["environments"][env]
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

    # @staticmethod
    # def load_db_config():
    #     """
    #     DB config resolution strategy:
    #     1. If running in Docker / CI / K8s → use environment variables
    #     2. Otherwise → fallback to db_config.yaml (local runs)
    #     """

    #     # 🚀 Docker / CI / Kubernetes path
    #     if os.getenv("DB_HOST"):
    #         return {
    #             "host": os.getenv("DB_HOST"),
    #             "port": int(os.getenv("DB_PORT", 5432)),
    #             "database": os.getenv("DB_NAME"),
    #             "username": os.getenv("DB_USER"),
    #             "password": os.getenv("DB_PASSWORD"),
    #         }

    #     # 🧑‍💻 Local development fallback
    #     with open("framework/config/db_config.yaml", "r") as file:
    #         config = yaml.safe_load(file)

    #     env = config["default_env"]
    #     return config["environments"][env]
    @staticmethod
    def load_db_config():
        with open("framework/config/db_config.yaml", "r") as file:
            content = file.read()

        for var in re.findall(r"\$\{(.*?)\}", content):
            value = os.getenv(var)
            if not value:
                raise RuntimeError(f"❌ Missing required env var: {var}")
            content = content.replace(f"${{{var}}}", value)

        config = yaml.safe_load(content)
        env = config["default_env"]
        return config["environments"][env]
