# main.py — Splash → Main, фоновые задачи без блокировки UI
from functools import wraps

from kivy.app import App
from kivy.factory import Factory
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from threading import Thread
import time


def pause(timeout: float =0.8):
    """
    Stop the function for timeout seconds if it takes less than timeout seconds to run.
    :param timeout: Timeout in seconds.
    :return:
    """

    def decorator(func):
        """

        :param func:
        :return:
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
    start_splash = BooleanProperty(False)
    name = StringProperty('splash')
    thread = ObjectProperty()
    t_start = NumericProperty()

    def on_enter(self, *args):
        """
        Method to start the loading of the application.
        :param args:
        """
        self.thread = Thread(target=self._load, daemon=True)
        self.thread.start()
        #self.thread.join()

    def _load(self):
        setattr(self, "app", App.get_running_app())
        tasks = [
            ("Готовим папки…", 1, self._prep_dirs),
            ("Init logs…", 1, self._init_logs),
            ("Init config, colors, fonts…", 1, self._load_configs),
            ("Init assets…", 1, self._warm_assets),
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
                Clock.schedule_once(lambda *_: setattr(self, 'status', f"Ошибка: "))
                return 1
            done += w
            pct = int(done / total * 100)
            Clock.schedule_once(lambda *_: setattr(self, 'progress', pct))
        dt = time.perf_counter() - self.t_start
        Clock.schedule_once(lambda *_: setattr(self, 'status', f"Done in {dt:.2f} c"))
        self.start_splash = True
        Clock.schedule_once(lambda *_: self.app.load_screens(self.start_splash), 0.5)

    @pause(0.2)
    def _prep_dirs(self):
        pass

    @pause(0.2)
    def _init_logs(self):
        from utils.config import config
        self.app.config = config  # loading config in app
        from utils.config_logger import log
        setattr(self, 'log', log)
        self.log.info("Init logs — completed")
        self.app.log = log

    @pause(0.2)
    def _load_configs(self):
        from utils.basemixin import BaseMixin
        Factory.register("BaseMixin", cls=BaseMixin)
        from utils.getcolor import color
        self.app.colors = color.get_color()  # a loading dict of colors in app
        from utils.getfont import font
        self.app.font_sizes = font.get_sizes_font()  # loading font sizes in app


    @pause(0.2)
    def _warm_assets(self):
        from utils.getimg import image
        from utils.i18n import i18n
        self.img = image  # loading image
        self.i18n = i18n  # loading i18n

    def _init_screens(self):
        time.sleep(0.2)
