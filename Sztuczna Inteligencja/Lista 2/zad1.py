import numpy as np

plik_wejsciowy = open("zad_input.txt")
plik_wyjsciowy = open("zad_output.txt", "w")

test = []

for wiersz in plik_wejsciowy:
    test.append(wiersz[:-1])

rozmiar = test[0].split()
rozmiar = (int(rozmiar[0]), int(rozmiar[1]))
tablica = np.zeros(rozmiar)

for i in range(1, len(test)):
    test[i] = test[i].split()

pom_list = []
mozliwe_rozklady_wierszy = []
mozliwe_rozklady_kolumn = []
pierwszy_raz = True

for obrot in range(1000):
    for i in range(0, rozmiar[0]):
        pom_list.clear()
        for j in range(len(test[i+1])):
            pom_list.append(int(test[i+1][j]))

        liczba_kratek = sum(pom_list)
        pom_list.clear()
        jeden_rozklad = []

        if pierwszy_raz == True:
            for binarny_zapis in range(1 << rozmiar[1]):
                jeden_rozklad.clear()
                rozklad = str(bin(binarny_zapis)[2:].zfill(rozmiar[1]))

                if bin(binarny_zapis).count("1") != liczba_kratek:
                    continue

                liczba_jedynek = 0
                seria = False
                kolejny_rozklad = False
                for cyfra in rozklad:
                    if cyfra == "1" and seria == False:
                        liczba_jedynek += 1
                        seria = True
                    elif cyfra == "1" and seria == True:
                        liczba_jedynek += 1
                    elif cyfra == "0" and seria == True:
                        jeden_rozklad.append(str(liczba_jedynek))
                        liczba_jedynek = 0
                        seria = False
                if (liczba_jedynek != 0):
                    jeden_rozklad.append(str(liczba_jedynek))

                if jeden_rozklad == test[i+1]:
                    pom_list.append(binarny_zapis)
            mozliwe_rozklady_wierszy.append(pom_list.copy())

        lista_wystapien = np.zeros(rozmiar[1])

        for liczba in mozliwe_rozklady_wierszy[i]:
            rozklad = str(bin(liczba)[2:].zfill(rozmiar[1]))
            for j in range(len(rozklad)):
                if (rozklad[j] == "0" and tablica[i][j] == 1) or (rozklad[j] == "1" and tablica[i][j] == 2):
                    mozliwe_rozklady_wierszy[i].remove(liczba)
                    break

        for liczba in mozliwe_rozklady_wierszy[i]:
            rozklad = str(bin(liczba)[2:].zfill(rozmiar[1]))
            for j in range(len(rozklad)):
                    if rozklad[j] == "1":
                        lista_wystapien[j] += 1

        for j in range(len(lista_wystapien)):
            if lista_wystapien[j] == len(mozliwe_rozklady_wierszy[i]):
                tablica[i][j] = 1
            if lista_wystapien[j] == 0:
                tablica[i][j] = 2

    for i in range(0, rozmiar[1]):
        pom_list.clear()
        for j in range(len(test[i+rozmiar[0]+1])):
            pom_list.append(int(test[i+rozmiar[0]+1][j]))

        liczba_kratek = sum(pom_list)
        pom_list.clear()
        jeden_rozklad = []

        if pierwszy_raz == True:
            for binarny_zapis in range(1 << rozmiar[0]):
                jeden_rozklad.clear()
                rozklad = str(bin(binarny_zapis)[2:].zfill(rozmiar[0]))

                if bin(binarny_zapis).count("1") != liczba_kratek:
                    continue

                liczba_jedynek = 0
                seria = False
                kolejny_rozklad = False
                for cyfra in rozklad:
                    if cyfra == "1" and seria == False:
                        liczba_jedynek += 1
                        seria = True
                    elif cyfra == "1" and seria == True:
                        liczba_jedynek += 1
                    elif cyfra == "0" and seria == True:
                        jeden_rozklad.append(str(liczba_jedynek))
                        liczba_jedynek = 0
                        seria = False
                if (liczba_jedynek != 0):
                    jeden_rozklad.append(str(liczba_jedynek))

                if jeden_rozklad == test[i+rozmiar[0]+1]:
                    pom_list.append(binarny_zapis)

            mozliwe_rozklady_kolumn.append(pom_list.copy())

        lista_wystapien = np.zeros(rozmiar[0])

        for liczba in mozliwe_rozklady_kolumn[i]:
            rozklad = str(bin(liczba)[2:].zfill(rozmiar[0]))
            for j in range(len(rozklad)):
                if (rozklad[j] == "0" and tablica[j][i] == 1) or (rozklad[j] == "1" and tablica[j][i] == 2):
                    mozliwe_rozklady_kolumn[i].remove(liczba)
                    break

        for liczba in mozliwe_rozklady_kolumn[i]:
            rozklad = str(bin(liczba)[2:].zfill(rozmiar[0]))
            for j in range(len(rozklad)):
                    if rozklad[j] == "1":
                        lista_wystapien[j] += 1

        for j in range(len(lista_wystapien)):
            if lista_wystapien[j] == len(mozliwe_rozklady_kolumn[i]):
                tablica[j][i] = 1
            if lista_wystapien[j] == 0:
                tablica[j][i] = 2

    pierwszy_raz = False
    if not 0 in tablica:
        break


for row in tablica:
    for element in row:
        if element == 1:
            plik_wyjsciowy.write("#")
            print("#", end='')
        if element == 2:
            plik_wyjsciowy.write(".")
            print(".", end='')
        if element == 0:
            plik_wyjsciowy.write(":")
            print(":", end='')
    print()
    plik_wyjsciowy.write("\n")
