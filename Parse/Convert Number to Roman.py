class Convert:
    def __init__(self):
        self.mapping = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
            1: 'I'
        }

    def to_roman(self, num):
        """Convert an integer to a Roman numeral."""
        if not isinstance(num, int) or num < 1 or num > 3999:
            raise ValueError("Input must be between 1 and 3999")

        result = ''
        for arabic, roman in sorted(self.mapping.items(), reverse=True):
            while num >= arabic:
                result += roman
                num -= arabic
        return result

    @staticmethod
    def to_number(roman):
        roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                     'XC': 90,
                     'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i + 2] in roman_dic:
                num += roman_dic[roman[i:i + 2]]
                i += 2
            else:
                num += roman_dic[roman[i]]
                i += 1
        return num


# Example usage
convert_obj = Convert()
print(convert_obj.to_roman(4))  # Output: IV
print(convert_obj.to_number('IV'))  # Expected output: 4
print(convert_obj.to_roman(40))  # Output: XL
print(convert_obj.to_number('XL'))  # Expected output: 40
print(convert_obj.to_roman(90))  # Output: XC
print(convert_obj.to_number('XC'))  # Expected output: 90
print(convert_obj.to_roman(400))  # Output: CD
print(convert_obj.to_number('CD'))  # Expected output: 400
print(convert_obj.to_roman(900))  # Output: CM
print(convert_obj.to_number('CM'))  # Expected output: 900
