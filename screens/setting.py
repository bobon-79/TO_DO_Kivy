"""

"""
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from utils.screens_data import ScreensData


class SettingsScreen(BoxLayout,Screen, ScreensData):
    name = 'settings'

    text_title = StringProperty()
    img_title = StringProperty()

    text_lang_ru = StringProperty()

    text_lang_en = StringProperty()

    text_back = StringProperty()
    img_back = StringProperty()

    text_version = StringProperty()

    def on_enter(self):
        """
        Start screen.
        """
        self._init_properties()
        self.log.debug("load settings screen")

    def change_lang(self):
        """
        Changes the language of the app
        """
        self.app.log.debug(f"Change language on-{self.config.get_param('app', 'language')}")
        if self.app.config.get_param("app", "language") == "en":
            lang = "ru"
            self.ids.ddl_open.dropdown.ids.btn_ru.normal_color = self.colors["accent_dark"]
            self.ids.ddl_open.dropdown.ids.btn_en.normal_color = self.colors["outline"]
        else:
            lang = "en"
            self.ids.ddl_open.dropdown.ids.btn_ru.normal_color = self.colors["outline"]
            self.ids.ddl_open.dropdown.ids.btn_en.normal_color = self.colors["accent_dark"]

        self.app.config.set("app", "language",
                            value=lang)
        self.splash.i18n.switch(lang)

        self._init_properties()

