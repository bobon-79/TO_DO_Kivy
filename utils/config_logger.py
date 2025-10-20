import logging
import logging.config
from logging import Logger
from typing import Any

from kivy.app import App

from utils.basejson import BaseJSONLoader
from utils.config import config


def setting_logger() -> tuple[Logger, Any]:
    """
    Setting logger for application.
    param: None
    return: logger object and mode

    Example: from utils import log
    log.info(“This is an info message”)
    log.debug(“This is a debug message”)
    """
    log_path = BaseJSONLoader.BASE_DIR / "logs/logging"
    file_log = BaseJSONLoader.BASE_DIR / "logs/app.log"
    config = App.get_running_app().config
    bl = BaseJSONLoader(log_path)
    conf = bl.data
    conf["handlers"]["file_prod"]["filename"] = file_log
    logging.config.dictConfig(conf)
    mode = config.get_param("app", "mode")

    if mode == "debug":
        return logging.getLogger("app"), mode
    if mode == "release":
        return logging.getLogger("kivy"), mode
    if mode == "root":
        return logging.getLogger("root"), mode
    return logging.getLogger("app"), mode


log, mode = setting_logger()

log.info(f"Application started with mode: {mode}")
