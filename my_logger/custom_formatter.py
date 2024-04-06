import logging


class CustomFormatter(logging.Formatter):

    def __init__(self, color=True):
        super().__init__()

        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        orange = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        lightgrey = "\033[37m"
        darkgrey = "\033[90m"
        lightred = "\033[91m"
        lightgreen = "\033[92m"
        yellow = "\033[93m"
        lightblue = "\033[94m"
        pink = "\033[95m"
        lightcyan = "\033[96m"
        reset = "\033[0m"

        self.fmt = "%(asctime)s.%(msecs)03d %(name)s [%(levelname)s]: %(message)s"
        self.fmt_color = (
            cyan
            + "%(asctime)s.%(msecs)03d "
            + reset
            + darkgrey
            + "%(name)s "
            + reset
            + "<lc>[%(levelname)s]: "
            + reset
            + "%(message)s"
        )
        self.color = color
        self.datefmt = "%Y-%m-%d %H:%M:%S"
        self.formats = {
            logging.DEBUG: self.fmt_color.replace("<lc>", reset),
            logging.INFO: self.fmt_color.replace("<lc>", green),
            logging.WARNING: self.fmt_color.replace("<lc>", yellow),
            logging.ERROR: self.fmt_color.replace("<lc>", red),
            logging.CRITICAL: self.fmt_color.replace("<lc>", red),
        }

    def format(self, record):
        if self.color:
            log_fmt = self.formats.get(record.levelno)
        else:
            log_fmt = self.fmt
        formatter = logging.Formatter(log_fmt, self.datefmt)
        return formatter.format(record)
