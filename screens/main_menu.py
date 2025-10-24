"""
The main menu screen of the project
"""

from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen


class MainMenu(BoxLayout, Screen):
    """
     Class for the main menu screen of the project
    """
    app = App.get_running_app()
    splash = app.root.get_screen("splash")
    text_label = StringProperty(splash.i18n.get_param("main_menu", "title_label"))
    img = StringProperty(splash.img.get_param("MD", "bookOpenVariant"))
    name = StringProperty("main")
    config = ObjectProperty(app.config)
    log = ObjectProperty(app.log)

    def on_enter(self, *args):
        """
        Initializes the screen
        """
        self.log.debug("Init MainMenu")

    def change_lang(self):
        """
        Changes the language of the app
        """
        lang = "ru" if self.config.get_param("app", "language") == "en" else "en"
        self.config.set("app", "language",
                        value=lang)
        self.splash.i18n.switch(lang)
        self.text_label = self.splash.i18n.get_param("main_menu", "title_label")
