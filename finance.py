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
        return Sum(self, addend)
    
    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(self.amount/rate, to)

class Bank():
    def __init__(self):
        self._rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def addRate(self, source, to, rate):
        self._rates[(source, to)] = rate

    def rate(self, source, to):
        if source == to:
            return 1
        return self._rates[(source, to)]
        
class Sum():
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend
    
    def reduce(self, bank, to):
        amount = self.augend.reduce(bank, to).amount + self.addend.reduce(bank,to).amount
        return Money(amount, to)