"""
Entry point of the project.
"""
import sys

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window

from utils import config
from screens import *


class TO_DOApp(App, BoxLayout):
    # list_screens: list = [MainMenu()]
    UI = StringProperty(str(config.BASE_DIR / "assets/fonts/materialdesignicons-webfont.ttf"))
    MDI = StringProperty(str(config.BASE_DIR / "assets/fonts/Wremena-Regular.ttf"))

    def on_start(self):
        if sys.platform.startswith("win"):
            Window.size = (324, 720)
            Window.clearcolor = 1, 1, 1, 1  # ширина, высота

    def build(self):
        pass


if __name__ == '__main__':
    TO_DOApp().run()
