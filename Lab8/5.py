

def dodawanie(*liczby_do_dodania):
    suma = 0
    for i in liczby_do_dodania:
        suma += i
    return suma


def odejmowanie(liczba, *liczby_do_odejmowania):
    for i in liczby_do_odejmowania:
        liczba -= i
    return liczba


def mnozenie(liczba, *liczby_do_mnozenia):
    for i in liczby_do_mnozenia:
        liczba *= i
    return liczba


def dzielenie(liczba, *liczby_do_dzielenia):
    for i in liczby_do_dzielenia:
        if(i != 0):
            liczba /= i
    return liczba



dict1 = {'+':dodawanie, '-':odejmowanie, '*':mnozenie, '/':dzielenie}

liczba1 = int(input("Podaj liczbe"))
liczba2 = int(input("Podaj druga liczbe"))
dzialanie = input("Podaj dzialanie")

print(dict1[dzialanie](liczba1, liczba2))



