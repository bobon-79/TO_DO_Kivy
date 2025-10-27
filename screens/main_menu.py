"""
The main menu screen of the project
"""

from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen


class MainMenu(BoxLayout, Screen):
    """
     Class for the main menu screen of the project
    """
    app = App.get_running_app()
    splash = app.root.get_screen("splash")
    text_list = DictProperty()
    img_list = DictProperty()

    text_title = StringProperty()
    img_title = StringProperty()

    text_listPlan = StringProperty()
    img_listPlan = StringProperty()

    text_addPlan = StringProperty()
    img_addPlan = StringProperty()

    text_calendar = StringProperty()
    img_calendar = StringProperty()

    text_settings = StringProperty()
    img_settings = StringProperty()

    text_exit = StringProperty()
    img_exit = StringProperty()

    text_ver = StringProperty(app.config.get_param("app", "version"))

    name = StringProperty("main")
    config = ObjectProperty(app.config)
    log = ObjectProperty(app.log)

    def _init_properties(self):
        """
        Initializes the properties of the screen
        """
        # init text properties
        setattr(self, "text_list", self.splash.i18n.get_param("main_menu"))
        for key, value in self.text_list.items():
            setattr(self, f"text_{key}", value)
            setattr(self, f"img_{key}", self.splash.img.get_param("MD", key))

    def on_kv_post(self, *args):
        """
        Method called when before starting the screen
        """
        self._init_properties()

    def on_enter(self, *args):
        """
        Initializes the screen
        """

        self.log.debug("Init MainMenu")



    def onconfirm_exit(self):
        """

        """
        box = BoxLayout(orientation="vertical", spacing=10, padding=10)
        box.add_widget(Label(text="Выйти из приложения?" if self.app.config.get_param("app", "language") == "ru"
        else "Do you want to exit?" ,font_name="UI", italic=True))
        self.app.log.debug(self.app.config.get_param("app", "language"))
        btn = BoxLayout(size_hint_y=None, height="40dp", spacing=10)
        btn.add_widget(Button(text="Отмена", on_release=lambda x: popup.dismiss()))
        btn.add_widget(Button(text="Да", on_release=lambda x: self.app.stop()))
        box.add_widget(btn)

        popup = Popup(title="Подтверждение", content=box, size_hint=(0.6, 0.3))
        popup.open()

    def change_lang(self):
        """
        Changes the language of the app
        """
        self.app.log.debug("Change language")
        lang = "ru" if self.app.config.get_param("app", "language") == "en" else "en"
        self.app.config.set("app", "language",
                            value=lang)
        self.splash.i18n.switch(lang)
        self._init_properties()