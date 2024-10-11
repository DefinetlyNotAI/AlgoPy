class Convert:
    class Binary:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            """
            Check if the input value is of the expected type.

            :param value: The value to check.
            :param expected_type: The expected type of the value.
            :return: True if the value is of the expected type, otherwise raises an Exception.
            """
            if not isinstance(value, expected_type):
                raise Exception(
                    f"Expected {expected_type.__name__}, got {type(value).__name__}"
                )
            return True

        @classmethod
        def to_hex(cls, Binary_Number: int) -> str:
            """
            Convert a binary number to its hexadecimal representation.

            :param Binary_Number: The binary number to convert.
            :return: The hexadecimal representation of the binary number.
            """
            if Binary_Number is None:
                raise Exception("No binary number provided")
            cls.__check_input_type(str(Binary_Number), str)
            return hex(int(str(Binary_Number), 2))[2:].upper()

        @classmethod
        def to_dec(cls, Binary_Number: int) -> int:
            """
            Convert a binary number to its decimal representation.

            :param Binary_Number: The binary number to convert.
            :return: The decimal representation of the binary number.
            """
            if Binary_Number is None:
                raise Exception("No binary number provided")
            cls.__check_input_type(str(Binary_Number), str)
            return int(str(Binary_Number), 2)

    class Decimal:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            """
            Check if the input value is of the expected type.

            :param value: The value to check.
            :param expected_type: The expected type of the value.
            :return: True if the value is of the expected type, otherwise raises an Exception.
            """
            if not isinstance(value, expected_type):
                raise Exception(
                    f"Expected {expected_type.__name__}, got {type(value).__name__}"
                )
            return True

        @staticmethod
        def to_roman(Number: int) -> str:
            """
            Convert a decimal number to its Roman numeral representation.

            :param Number: The decimal number to convert.
            :return: The Roman numeral representation of the decimal number.
            """
            mapping = {
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
            """
            Convert a decimal number to its ASCII art representation.

            :param Number: The decimal number to convert.
            :return: The ASCII art representation of the decimal number.
            """
            digits = [
                [
                    "  ***  ",
                    " *   * ",
                    "*     *",
                    "*     *",
                    "*     *",
                    " *   * ",
                    "  ***  ",
                ],
                [" * ", "** ", " * ", " * ", " * ", " * ", "***"],
                [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"],
                [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "],
                ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "],
                ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "],
                [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "],
                ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "],
                [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "],
                [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"],
            ]
            Number = str(Number)
            if Number is None:
                raise Exception("No input given.")
            ascii_art_lines = [
                "".join(digits[int(digit)][i] + "  " for digit in Number)
                for i in range(7)
            ]
            return "\n".join(ascii_art_lines)

        @classmethod
        def to_hex(cls, Decimal_Number: int) -> str:
            """
            Convert a decimal number to its hexadecimal representation.

            :param Decimal_Number: The decimal number to convert.
            :return: The hexadecimal representation of the decimal number.
            """
            if Decimal_Number is None:
                raise Exception("No decimal number provided")
            cls.__check_input_type(Decimal_Number, (int, str))
            return hex(Decimal_Number)[2:].upper()

        @classmethod
        def to_bin(cls, Decimal_Number: int) -> int:
            """
            Convert a decimal number to its binary representation.

            :param Decimal_Number: The decimal number to convert.
            :return: The binary representation of the decimal number.
            """
            if Decimal_Number is None:
                raise Exception("No decimal number provided")
            cls.__check_input_type(Decimal_Number, (int, str))
            return int(bin(Decimal_Number)[2:])

    class Hexadecimal:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            """
            Check if the input value is of the expected type.

            :param value: The value to check.
            :param expected_type: The expected type of the value.
            :return: True if the value is of the expected type, otherwise raises an Exception.
            """
            if not isinstance(value, expected_type):
                raise Exception(
                    f"Expected {expected_type.__name__}, got {type(value).__name__}"
                )
            return True

        @classmethod
        def to_bin(cls, Hexadecimal_Number: str) -> int:
            """
            Convert a hexadecimal number to its binary representation.

            :param Hexadecimal_Number: The hexadecimal number to convert.
            :return: The binary representation of the hexadecimal number.
            """
            if Hexadecimal_Number is None:
                raise Exception("No hexadecimal number provided")
            cls.__check_input_type(Hexadecimal_Number, str)
            return int(bin(int(Hexadecimal_Number, 16))[2:])

        @classmethod
        def to_dec(cls, Hexadecimal_Number: str) -> int:
            """
            Convert a hexadecimal number to its decimal representation.

            :param Hexadecimal_Number: The hexadecimal number to convert.
            :return: The decimal representation of the hexadecimal number.
            """
            if Hexadecimal_Number is None:
                raise Exception("No hexadecimal number provided")
            cls.__check_input_type(Hexadecimal_Number, str)
            return int(Hexadecimal_Number, 16)

    class Roman:
        @staticmethod
        def to_dec(Roman: str) -> int:
            """
            Convert a Roman numeral to its decimal representation.

            :param Roman: The Roman numeral to convert.
            :return: The decimal representation of the Roman numeral.
            """
            roman_to_numerical = {
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
            """
            Convert a temperature from Celsius to Fahrenheit.

            :param celsius: The temperature in Celsius.
            :return: The temperature in Fahrenheit.
            """
            if celsius is None:
                raise Exception("No temperature provided")
            return (celsius * 9 / 5) + 32

        @staticmethod
        def to_kelvin(celsius: float | int) -> float:
            """
            Convert a temperature from Celsius to Kelvin.

            :param celsius: The temperature in Celsius.
            :return: The temperature in Kelvin.
            """
            if celsius is None:
                raise Exception("No temperature provided")
            return celsius + 273.15

    class Kelvin:
        @staticmethod
        def to_celsius(kelvin: float | int) -> float:
            """
            Convert a temperature from Kelvin to Celsius.

            :param kelvin: The temperature in Kelvin.
            :return: The temperature in Celsius.
            """
            if kelvin is None:
                raise Exception("No temperature provided")
            return kelvin - 273.15

        @staticmethod
        def to_fahrenheit(kelvin: float | int) -> float:
            """
            Convert a temperature from Kelvin to Fahrenheit.

            :param kelvin: The temperature in Kelvin.
            :return: The temperature in Fahrenheit.
            """
            if kelvin is None:
                raise Exception("No temperature provided")
            return (kelvin - 273.15) * 9 / 5 + 32

    class Fahrenheit:
        @staticmethod
        def to_kelvin(fahrenheit: float | int) -> float:
            """
            Convert a temperature from Fahrenheit to Kelvin.

            :param fahrenheit: The temperature in Fahrenheit.
            :return: The temperature in Kelvin.
            """
            if fahrenheit is None:
                raise Exception("No temperature provided")
            return (fahrenheit - 32) * 5 / 9 + 273.15

        @staticmethod
        def to_celsius(fahrenheit: float | int) -> float:
            """
            Convert a temperature from Fahrenheit to Celsius.

            :param fahrenheit: The temperature in Fahrenheit.
            :return: The temperature in Celsius.
            """
            if fahrenheit is None:
                raise Exception("No temperature provided")
            return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def memory(number: int, input_unit: str, output_unit: str) -> str:
        """
        Convert a memory size from one unit to another.

        :param number: The memory size to convert.
        :param input_unit: The unit of the input memory size.
        :param output_unit: The unit of the output memory size.
        :return: The converted memory size in the output unit.
        """
        memory_dict = {
            "bit": 1,
            "byte": 8,
            "kilobyte": 8000,
            "megabyte": 8 * (1000 ** 2),
            "gigabyte": 8 * (1000 ** 3),
            "terrabyte": 8 * (1000 ** 4),
            "petabyte": 8 * (1000 ** 5),
            "kibibyte": 8192,
            "mebibyte": 8 * (1024 ** 2),
            "gibibyte": 8 * (1024 ** 3),
            "tebibyte": 8 * (1024 ** 4),
            "pebibyte": 8 * (1024 ** 5),
            "kilobit": 1000,
            "megabit": 1000 ** 2,
            "gigabit": 1000 ** 3,
            "terrabit": 1000 ** 4,
            "petabit": 1000 ** 5,
            "kibibit": 1024,
            "mebibit": 1024 ** 2,
            "gibibit": 1024 ** 3,
            "tebibit": 1024 ** 4,
            "pebibit": 1024 ** 5,
            "KB": 8000,
            "MB": 8 * (1000 ** 2),
            "GB": 8 * (1000 ** 3),
            "TB": 8 * (1000 ** 4),
            "PB": 8 * (1000 ** 5),
            "KiB": 8192,
            "MiB": 8 * (1024 ** 2),
            "GiB": 8 * (1024 ** 3),
            "TiB": 8 * (1024 ** 4),
            "PiB": 8 * (1024 ** 5),
            "Kb": 1000,
            "Mb": 1000 ** 2,
            "Gb": 1000 ** 3,
            "Tb": 1000 ** 4,
            "Pb": 1000 ** 5,
            "Kib": 1024,
            "Mib": 1024 ** 2,
            "Gib": 1024 ** 3,
            "Tib": 1024 ** 4,
            "Pib": 1024 ** 5,
        }
        if not all([number, input_unit, output_unit]):
            raise Exception(f"Invalid input: {number} {input_unit} -> {output_unit}")
        if input_unit == output_unit:
            return f"{number} {output_unit}"
        input_unit = (
            input_unit.lower()
            if len(input_unit) > 3 and input_unit.lower() != "bit"
            else input_unit
        )
        output_unit = (
            output_unit.lower()
            if len(output_unit) > 3 and output_unit.lower() != "bit"
            else output_unit
        )
        if (
                not isinstance(number, int)
                or input_unit not in memory_dict
                or output_unit not in memory_dict
        ):
            raise Exception(f"Invalid input: {number} {input_unit} -> {output_unit}")
        final_number = (number * memory_dict[input_unit]) / memory_dict[output_unit]
        return f"{final_number:.15f}".rstrip("0").rstrip(".") + f" {output_unit}"
