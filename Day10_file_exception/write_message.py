# write file into sub folder
import os

cur_path = os.path.dirname(__file__) # 获取当前文件的绝对路径
file_path = cur_path + r"/text_files/programming.txt"

with open(file_path, 'w') as fo: # 会重新更新文件
    fo.write("I love programming.\n")
    fo.write("I love creating new games.\n")
with open(file_path, 'a') as fo:
    fo.write("I also love finding meaning in large datasets.\n")
    fo.write("I love creating apps that can run in a browser.\n")