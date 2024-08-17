class CreditCards:
    @staticmethod
    def luhn_algorithm(card_number):
        """
        Validates the card number using the Luhn algorithm.

        Parameters:
        - card_number (str): The credit card number to validate.

        Returns:
        - bool: True if the card number is valid, False otherwise.
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
    def validate(cls, card_type, card_number):
        """
        Validates the card number based on the specified card type.

        Parameters:
        - cls: The class itself.
        - card_type (str): The type of the card (e.g., 'Visa', 'Mastercard').
        - card_number (str): The credit card number to validate.

        Returns:
        - bool: True if the card number is valid, False otherwise.
        """
        if card_type.lower() == 'visa':
            # Visa cards start with '4' and have a length between 13 to 16
            return cls.luhn_algorithm(card_number) and card_number.startswith('4') and 13 <= len(card_number) <= 16
        elif card_type.lower() == 'mastercard':
            # Mastercard cards start with '51', '52', '53', '54', or '55'
            return cls.luhn_algorithm(card_number) and (card_number.startswith(('5', '2')) and 16 == len(card_number))
        else:
            return False

# Example usage
print(CreditCards.validate('Visa', '4532015112830366'))  # Should print: True
print(CreditCards.validate('Mastercard', '5555555555554444'))  # Should print: True
print(CreditCards.validate('AmericanExpress', '378282246310005'))  # Should print: True
print(CreditCards.validate('Discover', '6011111111111117'))  # Should print: True
