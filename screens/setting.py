"""

"""
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty, DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from utils.getcolor import color
from utils.screens_data import ScreensData


class SettingsScreen(BoxLayout, Screen, ScreensData):
    name = 'settings'

    text_title = StringProperty()
    img_title = StringProperty()

    text_lang_ru = StringProperty()
    text_lang_en = StringProperty()
    text_theme_light = StringProperty()
    text_theme_dark = StringProperty()

    text_back = StringProperty()
    img_back = StringProperty()
    change_theme = StringProperty()
    text_version = StringProperty()

    height_base = NumericProperty()
    color = DictProperty()

    def change_ddt(self):
        """

        :param lang:
        """
        (setattr(self, "change_theme", self.text_theme_light)
         if self.config.get_param("app","theme") == "light"
         else setattr(self, "change_theme", self.text_theme_dark))

    def on_enter(self):
        """
        Start screen.
        """
        setattr(self, "height_base", self.app.btn_exit)
        self._init_properties()
        self.change_ddt()
        self.log.debug("load settings screen")

    def _change_lang(self, lang: str):
        """
        Changes the language of the app
        :param lang: str
        """
        dropdown = self.ids.ddl_open.dropdown_lang
        if lang == "ru":
            dropdown.ids.btn_ru.normal_color = self.colors["accent_dark"]
            dropdown.ids.btn_en.normal_color = self.colors["outline"]
        if lang == "en":
            dropdown.ids.btn_ru.normal_color = self.colors["outline"]
            dropdown.ids.btn_en.normal_color = self.colors["accent_dark"]

        self.config.set("app", "language",
                        value=lang)
        self.app.log.debug(f"Change language on - {self.config.get_param('app', 'language')}")
        self.splash.i18n.switch(lang)
        self._init_properties()
        self.change_ddt()

    def _change_theme(self, theme):
        dropdown = self.ids.ddt_open.dropdown_theme
        if theme == "light":
            dropdown.ids.btn_light.normal_color = self.colors["accent_dark"]
            dropdown.ids.btn_dark.normal_color = self.colors["outline"]
        if theme == "dark":
            dropdown.ids.btn_light.normal_color = self.colors["outline"]
            dropdown.ids.btn_dark.normal_color = self.colors["accent_dark"]
        self.config.set("app", "theme", value=theme)
        self.app.log.debug(f"Change Theme on - {self.config.get_param('app', 'theme')}")
        self.app.colors = color.get_color()
        Window.clearcolor = self.app.colors["background"]
