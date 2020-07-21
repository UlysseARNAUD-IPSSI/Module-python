#!/usr/bin/env python3

from collections import Counter

def main():
    texte = input('Texte : ')
    compte = Counter(texte.split(' '))
    for mot in compte:
        print('le mot {} apparait {} fois'.format(mot, compte[mot]))
    return

main()