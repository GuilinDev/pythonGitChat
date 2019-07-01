# 9-12
from car import Car, Battery

my_new_car123 = Car('audi', 'a8', 2019)
print(my_new_car123.get_descriptive_name())

my_new_car123.odemeter_reading = 321
my_new_car123.read_odometer()

my_new_car123 = Car('audi', 'aa4', 2020)
print(my_new_car123.get_descriptive_name())
my_new_car123.read_odometer()
my_new_car123.odemeter_reading = 2350
my_new_car123.read_odometer()

