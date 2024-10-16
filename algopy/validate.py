import os
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
    def _url_by_parsing(url: str) -> dict | bool:
        if not url:
            return False
        # Read TLDs from file
        record_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'registered.tld.record')
        with open(record_path, 'r') as file:
            tlds = {line.strip().lower() for line in file.readlines()[1:]}

        # Split the URL into components
        if '://' not in url:
            return False

        protocol, rest = url.split('://', 1)
        if '/' in rest:
            hostname, filename = rest.split('/', 1)
            filename = '/' + filename
        else:
            hostname = rest
            filename = ''

        # Extract TLD from hostname
        tld = hostname.split('.')[-1].lower()
        is_registered_tld = tld in tlds

        if not hostname.startswith('www.'):
            hostname = 'www.' + hostname

        return {
            'protocol': protocol,
            'hostname': hostname,
            'filename': filename,
            'TLD': is_registered_tld
        }

    @classmethod
    def this_url(cls, url: str, text_error: bool = False,
                 enforce_https: bool = False) -> bool:
        parsed_url = cls._url_by_parsing(url)
        if not parsed_url:
            error_message = 'Invalid URL: Reason - URL is empty or does not contain a protocol'
            return error_message if text_error else False

        # Validate protocol
        if parsed_url['protocol'] not in ['http', 'https']:
            error_message = 'Invalid URL: Reason - Protocol is not HTTP or HTTPS'
            return error_message if text_error else False
        elif enforce_https and parsed_url['protocol'] != 'https':
            error_message = 'Invalid URL: Reason - HTTPS protocol is enforced'
            return error_message if text_error else False

        # Validate hostname
        hostname = parsed_url['hostname']
        if len(hostname) > 253:
            error_message = 'Invalid URL: Reason - Hostname is too long'
            return error_message if text_error else False
        if hostname.count('.') < 1:
            error_message = 'Invalid URL: Reason - Hostname does not contain a domain'
            return error_message if text_error else False
        hostname_labels = hostname.split('.')
        for label in hostname_labels:
            if not all(c.isalnum() or c == '-' for c in label):
                error_message = 'Invalid URL: Reason - Invalid character in hostname'
                return error_message if text_error else False
            if label.startswith('-') or label.endswith('-'):
                error_message = 'Invalid URL: Reason - Label starts or ends with a hyphen'
                return error_message if text_error else False
            if label.isdigit():
                error_message = 'Invalid URL: Reason - Label is a number'
                return error_message if text_error else False

        # Validate filename
        filename = parsed_url['filename']
        if len(filename) > 256:
            error_message = 'Invalid URL: Reason - Filename is too long'
            return error_message if text_error else False
        if ' ' in filename:
            error_message = 'Invalid URL: Reason - Filename contains spaces'
            return error_message if text_error else False

        if not parsed_url['TLD']:
            error_message = 'Invalid URL: Reason - TLD is not registered'
            return error_message if text_error else False
        return True

    @staticmethod
    def this_phone_number(phone_number: int | str) -> bool:
        """
        Validates a phone number against a set of predefined formats.
        Allow only digits, parentheses, hyphens, periods, and spaces.

        Allowed formats:
            "(###)###-####",
            "(###)-###-####",
            "(###)###-###-####",
            "(###)-###-###-####",
            "(###)###-####-###",
            "(###)-###-####-###",
            "###-###-####",
            "###-####-###",
            "##########",
        Where # is a digit and - is a separator of any type allowed.

        Args:
            phone_number (int | str): The phone number to be validated.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        phone_number = str(phone_number)
        allowed_chars = set("0123456789()+-. ")
        if not all(char in allowed_chars for char in phone_number):
            return False

        phone_number_list = list(phone_number)
        for i, char in enumerate(phone_number_list):
            if char.isdigit():
                phone_number_list[i] = '#'
            elif char == '+' or char == '.' or char == ' ':
                phone_number_list[i] = '-'

        formatted_phone_number = ''.join(phone_number_list)
        valid_formats = [
            "(###)###-####",
            "(###)-###-####",
            "(###)###-###-####",
            "(###)-###-###-####",
            "(###)###-####-###",
            "(###)-###-####-###",
            "###-###-####",
            "###-####-###",
            "##########",
        ]

        return formatted_phone_number in valid_formats

    @staticmethod
    def this_date(date: str, datetime_format: str = "%Y-%m-%d") -> bool:
        r"""
        Validates a date string.

        The allowed date formats in the selected code are:

        - `DD-MM-YYYY`
        - `YYYY-MM-DD`

        These formats are normalized to either `YYYY-MM-DD` or `DD-MM-YYYY` before validation.
        Where `-` is a separator, and can be from the following set [-, /, \, ].

        Args:
            date (str): The date string to be validated.
            datetime_format (str): The format of the date string. Defaults to `"%Y-%m-%d"`. Always falls-back to `"%d-%m-%Y"`.

        Returns:
            bool: True if the date string is valid, False otherwise.
        """
        if not date:
            return False
        date = date.replace("/", "-")
        date = date.replace("\\", "-")
        date = date.replace(" ", "-")
        try:
            datetime.strptime(date, datetime_format)
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
                    and str(card_number).startswith(("51", "52", "53", "54", "55", "56", "57", "58", "59"))
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
                    and str(card_number).startswith(("40", "41", "42", "43", "44", "45", "46", "47", "48", "49"))
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
