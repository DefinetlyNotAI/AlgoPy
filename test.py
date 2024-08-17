class credit_card:
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
            ('62', '64', '65', '66', '67', '68', '69', '92', '93', '94', '95', '96', '97', '98', '99')) and 16 <= len(
            str(card_number)))

    @classmethod
    def dankort(cls, card_number: int) -> bool:
        """
        Validates Dankort card numbers.
        """
        return cls.__luhn_algorithm(card_number) and str(card_number).startswith('49') and 16 <= len(str(card_number))

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
        return cls.__luhn_algorithm(card_number) and str(card_number).startswith('35') and 16 <= len(str(card_number))

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




print(credit_card.v_pay(1234567890123456))
