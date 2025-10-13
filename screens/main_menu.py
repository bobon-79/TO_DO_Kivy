"""
The main menu screen of the project
"""

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import Screen

from utils import *


class MainMenu(BoxLayout, Screen):
    """
     Class for the main menu screen of the project
    """
    text_label = StringProperty(i18n.get_param("main_menu", "title_label"))
    blue = StringProperty(i18n.get_param("app", "blue"))
    img = StringProperty(image.get_param("MD", "bookOpenVariant"))

    def change_lang(self):
        """
        Changes the language of the app
        """
        lang = "ru" if config.get_param("app", "language") == "en" else "en"
        config.set("app", "language",
                   value=lang)
        i18n.switch(lang)
        self.text_label = i18n.get_param("main_menu", "title_label")
