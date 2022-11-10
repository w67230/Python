import random

x = int(input("Podaj liczbe elementow w 1 liscie"))
zestaw_1 = []

for i in range(x):
    zestaw_1.append(random.randint(1,10))

print(zestaw_1)


x = int(input("Podaj liczbe elementow w 2 liscie"))
zestaw_2 = []

for i in range(x):
    zestaw_2.append(random.randint(5,15))

print(zestaw_2)

x = int(input("Podaj liczbe: "))

for i in zestaw_1:
    if(x == i):
        print("Liczba z zestawu 1")
        break
else:
    for i in zestaw_2:
        if (x == i):
            print("Liczba z zestawu 2")
            break
    else: print("Nie ma takiej liczby w obu zestawach")

zestaw_1_2 = zestaw_1
for x in zestaw_2:
    zestaw_1_2.append(x)

zestaw_1_2.sort()
print(zestaw_1_2)