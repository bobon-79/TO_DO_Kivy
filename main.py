"""
Entry point of the project.
"""
import sys

from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window

from utils import *
from screens import *


class TO_DOApp(App, BoxLayout):
    # list_screens: list = [MainMenu()]
    title_size = NumericProperty(font.get_param("UI", "sizes", "title"))
    body_size = NumericProperty(font.get_param("UI", "sizes", "body"))
    subtitle_size = NumericProperty(font.get_param("UI", "sizes", "subtitle"))
    caption_size = NumericProperty(font.get_param("UI", "sizes", "caption"))

    def on_start(self):
        if sys.platform.startswith("win"):
            Window.size = (324, 720)  # ширина, высота
            Window.clearcolor = 1, 1, 1, 1

    def build(self):
        pass


if __name__ == '__main__':
    TO_DOApp().run()
