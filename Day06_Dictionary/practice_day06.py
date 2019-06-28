# 6-1
my_friendA = {
    'first_name':'john',
    'last_name':'smith',
    'age':'27',
    'city':'New York'
}
print(my_friendA)

# 6-2
favorite_numbers = {
    'allen': 11,
    'bolt': 35,
    'cathy': 3,
    'david':-21,
    'elley':12345
}
for value in favorite_numbers: # traverse keys
    print(value, end = ' ')
    print(favorite_numbers[value])

print("\n")

# 6-3 6-4
programmings = {
    "array": "a simple data structure",
    "python": "a popular programming languages",
    "debug": "fix problems in codes",
    "agile": "a development methodology",
    "nosql": "a set of non-relational data stores"
}
for key, value in programmings.items():
    print(key + ": " + value)

print("\n")

# 6-5
rivers = {
    "Nile": "egypt",
    "Yangzi": "china",
    "Amazon": "brazil"
}

for k, v in rivers.items():
    print(k.upper() + " runs through " + v.title() + ".")

print("\n")

# 6-6 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
new_name = str(input("Input your name: "))
if new_name.lower() in favorite_languages.keys():
    print("Thanks!")
else:
    print("Can you poll?")

# 6-7 6-8 pets
my_friendB = {
    'first_name':'kevin',
    'last_name':'kyle',
    'age':'17',
    'city':'Denvor'
}
my_friendC = {
    'first_name':'wayne',
    'last_name':'nite',
    'age':'40',
    'city':'Pheonix'
}
people = [my_friendA, my_friendB, my_friendC]
for value in people:
    print()
    for k, v in value.items():
        print(k + ":" + v)

# 6-9 6-10
favorites = { 
    'personA': ['palceA','placeAA'],
    'personB': ['placeB','placeBB'],
    'personC': ['placeC','placeCC']
}
for favK, favV in favorites.items():
    print(favK + ": ", end = ' ')
    for v in favV:
        print(v, end = " ")
    print()

# 6-11 6-12
cities = {
    'dsm': {'country':'usa', 'population':200000, 'story':'middle west'},
    'winiperg': {'country':'canada', 'population':150000, 'story':'very cold'},
    'zhuzhou': {'country':'china', 'population':300000, 'story':'in the south'}
}
for city, info in cities.items():
    print("City Name: " + city)
    for k, v in info.items():
        print(k + ":" + str(v))
    print()