# log.py
import inspect
import os
from datetime import datetime
import colorlog
import logging

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
            "colorlog_fmt_parameters": "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
        }
        self.EXCEPTION_LOG_LEVEL = 45
        self.INTERNAL_LOG_LEVEL = 15
        logging.addLevelName(self.EXCEPTION_LOG_LEVEL, "EXCEPTION")
        logging.addLevelName(self.INTERNAL_LOG_LEVEL, "INTERNAL")
        self.color = config.get("use_colorlog", True)
        self.filename = config.get("filename", "AlgoPy.log")
        if self.color:
            logger = colorlog.getLogger()
            logger.setLevel(
                getattr(logging, config["log_level"].upper(), logging.INFO)
            )
            handler = colorlog.StreamHandler()
            log_colors = {
                "INTERNAL": "cyan",
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
            try:
                getattr(logging, config["log_level"].upper())
            except AttributeError as AE:
                self.__internal(f"Log Level {config['log_level']} not found, setting default level to INFO -> {AE}")

        if not os.path.exists(self.filename):
            self.newline()
            self.raw("|     Timestamp     |  LOG Level  |" + " " * 71 + "LOG Messages" + " " * 71 + "|")
        self.newline()

    @staticmethod
    def __timestamp() -> str:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __pad_message(message: str) -> str:
        return (message + " " * (153 - len(message)) if len(message) < 153 else message[:150] + "...") + "|"

    def raw(self, message: str):
        frame = inspect.stack()[1]
        if frame.function == "<module>":
            self.__internal(f"Raw message called from a non-function - This is not recommended")
        with open(self.filename, "a") as f:
            f.write(f"{message}\n")

    def newline(self):
        with open(self.filename, "a") as f:
            f.write("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 154 + "|" + "\n")

    def info(self, message: str):
        if self.color:
            colorlog.info(message)
        self.raw(f"[{self.__timestamp()}] > INFO:     | {self.__pad_message(message)}")

    def warning(self, message: str):
        if self.color:
            colorlog.warning(message)
        self.raw(f"[{self.__timestamp()}] > WARNING:  | {self.__pad_message(message)}")

    def error(self, message: str):
        if self.color:
            colorlog.error(message)
        self.raw(f"[{self.__timestamp()}] > ERROR:    | {self.__pad_message(message)}")

    def critical(self, message: str):
        if self.color:
            colorlog.critical(message)
        self.raw(f"[{self.__timestamp()}] > CRITICAL: | {self.__pad_message(message)}")

    def debug(self, message: str):
        if message == "*-*":
            self.raw("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 152 + "|")
        else:
            colorlog.debug(message)

    def string(self, message: str, Type: str):
        type_map = {"err": "error", "warn": "warning", "crit": "critical"}
        Type = type_map.get(Type.lower(), Type)
        try:
            getattr(self, Type.lower())(message)
        except AttributeError as AE:
            self.__internal(f"A wrong Log Type was called: {Type} not found. -> {AE}")
            getattr(self, "Debug".lower())(message)

    def exception(self, message: str):
        if self.color:
            colorlog.log(self.EXCEPTION_LOG_LEVEL, message)
        self.raw(f"[{self.__timestamp()}] > EXCEPTION:| {self.__pad_message(message)}")

    def __internal(self, message: str):
        if self.color:
            colorlog.log(self.INTERNAL_LOG_LEVEL, message)


config = {"log_level": "debug"}
log = Log(config=config)
log.debug("This is a debug message")
log.info("This is an info message")
log.warning("This is a warning message")
log.error("This is an error message")
log.critical("This is a critical message")
log.raw("This is a raw message")
log.string("This is a log message from a string", "warn")
log.exception("This is an exception message")
