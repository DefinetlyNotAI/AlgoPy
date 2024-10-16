# misc.py
import os
import random
import string
import uuid


class Misc:
    @classmethod
    def __init__(cls):
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

    @staticmethod
    def generate_barcode(amount: int = 1, length: int = 12):
        return [''.join(random.choices(string.digits, k=length)) for _ in range(amount)]

    @staticmethod
    def generate_uuid(amount: int = 1, version: int = 4, namespace: uuid.UUID = uuid.uuid1(), name: str = os.name):
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
    def generate_random_text(cls, amount: int = 1, length: int = 100):
        return [' '.join(random.choices(cls.words, k=length)) for _ in range(amount)]
