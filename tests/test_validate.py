import unittest

from algopy.validate import Validate


class TestValidate(unittest.TestCase):
    def test_valid_url(self):
        self.assertTrue(Validate.this_url('https://www.google.com/'))
        self.assertTrue(Validate.this_url('http://www.google.com/'))
        self.assertTrue(Validate.this_url('https://www.google.com/search'))
        self.assertTrue(Validate.this_url('http://www.google.com/search'))
        self.assertTrue(Validate.this_url('https://www.google.com/search?q=python'))
        self.assertTrue(Validate.this_url('http://www.google.com/search?q=python'))

    def test_invalid_url(self):
        self.assertFalse(Validate.this_url(''))
        self.assertFalse(Validate.this_url('www.google.com'))
        self.assertFalse(Validate.this_url('https://www.google.com/search?q=python '))
        self.assertFalse(Validate.this_url('ftp://www.google.com/search?q=python'))
        self.assertFalse(Validate.this_url('http://www.google.com/search?q=python', enforce_https=True))

    def test_parse_url_valid(self):
        result = Validate._url_by_parsing("http://example.com/path")
        self.assertEqual(result, {
            'protocol': 'http',
            'hostname': 'www.example.com',
            'filename': '/path',
            'TLD': True
        })

    def test_parse_url_no_protocol(self):
        result = Validate._url_by_parsing("example.com/path")
        self.assertFalse(result)

    def test_parse_url_empty(self):
        result = Validate._url_by_parsing("")
        self.assertFalse(result)

    def test_parse_url_invalid_tld(self):
        result = Validate._url_by_parsing("http://example.invalidtld/path")
        self.assertEqual(result, {
            'protocol': 'http',
            'hostname': 'www.example.invalidtld',
            'filename': '/path',
            'TLD': False
        })

    def test_validate_url_valid(self):
        result = Validate.this_url("http://example.com/path")
        self.assertTrue(result)

    def test_validate_url_no_protocol(self):
        result = Validate.this_url("example.com/path")
        self.assertFalse(result)

    def test_validate_url_empty(self):
        result = Validate.this_url("")
        self.assertFalse(result)

    def test_validate_url_invalid_protocol(self):
        result = Validate.this_url("ftp://example.com/path")
        self.assertFalse(result)

    def test_validate_url_enforce_https(self):
        result = Validate.this_url("http://example.com/path", enforce_https=True)
        self.assertFalse(result)

    def test_validate_url_invalid_hostname(self):
        result = Validate.this_url("http://exa_mple.com/path")
        self.assertFalse(result)

    def test_validate_url_invalid_filename(self):
        result = Validate.this_url("http://example.com/pa th")
        self.assertFalse(result)

    def test_validate_url_invalid_tld(self):
        result = Validate.this_url("http://example.invalidtld/path")
        self.assertFalse(result)

    def test_phone_number_valid_formats(self):
        self.assertTrue(Validate.this_phone_number("123-456-7890"))
        self.assertTrue(Validate.this_phone_number("(123)456-7890"))
        self.assertTrue(Validate.this_phone_number("(123)-456-7890"))
        self.assertTrue(Validate.this_phone_number("(123)456-7890"))
        self.assertTrue(Validate.this_phone_number("(123)-456-7890"))
        self.assertTrue(Validate.this_phone_number("1234567890"))
        self.assertTrue(Validate.this_phone_number("123 456 7890"))
        self.assertTrue(Validate.this_phone_number("123.456.7890"))

    def test_phone_number_invalid_formats(self):
        self.assertFalse(Validate.this_phone_number("123-45-7890"))
        self.assertFalse(Validate.this_phone_number("(123)45-7890"))
        self.assertFalse(Validate.this_phone_number("123-456-789"))
        self.assertFalse(Validate.this_phone_number("123-456-78900"))
        self.assertFalse(Validate.this_phone_number("123-456-78a0"))
        self.assertFalse(Validate.this_phone_number("123-456-78 0"))
        self.assertFalse(Validate.this_phone_number("123-456-78.0"))
        self.assertFalse(Validate.this_phone_number("123-456-78+0"))

    def test_phone_number_empty_string(self):
        self.assertFalse(Validate.this_phone_number(""))

    def test_phone_number_none(self):
        self.assertFalse(Validate.this_phone_number(None))

    def test_date_valid_formats(self):
        self.assertTrue(Validate.this_date("2020/10/01"))
        self.assertTrue(Validate.this_date("2020-10-01"))
        self.assertTrue(Validate.this_date("01-10-2020"))
        self.assertTrue(Validate.this_date("01/10/2020"))
        self.assertTrue(Validate.this_date("2020\\10\\01"))
        self.assertTrue(Validate.this_date("01\\10\\2020"))
        self.assertTrue(Validate.this_date("01 10 2020"))
        self.assertTrue(Validate.this_date("2020 10 01"))

    def test_date_invalid_formats(self):
        self.assertFalse(Validate.this_date("20296/10/01"))
        self.assertFalse(Validate.this_date("2020-88-01"))
        self.assertFalse(Validate.this_date("01-10-202"))
        self.assertFalse(Validate.this_date("2020\\10\\677"))
        self.assertFalse(Validate.this_date("242\\10\\2020"))

    def test_date_empty_string(self):
        self.assertFalse(Validate.this_date(""))

    def test_date_none(self):
        self.assertFalse(Validate.this_date(None))

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
