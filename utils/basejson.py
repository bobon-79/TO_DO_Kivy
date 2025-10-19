"""
Module for loading JSON files and getting parameters.
"""

import json
import os
from pathlib import Path


class BaseJSONLoader:
    """Base class for JSON loaders and get parameters."""
    BASE_DIR = Path(__file__).resolve().parent.parent

    def __init__(self, path: str):
        self.data = {}
        self.config_path = BaseJSONLoader.BASE_DIR / f"{path}.json"
        self.load_json()

    def load_json(self):
        f"""
        Loads JSON {self.config_path}.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path, encoding="utf-8") as f:
            self.data = json.load(f)

    def get_param(self, *keys, default={}):
        """
        Get parameter from JSON data.
            :param keys:  keys to get parameter.
            :param default: Default value if parameter not found.
        """
        d = self.data
        for key in keys:
            if isinstance(d, dict) and key in d:
                d = d[key]
            else:
                return default
        return d


