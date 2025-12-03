import textwrap
p1 = 0
p2 = 0
for (l, r) in [map(int, l.split("-")) for l in open("input.txt").read().split(",")]:
    for e in range(l, r+1):
        s = str(e)
        if s[:len(s)//2] == s[len(s)//2:]:
            p1 += e
        for n in range(1, len(s)//2+1):
            if len(set(textwrap.wrap(s, n))) == 1:
                p2 += e
                break

print(p1)
print(p2)
