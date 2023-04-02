import logging
from logging.handlers import RotatingFileHandler
from ..bot import config


def DefaultLogger():
    logger    = logging.getLogger(__name__)
    handler   = RotatingFileHandler(
                    f"{config.LOG_DIR}/{config.LOG_FILE}", 
                    maxBytes=config.LOG_FILE_SIZE, 
                    backupCount=config.LOG_MAX_FILES)
    formatter = logging.Formatter(
                    "%(levelname)s %(name)s %(asctime)s %(message)s")
    handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

