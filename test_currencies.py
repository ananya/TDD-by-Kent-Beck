import unittest
from unittest import TestCase
from finance import Dollar

# public void testMultiplication() {
# Dollar five= new Dollar(5);
# five.times(2);
# assertEquals(10, five.amount);
# five.times(3);
# assertEquals(15, five.amount);
# }

class CurrencyTest(TestCase):
    def testMultiplication(self):
        five = Dollar(5)
        self.assertEqual(10,five.times(2))
        self.assertEqual(15,five.times(3))

if __name__ == '__main__':
    unittest.main()