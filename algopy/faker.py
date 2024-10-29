import os
import random
import string
import uuid
from datetime import datetime, timedelta


class Faker:
    class Misc:
        @classmethod
        def __init__(cls, extra_words: list = None):
            """
            Initialize the Misc class with optional extra words for random text generation.

            :param extra_words: List of additional words to include in the random text generation.
            """
            cls.words = [
                "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod",
                "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "Ut", "enim", "ad", "minim",
                "veniam", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea",
                "commodo", "consequat", "Duis", "aute", "irure", "dolor", "in", "reprehenderit", "in", "voluptate",
                "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla", "pariatur", "Excepteur", "sint",
                "occaecat", "cupidatat", "non", "proident", "sunt", "in", "culpa", "qui", "officia", "deserunt",
                "mollit", "anim", "id", "est", "laborum"
            ]
            if extra_words:
                cls.words.extend(extra_words)

        @staticmethod
        def generate_barcode(amount: int = 1, length: int = 12) -> list[str]:
            """
            Generate a list of random barcodes.

            :param amount: Number of barcodes to generate.
            :param length: Length of each barcode.
            :return: List of generated barcodes.
            """
            return [''.join(random.choices(string.digits, k=length)) for _ in range(amount)]

        @staticmethod
        def generate_uuid(amount: int = 1, version: int = 4, namespace: uuid.UUID = uuid.uuid1(),
                          name: str = os.name) -> list[str]:
            """
            Generate a list of UUIDs.

            :param amount: Number of UUIDs to generate.
            :param version: Version of the UUID to generate (1, 3, 4, or 5).
            :param namespace: Namespace for UUID versions 3 and 5.
            :param name: Name for UUID versions 3 and 5.
            :return: List of generated UUIDs.
            :raises ValueError: If an invalid UUID version is provided or required arguments are missing.
            """
            if version not in [1, 3, 4, 5]:
                raise ValueError("Invalid UUID version. Use 1, 3, 4, or 5.")
            if version in [3, 5] and (namespace is None or name is None):
                raise ValueError(f"UUID version {version} requires 'namespace' and 'name' arguments")
            uuid_func = {
                1: uuid.uuid1,
                3: lambda: uuid.uuid3(namespace, name),
                4: uuid.uuid4,
                5: lambda: uuid.uuid5(namespace, name)
            }.get(version)
            if uuid_func is None:
                raise ValueError(f"Invalid UUID version: {version}")
            return [str(uuid_func()) for _ in range(amount)]

        @classmethod
        def generate_random_text(cls, amount: int = 1, length: int = 100) -> list[str]:
            """
            Generate a list of random text strings.

            :param amount: Number of text strings to generate.
            :param length: Number of words in each text string.
            :return: List of generated random text strings.
            """
            if not hasattr(cls, 'words'):
                cls.__init__()
            return [' '.join(random.choices(cls.words, k=length)) for _ in range(amount)]

    class Financial:
        @staticmethod
        def __luhn_checksum(card_number: str) -> int:
            """
            Calculate the Luhn checksum for a card number.

            :param card_number: Card number to calculate the checksum for.
            :return: Luhn checksum.
            """
            def digits_of(n):
                return [int(d) for d in str(n)]

            digits = digits_of(card_number)
            odd_digits = digits[-1::-2]
            even_digits = digits[-2::-2]
            checksum = sum(odd_digits)
            for d in even_digits:
                checksum += sum(digits_of(d * 2))
            return checksum % 10

        @classmethod
        def __generate_compliant_number(cls, length: int) -> str:
            """
            Generate a Luhn-compliant card number of a specified length.

            :param length: Length of the card number to generate.
            :return: Generated Luhn-compliant card number.
            """
            number = ''.join(random.choices(string.digits, k=length - 1))
            checksum = cls.__luhn_checksum(number + '0')
            check_digit = (10 - checksum) % 10
            return number + str(check_digit)

        @classmethod
        def credit_card(cls, amount: int = 1) -> list[dict[str, str]]:
            """
            Generate a list of random credit card details.

            :param amount: Number of credit card details to generate.
            :return: List of generated credit card details.
            """
            credit_cards = []
            for _ in range(amount):
                credit_card_number = cls.__generate_compliant_number(16)
                cvv = ''.join(random.choices(string.digits, k=3))
                expiration_date = f"{random.randint(1, 12):02d}/{random.randint(22, 30):02d}"
                credit_cards.append({
                    "card_number": credit_card_number,
                    "cvv": cvv,
                    "expiration_date": expiration_date
                })
            return credit_cards

        @staticmethod
        def bank_account(amount: int = 1) -> list[dict[str, str]]:
            """
            Generate a list of random bank account details.

            :param amount: Number of bank account details to generate.
            :return: List of generated bank account details.
            """
            bank_accounts = []
            for _ in range(amount):
                bank_account_number = ''.join(random.choices(string.digits, k=12))
                bank_routing_number = ''.join(random.choices(string.digits, k=8))
                bank_routing_number += str(
                    (10 - sum(int(digit) for digit in bank_routing_number) % 10) % 10)  # Check digit
                bank_accounts.append({
                    "account_number": bank_account_number,
                    "routing_number": bank_routing_number
                })
            return bank_accounts

    class Personal:
        @classmethod
        def __init__(cls, extra_data: dict = None):
            """
            Initialize the Personal class with optional extra data for name, address, and email generation.

            :param extra_data: Dictionary containing additional data for first names, last names, cities, countries, street names, and domains.
            """
            cls.first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank"]
            cls.last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez"]
            cls.cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
            cls.countries = ["USA", "Canada", "Mexico", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Japan"]
            cls.street_names = ["Main", "Broadway", "Market", "Elm", "Maple", "Oak", "Pine", "Cedar", "Birch", "Walnut"]
            cls.domains = ["example.com", "test.com", "demo.com", "fake.com", "sample.com", "mock.com", "dummy.com", "faux.com", "simulated.com", "placeholder.com"]

            if extra_data:
                cls.first_names.extend(extra_data.get("extra_first_names", []))
                cls.last_names.extend(extra_data.get("extra_last_names", []))
                cls.cities.extend(extra_data.get("extra_cities", []))
                cls.countries.extend(extra_data.get("extra_countries", []))
                cls.street_names.extend(extra_data.get("extra_street_names", []))
                cls.domains.extend(extra_data.get("extra_domains", []))

        @classmethod
        def name(cls, format: str = None, amount: int = 1) -> list[str]:
            """
            Generate a list of random names.

            Format string can contain {first_name} and {last_name} placeholders.
            Example format: "{first_name} {last_name}".

            :param format: Optional format string for the names, using {first_name} and {last_name} as placeholders.
            :param amount: Number of names to generate.
            :return: List of generated names.
            """
            return [format.replace("{first_name}", random.choice(cls.first_names)).replace("{last_name}", random.choice(
                cls.last_names)) if format else f"{random.choice(cls.first_names)} {random.choice(cls.last_names)}" for
                    _
                    in range(amount)]

        @classmethod
        def address(cls, format: str = None, amount: int = 1) -> list[str]:
            """
            Generate a list of random addresses.

            Format string can contain {street_address}, {city}, {country}, and {postal_code} placeholders.
            Example format: "{street_address}, {city}, {country} {postal_code}".

            :param format: Optional format string for the addresses, using {street_address}, {city}, {country}, and {postal_code} as placeholders.
            :param amount: Number of addresses to generate.
            :return: List of generated addresses.
            """
            if not hasattr(cls, 'street_names'):
                cls.__init__()
            addresses = []
            for _ in range(amount):
                address = cls.__helper_address()
                if format:
                    formatted_address = format
                    for key, value in address.items():
                        formatted_address = formatted_address.replace(f"{{{key}}}", value)
                    addresses.append(formatted_address)
                else:
                    addresses.append(address)
            return addresses

        @classmethod
        def __helper_address(cls):
            address = {
                "street_address": f"{random.randint(1, 9999)} {random.choice(cls.street_names)} St",
                "city": random.choice(cls.cities),
                "country": random.choice(cls.countries),
                "postal_code": f"{random.randint(10000, 99999)}"
            }
            return address

        @staticmethod
        def phone_number(format: str = None, amount: int = 1) -> list[str]:
            """
            Generate a list of random phone numbers.

            Format string can contain {phone_number} as a placeholder.
            Example format: "John's phone number is {phone_number}".

            :param format: Optional format string for the phone numbers, using {phone_number} as a placeholder.
            :param amount: Number of phone numbers to generate.
            :return: List of generated phone numbers.
            """
            return [format.replace("{phone_number}",
                                   f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}") if format else f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
                    for _ in range(amount)]

        @classmethod
        def email(cls, format: str = None, amount: int = 1) -> list[str]:
            """
            Generate a list of random email addresses.

            Format string can contain {email} as a placeholder.
            Example format: "John's email is {email}"

            :param format: Optional format string for the email addresses, using {email} as a placeholder.
            :param amount: Number of email addresses to generate.
            :return: List of generated email addresses.
            """
            if not hasattr(cls, 'first_names') or not hasattr(cls, 'last_names') or not hasattr(cls, 'domains'):
                cls.__init__()
            return [format.replace("{email}",
                                   f"{random.choice(cls.first_names).lower()}.{random.choice(cls.last_names).lower()}@{random.choice(cls.domains)}") if format else f"{random.choice(cls.first_names).lower()}.{random.choice(cls.last_names).lower()}@{random.choice(cls.domains)}"
                    for _ in range(amount)]

        @staticmethod
        def date(format: str = None, amount: int = 1) -> list[str]:
            """
            Generate a list of random dates.

            Format string should be in the strftime format.
            Example format: "%Y-%m-%d".

            :param format: Optional format string for the dates.
            :param amount: Number of dates to generate.
            :return: List of generated dates.
            """
            dates = []
            for _ in range(amount):
                start_date = datetime.now()
                end_date = start_date + timedelta(days=365)
                date = start_date + (end_date - start_date) * random.random()
                dates.append(date.strftime(format) if format else date.strftime("%Y-%m-%d"))
            return dates

    class Business:
        @classmethod
        def __init__(cls, extra_company_names: list = None, extra_job_titles: list = None):
            """
            Initialize the Business class with optional extra data for company names and job titles.

            :param extra_company_names: List of additional company names.
            :param extra_job_titles: List of additional job titles.
            """
            cls.company_names = ["TechCorp", "InnovateX", "AlphaSolutions", "BetaWorks", "GammaEnterprises"]
            cls.job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "Designer", "QA Engineer"]
            if extra_company_names:
                cls.company_names.extend(extra_company_names)
            if extra_job_titles:
                cls.job_titles.extend(extra_job_titles)

        @classmethod
        def company_name(cls, amount: int = 1) -> list[str]:
            """
            Generate a list of random company names.

            :param amount: Number of company names to generate.
            :return: List of generated company names.
            """
            if not hasattr(cls, 'company_names'):
                cls.__init__()
            return [str(random.choice(cls.company_names)) for _ in range(amount)]

        @classmethod
        def job_title(cls, amount: int = 1) -> list[str]:
            """
            Generate a list of random job titles.

            :param amount: Number of job titles to generate.
            :return: List of generated job titles.
            """
            return [str(random.choice(cls.job_titles)) for _ in range(amount)]

        @staticmethod
        def employee_id(amount: int = 1, characters_to_use: str = (string.ascii_uppercase + string.digits)) -> list[str]:
            """
            Generate a list of random employee IDs.

            :param amount: Number of employee IDs to generate.
            :param characters_to_use: Characters to use for generating the employee IDs.
            :return: List of generated employee IDs.
            """
            return [''.join(random.choices(characters_to_use, k=8)) for _ in range(amount)]

    class Product:
        @classmethod
        def __init__(cls, extra_product_names: list = None, extra_product_categories: list = None):
            """
            Initialize the Product class with optional extra data for product names and categories.

            :param extra_product_names: List of additional product names.
            :param extra_product_categories: List of additional product categories.
            """
            cls.product_names = ["Widget", "Gadget", "Thingamajig", "Doodad", "Gizmo"]
            cls.product_categories = ["Electronics", "Home", "Toys", "Clothing", "Sports"]
            if extra_product_names:
                cls.product_names.extend(extra_product_names)
            if extra_product_categories:
                cls.product_categories.extend(extra_product_categories)

        @classmethod
        def generate_product_name(cls, amount: int = 1) -> list[str]:
            """
            Generate a list of random product names.

            :param amount: Number of product names to generate.
            :return: List of generated product names.
            """
            if not hasattr(cls, 'product_names'):
                cls.__init__()
            return [str(random.choice(cls.product_names)) for _ in range(amount)]

        @classmethod
        def generate_product_category(cls, amount: int = 1) -> list[str]:
            """
            Generate a list of random product categories.

            :param amount: Number of product categories to generate.
            :return: List of generated product categories.
            """
            if not hasattr(cls, 'product_categories'):
                cls.__init__()
            return [str(random.choice(cls.product_categories)) for _ in range(amount)]

        @staticmethod
        def generate_price(amount: int = 1, min_price: float = 1.0, max_price: float = 100.0) -> list[float]:
            """
            Generate a list of random prices within a specified range.

            :param amount: Number of prices to generate.
            :param min_price: Minimum price value.
            :param max_price: Maximum price value.
            :return: List of generated prices.
            """
            return [round(random.uniform(min_price, max_price), 2) for _ in range(amount)]

    class Internet:
        """
        A class to generate various types of internet-related fake data.
        """

        @classmethod
        def __init__(cls, extra_domains: list = None):
            """
            Initialize the Internet class with optional extra domains.

            :param extra_domains: List of additional domains to include.
            """
            cls.domains = ["example.com", "test.com", "sample.org", "demo.net", "fake.com",
                           "mock.org", "example.net", "test.org", "sample.com", "demo.net"]
            if extra_domains:
                cls.domains.extend(extra_domains)

        @staticmethod
        def generate_username(amount: int = 1, size: int = 8,
                              charset: str = string.ascii_letters) -> list[str]:
            """
            Generate a list of random usernames.

            :param amount: Number of usernames to generate.
            :param size: Length of each username.
            :param charset: Characters to use for generating the usernames.
            :return: List of generated usernames.
            """
            return [''.join(random.choices(charset, k=size)) for _ in range(amount)]

        @staticmethod
        def generate_password(amount: int = 1, size: int = 12,
                              charset: str = (string.ascii_letters + string.digits + string.punctuation)) -> list[str]:
            """
            Generate a list of random passwords.

            :param amount: Number of passwords to generate.
            :param size: Length of each password.
            :param charset: Characters to use for generating the passwords.
            :return: List of generated passwords.
            """
            return [''.join(random.choices(charset, k=size)) for _ in range(amount)]

        @staticmethod
        def generate_ip_address(amount: int = 1, version=4) -> list[str]:
            """
            Generate a list of random IP addresses.

            :param amount: Number of IP addresses to generate.
            :param version: IP version (4 or 6).
            :return: List of generated IP addresses.
            """
            ip_addresses = []
            for _ in range(amount):
                if version == 4:
                    ip_addresses.append('.'.join(str(random.randint(0, 255)) for _ in range(4)))
                elif version == 6:
                    ip_addresses.append(':'.join(''.join(random.choices('0123456789abcdef', k=4)) for _ in range(8)))
                else:
                    raise ValueError("Invalid IP version. Use 4 or 6.")
            return ip_addresses

        @classmethod
        def generate_url(cls, amount: int = 1, format: str = None) -> list[str]:
            """
            Generate a list of random URLs.

            Format string can contain {domain} and {path} placeholders.
            Example format: "https://{domain}/{path}".

            :param amount: Number of URLs to generate.
            :param format: Optional format string for the URLs, using {domain} and {path} as placeholders.
            :return: List of generated URLs.
            """
            if not hasattr(cls, 'domains'):
                cls.__init__()
            urls = []
            for _ in range(amount):
                domain = random.choice(cls.domains)
                path = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                url = f"https://{domain}/{path}"
                if format:
                    url = format.replace("{domain}", domain).replace("{path}", path)
                urls.append(url)
            return urls
