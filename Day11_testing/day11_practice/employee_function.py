class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.salary = 100000

    def give_raise(self, raise_amount = 5000):
        return ("Hi, " + self.first.title() + ' ' + self.last.title() + 
        ", you have raised: $" + str(raise_amount))