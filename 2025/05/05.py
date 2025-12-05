p1 = 0
p2 = 0
a = []
l, r = open("input.txt").read().split("\n\n")
for l in l.split():
    h, j = l.split("-")
    a.append((int(h), int(j)))
a.sort()
c = -1
for e in a:
    p2 += max(0, e[1] + 1 - max(e[0], c))
    c = max(c, e[1] + 1)

for l in map(int, r.split()):
    for e in a:
        if e[0] <= l and e[1] >= l:
            p1 += 1
            break
print(p1)
print(p2)
