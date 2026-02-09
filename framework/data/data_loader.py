import yaml
import csv
import os


class DataLoader:

    @staticmethod
    def _project_root():
        return os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

    @staticmethod
    def load_yaml(relative_path: str):
        """
        Example:
        load_yaml("login_users.yaml")
        load_yaml("static/ui/login_users.yaml")
        """
        data_path = os.path.join(
            DataLoader._project_root(),
            "framework",
            "testdata",
            relative_path
        )

        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Test data file not found: {data_path}")

        with open(data_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    @staticmethod
    def load_csv(relative_path: str):
        data_path = os.path.join(
            DataLoader._project_root(),
            "framework",
            "testdata",
            relative_path
        )

        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Test data file not found: {data_path}")

        with open(data_path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
