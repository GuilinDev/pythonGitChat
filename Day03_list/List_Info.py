# 3.1 what is list
print("==========3.1==========")
## bicycles.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

## 3.1.1 visit list elements
print(bicycles[0])
print(bicycles[0].title())
## 3.1.2 index starts from 0
print(bicycles[1])
print(bicycles[-2]) # useful when do not know the length of list
## 3.1.3 use elements
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)

#### practice
names = ['John', 'Smith', 'Mark', 'Bill']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-4])
##### print(names[4]) print(names[-5]) - IndexError: list index out of range
print(names[0] + ", greetings!")
print(names[1] + ", greetings!")
print(names[2] + ", greetings!")
print(names[3] + ", greetings!")

transport_ways = ['bicycle', 'motobike', 'vehicle', 'train', 'airplane']
brands = ['Honda', 'GM', 'Cheverolet', 'Ford']
slogan = "I would like to own a " + brands[2] + " " + transport_ways[2] + "."
print(slogan)

# 3.2 Edit, Add and Delete elements
print("==========3.2==========")
"""Dynamic List"""
## 3.2.1 Edit elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
## 3.2.2 Add elements (use append() to add at end, use insert() to add at any position)
motorcycles.append('harley')
print(motorcycles)
motorcycles.insert(0, 'Jialing')
motorcycles.insert(10000, 'Jialing') # will insert at end if index is greater than the length of list (append()) - differ from visiting elements that throw errors 
print(motorcycles)
## 3.2.3 Delete elements
"""
del() - delete by index, no return value
pop() without param- delete the value at the end, return the element itself
pop() with index as param - delete any element with specified index, return the element itself
remove() with name as param - delete the element with same name value
"""
del motorcycles[-1]
print(motorcycles)

last_owned = motorcycles.pop()
print(motorcycles)
print(last_owned)
print("The last motorcucle I owned was a " + last_owned.title() + ".")
first_owned = motorcycles.pop(0)
print("The first motorcucle I owned was a " + first_owned.title() + ".")
print(motorcycles)
#### remove()
motorcycles.insert(0, 'ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive) # only delete the first element that matches
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

### Practice
#### 3-4 Guests list
guests = ['John', 'Smith', 'Mark', 'Bill']
welcome_message = ", welcome to the party!"
print("Hi," + guests[0] + welcome_message)
print("Hi," + guests[1] + welcome_message)
print("Hi," + guests[2] + welcome_message)
print("Hi," + guests[3] + welcome_message)
#### 3-5 Edit guests list
guests[1] = "Susan"
guests.pop(0);
guests.insert(0, 'Aaron')
print("\n")
print("Hi," + guests[0] + welcome_message)
print("Hi," + guests[1] + welcome_message)
print("Hi," + guests[2] + welcome_message)
print("Hi," + guests[3] + welcome_message)
#### 3-6 Add guest names
print("\nI found a larger dinning table!")
guests.insert(0, 'Linda')
guests.insert(2, 'Wayne')
guests.append("Whoever")
print("Hi, " + guests[0] + welcome_message)
print("Hi, " + guests[1] + welcome_message)
print("Hi, " + guests[2] + welcome_message)
print("Hi, " + guests[3] + welcome_message)
print("Hi, " + guests[4] + welcome_message)
print("Hi, " + guests[5] + welcome_message)
print("Hi, " + guests[6] + welcome_message)

print("WTF, only two guests can be invited!")
cannot_be_invited = guests.pop();
print("Sorry, " + cannot_be_invited)
cannot_be_invited = guests.pop();
print("Sorry, " + cannot_be_invited)
cannot_be_invited = guests.pop();
print("Sorry, " + cannot_be_invited)
cannot_be_invited = guests.pop();
print("Sorry, " + cannot_be_invited)
cannot_be_invited = guests.pop();
print("Sorry, " + cannot_be_invited)

print("Hi, " + guests[0] + " you will still be invited.")
print("Hi, " + guests[1] + " you will still be invited.")

del guests[1]
del guests[0]
print(guests)

# Organize List
print("==========3.3==========")
## 3.3.1 sort() - will not keep original order, it's a method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
## 3.3.2 sorted() - will keep original order, it's function
cars = ['bmw', 'audi', 'toyota', 'subaru'] # re-define
print(cars)
print("\nOriginal order:")
print(cars)
print("\nSorted:")
print(sorted(cars))
print("\nOriginal order again:")
print(cars)
print("\n")
"""
Notice: case sensitive
"""
## 3.3.3 Reverse list - reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru'] # re-define
print(cars)
cars.reverse() # permenently reverse list
print(cars)
print("\n")
## 3.3.4 Find length of list
cars = ['bmw', 'audi', 'toyota', 'subaru'] # re-define
print(cars)
print(len(cars)) # len starts from 1
print("\n")

### Practice
travel_places = ['Tokoyo', 'Milan', 'Madrid', 'New Castle', 'AA', 'Berlin']
print(travel_places)
print(sorted(travel_places)) # temperarely sorted
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.sort();
print(travel_places)

print("Have invited " + str(len(guests)) + " guests.") # 0, since guests now is empty after del

# 3.4 Index error
##### like above, IndexEoor: list index out of range
test_list = [1, 2, 3, 4]
print(test_list)
print(len(test_list))
print(test_list[-2])
#####  Error: print(test_list[100])
#####  Error: print(test_list[-100])

#3.5 Summary
"""
List
visit elements
append(), insert()
del, pop(), remove()
sort(), sorted()
reverse()
len()
index error out of range
"""
