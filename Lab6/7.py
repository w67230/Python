def odwrocStringa(tekst):
    reversed = ""
    indeks = -1
    for s in range(len(tekst)):
        reversed += tekst[indeks]
        indeks -= 1
    return reversed

str = "Odwracam se stringi funkcja"
print(str)

print("Po odwroceniu: ", odwrocStringa(str))



