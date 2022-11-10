import random


punkty = []
for x in range(15):
    punkty.append(random.randint(0,50))

min = 100
max = 0
for x in punkty:
    if(x > max): max = x
    if(x < min): min = x

print("Najwieksza liczba punktow: ", max)
print("Najmniejsza liczba punktow: ", min)

x = int(input("Podaj liczbe punktow: "))

index = 0
for i in punkty:
    if(i == x):
        print("Indeks: ", index)
        break
    else:
        index += 1
else:
    print("Nie ma takiej liczby punktow")

srednia = 0.0
for i in punkty:
    srednia += i
srednia /= (len(punkty)+1)
print("Srednia punktow: ", srednia)

pow = 0
pon = 0
for i in punkty:
    if(i < srednia):
        pon += 1
    else:
        pow += 1

print("Punkty powyzej sredniej zdobylo: ", pow, " studentow")
print("Punkty ponizej sredniej zdobylo: ", pon, " studentow")

print("Punkty powyzej sredniej:")
for i in punkty:
    if(i >= srednia):
        print(i, end=' ')

print()

print("Punkty ponizej sredniej:")
for i in punkty:
    if(i < srednia):
        print(i, end=' ')


