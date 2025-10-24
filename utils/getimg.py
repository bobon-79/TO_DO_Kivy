"""
Module to get image from assets/icons/icons
"""
from kivy.app import App

from utils import app


class Image(app.preload):
    """
    Class to get image from assets/icons/icons
    """
    CONFIG_PATH = app.preload.BASE_DIR / "assets/icons/icons"

    def __init__(self, path=CONFIG_PATH):
        super().__init__(path)
        self.log = None

    def get_param(self, *keys, default=" "):
        """
        Get text from JSON and convert to Unicode symbol.
        :param keys: Keys to get a value from JSON.
        :param default:
        :return:
        """
        self.log = app.log

        try:
            img = chr(int(super().get_param(*keys)[1:], 16))
        except (KeyError, ValueError):
            img = default
            self.log.error(f"Image not found for {keys}")

        return  img


image = Image()
