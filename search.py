from itertools import combinations
import numpy as np
from decimal import *
getcontext().prec = 4

navn = 0
value = 1
points = 2
megadriver = True

runder = 3
max_value = 101.7
min_value = 90

nonTurbo = ["Ham", "Ver", "Bot"]
nonMega = []

constuctor = [
    ["Mer", 37.6, 173],
    ["Red", 26.1, 152],
    ["McL", 18.8, 133],
    ["Fer", 19, 91],
    ["AsM", 16.6, 39],
    ["Alp", 15.1, 65],
    ["AlT", 13, 43],
    ["Alf", 8.9, 33],
    ["Will", 6.3, 10],
    ["Has", 6.1, 29]
]

drivers = [
    ["Ham", 33.3, 128],
    ["Ver", 25.3, 116],
    ["Bot", 23.3, 55],
    ["Per", 18.3, 51],
    ["Lec", 17.8, 70],
    ["Ric", 16.4, 48],
    ["Vet", 15.1, 17],
    ["Alo", 15, 23],
    ["Sai", 14.4, 36],
    ["Str", 13.6, 37],
    ["Nor", 13.7, 90],
    ["Gas", 11.7, 29],
    ["Oco", 9.9, 42],
    ["Rai", 9.4, 12],
    ["Tsu", 9.2, 24],
    ["Glo", 7.8, 21],
    ["Lat", 6.4, 10],
    ["Rus", 6.3, 2],
    ["Msc", 5.7, 33],
    ["Maz", 5.3, 4]
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
    print(lager[0])
    print(lager[1])
    print(lager[2])
    print(lager[3])
    print(lager[4])

if False:
    sjekken = ["videre"]
    def sjekk(arr,i):
        try:
            arr.index(i)
            return "stopp"
        except ValueError:
            return "videre"
    for i in range(1):
        unntak1 = []
        unntak2 = []
        unntak3 = []
        unntak4 = []
        for u in range(len(drivers)):
            lag = [u]
            for y in range(len(drivers)):
                try:
                    #Stopp hvis en ikke er error
                    sjekken.index(sjekk(unntak1, y))
                    sjekken.index(sjekk(lag, y))
                    lag = [u,y]
                    for t in range(len(drivers)):
                        try:
                            sjekken.index(sjekk(unntak1, t))
                            sjekken.index(sjekk(unntak2, t))
                            sjekken.index(sjekk(lag, t))
                            lag = [u,y,t]
                            for r in range(len(drivers)):
                                try:
                                    sjekken.index(sjekk(unntak1, r))
                                    sjekken.index(sjekk(unntak2, r))
                                    sjekken.index(sjekk(unntak3, r))
                                    sjekken.index(sjekk(lag, r))
                                    lag = [u,y,t,r]
                                    for e in range(len(drivers)):
                                        try:
                                            sjekken.index(sjekk(unntak1, e))
                                            sjekken.index(sjekk(unntak2, e))
                                            sjekken.index(sjekk(unntak3, e))
                                            sjekken.index(sjekk(unntak4, e))
                                            sjekken.index(sjekk(lag, e))
                                            lager.append([u,y,t,r,e])
                                        except ValueError:
                                            pass
                                    unntak4.append(r)
                                except ValueError:
                                    pass
                            unntak4 = []
                            unntak3.append(t)
                        except ValueError:
                            pass
                    unntak3 = []
                    unntak4 = []
                    unntak2.append(y)
                except ValueError:
                    pass
            unntak2 = []
            unntak3 = []
            unntak4 = []
            unntak1.append(u)
        unntak2 = []
        unntak3 = []
        unntak4 = []
        unntak1 = []
        print(len(lager))
