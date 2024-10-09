import re
from datetime import datetime


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
