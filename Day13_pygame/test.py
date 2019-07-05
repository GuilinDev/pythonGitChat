class Test:
    def __init__(self, username):
        self.username = username

    def sayHello(self):
        print("Hello, " + self.username)

test = Test("Smith")
test.sayHello()