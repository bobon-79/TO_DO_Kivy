"""
Entry point of the project.
"""
import sys
from kivy.uix.screenmanager import FadeTransition
from kivy.properties import BooleanProperty, ObjectProperty, Clock
from kivy.app import App
from kivy.core.window import Window
from screens import SplashScreen


class TO_DOApp(App):
    start_splash = BooleanProperty(False)
    log = ObjectProperty()
    colors = ObjectProperty()
    menu = ObjectProperty()

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
