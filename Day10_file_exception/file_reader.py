# read file from sub folder
import os

cur_path = os.path.dirname(__file__) # 获取当前文件的绝对路径
file_path = cur_path + r"/text_files/pi_digits.txt"
file_path2 = cur_path + r"/text_files/pi_million_digits.txt"

with open(file_path) as file_object:
    # contents = file_object.read() ## 注意这里
    # print(contents)
    for line in file_object:
        print(line.rstrip()) 

# readlines() 创建列表
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    print(line.rstrip())
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 测试100万行的大文件
with open(file_path2) as file_object2:
    lines2 = file_object2.readlines()
pi_string2 = ''
for line2 in lines2:
    pi_string2 += line2.strip()

print(pi_string2[:52] + "...")
print(len(pi_string2))

# 测试生日
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string2:
      print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
