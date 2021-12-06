l = list(map(int, open("input.txt", "r").read().split(",")))

fishies = [0]*10
for e in l:
    fishies[e] += 1

def calcFishies(fishies):
    while True:
        for i, e in enumerate(fishies):
            if i == 0:
                fishies[9] = e
                fishies[7] += e
            else:
                fishies[i-1] = e
        fishies[9] = 0
        yield fishies

des = {80, 256}
for i, e in enumerate(calcFishies(fishies)):
    if i in des:
        print(sum(e))
        des.remove(i)
    if not des:
        break
