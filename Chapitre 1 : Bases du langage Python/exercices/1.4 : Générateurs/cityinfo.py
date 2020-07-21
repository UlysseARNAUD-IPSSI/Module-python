
infoCity = {'Lyon': (513275, 47.87, 'Lyonnais'),
            'Paris': (2206488, 105.40, 'Parisiens'),
            'Brest': (139163, 49.51, 'Brestois'),
            'Bordeaux': (249712, 49.36, 'Bordelais'),
            }

cities = ['Lyon', 'Paris', 'Brest']

def gen_city_info(list):
    for city in list:
        if city in infoCity:
            population, surface, gentile = infoCity[city]
            yield (population, surface, gentile)

def gen_city_info2(*cities):
    for city in cities:
            yield (city, infoCity.get(city, (None, None, None)))



def main():
    print(*gen_city_info(cities))

def main2():
    print(*gen_city_info2('Lyon', 'Montpellier', 'Paris', 'Brest', 'Concarneau'))


main()
main2()
