# 返回简单值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 实参是可选的
def get_formatted_name2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()
print(get_formatted_name2('jimi', 'hooker', 'lee'))
print(get_formatted_name2('jimi', 'hendrix'))

# 跟while循环结合练习
def get_formatted_name3(first_name, last_name):
    return first_name.title() + ' ' + last_name.title()
while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at any time to quit)")

    f_name = input("First Name:")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    print("Hello, " + get_formatted_name3(f_name, l_name) + "!")
