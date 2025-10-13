"""
Entry point of the project.
"""
import sys

from kivy.factory import Factory
from kivy.lang import Builder
from utils import *
from kivy.properties import DictProperty
from kivy.app import App
from kivy.core.window import Window
from screens import *


class TO_DApp(App):
    colors = DictProperty(color.get_color())
    Factory.register("BaseMixin", cls=BaseMixin)

    def on_start(self):
        if sys.platform.startswith("win"):
            Window.size = (324, 720)  # ширина, высота
            Window.clearcolor = self.colors["background"]

    def build(self):
        """
        Method for building the application.
        :param self:
        :return:
        """
        self.title = "Планировщик задач"
        return Builder.load_file("TO_DO.kv")


if __name__ == '__main__':
    TO_DApp().run()
