f = open("input.txt", "r")
orbits = {}
for line in f.readlines():
    a, b = line.strip().split(")")
    if b not in orbits:
        orbits[b] = set()
    orbits[b].add(a)
    if a not in orbits:
        orbits[a] = set()
rtot = 0
for papa in orbits.keys():
    while len(orbits[papa]) != 0:
        rtot += 1
        for e in orbits[papa]:
            papa = e
print(rtot)
# PART 2
you = {}
curr = "YOU"
i = 0
while len(orbits[curr]) != 0:
    for e in orbits[curr]:
        curr = e
        you[curr] = i
        i += 1
curr = "SAN"
i = 0
while len(orbits[curr]) != 0:
    for e in orbits[curr]:
        curr = e
        if e in you:
            print(i+you[e])
            exit(0)
        i += 1
