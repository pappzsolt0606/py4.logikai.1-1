'''
1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
'''
szam = int(input('Adj meg egy számot! '))
if szam >= 0:
    print('A szám pozitív')
    if szam %2 == 0:
        print('A szám páros')
    else:
        print('A szám páratlan')
if szam < 0:
    print('A szám negatív')
    if szam %2 == 0:
        print('A szám páros')
    else:
        print('A szám páratlan')