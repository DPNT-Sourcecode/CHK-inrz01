import unittest
from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_chk_empty_sku(self):
        self.assertEqual(checkout(''), -1)


if __name__ == '__main__':
    unittest.main()

