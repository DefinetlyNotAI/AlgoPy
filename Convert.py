

from colorlog_setup import *


class Convert:
    def __init__(self, show_errors=True):
        """
        Initializes the Convert class with default show_errors set to True.

        Parameters:
            show_errors (bool): Flag to indicate whether to show errors. Default is True.

        Returns:
            None
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

        Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]

        One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]

        Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]

        Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]

        Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]

        Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]

        Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]

        Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]

        Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]

        Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

        self.digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
        self.error_level = show_errors

    def to_roman(self, num):
        """
        Converts an integer to a Roman numeral representation.

        Args:
            num (int): The integer to be converted.

        Returns:
            str: The Roman numeral representation of the input integer.

        Raises:
            KeyError: If the input integer is invalid.
            Exception: If an error occurs during the conversion process.

        Notes:
            - The input integer must be greater than or equal to 1.
            - If the input integer is greater than 10,000, a warning is raised.
            - If an error occurs during the conversion process, an error message is displayed if `show_errors` is True.
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
        Converts a Roman numeral to its corresponding decimal number.

        Args:
            roman (str): The Roman numeral to be converted.

        Returns:
            int: The decimal number corresponding to the input Roman numeral.

        Raises:
            KeyError: If the input Roman numeral is invalid.
            Exception: If an error occurs during the conversion process.

        Notes:
            - The input Roman numeral must be in uppercase.
            - If the input Roman numeral is invalid, an error message is displayed if `show_errors` is True.

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
        Generate ASCII art based on the input number and return the ASCII art as a string.

        Parameters:
            Number (str): The number to be converted to ASCII art.

        Returns:
            str: The ASCII art representation of the input number.
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
            for j in range(
                    len(Number)
            ):  # Loop through each character (digit) in the number
                current_num = int(Number[j])
                digit = self.digits[current_num]
                line += digit[i] + "  "  # Append the current digit's row to the line
            ascii_art_lines.append(line)  # Add the completed line to the list

        # Join all lines with newline characters to form the final ASCII art string
        ascii_art = "\n".join(ascii_art_lines)

        return ascii_art


"""
from Convert import *

convert = Convert(show_errors=False)

print(convert.to_roman(5000))
print(convert.to_number("MMMCMXCIX"))
print(convert.to_ascii(3000))  # Optional, leave empty for dynamic user input
"""
