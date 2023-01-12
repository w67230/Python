

def potega(lista, lista_poteg):
    if(len(lista) == len(lista_poteg)):
        for i in range(len(lista)):
            lista[i] = lista[i] ** lista_poteg[i]
    return lista

list = [1, 2, 3, 4, 5, 6]
potegi = [3, 3, 3, 3, 3, 2]

wynik = potega(list, potegi)

print(wynik)