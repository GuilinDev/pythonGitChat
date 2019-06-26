# 4.4 Python list, slice, copy

## slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # open at left, close at right
print(players[:4])
print(players[2:])
for player in players[:3]:
    print(player, end = ' ')
print()

## copy
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods1 = my_foods # shallow copy
friend_foods2 = my_foods[:] # deep copy
my_foods.insert(0, 'dumplings')
friend_foods2.append('noodles')
print(my_foods)
print(friend_foods1)
print(friend_foods2)