# 2.1 Run hello word
print("==========2.1==========")


print("Hello Python world!")

## Use method to print Hello World
def main():
  print("Hello Python world!")


if __name__ == "__main__":
  main()



# 2.2 Variables 
print("==========2.2==========")


message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

# 2.2.1
## Naming rules for python variables
# 2.2.2
## Error handeling

# practice for 2.2
# 2-1 simple message
simple_message = "This is the test for simple message."
print(simple_message)
# 2-2 multiple simples messages
multiple_simple_message = "This message will be changed."
print(multiple_simple_message)
multiple_simple_message = "This message has been changed."
print(multiple_simple_message) 


# 2.3 String
print("==========2.3==========")
"""
Anything be cited by apostrophe ' or double quotes " are strings;
No need to escape like Java and C++
"""
## 2.3.1
name = "ada lovelace"
print(name)
print(name.title())
print(name.upper())
print(name.lower())

## 2.3.2 Concatenate Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())

message = "Hello, " + full_name.title() + "!"
print(message)

## 2.3.3 Use Tabs and Line breaks
print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

## 2.3.4 Delete Spaces
"""
rstrip()
"""
favorite_language = ' python '
print(favorite_language.rstrip()) # delete spaces at the end(right)
print(favorite_language.lstrip()) # delete spaces at the start(left)
print(favorite_language.strip()) # delete spaces at both sides

## 2.3.5 single and double quote endings
## 2.3.6 legacy print in python2, not a fucntion

# 2.4 Number
print("==========2.4==========")

## 2.4.1 Integer
"""
+
-
*
/
//
**
"""

## 2.4.2 Float
print(3.1415926 + 1000)
print(5 * 0.13)

## 2.4.3 Use str() to avoid type error
"""
Convert variable to String
"""
age = 23
message = "Happy " + str(age) + "rd Birthday!" # will throw error: message = "Happy " + age + "rd Birthday!"
print(message)

print(5 + 3)
print(11 - 3)
print (20 * 0.4)
print (64 / 8)


# 2.5 Comment
# Single line comment
"""
Muliple line comments 1
Muliple line comments 2
"""

# Zen of Python
"""
1) import this - at IDLE you can see all zen of python when type it

2) Simple is better than complex.
3) Complex is better than complicated.
4) Readability counts;
5) There should be one -- and preferably only one -- obvious way to do it.
6) Now is better than never.

"""