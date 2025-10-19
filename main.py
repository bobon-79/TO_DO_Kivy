"""
Entry point of the project.
"""
import json
import logging
import logging.config
import sys

from kivy.clock import Clock
from kivy.factory import Factory
from kivy.lang import Builder
from utils import *
from kivy.properties import DictProperty, BooleanProperty
from kivy.app import App
from kivy.core.window import Window
from screens import *


class TO_DApp(App):
    colors = DictProperty(color.get_color())
    Factory.register("BaseMixin", cls=BaseMixin)
    start_app = BooleanProperty(False)

    def on_start(self, *args):
        log.info(f"App started")
        Clock.schedule_once(lambda x: setattr(self, "start_app", True))

    def build(self):
        """
        Method for building the application.
        :param self:
        :return:
        """
        if sys.platform.startswith("win"):
            Window.size = (324, 720)  # ширина, высота
            Window.clearcolor = self.colors["background"]
        self.title = "Планировщик задач"
        return Builder.load_file("TO_DO.kv")


if __name__ == '__main__':
    TO_DApp().run()
