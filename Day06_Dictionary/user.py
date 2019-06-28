user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

many_users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for user, userinfo in many_users.items():
    print(user)
    for k, v in userinfo.items():
        print(k + ": " + v + ";", end = " ")
    print()