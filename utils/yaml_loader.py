# @Author: Sheep Wang
# @File: yaml_loader.py
# @Created: 2026-09-07 21:26
# @Description: yaml_loader.py


import os
import yaml
from utils.logger import log
from pathlib import Path




def load_yaml(file_relative_path: str):
    """
    Loads YAML data file using a path relative to the project root.
    Example usage: load_yaml("testdata/auth_data.yaml")
    """
    # Calculate absolute path relative to project root
    project_root = Path(__file__).resolve().parent.parent
    absolute_path = project_root / file_relative_path

    if not os.path.exists(absolute_path):
        log.error(f"YAML data file not found at: {absolute_path}")
        raise FileNotFoundError(f"YAML file missing: {absolute_path}")

    try:
        with open(absolute_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            log.info(f"Successfully loaded test data from: {file_relative_path}")
            return data
        
    except Exception as e:
        log.error(f"Failed to parse YAML file {file_relative_path}: {str(e)}")
        raise e


if __name__ == "__main__":
    print(Path(__file__).resolve().parent.parent)