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
        pattern = re.compile(
            r"^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        )
        return bool(pattern.search(email_address))

    @staticmethod
    def this_url(url_string: str, use_https: bool = True) -> bool:
        """
        Validates a URL string.

        Args:
            url_string (str): The URL string to be validated.
            use_https (bool): Whether to enforce HTTPS. Defaults to True.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """
        if not url_string or " " in url_string:
            return False
        https = bool(
            (
                re.compile(r"^(https://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w.-]*)*/?$")
            ).search(url_string)
        )
        http = bool(
            (
                re.compile(r"^(http://)?([\da-z.-]+)\.([a-z.]{2,6})([/\w.-]*)*/?$")
            ).search(url_string)
        )
        if use_https:
            return https
        return https or http

    @staticmethod
    def this_phone_number(phone_number: int | str) -> bool:
        """
        Validates a phone number.

        Args:
            phone_number (int | str): The phone number to be validated.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        pattern = re.compile(r"^(\(\d{3}\)[\s-]?)?\d{3}[\s-]?\d{4}[\s-]?\d{3}$")
        return bool(pattern.match(str(phone_number)))

    @staticmethod
    def this_date(date: str) -> bool:
        """
        Validates a date string.

        Args:
            date (str): The date string to be validated.

        Returns:
            bool: True if the date string is valid, False otherwise.
        """
        date = date.replace("/", "-")
        date = date.replace("\\", "-")
        date = date.replace(" ", "-")
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
        def __luhn_algorithm(card_number: str) -> bool:
            """
            Validates a card number using the Luhn algorithm.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            if len(card_number) < 13 or len(card_number) > 19:
                return False
            num_list = [int(digit) for digit in card_number]
            num_list.reverse()
            total = 0
            for i, num in enumerate(num_list):
                if i % 2 == 1:
                    doubled = num * 2
                    if doubled > 9:
                        doubled -= 9
                    total += doubled
                else:
                    total += num
            return total % 10 == 0

        @classmethod
        def american_express(cls, card_number: str) -> bool:
            """
            Validates American Express card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(("34", "37"))
                    and 15 <= len(str(card_number)) <= 16
            )

        @classmethod
        def china_unionpay(cls, card_number: str) -> bool:
            """
            Validates China UnionPay card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
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
        def dankort(cls, card_number: str) -> bool:
            """
            Validates Dankort card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith("49")
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def diners_club(cls, card_number: str) -> bool:
            """
            Validates Diners Club International card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            return cls.__luhn_algorithm(card_number) and (
                    str(card_number).startswith(("36", "38"))
                    and 14 <= len(str(card_number)) <= 19
            )

        @classmethod
        def discover(cls, card_number: str) -> bool:
            """
            Validates Discover card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
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
        def jcb(cls, card_number: str) -> bool:
            """
            Validates JCB card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith("35")
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def maestro(cls, card_number: str) -> bool:
            """
            Validates Maestro card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
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
        def mastercard(cls, card_number: str) -> bool:
            """
            Validates Mastercard card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith(
                ("51", "52", "53", "54", "55", "56", "57", "58", "59")
            )
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def visa(cls, card_number: str) -> bool:
            """
            Validates Visa card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith("4")
                    and 13 <= len(str(card_number)) <= 16
            )

        @classmethod
        def visa_electron(cls, card_number: str) -> bool:
            """
            Validates Visa Electron card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(card_number).startswith(
                ("40", "41", "42", "43", "44", "45", "46", "47", "48", "49")
            )
                    and 16 <= len(str(card_number))
            )

        @classmethod
        def v_pay(cls, card_number: str) -> bool:
            """
            Validates V Pay card numbers.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            return (
                    cls.__luhn_algorithm(card_number)
                    and str(str(card_number)).startswith("28")
                    and 16 <= len(str(str(card_number)))
            )

        @classmethod
        def any(cls, card_number: str) -> bool:
            """
            Validates any card number just by passing it to the Luhn algorithm.

            Args:
                card_number (str): The card number to be validated.

            Returns:
                bool: True if the card number is valid, False otherwise.
            """
            return cls.__luhn_algorithm(card_number)
