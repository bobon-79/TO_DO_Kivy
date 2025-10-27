"""
 A module for setting logging in the Kivy application.
"""
import logging
import logging.config
from logging import Logger
from typing import Any

from kivy.app import App

from utils import app


def setting_logger() -> tuple[Logger, Any]:
    """
    Setting logger for application.
    param: None
    return: logger object and mode_log.

    Example: from utils import log
    log.info(“This is an info message”)
    log.debug(“This is a debug message”)
    """
    log_path = app.preload.BASE_DIR / "logs/logging"
    file_log = app.preload.BASE_DIR / "logs/app.log"
    bl = app.preload(log_path)
    conf = bl.data
    conf["handlers"]["file_prod"]["filename"] = file_log
    logging.config.dictConfig(conf)
    mode_log = App.get_running_app().config.get_param("app", "mode")

    if mode_log == "debug":
        return logging.getLogger("app"), mode_log
    if mode_log == "release":
        return logging.getLogger("kivy"), mode_log
    if mode_log == "root":
        return logging.getLogger("root"), mode_log
    return logging.getLogger("app"), mode_log


log, mode = setting_logger()

log.warning(f"Application started with mode: {mode}")
