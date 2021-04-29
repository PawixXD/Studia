# -*- coding: utf-8 -*-

import numpy as np
import pdb

kolejka = []

rozstawienie = np.ndarray(shape = (8, 8, 8, 8, 8, 8), dtype = bool)
rozstawienie[:,] = False

plik_wejsciowy = open("zad1_input.txt")
#plik_wyjsciowy = open("zad1_output.txt", "w")

odpowiedz = []

def odzyskiwanie(liczba_posuniec, ostatni):
    #print([x for x in wszystkie_ruchy if x[1][2] == "g8" and x[1][1] == "b1" and x[1][0] == "g6"])
    poprzedni_ruch = [x for x in wszystkie_ruchy if x[1] == ostatni]
    poprzedni_ruch = poprzedni_ruch[0]
    #print(poprzedni_ruch)
    liczba_posuniec -= 1
    if poprzedni_ruch[0][0] != poprzedni_ruch[1][0]:
        odpowiedz.append(str(poprzedni_ruch[0][0]) + str(poprzedni_ruch[1][0]))
    if poprzedni_ruch[0][1] != poprzedni_ruch[1][1]:
        odpowiedz.append(str(poprzedni_ruch[0][1]) + str(poprzedni_ruch[1][1]))
    if poprzedni_ruch[0][2] != poprzedni_ruch[1][2]:
        odpowiedz.append(str(poprzedni_ruch[0][2]) + str(poprzedni_ruch[1][2]))

    poprzedni_ruch = poprzedni_ruch[0]

    while (liczba_posuniec > 0):
        #print(poprzedni_ruch)
        ruch = [x for x in wszystkie_ruchy if x[1] == poprzedni_ruch]
        #print(ruch)
        ruch = ruch[0]
        if ruch[0][0] != ruch[1][0]:
            odpowiedz.append(str(ruch[0][0]) + str(ruch[1][0]))
        if ruch[0][1] != ruch[1][1]:
            odpowiedz.append(str(ruch[0][1]) + str(ruch[1][1]))
        if ruch[0][2] != ruch[1][2]:
            odpowiedz.append(str(ruch[0][2]) + str(ruch[1][2]))
        poprzedni_ruch = ruch[0]
        liczba_posuniec -= 1

    for i in range(1, len(odpowiedz) + 1):
        print(odpowiedz[-i], end=' ')

    print(odpowiedz[-len(odpowiedz)], end='')



def slownik(litera):
    dict = {
    "a": 8,
    "b": 7,
    "c": 6,
    "d": 5,
    "e": 4,
    "f": 3,
    "g": 2,
    "h": 1
    }
    return int(dict[litera])

def slownik_v2(cyfra):
    dict = {
    1: "h",
    2: "g",
    3: "f",
    4: "e",
    5: "d",
    6: "c",
    7: "b",
    8: "a"
    }
    return str(dict[cyfra])

def reset_planszy():
    plansza = np.zeros((10, 10))
    plansza[0,] = plansza[:,0] = plansza[9,] = plansza[:, 9] = -1
    return plansza

def zakres_ruchu(koordynaty, kolor, figura):
    x = int(koordynaty[1])
    y = slownik(koordynaty[0])
    if kolor == 1:
        if figura == "W":
            for i in range(4):
                a = b = 0
                while 1:
                    if (i == 0):
                        a -= 1
                    if (i == 1):
                        b += 1
                    if (i == 2):
                        a += 1
                    if (i == 3):
                        b -= 1
                    if plansza[x + a, y + b] == 0:
                        plansza[x + a, y + b] = -1
                    elif plansza[x + a, y + b] == 3:
                        plansza[x + a, y + b] = 4
                    else:
                        break
        if figura == "K":
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if plansza[x + i, y + j] == 0:
                        plansza[x + i, y + j] = -1
    else:
        if figura == "K":
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if plansza[x + i, y + j] == 0:
                        plansza[x + i, y + j] = -1
    return

def ruch_czarnego_krola(krol_cz, x, y, krol_b, wieza, ruchy):
    a = int(krol_b[1])
    b = slownik(krol_b[0])
    c = int(wieza[1])
    d = slownik(wieza[0])

    mozliwosc_ruchu = False

    for i in range(-1, 2):
        for j in range(-1, 2):
            if plansza[x + i, y + j] == 0:
                mozliwosc_ruchu = True
                if rozstawienie[a-1, b-1, c-1, d-1, x+i-1, y+j-1] == False:
                    rozstawienie[a-1, b-1, c-1, d-1, x+i-1, y+j-1] = True
                    kolejka.append(" ".join([str(ruchy+1), "white", krol_b, wieza, slownik_v2(y+j) + str(x+i)]))
                    wszystkie_ruchy.append(([krol_b, wieza, krol_cz], [krol_b, wieza, slownik_v2(y+j) + str(x+i)], ruchy))

    if (mozliwosc_ruchu == False and plansza[x, y] == 4):
        i, j = np.where(plansza == 1)
        k, l = np.where(plansza == 2)
        m, n = np.where(plansza == 4)
        ostatni = [slownik_v2(int(j)) + str(i)[1], slownik_v2(int(l)) + str(k)[1], slownik_v2(int(n)) + str(m)[1]]
        odzyskiwanie(ruchy, ostatni)
        #plik_wyjsciowy.write(str(ruchy))
        #plik_wyjsciowy.close()
        exit()
    return

def ruch_bialego_krola(krol_b, x, y, krol_cz, wieza, ruchy):
    a = int(krol_cz[1])
    b = slownik(krol_cz[0])
    c = int(wieza[1])
    d = slownik(wieza[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            if plansza[x + i, y + j] == 0:
                if rozstawienie[x+i-1, y+j-1, c-1, d-1, a-1, b-1] == False:
                    rozstawienie[x+i-1, y+j-1, c-1, d-1, a-1, b-1] = True
                    kolejka.append(" ".join([str(ruchy+1), "black", slownik_v2(y+j) + str(x+i), wieza, krol_cz]))
                    wszystkie_ruchy.append(([krol_b, wieza, krol_cz], [slownik_v2(y+j) + str(x+i), wieza, krol_cz], ruchy))
    return

def ruch_bialej_wiezy(wieza, x, y, krol_b, krol_cz, ruchy):
    a = int(krol_b[1])
    b = slownik(krol_b[0])
    c = int(krol_cz[1])
    d = slownik(krol_cz[0])

    for i in range(4):
        p = q = 0
        while 1:
            if (i == 0):
                p -= 1
            if (i == 1):
                q += 1
            if (i == 2):
                p += 1
            if (i == 3):
                q -= 1
            if plansza[x + p, y + q] == 0:
                if rozstawienie[a-1, b-1, x+p-1, y+q-1, c-1, d-1] == False:
                    rozstawienie[a-1, b-1, x+p-1, y+q-1, c-1, d-1] = True
                    kolejka.append(" ".join([str(ruchy+1), "black", krol_b, slownik_v2(y+q) + str(x+p), krol_cz]))
                    wszystkie_ruchy.append(([krol_b, wieza, krol_cz], [krol_b, slownik_v2(y+q) + str(x+p), krol_cz], ruchy))
            else:
                break
    return

wszystkie_ruchy = []

for sytuacja in plik_wejsciowy:
    liczba_ruchow = 0
    kolejka.append(" ".join([str(liczba_ruchow), sytuacja]))

    while kolejka:
        wiersz = kolejka.pop(0)

        liczba_ruchow = str.split(wiersz)[0]

        if str.split(wiersz)[1] == "black":
            kolor = 1 #czarny
        else:
            kolor = 0 #biały

        krol_bialy = str.split(wiersz)[2]
        wieza_biala = str.split(wiersz)[3]
        krol_czarny = str.split(wiersz)[4]

        plansza = reset_planszy()

        plansza[int(krol_bialy[1]), slownik(krol_bialy[0])] = 1
        plansza[int(wieza_biala[1]), slownik(wieza_biala[0])] = 2
        plansza[int(krol_czarny[1]), slownik(krol_czarny[0])] = 3

        #print(plansza)

        if kolor == 1: #czarny
            zakres_ruchu(wieza_biala, kolor, "W")
            zakres_ruchu(krol_bialy, kolor, "K")
            ruch_czarnego_krola(krol_czarny, int(krol_czarny[1]), slownik(krol_czarny[0]), krol_bialy, wieza_biala, int(liczba_ruchow))
        else:
            zakres_ruchu(krol_czarny, kolor, "K")
            ruch_bialego_krola(krol_bialy, int(krol_bialy[1]), slownik(krol_bialy[0]), krol_czarny, wieza_biala, int(liczba_ruchow))
            ruch_bialej_wiezy(wieza_biala, int(wieza_biala[1]), slownik(wieza_biala[0]), krol_bialy, krol_czarny, int(liczba_ruchow))
