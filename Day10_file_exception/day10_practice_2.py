# 10-11 10-12
import os, json, time
cur_path = os.path.dirname(__file__)

filename = cur_path + r"/text_files/favoriteNumber.json"

with open(filename, 'w') as fo:
    favorite_number = input("Input your favorite number: ")
    json.dump(favorite_number, fo)

time.sleep(5)

with open(filename) as fo:
    try: 
        print("I know you favorite number, it is: " + json.load(fo))
    except FileNotFoundError:
        print("I do not know your favorite")
