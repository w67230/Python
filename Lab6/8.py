def liczbaLiterITD(tekst):
    slownik = {"duzeLitery":0,
               "maleLitery":0,
               "inneZnaki(spacjeTez)":0}
    for s in tekst:
        if (s.isupper()):
            slownik["duzeLitery"] += 1
        elif (s.islower()):
            slownik["maleLitery"] += 1
        else:
            slownik["inneZnaki(spacjeTez)"] += 1
    return slownik

mojSlownik = liczbaLiterITD("SprAwDZAm soBie Duze I maLE liTeRy **&")

print(mojSlownik)