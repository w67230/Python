def cos(**slownik):
    end = " "
    for i in slownik.keys():
        if(i == "end"):
            end = slownik[i]
    for i in slownik.keys():
        if(i != "end"):
            print(slownik[i], end=end)


cos(a = 1, b = 2, c = 3)