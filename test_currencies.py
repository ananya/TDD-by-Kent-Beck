import unittest
from unittest import TestCase
from finance import Dollar


class CurrencyTest(TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        self.assertEqual(10,five.times(2))
        self.assertEqual(15,five.times(3))

if __name__ == '__main__':
    unittest.main()