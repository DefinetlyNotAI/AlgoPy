import os
import random
import string
import uuid
from datetime import datetime, timedelta


class Faker:
    class Misc:
        @classmethod
        def __init__(cls, extra_words: list = None):
            cls.words = [
                "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod",
                "tempor",
                "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "Ut", "enim", "ad", "minim", "veniam",
                "quis",
                "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea", "commodo",
                "consequat",
                "Duis", "aute", "irure", "dolor", "in", "reprehenderit", "in", "voluptate", "velit", "esse", "cillum",
                "dolore",
                "eu", "fugiat", "nulla", "pariatur", "Excepteur", "sint", "occaecat", "cupidatat", "non", "proident",
                "sunt",
                "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum"
            ]
            if extra_words:
                cls.words.extend(extra_words)

        @staticmethod
        def generate_barcode(amount: int = 1, length: int = 12) -> list[str]:
            return [''.join(random.choices(string.digits, k=length)) for _ in range(amount)]

        @staticmethod
        def generate_uuid(amount: int = 1, version: int = 4, namespace: uuid.UUID = uuid.uuid1(),
                          name: str = os.name) -> list[str]:
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
            if not hasattr(cls, 'words'):
                cls.__init__()
            return [' '.join(random.choices(cls.words, k=length)) for _ in range(amount)]

    class Financial:
        @staticmethod
        def __luhn_checksum(card_number: str) -> int:
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
        def __generate_luhn_compliant_number(cls, length: int) -> str:
            number = ''.join(random.choices(string.digits, k=length - 1))
            checksum = cls.__luhn_checksum(number + '0')
            check_digit = (10 - checksum) % 10
            return number + str(check_digit)

        @classmethod
        def credit_card(cls, amount: int = 1) -> list[dict[str, str]]:
            credit_cards = []
            for _ in range(amount):
                credit_card_number = cls.__generate_luhn_compliant_number(16)
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
        def __init__(cls, extra_first_names: list = None, extra_last_names: list = None, extra_cities: list = None,
                     extra_countries: list = None, extra_street_names: list = None, extra_domains: list = None):
            cls.first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank"]
            cls.last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
                              "Martinez"]
            cls.cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
                          "San Diego", "Dallas", "San Jose"]
            cls.countries = ["USA", "Canada", "Mexico", "UK", "Germany", "France", "Italy", "Spain", "Australia",
                             "Japan"]
            cls.street_names = ["Main", "Broadway", "Market", "Elm", "Maple", "Oak", "Pine", "Cedar", "Birch", "Walnut"]
            cls.domains = ["example.com", "test.com", "demo.com", "fake.com", "sample.com", "mock.com", "dummy.com",
                           "faux.com", "simulated.com", "placeholder.com"]
            if extra_first_names:
                cls.first_names.extend(extra_first_names)
            if extra_last_names:
                cls.last_names.extend(extra_last_names)
            if extra_cities:
                cls.cities.extend(extra_cities)
            if extra_countries:
                cls.countries.extend(extra_countries)
            if extra_street_names:
                cls.street_names.extend(extra_street_names)
            if extra_domains:
                cls.domains.extend(extra_domains)

        @classmethod
        def name(cls, format: str = None, amount: int = 1) -> list[str]:
            return [format.replace("{first_name}", random.choice(cls.first_names)).replace("{last_name}", random.choice(
                cls.last_names)) if format else f"{random.choice(cls.first_names)} {random.choice(cls.last_names)}" for
                    _
                    in range(amount)]

        @classmethod
        def address(cls, format: str = None, amount: int = 1) -> list[str]:
            if not hasattr(cls, 'street_names'):
                cls.__init__()
            addresses = []
            for _ in range(amount):
                address = {
                    "street_address": f"{random.randint(1, 9999)} {random.choice(cls.street_names)} St",
                    "city": random.choice(cls.cities),
                    "country": random.choice(cls.countries),
                    "postal_code": f"{random.randint(10000, 99999)}"
                }
                if format:
                    formatted_address = format
                    for key, value in address.items():
                        formatted_address = formatted_address.replace(f"{{{key}}}", value)
                    addresses.append(formatted_address)
                else:
                    addresses.append(address)
            return addresses

        @staticmethod
        def phone_number(format: str = None, amount: int = 1) -> list[str]:
            return [format.replace("{phone_number}",
                                   f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}") if format else f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
                    for _ in range(amount)]

        @classmethod
        def email(cls, format: str = None, amount: int = 1) -> list[str]:
            if not hasattr(cls, 'first_names') or not hasattr(cls, 'last_names') or not hasattr(cls, 'domains'):
                cls.__init__()
            return [format.replace("{email}",
                                   f"{random.choice(cls.first_names).lower()}.{random.choice(cls.last_names).lower()}@{random.choice(cls.domains)}") if format else f"{random.choice(cls.first_names).lower()}.{random.choice(cls.last_names).lower()}@{random.choice(cls.domains)}"
                    for _ in range(amount)]

        @staticmethod
        def date(format: str = None, amount: int = 1) -> list[str]:
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
            cls.company_names = ["TechCorp", "InnovateX", "AlphaSolutions", "BetaWorks", "GammaEnterprises"]
            cls.job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "Designer", "QA Engineer"]
            if extra_company_names:
                cls.company_names.extend(extra_company_names)
            if extra_job_titles:
                cls.job_titles.extend(extra_job_titles)

        @classmethod
        def company_name(cls, amount: int = 1) -> list[str]:
            if not hasattr(cls, 'company_names'):
                cls.__init__()
            return [str(random.choice(cls.company_names)) for _ in range(amount)]

        @classmethod
        def job_title(cls, amount: int = 1) -> list[str]:
            return [str(random.choice(cls.job_titles)) for _ in range(amount)]

        @staticmethod
        def employee_id(amount: int = 1, characters_to_use: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") -> list[str]:
            return [''.join(random.choices(characters_to_use, k=8)) for _ in range(amount)]

    class Product:
        @classmethod
        def __init__(cls, extra_product_names: list = None, extra_product_categories: list = None):
            cls.product_names = ["Widget", "Gadget", "Thingamajig", "Doodad", "Gizmo"]
            cls.product_categories = ["Electronics", "Home", "Toys", "Clothing", "Sports"]
            if extra_product_names:
                cls.product_names.extend(extra_product_names)
            if extra_product_categories:
                cls.product_categories.extend(extra_product_categories)

        @classmethod
        def generate_product_name(cls, amount: int = 1) -> list[str]:
            if not hasattr(cls, 'product_names'):
                cls.__init__()
            return [str(random.choice(cls.product_names)) for _ in range(amount)]

        @classmethod
        def generate_product_category(cls, amount: int = 1) -> list[str]:
            if not hasattr(cls, 'product_categories'):
                cls.__init__()
            return [str(random.choice(cls.product_categories)) for _ in range(amount)]

        @staticmethod
        def generate_price(amount: int = 1, min_price: float = 1.0, max_price: float = 100.0) -> list[float]:
            return [round(random.uniform(min_price, max_price), 2) for _ in range(amount)]

    class Internet:
        @classmethod
        def __init__(cls, extra_domains: list = None):
            cls.domains = ["example.com", "test.com", "sample.org", "demo.net"]
            if extra_domains:
                cls.domains.extend(extra_domains)

        @staticmethod
        def generate_username(amount: int = 1, size: int = 8,
                              charset: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-<>?!@#$%^&*()[]{};=-_") -> \
                list[str]:
            return [''.join(random.choices(charset, k=size)) for _ in range(amount)]

        @staticmethod
        def generate_password(amount: int = 1, size: int = 12,
                              charset: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-<>?!@#$%^&*()[]{};=-_") -> \
                list[str]:
            return [''.join(random.choices(charset, k=size)) for _ in range(amount)]

        @staticmethod
        def generate_ip_address(amount: int = 1, version=4) -> list[str]:
            ip_addresses = []
            for _ in range(amount):
                if version == 4:
                    ip_addresses.append('.'.join(str(random.randint(0, 255)) for _ in range(4)))
                elif version == 6:
                    ip_addresses.append(
                        ':'.join(''.join(random.choices('0123456789abcdef', k=4)) for _ in range(8)))
            return ip_addresses

        @classmethod
        def generate_url(cls, amount: int = 1, format: str = None) -> list[str]:
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
