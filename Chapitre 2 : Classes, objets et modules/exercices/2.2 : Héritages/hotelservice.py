#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

from datetime import date
from decimal import Decimal

class HotelService:
    """Service générique d'hôtel"""

    def __init__(self, number, when=None, cost=0, label=None):
        self.__dict__.update({
            'number': number,
            'cost': cost,
            'date': when or date.today(),
            'label': label
        })

    def __getattr__(self, name):
        return self.__dict__.get(name, None)

    def getInfo(self):
        return dict(self.__dict__)

    def showInfo(self):
        """Affiche les informations sur un service d'hôtel"""
        print(f'Numéro de chambre : {self.number}')
        print(f'Date : {self.date}')
        print(f'Prix : {self.cost:.2f}')
        print(f'label : {self.label}')

    def discount(self, rebate):
        """Applique une réduction sur le service"""
        if hasattr(self, 'rebate'):  # vérifie que self.rebate existe ou pas
            print('Warning: discount already applied (not applied)')
            return False
        else:
            self.__dict__.update({
                'rebate': Decimal(rebate),
                'cost': (self.cost * (100 - rebate)) / 100
            })
            return True


class Breakfast(HotelService):
    forbidden = 'beer wine whisky'.split()
    price = 9

    def __init__(self, number, beverage='coffee', when=None):
        self.beverage = beverage if beverage not in Breakfast.forbidden else 'coffee'
        super().__init__(number, when, Breakfast.price, 'Petit Déjeuner')

    def getInfo(self):
        return dict(super().getInfo(), beverage=self.beverage)

    def showInfo(self):
        super().showInfo()
        print(f'Boisson : {self.beverage}')

class Meal(HotelService):
    """Repas"""
    menu_price = {'basic': Decimal('15.00'), 'premium': 28, 'luxury': 98}

    def __init__(self, num, beverage, when=None, menu='basic'):
        if menu not in Meal.menu_price:
            raise ValueError(f'Menu inconnu : {menu}')

        self.menu = menu
        self.beverage = beverage
        super().__init__(num, when, Meal.menu_price[menu], f'Repas (formule {menu})')

    def getInfo(self):
        return dict(super().getInfo(), beverage=self.beverage, menu=self.menu)

    def showInfo(self):
        super().showInfo()
        print(f'Boisson : {self.beverage}')
        print(f'Menu : {self.menu}')


breakfast = Breakfast(301, 'tea', date(2020, 7, 20))
breakfast.showInfo()
print(breakfast.getInfo())
breakfast.discount(10)
breakfast.showInfo()
print(breakfast.getInfo())

myDinner = Meal(301, 'wine', menu='premium')
myDinner.showInfo()
print(myDinner.getInfo())
myDinner.discount(30)
myDinner.showInfo()
myDinner.discount(20) # sera ignorée
myDinner.showInfo()

# doit échouer sur une exception
try:
    yourDinner = Meal(301, 'wine', menu='super luxury')
except ValueError as e:
    print(f'\r\nException raised: {e.__class__.__name__}', end='')
    print(e.args)
    print('Erreur si mauvais nom de menu: OK')

# un test un peu plus "métier", un client entier !

customerServices = [Breakfast(301, 'tea', date(2018, 11, 7)),
                    Meal(301, 'wine', date(2018, 11, 7), menu='basic'),
                    Breakfast(301, 'coffee', date(2018, 11, 8)),
                    Meal(301, 'wine', date(2018, 11, 7), menu='premium'),
                    Breakfast(301, 'coffee', date(2018, 11, 9))]

print('\r\nTous les services de notre client (getInfo):')
for s in customerServices:
    print(s.getInfo())

print('\r\nPrix total :', sum((s.cost for s in customerServices)))

print('\r\nRéduction de 10% sur tout les menus premium')
for s in customerServices:
    if isinstance(s, Meal) and s.menu == 'premium':
        s.discount(10)

print('\r\nTous les services de notre client (après réduction) :')
for s in customerServices:
    print(s.getInfo())

print('\r\nPrix total :', sum((s.cost for s in customerServices)))
