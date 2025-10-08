"""

"""
from kivy.utils import get_color_from_hex

from utils.basejson import BaseJSONLoader
from utils.config import config


class Color(BaseJSONLoader):
    """
    Color class to load color from a JSON file.
    """
    CONFIG_PATH = BaseJSONLoader.BASE_DIR / "assets/color/color"

    def __init__(self, path=CONFIG_PATH):
        super().__init__(path)
        self.theme = config.get_param("app", "theme")

    def get_color(self):
        """
        Get color from the JSON file.
        {primary, primary_dark, accent, background, surface,
         on_background, on_primary, on_surface, error}.
        """
        if self.theme == "light":
            colors = self.get_param("light")
            return {k: get_color_from_hex(v) for k, v in colors.items()}
        if self.theme == "dark":
            colors = self.get_param("dark")
            return {k: get_color_from_hex(v) for k, v in colors.items()}
        return {}


color = Color()

