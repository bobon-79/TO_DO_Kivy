"""
Entry point of the project.
"""
import sys

from kivy.properties import StringProperty, NumericProperty, DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window

from utils import *
from screens import *


class TO_DOApp(App, BoxLayout):
    font_sizes = DictProperty(font.get_sizes_font())
    colors = DictProperty(color.get_color())

    def on_start(self):
        if sys.platform.startswith("win"):
            Window.size = (324, 720)  # ширина, высота
            Window.clearcolor = self.colors["background"]  # цвет фона

    def build(self):
        pass


if __name__ == '__main__':
    TO_DOApp().run()
