# 7-8
sandwich_orders = ['tuna', 'turkey', 'roasted beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.insert(0, current_sandwich)

print("I made all sandwiches!")
print(finished_sandwiches)

# 7-9
sandwich_orders = ['tuna', 'pastrami', 'pastrami','turkey', 'pastrami','roasted beef', 'pastrami']
print(sandwich_orders)
print("The pastrami is already out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

# 7-10
responses = {}
while True:
    name = input("What is your name? ")
    place = input("where you want go? ")

    responses[name] = place
    for k, v in responses.items():
        print(k + "'s place is: " + v + ".")
    message = input("Would like to take another survey? (yes / no) ")
    if message == 'yes':
        continue
    else:
        break