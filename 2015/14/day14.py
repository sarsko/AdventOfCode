rests = {}
kilos = {}
durat = {}
positions = {}
points = {}

for e in open("input.txt").read().strip().split("\n"):
    name, can, fly, numkms, kms, fr, secs, seconds, but, then, must, rest, fr, restsecs, seconds = e.split()
    rests[name] = int(restsecs)
    kilos[name] = int(numkms)
    durat[name] = int(secs)
    positions[name] = []
    points[name] = 0

bst = 0
for k, v in kilos.items():
    curr = 0
    rem = durat[k]
    res = rests[k]
    for i in range(2503):
        if rem:
            rem -= 1
            curr += v
        else:
            if res:
                res -= 1
            if not res:
                rem = durat[k]
                res = rests[k]
        positions[k].append(curr)
    if curr > bst:
        bst = curr

print(bst)

for i in range(2503):
    bst = 0
    for k, _ in kilos.items():
        if positions[k][i] > bst:
            bst = positions[k][i]
    for k, _ in kilos.items():
        if positions[k][i] == bst:
            points[k] += 1

print(max(points.values()))
