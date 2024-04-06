import logging
from .custom_formatter import CustomFormatter


def configure_logger(logger, log_level=logging.INFO, log_file=None):
    logger.setLevel(log_level)

    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)

    # file handler
    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setLevel(log_level)
        fh.setFormatter(CustomFormatter(color=False))
        logger.addHandler(fh)
