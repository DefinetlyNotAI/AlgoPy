import random
from datetime import datetime, timedelta


class PersonalInformation:
    def __init__(self):
        self.first_names = [
            "John", "Jane", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank"
        ]
        self.last_names = [
            "Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez"
        ]
        self.cities = [
            "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego",
            "Dallas", "San Jose"
        ]
        self.states = [
            "NY", "CA", "IL", "TX", "AZ", "PA", "OH", "MI", "GA", "NC"
        ]
        self.countries = [
            "USA", "Canada", "Mexico", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Japan"
        ]
        self.street_names = [
            "Main", "Broadway", "Market", "Elm", "Maple", "Oak", "Pine", "Cedar", "Birch", "Walnut"
        ]
        self.domains = [
            "example.com", "test.com", "demo.com", "fake.com", "sample.com", "mock.com", "dummy.com", "faux.com",
            "simulated.com", "placeholder.com"
        ]

    def generate(self, data_type, format: str = None, amount: int = 1, card_type: str = None) -> list[str]:
        if amount is None or amount <= 0:
            raise ValueError("Amount must be greater than 0")

        methods = {
            'name': self._generate_name,
            'address': self._generate_address,
            'phone_number': self._generate_phone_number,
            'email': self._generate_email,
            'date': self._generate_date,
            'credit_card': lambda fmt: self._generate_credit_card(fmt, card_type),
            'bank_account': self._generate_bank_account
        }

        if data_type not in methods:
            raise ValueError(f"Unsupported data type: {data_type}")

        return [methods[data_type](format) for _ in range(amount)]

    def _generate_name(self, format: str = None) -> str:
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        if format:
            return format.replace("{first_name}", first_name).replace("{last_name}", last_name)
        return f"{first_name} {last_name}"

    def _generate_address(self, format: str = None) -> dict:
        address = {
            "street_address": f"{random.randint(1, 9999)} {random.choice(self.street_names)} St",
            "city": random.choice(self.cities),
            "state": random.choice(self.states),
            "country": random.choice(self.countries),
            "postal_code": f"{random.randint(10000, 99999)}"
        }
        if format:
            for key, value in address.items():
                format = format.replace(f"{{{key}}}", value)
            return format
        return address

    @staticmethod
    def _generate_phone_number(format: str = None) -> str:
        phone_number = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        if format:
            return format.replace("{phone_number}", phone_number)
        return phone_number

    def _generate_email(self, format: str = None) -> str:
        email = f"{random.choice(self.first_names).lower()}.{random.choice(self.last_names).lower()}@{random.choice(self.domains)}"
        if format:
            return format.replace("{email}", email)
        return email

    @staticmethod
    def _generate_date(format: str = None) -> str:
        start_date = datetime.now()
        end_date = start_date + timedelta(days=365)
        date = start_date + (end_date - start_date) * random.random()
        if format:
            return date.strftime(format)
        return date.strftime("%Y-%m-%d")

    def _generate_credit_card(self, format: str, card_type: str):
        prefixes = {
            'visa': '4',
            'mastercard': '5',
            'amex': '34',
            'discover': '6011'
        }

        if card_type not in prefixes:
            raise ValueError("Unsupported card type. Supported types are: visa, mastercard, amex, discover")

        prefix = prefixes[card_type]
        length = 16 if card_type != 'amex' else 15
        number = prefix + ''.join([str(random.randint(0, 9)) for _ in range(length - len(prefix) - 1)])
        number += self.__calculate_luhn_check_digit(number)

        if format:
            return format.replace("{credit_card}", number)
        return number

    @staticmethod
    def _generate_bank_account(format: str):
        number = "".join([str(random.randint(0, 9)) for _ in range(12)])
        if format:
            return format.replace("{bank_account}", number)
        return number

    @staticmethod
    def __calculate_luhn_check_digit(number):
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return str((10 - checksum % 10) % 10)


# Example usage
PI = PersonalInformation()
print(PI.generate(data_type='name', format="{first_name} {last_name}", amount=1))
print(PI.generate(data_type='address', format="{street_address}, {city}, {state}, {country}, {postal_code}", amount=1))
print(PI.generate(data_type='phone_number', amount=1))
print(PI.generate(data_type='email', amount=1))
print(PI.generate(data_type='date', format="%Y-%m-%d", amount=1))
print(PI.generate(data_type='credit_card', amount=1, format="{credit_card}", card_type='visa'))  # FIXME: actual logic
print(PI.generate(data_type='bank_account', amount=1))  # TODO TEST: actual logic
