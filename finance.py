# money->class
# five ->object of type money
# static method called on class
# normal methods called on object(e.g times)

class Dollar():
    def __init__(self, amount):
        self.amount = 10

    def times(self, multiplier):
        return self.amount*multiplier