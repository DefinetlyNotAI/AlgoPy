r"""
Converts integers to Roman numerals and vice versa.

Please note that this is not an exhaustive list of all possible Roman numerals
that can be represented and is a mix of preset and algorithmic calculations.

If an error occurs during the conversion process, an error message will be displayed if set to True,
as well as the class returning False.

COMPLEXITY = O(n*log(n)) [to_roman] and [to_number]
COMPLEXITY = O(n*m) [to_ascii]

SPACE COMPLEXITY = O(1)
"""

import colorlog

# Configure colorlog for logging messages with colors
logger = colorlog.getLogger()
logger.setLevel(colorlog.INFO)  # Set the log level to INFO to capture all relevant logs

handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    },
)
handler.setFormatter(formatter)
logger.addHandler(handler)


class Convert:
    def __init__(self, show_errors=True):
        """
        Initializes the mapping dictionary with Roman numeral values corresponding to integers.
        Initializes the roman_to_numerical dictionary with integer values corresponding to Roman numerals.
        Initializes the error_level bool (optional) whether to show error messages. Defaults to True.
        """
        self.mapping = {
            10000: "/X/",
            9000: "M/X/",
            8000: "/VIII/",
            5000: "/V/",
            4000: "M/V/",
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        # Initialize the roman_to_numerical dictionary here since it's used in both methods.
        self.roman_to_numerical = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "/X/": 10000,
            "M/X/": 9000,
            "/VIII/": 8000,
            "/V/": 5000,
            "M/V/": 4000,
        }

        Zero = ["  ***  ",
                " *   * ",
                "*     *",
                "*     *",
                "*     *",
                " *   * ",
                "  ***  "]

        One = [" * ",
               "** ",
               " * ",
               " * ",
               " * ",
               " * ",
               "***"]

        Two = [" *** ",
               "*   *",
               "*  * ",
               "  *  ",
               " *   ",
               "*    ",
               "*****"]

        Three = [" *** ",
                 "*   *",
                 "    *",
                 "  ** ",
                 "    *",
                 "*   *",
                 " *** "]

        Four = ["   *  ",
                "  **  ",
                " * *  ",
                "*  *  ",
                "******",
                "   *  ",
                "   *  "]

        Five = ["*****",
                "*    ",
                "*    ",
                " *** ",
                "    *",
                "*   *",
                " *** "]

        Six = [" *** ",
               "*    ",
               "*    ",
               "**** ",
               "*   *",
               "*   *",
               " *** "]

        Seven = ["*****",
                 "    *",
                 "   * ",
                 "  *  ",
                 " *   ",
                 "*    ",
                 "*    "]

        Eight = [" *** ",
                 "*   *",
                 "*   *",
                 " *** ",
                 "*   *",
                 "*   *",
                 " *** "]

        Nine = [" ****",
                "*   *",
                "*   *",
                " ****",
                "    *",
                "    *",
                "    *"]

        self.digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
        self.error_level = show_errors

    def to_roman(self, num):
        """
        Converts an integer number to its corresponding Roman numeral representation.

        Parameters:
            num (int): The integer number to be converted.

        Returns:
            str: The Roman numeral representation of the input number.

        Raises:
            KeyError: If the input number is smaller than 1.
            Exception: If any other error occurs during the conversion process.
        """
        try:
            num = int(num)
            if num <= 1:
                if self.error_level:
                    colorlog.error("Input must be greater or equal to 1.")
                return False
            if num > 10000 and self.error_level:
                colorlog.warning(
                    "Input is too large. This may result in inaccurate results."
                )

            result = ""
            for numerical, roman in sorted(self.mapping.items(), reverse=True):
                while num >= numerical:
                    result += roman
                    num -= numerical
            return result
        except KeyError as ke:
            if self.error_level:
                colorlog.error("Invalid numeral: " + str(ke))
            return False
        except Exception as e:
            if self.error_level:
                colorlog.error(str(e))
            return False

    def to_number(self, roman):
        """
        Converts a Roman numeral to its corresponding integer representation.

        Parameters:
            roman (str): The Roman numeral to be converted.

        Returns:
            int: The integer representation of the input Roman numeral.

        Raises:
            KeyError: If the input Roman numeral is not valid.
            Exception: If any other error occurs during the conversion process.
        """
        try:
            i = 0
            num = 0
            roman = roman.upper()
            while i < len(roman):
                if i + 1 < len(roman) and roman[i: i + 2] in self.roman_to_numerical:
                    num += self.roman_to_numerical[roman[i: i + 2]]
                    i += 2
                else:
                    num += self.roman_to_numerical[roman[i]]
                    i += 1
            return num
        except KeyError as ke:
            if self.error_level:
                colorlog.error(f"Invalid Roman numeral: {ke}")
            return False
        except Exception as e:
            if self.error_level:
                colorlog.error(str(e))
            return False

    def to_ascii(self, Number=None):
        """
        Generates ASCII art representation of a Number.

        Parameters:
            Number (str): The number to convert into ASCII art. If None, user input is requested.

        Returns:
            str: The ASCII art representation of the input Number.
        """
        if Number is None:
            while True:
                Number = input("Input a number to expand: ")
                if Number.isdigit():
                    break
                else:
                    colorlog.error("Invalid input. Please enter a number.")
        elif not Number.isdigit():
            if self.error_level:
                colorlog.error("Invalid input. Please enter a number.")
            return False

        # Initialize an empty list to store each line of the ASCII art
        ascii_art_lines = []

        for i in range(7):  # Loop through each row
            line = ""
            for j in range(len(Number)):  # Loop through each character (digit) in the number
                current_num = int(Number[j])
                digit = self.digits[current_num]
                line += digit[i] + "  "  # Append the current digit's row to the line
            ascii_art_lines.append(line)  # Add the completed line to the list

        # Join all lines with newline characters to form the final ASCII art string
        ascii_art = "\n".join(ascii_art_lines)

        return ascii_art


"""
from --- import *

convert = Convert(show_errors=False)
print(convert.to_roman(5000))
print(convert.to_number("MMMCMXCIX"))
print(convert.to_ascii(3000))  # Optional, leave empty for dynamic user input
"""
