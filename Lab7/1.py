import numpy as np

list = []
liczbaElementow = 8
for x in range(liczbaElementow - 1, -1, -1):
    list.append(2 ** x)


wagi = np.array(list)

liczba_bin = np.random.randint(0, 2, 8)

liczba_dziesietna = np.array(liczba_bin * wagi)

print(liczba_bin)
print(liczba_dziesietna)

print(liczba_dziesietna.sum())