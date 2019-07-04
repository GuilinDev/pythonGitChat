# 4.5 Tuple 4.6 PEP8
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
##### print(dimensions[100]) # IndexError: tuple index out of range
##### dimensions[0] = 100 # TypeError: 'tuple' object does not support item assignment
for dimension in dimensions:
    print(dimension)

## re-define
print(dimensions)
dimensions = (2000, 500)
print(dimensions)
dimensions = (2000, 500, 123)
print(dimensions)