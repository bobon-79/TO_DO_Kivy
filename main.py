"""
Entry point of the project.
"""
import sys

from kivy.factory import Factory
from kivy.logger import Logger
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition
from kivy.properties import BooleanProperty, ObjectProperty, DictProperty
from kivy.app import App
from kivy.core.window import Window
from screens.splash import SplashScreen


def _load_kv():
    try:
        for kv_files in [
            "kv/components/all_widgets.kv",
            "kv/components/hover.kv",
            "kv/components/label.kv",
            "kv/components/button.kv",
            "kv/components/title_label.kv",
            "kv/components/dropdown.kv",
            "kv/screens/main_menu.kv",
            "kv/screens/settings.kv",

        ]:
            Builder.load_file(kv_files)
    except Exception as e:
        Logger.error(f"main.py: {e}")


class TO_DOApp(App):
    _load_kv()
    start_splash = BooleanProperty(False)
    log = ObjectProperty()
    preload = ObjectProperty()
    """Class for loading JSON data."""
    colors = DictProperty()
    menu = ObjectProperty()
    settings = ObjectProperty()

    def on_start(self, *args):
        pass

    def build(self):
        """
        Method for building the application.
        :param self:
        :return:
        """
        if sys.platform.startswith("win"):
            Window.size = (324, 720)  # ширина, высота
            Window.clearcolor = "#8E8BE1"
    # Window.borderless = True

    def load_screens(self):
        """
         Method for loading screens.
        """
        Window.clearcolor = self.colors["background"]
        self.root.transition = FadeTransition(duration=0.4)
        self.root.add_widget(self.menu())
        self.root.add_widget(self.settings())
        self.root.current = "main"

if __name__ == '__main__':
    TO_DOApp().run()
