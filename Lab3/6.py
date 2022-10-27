n = int(input("Podaj liczbe studentow"))
x = 0
srednia = 0
wpisane = 0
while True:
    print("Podaj liczbe punktow dla studenta ", x+1)
    wpisane = int(input())
    if wpisane < 0 or wpisane > 100: continue
    srednia += wpisane
    x += 1
    if x == n: break

srednia /= n
print("Srednia liczba punktow wynosi: ", srednia)