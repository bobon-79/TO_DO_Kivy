"""
The main menu screen of the project
"""

from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, DictProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from utils.screens_data import ScreensData


class MainMenu(BoxLayout, Screen, ScreensData):
    """
     Class for the main menu screen of the project
    """

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

    text_version = StringProperty()

    name = StringProperty("main")


    def on_kv_post(self, *args):
        """
        Method called when before starting the screen
        """
    def on_pre_leave(self, *args, **kwargs):
        """
        Method called when before leaving the screen.
        :param args:
        :return:
        """
        setattr(self.app, 'btn_exit', self.ids.btn_exit.height)

    def on_enter(self, *args):
        """
        Initializes the screen
        """
        self.log.debug("Init MainMenu")
        self._init_properties()



    def _on_confirm_exit(self):
        """
        Method called when the screen exits the application.
        """
        color = self.colors["on_primary"]
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
                      size_hint=(.9, 0.3),
                      background="",
                      background_color=self.app.colors["primary_dark"],
                      )

        popup.open()
        popup.bind(on_open=lambda *_: self.log.debug("Open confirmation popup"))

