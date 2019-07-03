# 11-1 11-2
def cityCountry(city, country, population=''):
    if population:
        return city + ', ' + country + ', ' + str(population)
    else:
        return city + ', ' + country
    