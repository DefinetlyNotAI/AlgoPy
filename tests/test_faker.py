import unittest
import uuid

from algopy import validate
from algopy.faker import FakeData


class TestFaker(unittest.TestCase):
    def test_barcode_generation(self):
        barcodes = FakeData.Misc.generate_barcode(amount=500, length=12)
        self.assertEqual(len(barcodes), 500)
        for barcode in barcodes:
            self.assertEqual(len(barcode), 12)
            self.assertTrue(barcode.isdigit())

    def test_uuid_generation(self):
        uuids = FakeData.Misc.generate_uuid(amount=500, version=4)
        self.assertEqual(len(uuids), 500)
        for uuid_str in uuids:
            self.assertTrue(uuid.UUID(uuid_str))

    def test_random_text_generation(self):
        texts = FakeData.Misc.generate_random_text(amount=500, length=10)
        self.assertEqual(len(texts), 500)
        for text in texts:
            self.assertEqual(len(text.split()), 10)

    def test_credit_card_generation(self):
        cards = FakeData.Financial.credit_card(amount=500)
        self.assertEqual(len(cards), 500)
        for card in cards:
            self.assertTrue(validate.Validate.CreditCard.any(card["card_number"]))
            self.assertEqual(len(card["cvv"]), 3)
            self.assertRegex(card["expiration_date"], r"\d{2}/\d{2}")

    def test_bank_account_generation(self):
        accounts = FakeData.Financial.bank_account(amount=500)
        self.assertEqual(len(accounts), 500)
        for account in accounts:
            self.assertEqual(len(account["account_number"]), 12)
            self.assertEqual(len(account["routing_number"]), 9)

    def test_name_generation(self):
        names = FakeData.Personal.name(amount=500)
        self.assertEqual(len(names), 500)
        for name in names:
            self.assertIn(" ", name)

    def test_address_generation(self):
        addresses = FakeData.Personal.address(amount=500)
        self.assertEqual(len(addresses), 500)
        for address in addresses:
            self.assertIn("street_address", address)
            self.assertIn("city", address)
            self.assertIn("country", address)
            self.assertIn("postal_code", address)

    def test_phone_number_generation(self):
        phone_numbers = FakeData.Personal.phone_number(amount=500)
        self.assertEqual(len(phone_numbers), 500)
        for number in phone_numbers:
            self.assertRegex(number, r"\d{3}-\d{3}-\d{4}")
            self.assertTrue(validate.Validate.this_phone_number(number))

    def test_email_generation(self):
        emails = FakeData.Personal.email(amount=500)
        self.assertEqual(len(emails), 500)
        for email in emails:
            self.assertIn("@", email)
            self.assertTrue(validate.Validate.this_email(email))

    def test_date_generation(self):
        dates = FakeData.Personal.date(amount=500)
        self.assertEqual(len(dates), 500)
        for date in dates:
            self.assertRegex(date, r"\d{4}-\d{2}-\d{2}")
            self.assertTrue(validate.Validate.this_date(date))

    def test_company_name_generation(self):
        company_names = FakeData.Business.company_name(amount=500)
        self.assertEqual(len(company_names), 500)

    def test_job_title_generation(self):
        job_titles = FakeData.Business.job_title(amount=500)
        self.assertEqual(len(job_titles), 500)

    def test_employee_id_generation(self):
        employee_ids = FakeData.Business.employee_id(amount=500)
        self.assertEqual(len(employee_ids), 500)
        for emp_id in employee_ids:
            self.assertEqual(len(emp_id), 8)

    def test_product_name_generation(self):
        product_names = FakeData.Product.generate_product_name(amount=500)
        self.assertEqual(len(product_names), 500)

    def test_product_category_generation(self):
        product_categories = FakeData.Product.generate_product_category(amount=500)
        self.assertEqual(len(product_categories), 500)

    def test_price_generation(self):
        prices = FakeData.Product.generate_price(amount=500, min_price=10.0, max_price=20.0)
        self.assertEqual(len(prices), 500)
        for price in prices:
            self.assertGreaterEqual(price, 10.0)
            self.assertLessEqual(price, 20.0)

    def test_username_generation(self):
        usernames = FakeData.Internet.generate_username(amount=500, size=8)
        self.assertEqual(len(usernames), 500)
        for username in usernames:
            self.assertEqual(len(username), 8)

    def test_password_generation(self):
        passwords = FakeData.Internet.generate_password(amount=500, size=12)
        self.assertEqual(len(passwords), 500)
        for password in passwords:
            self.assertEqual(len(password), 12)

    def test_ip_address_generation(self):
        ip_addresses = FakeData.Internet.generate_ip_address(amount=500, version=4)
        self.assertEqual(len(ip_addresses), 500)
        for ip in ip_addresses:
            self.assertRegex(ip, r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
            self.assertEqual(len(ip.split(".")), 4)

    def test_url_generation(self):
        urls = FakeData.Internet.generate_url(amount=500)
        self.assertEqual(len(urls), 500)
        for url in urls:
            self.assertTrue(url.startswith("https://"))
            self.assertTrue(validate.Validate.this_url(url))


if __name__ == "__main__":
    unittest.main()
