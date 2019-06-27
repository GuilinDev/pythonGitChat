# 5-1 5-2
my_car = "Cheverolet"
print("Is my car == 'Cheverolet ? I predict True.")
print(my_car == 'Cheverolet')

print("\nIs my car == 'BMW ? I predict False.")
print(my_car == 'BMW')

print("\nIs my car != 'Ford ? I predict True.")
print(my_car != 'Ford')

print("\nIs my car == 'cheverolet ? I predict True.")
print(my_car.lower() == 'cheverolet')

car_price = 20000
print(car_price >= 15000)

cars = ['Cheverolet', 'Ford', 'BMW']
print('Honda' not in cars) # True
print('Ford' not in cars) # False

# 5-3 5-4 5-5
alien_color = str(input("Alien's color: "))
if alien_color == 'green':
    print("you got 5 points.")
elif alien_color == 'yellow':
    print("you got 10 points.")
elif alien_color == 'red':
    print("you got 15 points.")

# 5-6
age = int(input("Age: "))
if age < 2:
    print("Baby.")
elif age < 4:
    print("Learning walking")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teneeger")
elif age < 65:
    print("Adult")
else:
    print("Elder")

# 5-7 
favorite_fruits = ['grape', 'banana', 'peach', 'apple']
fruit1 = 'orange'
fruit2 = 'grape'
if fruit1 not in favorite_fruits:
    print("That's it.")
if fruit2 in favorite_fruits:
    print("you really like " + fruit2)

# 5-8 5-9 5-10
current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
user = str(input('Username: '))
if user.lower() == 'admin':
    print("Hello admin, would like to see a status report?")
elif user:
    print("Hello, " + user.title() + "thank you for logging in again")
else:
    print("We need to find some users!")
new_user = str(input("new user: "))
if (new_user.lower() not in current_users):
    current_users.insert(0, new_user)
else:
    print("username already existed.")

# 5-11 5-12 5-13
numbers = range(1, 10)
for value in numbers:
    if (value == 1):
        print("1st", end = ' ')
    elif value == 2:
        print("2nd", end = ' ')
    elif value == 3:
        print("3rd", end = ' ')
    else:
        print(str(value) + "th", end = ' ')
print()