import os, json
cur_path = os.path.dirname(__file__) # 获取当前文件的绝对路径

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = cur_path + r"/text_files/username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = cur_path + r"/text_files/username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Is it you, " + username + "? (y / n)")
        isRightUser = input()
        if isRightUser == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
    

greet_user()