import logging, logging.config

from utils.config import config
from utils.basejson import BaseJSONLoader


def setting_logger()-> logging.Logger:
    """
    Setting logger for application.
    param: None
    return: logger object

    Example: from utils import log
    log.info(“This is an info message”)
    log.debug(“This is a debug message”)
    """
    log_path = BaseJSONLoader.BASE_DIR / "logs/logging"
    file_log = BaseJSONLoader.BASE_DIR / "logs/app.log"
    bl = BaseJSONLoader(log_path)
    conf = bl.data
    conf["handlers"]["file_prod"]["filename"] = file_log
    logging.config.dictConfig(conf)
    mode = config.get_param("app", "mode")

    if mode == "debug":
        return logging.getLogger("app")
    if mode == "release":
        return logging.getLogger("kivy")
    if mode == "root":
        return logging.getLogger("root")
    return logging.getLogger("app")


log = setting_logger()
