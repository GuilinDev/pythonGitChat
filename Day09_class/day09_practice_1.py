# 9-7 9-8 9-11
from day09_practice_0 import User
class Admin(User):
    
    def __init__(self, company, hobbies):
        super().__init__(company, hobbies)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Admin at " + self.company + " can do: ")
        for privilege in self.privileges:
            print(privilege)


admin = Admin('Apple', ['cooking'])
admin.show_privileges()

# 9-13
from collections import OrderedDict
class testOrderDict():

    def __init__(self,  number):
        self.number = number

    def show_details(self):
        result1 = OrderedDict()
        result1['a'] = 1
        result1['b'] = 2
        result1['c'] = 3
        result1['d'] = 4
        print(result1)

        result2 = {} # 3.7.x开始正常的dict也是有序的
        result2['a'] = 1
        result2['b'] = 2
        result2['c'] = 3
        result2['d'] = 4
        print(result2)
test = testOrderDict(11111)
test.show_details()

# 9-14 9-15
from random import randint
class Die():
    def __init__(self, sides):
        self.sides = sides;

    def roll_die(self):
        print("This is a " + str(self.sides) + "-sided die.")
        for side in range(9): # 掷10次
            points = randint(1, self.sides) # 前开后开
            print("You get: " + str(points) + " points.")
die1 = Die(6)
die1.roll_die()
die2 = Die(10)
die2.roll_die()


