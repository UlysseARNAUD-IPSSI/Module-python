"""
"""

class City:

    def __init__(self, name, population=None, surface=None, gentile=None):
        self.__dict__.update({
            'name': name,
            'population': population,
            'surface': surface,
            'gentile': gentile
        })

    def __getattr__(self, name):
        return self.__dict__.get(name, None)

    def getInfo(self):
        return self.__dict__.values()

    def showInfo(self):
        print(f'\nVille : {self.name}')
        if self.population is not None: print(f' Habitants : {self.population}')
        if self.surface is not None: print(f' Surface : {self.surface} km2')
        if self.gentile is not None: print(f' Gentile : {self.gentile}')

"""
"""

def main():
    lyon = City('Lyon', population=513275, surface=47.87, gentile="Lyonnais")
    paris = City('Paris', population=2206488, surface=105.40, gentile="Paris")
    brest = City('Brest', surface=49.51)
    montpellier = City('Montpellier')

    print('\r\nTest de getInfo')
    print(paris.getInfo())
    print(lyon.getInfo())
    print(brest.getInfo())
    print(montpellier.getInfo())

    print('\r\nTest de showInfo')
    print(paris.showInfo())
    print(lyon.showInfo())
    print(brest.showInfo())
    print(montpellier.showInfo())

main()