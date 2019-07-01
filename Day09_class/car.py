class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0 # 指定默认值

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odemeter_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odemeter_reading:
            self.odemeter_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odemeter_reading += miles

    def fill_gas_tank(self):
        """传统汽车有油箱"""
        print("This car needs a gas tank!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odemeter_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.read_odometer()

my_new_car.update_odometer(90)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

class Battery():
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    # 9-9
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

class ElectricCar(Car):

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery() # 调用Battery类的构造器

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    # 直接重写父类方法
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
        super().fill_gas_tank()

my_tesla = ElectricCar('tesla', "model3s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.describe_battery() # ElectricCar中的battery使用ElectricCar中的方法
my_tesla.battery.get_range() # ElectricCar中的battery使用Battery中的方法
# 升级电池
print("准备升级电池...")
my_tesla.battery.upgrade_battery();
print("升级电池完成!")
my_tesla.battery.get_range()

