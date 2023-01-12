

def znaki(moj_string):
    dict1 = dict()
    for s in moj_string:
        if(s in dict1.keys()):
            dict1[s] += 1
        else:
            dict1[s] = 1
    return dict1

slownik = znaki("znaki napisu")

print(slownik)