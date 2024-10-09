# TODO Create a repo that uses this credit card validator to create a credit card printer

# TODO Separate these files as an actual library

import re
import inspect
import os
from datetime import datetime
import colorlog
import logging
from typing import Type


# TODO Create algopy faker.js alt

# TODO Redo all Algopy to include the following:
#    Block sort
#    Tournament sort
#    Comb sort
#    Gnome sort
#    Quick sort
#    Selection sort
#    Stooge sort
#    Strand sort
#    Tree sort
#    Cycle sort
#    Library sort
#    Patience sort
#    Smooth sort
#    Bucket Sort
#    Bingo Sort Algorithm
#    ShellSort
#    Comb Sort
#    Pigeonhole Sort
#    Cycle Sort
#    Cocktail Sort
#    Strand Sort
#    Bitonic Sort
#    Pancake sorting
#    Stooge Sort
#    Tag Sort (To get both sorted and original)
#    Brick Sort
#    3-way Merge Sort
#    Dual-Pivot Quicksort
#    Flash_sort


# DONE
class Log:
    """
    A logging class that supports colored output using the colorlog library.
    """

    def __init__(self, config: dict = None):
        """
        Initializes the Log class with the given configuration.

        :param config: A dictionary containing configuration options.
        """
        config = config or {
            "filename": "../ACCESS/LOGS/Logicytics.log",
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
        self.filename = config.get("filename", "../ACCESS/LOGS/Logicytics.log")
        if self.color:
            logger = colorlog.getLogger()
            logger.setLevel(getattr(logging, config["log_level"].upper(), logging.INFO))
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
                config.get(
                    "colorlog_fmt_parameters",
                    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
                ),
                log_colors=log_colors,
            )

            handler.setFormatter(formatter)
            logger.addHandler(handler)
            try:
                getattr(logging, config["log_level"].upper())
            except AttributeError as AE:
                self.__internal(
                    f"Log Level {config['log_level']} not found, setting default level to INFO -> {AE}"
                )

        if not os.path.exists(self.filename):
            self.newline()
            self.raw(
                "|     Timestamp     |  LOG Level  |"
                + " " * 71
                + "LOG Messages"
                + " " * 71
                + "|"
            )
        self.newline()

    @staticmethod
    def __timestamp() -> str:
        """
        Returns the current timestamp as a string.

        :return: Current timestamp in 'YYYY-MM-DD HH:MM:SS' format.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def __pad_message(message: str) -> str:
        """
        Pads or truncates the message to fit the log format.

        :param message: The log message to be padded or truncated.
        :return: The padded or truncated message.
        """
        return (
            message + " " * (153 - len(message))
            if len(message) < 153
            else message[:150] + "..."
        ) + "|"

    def raw(self, message):
        """
        Logs a raw message directly to the log file.

        :param message: The raw message to be logged.
        """
        frame = inspect.stack()[1]
        if frame.function == "<module>":
            self.__internal(
                f"Raw message called from a non-function - This is not recommended"
            )
        if message != "None" and message is not None:
            with open(self.filename, "a") as f:
                f.write(f"{str(message)}\n")

    def newline(self):
        """
        Logs a newline separator in the log file.
        """
        with open(self.filename, "a") as f:
            f.write("|" + "-" * 19 + "|" + "-" * 13 + "|" + "-" * 154 + "|" + "\n")

    def info(self, message):
        """
        Logs an info message.

        :param message: The info message to be logged.
        """
        if self.color and message != "None" and message is not None:
            colorlog.info(str(message))
        self.raw(
            f"[{self.__timestamp()}] > INFO:     | {self.__pad_message(str(message))}"
        )

    def warning(self, message):
        """
        Logs a warning message.

        :param message: The warning message to be logged.
        """
        if self.color and message != "None" and message is not None:
            colorlog.warning(str(message))
        self.raw(
            f"[{self.__timestamp()}] > WARNING:  | {self.__pad_message(str(message))}"
        )

    def error(self, message):
        """
        Logs an error message.

        :param message: The error message to be logged.
        """
        if self.color and message != "None" and message is not None:
            colorlog.error(str(message))
        self.raw(
            f"[{self.__timestamp()}] > ERROR:    | {self.__pad_message(str(message))}"
        )

    def critical(self, message):
        """
        Logs a critical message.

        :param message: The critical message to be logged.
        """
        if self.color and message != "None" and message is not None:
            colorlog.critical(str(message))
        self.raw(
            f"[{self.__timestamp()}] > CRITICAL: | {self.__pad_message(str(message))}"
        )

    @staticmethod
    def debug(message):
        """
        Logs a debug message.

        :param message: The debug message to be logged.
        """
        if message != "None" and message is not None:
            colorlog.debug(str(message))

    def string(self, message, type: str):
        """
        Logs a message with a specified type. Supported types are 'debug', 'info', 'warning', 'error', 'critical'
        as well as the aliases 'err', 'warn', and 'crit'.

        :param message: The message to be logged.
        :param type: The type of the log message.
        """
        if self.color and message != "None" and message is not None:
            type_map = {"err": "error", "warn": "warning", "crit": "critical"}
            type = type_map.get(type.lower(), type)
            try:
                getattr(self, type.lower())(str(message))
            except AttributeError as AE:
                self.__internal(f"A wrong Log Type was called: {type} not found. -> {AE}")
                getattr(self, "Debug".lower())(str(message))

    def exception(self, message, exception_type: Type = Exception):
        """
        Logs an exception message.

        :param message: The exception message to be logged.
        :param exception_type: The type of exception to raise.
        """
        if self.color and message != "None" and message is not None:
            self.raw(
                f"[{self.__timestamp()}] > EXCEPTION:| {self.__pad_message(f'{message} -> Exception provoked: {str(exception_type)}')}"
            )
        raise exception_type(message)

    def __internal(self, message):
        """
        Logs an internal message.

        :param message: The internal message to be logged.
        """
        if self.color and message != "None" and message is not None:
            colorlog.log(self.INTERNAL_LOG_LEVEL, str(message))


# DONE
class Validate:
    @staticmethod
    def this_email(email_address: str) -> bool:
        """
        Validates an email address against a set of predefined rules.

        Args:
            email_address (str): The email address to be validated.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        if len(email_address) < 1 or len(email_address) > 320:
            return False
        if " " in email_address:
            return False
        pattern = re.compile(r"^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        return bool(pattern.search(email_address))

    @staticmethod
    def this_url(url_string: str) -> bool:
        """
        Validates a URL against a set of predefined rules.

        Args:
            url_string (str): The URL to be validated.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """
        if " " in url_string:
            return False
        pattern = re.compile(r"^(https?://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w.-]*)*/?$")
        return bool(pattern.search(url_string))

    @staticmethod
    def this_phone_number(phone_number: int | str) -> bool:
        pattern = re.compile(r"^(\(\d{3}\)[\s-]?)?\d{3}[\s-]?\d{4}[\s-]?\d{3}$")
        return bool(pattern.match(str(phone_number)))

    @staticmethod
    def this_date(date: str) -> bool:
        date = date.replace("/", "-")
        date = date.replace("\\", "-")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            try:
                datetime.strptime(date, "%d-%m-%Y")
                return True
            except ValueError:
                return False

    class CreditCard:
        def __init__(self):
            """
            Validates a card number using the Luhn algorithm.
            Specify in specifics inside the class.

            Returns a boolean value if the card number is valid or not.
            """
            pass

        @staticmethod
        def __luhn_algorithm(card_number: int) -> bool:
            """
            Validates a card number using the Luhn algorithm.

            Args:
                card_number (int): The card number to validate.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            if len(str(card_number)) < 13 or len(str(card_number)) > 19:
                return False
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
                    str(card_number).startswith(("34", "37"))
                    and 15 <= len(str(card_number)) <= 16
            )

        @classmethod
        def china_unionpay(cls, card_number: int) -> bool:
            """
            Validates China UnionPay card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(
                        (
                            "62",
                            "64",
                            "65",
                            "66",
                            "67",
                            "68",
                            "69",
                            "92",
                            "93",
                            "94",
                            "95",
                            "96",
                            "97",
                            "98",
                            "99",
                        )
                    )
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def dankort(cls, card_number: int) -> bool:
            """
            Validates Dankort card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith("49")
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def diners_club(cls, card_number: int) -> bool:
            """
            Validates Diners Club International card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(("36", "38"))
                    and 14 <= len(str(card_number)) <= 19
            )

        @classmethod
        def discover(cls, card_number: int) -> bool:
            """
            Validates Discover card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(
                        (
                            "6011",
                            "6221",
                            "6222",
                            "6223",
                            "623",
                            "624",
                            "625",
                            "626",
                            "627",
                            "628",
                            "641",
                            "642",
                            "643",
                            "644",
                            "645",
                            "646",
                            "647",
                            "648",
                            "649",
                            "65",
                            "66",
                            "67",
                            "68",
                            "69",
                            "71",
                            "72",
                            "73",
                            "74",
                            "75",
                            "76",
                            "77",
                            "78",
                            "79",
                        )
                    )
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def jcb(cls, card_number: int) -> bool:
            """
            Validates JCB card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith("35")
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def maestro(cls, card_number: int) -> bool:
            """
            Validates Maestro card numbers.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(
                        (
                            "50",
                            "51",
                            "52",
                            "53",
                            "54",
                            "55",
                            "56",
                            "57",
                            "58",
                            "60",
                            "61",
                            "62",
                            "63",
                            "64",
                            "65",
                            "66",
                            "67",
                            "68",
                            "69",
                            "70",
                            "71",
                            "72",
                            "73",
                            "74",
                            "75",
                            "76",
                            "77",
                            "78",
                            "79",
                        )
                    )
                    and 12 <= len(str(card_number)) <= 19
            )

        @classmethod
        def mastercard(cls, card_number: int) -> bool:
            """
            Validates Mastercard card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith(("51", "52", "53", "54", "55", "56", "57", "58", "59"))
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def visa(cls, card_number: int) -> bool:
            """
            Validates Visa card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith("4")
                    and 13 <= len(str(card_number)) <= 16
            )

        @classmethod
        def visa_electron(cls, card_number: int) -> bool:
            """
            Validates Visa Electron card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith(("40", "41", "42", "43", "44", "45", "46", "47", "48", "49"))
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def v_pay(cls, card_number: int) -> bool:
            """
            Validates V Pay card numbers.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(str(card_number)).startswith("28")
                    and 16 <= len(str(str(card_number)))
            )

        @classmethod
        def any(cls, card_number: int) -> bool:
            """
            Validates any card number just by passing it to the Luhn algorithm.
            """
            return cls.__luhn_algorithm(card_number)


# DONE
class Convert:
    class Binary:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            if not isinstance(value, expected_type):
                raise Exception(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return True

        @classmethod
        def to_hex(cls, Binary_Number: int) -> str:
            if Binary_Number is None:
                raise Exception("No binary number provided")
            cls.__check_input_type(str(Binary_Number), str)
            return hex(int(str(Binary_Number), 2))[2:].upper()

        @classmethod
        def to_dec(cls, Binary_Number: int) -> int:
            if Binary_Number is None:
                raise Exception("No binary number provided")
            cls.__check_input_type(str(Binary_Number), str)
            return int(str(Binary_Number), 2)

    class Decimal:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            if not isinstance(value, expected_type):
                raise Exception(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return True

        @staticmethod
        def to_roman(Number: int) -> str:
            mapping = {
                1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
                50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
            }
            if Number is None or Number < 1:
                raise Exception("Invalid input.")
            result = ""
            for num, roman in sorted(mapping.items(), reverse=True):
                while Number >= num:
                    result += roman
                    Number -= num
            return result

        @staticmethod
        def to_ascii(Number: int | str) -> str:
            digits = [
                ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "],
                [" * ", "** ", " * ", " * ", " * ", " * ", "***"],
                [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"],
                [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "],
                ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "],
                ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "],
                [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "],
                ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "],
                [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "],
                [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
            ]
            Number = str(Number)
            if Number is None:
                raise Exception("No input given.")
            ascii_art_lines = ["".join(digits[int(digit)][i] + "  " for digit in Number) for i in range(7)]
            return "\n".join(ascii_art_lines)

        @classmethod
        def to_hex(cls, Decimal_Number: int) -> str:
            if Decimal_Number is None:
                raise Exception("No decimal number provided")
            cls.__check_input_type(Decimal_Number, (int, str))
            return hex(Decimal_Number)[2:].upper()

        @classmethod
        def to_bin(cls, Decimal_Number: int) -> int:
            if Decimal_Number is None:
                raise Exception("No decimal number provided")
            cls.__check_input_type(Decimal_Number, (int, str))
            return int(bin(Decimal_Number)[2:])

    class Hexadecimal:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            if not isinstance(value, expected_type):
                raise Exception(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return True

        @classmethod
        def to_bin(cls, Hexadecimal_Number: str) -> int:
            if Hexadecimal_Number is None:
                raise Exception("No hexadecimal number provided")
            cls.__check_input_type(Hexadecimal_Number, str)
            return int(bin(int(Hexadecimal_Number, 16))[2:])

        @classmethod
        def to_dec(cls, Hexadecimal_Number: str) -> int:
            if Hexadecimal_Number is None:
                raise Exception("No hexadecimal number provided")
            cls.__check_input_type(Hexadecimal_Number, str)
            return int(Hexadecimal_Number, 16)

    class Roman:
        @staticmethod
        def to_dec(Roman: str) -> int:
            roman_to_numerical = {
                "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
            }
            if not isinstance(Roman, str):
                raise Exception("Input must be a string.")
            elif not Roman.isupper():
                raise Exception("Input must be uppercase.")
            elif Roman is None:
                raise Exception("Input cannot be None.")
            i, num = 0, 0
            Roman = Roman.upper()
            while i < len(Roman):
                if i + 1 < len(Roman) and Roman[i: i + 2] in roman_to_numerical:
                    num += roman_to_numerical[Roman[i: i + 2]]
                    i += 2
                else:
                    num += roman_to_numerical[Roman[i]]
                    i += 1
            return num

    class Celsius:
        @staticmethod
        def to_fahrenheit(celsius: float | int) -> float:
            if celsius is None:
                raise Exception("No temperature provided")
            return (celsius * 9 / 5) + 32

        @staticmethod
        def to_kelvin(celsius: float | int) -> float:
            if celsius is None:
                raise Exception("No temperature provided")
            return celsius + 273.15

    class Kelvin:
        @staticmethod
        def to_celsius(kelvin: float | int) -> float:
            if kelvin is None:
                raise Exception("No temperature provided")
            return kelvin - 273.15

        @staticmethod
        def to_fahrenheit(kelvin: float | int) -> float:
            if kelvin is None:
                raise Exception("No temperature provided")
            return (kelvin - 273.15) * 9 / 5 + 32

    class Fahrenheit:
        @staticmethod
        def to_kelvin(fahrenheit: float | int) -> float:
            if fahrenheit is None:
                raise Exception("No temperature provided")
            return (fahrenheit - 32) * 5 / 9 + 273.15

        @staticmethod
        def to_celsius(fahrenheit: float | int) -> float:
            if fahrenheit is None:
                raise Exception("No temperature provided")
            return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def memory(number: int, input_unit: str, output_unit: str) -> str:
        memory_dict = {
            "bit": 1, "byte": 8, "kilobyte": 8000, "megabyte": 8 * (1000 ** 2), "gigabyte": 8 * (1000 ** 3),
            "terrabyte": 8 * (1000 ** 4), "petabyte": 8 * (1000 ** 5), "kibibyte": 8192, "mebibyte": 8 * (1024 ** 2),
            "gibibyte": 8 * (1024 ** 3), "tebibyte": 8 * (1024 ** 4), "pebibyte": 8 * (1024 ** 5),
            "kilobit": 1000, "megabit": 1000 ** 2, "gigabit": 1000 ** 3, "terrabit": 1000 ** 4, "petabit": 1000 ** 5,
            "kibibit": 1024, "mebibit": 1024 ** 2, "gibibit": 1024 ** 3, "tebibit": 1024 ** 4, "pebibit": 1024 ** 5,
            "KB": 8000, "MB": 8 * (1000 ** 2), "GB": 8 * (1000 ** 3), "TB": 8 * (1000 ** 4), "PB": 8 * (1000 ** 5),
            "KiB": 8192, "MiB": 8 * (1024 ** 2), "GiB": 8 * (1024 ** 3), "TiB": 8 * (1024 ** 4), "PiB": 8 * (1024 ** 5),
            "Kb": 1000, "Mb": 1000 ** 2, "Gb": 1000 ** 3, "Tb": 1000 ** 4, "Pb": 1000 ** 5,
            "Kib": 1024, "Mib": 1024 ** 2, "Gib": 1024 ** 3, "Tib": 1024 ** 4, "Pib": 1024 ** 5
        }
        if not all([number, input_unit, output_unit]):
            raise Exception(f"Invalid input: {number} {input_unit} -> {output_unit}")
        if input_unit == output_unit:
            return f"{number} {output_unit}"
        input_unit = input_unit.lower() if len(input_unit) > 3 and input_unit.lower() != "bit" else input_unit
        output_unit = output_unit.lower() if len(output_unit) > 3 and output_unit.lower() != "bit" else output_unit
        if not isinstance(number, int) or input_unit not in memory_dict or output_unit not in memory_dict:
            raise Exception(f"Invalid input: {number} {input_unit} -> {output_unit}")
        final_number = (number * memory_dict[input_unit]) / memory_dict[output_unit]
        return f"{final_number:.15f}".rstrip('0').rstrip('.') + f" {output_unit}"


# DONE
class Find:
    class InArray:
        @staticmethod
        def __sort(List: list) -> list[int | float]:
            if List is None:
                raise Exception("No input given.")
            converted_list = sorted(float(item) for item in List if isinstance(item, (int, float)))
            return [int(item) if item.is_integer() else item for item in converted_list]

        @classmethod
        def largest_number(cls, List: list[int | float]) -> int | float:
            if List is None:
                raise Exception("No input given.")
            sorted_list = cls.__sort(List)
            return sorted_list[-1] if sorted_list else None

        @classmethod
        def smallest_number(cls, List: list[int | float]) -> int | float:
            if List is None:
                raise Exception("No input given.")
            sorted_list = cls.__sort(List)
            return sorted_list[0] if sorted_list else None

        class Objects:
            @staticmethod
            def index_all(List: list, value_to_find: any) -> list[int]:
                if List is None or value_to_find is None:
                    raise Exception("No input given.")
                return [index for index, value in enumerate(List) if value == value_to_find]

            @staticmethod
            def index(List: list, value_to_find: any) -> int | bool:
                if List is None or value_to_find is None:
                    raise Exception("No input given.")
                try:
                    return List.index(value_to_find)
                except ValueError:
                    return False

    class InSentence:
        @staticmethod
        def longest_word(text: str) -> str:
            if text is None:
                raise Exception("No input given.")
            words = text.split()
            return max(words, key=len) if words else ""

        @staticmethod
        def shortest_word(text: str) -> str:
            if text is None:
                raise Exception("No input given.")
            words = text.split()
            return min(words, key=len) if words else ""

        class Word:
            @staticmethod
            def exists(text: str, word_to_find: str) -> bool:
                if text is None or word_to_find is None:
                    raise Exception("No input given.")
                return word_to_find in text

            @staticmethod
            def occurrences(text: str, word_to_count: str) -> int:
                if text is None or word_to_count is None:
                    raise Exception("No input given.")
                return text.lower().split().count(word_to_count.lower())

    class InWord:
        @classmethod
        def total_vowels(cls, Word: str) -> int:
            if Word is None:
                raise Exception("No input given.")
            vowels = cls.__vowel_y(Word)
            return sum(1 for char in Word if char in vowels)

        @classmethod
        def every_vowel(cls, Word: str) -> str:
            if Word is None:
                raise Exception("No input given.")
            vowels = cls.__vowel_y(Word, True)
            # TODO Turn to json
            return "\n".join(f"{vowel} {Word.count(vowel)}" for vowel in vowels)

        @staticmethod
        def __vowel_y(string: str, only_lowercase=False) -> str:
            if string is None:
                raise Exception("No input given.")
            if string in [
                "Cry", "Dry", "Gym", "Hymn", "Lynx", "Myth", "Pry", "Rhythm", "Shy", "Spy", "Spry", "Sync", "Try",
                "Why",
                "City", "Party", "Fly", "Shy", "Wary", "Worthwhile", "Type", "Typical", "Thyme", "Cyst", "Symbol",
                "System",
                "Lady", "Pretty", "Very", "Deny", "Daddy", "Quickly",
            ]:
                return "aeiouy" if only_lowercase else "aeiouyAEIOUY"
            return "aeiou" if only_lowercase else "aeiouAEIOU"
