"""
------------------------------------------------------------------------------------------------------------------------

N = number of elements to process.
M = difference between the largest number and smallest number in the list.
K = integers length of the largest number in the list.

### Time Complexity
- **O(1)**:
  - [Log.info]
  - [Log.warning]
  - [Log.error]
  - [Log.critical]
  - [Convert.memory]

- **O(n)**:
  - [Find.value_index]
  - [Validate.email]
  - [Validate.url]
  - [Validate.phone_number]
  - [Convert.dec_to_roman]
  - [Convert.roman_to_dec]
  - [Find.total_vowels]
  - [Find.every_vowel]
  - [Convert.bin_to_dec]
  - [Convert.bin_to_hex]
  - [Convert.hex_to_bin]
  - [Convert.hex_to_dec]

- **O(n + m)**:
  - [Sort.using_counting_sort]

- **O(log n)**:
  - [Convert.dec_to_hex]
  - [Convert.dec_to_bin]

- **O(n log n)**:
  - [Find.largest]
  - [Find.smallest]
  - [Sort.using_quicksort]
  - [Sort.using_merge_sort]
  - [Sort.using_heap_sort]

- **O(n * k)**:
  - [Convert.dec_to_ascii]
  - [Sort.using_radix_sort]

- **O(n^2)**:
  - [Sort.using_selection]
  - [Sort.using_bubble]
  - [Sort.using_insertion]

- **O((n+1)! / 2) OR Unbounded(infinite)**:
  - [Sort.using_bogo_sort]

------------------------------------------------------------------------------------------------------------------------

### Space Complexity
- O(1):
  - [Find.value_index]
  - [Find.total_vowels]
  - [Find.every_vowel]
  - [Sort.using_selection]
  - [Sort.using_bubble]
  - [Sort.using_insertion]
  - [Sort.using_heap_sort]
  - [Convert.dec_to_ascii]
  - [Convert.dec_to_roman]
  - [Convert.roman_to_dec]
  - [Convert.bin_to_dec]
  - [Convert.bin_to_hex]
  - [Convert.hex_to_bin]
  - [Convert.hex_to_dec]
  - [Convert.dec_to_hex]
  - [Convert.dec_to_bin]
  - [Convert.memory]
  - [Sort.using_bogo_sort]
  - [Validate.email]
  - [Validate.url]
  - [Validate.phone_number]


- O(n):
  - [Find.largest]
  - [Find.smallest]
  - [Log.info]
  - [Log.warning]
  - [Log.error]
  - [Log.critical]
  - [Sort.using_merge_sort]

- **O(n + k)**:
  - [Sort.using_radix_sort]

- **O(n + m)**:
  - [Sort.using_counting_sort]

- O(log n):
  - [Sort.using_quicksort]

------------------------------------------------------------------------------------------------------------------------
"""
# Fun Fact: Interstellar + Undertale + Deltarune + Stardew + Terraria + Minecraft = Life

import heapq
import os
import random
import re
from datetime import datetime
import colorlog


# TODO redoc everything


class Log:
    def __init__(self, filename="Server.log", use_colorlog=True, DEBUG=False, debug_color="cyan", info_color="green",
                 warning_color="yellow", error_color="red", critical_color="red",
                 colorlog_fmt_parameters="%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"):
        """
        Initializes a new instance of the LOG class.

        The log class logs every interaction when called in both colorlog and in the log file

        Best to only modify filename, and DEBUG.

        Only if you are planning to use the dual-log parameter that allows you to both log unto the shell and the log file:
            IMPORTANT: This class requires colorlog to be installed and also uses it in the INFO level,
            To use the debug level, set DEBUG to True.

            If you are using colorlog, DO NOT INITIALIZE IT MANUALLY, USE THE LOG CLASS PARAMETER'S INSTEAD.
            Sorry for any inconvenience that may arise.

        Args:
            filename (str, optional): The name of the log file. Defaults to "Server.log".
            use_colorlog (bool, optional): Whether to use colorlog. Defaults to True.
            DEBUG (bool, optional): Whether to use the debug level. Defaults to False (which uses the INFO level).
            debug_color (str, optional): The color of the debug level. Defaults to "cyan".
            info_color (str, optional): The color of the info level. Defaults to "green".
            warning_color (str, optional): The color of the warning level. Defaults to "yellow".
            error_color (str, optional): The color of the error level. Defaults to "red".
            critical_color (str, optional): The color of the critical level. Defaults to "red".
            colorlog_fmt_parameters (str, optional): The format of the log message. Defaults to "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s".

        Returns:
            None
        """
        self.color = use_colorlog
        if self.color:
            # Configure colorlog for logging messages with colors
            logger = colorlog.getLogger()
            if DEBUG:
                logger.setLevel(colorlog.DEBUG)  # Set the log level to DEBUG to capture all relevant logs
            else:
                logger.setLevel(colorlog.INFO)  # Set the log level to INFO to capture all relevant logs
            handler = colorlog.StreamHandler()
            formatter = colorlog.ColoredFormatter(
                colorlog_fmt_parameters,
                datefmt=None,
                reset=True,
                log_colors={
                    "DEBUG": debug_color,
                    "INFO": info_color,
                    "WARNING": warning_color,
                    "ERROR": error_color,
                    "CRITICAL": critical_color,
                },
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        self.filename = str(filename)
        if not os.path.exists(self.filename):
            self.__only("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 154 + "|")
            self.__only("|     Timestamp     |  LOG Level  |" + " " * 71 + "LOG Messages" + " " * 71 + "|")
        self.__only("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 154 + "|")

    @staticmethod
    def __timestamp() -> str:
        """
        Returns the current timestamp as a string in the format 'YYYY-MM-DD HH:MM:SS'.

        Returns:
            str: The current timestamp.
        """
        now = datetime.now()
        time = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"
        return time

    def __only(self, message):
        """
        Logs a quick message to the log file.

        Args:
            message: The message to be logged.

        Returns:
            None
        """
        with open(self.filename, "a") as f:
            f.write(f"{str(message)}\n")

    @staticmethod
    def __pad_message(message):
        """
        Adds spaces to the end of a message until its length is exactly 153 characters.

        Parameters:
        - message (str): The input message string.

        Returns:
        - str: The padded message with a length of exactly 153 characters.
        """
        # Calculate the number of spaces needed
        num_spaces = 153 - len(message)

        if num_spaces > 0:
            # If the message is shorter than 153 characters, add spaces to the end
            padded_message = message + ' ' * num_spaces
        else:
            # If the message is already longer than 153 characters, truncate it to the first 153 characters
            padded_message = message[:150]
            padded_message += "..."

        padded_message += "|"
        return padded_message

    def info(self, message):
        """
        Logs an informational message to the log file.

        Args:
            message: The message to be logged.

        Returns:
            None
        """
        if self.color:
            colorlog.info(message)
        with open(self.filename, "a") as f:
            f.write(f"[{self.__timestamp()}] > INFO:     | {self.__pad_message(str(message))}\n")

    def warning(self, message):
        """
        Logs a warning message to the log file.

        Args:
            message: The warning message to be logged.

        Returns:
            None
        """
        if self.color:
            colorlog.warning(message)
        with open(self.filename, "a") as f:
            f.write(f"[{self.__timestamp()}] > WARNING:  | {self.__pad_message(str(message))}\n")

    def error(self, message):
        """
        Logs an error message to the log file.

        Args:
            message: The error message to be logged.

        Returns:
            None
        """
        if self.color:
            colorlog.error(message)
        with open(self.filename, "a") as f:
            f.write(f"[{self.__timestamp()}] > ERROR:    | {self.__pad_message(str(message))}\n")

    def critical(self, message):
        """
        Writes a critical message to the log file.

        Args:
            message: The critical message to be logged.

        Returns:
            None
        """
        if self.color:
            colorlog.critical(message)
        with open(self.filename, "a") as f:
            f.write(f"[{self.__timestamp()}] > CRITICAL: | {self.__pad_message(str(message))}\n")


class Find:
    def __init__(self):
        self.special_y_words = [
            "Cry",
            "Dry",
            "Gym",
            "Hymn",
            "Lynx",
            "Myth",
            "Pry",
            "Rhythm",
            "Shy",
            "Spy",
            "Spry",
            "Sync",
            "Try",
            "Why",
            "City",
            "Party",
            "Fly",
            "Shy",
            "Wary",
            "Worthwhile",
            "Type",
            "Typical",
            "Thyme",
            "Cyst",
            "Symbol",
            "System",
            "Lady",
            "Pretty",
            "Very",
            "Deny",
            "Daddy",
            "Quickly",
        ]

    @staticmethod
    def __sort(List):
        if List is None:
            raise Exception("No input given.")

        converted_list = sorted(
            float(item) for item in List if isinstance(item, (int, float))
        )
        final_list = [
            int(item) if item.is_integer() else item for item in converted_list
        ]
        return final_list

    def __vowel_y(self, string: str, only_lowercase=False):
        if string is None:
            raise Exception("No input given.")
        if self.__value_index(self.special_y_words, string):
            if only_lowercase:
                vowels = "aeiouy"
            else:
                vowels = "aeiouyAEIOUY"
        else:
            if only_lowercase:
                vowels = "aeiou"
            else:
                vowels = "aeiouAEIOU"
        return vowels

    @staticmethod
    def __count_character(Word, Vowel):
        count = 0
        for i in range(len(Word)):
            if Word[i] == Vowel:
                count += 1

        return f"{Vowel} {count}"

    @staticmethod
    def __value_index(array, Word):
        for index, value in enumerate(array):
            if value == Word:
                return True
        return False

    def largest_in_array(self, List: list[int | float]):
        if List is None:
            raise Exception("No input given.")
        largeList = self.__sort(List)
        if largeList is None:
            raise Exception("No input given.")
        return largeList[-1] if largeList else None

    def smallest_in_array(self, List: list[int | float]):
        if List is None:
            raise Exception("No input given.")
        smallList = self.__sort(List)
        if smallList is None:
            raise Exception("No input given.")
        return smallList[0] if smallList else None

    def total_vowels_in_string(self, Word: str):
        if Word is None:
            raise Exception("No input given.")
        vowels = self.__vowel_y(Word)
        vowel_count = sum(1 for char in Word if char in vowels)
        return vowel_count

    def every_vowel_in_string(self, Word: str):
        if Word is None:
            raise Exception("No input given.")
        result = ""
        vowels = self.__vowel_y(Word, True)
        for vowel in vowels:
            result += self.__count_character(Word, vowel) + "\n"
        return result.rstrip("\n")

    @staticmethod
    def value_index_in_array(List: list, value_to_find):
        if List is None or value_to_find is None:
            raise Exception("No input given.")
        for index, value in enumerate(List):
            if value == value_to_find:
                return index
        return False


class Sort:
    @staticmethod
    def __isinteger(Array):
        return all(isinstance(item, int) for item in Array)

    def using_quick_sort(self, Array):
        if Array is None:
            raise Exception("No input given.")
        if not self.__isinteger(Array):
            raise Exception("Input is not an integer array.")
        if len(Array) <= 1:
            return Array
        pivot = Array[len(Array) // 2]
        left = [x for x in Array if x < pivot]
        middle = [x for x in Array if x == pivot]
        right = [x for x in Array if x > pivot]
        return self.using_quick_sort(left) + middle + self.using_quick_sort(right)

    def using_merge_sort(self, Array):
        if Array is None:
            raise Exception("No input given.")
        if not self.__isinteger(Array):
            raise Exception("Input is not an integer array.")
        if len(Array) <= 1:
            return Array
        mid = len(Array) // 2
        left = Array[:mid]
        right = Array[mid:]
        return Sort.__merge(self.using_merge_sort(left), self.using_merge_sort(right))

    @staticmethod
    def __merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def using_selection_sort(self, Array):
        if Array is None:
            raise Exception("No input given.")
        if not self.__isinteger(Array):
            raise Exception("Input is not an integer array.")
        for i in range(len(Array)):
            min_index = i
            for j in range(i + 1, len(Array)):
                if Array[min_index] > Array[j]:
                    min_index = j
            Array[i], Array[min_index] = Array[min_index], Array[i]
        return Array

    def using_bubble_sort(self, Array):
        if Array is None:
            raise Exception("No input given.")
        if not self.__isinteger(Array):
            raise Exception("Input is not an integer array.")
        n = len(Array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if Array[j] > Array[j + 1]:
                    Array[j], Array[j + 1] = Array[j + 1], Array[j]
        return Array

    def using_insertion_sort(self, Array):
        if Array is None:
            raise Exception("No input given.")
        if not self.__isinteger(Array):
            raise Exception("Input is not an integer array.")
        for i in range(1, len(Array)):
            key = Array[i]
            j = i - 1
            while j >= 0 and key < Array[j]:
                Array[j + 1] = Array[j]
                j -= 1
            Array[j + 1] = key
        return Array

    def using_heap_sort(self, Array):
        if Array is None:
            raise Exception("No input given.")
        if not self.__isinteger(Array):
            raise Exception("Input is not an integer array.")
        heapq.heapify(Array)
        return [heapq.heappop(Array) for _ in range(len(Array))]

    def using_radix_sort(self, Array):
        if Array is None:
            raise Exception("No input given.")
        if not self.__isinteger(Array):
            raise Exception("Input is not an integer array.")
        max_value = max(Array)
        max_exponent = len(str(max_value))
        for exponent in range(max_exponent):
            digits = [[] for _ in range(10)]
            for num in Array:
                digit = (num // 10 ** exponent) % 10
                digits[digit].append(num)
            Array = []
            for digit_list in digits:
                Array.extend(digit_list)
        return Array

    def using_counting_sort(self, Array):
        if Array is None:
            raise Exception("No input given.")
        if not self.__isinteger(Array):
            raise Exception("Input is not an integer array.")
        max_value = max(Array)
        min_value = min(Array)
        range_of_elements = max_value - min_value + 1
        count = [0] * range_of_elements
        output = [0] * len(Array)
        for num in Array:
            count[num - min_value] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        for num in reversed(Array):
            output[count[num - min_value] - 1] = num
            count[num - min_value] -= 1
        return output

    def using_bogo_sort(self, Array):
        if Array is None:
            raise Exception("No input given.")
        if not self.__isinteger(Array):
            raise Exception("Input is not an integer array.")

        while not self.__is_sorted(Array):
            random.shuffle(Array)
        return Array

    @staticmethod
    def __is_sorted(Array):
        return all(Array[i] <= Array[i + 1] for i in range(len(Array) - 1))


class Validate:
    def __init__(self):
        self.url = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?$'
        self.email = r'^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.phone = r'^\+?[0-9]{1,3}?[ -]?[0-9]{1,3}?[ -]?[0-9]{1,4}$'

    def this_email(self, email_address):
        if len(email_address) < 1 or len(email_address) > 320:
            return False

        if ' ' in email_address:
            return False

        if not re.match(self.email, email_address):
            return False

        return True

    def this_url(self, url_string):
        if ' ' in url_string:
            return False

        # Compile the regular expression pattern once to improve performance
        compiled_pattern = re.compile(self.url)

        # Check if the input string matches the compiled pattern
        return bool(compiled_pattern.search(url_string))

    def this_phone_number(self, phone_number):
        pattern = re.compile(self.phone)
        return bool(pattern.match(phone_number))

    class CreditCard:
        @staticmethod
        def __luhn_algorithm(card_number: int) -> bool:
            """
            Validates a card number using the Luhn algorithm.

            Args:
                card_number (int): The card number to validate.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            num_list = [int(digit) for digit in str(card_number)]
            num_list.reverse()
            total = 0
            for i, num in enumerate(num_list):
                doubled = num * 2
                if doubled > 9:
                    doubled -= 9
                total += doubled
            return total % 10 == 0

        @classmethod
        def american_express(cls, card_number: int) -> bool:
            """
            Validates American Express card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(('34', '37')) and 15 <= len(str(card_number)) <= 16)

        @classmethod
        def china_unionpay(cls, card_number: int) -> bool:
            """
            Validates China UnionPay card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (str(card_number).startswith(
                ('62', '64', '65', '66', '67', '68', '69', '92', '93', '94', '95', '96', '97', '98',
                 '99')) and 16 <= len(
                str(card_number)))

        @classmethod
        def dankort(cls, card_number: int) -> bool:
            """
            Validates Dankort card numbers.
            """
            return cls.__luhn_algorithm(card_number) and str(card_number).startswith('49') and 16 <= len(
                str(card_number))

        @classmethod
        def diners_club(cls, card_number: int) -> bool:
            """
            Validates Diners Club International card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(('36', '38')) and 14 <= len(str(card_number)) <= 19)

        @classmethod
        def discover(cls, card_number: int) -> bool:
            """
            Validates Discover card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(('6011', '6221', '6222', '6223', '623',
                                                 '624', '625', '626', '627', '628', '641',
                                                 '642', '643', '644', '645', '646', '647',
                                                 '648', '649', '65', '66', '67', '68',
                                                 '69', '71', '72', '73', '74', '75', '76',
                                                 '77', '78', '79')) and 16 <= len(str(card_number)))

        @classmethod
        def jcb(cls, card_number: int) -> bool:
            """
            Validates JCB card numbers.
            """
            return cls.__luhn_algorithm(card_number) and str(card_number).startswith('35') and 16 <= len(
                str(card_number))

        @classmethod
        def maestro(cls, card_number: int) -> bool:
            """
            Validates Maestro card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(('50', '51', '52', '53', '54', '55', '56',
                                                 '57', '58', '60', '61', '62', '63', '64',
                                                 '65', '66', '67', '68', '69', '70', '71',
                                                 '72', '73', '74', '75', '76', '77', '78',
                                                 '79')) and 12 <= len(str(card_number)) <= 19)

        @classmethod
        def mastercard(cls, card_number: int) -> bool:
            """
            Validates Mastercard card numbers.
            """
            return cls.__luhn_algorithm(card_number) and str(card_number).startswith(
                ('51', '52', '53', '54', '55', '56', '57', '58', '59')) and 16 <= len(str(card_number))

        @classmethod
        def visa(cls, card_number: int) -> bool:
            """
            Validates Visa card numbers.
            """
            return cls.__luhn_algorithm(card_number) and str(card_number).startswith('4') and 13 <= len(
                str(card_number)) <= 16

        @classmethod
        def visa_electron(cls, card_number: int) -> bool:
            """
            Validates Visa Electron card numbers.
            """
            return cls.__luhn_algorithm(card_number) and str(card_number).startswith(
                ('40', '41', '42', '43', '44', '45', '46', '47', '48', '49')) and 16 <= len(str(card_number))

        @classmethod
        def v_pay(cls, card_number: int) -> bool:
            """
            Validates V Pay card numbers.
            """
            return cls.__luhn_algorithm(card_number) and str(str(card_number)).startswith('28') and 16 <= len(
                str(str(card_number)))

        @classmethod
        def any(cls, card_number: int) -> bool:
            """
            Validates any card number just by passing it to the Luhn algorithm.
            """
            return cls.__luhn_algorithm(card_number)


# TODO Credit Card Number Validation


class Convert:
    def __init__(self, show_warnings=False):
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
        self.memory_dict = {
            'Bit': 1,
            'Byte': 8,
            'KB': 8 * 1000,
            'MB': 8 * (1000 ** 2),
            'GB': 8 * (1000 ** 3),
            'TB': 8 * (1000 ** 4),
            'PB': 8 * (1000 ** 5),
            'KiB': 8 * 1024,
            'MiB': 8 * (1024 ** 2),
            'GiB': 8 * (1024 ** 3),
            'TiB': 8 * (1024 ** 4),
            'PiB': 8 * (1024 ** 5),
            'Kb': 1000,
            'Mb': 1000 ** 2,
            'Gb': 1000 ** 3,
            'Tb': 1000 ** 4,
            'Pb': 1000 ** 5,
            'Kib': 1024,
            'Mib': 1024 ** 2,
            'Gib': 1024 ** 3,
            'Tib': 1024 ** 4,
            'Pib': 1024 ** 5,
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
        self.show_warnings = show_warnings

    def dec_to_roman(self, Number):
        if Number is None:
            raise Exception("No input given.")
        Number = int(Number)
        if Number <= 1:
            raise Exception("Input must be greater or equal to 1.")
        if Number > 10000 and self.show_warnings:
            print(
                "Input is too large. This may result in inaccurate results."
            )

        result = ""
        for numerical, roman in sorted(self.mapping.items(), reverse=True):
            while Number >= numerical:
                result += roman
                Number -= numerical
        return result

    def roman_to_dec(self, Roman):
        if not isinstance(Roman, str):
            raise Exception("Input must be a string.")
        elif not Roman.isupper():
            raise Exception("Input must be uppercase.")
        elif Roman is None:
            raise Exception("Input cannot be None.")
        i = 0
        num = 0
        Roman = Roman.upper()
        while i < len(Roman):
            if i + 1 < len(Roman) and Roman[i: i + 2] in self.roman_to_numerical:
                num += self.roman_to_numerical[Roman[i: i + 2]]
                i += 2
            else:
                num += self.roman_to_numerical[Roman[i]]
                i += 1
        return num

    def dec_to_ascii(self, Number):
        if Number is None:
            raise Exception("No input given.")
        elif not Number.isdigit():
            raise Exception("Invalid input. Please enter a number.")
        ascii_art_lines = []
        for i in range(7):
            line = ""
            for j in range(
                    len(Number)
            ):
                current_num = int(Number[j])
                digit = self.digits[current_num]
                line += digit[i] + "  "
            ascii_art_lines.append(line)
        ascii_art = "\n".join(ascii_art_lines)
        return ascii_art

    @staticmethod
    def __check_input_type(value, expected_type):
        if not isinstance(value, expected_type):
            raise Exception(f"Expected {expected_type.__name__}, got {type(value).__name__}")
        return True

    def bin_to_hex(self, Binary_Number):
        if Binary_Number is None:
            raise Exception("Conversion failed: No binary number provided")
        Binary_Number = str(Binary_Number)
        if not self.__check_input_type(Binary_Number, str):
            return False
        Hexadecimal_Number = hex(int(Binary_Number, 2))[2:]
        return Hexadecimal_Number.upper()

    def bin_to_dec(self, Binary_Number):
        if Binary_Number is None:
            raise Exception("Conversion failed: No binary number provided")
        Binary_Number = str(Binary_Number)
        if not self.__check_input_type(Binary_Number, str):
            return False
        return int(Binary_Number, 2)

    def dec_to_hex(self, Decimal_Number):
        Decimal_Number = int(Decimal_Number)
        if Decimal_Number is None:
            raise Exception("Conversion failed: No decimal number provided")
        if not self.__check_input_type(Decimal_Number, (int, str)):
            return False
        Hexadecimal_Number = hex(Decimal_Number)[2:]
        return Hexadecimal_Number.upper()

    def dec_to_bin(self, Decimal_Number):
        Decimal_Number = int(Decimal_Number)
        if Decimal_Number is None:
            raise Exception("Conversion failed: No decimal number provided")
        if not self.__check_input_type(Decimal_Number, (int, str)):
            return False
        Binary_Number = bin(Decimal_Number)[2:]
        return Binary_Number

    def hex_to_bin(self, Hexadecimal_Number):
        if Hexadecimal_Number is None:
            raise Exception("Conversion failed: No hexadecimal number provided")
        if not self.__check_input_type(Hexadecimal_Number, str):
            return False
        Binary_Number = bin(int(Hexadecimal_Number, 16))[2:]
        return Binary_Number

    def hex_to_dec(self, Hexadecimal_Number):
        if Hexadecimal_Number is None:
            raise Exception("Conversion failed: No hexadecimal number provided")
        if not self.__check_input_type(Hexadecimal_Number, str):
            return False
        return int(Hexadecimal_Number, 16)

    def memory(self, number, input_unit, output_unit):
        if number is None or input_unit is None or output_unit is None:
            raise Exception("Invalid input. Number, input_unit, and output_unit must all be provided.")
        if not isinstance(number, int) or input_unit not in self.memory_dict or output_unit not in self.memory_dict:
            raise Exception("Invalid input. Number must be an integer, and both units must exist in memory_dict.")
        input_factor = self.memory_dict[input_unit]
        number_in_bits = number * input_factor
        output_factor = self.memory_dict[output_unit]
        final_number = number_in_bits / output_factor
        return f"{final_number:.2f} {output_unit}"
