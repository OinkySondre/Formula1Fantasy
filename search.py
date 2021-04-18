from itertools import combinations
import numpy as np
from decimal import *
getcontext().prec = 4

navn = 0
value = 1
points = 2
megadriver = False

runder = 2
max_value = 100.6
min_value = 90

nonTurbo = ["Ham", "Ver", "Bot"]
nonMega = []

constuctor = [
["Mer",37.8, 103],
["Red",26, 97],
["McL", 18.7, 87],
["Fer", 18.7, 72],
["AsM", 16.8, 36],
["Alp", 15.1, 29],
["AlT", 13.2, 32],
["Alf", 8.9, 34],
["Will", 6.3, 10],
["Has", 6.1, 19]
]

drivers = [
["Ham", 33.4, 85],
["Ver", 25.1, 79],
["Bot", 23.5, 23],
["Per", 18.4, 28],
["Lec", 17.4, 48],
["Ric", 16.7, 34],
["Vet", 15.4, 13],
["Alo", 15.1, 3],
["Sai", 14.3, 34],
["Str", 13.6, 33],
["Nor", 13.4, 63],
["Gas", 11.7, 15],
["Oco", 9.7, 21],
["Rai", 9.4, 31],
["Tsu", 9.4, 22],
["Glo", 7.8, 13],
["Lat", 6.5, 12],
["Rus", 6.2, 1],
["Msc", 5.7, 22],
["Maz", 5.3, 8]
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
            lager.append([poeng]+i)

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
