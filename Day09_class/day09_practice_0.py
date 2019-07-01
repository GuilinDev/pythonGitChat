# 9-1 9-2 9-4
class Restaurant:

    def __init__(self, resuaurant_name, cuisine_type):
        self.resuaurant_name = resuaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 50
    
    def describe_restaurant(self):
        print("The name of resturant: " + self.resuaurant_name +
            ", and its cusine type is: " + self.cuisine_type)

    def open_restaurant(self):
        print("The " + self.resuaurant_name + " is now open.")

    def set_number_served(self, number_new_served):
        self.number_served = number_new_served

    def increment_number_served(self, new_guests):
        self.number_served += new_guests

res1 = Restaurant('Panda express', 'Chinese')
res1.describe_restaurant()
print(res1.number_served)
res1.set_number_served(100)
print(res1.number_served)

res2 = Restaurant('Abys', 'American')
res2.open_restaurant()
print(res2.number_served)
res2.increment_number_served(1000)
print(res2.number_served)

print("\n")
# 9-3 9-5
class User():

    def __init__(self, company, hobbies):
        self.company = company;
        self.hobbies = hobbies;
        self.login_attempts = 0

    def describe_user(self):
        print("Here is the user's company: ")
        print(self.company)
        print("Here are the user's hobbies: ")
        for hobby in self.hobbies:
            print(hobby, end = ' ')
        print()

    def greet_user(self, first_name, last_name):
        print("Hello, " + first_name + ' ' + last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("You have tried login " + str(self.login_attempts) + " times.")

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Google', ['skiing', 'boating'])
user1.describe_user()
user2 = User('MicroSoft', ['hiking', 'running', 'biking'])
user2.greet_user('Alen', 'Smith')

user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
print(user2.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
print(user2.login_attempts)


# 9-6 9-10
class IceCreamStand():
    def __init__(self, resuaurant_name, cuisine_type, flavor = 'vanilla'):
        self.resuaurant_name = resuaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 50
        self.flavor = flavor
    
    def describe_restaurant(self):
        print("The name of resturant: " + self.resuaurant_name +
            ", and its cusine type is: " + self.cuisine_type)

    def open_restaurant(self):
        print("The " + self.resuaurant_name + " is now open.")

    def set_number_served(self, number_new_served):
        self.number_served = number_new_served

    def increment_number_served(self, new_guests):
        self.number_served += new_guests
    
    def show_flavor(self):
        print("The flavor is: " + self.flavor)

ics1 = IceCreamStand('chip chop', 'world wide')
ics1.show_flavor();
ics2 = IceCreamStand('dukin donuts', 'American', 'strawberry')
ics2.show_flavor()