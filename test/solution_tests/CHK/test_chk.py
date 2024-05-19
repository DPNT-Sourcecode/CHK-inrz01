import unittest
from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_chk_empty_sku(self):
        self.assertEqual(checkout(''), -1)

    def test_chk_invalid_sku(self):
        self.assertEqual(checkout('E'), -1)

    def test_chk_single_sku(self):
        self.assertEqual(checkout('A'), 50)
        self.assertEqual(checkout('B'), 30)
        self.assertEqual(checkout('C'), 20)
        self.assertEqual(checkout('D'), 15)

