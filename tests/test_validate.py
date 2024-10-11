import unittest

from algopy.validate import Validate


class TestValidate(unittest.TestCase):
    def test_email_valid(self):
        self.assertTrue(Validate.this_email("test@example.com"))

    def test_email_invalid(self):
        self.assertFalse(Validate.this_email("test@ example.com"))

    def test_url_valid(self):
        self.assertTrue(Validate.this_url("https://www.example.com"))
        self.assertTrue(Validate.this_url("https://www.example.me"))
        self.assertTrue(Validate.this_url("http://www.example.com", False))

    def test_url_invalid(self):
        self.assertFalse(Validate.this_url("https:// example .com"))
        self.assertFalse(Validate.this_url("https:// example . lolz"))
        self.assertFalse(Validate.this_url("http://www.example.com"))
        self.assertFalse(Validate.this_url(None))

    def test_phone_number_valid(self):
        self.assertTrue(Validate.this_phone_number("123-4567-890"))
        self.assertTrue(Validate.this_phone_number("(000)-123-4567-890"))
        self.assertTrue(Validate.this_phone_number("123 4567 890"))
        self.assertTrue(Validate.this_phone_number("123 4567-890"))
        self.assertTrue(Validate.this_phone_number("(000) 123 4567 890"))
        self.assertTrue(Validate.this_phone_number("(000) 123-4567-890"))

    def test_phone_number_invalid(self):
        self.assertFalse(Validate.this_phone_number("(000)-123-45-7890"))
        self.assertFalse(Validate.this_phone_number("(0000)-123-4578-900"))
        self.assertFalse(Validate.this_phone_number("123-45-7890"))

    def test_date_valid(self):
        self.assertTrue(Validate.this_date("2020/10/01"))
        self.assertTrue(Validate.this_date("2020-10-01"))
        self.assertTrue(Validate.this_date("01-10-2020"))
        self.assertTrue(Validate.this_date("01/10/2020"))
        self.assertTrue(Validate.this_date("2020\\10\\01"))
        self.assertTrue(Validate.this_date("01\\10\\2020"))
        self.assertTrue(Validate.this_date("01 10 2020"))
        self.assertTrue(Validate.this_date("2020 10 01"))

    def test_date_invalid(self):
        self.assertFalse(Validate.this_date("20296/10/01"))
        self.assertFalse(Validate.this_date("2020-88-01"))
        self.assertFalse(Validate.this_date("01-10-202"))
        self.assertFalse(Validate.this_date("2020\\10\\677"))
        self.assertFalse(Validate.this_date("242\\10\\2020"))

    def test_credit_card_amex_valid(self):
        self.assertTrue(Validate.CreditCard.american_express("378282246310005"))

    def test_credit_card_amex_invalid(self):
        self.assertFalse(Validate.CreditCard.american_express("37828224631000"))

    def test_credit_card_visa_valid(self):
        self.assertTrue(Validate.CreditCard.visa("4111111111111111"))

    def test_credit_card_visa_invalid(self):
        self.assertFalse(Validate.CreditCard.visa("4111111111111"))

    def test_credit_card_mastercard_valid(self):
        self.assertTrue(Validate.CreditCard.mastercard("5555555555554444"))

    def test_credit_card_mastercard_invalid(self):
        self.assertFalse(Validate.CreditCard.mastercard("555555555555444"))

    def test_credit_card_discover_valid(self):
        self.assertTrue(Validate.CreditCard.discover("6011111111111117"))

    def test_credit_card_discover_invalid(self):
        self.assertFalse(Validate.CreditCard.discover("601111111111111"))

    def test_credit_card_jcb_valid(self):
        self.assertTrue(Validate.CreditCard.jcb("3530111333300000"))

    def test_credit_card_jcb_invalid(self):
        self.assertFalse(Validate.CreditCard.jcb("353011133330000"))

    def test_credit_card_maestro_valid(self):
        self.assertTrue(Validate.CreditCard.maestro("6759649826438453"))

    def test_credit_card_maestro_invalid(self):
        self.assertFalse(Validate.CreditCard.maestro("675964982643845"))

    def test_credit_card_any_valid(self):
        self.assertTrue(Validate.CreditCard.any("4111111111111111"))

    def test_credit_card_any_invalid(self):
        self.assertFalse(Validate.CreditCard.any("4111111111111"))
