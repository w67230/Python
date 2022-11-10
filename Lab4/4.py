

imiona = ["Kasia", "Tomek", "Jan", "Ola", "Jerzy", "Marek", "Piotr", "Zuzia", "Bartek", "Jacek"]

imiona[3] = "Ukasz"
imiona[4] = "Marcin"

imiona.pop(6)

print(imiona)

imiona.insert(0, "Kamil")
imiona.insert(1, "Karol")
imiona.insert(2, "Kuba")

str = input("Podaj imie")

imiona.remove(str)

imiona[-1] = "Henryk"

print(imiona[0], imiona[1], imiona[2], imiona[-1], imiona[-2], imiona[-3])

str = input("Podaj imie: ")

for x in imiona:
    if(x == str):
        print(str , " znajduje sie na liscie")
        break
else:
    print("Podane imie nie znajduje sie na liscie")

imiona.sort()
print(imiona)
imiona.reverse()
print(imiona)

for i in range(int(len(imiona)/2)):
    imiona.pop(-1)

print(imiona)
