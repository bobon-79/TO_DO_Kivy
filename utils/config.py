"""
File containing the Config class

"""
import json
from utils import PreloadJs, dataclass, field, Any

@dataclass
class Config(PreloadJs):
    """Class for loading and accessing application settings."""
    path: str = field(default="config")
    data: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        super().__post_init__()

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
