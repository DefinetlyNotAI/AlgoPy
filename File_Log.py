

from datetime import datetime
import os


class Log:
    def __init__(self, filename="Server.log", max_size=None):
        """
        Initializes a new instance of the Log class.

        Args:
            filename (str, optional): The name of the log file. Defaults to "Server.log".
            max_size (int, optional): The maximum size of the log file in bytes. Defaults to infinity.

        Initializes the `filename` and `size` attributes of the Log instance.
        If the log file does not exist, it creates an empty file with the specified name.

        """
        # Use the provided filename or default to 'Server.log'
        self.filename = str(filename)
        self.size = int(max_size)

        # Check if the file exists and create it if it doesn't
        if not os.path.exists(self.filename):
            with open(self.filename, "w"):
                pass  # Empty file content is fine here since we append logs

    @staticmethod
    def __timestamp():
        """
        Retrieves the current date and time and formats it into a string timestamp.

        Returns:
            str: A string representing the formatted timestamp.
        """
        # Get the current date and time
        now = datetime.now()

        # Format the timestamp as a string
        time = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"

        return time

    def __remove(self):
        """
        Remove the log file if it exists and the number of lines in the file exceeds the specified size.

        This function checks if the log file specified by the `filename` attribute exists. If it does, it opens the file in read mode and counts the number of lines in the file. If the number of lines is greater than the specified `size`, the file is removed.

        Returns:
            None
        """
        if os.path.exists(self.filename) and self.size is not None:
            with open(self.filename, "r") as file:
                line_count = sum(1 for _ in file)
            if line_count > self.size:
                os.remove(self.filename)

    def info(self, message):
        """
        Writes an information log message to the log file.

        Args:
            message (str): The message to be logged.

        Returns:
            None
        """
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"INFO: {message} at {self.__timestamp()}\n")

    def warning(self, message):
        """
        Writes a warning log message to the log file.

        Args:
            message (str): The warning message to be logged.

        Returns:
            None
        """
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"WARNING: {message} at {self.__timestamp()}\n")

    def error(self, message):
        """
        Writes an error log message to the log file.

        Args:
            message (str): The error message to be logged.

        Returns:
            None
        """
        self.__remove()
        with open(self.filename, "a") as f:
            f.write(f"ERROR: {message} at {self.__timestamp()}\n")

    def critical(self, message):
        """
        Writes a critical log message to the log file.

        Args:
            message (str): The critical message to be logged.

        Returns:
            None
        """
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
