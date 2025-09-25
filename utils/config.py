"""
File containing the Config class

"""
import json
import os
from pathlib import Path


class Config:
    """Class for loading and accessing application settings."""
    BASE_DIR = Path(__file__).resolve().parent.parent  # Path to project root directory
    CONFIG_PATH = BASE_DIR / "config.json"

    def __init__(self, path=CONFIG_PATH):
        self.path = path
        self.data = {}
        self.load()

    def load(self):
        """Load settings from config.json file"""
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Config file not found: {self.path}")
        with open(self.path, encoding="utf-8") as f:
            self.data = json.load(f)

    def save(self):
        """Save settings to config.json file"""
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def get(self, *keys, default=None) -> dict:
        """Access settings via keychain"""
        d = self.data
        for key in keys:
            if isinstance(d, dict) and key in d:
                d = d[key]
            else:
                return default
        return d

    def set(self, *keys, value):
        """Set a setting value"""
        d = self.data
        for key in keys[:-1]:
            d = d.setdefault(key, {})
        d[keys[-1]] = value
        self.save()
config = Config()

if __name__ == "__main__":
    print(config.data)