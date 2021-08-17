from itertools import combinations
import numpy as np
from decimal import *
getcontext().prec = 4

navn = 0
value = 1
points = 2
megadriver = False

runder = 10
max_value = 103.2
min_value = 90

nonTurbo = ["Ham", "Ver", "Bot"]
nonMega = []

constuctor = [
    ["Mer", 37.1, 546],
    ["Red", 26.7, 573],
    ["McL", 18.6, 402],
    ["Fer", 18.7, 349],
    ["AsM", 16.4, 185],
    ["Alp", 15.1, 170],
    ["AlT", 12.7, 175],
    ["Alf", 9.2, 124],
    ["Will", 6.3, 74],
    ["Has", 6.1, 99]
]

drivers = [
    ["Ham", 33, 378],
    ["Ver", 25.7, 386],
    ["Bot", 23, 223],
    ["Per", 18.7, 249],
    ["Lec", 17.6, 205],
    ["Ric", 15.8, 157],
    ["Vet", 15.2, 110],
    ["Alo", 14.9, 131],
    ["Sai", 14.4, 176],
    ["Str", 13.3, 87],
    ["Nor", 14.2, 317],
    ["Gas", 11.9, 143],
    ["Oco", 10, 56],
    ["Rai", 9.3, 81],
    ["Tsu", 8.5, 59],
    ["Glo", 8.1, 75],
    ["Lat", 6.4, 31],
    ["Rus", 6.2, 47],
    ["Msc", 5.8, 89],
    ["Maz", 5.3, 42]
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

    for i in range(len(lage)):
        i = lage[i]
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
            i[u][points] = round(i[u][points],2)

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

        if verdi>min_value and verdi<=max_value:
            lager.append([round(poeng)]+[float(verdi)]+i)

    lager.sort(reverse=True)
    print(len(lager))
    for i in range(10):
        print(lager[i])
