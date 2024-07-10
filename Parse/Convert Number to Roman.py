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

    def to_number(self, roman):
        """Convert a Roman numeral to an integer."""
        if not isinstance(roman, str) or any(char not in self.mapping.keys() for char in roman):
            raise ValueError("Invalid Roman numeral")

        total = 0
        i = 0
        while i < len(roman):
            s1 = self.mapping.get(int(roman[i]), None)
            if i + 1 < len(roman):
                s2 = self.mapping.get(int(roman[i:i+2]), None)
            else:
                s2 = None

            if s1 != s2:
                if s2:
                    total += self.mapping[int(roman[i:i+2])] - self.mapping[int(roman[i])]
                else:
                    total += self.mapping[int(roman[i])]
            else:
                total += self.mapping[int(roman[i])]
            i += 1
        return total

# Example usage
convert_obj = Convert()
print(convert_obj.to_roman(2022))  # Output: MMXXII
print(convert_obj.to_number('MMXXII'))  # Output: 2022
