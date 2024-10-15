# personal_and_finance.py
import random


class Business:
    def __init__(self):
        self.company_names = ["TechCorp", "InnovateX", "AlphaSolutions", "BetaWorks", "GammaEnterprises"]
        self.job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "Designer", "QA Engineer"]

    def generate_company_name(self, amount: int = 1):
        return [random.choice(self.company_names) for _ in range(amount)]

    def generate_job_title(self, amount: int = 1):
        return [random.choice(self.job_titles) for _ in range(amount)]

    def generate_employee_id(self, amount: int = 1, characters_to_use: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
        return [''.join(random.choices(characters_to_use, k=8)) for _ in range(amount)]
