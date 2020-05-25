import unittest
from unittest import TestCase
from finance import Money

class CurrencyTest(TestCase):
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10),five.times(2))
        self.assertEqual(Money.dollar(15),five.times(3))

    def testEquality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))  
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))   
        self.assertEqual(Money.franc(5), Money.franc(5))  
        self.assertNotEqual(Money.franc(5), Money.franc(6))   
        self.assertNotEqual(Money.franc(5), Money.dollar(5))   

    def testFrancMultiplication(self):
        five = Money.franc(5)
        self.assertEqual(Money.franc(10),five.times(2))
        self.assertEqual(Money.franc(15),five.times(3))


if __name__ == '__main__':
    unittest.main()