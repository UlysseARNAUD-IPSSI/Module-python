#!/usr/bin/env python3

def main():
    texte = input('Texte : ')
    if siPalindrome(texte):
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")
    return

def siPalindrome(texte):
    return texte == texte[::-1]


main()