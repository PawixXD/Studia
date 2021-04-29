import numpy as np
import random


blotkarz = []
figurant = []
blotki = []
figury = []

def karty_blotkarza():
    for i in range (1, 10):
        for j in range (1, 5):
            blotki.append((i, j))

def karty_figuranta():
    for i in range (1, 5):
        for j in range (1, 5):
            figury.append((i, j))

def sila_ukladu(karty):
    karty = sorted(karty)
    wynik = 1
    if (karty[0][1] == karty[1][1] == karty[2][1] == karty[3][1] == karty[4][1]): #kolor
        wynik = max(wynik, 6)
        if (karty[0][0] + 4) == (karty[0][0] + 3) == (karty[0][0] + 2) == (karty[0][0] + 1) == (karty[0][0]): #poker
            wynik = max(wynik, 9)
    if (karty[0][0] == karty[1][0] == karty[2][0] == karty[3][0]) or (karty[1][0] == karty[2][0] == karty[3][0] == karty[4][0]): #kareta
        wynik = max(wynik, 8)
    if ((karty[0][0] == karty[1][0] == karty[2][0]) and (karty[3][0] == karty[4][0])) or ((karty[0][0] == karty[1][0]) and (karty[2][0] == karty[3][0] == karty[4][0])): #full
        wynik = max(wynik, 7)
    if (karty[0][0] + 4) == (karty[0][0] + 3) == (karty[0][0] + 2) == (karty[0][0] + 1) == (karty[0][0]): #strit
        wynik = max(wynik, 5)
    if (karty[0][0] == karty[1][0] == karty[2][0]) or (karty[1][0] == karty[2][0] == karty[3][0]) or (karty[2][0] == karty[3][0] == karty[4][0]): #trójka
        wynik = max(wynik, 4)
    if ((karty[0][0] == karty[1][0]) and (karty[2][0] == karty[3][0])) or ((karty[0][0] == karty[1][0]) and (karty[3][0] == karty[4][0])) or ((karty[1][0] == karty[2][0]) and (karty[3][0] == karty[4][0])): #2 pary
        wynik = max(wynik, 3)
    if ((karty[0][0] == karty[1][0]) or (karty[1][0] == karty[2][0]) or (karty[2][0] == karty[3][0]) or (karty[3][0] == karty[4][0])): #para
        wynik = max(wynik, 2)

    return wynik

karty_blotkarza()
karty_figuranta()
zwyciestwo = 0

for i in range(10000):
    random.shuffle(blotki)
    blotkarz = blotki[:5]
    random.shuffle(figury)
    figurant = figury[:5]
    sila_blotkarza = sila_ukladu(blotkarz)
    sila_figuranta = sila_ukladu(figurant)
    if (sila_blotkarza > sila_figuranta):
        zwyciestwo += 1
    print("Procent zwyciest blotkarz:", zwyciestwo/(i + 1))
