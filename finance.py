# money->class
# five ->object of type money
# static method called on class
# normal methods called on object(e.g times)

class Money():
    def __init__(self, amount):
        self.amount = amount
    
    def __eq__(self, other):
        return self.amount == other.amount

class Dollar (Money):
    def times(self, multiplier):
        return Dollar(self.amount*multiplier)

class Franc(Money):
    def times(self, multiplier):
        return Franc(self.amount*multiplier)
