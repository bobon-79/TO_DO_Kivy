"""
The utils package.
"""
from .config import config
from .i18n import i18n
from .basejson import BaseJSONLoader
from .getfont import font
from .getimg import image
from .getcolor import color

__all__ = ["config",
           "i18n",
           "BaseJSONLoader",
           "font",
           "image",
           "color"]
