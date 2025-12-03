p1 = 0
p2 = 0

for l in open("input.txt").read().split():
    f = max(l[:-1])
    s = max(l[l.index(f)+1:])
    p1 += int(f + s)

    tmp = ""
    index = 0
    for i in range(0, 12):
        sub = l[index:len(l) - 11 + i]
        n = max(sub)
        index += sub.index(n) + 1 
        tmp += n
    p2 += int(tmp)

print(p1)
print(p2)
