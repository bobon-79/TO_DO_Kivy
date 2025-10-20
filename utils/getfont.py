"""
The module fonts.
"""
from kivy.app import App
from kivy.core.text import LabelBase
from utils.basejson import BaseJSONLoader


class Font(BaseJSONLoader):
    """
    The Font class.
    """
    CONFIG_PATH = BaseJSONLoader.BASE_DIR / "assets/fonts/font"

    def __init__(self, path=CONFIG_PATH):
        super().__init__(path)
        LabelBase.register(
            name="UI",
            fn_regular=self.get_param("UI", "regular"),
            fn_bold=self.get_param("UI", "bold"),
        )  # Register the font with Kivy.
        LabelBase.register(
            name="MDI",
            fn_regular=self.get_param("MDI", "regular"))
        LabelBase.register(
            name="Emoji",
            fn_regular=self.get_param("Emoji", "regular"))
        self.log = None

    def get_sizes_font(self, default_size="16sp"):
        """
        Method to get the sizes of the font.
        {body, title, subtitle, caption}.
        return: dict the size of font.

        """
        self.log = App.get_running_app().log
        try:
            sizes = self.get_param("UI", "sizes")
        except KeyError or ValueError:
            self.log.Warning(f"Font sizes not found")
            return default_size
        return sizes

font = Font()
