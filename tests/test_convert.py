import unittest
from convert import Convert


class TestConvert(unittest.TestCase):
    def test_binary_to_hex_valid(self):
        self.assertEqual(Convert.Binary.to_hex(1010), 'A')

    def test_binary_to_hex_invalid_type(self):
        with self.assertRaises(Exception):
            Convert.Binary.to_hex(10.1)

    def test_binary_to_dec_valid(self):
        self.assertEqual(Convert.Binary.to_dec(1010), 10)

    def test_binary_to_dec_invalid_type(self):
        with self.assertRaises(Exception):
            Convert.Binary.to_dec(10.1)

    def test_decimal_to_roman_valid(self):
        self.assertEqual(Convert.Decimal.to_roman(1990), 'MCMXC')

    def test_decimal_to_roman_invalid(self):
        with self.assertRaises(Exception):
            Convert.Decimal.to_roman(0)

    def test_decimal_to_ascii_invalid(self):
        with self.assertRaises(Exception):
            Convert.Decimal.to_ascii(None)

    def test_decimal_to_hex_valid(self):
        self.assertEqual(Convert.Decimal.to_hex(255), 'FF')

    def test_decimal_to_hex_invalid_type(self):
        with self.assertRaises(Exception):
            Convert.Decimal.to_hex(10.1)

    def test_decimal_to_bin_valid(self):
        self.assertEqual(Convert.Decimal.to_bin(10), 1010)

    def test_decimal_to_bin_invalid_type(self):
        with self.assertRaises(Exception):
            Convert.Decimal.to_bin(10.1)

    def test_hex_to_bin_valid(self):
        self.assertEqual(Convert.Hexadecimal.to_bin('A'), 1010)

    def test_hex_to_bin_invalid_type(self):
        with self.assertRaises(Exception):
            Convert.Hexadecimal.to_bin(10)

    def test_hex_to_dec_valid(self):
        self.assertEqual(Convert.Hexadecimal.to_dec('A'), 10)

    def test_hex_to_dec_invalid_type(self):
        with self.assertRaises(Exception):
            Convert.Hexadecimal.to_dec(10)

    def test_roman_to_dec_valid(self):
        self.assertEqual(Convert.Roman.to_dec('MCMXC'), 1990)

    def test_roman_to_dec_invalid(self):
        with self.assertRaises(Exception):
            Convert.Roman.to_dec('mcmxc')

    def test_celsius_to_fahrenheit_valid(self):
        self.assertEqual(Convert.Celsius.to_fahrenheit(0), 32.0)

    def test_celsius_to_kelvin_valid(self):
        self.assertEqual(Convert.Celsius.to_kelvin(0), 273.15)

    def test_kelvin_to_celsius_valid(self):
        self.assertEqual(Convert.Kelvin.to_celsius(273.15), 0)

    def test_kelvin_to_fahrenheit_valid(self):
        self.assertEqual(Convert.Kelvin.to_fahrenheit(273.15), 32.0)

    def test_fahrenheit_to_kelvin_valid(self):
        self.assertEqual(Convert.Fahrenheit.to_kelvin(32), 273.15)

    def test_fahrenheit_to_celsius_valid(self):
        self.assertEqual(Convert.Fahrenheit.to_celsius(32), 0)

    def test_memory_conversion_valid(self):
        self.assertEqual(Convert.memory(1, 'byte', 'bit'), '8 bit')

    def test_memory_conversion_invalid(self):
        with self.assertRaises(Exception):
            Convert.memory(1, 'byte', 'invalid_unit')


if __name__ == '__main__':
    unittest.main()
