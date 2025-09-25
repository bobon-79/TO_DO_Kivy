"""
Internationalization and localization support.
"""

from utils import *
import json


class I18N:
    """
    Class for internationalization and localization support.
    """
    LOCALES_DIR = config.BASE_DIR / "locales"

    def __init__(self):
        self.lang = config.get("app", "language")
        self.texts = {}
        self.load_locale()

    def load_locale(self) -> dict:
        """
        Method for loading a locale file.
        :param self:
        :return: Dict
        """
        path = I18N.LOCALES_DIR / f"{self.lang}.json"
        if not path.exists():
            raise FileNotFoundError(f"Нет перевода для языка: {self.lang}")
        with open(path, encoding="utf-8") as f:
            self.texts = json.load(f)

    def get_locale_text(self, *keys, default=None):
        """
        Method for getting translation for given keys.
        :param default:
        :param self:
        :param keys: str
        :return: Dict
        """
        d = self.texts
        for key in keys:
            if isinstance(d, dict) and key in d:
                d = d[key]
            else:
                return default
        return d

    def switch(self, lang):
        """
    Method for switching language.
        :param self:
        :param lang:
        """
        self.lang = lang
        self.texts = self.load_locale


i18n = I18N()

if __name__ == "__main__":
    print(i18n.get_locale_text("main_menu", "title_label"))
