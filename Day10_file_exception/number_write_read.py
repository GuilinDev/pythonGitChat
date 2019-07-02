import os, json

cur_path = os.path.dirname(__file__) # 获取当前文件的绝对路径
file_path = cur_path + r"/text_files/numbers.json"

numbers = [2, 3, 5, 7, 100]
with open(file_path, 'w') as fo:
    json.dump(numbers, fo)

with open(file_path) as fo:
    numbers = json.load(fo)
    print(numbers)