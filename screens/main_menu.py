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
    """ Calling properties of the app """
    splash = app.root.get_screen("splash")
    """Calling properties of the splash screen"""
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

    text_ver = StringProperty()

    name = StringProperty("main")
    config = ObjectProperty(app.config)
    """ Calling config values  """
    log = ObjectProperty(app.log)
    """ Logging for the main menu screen """

    def _init_properties(self):
        """
        Initializes the properties of the screen
        """
        version = self.config.get_param("app", "version")
        setattr(self, "text_ver", f"  версия\n{version}" if self.app.config.get_param("app", "language") == "ru"
                                                         else f"  version\n{version}")
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

    def _on_confirm_exit(self):
        """
        Method called when the screen exits the application.
        """
        color = self.app.colors["on_primary"]
        font_name = "UI"
        check_lang = self.config.get_param("app", "language") == "ru"
        box = BoxLayout(orientation="vertical", spacing=10, padding=10)
        box.add_widget(Label(text="Выйти из приложения?" if check_lang else "Do you want to exit?",
                             font_name=font_name,
                             italic=True,
                             color=color))
        btn = BoxLayout(size_hint_y=None, height="40dp", spacing=10)
        btn.add_widget(Button(text="Отмена" if check_lang else "Cancel",
                              on_release=lambda _: popup.dismiss(),
                              font_name=font_name,
                              color=color))
        btn.add_widget(Button(text="Да" if check_lang else "Yes",
                              on_release=lambda _: self.app.stop(),
                              font_name=font_name,
                              color=color))
        box.add_widget(btn)

        popup = Popup(title="Подтверждение" if check_lang else "Confirmation",
                      title_align="center",
                      title_color=color,
                      separator_color=color,
                      content=box,
                      size_hint=(0.6, 0.3),
                      background="",
                      background_color=self.app.colors["primary_dark"],
                      )

        popup.open()
        popup.bind(on_open=lambda *_: self.log.debug("Open confirmation popup"))

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
