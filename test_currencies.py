import unittest
from unittest import TestCase
from finance import Money, Bank

class CurrencyTest(TestCase):
    def testMultiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10),five.times(2))
        self.assertEqual(Money.dollar(15),five.times(3))

    def testEquality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))  
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))   
        self.assertNotEqual(Money.franc(5), Money.dollar(5))   

    def testCurrency(self):
        self.assertEqual("USD", Money.dollar(1).currency)
        self.assertEqual("CHF", Money.franc(1).currency)

    def testDifferentClassEquality(self):
        self.assertEqual(Money(10,"CHF"), Money.franc(10))

    def testSimpleAddition(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        reduced = Bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(10), reduced)

if __name__ == '__main__':
    unittest.main()