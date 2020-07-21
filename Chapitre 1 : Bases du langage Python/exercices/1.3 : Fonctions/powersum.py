from math import*

"""
"""

def powersum(*,x,y,n,to_float=False):

    resultat = pow(int(x), int(n)) + pow(int(y), int(n))

    if False == bool(to_float) or '0' == to_float:
        resultat = int(resultat)

    return resultat


"""
"""


def main():
    while True:
        menu()


"""
"""


def menu():
    action = input('(END pour quitter, RUN pour lancer le script) ').strip()
    conditions = {
        'END': quitter,
        'RUN': lancerScript
    }

    for nom in conditions:
        if nom.lower() == action.lower():
            conditions[nom]()
            return

    print('Action "{}" inconnue'.format(action))
    return


"""
"""


def quitter():
    print('Au revoir !')
    quit()


"""
"""


def lancerScript():
    x = y = n = to_float = None

    while x is None:
        x = saisirNombre('Premier paramètre (x)')
    while y is None:
        y = saisirNombre('Deuxième paramètre (y)')
    while n is None:
        n = saisirNombre('Troisième paramètre (n)')
    while to_float is None:
        to_float = saisirBool('Valeur flottante (to_float) ? [0 ou 1] ')

    parametres = dict({'x':x, 'y':y, 'n':n, 'to_float':to_float})

    resultat = powersum(**parametres)

    print("La fonction powersum avec comme paramètres ({})"
          " renvoie comme resultat {}.".format(parametres, resultat))


"""
"""


def saisirNombre(message):
    valeur = input('{} : '.format(message)).strip()

    if not valeur.isdigit():
        valeur = None
        print('Nombre attendu.')

    return valeur

"""
"""

def saisirBool(message):
    valeur = input('{} : '.format(message)).strip()

    if not valeur.isdigit():
        valeur = None
        print('Booléen attendu.')

    if valeur == '0' or valeur == '1':
        return valeur

    print('Valeur 0 ou 1 attendue.')
    return


"""
"""

main()
