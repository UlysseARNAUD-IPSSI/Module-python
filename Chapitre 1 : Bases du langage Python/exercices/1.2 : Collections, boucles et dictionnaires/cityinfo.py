#!/usr/bin/env python3

"""
Variables utilisées
"""

infoCity = {'Lyon': (513275, 47.87, 'Lyonnais'),
            'Paris': (2206488, 105.40, 'Parisiens'),
            'Brest': (139163, 49.51, 'Brestois'),
            'Bordeaux': (249712, 49.36, 'Bordelais'),
            }

cities = ['Lyon', 'Paris', 'Brest']

"""
Fonction principale
"""


def main():
    for city in cities:
        voirVille(city)

    while True:
        choisirVille()


"""
Choix de la ville
"""


def choisirVille():
    city = input('Saisissez une ville : (END pour quitter, DUMP pour voir les villes) ').strip()
    conditions = {
        'END': quitter,
        'DUMP': voir
    }

    action = conditions.get(city, False)

    if (action == False):
        voirVille(city)
    else:
        action()



"""
Voir les informations sur une ville
"""


def voirVille(city):
    info = infoCity.get(city, False)

    if info == False:
        print('Ville inconnue')
        return

    population, surface, gentile = infoCity[city]
    print("La ville de {} contient {} habitants pour une surface de {}."
          "Les habitants de cette ville sont les {}."
          .format(city, population, surface, gentile))
    return


"""
Quitter le programme
"""


def quitter():
    print('Au revoir !')
    quit()


"""
Voir les informations de toutes les villes
"""


def voir():
    for city in infoCity:
        voirVille(city)
    return


main()
