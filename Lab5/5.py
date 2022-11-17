

dict1 = {'name':100, 'data2':-54, 'data3':247}
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "data2": 8000,
 "city": "New york"}

for i in dict1.keys():
    if i in sample_dict.keys():
        try:
            sample_dict[i] = sample_dict[i] + dict1[i]
        except:
            print("Nie mozna dodac wartosci: ", sample_dict[i], " i ", dict1[i], " - pozostawiono wartość z pierwszego słownika")
        else:
            sample_dict[i] = sample_dict[i] + dict1[i]
    else:
        sample_dict[i] = dict1[i]

print(sample_dict)