x = int(input("Podaj wielkosc szachownicy: "))

X = []
for i in range(x):
    X.append([])

for i in range(x):
    for l in range(x):
        if(i%2 == 0):
            if (x % 2 == 0):
                X[x].append(0)
            else:
                X[x].append(1)
        else:
            if (x % 2 == 0):
                X[x].append(1)
            else:
                X[x].append(0)


print(X)