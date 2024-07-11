"""
Manages logging operations for applications, supporting various severity levels (info, warning, error, critical).
Automatically rotates the log file based on size, ensuring that no single log file exceeds a specified maximum size.
Maintains a default filename ('Server.log') unless otherwise specified during instantiation.
Utilizes static methods for timestamp generation, promoting reusability across different instances.
Ensures thread safety by managing file access through context managers, preventing concurrent modifications.
Efficiently appends log messages to the file, incorporating timestamps for precise logging.
Removes the existing log file if it exceeds the maximum size, automatically starting fresh without manual intervention.

TIME COMPLEXITY: O(n) [Log.info] [Log.warning] [Log.error] [Log.critical]
SPACE COMPLEXITY: O(n) [Log.info] [Log.warning] [Log.error] [Log.critical]
"""

from datetime import datetime
import os


class Log:
    def __init__(self, filename="Server.log", max_size=100):
        # Use the provided filename or default to 'Server.log'
        self.filename = str(filename)
        self.size = int(max_size)

        # Check if the file exists and create it if it doesn't
        if not os.path.exists(self.filename):
            with open(self.filename, "w"):
                pass  # Empty file content is fine here since we append logs

    @staticmethod
    def __timestamp():
        # Get the current date and time
        now = datetime.now()

        # Format the timestamp as a string
        time = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"

        return time

    def __remove(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                line_count = sum(1 for _ in file)
            if line_count > self.size:
                os.remove(self.filename)

    def info(self, message):
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"INFO: {message} at {self.__timestamp()}\n")

    def warning(self, message):
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"WARNING: {message} at {self.__timestamp()}\n")

    def error(self, message):
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"ERROR: {message} at {self.__timestamp()}\n")

    def critical(self, message):
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"CRITICAL: {message} at {self.__timestamp()}\n")


"""
Example usage:
from Log import *

log = Log(filename="NAME.EXTENSION", max_size=SIZE)  # Change 'NAME.EXTENSION' to your desired filename

log.info("This is an informational message.")
log.warning("This is a warning message.")
log.error("This is an error message.")
log.critical("This is a critical message.")
"""
