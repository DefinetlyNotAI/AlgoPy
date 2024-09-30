class Convert:
    class Binary:
        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            if not isinstance(value, expected_type):
                raise Exception(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return True

        def to_hex(self, Binary_Number: int) -> str:
            if Binary_Number is None:
                raise Exception("No binary number provided")
            self.__check_input_type(str(Binary_Number), str)
            return hex(int(str(Binary_Number), 2))[2:].upper()

        def to_dec(self, Binary_Number: int) -> int:
            if Binary_Number is None:
                raise Exception("No binary number provided")
            self.__check_input_type(str(Binary_Number), str)
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

        def to_hex(self, Decimal_Number: int) -> str:
            if Decimal_Number is None:
                raise Exception("No decimal number provided")
            self.__check_input_type(Decimal_Number, (int, str))
            return hex(Decimal_Number)[2:].upper()

        def to_bin(self, Decimal_Number: int) -> int:
            if Decimal_Number is None:
                raise Exception("No decimal number provided")
            self.__check_input_type(Decimal_Number, (int, str))
            return int(bin(Decimal_Number)[2:])

    class Hexadecimal:

        @staticmethod
        def __check_input_type(value, expected_type) -> bool:
            if not isinstance(value, expected_type):
                raise Exception(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return True

        def to_bin(self, Hexadecimal_Number: str) -> int:
            if Hexadecimal_Number is None:
                raise Exception("No hexadecimal number provided")
            self.__check_input_type(Hexadecimal_Number, str)
            return int(bin(int(Hexadecimal_Number, 16))[2:])

        def to_dec(self, Hexadecimal_Number: str) -> int:
            if Hexadecimal_Number is None:
                raise Exception("No hexadecimal number provided")
            self.__check_input_type(Hexadecimal_Number, str)
            return int(Hexadecimal_Number, 16)

    class Roman:
        @staticmethod
        def to_dec(Roman: str) -> int:
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
                "/X/": 10000,
                "M/X/": 9000,
                "/VIII/": 8000,
                "/V/": 5000,
                "M/V/": 4000,
            }
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
            "Bit": 1, "Byte": 8, "KB": 8000, "MB": 8 * (1000 ** 2), "GB": 8 * (1000 ** 3),
            "TB": 8 * (1000 ** 4), "PB": 8 * (1000 ** 5), "KiB": 8192, "MiB": 8 * (1024 ** 2),
            "GiB": 8 * (1024 ** 3), "TiB": 8 * (1024 ** 4), "PiB": 8 * (1024 ** 5),
            "Kb": 1000, "Mb": 1000 ** 2, "Gb": 1000 ** 3, "Tb": 1000 ** 4, "Pb": 1000 ** 5,
            "Kib": 1024, "Mib": 1024 ** 2, "Gib": 1024 ** 3, "Tib": 1024 ** 4, "Pib": 1024 ** 5
        }
        if number is None or input_unit is None or output_unit is None:
            raise Exception("Invalid input.")
        if not isinstance(number, int) or input_unit not in memory_dict or output_unit not in memory_dict:
            raise Exception("Invalid input.")
        input_factor = memory_dict[input_unit]
        output_factor = memory_dict[output_unit]
        final_number = (number * input_factor) / output_factor
        return f"{final_number:.2f} {output_unit}"
