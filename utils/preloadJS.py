"""
Module for loading JSON files and getting parameters.
"""
from __future__ import annotations

from utils import dataclass, field, ClassVar,Any, Path, json, os

@dataclass
class PreloadJs:
    """
    Upload JSON and access parameters.
    Attributes: path,data, config_path\n
        path: str - path to JSON file.\n
       data: dict[str | Any] — dictionary with JSON data.\n
        config_path: Path - path to JSON file.\n
    Methods: load_json, get_param\n
        load_json() — load JSON file.\n
        get_param(*keys: str, default: Any = None) → dict[str, Any]|str — get parameter from JSON file.
    """
    path: str
    config_path: Path = field(init=False)
    data: dict[str | Any] = field(default_factory=dict)

    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent.parent

    def __post_init__(self) -> None:
        self.config_path = self.BASE_DIR / f"{self.path}.json"
        self.load_json()

    def load_json(self) -> None:
        """
        Load JSON files.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path, encoding="utf-8") as f:
            self.data = json.load(f)

    def get_param(self, *keys: str, default: Any = None) -> dict[str, Any]|str:
        """
        Method for getting parameter.
        :param keys:
        :param default:
        :return:
        """
        d: Any = self.data
        for k in keys:
            if isinstance(d, dict) and k in d:
                d = d[k]
            else:
                return default
        return d
