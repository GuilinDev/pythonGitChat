 ## 先定义再调用
def greeter_user():
    print("Hello!")

greeter_user()

def greeter_user2(username):
    print("Hello, " + username.title() + "!")
greeter_user2("jessie")