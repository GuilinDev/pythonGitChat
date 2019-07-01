class Dog(): # Python的类首字母得大写
    """模拟小狗"""

    def __init__(self, name, age):
        """ 初始化属性 name and age """
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.") 

    def roll_over(self):
        print(self.name.title() + " rolled over!")

    @staticmethod
    def test():
        print("In the test.")

# 实例化对象
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is: " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# 调用方法
my_dog.sit();
my_dog.roll_over();

your_dog.roll_over()
your_dog.test()