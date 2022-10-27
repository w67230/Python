liczba = int(input("Podaj liczbe gwiazdek w wierszu"))
s = ""
for x in range(0,3):
    for i in range(0, liczba):
        s += "*"
    print(s)
    s = ""