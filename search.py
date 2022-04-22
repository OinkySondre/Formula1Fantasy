from itertools import combinations
import numpy as np
from decimal import *
getcontext().prec = 4

navn = 0
value = 1
points = 2
megadriver = False

runder = 3
max_value = 103.3
min_value = 90

nonTurbo = ["Ham", "Ver", "Rus"]
nonMega = []
print("--------------------------------------------------------------------------------")


constuctor = [
    ["Mer", 33.9, 155],
    ["Red", 32.1, 105],
    ["Fer", 25.8, 183],
    ["McL", 17.5, 55],
    ["AsM", 11, 30],
    ["Alp", 14.1, 47],
    ["AlT", 10.2, 15],
    ["Alf", 8.4, 58],
    ["Will", 6.6, 22],
    ["Has", 6.7, 51]
]

drivers = [
    ["Ham", 30.4, 73],
    ["Ver", 30.3, 54],
    ["Rus", 23.9, 87],
    ["Lec", 18.8, 139],
    ["Per", 18.0, 61],
    ["Sai", 17.3, 54],
    ["Lan", 15.9, 47],
    ["Ric", 14, 23],
    ["Gas", 13.1, 27],
    ["Alo", 12.5, 1],
    ["Oco", 12.6, 61],
    ["Vet", 11.4, 12],
    ["Str", 9.0, 33],
    ["Bot", 9.4, 40],
    ["Tsu", 8.4, 3],
    ["Zho", 8.5, 33],
    ["Alb", 7.1, 28],
    ["Lat", 6.7, 9],
    ["Msc", 6.2, 19],
    ["Mag", 6.0, 47]
]

#--------------------------------------------------------------------------------
"""
poeng = [0,49,32,34,28,26,24,22,20,18,16,14,12,10,8,6,4,2,1]
drivers = [
    ["Ham", drivers[0][1], poeng[4]],
    ["Ver", drivers[1][1], poeng[2]],
    ["Rus", drivers[2][1], poeng[6]],
    ["Lec", drivers[3][1], poeng[1]],
    ["Per", drivers[4][1], poeng[5]],
    ["Sai", drivers[5][1], poeng[3]],
    ["Lan", drivers[6][1], poeng[8]],
    ["Ric", drivers[7][1], poeng[15]],
    ["Gas", drivers[8][1], poeng[13]],
    ["Alo", drivers[9][1], poeng[11]],
    ["Oco", drivers[10][1], poeng[9]],
    ["Vet", drivers[11][1], poeng[16]],
    ["Str", drivers[12][1], poeng[14]],
    ["Bot", drivers[13][1], poeng[7]],
    ["Tsu", drivers[14][1], poeng[10]],
    ["Zho", drivers[15][1], poeng[12]],
    ["Alb", drivers[16][1], poeng[14]],
    ["Lat", drivers[17][1], poeng[15]],
    ["Msc", drivers[18][1], poeng[13]],
    ["Mag", drivers[19][1], poeng[15]]
]
constuctor = [
    ["Mer", constuctor[0][1], drivers[0][2]+drivers[2][2]],
    ["Red", constuctor[1][1], drivers[1][2]+drivers[4][2]],
    ["Fer", constuctor[2][1], drivers[3][2]+drivers[5][2]],
    ["McL", constuctor[3][1], drivers[6][2]+drivers[7][2]],
    ["AsM", constuctor[4][1], drivers[11][2]+drivers[12][2]],
    ["Alp", constuctor[5][1], drivers[10][2]+drivers[9][2]],
    ["AlT", constuctor[6][1], drivers[14][2]+drivers[8][2]],
    ["Alf", constuctor[7][1], drivers[13][2]+drivers[15][2]],
    ["Will", constuctor[8][1], drivers[16][2]+drivers[17][2]],
    ["Has", constuctor[9][1], drivers[18][2]+drivers[19][2]],
]
"""

#--------------------------------------------------------------------------------





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
