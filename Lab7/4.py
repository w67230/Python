import numpy as np


def reverse(tablica):
    #zeroTab = np.array(np.zeros(shape=(5, 5)))
    #tablica = zeroTab < tablica
    for x in tablica:
        for i in x:
            if(i == 1):
            else:
    return tablica


tab = np.array(np.zeros(shape=(5,5)))

tab[:, (0, 4)] = 1
tab[(0,4), :] = 1

print(tab)

tab = reverse(tab)

print(tab)