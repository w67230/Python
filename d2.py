dwo = str(input("Podaj liczbe binarna"))
wartosc = 0
bin = True
for x in dwo:
    if x == "1":
        if wartosc == 0:
            wartosc = 1
        else:
            wartosc = wartosc * 2 + 1
    elif x == "0":
        if wartosc != 0:
            wartosc *= 2
    else:
        print("To nie jest liczba binarna!")
        bin = False
        break

if bin:
    print(wartosc)
