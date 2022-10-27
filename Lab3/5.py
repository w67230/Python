
n = int(input("Podaj liczbe studentow"))
x = 0
srednia = 0
while x < n:
    print("Podaj liczbe punktow dla studenta ", x+1)
    srednia += int(input())
    x += 1

srednia /= n
print("Srednia liczba punktow wynosi: ", srednia)