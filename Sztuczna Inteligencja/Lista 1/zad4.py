def opt_dist(lista, liczba):
    res = len(lista)
    for i in range(len(lista) - liczba + 1):
        zmiany = 0
        for j in range(len(lista)):
            if (j < i and lista[j] == "1") or (j >= i and j < (i + liczba) and lista[j] == "0") or (j >= (i + liczba) and lista[j] == "1"):
                zmiany += 1
        res = min(res, zmiany)
    return str(res)

plik_wejsciowy = open("zad4_input.txt")
plik_wyjsciowy = open("zad4_output.txt", "w")

for przyklad in plik_wejsciowy:
    #print(przyklad[:-3] + " " + przyklad[-2])
    #print(opt_dist(przyklad[:-3], int(przyklad[-2])))
    plik_wyjsciowy.write(opt_dist(przyklad[:-3], int(przyklad[-2])) + "\n")

plik_wyjsciowy.close()
