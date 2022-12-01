def dodawanie(pierwszaLiczba, *liczbyDoDodawania):
    for i in liczbyDoDodawania:
        pierwszaLiczba += i
    return pierwszaLiczba

def odejmowanie(pierwszaLiczba, *liczbyDoOdejmowania):
    for i in liczbyDoOdejmowania:
        pierwszaLiczba -= i
    return pierwszaLiczba

def mnozenie(pierwszaLiczba, *liczbyDoMnozenia):
    for i in liczbyDoMnozenia:
        pierwszaLiczba *= i
    return pierwszaLiczba

def dzielenie(pierwszaLiczba, *liczbyDoDzielenia):
    for i in liczbyDoDzielenia:
        pierwszaLiczba /= i
    return pierwszaLiczba


slownik = {"dodawanie":dodawanie(2, 3, 5, -2, 5),
           "odejmowanie":odejmowanie(150, 43, 1, -9, 18),
           "mnozenie":mnozenie(2, 2, 2, 2, 2, 2, 2),
           "dzielenie":dzielenie(100, 2, 5, 2)}

print(slownik)
