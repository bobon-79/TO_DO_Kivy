"""
Internationalization and localization support.
"""
from utils import app

class I18N(app.preload):
    """
    Class for internationalization and localization support.
    """
    config = app.config
    CONFIG_PATH = ""
    if config.get_param("app", "language") == "ru":
        CONFIG_PATH = "locales/ru"
    if config.get_param("app", "language") == "en":
        CONFIG_PATH = "locales/en"

    def __init__(self, path=CONFIG_PATH):
        super().__init__(path)
        self.lang = self.config.get_param("app", "language", default="ru")

    def switch(self, lang):
        """
    Method for switching language.
        :param self:
        :param lang:
        """
        self.lang = lang
        self.config_path = app.preload.BASE_DIR / f"locales/{lang}.json"
        self.load_json()


i18n = I18N()


