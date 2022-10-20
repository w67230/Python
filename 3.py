
print("1) Dodawanie")
print("2) Odejmowanie")
print("3) Mnozenie")
print("4) Dzielenie")
print("5) Potegowanie")

x = int(input("Jaka operacje chcesz wykonac? Wpisz numer: "))
if 0 < x < 6:
    a = float(input("Podaj a:"))
    b = float(input("Podaj b:"))
    if x == 4 and b == 0:
        print("Nie dziel przez zero")
        x = 6
if x == 1:
    print("Wynik: ", a + b)
elif x == 2:
    print("Wynik: ", a - b)
elif x == 3:
    print("Wynik: ", a * b)
elif x == 4:
    print("Wynik: ", a / b)
elif x == 5:
    print("Wynik: ", a ** b)
else:
    print("Zla opcja")