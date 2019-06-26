# 4.3 Create number list
## range(), open at left, close at right
for value in range(1, 5): # so does not include number 5
    print(value)

# use range() to create list, list() is a function
numbers = list(range(1, 6))
print(numbers)

# also can specify step size
even_numbers = list(range(2, 11, 2)) # start, end, step size
print(even_numbers)

# min(), max(), sum()
digits = list(range(1, 20, 3))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))