import numpy as np

macierz = np.random.randint(low=0, high =11, size=(5,5))
print(macierz)

print("Max", macierz.max())
print("Min", macierz.min())
print("Max wiersz", macierz.max(axis=1))
print("Max kolumna", macierz.min(axis=0))