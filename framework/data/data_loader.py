import yaml
import os


class DataLoader:

    @staticmethod
    def load_yaml(file_name: str):
        project_root = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

        data_path = os.path.join(
            project_root,
            "framework",
            "data",
            file_name
        )

        with open(data_path, "r") as f:
            return yaml.safe_load(f)
