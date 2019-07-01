# 8-9 8-10 8-11
def show_magicians(magicians):
    for magician in magicians:
        print(magician + ' the Great', end = ' ')
    print()
magicians = ['magicianA', 'magicianB', 'magicianC']
show_magicians(magicians)

# 8-12
def show_sandwishes(*sandwishes):
    print(sandwishes)
show_sandwishes('sandiwishA', 'sandiwishB')

# 8-13
# 8-14
def make_car(manufacture, model, **others):
    result = {}
    result['Manufacture'] = manufacture
    result['Model'] = model
    for key, value in others.items():
        result[key] = value
    return result
print(make_car('subaru', 'outback', color='blue', tow_package='True', price=20000))

# 8-15 8-16 8-17
from print_functions import *
printing_test()
printing_test2()