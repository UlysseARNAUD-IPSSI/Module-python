from random import random, choice


def bkfst_gen(*, endp=30, spam=5):
    tableau = ['bacon', 'egg'] + (['spam'] * int(random() * spam + 1))
    while True:
        if random() * 100 < endp: yield choice(tableau)
        return None

def main():
    for curseur in range(3):
        print(*bkfst_gen())


main()
