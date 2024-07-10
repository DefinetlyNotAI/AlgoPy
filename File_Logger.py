from datetime import datetime
import os


class LoggerDB:
    def __init__(self, filename="Server.log", max_size=100):
        """
        Initialize the Logger class.

        This method initializes the Logger class and allows setting the filename attribute through initialization parameters. It also checks if the file exists and creates it if it doesn't.

        Parameters:
            filename (str): The name of the log file. Defaults to 'Server.log'.
            max_size (int): The maximum size of the log file in bytes. Defaults to 100.

        Returns:
            None
        """
        # Use the provided filename or default to 'Server.log'
        self.filename = str(filename)
        self.size = int(max_size)

        # Check if the file exists and create it if it doesn't
        if not os.path.exists(self.filename):
            with open(self.filename, "w"):
                pass  # Empty file content is fine here since we append logs

    @staticmethod
    def timestamp():
        """
        Get the current date and time and format it as a string in the format 'YYYY-MM-DD HH:MM:SS'.

        Returns:
            str: The formatted timestamp.
        """
        # Get the current date and time
        now = datetime.now()

        # Format the timestamp as a string
        time = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"

        return time

    def remove(self):
        """
        Removes the log file if it exists and is larger than the maximum size.

        Returns:
            None
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                line_count = sum(1 for _ in file)
            if line_count > self.size:
                os.remove(self.filename)

    def info(self, message):
        """
        Writes an informational message to the log file.

        Parameters:
            message (str): The informational message to be written.

        Returns:
            None
        """
        self.remove()
        with open(self.filename, "a") as f:
            f.write(f"INFO: {message} at {self.timestamp()}\n")

    def warning(self, message):
        """
        Writes a warning message to the log file.

        Parameters:
            message (str): The warning message to be written.

        Returns:
            None
        """
        self.remove()
        with open(self.filename, "a") as f:
            f.write(f"WARNING: {message} at {self.timestamp()}\n")

    def error(self, message):
        """
        Writes an error message to the log file.

        Parameters:
            message (str): The error message to be written.

        Returns:
            None
        """
        self.remove()
        with open(self.filename, "a") as f:
            f.write(f"ERROR: {message} at {self.timestamp()}\n")

    def critical(self, message):
        """
        Writes an error message to the log file.

        Parameters:
            message (str): The error message to be written.

        Returns:
            None
        """
        self.remove()
        with open(self.filename, "a") as f:
            f.write(f"CRITICAL: {message} at {self.timestamp()}\n")


"""
Example usage:

logger = LoggerDB(filename="NAME.EXTENSION", max_size=SIZE)  # Change 'NAME.EXTENSION' to your desired filename
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
"""
