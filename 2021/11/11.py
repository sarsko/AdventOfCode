f = open("input.txt").read().split("\n")
l = []
for e in f:
    if e :
        l.append(list(map(int, e)))

h=w=len(l)
def calcOcto(octos):
    flashes = 0
    cntr = 0
    while True:
        cntr += 1
        for i, e in enumerate(octos):
            for j, _ in enumerate(e):
                octos[i][j] += 1
        hasflashed = []
        for i, o in enumerate(octos):
            tmp = []
            for _ in o:
                tmp.append(False)
            hasflashed.append(tmp)
        stab = False
        while not stab:
            stab = True
            for i, o in enumerate(octos):
                for j, e in enumerate(o):
                    if e > 9 and not hasflashed[i][j]:
                        hasflashed[i][j] = True
                        stab = False
                        if j > 0:
                            try:
                                octos[i][j-1] += 1
                            except:
                                pass
                            try:
                                octos[i+1][j-1] += 1
                            except:
                                pass
                        try:
                            octos[i][j+1] += 1
                        except:
                            pass
                        if i  > 0:
                            try:
                                octos[i-1][j] += 1
                            except:
                                pass
                            try:
                                octos[i-1][j+1] += 1
                            except:
                                pass
                            if j > 0:
                                try:
                                    octos[i-1][j-1] += 1
                                except:
                                    pass
                        try:
                            octos[i+1][j+1] += 1
                        except:
                            pass
                        try:
                            octos[i+1][j] += 1
                        except:
                            pass
        for i, o in enumerate(octos):
            for j, e in enumerate(o):
                if e > 9:
                    flashes += 1
                    octos[i][j] = 0
        notnow = False
        for e in hasflashed:
            for j in e:
                if j == False:
                    notnow = True
        if not notnow:
            print(cntr)
            exit(0)
        yield flashes

des = {99, 999}
for i, e in enumerate(calcOcto(l)):
    if i in des:
        print(e)
        des.remove(i)
    if not des:
        break
