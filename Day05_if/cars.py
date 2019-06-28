#5.1 5.2
## lower() upper()
cars = ['audu', 'bmw','subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

## != , toppings.py
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

## magic_number.py
answer = 17

if answer != 42:
    print("That's not correct number. Try again.")

## and, or, banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

## True, False
## if-else, if-elif-else
## amusement_park.py
age = 12
if age < 4:
    print("Your admission cos is $0.")
elif age < 18:
    print("Your admission cos is $5.")
elif age < 65:
    print("Your admission cos is $10.")
else:
    print("Your admission cos is $5.")

## check empty list
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print("Adding " + topping + ".")
    print("\nFinished making your pizza.")
else:
    print("you sure what a plain pizza?")