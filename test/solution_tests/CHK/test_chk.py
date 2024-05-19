import unittest
from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_chk_empty_sku(self):
        self.assertEqual(checkout(''), 0)

    def test_chk_invalid_sku(self):
        self.assertEqual(checkout('F'), -1)

    def test_chk_single_sku(self):
        self.assertEqual(checkout('A'), 50)
        self.assertEqual(checkout('B'), 30)
        self.assertEqual(checkout('C'), 20)
        self.assertEqual(checkout('D'), 15)

    def test_chk_sku_with_offer(self):
        self.assertEqual(checkout('AAA'), 130)
        self.assertEqual(checkout('BB'), 45)

    def test_chk_sku_with_mixed_offer(self):
        self.assertEqual(checkout('ABB'), 95)
        self.assertEqual(checkout('CAAA'), 150)

    def test_chk_sku_with_free_offer(self):
        self.assertEqual(checkout('EE'), 80)
        self.assertEqual(checkout('EEB'), 80)
