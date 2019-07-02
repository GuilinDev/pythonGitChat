# 10-6 10-7 10-9
def addition(a, b):
    try:
        c = int(a) + int(b)
    except ValueError:
        print("Type two numbers!")
    except NameError:
        pass
    else:
        print("The result: " + str(c))
        return c

while True:
    num1= input("Input number1: ")
    num2 = input("Input number2: ")
    result = addition(num1, num2)
    if result:
        break
    else:
        print("You need to input two numbers!")

# 10-10
import os
cur_path = os.path.dirname(__file__) # 获取当前文件的绝对路径
file_path = cur_path + r"/text_files/moby_dict.txt"

with open(file_path) as fo:
    contents = fo.read()
    print(contents.lower().count('whale')) # 统计全文中whale出现的次数，不分大小写
