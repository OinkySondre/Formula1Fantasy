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

constuctor = [
    ["Mer", 34.5, 20],
    ["Red", 32.5, 10],
    ["Fer", 25.0, 9],
    ["McL", 18.5, 8],
    ["AsM", 11.5, 7],
    ["Alp", 14.0, 6],
    ["AlT", 10.5, 5],
    ["Alf", 8.0, 4],
    ["Will", 7.0, 3],
    ["Has", 6.0, 2]
]

drivers = [
    ["Ham", 31.0, 20],
    ["Ver", 30.5, 19],
    ["Rus", 24, 18],
    ["Lec", 18.0, 17],
    ["Per", 17.5, 16],
    ["Sai", 17.0, 15],
    ["Lan", 16.0, 14],
    ["Ric", 14.5, 13],
    ["Gas", 13.5, 12],
    ["Alo", 12.5, 11],
    ["Oco", 12.0, 10],
    ["Vet", 11.5, 9],
    ["Str", 9.5, 8],
    ["Bot", 9.0, 7],
    ["Tsu", 8.5, 6],
    ["Zho", 8.0, 5],
    ["Alb", 7.5, 4],
    ["Lat", 7, 3],
    ["Msc", 6.5, 2],
    ["Mag", 5.5, 1]
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
