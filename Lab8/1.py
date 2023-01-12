

def find(lista, wartosc):
    wynik = []
    for i in range(len(lista)):
        if(lista[i] == wartosc):
            wynik.append(i)
    return wynik

list = [1, 1, 3, 5, 1, 8, 1, 1, 5, 5, 1, 1, 2, 5]

lista2 = find(list, 5)

print(lista2)

