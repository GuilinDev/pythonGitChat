# 返回字典
def build_person(first_name, last_name, age = 18):
    person = {'first': first_name, 'last': last_name, 'age': 18} # 接受参数并封装到字典中
    return person

musician = build_person('jimi', 'hendrix')
print(musician)