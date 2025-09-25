"""
Entry point of the project.
"""
import sys

from kivy.uix.screenmanager import ScreenManager

from screens import *
from kivy.app import App
from kivy.core.window import Window




class TO_DOApp(App):
    list_screens:list = [MainMenu()]
    def on_start(self):
        if sys.platform.startswith("win"):
            Window.size = (324, 720)  # ширина, высота

    def build(self):
        sc = ScreenManager()
        sc.add_widget(MainMenu())


if __name__ == '__main__':
    TO_DOApp().run()
