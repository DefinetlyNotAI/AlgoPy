class Convert:
    def __init__(self):
        """
        Initializes the mapping dictionary with Roman numeral values corresponding to integers.
        Initializes the roman_to_numerical dictionary with integer values corresponding to Roman numerals.
        """
        self.mapping = {
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
        }

    def to_roman(self, num):
        """
        Converts an integer number to its corresponding Roman numeral representation.

        Parameters:
            num (int): The integer number to be converted.

        Returns:
            str: The Roman numeral representation of the input number.

        Raises:
            KeyError: If the input number is not between 1 and 3999.
            Exception: If any other error occurs during the conversion process.
        """
        try:
            num = int(num)
            if num < 1 or num > 3999:
                exit("Error: Input must be between 1 and 3999 and an integer.")

            result = ""
            for numerical, roman in sorted(self.mapping.items(), reverse=True):
                while num >= numerical:
                    result += roman
                    num -= numerical
            return result
        except KeyError as ke:
            exit("Error: Invalid numeral: " + str(ke))
        except Exception as e:
            exit("Error: " + str(e))

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
            while i < len(roman):
                if i + 1 < len(roman) and roman[i: i + 2] in self.roman_to_numerical:
                    num += self.roman_to_numerical[roman[i: i + 2]]
                    i += 2
                else:
                    num += self.roman_to_numerical[roman[i]]
                    i += 1
            return num
        except KeyError as ke:
            exit("Error: Invalid Roman numeral: " + str(ke))
        except Exception as e:
            exit("Error: " + str(e))


# Example usage
convert = Convert()
print(convert.to_roman(5))
print(convert.to_number("IV"))
