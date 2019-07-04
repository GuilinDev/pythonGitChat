# 4.3.4 parsing list
## traditional way
squares1 = []
for whatever_value in range(1, 11):
    squares1.append(whatever_value**2)

print(squares1)

## parsing list
squares2 = [value**2 for value in range(1, 11)]
print(squares2)