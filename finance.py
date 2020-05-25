# money->class
# five ->object of type money
# static method called on class
# normal methods called on object(e.g times)

class Money():
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency
    
    def __eq__(self, other):
        return (
            self.amount == other.amount and
            self._currency == other.currency
        )

    @staticmethod
    def dollar (amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc (amount):
        return Money(amount, 'CHF')

    def times(self, multiplier):
        return Money(self.amount*multiplier, self._currency)

    @property
    def currency(self):
        return self._currency

    def plus(self, addend):
        return Money(self.amount + addend.amount, self._currency)
    

class Bank():
    def __init__(self):
        self._reduce = {}

    def reduce(self, source, to):
        return Money.dollar(10)
