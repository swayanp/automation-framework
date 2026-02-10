import psycopg2
from framework.config.config_loader import ConfigLoader
class DBClient:
    def __init__(self):
        config = ConfigLoader.load_db_config()
        print("🔥 DB CONFIG IN USE:", config)

        self.connection = psycopg2.connect(
            host=config["host"],
            port=config["port"],
            database=config["database"],
            user=config["username"],
            password=config["password"]
        )
