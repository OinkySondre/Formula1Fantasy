from itertools import combinations
import numpy as np
from decimal import *
getcontext().prec = 4

navn = 0
value = 1
points = 2

runder = 1
max_value = 100.2
min_value = 80

nonTurbo = ["Ham", "Ver", "Bot", "Mer", "Red", "McL", "Fer", "Ast", "Alp", "AlT", "Alf", "Will", "Has"]

constuctor = [
["Mer",38, 67],
["Red",25.9, 53],
["McL", 18.9, 39],
["Fer", 18.2, 26],
["Ast", 17.4, 18],
["Alp", 15.3, 13],
["AlT", 12.8, 13],
["Alf", 8.9, 12],
["Will", 6.3, 6],
["Has", 6.1, 7]
]

drivers = [
["Ham", 33.5, 45],
["Ver", 24.9, 35],
["Bot", 23.6, 32],
["Per", 18.4, 23],
["Ric", 17.2, 15],
["Lec", 17, 20],
["Vet", 16, 12],
["Alo", 15.5, -8],
["Sai", 14.4, 11],
["Str", 13.9, 11],
["Nor", 13.2, 29],
["Gas", 11.7, 2],
["Oco", 10, 11],
["Rai", 9.6, 12],
["Tsu", 8.9, 16],
["Glo", 7.9, 5],
["Lat", 6.5, 1],
["Rus", 6.2, 10],
["Msc", 5.8, 11],
["Maz", 5.5, -14]
]

lage = []
lager = []
liste = []
for i in range(len(drivers)):
    liste.append(i)

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
        for u in range(len(i)):
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
