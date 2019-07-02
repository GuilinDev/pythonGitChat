# 10-1 10-2
import os

cur_path = os.path.dirname(__file__) # 获取当前文件的绝对路径
file_path = cur_path + r"/text_files/learning_python.txt"

# 整个文件读取
with open(file_path) as fo:
    contents = fo.read()
    print(contents)

print()
# 一行行读取
with open(file_path) as fo:
    lines = fo.readlines()
    for line in lines:
        print(line.strip())

print()
# 存入到列表
result_list = []
with open(file_path) as fo:
    lines = fo.readlines()
    for line in lines:
        newLine = line.replace('you', 'I') # 使用replace()不改变原来的值
        result_list.insert(0, newLine.strip())
for oneL in result_list:
    print(oneL)


print("\n")
# 10-3 10-4 10-5
file_path_write = cur_path + r"/text_files/guests.txt"
with open(file_path_write, 'w') as fo:
    count = 0
    while count < 3:
        name = input("Type name: ")
        fo.write(name + '\n')
        count += 1