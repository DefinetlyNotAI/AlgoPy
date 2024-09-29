# log.py
import os
from datetime import datetime
import colorlog
import logging

# TODO redo the log class of both logicytics and algopy to make it easier to setup and use,
#  make it less janky
#  Set up using a dictionary, and then use the dictionary to set up the logger,
#  and then use the debug logger to log the dictionary )

# The available color names are:
#
# black
# red
# green
# yellow
# blue,
# purple
# cyan
# white
# You can also use "bright" colors. These aren't standard ANSI codes, and support for these varies wildly across different terminals.
#
# light_black
# light_red
# light_green
# light_yellow
# light_blue
# light_purple
# light_cyan
# light_white


# Define custom log levels
EXCEPTION_LOG_LEVEL = 45
INTERNAL_LOG_LEVEL = 5

logging.addLevelName(EXCEPTION_LOG_LEVEL, "EXCEPTION")
logging.addLevelName(INTERNAL_LOG_LEVEL, "INTERNAL")

class Log:
    def __init__(self, config: dict = None):
        config = config or {
            "filename": "AlgoPy.log",
            "use_colorlog": True,
            "log_level": "INFO",
            "debug_color": "cyan",
            "info_color": "green",
            "warning_color": "yellow",
            "error_color": "red",
            "critical_color": "red",
            "exception_color": "red",
            "internal_color": "blue",
            "colorlog_fmt_parameters": "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
        }

        self.debug_bool = config.get("log_level", "INFO").upper() == "DEBUG"
        self.color = config.get("use_colorlog", True)
        self.filename = config.get("filename", "AlgoPy.log")
        if self.color:
            logger = colorlog.getLogger()
            logger.setLevel(
                getattr(logging, config["log_level"].upper(), logging.INFO)
            )
            handler = colorlog.StreamHandler()
            log_colors = {
                "INTERNAL": config.get("internal_color", "blue"),
                "DEBUG": config.get("debug_color", "cyan"),
                "INFO": config.get("info_color", "green"),
                "WARNING": config.get("warning_color", "yellow"),
                "ERROR": config.get("error_color", "red"),
                "CRITICAL": config.get("critical_color", "red"),
                "EXCEPTION": config.get("exception_color", "red"),
            }

            formatter = colorlog.ColoredFormatter(
                config.get("colorlog_fmt_parameters", "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"),
                log_colors=log_colors,
            )

            handler.setFormatter(formatter)
            logger.addHandler(handler)
            getattr(logging, config["log_level"].upper(), self.warning(f"Log Level {config['log_level']} not found, setting default level to INFO"))

        if not os.path.exists(self.filename):
            self.newline()
            self.raw("|     Timestamp     |  LOG Level  |" + " " * 71 + "LOG Messages" + " " * 71 + "|")
        self.newline()

    @staticmethod
    def __timestamp() -> str:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __pad_message(message):
        return (message + " " * (153 - len(message)) if len(message) < 153 else message[:150] + "...") + "|"

    def raw(self, message):
        with open(self.filename, "a") as f:
            f.write(f"{message}\n")

    def newline(self):
        with open(self.filename, "a") as f:
            f.write("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 154 + "|")

    def info(self, message):
        if self.color:
            colorlog.info(message)
        self.raw(f"[{self.__timestamp()}] > INFO:     | {self.__pad_message(message)}\n")

    def warning(self, message):
        if self.color:
            colorlog.warning(message)
        self.raw(f"[{self.__timestamp()}] > WARNING:  | {self.__pad_message(message)}\n")

    def error(self, message):
        if self.color:
            colorlog.error(message)
        self.raw(f"[{self.__timestamp()}] > ERROR:    | {self.__pad_message(message)}\n")

    def critical(self, message):
        if self.color:
            colorlog.critical(message)
        self.raw(f"[{self.__timestamp()}] > CRITICAL: | {self.__pad_message(message)}\n")

    def debug(self, message):
        if message == "*-*":
            self.raw("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 152 + "|")
        else:
            colorlog.debug(message)

    def string(self, Message: str, Type: str):
        type_map = {"err": "error", "warn": "warning", "crit": "critical"}
        Type = type_map.get(Type.lower(), Type)
        try:
            getattr(self, Type.lower())(Message)
        except AttributeError as AE:
            self.warning(f"A wrong Log Type was called: {Type} not found. -> {AE}")
            getattr(self, "Debug".lower())(Message)

    def exception(self, message):
        if self.color:
            colorlog.log(EXCEPTION_LOG_LEVEL, message)
        self.raw(f"[{self.__timestamp()}] > EXCEPTION:| {self.__pad_message(message)}\n")

    def internal(self, message):
        if self.color and self.debug_bool:
            colorlog.log(INTERNAL_LOG_LEVEL, message)

config = {"log_level": "DEBUG"}
log = Log(config=config)
log.debug("This is a debug message")
log.error("This is an error message")
log.info("This is an info message")
log.warning("This is a warning message")
log.critical("This is a critical message")
log.raw("This is a raw message")
log.string("This is log message from a string", "warn")
log.exception("This is an exception message")
log.internal("This is an internal message")