"""
Entry point of the project.
"""
import sys
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition
from kivy.properties import BooleanProperty
from kivy.app import App
from kivy.core.window import Window
from screens import SplashScreen


class TO_DOApp(App):
    start_splash = BooleanProperty(False)

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
            Window.clearcolor = ("#8E8BE1")

    def load_screens(self, ready):
        """
         Method for loading screens.
        """
        from screens.main_menu import MainMenu
        self.start_splash = ready
        if self.start_splash:
            self.log.info("Loading screens...")
        Window.clearcolor = self.colors["background"]
        self.root.transition = FadeTransition(duration=0.2)
        self.root.add_widget(MainMenu(name="main"))
        #Builder.load_file("kv/main_menu.kv")
        self.root.current = "main"


if __name__ == '__main__':
    TO_DOApp().run()
