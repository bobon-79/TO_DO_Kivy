"""
Entry point of the project.
"""
import sys
from fileinput import lineno, filename

from kivy.logger import Logger
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.app import App
from kivy.core.window import Window
from screens import SplashScreen


def _load_kv():
    try:
        for kv_files in [
            "kv/components/all_widgets.kv",
            "kv/components/button.kv",
            "kv/components/title_label.kv",
            "kv/screens/main_menu.kv",
        ]:
            Builder.load_file(kv_files)
    except FileNotFoundError as e:
        Logger.error(f"main.py: {e}")

class TO_DOApp(App):
    _load_kv()
    start_splash = BooleanProperty(False)
    log = ObjectProperty()
    colors = ObjectProperty()
    menu = ObjectProperty()

    def on_start(self, *args):
        pass
    def animate_button(self, widget, color):
        """
         Method for animating the button.
        :param widget:
        :param color:
        """
        Animation(background_color=color, duration=0.1).start(widget)

    def build(self):
        """
        Method for building the application.
        :param self:
        :return:
        """

        self.root.add_widget(SplashScreen(), name="splash")
        if sys.platform.startswith("win"):
            Window.size = (324, 720)  # ширина, высота
            Window.clearcolor = "#8E8BE1"
        Window.borderless = True
        return self.root

    def load_screens(self):
        """
         Method for loading screens.
        """
        Window.clearcolor = self.colors["background"]
        self.root.transition = FadeTransition(duration=0.4)
        self.root.add_widget(self.menu())
        self.root.current = "main"


if __name__ == '__main__':
    TO_DOApp().run()
