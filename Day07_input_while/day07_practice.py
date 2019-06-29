# 7-1
car_name = input("can you tell me what car do you need? ")
print("\nLet me see if I can find you a " + car_name.title() + ".");
# 7-2
people_dinning = int(input("How many people for dining? "))
if people_dinning > 8:
    print("Sorry no seats")
else:
    print("Yes Please.") 
# 7-3
numberOfTen = int(input("Inut a number: "))
if numberOfTen % 10 == 0:
    print("\nThe number " + str(numberOfTen) + " can be divided by ten.")
else:
    print("\nThe number " + str(numberOfTen) + " can't be divided by ten.")

# 7-4 
while True:
    topping = input("Please input topping for pizza (type 'quit' to quit): ")
    if topping == 'quit':
        break
    else:
        print("We will add " + topping)

# 7-5 7-6 7-7
guests = {'john': 10, 'allen': 28, 'bob': 7}
for k, v in guests.items():
    if v < 3:
        print("Hi, " + k + ", your ticket price is: free")
    elif v <= 12:
        print("Hi, " + k + ", your ticket price is: 10")
    else:
        print("Hi, " + k + ", your ticket price is: 15")

guests_number = 0
while guests_number <= 10:
    print("need more guests.")
    guests_number += 2

