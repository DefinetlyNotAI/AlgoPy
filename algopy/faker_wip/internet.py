# internet.py
import random
import string


class Internet:
    def __init__(self):
        self.domains = ["example.com", "test.com", "sample.org", "demo.net"]

    @staticmethod
    def generate_username(amount: int = 1, size: int = 8,
                          charset: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-<>?!@#$%^&*()[]{};=-_"):
        return [''.join(random.choices(charset, k=size)) for _ in range(amount)]

    @staticmethod
    def generate_password(amount: int = 1, size: int = 12,
                          charset: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-<>?!@#$%^&*()[]{};=-_"):
        return [''.join(random.choices(charset, k=size)) for _ in range(amount)]

    @staticmethod
    def generate_ip_address(amount: int = 1, version=4):
        ip_addresses = []
        for _ in range(amount):
            if version == 4:
                ip_addresses.append('.'.join(str(random.randint(0, 255)) for _ in range(4)))
            elif version == 6:
                ip_addresses.append(':'.join(''.join(random.choices('0123456789abcdef', k=4)) for _ in range(8)))
        return ip_addresses

    def generate_url(self, amount: int = 1, format: str = None):
        urls = []
        for _ in range(amount):
            domain = random.choice(self.domains)
            path = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            url = f"https://{domain}/{path}"
            if format:
                url = format.replace("{domain}", domain).replace("{path}", path)
            urls.append(url)
        return urls
