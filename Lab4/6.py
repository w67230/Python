#pierwszy sposob
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(-1, -4, -1):
    liczba = X[-1]
    X.pop(-1)
    X.reverse()
    X.append(liczba)
    X.reverse()
print(X)

#drugi sposob
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liczba = X[0:7]
X[0:7] = []
for i in liczba:
    X.append(i)
print(X)

#drugie polecenie
Y = X
Y[2] = 173
print(Y)
print(X)
