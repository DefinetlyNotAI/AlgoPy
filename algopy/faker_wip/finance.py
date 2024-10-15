# faker.py
import random
import string
from typing import LiteralString

import validate


class Financial:
    def credit_card(self, amount: int = 1, precise: bool = False) -> list[dict[str, LiteralString | str]]:
        credit_cards = []
        for _ in range(amount):
            credit_card_number = ''.join(random.choices(string.digits, k=15))
            credit_card_number += str(
                (10 - sum(int(digit) for digit in credit_card_number) % 10) % 10)  # Luhn check digit
            if precise and not validate.Validate.CreditCard.any(credit_card_number):
                return self.credit_card(amount, precise=True)
            cvv = ''.join(random.choices(string.digits, k=3))
            expiration_date = f"{random.randint(1, 12):02d}/{random.randint(22, 30):02d}"
            credit_cards.append({
                "credit_card_number": credit_card_number,
                "cvv": cvv,
                "expiration_date": expiration_date
            })
        return credit_cards

    @staticmethod
    def bank_account(amount: int = 1) -> list[dict[str, LiteralString | str]]:
        bank_accounts = []
        for _ in range(amount):
            bank_account_number = ''.join(random.choices(string.digits, k=12))
            bank_routing_number = ''.join(random.choices(string.digits, k=8))
            bank_routing_number += str((10 - sum(int(digit) for digit in bank_routing_number) % 10) % 10)  # Check digit
            bank_accounts.append({
                "bank_account_number": bank_account_number,
                "bank_routing_number": bank_routing_number
            })
        return bank_accounts
