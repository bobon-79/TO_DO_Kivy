"""
The main menu screen of the project
"""

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from utils import *


class MainMenu(BoxLayout,Screen):
    """
     Class for the main menu screen of the project
    """
    text_label = StringProperty(i18n.get_locale_text("main_menu", "title_label"))
    icon = str(config.BASE_DIR / "assets" / "label_mainmenu.png")
    color: list = [0.35, 0.88, 0.38, 1]





