"""
File containing the Config class

"""
import json
from kivy.app import App

app = App.get_running_app()


class Config(app.preload):
    """Class for loading and accessing application settings."""
    CONFIG_PATH = "config"

    def __init__(self, path=CONFIG_PATH):
        super().__init__(path)
        self.data = {}
        self.load_json()

    def save(self):
        """Save settings to the config.json file"""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def set(self, *keys, value):
        """Set a setting value"""
        d = self.data
        for key in keys[:-1]:
            d = d.setdefault(key, {})
        d[keys[-1]] = value
        self.save()


config = Config()
