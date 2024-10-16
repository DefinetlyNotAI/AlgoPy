# personal_and_finance.py
import random


class Business:
    @classmethod
    def __init__(cls):
        cls.company_names = ["TechCorp", "InnovateX", "AlphaSolutions", "BetaWorks", "GammaEnterprises"]
        cls.job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "Designer", "QA Engineer"]

    @classmethod
    def generate_company_name(cls, amount: int = 1):
        return [random.choice(cls.company_names) for _ in range(amount)]

    @classmethod
    def generate_job_title(cls, amount: int = 1):
        return [random.choice(cls.job_titles) for _ in range(amount)]

    @staticmethod
    def generate_employee_id(amount: int = 1, characters_to_use: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
        return [''.join(random.choices(characters_to_use, k=8)) for _ in range(amount)]


class ProductDataGenerator:
    @classmethod
    def __init__(cls):
        cls.product_names = ["Widget", "Gadget", "Thingamajig", "Doodad", "Gizmo"]
        cls.product_categories = ["Electronics", "Home", "Toys", "Clothing", "Sports"]

    @classmethod
    def generate_product_name(cls, amount: int = 1):
        return [random.choice(cls.product_names) for _ in range(amount)]

    @classmethod
    def generate_product_category(cls, amount: int = 1):
        return [random.choice(cls.product_categories) for _ in range(amount)]

    @staticmethod
    def generate_price(amount: int = 1, min_price: float = 1.0, max_price: float = 100.0):
        return [round(random.uniform(min_price, max_price), 2) for _ in range(amount)]
