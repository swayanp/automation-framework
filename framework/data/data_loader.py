import os
import yaml
import re


class DataLoader:

    @staticmethod
    def load_yaml(file_name: str):
        with open(file_name, "r") as f:
            content = f.read()

        # Replace ${VAR_NAME} with env values
        for var in re.findall(r"\$\{(.*?)\}", content):
            content = content.replace(
                f"${{{var}}}", os.getenv(var, "")
            )

        return yaml.safe_load(content)
