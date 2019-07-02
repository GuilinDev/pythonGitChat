import os

cur_path = os.path.dirname(__file__) # 获取当前文件的绝对路径
file_path = cur_path + r"/text_files/alice.txt"

def count_words(filename):
    try:
        with open(filename) as fo:
            contents = fo.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    except TypeError: # 失败时一声不吭
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")

count_words(file_path)
# Iterate目录下的所有文件
for file in os.listdir(cur_path + r"/text_files"):
    count_words(cur_path + r"/text_files/" + file)
