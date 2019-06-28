favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("Sarah's favorite language is: " + favorite_languages['sarah'] + ".")
for testKey, testValue in favorite_languages.items():
    print(testKey.title() + "'s favorite language is " +
    testValue.title() + ".")
print("\n")
for testKey, testValue in sorted(favorite_languages.items()):
    print(testKey.title() + "'s favorite language is " +
    testValue.title() + ".")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favoriate language is " +
        favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# re define
favorite_languages = {
    'jen': ['python', 'go'],
    'sarah': ['c', 'java'],
    'edward': ['ruby', 'js'],
    'phil': ['python']
}
for name in favorite_languages:
    print(name.title() + "'s favorite languages are: ", end = ' ')
    for language in favorite_languages[name]:
        print(language, end = ' ')
    print()