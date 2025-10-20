"""Module for font size adaptation."""
from kivy.app import App
from kivy.clock import Clock


class BaseMixin:
    """A class to change font size responsively depending on the screen."""

    font_sizes: dict = {}

    def on_kv_post(self, base_widget)-> None:
        """
        Method Takes the widget size value at a startup.
        :param base_widget:
        :return: None

        """
        if not hasattr(self, '_base_width'):
            Clock.schedule_once(lambda dt: setattr(self, '_base_width', base_widget.width), 0.8)


    def adaptive_font(self, size_key: str, width: float, min_sp: int = 14,
                      max_sp: int = 38) -> float:
        """
        Method for adaptive font size depending on the screen size.
        :param size_key: Dictionary key font sizes
        :param width: Screen width.
        :param min_sp: Minimal font size.
        :param max_sp: Maximal font size.
        :return: Float font size.

        Example: Can be used in kv file as:
        font_size: app.adaptive_font(<size_key>, <root.width>)
        """
        self.font_sizes = App.get_running_app().font_sizes
        base_width = 0
        if hasattr(self, '_base_width'):
            base_width = self._base_width
        if not hasattr(self, '_base_width'):
            base_width = width
        base = float(self.font_sizes[size_key])
        scale = width / base_width
        return max(min_sp, min(max_sp, base * scale))
