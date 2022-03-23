from itertools import combinations
import numpy as np
from decimal import *
getcontext().prec = 4

navn = 0
value = 1
points = 2
megadriver = True

runder = 1
max_value = 100
min_value = 90

nonTurbo = ["Ham", "Ver", "Rus"]
nonMega = []
print("--------------------------------------------------------------------------------")
constuctor = [
    ["Mer", 34.5, 57],
    ["Red", 32.5, 4],
    ["Fer", 25.0, 76],
    ["McL", 18.5, 9],
    ["AsM", 11.5, 14],
    ["Alp", 14.0, 24],
    ["AlT", 10.5, 10],
    ["Alf", 8.0, 31],
    ["Will", 7.0, 15],
    ["Has", 6.0, 27]
]
constuctor = [
    ["Mer", 34.5, 40],
    ["Red", 32.5, 60],
    ["Fer", 25.0, 76],
    ["McL", 18.5, 9],
    ["AsM", 11.5, 14],
    ["Alp", 14.0, 24],
    ["AlT", 10.5, 10],
    ["Alf", 8.0, 31],
    ["Will", 7.0, 15],
    ["Has", 6.0, 27]
]

drivers = [
    ["Ham", 31.0, 34],
    ["Ver", 30.5, 5],
    ["Rus", 24, 28],
    ["Lec", 18.0, 49],
    ["Per", 17.5, 4],
    ["Sai", 17.0, 32],
    ["Lan", 16.0, 1],
    ["Ric", 14.5, 13],
    ["Gas", 13.5, 0],
    ["Alo", 12.5, 9],
    ["Oco", 12.0, 20],
    ["Vet", 11.5, 4],
    ["Str", 9.5, 15],
    ["Bot", 9.0, 22],
    ["Tsu", 8.5, 19],
    ["Zho", 8.0, 14],
    ["Alb", 7.5, 10],
    ["Lat", 7, 10],
    ["Msc", 6.5, 5],
    ["Mag", 5.5, 27]
]
drivers = [
    ["Ham", 31.0, 28],
    ["Ver", 30.5, 38],
    ["Rus", 24, 28],
    ["Lec", 18.0, 49],
    ["Per", 17.5, 25],
    ["Sai", 17.0, 32],
    ["Lan", 16.0, 1],
    ["Ric", 14.5, 13],
    ["Gas", 13.5, 0],
    ["Alo", 12.5, 9],
    ["Oco", 12.0, 20],
    ["Vet", 11.5, 4],
    ["Str", 9.5, 15],
    ["Bot", 9.0, 22],
    ["Tsu", 8.5, 19],
    ["Zho", 8.0, 14],
    ["Alb", 7.5, 10],
    ["Lat", 7, 10],
    ["Msc", 6.5, 5],
    ["Mag", 5.5, 20]
]

lage = []
lager = []

for i in constuctor:
    nonTurbo.append(i[navn])
    nonMega.append(i[navn])

for i in drivers:
    nonTurbo.append(i[navn]+"_MD")

if True:
    comb = combinations(drivers, 5)
    comb = np.array(list(comb))
    comb = comb.tolist()
    for i in comb:
        for u in constuctor:
            lage.append([u]+i)

    for i in lage:
        verdi = 0
        poeng = 0
        for u in range(len(i)):
            i[u] = i[u][::]
            i[u][points] = int(i[u][points])
            verdi += Decimal(i[u][value])
        i = sorted(i, key=lambda x: x[points], reverse=True)

        test = True
        if megadriver:
            test1 = True
        else:
            test1 = False

        for u in range(len(i)):
            i[u][points] /= runder
            i[u][points] = round(i[u][points], 2)

            if test1:
                try:
                    nonMega.index(i[u][navn])
                except ValueError:
                    i[u][points] *= 3
                    i[u][navn] += "_MD"
                    test1 = False

            if test:
                try:
                    nonTurbo.index(i[u][navn])
                except ValueError:
                    i[u][points] *= 2
                    i[u][navn] += "_TD"
                    test = False
            poeng += i[u][points]

        if verdi > min_value and verdi <= max_value:
            lager.append([round(poeng)]+[float(verdi)]+i)

    lager.sort(reverse=True)
    print(len(lager))
    for i in range(10):
        print(lager[i])
