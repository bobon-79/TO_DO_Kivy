"""

"""
from utils import BaseJSONLoader


class Image(BaseJSONLoader):
    CONFIG_PATH = BaseJSONLoader.BASE_DIR / "assets/icons/icons"

    def __init__(self, path=CONFIG_PATH):
        super().__init__(path)

    def get_param(self, *keys, default=None):
        return chr(int(super().get_param(*keys)[1:],16))


image = Image()
