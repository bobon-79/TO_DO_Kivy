"""
Module to get image from assets/icons/icons
"""
from logging import Logger
from utils import app, PreloadJs, dataclass, field

@dataclass
class Image(PreloadJs):
    """
    Class to get image from assets/icons/icons
    """
    path: str = field(default="assets/icons/icons")
    log: Logger = field(default=app.log)

    def get_param(self, *keys, default=""):
        """
        Get text from JSON and convert to Unicode symbol.
        :param keys: Keys to get a value from JSON.
        :param default:
        :return:
        """
        try:
            img = chr(int(super().get_param(*keys)[1:], 16))
        except (KeyError, ValueError) as e:
            img = default
            self.log.error(f"Image not found for {keys}, {e}")

        return  img


image = Image()
