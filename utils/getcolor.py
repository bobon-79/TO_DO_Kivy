"""
Module to get color from a JSON file.
"""
from email.policy import default

from kivy.utils import get_color_from_hex
from utils import app, PreloadJs, dataclass, field


@dataclass
class Color(PreloadJs):
    """
    Color class to load color from a JSON file.
    Attributes: path, theme\n
       path: str = "assets/color/color”\n
       theme: str = field(init=False)\n
    """

    path: str = field(default="assets/color/color")
    theme: str = field(init=False)


    def get_color(self)->dict[str, list[float]]:
        """
        Get color from the JSON file.\n
        Returns: dict[str, list[float]]\n

        {primary, primary_dark, accent, background, surface,
         on_background, on_primary, on_surface, error}.
        """
        setattr(self, "theme", app.config.get_param("app", "theme"))
        if self.theme == "light":
            colors = self.get_param("light")
            return {k: get_color_from_hex(v) for k, v in colors.items()}
        if self.theme == "dark":
            colors = self.get_param("dark")
            return {k: get_color_from_hex(v) for k, v in colors.items()}
        return {}


color = Color()
