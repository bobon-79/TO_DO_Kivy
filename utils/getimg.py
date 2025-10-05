"""
Module to get image from assets/icons/icons
"""
from utils import BaseJSONLoader


class Image(BaseJSONLoader):
    """
    Class to get image from assets/icons/icons
    """
    CONFIG_PATH = BaseJSONLoader.BASE_DIR / "assets/icons/icons"

    def __init__(self, path=CONFIG_PATH):
        super().__init__(path)

    def get_param(self, *keys, default=None):
        """
        Get text from JSON and convert to Unicode symbol.
        :param keys: ключи для получения значения из JSON
        :param default:
        :return:
        """
        return chr(int(super().get_param(*keys)[1:],16))


image = Image()
