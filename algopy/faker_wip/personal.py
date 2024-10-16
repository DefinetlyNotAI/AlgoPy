import random
from datetime import datetime, timedelta


class PersonalFaker:
    @classmethod
    def __init__(cls):
        cls.first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank"]
        cls.last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
                          "Martinez"]
        cls.cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
                      "San Diego", "Dallas", "San Jose"]
        cls.countries = ["USA", "Canada", "Mexico", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Japan"]
        cls.street_names = ["Main", "Broadway", "Market", "Elm", "Maple", "Oak", "Pine", "Cedar", "Birch", "Walnut"]
        cls.domains = ["example.com", "test.com", "demo.com", "fake.com", "sample.com", "mock.com", "dummy.com",
                       "faux.com", "simulated.com", "placeholder.com"]

    @classmethod
    def name(cls, format: str = None, amount: int = 1) -> list:
        return [format.replace("{first_name}", random.choice(cls.first_names)).replace("{last_name}", random.choice(
            cls.last_names)) if format else f"{random.choice(cls.first_names)} {random.choice(cls.last_names)}" for _
                in range(amount)]

    @classmethod
    def address(cls, format: str = None, amount: int = 1) -> list:
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
    def phone_number(format: str = None, amount: int = 1) -> list:
        return [format.replace("{phone_number}",
                               f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}") if format else f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
                for _ in range(amount)]

    @classmethod
    def email(cls, format: str = None, amount: int = 1) -> list:
        return [format.replace("{email}",
                               f"{random.choice(cls.first_names).lower()}.{random.choice(cls.last_names).lower()}@{random.choice(cls.domains)}") if format else f"{random.choice(cls.first_names).lower()}.{random.choice(cls.last_names).lower()}@{random.choice(cls.domains)}"
                for _ in range(amount)]

    @staticmethod
    def date(format: str = None, amount: int = 1) -> list:
        dates = []
        for _ in range(amount):
            start_date = datetime.now()
            end_date = start_date + timedelta(days=365)
            date = start_date + (end_date - start_date) * random.random()
            dates.append(date.strftime(format) if format else date.strftime("%Y-%m-%d"))
        return dates
