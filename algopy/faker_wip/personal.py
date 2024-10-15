import random
from datetime import datetime, timedelta


class PersonalFaker:
    def __init__(self):
        self.first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank"]
        self.last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
                           "Martinez"]
        self.cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
                       "San Diego", "Dallas", "San Jose"]
        self.countries = ["USA", "Canada", "Mexico", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Japan"]
        self.street_names = ["Main", "Broadway", "Market", "Elm", "Maple", "Oak", "Pine", "Cedar", "Birch", "Walnut"]
        self.domains = ["example.com", "test.com", "demo.com", "fake.com", "sample.com", "mock.com", "dummy.com",
                        "faux.com", "simulated.com", "placeholder.com"]

    def name(self, format: str = None, amount: int = 1) -> list:
        return [format.replace("{first_name}", random.choice(self.first_names)).replace("{last_name}", random.choice(
            self.last_names)) if format else f"{random.choice(self.first_names)} {random.choice(self.last_names)}" for _
                in range(amount)]

    def address(self, format: str = None, amount: int = 1) -> list:
        addresses = []
        for _ in range(amount):
            address = {
                "street_address": f"{random.randint(1, 9999)} {random.choice(self.street_names)} St",
                "city": random.choice(self.cities),
                "country": random.choice(self.countries),
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

    def email(self, format: str = None, amount: int = 1) -> list:
        return [format.replace("{email}",
                               f"{random.choice(self.first_names).lower()}.{random.choice(self.last_names).lower()}@{random.choice(self.domains)}") if format else f"{random.choice(self.first_names).lower()}.{random.choice(self.last_names).lower()}@{random.choice(self.domains)}"
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
