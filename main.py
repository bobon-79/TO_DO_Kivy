"""
Entry point of the project.
"""
import sys

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window

from utils import *
from screens import *

class TO_DOApp(App, BoxLayout):
    # list_screens: list = [MainMenu()]

    def on_start(self):
        if sys.platform.startswith("win"):
            Window.size = (324, 720) # ширина, высота
            Window.clearcolor = 1, 1, 1, 1

    def build(self):
        pass


if __name__ == '__main__':
    TO_DOApp().run()
