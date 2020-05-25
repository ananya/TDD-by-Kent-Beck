# money->class
# five ->object of type money
# static method called on class
# normal methods called on object(e.g times)

class Money():
    def __init__(self, amount):
        self.amount = amount
    
    def __eq__(self, other):
        return self.amount == other.amount

    @staticmethod
    def dollar (amount):
        return Money(amount)

    @staticmethod
    def franc (amount):
        return Money(amount)

    def times(self, multiplier):
        return Money(self.amount*multiplier)