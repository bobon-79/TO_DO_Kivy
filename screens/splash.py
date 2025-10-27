"""
The SplashScreen of the project.
"""

from functools import wraps

from kivy.logger import Logger

from kivy.app import App
from kivy.factory import Factory
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from threading import Thread, Event
import time

t = 0.2


def pause(timeout: float = t):
    """
    Stop the function for timeout seconds if it takes less than timeout seconds to run.
    :param timeout: Timeout in seconds.
    :return: A decorator.
    """

    def decorator(func):
        """
        :param func:
        :return: wrapper
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Decorator wrapper for alignment of the function execution time.
            :param args:
            :param kwargs:
            """
            t0 = time.perf_counter()
            func(*args, **kwargs)
            t1 = time.perf_counter()
            dt = t1 - t0
            if dt < timeout:
                time.sleep(timeout - dt)

        return wrapper

    return decorator


class SplashScreen(Screen):
    progress = NumericProperty()  # 0..100
    status = StringProperty('Start...')
    name = StringProperty('splash')
    thread = ObjectProperty()
    t_start = NumericProperty()
    event = ObjectProperty(Event())

    def on_enter(self, *args):
        """
        Method to start the loading of the application.
        :param args:
        """
        Logger.info("SplashScreen: on enter")
        self.thread = Thread(target=self._load, daemon=True)
        self.thread.start()

    def _load(self):
        setattr(self, "app", App.get_running_app())
        tasks = [
            ("Init config and preload JSON…", 1, self._load_configs),
            ("Init logging…", 1, self._init_logs),
            ("loading fonts", 1, self._load_fonts),
            ("loading colors", 1, self._load_colors),
            ("loading i18n…", 1, self._load_i18n),
            ("Loading screens…", 1, self._init_screens),
        ]
        done = 0
        total = sum(w for _, w, __ in tasks)
        self.t_start = time.perf_counter()

        for msg, w, fn in tasks:
            Clock.schedule_once(lambda *_: setattr(self, 'status', msg))
            try:
                fn()
            except Exception as e:
                print(e)
                err = e
                Clock.schedule_once(lambda *_: setattr(self, 'status', f"Error:{err}\n on init -  self.{fn.__name__} "))
                return 1
            done += w
            pct = int(done / total * 100)
            Clock.schedule_once(lambda *_: setattr(self, 'progress', pct))
        dt = time.perf_counter() - self.t_start
        Clock.schedule_once(lambda *_: setattr(self, 'status', f"Done in {dt:.2f} c"))
        Clock.schedule_once(lambda *_: self.app.load_screens(),0.8 )

    @pause()
    def _load_configs(self):
        from utils.preloadJS import PreloadJs
        self.app.preload = PreloadJs
        from utils.config import config
        self.app.config = config


    @pause()
    def _init_logs(self):
        from utils.config_logger import log
        setattr(self, 'log', log)
        self.app.log = log

    @pause()
    def _load_fonts(self):
        from utils.basemixin import BaseMixin
        Factory.register("BaseMixin", cls=BaseMixin)
        from utils.getfont import font
        self.app.font_sizes = font.get_sizes_font()
        from utils.getimg import image
        self.img = image  # loading image


    @pause()
    def _load_colors(self):
        from utils.getcolor import color
        self.app.colors = color.get_color()

    @pause()
    def _load_i18n(self):
        from utils.i18n import i18n
        self.i18n = i18n  # loading i18n

    @pause()
    def _init_screens(self):
        from screens.main_menu import MainMenu
        menu = MainMenu
        self.app.menu = menu
