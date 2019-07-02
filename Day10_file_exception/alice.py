import os

cur_path = os.path.dirname(__file__) # 获取当前文件的绝对路径
file_path = cur_path + r"/text_files/alice.txt"

try:
    with open(file_path) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_path + " does not exist."
    print(msg)
else:
    # word count 存入列表
    words = contents.split()
    num_words = len(words)
    print("The file " + file_path + " has about " + str(num_words) + " words.")