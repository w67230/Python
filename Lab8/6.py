import numpy as np


def odwrocZeraJedynki(macierz):
    indeks = 0
    for x in macierz:
        drugi_indeks = 0
        for i in x:
            if(i == 1):
                macierz[indeks][drugi_indeks] = 0
            else:
                macierz[indeks][drugi_indeks] = 1
            drugi_indeks += 1
        indeks += 1
    return macierz




macierz = np.zeros( (5,5) )


macierz[0] = np.ones((1,1))
macierz[-1] = np.ones((1,1))

for i in range(len(macierz) - 1):
    if(i == 0): continue
    macierz[i][0] = 1
    macierz[i][-1] = 1

print(macierz)

macierz = odwrocZeraJedynki(macierz)

print(macierz)


