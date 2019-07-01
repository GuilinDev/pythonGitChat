# 8-1
def display_message(message):
    print(message)
display_message("I learned function at this chapter.")

# 8-2
def favoriate_books(title):
    print("One of my favoriate book is " + title + ".")
favoriate_books("Alice in Wonderland")

# 8-3 8-4
def make_shirt(size, font):
    print("The size of t-shirt: " + str(size) + ", and the font will be " + str(font) + ".")
make_shirt('medium', 'time new roma')
make_shirt(10, True)

# 8-5 8-6
def city_country(city, country):
    full_name = city.title() + ", " + country.title()
    return full_name
print(city_country('santiago', 'chile'))

# 8-7 8-8
def make_almum(singer, almum, year=2020):
    full = {'Singer': singer.title(), 'Almum': almum.title(), 'year': year}
    return full
flag = 2
while flag > 0:
    flag -= 1
    print("Input songs information: ")
    fn = input("first name: ")
    ln = input("last name: ")
    print(make_almum(fn, ln))