"""
The main menu screen of the project
"""
from kivy.clock import Clock
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
    img = chr(int(i18n.get_param("main_menu", "img")[1:], 16))

    def on_kv_post(self, base_widget):
        """

        :param base_widget:
        """
        pass
        #✔Clock.schedule_once(lambda dt: print(self.ids.card_label.text))
