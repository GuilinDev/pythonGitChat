# 4-1
pizzas = ['pizza hut', "Domino's", 'California pizza kitchen', "papa john's"]
for pizza in pizzas:
    print(pizza)
    print("I don't like " + pizza + " pizza.")

print("I don't love all pizzas.")

# 4-2
birds = ['sparrow', 'swallow', 'woodpecker']
for bird in birds:
    print(bird)
    print("A " + bird + " is beneficial bird.")

print("Any of these bird would make a great forest!")

# 4-3
for value in range(1, 21):
    print(value, end = ' ')
print("\n")

# 4-4 
one_million = [value for value in range(1, 1000001)]
# print(one_million)

# 4-5
print(min(one_million))
print(max(one_million))
print(sum(one_million))

# 4-6
odd_numbers = [odd_number for odd_number in range (1, 20, 2)]
for odd_number in odd_numbers:
    print(odd_number, end = ' ')
print("\n")

# 4-7
multiple_of_3 = [value for value in range(3, 31, 3)]
for value in multiple_of_3:
    print(value, end = ' ')
print("\n")

# 4-8 4-9
cubic_values = [value**3 for value in range(1, 11)]
for cubic_value in cubic_values:
    print(cubic_value, end = ' ')
print("\n")

# 4-10
items = ['iteamA', 'iteamB', 'itemC', 'itemD', 'itemE']
print("The first three items are: " + str(items[:3]))
print("The middle three items are: " + str(items[1:4]))
print("The last three items are: " + str(items[2:]))

# 4-11
friend_pizzas = pizzas[:]
pizzas.insert(0, "my Pizza")
print(pizzas)
print(friend_pizzas)

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods1 = my_foods # shallow copy
friend_foods2 = my_foods[:] # deep copy
my_foods.insert(0, 'dumplings')
friend_foods2.append('noodles')
for my_food in my_foods:
    print(my_food, end = ' ')
print()
for friend_food1 in friend_foods1:
    print(friend_food1, end = ' ')
print()
for friend_food2 in friend_foods2:
    print(friend_food2, end = " ")
print()

# 1-13
buffets = ('noodles', 'fried rice', 'brocolli', 'bread', 'pizza')
for buffet in buffets:
    print(buffet, end = ' ')
print()
##### buffets[0] = "cabbage" # error
buffets = ('noodles', 'fried rice', 'brocolli', 'hotdog', 'steak')
for buffet in buffets:
    print(buffet, end = ' ')