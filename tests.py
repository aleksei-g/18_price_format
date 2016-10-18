import unittest
from format_price import format_price

class PriceFormatTestCase(unittest.TestCase):
    def test_correct__float_value(self):
        input_pirce = 1999.99
        formatted_price = '1 999.99'
        self.assertEqual(format_price(input_pirce), formatted_price)
    def test_correct_int_value(self):
        input_pirce = 199999
        formatted_price = '199 999'
        self.assertEqual(format_price(input_pirce), formatted_price)
    def test_correct_str_value(self):
        input_pirce = '  199.999  '
        formatted_price = '200'
        self.assertEqual(format_price(input_pirce), formatted_price)
    def test_incorrect_str_value(self):
        input_pirce = '-199.999'
        with self.assertRaises(ValueError):
            format_price(input_pirce)
    def test_incorrect_str_value_2(self):
        input_pirce = '199,999'
        with self.assertRaises(ValueError):
            format_price(input_pirce)
    def test_incorrect_flaot_value(self):
        input_pirce = -199.999
        with self.assertRaises(ValueError):
            format_price(input_pirce)
    def test_type_err(self):
        input_pirce = [199,999]
        with self.assertRaises(TypeError):
            format_price(input_pirce)


if __name__ == '__main__':
    unittest.main()