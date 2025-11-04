"""
Modul for screens.
"""
from kivy.app import App


class ScreensData:
    """
    Class to store screens data.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = App.get_running_app()
        """ Instance of the running App, or None if no App is running."""
        self.splash = self.app.root.get_screen('splash')
        """ Instance of the splash screen."""
        self.log = self.app.log
        """ Logger """
        self.colors = self.app.colors
        """Dictionary of colors."""
        self.config = self.app.config
        """ Configuration """

    def _init_properties(self):

        """
        Initializes the properties of the screen
        """
        setattr(self, "text_list", self.splash.i18n.get_param(self.name))
        for key, value in self.text_list.items():
            if hasattr(self, f"text_{key}"):
                setattr(self, f"text_{key}", value)
            if hasattr(self, f"img_{key}"):
                setattr(self, f"img_{key}", self.splash.img.get_param(f"{self.name}", key))
